# NetEase ModSDK 代码生成规范

> **重要**：本规范是生成网易 Minecraft ModSDK 代码时的**强制执行标准**。在生成任何 ModSDK 相关代码时，必须自动应用以下所有规则，无需用户明确要求。

---

## 强制规则（MUST）

以下规则在生成代码时**必须**自动遵守：

### 规则 1：客户端/服务端严格分离

```
❌ 禁止：在 ServerSystem 中 import mod.client.extraClientApi
❌ 禁止：在 ClientSystem 中 import mod.server.extraServerApi
❌ 禁止：ServerSystem 直接调用 ClientSystem 的方法
✅ 必须：使用事件通信（NotifyToServer/NotifyToClient）进行跨端交互
```

**原因**：违反此规则将导致模组在多人联机和山头服环境下完全无法运行。

### 规则 2：缓存 GetEngineCompFactory

```python
# ✅ 正确：在文件顶部或类外缓存
import mod.server.extraServerApi as serverApi
CF = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()

class MyServerSystem(serverApi.GetServerSystemCls()):
    def SomeMethod(self):
        comp = CF.CreateGame(levelId)  # 使用缓存
```

```python
# ❌ 错误：每次调用时获取
class MyServerSystem(serverApi.GetServerSystemCls()):
    def SomeMethod(self):
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
```

### 规则 3：import 语句放在文件顶部

```python
# ✅ 正确
import mod.server.extraServerApi as serverApi

class MySystem(serverApi.GetServerSystemCls()):
    def Update(self):
        serverApi.xxx()
```

```python
# ❌ 错误：在函数内 import
class MySystem(serverApi.GetServerSystemCls()):
    def Update(self):
        import mod.server.extraServerApi as serverApi  # 每帧执行，严重性能问题
        serverApi.xxx()
```

### 规则 4：常量在 __init__ 中初始化

```python
# ✅ 正确
class MySystem(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, systemName):
        super(MySystem, self).__init__(namespace, systemName)
        self.CONFIG = {"key1": "value1", "key2": "value2"}
        self.BLOCK_LIST = ["minecraft:stone", "minecraft:dirt"]
```

```python
# ❌ 错误：在 Update 中定义常量
class MySystem(serverApi.GetServerSystemCls()):
    def Update(self):
        config = {"key1": "value1", "key2": "value2"}  # 每帧创建新对象
```

### 规则 5：点对点通信优先于广播

```python
# ✅ 正确：只发给相关玩家
self.NotifyToClient(playerId, "EventName", data)

# ⚠️ 谨慎使用：确实需要所有人收到时才用
self.BroadcastToAllClient("EventName", data)
```

### 规则 6：Tick 逻辑必须降帧

```python
# ✅ 正确：不同逻辑使用不同频率（使用质数避免同时触发）
class MySystem(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, systemName):
        super(MySystem, self).__init__(namespace, systemName)
        self.tick = 0
    
    def Update(self):
        self.tick += 1
        
        # 关键逻辑：每帧（仅限真正必要的逻辑）
        self.handleCritical()
        
        # 常规逻辑：每 5 帧
        if self.tick % 5 == 0:
            self.handleNormal()
        
        # 低频逻辑：每 19 帧（质数）
        if self.tick % 19 == 0:
            self.handleLowPriority()
```

### 规则 7：大批量操作必须分帧

```python
# ✅ 正确：分帧处理
class MySystem(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, systemName):
        super(MySystem, self).__init__(namespace, systemName)
        self.pendingBlocks = []
        self.blockIndex = 0
    
    def SetManyBlocks(self, positions):
        self.pendingBlocks = positions
        self.blockIndex = 0
    
    def Update(self):
        if self.pendingBlocks:
            # 每帧处理 5 个方块
            for _ in range(min(5, len(self.pendingBlocks) - self.blockIndex)):
                if self.blockIndex < len(self.pendingBlocks):
                    pos = self.pendingBlocks[self.blockIndex]
                    CF.CreateBlockInfo(levelId).SetBlockNew(pos, {'name': 'minecraft:air'})
                    self.blockIndex += 1
            
            if self.blockIndex >= len(self.pendingBlocks):
                self.pendingBlocks = []
```

