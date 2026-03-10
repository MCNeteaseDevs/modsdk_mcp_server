---
sidebarDepth: 1
---
# 零件PartBase



## 概述

- 继承关系

```mermaid
classDiagram
SdkInterface <|-- PartBase
link SdkInterface "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/SDK%E6%8E%A5%E5%8F%A3%E5%B0%81%E8%A3%85SdkInterface.html"
TransformObject <|-- PartBase
link TransformObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E5%8F%98%E6%8D%A2%E5%AF%B9%E8%B1%A1TransformObject.html"
GameObject <|-- TransformObject
link GameObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E6%B8%B8%E6%88%8F%E5%AF%B9%E8%B1%A1GameObject.html"
PartBase: 零件
SdkInterface: SDK接口封装
SdkInterface: (点击跳转)
TransformObject: 变换对象
TransformObject: (点击跳转)
GameObject: 游戏对象
GameObject: (点击跳转)
```

- 描述

    PartBase（零件基类）是可以与零件进行绑定，而零件可以挂接在预设下，以实现带逻辑的预设的组装。所有的自定义零件都需要继承PartBase，预设系统下的大部分代码都需要写在自定义零件中。注意，自定义零件只有挂接到预设，并且在游戏中实例化才能生效。

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | tickEnable | str | 是否启用零件tick |
    | replicated | list | 启用网络复制的字段列表 |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [InitClient](#initclient) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端的零件对象初始化入口 |
| [InitServer](#initserver) | <span style="display:inline;color:#ff5555">服务端</span> | 服务端的零件对象初始化入口 |
| [TickClient](#tickclient) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端的零件对象逻辑驱动入口 |
| [TickServer](#tickserver) | <span style="display:inline;color:#ff5555">服务端</span> | 服务端的零件对象逻辑驱动入口 |
| [UnloadClient](#unloadclient) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端的零件对象卸载逻辑入口 |
| [UnloadServer](#unloadserver) | <span style="display:inline;color:#ff5555">服务端</span> | 服务端的零件对象卸载逻辑入口 |
| [DestroyClient](#destroyclient) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端的零件对象销毁逻辑入口 |
| [DestroyServer](#destroyserver) | <span style="display:inline;color:#ff5555">服务端</span> | 服务端的零件对象销毁逻辑入口 |
| [CanAdd](#canadd) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 判断零件是否可以挂接到指定的父节点上 |
| [GetTickCount](#gettickcount) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前帧数 |
| [LogDebug](#logdebug) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 打印msg % args调试日志，仅PC开发包有效 |
| [LogInfo](#loginfo) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 打印msg % args消息日志 |
| [LogError](#logerror) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 打印msg % args错误日志 |
| [GetGameObjectById](#getgameobjectbyid) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取指定对象ID的游戏对象 |
| [GetGameObjectByEntityId](#getgameobjectbyentityid) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取指定实体ID的游戏对象 |
| [GetLoadedPlayers](#getloadedplayers) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取服务器所有玩家的ID列表 |
| [GetPlayerObject](#getplayerobject) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取玩家对象 |
| [GetEntityObject](#getentityobject) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取实体对象 |
| [GetEffectObject](#geteffectobject) | <span style="display:inline;color:#7575f9">客户端</span> | 获取特效对象 |
| [CreateEffectPreset](#createeffectpreset) | <span style="display:inline;color:#7575f9">客户端</span> | 创建特效对象 |
| [CreateTextboardPreset](#createtextboardpreset) | <span style="display:inline;color:#7575f9">客户端</span> | 创建文字面板预设对象 |
| [ListenForEvent](#listenforevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 监听指定的事件 |
| [UnListenForEvent](#unlistenforevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 反监听指定的事件 |
| [ListenForEngineEvent](#listenforengineevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 监听指定的引擎事件 |
| [UnListenForEngineEvent](#unlistenforengineevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 反监听指定的引擎事件 |
| [CreateEventData](#createeventdata) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建自定义事件的数据，eventData用于发送事件。创建的eventData可以理解为一个dict，可以嵌套赋值dict,list和基本数据类型，但不支持tuple |
| [BroadcastEvent](#broadcastevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 广播事件，双端通用 |
| [BroadcastPresetSystemEvent](#broadcastpresetsystemevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 广播给预设系统 |
| [NotifyToServer](#notifytoserver) | <span style="display:inline;color:#7575f9">客户端</span> | 通知服务端触发事件 |
| [NotifyToClient](#notifytoclient) | <span style="display:inline;color:#ff5555">服务端</span> | 通知指定客户端触发事件 |
| [BroadcastToAllClient](#broadcasttoallclient) | <span style="display:inline;color:#ff5555">服务端</span> | 通知指所有客户端触发事件 |
| [ListenSelfEvent](#listenselfevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 监听来自自己的事件 |
| [UnListenSelfEvent](#unlistenselfevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 反监听来自自己的事件 |
| [ListenPartEvent](#listenpartevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 监听来自指定零件的事件 |
| [UnListenPartEvent](#unlistenpartevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 反监听来自指定零件的事件 |
| [ListenPresetSystemEvent](#listenpresetsystemevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 监听来自预设系统的事件 |
| [UnListenPresetSystemEvent](#unlistenpresetsystemevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 反监听来自预设系统的事件 |
| [DestroyStoryLines](#destroystorylines) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 手动销毁零件蓝图 |
| [GetSelf](#getself) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取零件自身 |
| [GetApi](#getapi) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 返回当前对象可使用的SDK API模块 |
| [IsPlayerSneaking](#isplayersneaking) | <span style="display:inline;color:#ff5555">服务端</span> | 是否潜行 |
| [GetPlayerHunger](#getplayerhunger) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家饥饿度，展示在UI饥饿度进度条上，初始值为20，即每一个鸡腿代表2个饥饿度。 **饱和度(saturation)** ：玩家当前饱和度，初始值为5，最大值始终为玩家当前饥饿度(hunger)，该值直接影响玩家**饥饿度(hunger)**。<br>1）增加方法：吃食物。<br>2）减少方法：每触发一次**消耗事件**，该值减少1，如果该值不大于0，直接把玩家 **饥饿度(hunger)** 减少1。 |
| [SetPlayerHunger](#setplayerhunger) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家饥饿度。 |




## InitClient

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    客户端的零件对象初始化入口

- 参数

    无

- 返回值

    无



## InitServer

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    服务端的零件对象初始化入口

- 参数

    无

- 返回值

    无



## TickClient

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    客户端的零件对象逻辑驱动入口

- 参数

    无

- 返回值

    无



## TickServer

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    服务端的零件对象逻辑驱动入口

- 参数

    无

- 返回值

    无



## UnloadClient

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    客户端的零件对象卸载逻辑入口

- 参数

    无

- 返回值

    无



## UnloadServer

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    服务端的零件对象卸载逻辑入口

- 参数

    无

- 返回值

    无



## DestroyClient

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    客户端的零件对象销毁逻辑入口

- 参数

    无

- 返回值

    无



## DestroyServer

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    服务端的零件对象销毁逻辑入口

- 参数

    无

- 返回值

    无



## CanAdd

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    判断零件是否可以挂接到指定的父节点上

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | parent | PresetBase | 即将挂接的父预设 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 不允许挂接时，返回对应的错误提示 |



## GetTickCount

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    获取当前帧数

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 当前帧数 |



## LogDebug

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    打印msg % args调试日志，仅PC开发包有效

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | msg | str | 要打印的格式化字符串 |
    | *args | list(object) | 格式化参数列表 |

- 返回值

    无

- 示例

```python
self.LogDebug(“self.isClient: %s”, self.isClient)
```



## LogInfo

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    打印msg % args消息日志

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | msg | str | 要打印的格式化字符串 |
    | *args | list(object) | 格式化参数列表 |

- 返回值

    无

- 示例

```python
self.LogInfo(“self.isClient: %s”, self.isClient)
```



## LogError

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    打印msg % args错误日志

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | msg | str | 要打印的格式化字符串 |
    | *args | list(object) | 格式化参数列表 |

- 返回值

    无

- 示例

```python
self.LogError(“self.isClient: %s”, self.isClient)
```



## GetGameObjectById

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    获取指定对象ID的游戏对象

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | int | 指定的对象ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | TransformObject | 成功返回游戏对象，失败返回None |

- 示例

```python
obj = self.GetGameObjectById(0)
```



## GetGameObjectByEntityId

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    获取指定实体ID的游戏对象

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 指定的实体ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | TransformObject | 成功返回游戏对象，失败返回None |

- 示例

```python
obj = self.GetGameObjectByEntityId(0)
```



## GetLoadedPlayers

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    获取服务器所有玩家的ID列表

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 所有玩家的ID列表 |



## GetPlayerObject

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    获取玩家对象

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PlayerObject | 成功返回玩家对象，失败返回None |

- 示例

```python
player = self.GetPlayerObject(playerId)
```



## GetEntityObject

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    获取实体对象

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 指定的实体ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EntityObject | 成功返回实体对象，失败返回None |

- 示例

```python
entity = self.GetEntityObject(entityId)
```



## GetEffectObject

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    获取特效对象

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | effectId | int | 特效ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EffectObject | 成功返回特效对象，失败返回None |

- 示例

```python
effect = self.GetEffectObject(effectId)
```



## CreateEffectPreset

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    创建特效对象

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | resource | str | 特效资源json |
    | pos | tuple(float,float,float) | 特效位置 |
    | rotation | tuple(float,float,float) | 特效旋转 |
    | scale | tuple(float,float,float) | 特效缩放 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EffectPreset | 成功返回特效对象，失败返回None |

- 示例

```python
# 在某个实体位置播放指定特效
effect = self.CreateEffectPreset("effects/xxx", self.GetEntityPos(entityId))
```



## CreateTextboardPreset

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    创建文字面板预设对象

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | text | str | 文字显示内容 |
    | textColor | tuple(float,float,float,float) | 文字颜色的RGBA值，范围0-1 |
    | boardColor | tuple(float,float,float,float) | 可选参数，默认None，设置为黑色，面板颜色的RGBA值，范围0-1 |
    | pos | tuple(float,float,float) | 可选参数，默认(0, 0, 0) 生成文字面板位置 |
    | faceCamera | bool | 是否始终朝向相机, 默认为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | TextboardPreset | 成功返回文字面板对象，失败返回None |

- 示例

```python
# 在某个位置生成文字面板预设
textboard = self.CreateTextboardPreset('Hello', (0.5, 0.4, 0.3, 0.8))
```



## ListenForEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    监听指定的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | namespace | str | 命名空间 |
    | systemName | str | 事件系统名称 |
    | eventName | str | 事件名称 |
    | instance | object | 实例 |
    | func | object | 函数 |
    | priority | str | 优先级 |

- 返回值

    无



## UnListenForEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    反监听指定的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | namespace | str | 命名空间 |
    | systemName | str | 事件系统名称 |
    | eventName | str | 事件名称 |
    | instance | object | 实例 |
    | func | object | 函数 |
    | priority | str | 优先级 |

- 返回值

    无



## ListenForEngineEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    监听指定的引擎事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名称 |
    | instance | object | 实例 |
    | func | object | 函数 |
    | priority | str | 优先级 |

- 返回值

    无



## UnListenForEngineEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    反监听指定的引擎事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名称 |
    | instance | object | 实例 |
    | func | object | 函数 |
    | priority | str | 优先级 |

- 返回值

    无



## CreateEventData

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    创建自定义事件的数据，eventData用于发送事件。创建的eventData可以理解为一个dict，可以嵌套赋值dict,list和基本数据类型，但不支持tuple

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 事件数据 |



## BroadcastEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    广播事件，双端通用

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名称 |
    | eventData | object | 事件数据 |

- 返回值

    无



## BroadcastPresetSystemEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    广播给预设系统

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名称 |
    | eventData | object | 事件数据 |

- 返回值

    无



## NotifyToServer

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    通知服务端触发事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名称 |
    | eventData | object | 事件数据 |

- 返回值

    无



## NotifyToClient

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    通知指定客户端触发事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家ID |
    | eventName | str | 事件名称 |
    | eventData | object | 事件数据 |

- 返回值

    无



## BroadcastToAllClient

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    通知指所有客户端触发事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名称 |
    | eventData | object | 事件数据 |

- 返回值

    无



## ListenSelfEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    监听来自自己的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名称 |
    | target | object | 目标 |
    | func | object | 回调函数 |

- 返回值

    无



## UnListenSelfEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    反监听来自自己的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名称 |
    | target | object | 目标 |
    | func | object | 回调函数 |

- 返回值

    无



## ListenPartEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    监听来自指定零件的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | partId | int | 指定零件的ID |
    | eventName | str | 事件名称 |
    | target | object | 目标 |
    | func | object | 回调函数 |

- 返回值

    无



## UnListenPartEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    反监听来自指定零件的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | partId | int | 指定零件的ID |
    | eventName | str | 事件名称 |
    | target | object | 目标 |
    | func | object | 回调函数 |

- 返回值

    无



## ListenPresetSystemEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    监听来自预设系统的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名称 |
    | target | object | 目标 |
    | func | object | 回调函数 |

- 返回值

    无



## UnListenPresetSystemEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    反监听来自预设系统的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名称 |
    | target | object | 目标 |
    | func | object | 回调函数 |

- 返回值

    无



## DestroyStoryLines

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    手动销毁零件蓝图

- 参数

    无

- 返回值

    无



## GetSelf

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.PartBase.PartBase

- 描述

    获取零件自身

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PartBase | 零件自身 |



## GetApi

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    返回当前对象可使用的SDK API模块

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | extraClientApi或extraServerApi | 返回当前对象可使用的SDK API模块 |



## IsPlayerSneaking

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    是否潜行

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否潜行 |

- 示例

```python
self.IsPlayerSneaking(playerId)
```



## GetPlayerHunger

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取玩家饥饿度，展示在UI饥饿度进度条上，初始值为20，即每一个鸡腿代表2个饥饿度。 **饱和度(saturation)** ：玩家当前饱和度，初始值为5，最大值始终为玩家当前饥饿度(hunger)，该值直接影响玩家**饥饿度(hunger)**。<br>1）增加方法：吃食物。<br>2）减少方法：每触发一次**消耗事件**，该值减少1，如果该值不大于0，直接把玩家 **饥饿度(hunger)** 减少1。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 玩家饥饿度 |

- 示例

```python
self.GetPlayerHunger(playerId)
```



## SetPlayerHunger

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置玩家饥饿度。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |
    | value | float | 饥饿度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetPlayerHunger(playerId, 10)
```



