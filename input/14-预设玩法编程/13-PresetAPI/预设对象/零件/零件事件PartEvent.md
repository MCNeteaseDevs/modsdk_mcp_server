---
sidebarDepth: 1
---
# 零件事件PartEvent

## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [OnTriggerEntityEnter](#ontriggerentityenter) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 触发器范围有实体进入时触发，只适用于TriggerPart |
| [OnTriggerEntityExit](#ontriggerentityexit) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 触发器范围有实体离开时触发，只适用于TriggerPart |
| [OnTriggerEntityStay](#ontriggerentitystay) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 触发器范围有实体停留时触发，只适用于TriggerPart |




## OnTriggerEntityEnter

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Parts.PartEvent

- 描述

    触发器范围有实体进入时触发，只适用于TriggerPart

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | TriggerPart | PartBase | 发射事件的触发器零件 |
    | EnterEntityIds | list(str) | 进入触发器范围的实体ID列表 |

- 返回值

    无

- 示例

```python
part = self.GetParent().GetPartByType("TriggerPart")
if not part:
    return
self.ListenPartClientEvent(part.id, "OnTriggerEntityEnter", self, self.OnTriggerEntityEnter)
```



## OnTriggerEntityExit

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Parts.PartEvent

- 描述

    触发器范围有实体离开时触发，只适用于TriggerPart

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | TriggerPart | PartBase | 发射事件的触发器零件 |
    | ExitEntityIds | list(str) | 离开触发器范围的实体ID列表 |

- 返回值

    无

- 示例

```python
part = self.GetParent().GetPartByType("TriggerPart")
if not part:
    return
self.ListenPartClientEvent(part.id, "OnTriggerEntityExit", self, self.OnTriggerEntityExit)
```



## OnTriggerEntityStay

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Parts.PartEvent

- 描述

    触发器范围有实体停留时触发，只适用于TriggerPart

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | TriggerPart | PartBase | 发射事件的触发器零件 |
    | StayEntityIds | list(str) | 停留在触发器范围的实体ID列表 |

- 返回值

    无

- 示例

```python
part = self.GetParent().GetPartByType("TriggerPart")
if not part:
    return
self.ListenPartClientEvent(part.id, "OnTriggerEntityStay", self, self.OnTriggerEntityStay)
```



