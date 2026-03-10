---
sidebarDepth: 1
---
# 变换对象TransformObject



## 概述

- 继承关系

```mermaid
classDiagram
GameObject <|-- TransformObject
link GameObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E6%B8%B8%E6%88%8F%E5%AF%B9%E8%B1%A1GameObject.html"
TransformObject: 变换对象
GameObject: 游戏对象
GameObject: (点击跳转)
```

- 描述

    TransformObject（变换对象）是拥有变换属性的GameObject（游戏对象）的基类，他们在游戏世界中有着确切的位置等信息。

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 对象名称 |
    | transform | Transform | 局部坐标变换 |
    | dimension | Transform | 所在维度ID |
    | isBroken | bool | 是否可用，当素材文件丢失，零件代码语法错误时处于不可用状态 |
    | isRemoved | bool | 是否已销毁 |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetDimension](#getdimension) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取所在的维度 |
| [SetDimension](#setdimension) | <span style="display:inline;color:#ff5555">服务端</span> | 设置所在的维度 |
| [GetChildTransformObjects](#getchildtransformobjects) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取子TransformObject列表 |
| [GetTransformObjects](#gettransformobjects) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取TransformObject列表，包含自身 |
| [GetChildGameObjects](#getchildgameobjects) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取子GameObject列表 |
| [GetGameObjects](#getgameobjects) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取GameObject列表，包含自身 |
| [GetGameObjectById](#getgameobjectbyid) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 根据ID获取GameObject |
| [GetGameObjectByEntityId](#getgameobjectbyentityid) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 根据实体ID获取GameObject |
| [GetId](#getid) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的ID |
| [GetEntityId](#getentityid) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的实体ID |
| [GetDisplayName](#getdisplayname) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的显示名称 |
| [GetDisplayPath](#getdisplaypath) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设到根节点的显示路径 |
| [GetLocalTransform](#getlocaltransform) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的局部坐标变换 |
| [SetLocalTransform](#setlocaltransform) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置当前预设的局部坐标变换 |
| [GetLocalPosition](#getlocalposition) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的局部坐标位置 |
| [SetLocalPosition](#setlocalposition) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置当前预设的局部坐标位置 |
| [GetLocalRotation](#getlocalrotation) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的局部坐标旋转 |
| [SetLocalRotation](#setlocalrotation) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置当前预设的局部坐标旋转 |
| [GetLocalScale](#getlocalscale) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的局部坐标缩放 |
| [SetLocalScale](#setlocalscale) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置当前预设的局部坐标缩放 |
| [GetWorldTransform](#getworldtransform) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的世界坐标变换 |
| [GetWorldMatrix](#getworldmatrix) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取世界坐标变换矩阵 |
| [GetLocalMatrix](#getlocalmatrix) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取局部坐标变换矩阵 |
| [SetWorldTransform](#setworldtransform) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置当前预设的世界坐标变换 |
| [GetWorldPosition](#getworldposition) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的世界坐标位置 |
| [SetWorldPosition](#setworldposition) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置当前预设的世界坐标位置 |
| [GetWorldRotation](#getworldrotation) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的世界坐标旋转 |
| [SetWorldRotation](#setworldrotation) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置当前预设的世界坐标旋转 |
| [GetWorldScale](#getworldscale) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的世界坐标缩放 |
| [SetWorldScale](#setworldscale) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置当前预设的世界坐标缩放 |
| [AddLocalOffset](#addlocaloffset) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给局部坐标变换位置增加偏移量 |
| [AddWorldOffset](#addworldoffset) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给世界坐标变换位置增加偏移量 |
| [AddLocalRotation](#addlocalrotation) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给局部坐标变换旋转增加偏移量 |
| [AddWorldRotation](#addworldrotation) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给世界坐标变换旋转增加偏移量 |
| [AddLocalScale](#addlocalscale) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给局部坐标变换缩放增加偏移量 |
| [AddWorldScale](#addworldscale) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给世界坐标变换缩放增加偏移量 |
| [AddLocalTransform](#addlocaltransform) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给局部坐标变换增加偏移量 |
| [AddWorldTransform](#addworldtransform) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给世界坐标变换增加偏移量 |
| [GetRootParent](#getrootparent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设所在的根预设 |
| [GetParent](#getparent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设的父预设 |
| [SetParent](#setparent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置当前预设的父预设 |
| [GetManager](#getmanager) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前预设所在的预设管理器 |
| [Unload](#unload) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 卸载当前预设 |
| [Destroy](#destroy) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 销毁当前预设 |




## GetDimension

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取所在的维度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 维度ID |



## SetDimension

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    设置所在的维度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 目标维度ID |
    | pos | tuple(int,int,int) | 传送的坐标，默认为空，非空时会更新该对象的世界坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否真正变更了维度，如果目标维度与对象维度一致，会返回False |



## GetChildTransformObjects

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取子TransformObject列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | recursive | bool | 是否递归查找所有子节点 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(TransformObject) | TransformObject列表 |



## GetTransformObjects

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取TransformObject列表，包含自身

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | recursive | bool | 是否递归查找所有子节点 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(TransformObject) | TransformObject列表 |



## GetChildGameObjects

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取子GameObject列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | recursive | bool | 是否递归查找所有子节点 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(GameObject) | 游戏对象列表 |



## GetGameObjects

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取GameObject列表，包含自身

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | recursive | bool | 是否递归查找所有子节点 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(GameObject) | 游戏对象列表 |



## GetGameObjectById

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    根据ID获取GameObject

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | GameObject | 游戏对象 |



## GetGameObjectByEntityId

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    根据实体ID获取GameObject

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | GameObject | 游戏对象 |



## GetId

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的ID

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | ID |



## GetEntityId

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的实体ID

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 实体ID |



## GetDisplayName

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的显示名称

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 名称 |



## GetDisplayPath

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设到根节点的显示路径

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 节点路径 |



## GetLocalTransform

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的局部坐标变换

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | Transform | 坐标变换 |



## SetLocalTransform

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    设置当前预设的局部坐标变换

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | transform | Transform | 坐标变换 |

- 返回值

    无



## GetLocalPosition

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的局部坐标位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | （X轴位置，Y轴位置，Z轴位置） |



## SetLocalPosition

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    设置当前预设的局部坐标位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | （X轴位置，Y轴位置，Z轴位置） |

- 返回值

    无



## GetLocalRotation

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的局部坐标旋转

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | （X轴角度，Y轴角度，Z轴角度） |



## SetLocalRotation

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    设置当前预设的局部坐标旋转

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rotation | tuple(float,float,float) | （X轴角度，Y轴角度，Z轴角度） |

- 返回值

    无



## GetLocalScale

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的局部坐标缩放

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | （X轴缩放，Y轴缩放，Z轴缩放） |



## SetLocalScale

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    设置当前预设的局部坐标缩放

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | scale | tuple(float,float,float) | （X轴缩放，Y轴缩放，Z轴缩放） |

- 返回值

    无



## GetWorldTransform

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的世界坐标变换

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | Transform | 坐标变换 |



## GetWorldMatrix

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取世界坐标变换矩阵

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | Matrix | 世界坐标变换矩阵 |



## GetLocalMatrix

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取局部坐标变换矩阵

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | Matrix | 局部坐标变换矩阵 |



## SetWorldTransform

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    设置当前预设的世界坐标变换

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | transform | Transform | 坐标变换 |

- 返回值

    无



## GetWorldPosition

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的世界坐标位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | （X轴位置，Y轴位置，Z轴位置） |



## SetWorldPosition

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    设置当前预设的世界坐标位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | （X轴位置，Y轴位置，Z轴位置） |

- 返回值

    无



## GetWorldRotation

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的世界坐标旋转

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | （X轴角度，Y轴角度，Z轴角度） |



## SetWorldRotation

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    设置当前预设的世界坐标旋转

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rotation | tuple(float,float,float) | （X轴角度，Y轴角度，Z轴角度） |

- 返回值

    无



## GetWorldScale

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的世界坐标缩放

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | （X轴缩放，Y轴缩放，Z轴缩放） |



## SetWorldScale

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    设置当前预设的世界坐标缩放

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | scale | tuple(float,float,float) | （X轴缩放，Y轴缩放，Z轴缩放） |

- 返回值

    无



## AddLocalOffset

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    给局部坐标变换位置增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | offset | tuple(float,float,float) | 变换位置 |

- 返回值

    无



## AddWorldOffset

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    给世界坐标变换位置增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | offset | tuple(float,float,float) | 变换位置 |

- 返回值

    无



## AddLocalRotation

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    给局部坐标变换旋转增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rotation | tuple(float,float,float) | 变换旋转 |

- 返回值

    无



## AddWorldRotation

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    给世界坐标变换旋转增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rotation | tuple(float,float,float) | 变换旋转 |

- 返回值

    无



## AddLocalScale

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    给局部坐标变换缩放增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | scale | tuple(float,float,float) | 变换缩放 |

- 返回值

    无



## AddWorldScale

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    给世界坐标变换缩放增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | scale | tuple(float,float,float) | 变换缩放 |

- 返回值

    无



## AddLocalTransform

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    给局部坐标变换增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | transform | Transform | 坐标变换 |

- 返回值

    无



## AddWorldTransform

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    给世界坐标变换增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | transform | Transform | 坐标变换 |

- 返回值

    无



## GetRootParent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设所在的根预设

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PresetBase | 预设 |



## GetParent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设的父预设

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PresetBase | 预设 |



## SetParent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    设置当前预设的父预设

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | parent | PresetBase | 预设 |

- 返回值

    无



## GetManager

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    获取当前预设所在的预设管理器

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PresetManager | 预设管理 |



## Unload

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    卸载当前预设

- 参数

    无

- 返回值

    无



## Destroy

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.TransformObject.TransformObject

- 描述

    销毁当前预设

- 参数

    无

- 返回值

    无



