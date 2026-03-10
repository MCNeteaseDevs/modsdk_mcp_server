---
sidebarDepth: 1
---
# 坐标变换Transform



## 概述

- 继承关系

```mermaid
classDiagram
GameObject <|-- Transform
link GameObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E6%B8%B8%E6%88%8F%E5%AF%B9%E8%B1%A1GameObject.html"
Transform: 坐标变换
GameObject: 游戏对象
GameObject: (点击跳转)
```

- 描述

    坐标变换，包含位置、旋转和缩放

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 位置变换 |
    | rotation | tuple(float,float,float) | 旋转变换 |
    | scale | tuple(float,float,float) |  缩放变换 |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddOffset](#addoffset) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给坐标变换位置增加偏移量 |
| [AddRotation](#addrotation) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给坐标变换旋转增加偏移量 |
| [AddScale](#addscale) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给坐标变换缩放增加偏移量 |
| [AddTransform](#addtransform) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给坐标变换增加偏移量 |
| [GetMatrix](#getmatrix) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取坐标变换矩阵 |




## AddOffset

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Transform.Transform

- 描述

    给坐标变换位置增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | offset | tuple(float,float,float) | 变换位置 |

- 返回值

    无



## AddRotation

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Transform.Transform

- 描述

    给坐标变换旋转增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rotation | tuple(float,float,float) | 变换旋转 |

- 返回值

    无



## AddScale

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Transform.Transform

- 描述

    给坐标变换缩放增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | scale | tuple(float,float,float) | 变换缩放 |

- 返回值

    无



## AddTransform

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Transform.Transform

- 描述

    给坐标变换增加偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | transform | Transform | 坐标变换 |

- 返回值

    无



## GetMatrix

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Transform.Transform

- 描述

    获取坐标变换矩阵

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | Matrix | 坐标变换矩阵 |



