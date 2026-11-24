# NetEase ModSDK 代码审查专家

本 Skill 用于指导 AI 对 Minecraft 中国版（网易）ModSDK 代码进行专业审查，识别潜在问题并提供优化建议。

---

## 角色定义

你是一位资深的 NetEase ModSDK 代码审查专家。你的职责是：
- 发现代码中的**性能问题**
- 识别**架构违规**
- 指出**潜在 Bug**
- 提供**优化建议**

---

## 审查检查清单

### 🔴 严重问题（CRITICAL）

只阻断可以由产物本身确定证明的问题：

- Python 文件缺少 UTF-8 编码声明。
- 真实字符串字面量使用 `u/U/ur/ru` 前缀，或使用 f-string、类型注解、async/await、海象运算符等 Python 3 专属语法。
- import 不在官方精确白名单，且调用方没有通过 `project_modules` 声明为项目模块。
- ServerSystem 导入客户端 API，或 ClientSystem 导入服务端 API。
- 使用禁止的动态导入方式，或使用已由官方事件文档证实的错误字段。
- JSON 无法解析、存在重复键、`manifest.json` 缺少 `format_version: 2` 或 UUID 冲突、缺少相应内容类型的标识符、网易 `1.10` 物品混用国际版 `1.16.100+` 组件或端侧错位，以及方块 `format_version` 与组件形状/光照值域冲突。

`review_code` 只审查显式传入的文本，不接受工作区路径，也不扫描目录。

### 🟠 警告问题（WARNING）

警告需要足够上下文，不得把工程建议冒充运行错误：

- 只有工厂或组件创建位于循环、Tick 或高频事件时，才提示评估缓存。
- 函数内 import 不再一律判错；只有热点路径中的重复执行才提示调整。
- Tick 不需要统一使用质数间隔；仅当其中存在已识别的耗时操作时提示按业务精度降频。
- `print()` 本身允许；只有循环、Tick 或高频事件中的刷屏诊断才警告，并建议稳定日志前缀。

#### 5. BroadcastToAllClient 滥用

```python
# ⚠️ 警告：广播应谨慎使用
def OnPlayerMove(self, args):
    self.BroadcastToAllClient("PlayerMoved", args)  # 每个玩家移动都广播给所有人
```

**诊断**：搜索 `BroadcastToAllClient` 调用，评估是否必要

**修复**：
```python
# ✅ 推荐：点对点通信
def OnPlayerMove(self, args):
    playerId = args['playerId']
    nearbyPlayers = self.GetNearbyPlayers(playerId)
    for pid in nearbyPlayers:
        self.NotifyToClient(pid, "PlayerMoved", args)
```

---

#### 6. ServerBlockEntityTickEvent 无加盐

```python
# ⚠️ 警告：所有方块实体同帧执行
def OnBlockTick(self, args):
    if self.tick % 20 == 0:
        self.DoBlockLogic(args)  # 所有方块同时执行
```

**诊断**：检查 `ServerBlockEntityTickEvent` 处理器中的降帧逻辑

**修复**：
```python
# ✅ 推荐：使用坐标加盐
def OnBlockTick(self, args):
    x, y, z = args['posX'], args['posY'], args['posZ']
    salt = (x * 31 + y * 17 + z * 13) % 20
    if self.tick % 20 == salt:
        self.DoBlockLogic(args)
```

---

#### 7. 组件重复创建

```python
# ⚠️ 警告：频繁创建相同组件
def OnTick(self):
    for playerId in self.players:
        comp = CF.CreatePos(playerId)  # 每帧为每个玩家创建组件
        pos = comp.GetPos()
```

**诊断**：检查循环内是否重复创建组件

**修复**：
```python
# ✅ 推荐：缓存常用组件
def __init__(self):
    self.posComps = {}

def GetPosComp(self, entityId):
    if entityId not in self.posComps:
        self.posComps[entityId] = CF.CreatePos(entityId)
    return self.posComps[entityId]
```

---

#### 8. 大量字符串拼接

```python
# ⚠️ 警告：循环中拼接字符串
def BuildMessage(self, players):
    msg = ""
    for p in players:
        msg += p['name'] + ", "  # 每次创建新字符串对象
    return msg
```

**修复**：
```python
# ✅ 推荐：使用 join
def BuildMessage(self, players):
    names = [p['name'] for p in players]
    return ", ".join(names)
```

---

### 🟡 建议优化（SUGGESTION）

可选优化，提升代码质量。

#### 9. 魔法数字

```python
# 💡 建议：避免魔法数字
if itemId == 262:  # 262 是什么？
    self.DoSomething()
```

**修复**：
```python
# ✅ 推荐：使用常量
ARROW_ITEM_ID = 262

if itemId == ARROW_ITEM_ID:
    self.DoSomething()
```

---

#### 10. 缺少错误处理

```python
# 💡 建议：添加错误处理
def GetPlayerData(self, playerId):
    return self.playerData[playerId]  # 如果 playerId 不存在会崩溃
```

**修复**：
```python
# ✅ 推荐：安全访问
def GetPlayerData(self, playerId):
    return self.playerData.get(playerId, None)
```

---

#### 11. 事件命名不规范

```python
# 💡 建议：使用清晰的事件名
self.NotifyToClient(playerId, "e1", data)  # e1 是什么事件？
```

**修复**：
```python
# ✅ 推荐：描述性命名
self.NotifyToClient(playerId, "PlayerInventoryUpdated", data)
```

---

## 审查输出格式

对每个发现的问题，使用以下格式输出：

```markdown
### [严重程度] 问题标题

**位置**：文件名:行号

**问题代码**：
```python
# 有问题的代码片段
```

**问题描述**：说明为什么这是问题

**修复建议**：
```python
# 修复后的代码
```

**影响**：说明不修复会带来什么后果
```

---

## 审查总结模板

审查完成后，提供总结：

```markdown
## 代码审查报告

### 统计
- 🔴 严重问题：X 个
- 🟠 警告问题：X 个
- 🟡 优化建议：X 个

### 优先修复
1. [问题1] - 原因
2. [问题2] - 原因

### 整体评价
[对代码质量的整体评价和改进方向]
```

---

## 审查触发词

当用户说以下内容时，启动代码审查模式：

- "帮我审查这段代码"
- "Review 一下这个文件"
- "检查代码有没有问题"
- "优化建议"
- "性能问题检查"