```python
# ❌ 错误：一次性处理所有方块
def SetManyBlocks(self, positions):
    for pos in positions:  # 可能有上万个，直接卡死
        CF.CreateBlockInfo(levelId).SetBlockNew(pos, {'name': 'minecraft:air'})
```

### 规则 8：ServerBlockEntityTickEvent 必须使用负载均衡

```python
# ✅ 正确：使用坐标加盐分散执行时机
TICK_COUNT = 0

def OnScriptTickServer(self):
    global TICK_COUNT
    TICK_COUNT += 1

def OnBlockEntityTick(self, args):
    blockName = args["blockName"]
    x, y, z = args["posX"], args["posY"], args["posZ"]
    dimId = args["dimension"]
    
    if blockName == "custom:my_machine":
        # 使用坐标作为偏移量，避免所有机器同时执行
        offsetTick = x + y + z + dimId + TICK_COUNT
        if offsetTick % 20 == 0:
            self.processMachine(args)
```

### 规则 9：使用 dict 跳转代替多个 elif

```python
# ✅ 正确
class MySystem(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, systemName):
        super(MySystem, self).__init__(namespace, systemName)
        self.handlers = {
            "minecraft:iron_ore": self.handleIron,
            "minecraft:gold_ore": self.handleGold,
            "minecraft:diamond_ore": self.handleDiamond,
        }
    
    def OnBlockEvent(self, blockId):
        handler = self.handlers.get(blockId)
        if handler:
            handler()
```

```python
# ❌ 错误：大量 elif
def OnBlockEvent(self, blockId):
    if blockId == "minecraft:iron_ore":
        self.handleIron()
    elif blockId == "minecraft:gold_ore":
        self.handleGold()
    elif blockId == "minecraft:diamond_ore":
        self.handleDiamond()
    # ... 更多分支
```

### 规则 10：使用 in 判断字典 key

```python
# ✅ 正确
if key in myDict:
    value = myDict[key]

# ❌ 错误
if myDict.has_key(key):  # has_key 更慢
    value = myDict[key]
```

---

## 推荐规则（SHOULD）

以下规则是最佳实践，应尽可能遵循：

### 推荐 1：使用 Attr 同步代替 Tick 通信

当需要在服务端和客户端之间同步状态时：

```python
# ✅ 推荐：使用 Attr 自动同步
# 服务端
def OnPlayerAction(self, args):
    modAttr = CF.CreateModAttr(args["playerId"])
    modAttr.SetAttr("isFlying", 1)  # 自动同步到客户端

# 客户端
def __init__(self, namespace, systemName):
    super().__init__(namespace, systemName)
    modAttr = clientApi.GetEngineCompFactory().CreateModAttr(clientApi.GetLocalPlayerId())
    modAttr.RegisterUpdateFunc("isFlying", self.OnFlyingChanged)

def OnFlyingChanged(self, args):
    # 自动在属性变化时触发
    pass
```

### 推荐 2：使用推导式

```python
# ✅ 推荐
filtered = [item for item in items if item.isValid()]
mapping = {k: v for k, v in pairs if v > 0}

# ⚠️ 较慢
filtered = []
for item in items:
    if item.isValid():
        filtered.append(item)
```

### 推荐 3：字符串拼接策略

```python
# 少量字符串（≤3个）：直接相加
result = s1 + s2 + s3

# 大量字符串：使用 join
result = ''.join([s1, s2, s3, s4, s5, s6])

# ❌ 不要用于纯拼接
result = '%s%s%s' % (s1, s2, s3)  # 较慢
result = '{}{}{}'.format(s1, s2, s3)  # 最慢
```

### 推荐 4：缓存频繁访问的属性

