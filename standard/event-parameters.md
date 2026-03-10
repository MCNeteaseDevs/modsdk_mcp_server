# ModSDK 事件参数参考手册

## ⚠️ 重要提醒

**不同事件的参数名称不一致！使用前必须查阅此文档或调用 search_event 工具。**

---

## 服务端事件参数对照表

### 玩家相关事件

| 事件名 | 玩家 ID | 取消参数 | 其他重要参数 |
|--------|---------|----------|--------------|
| `AddServerPlayerEvent` | `id` | - | `isTransfer`, `isPeUser` |
| `DelServerPlayerEvent` | `id` | - | `isTransfer` |
| `ServerPlayerTryDestroyBlockEvent` | `playerId` | `cancel` | `x`, `y`, `z`, `face`, `fullName` |
| `PlayerAttackEntityEvent` | `playerId` | `cancel` | `victimId`, `damage` |
| `PlayerDieEvent` | `id` | - | `attacker` |
| `PlayerRespawnEvent` | `playerId` | - | - |

### 物品相关事件

| 事件名 | 玩家/实体 ID | 取消参数 | 其他重要参数 |
|--------|-------------|----------|--------------|
| `ServerItemUseOnEvent` | `entityId` ⚠️ | `ret` ⚠️ | `itemDict`, `x`, `y`, `z`, `face` |
| `ServerItemUseEvent` | `playerId` | `cancel` | `itemDict` |
| `ActorAcquiredItemServerEvent` | `playerId` | - | `itemDict`, `acquireMethod` |
| `PlayerDropItemServerEvent` | `playerId` | `cancel` | `itemDict` |
| `InventoryItemChangedServerEvent` | `playerId` | - | `slot`, `oldItemDict`, `newItemDict` |

### 方块相关事件

| 事件名 | 实体 ID | 取消参数 | 其他重要参数 |
|--------|---------|----------|--------------|
| `ServerEntityTryPlaceBlockEvent` | `entityId` | `cancel` | `x`, `y`, `z`, `fullName` |
| `ServerBlockUseEvent` | `playerId` | `cancel` | `x`, `y`, `z`, `blockName` |
| `BlockDestroyedByPlayerEvent` | `playerId` | - | `x`, `y`, `z`, `fullName` |
| `BlockNeighborChangedServerEvent` | - | - | `posX`, `posY`, `posZ` |

### 实体相关事件

| 事件名 | 实体 ID | 取消参数 | 其他重要参数 |
|--------|---------|----------|--------------|
| `EntityHurtEvent` | `entityId` | `cancel` | `srcId`, `damage`, `cause` |
| `EntityDeathEvent` | `id` | - | `attacker` |
| `MobSpawnEvent` | `entityId` | `cancel` | `identifier`, `posX`, `posY`, `posZ` |
| `ProjectileHitEntityServerEvent` | `entityId` | - | `targetId`, `hitX`, `hitY`, `hitZ` |

---

## 客户端事件参数对照表

### UI 相关事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `UiInitFinished` | - | UI 初始化完成 |
| `OnKeyPressInGame` | `key`, `isDown` | 按键事件 |
| `OnMousePressInGame` | `button`, `isDown` | 鼠标事件 |

### 物品相关事件

| 事件名 | 玩家 ID | 取消参数 | 其他重要参数 |
|--------|---------|----------|--------------|
| `ClientItemUseOnEvent` | `playerId` | `ret` ⚠️ | `itemDict`, `x`, `y`, `z` |

---

## 常见错误示例

### ❌ 错误：假设所有事件都用 playerId

```python
def on_item_use_on(self, args):
    player_id = args.get("playerId")  # ❌ 错误！
```

### ✅ 正确：查阅文档使用 entityId

```python
def on_item_use_on(self, args):
    player_id = args.get("entityId")  # ✅ 正确
```

### ❌ 错误：假设所有事件都用 cancel

```python
def on_item_use_on(self, args):
    args["cancel"] = True  # ❌ 错误！
```

### ✅ 正确：ServerItemUseOnEvent 使用 ret

```python
def on_item_use_on(self, args):
    args["ret"] = True  # ✅ 正确
```

---

## 如何查询事件参数

### 方法 1：使用 MCP 工具

```
search_event("ServerItemUseOnEvent")
```

### 方法 2：查看 QuServerApi/Events.py

在 `input/` 目录下的示例项目中，`QuModLibs/QuServerApi/Events.py` 文件包含所有事件的参数定义。

### 方法 3：查看官方文档

使用 `search_docs` 工具搜索事件名称。