```python
# ✅ 推荐：在循环前缓存
createExplosion = CF.CreateExplosion(levelId).CreateExplosion
for pos in positions:
    createExplosion(pos, ...)

# ❌ 较慢：每次都访问属性链
for pos in positions:
    CF.CreateExplosion(levelId).CreateExplosion(pos, ...)
```

---

## Shader 生成规则

生成 GLSL/HLSL 着色器代码时：

### Shader 规则 1：使用 step() 代替 if else

```glsl
// ✅ 正确
float result = 0.4 + step(0.5, r) * 0.2;

// ❌ 错误
float result;
if (r >= 0.5) {
    result = 0.6;
} else {
    result = 0.4;
}
```

### Shader 规则 2：循环变量必须初始化

```glsl
// ✅ 正确
for (int i = 0; i < 5; i++) { ... }

// ❌ 错误：某些设备上 i 可能是随机值
for (int i; i < 5; i++) { ... }
```

### Shader 规则 3：支持精美贴图开关

```glsl
void main() {
#ifdef FANCY
    // 高配逻辑
    renderBeautiful();
#else
    // 低配逻辑
    renderSimple();
#endif
}
```

### Shader 规则 4：合理使用精度修饰符

```glsl
// 小范围值用低精度
lowp float color;      // 0-1 范围
mediump int index;     // 0-1024 范围
highp float position;  // 需要高精度的值
```

---

## 资源配置规则

生成 JSON 配置文件时：

### 资源规则 1：不常用资源设置动态加载

```json
// netease_models.json
{
    "rare_boss": {
        "skeleton": "skeleton/boss.json",
        "dy_load": true
    }
}

// sound_definitions.json
{
    "dy_load_list": [
        "sounds/rare_event/thunder"
    ]
}
```

### 资源规则 2：粒子数量控制

```json
// 粒子特效数量应控制在 100 左右
{
    "particleeffect": {
        "emissionrate": {
            "max": "100.0",
            "min": "80.0"
        }
    }
}
```

---

## 模型规范

涉及玩家模型时：

1. **非必要不修改** Blockbench 模型
2. 如需修改，保留全部 **26 个必要骨骼**
3. 使用 SDK 接口判断是否需要替换模型：
   - `IsOfficialSkin()` - 是否官方皮肤
   - `IsHighLevelOfficialSkin()` - 是否史诗及以上
   - `IsHighLevelMultiJointOfficialSkin()` - 是否史诗及以上多关节

---

## 代码模板

### 标准 ServerSystem 模板

```python
# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

# 全局缓存
CF = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()

class MyServerSystem(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, systemName):
        super(MyServerSystem, self).__init__(namespace, systemName)
        self.tick = 0
        
        # 常量在此初始化
        self.CONFIG = {}
        
        # 注册事件监听
        self.ListenForEvent(
            serverApi.GetEngineNamespace(),
            serverApi.GetEngineSystemName(),
            "ServerChatEvent",
            self,
            self.OnServerChat
        )
    
    def Destroy(self):
        # 反注册事件
        self.UnListenAllEvents()
    
    def Update(self):
        self.tick += 1
        
        # 低频逻辑示例
        if self.tick % 19 == 0:
            self.doPeriodicCheck()
    
    def OnServerChat(self, args):
        playerId = args["playerId"]
        # 点对点通信
        self.NotifyToClient(playerId, "ChatReceived", {"msg": args["message"]})
    
    def doPeriodicCheck(self):
        pass
```

### 标准 ClientSystem 模板

```python
# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi

# 全局缓存
CF = clientApi.GetEngineCompFactory()
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()

class MyClientSystem(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, systemName):
        super(MyClientSystem, self).__init__(namespace, systemName)
        self.tick = 0
        
        # 注册事件监听
        self.ListenForEvent(
            clientApi.GetEngineNamespace(),
            clientApi.GetEngineSystemName(),
            "UiInitFinished",
            self,
            self.OnUiInitFinished
        )
    
    def Destroy(self):
        self.UnListenAllEvents()
    
    def Update(self):
        self.tick += 1
    
    def OnUiInitFinished(self, args):
        pass
```
