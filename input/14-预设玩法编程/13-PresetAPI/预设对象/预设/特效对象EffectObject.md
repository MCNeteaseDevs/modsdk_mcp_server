---
sidebarDepth: 1
---
# 特效对象EffectObject



## 概述

- 继承关系

```mermaid
classDiagram
SdkInterface <|-- EffectObject
link SdkInterface "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/SDK%E6%8E%A5%E5%8F%A3%E5%B0%81%E8%A3%85SdkInterface.html"
EffectObject: 特效对象
SdkInterface: SDK接口封装
SdkInterface: (点击跳转)
```

- 描述

    EffectObject（特效对象）是对特效对象封装的基类，它为特效提供了面向对象的使用方式。

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | effectId | int | 关联特效ID |
    | effectType | str | 关联特效类型，frame/particle |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [Play](#play) | <span style="display:inline;color:#7575f9">客户端</span> | 播放特效，仅客户端有效 |
| [Stop](#stop) | <span style="display:inline;color:#7575f9">客户端</span> | 停止播放特效，仅客户端有效 |
| [BindToEntity](#bindtoentity) | <span style="display:inline;color:#7575f9">客户端</span> | 绑定到实体 |
| [BindToSkeleton](#bindtoskeleton) | <span style="display:inline;color:#7575f9">客户端</span> | 绑定骨骼模型 |
| [SetLoop](#setloop) | <span style="display:inline;color:#7575f9">客户端</span> | 设置特效是否循环播放，默认为否，仅对序列帧有效 |
| [SetDeepTest](#setdeeptest) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧是否透视，默认为否 |
| [SetFaceCamera](#setfacecamera) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧是否始终朝向摄像机，默认为是 |




## Play

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Effect.EffectObject.EffectObject

- 描述

    播放特效，仅客户端有效

- 参数

    无

- 返回值

    无



## Stop

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Effect.EffectObject.EffectObject

- 描述

    停止播放特效，仅客户端有效

- 参数

    无

- 返回值

    无



## BindToEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Effect.EffectObject.EffectObject

- 描述

    绑定到实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | bindEntityId | str | 绑定的实体ID |
    | offset | tuple(float,float,float) | 绑定的偏移量 |
    | rot | tuple(float,float,float) | 绑定的旋转角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.BindToEntity(entityId, (0, 1, 0), (0, 0, 0))
```



## BindToSkeleton

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Effect.EffectObject.EffectObject

- 描述

    绑定骨骼模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | modelId | int | 绑定的骨骼模型的ID（见model组件的GetModelId） |
    | boneName | str | 绑定具体骨骼的名称 |
    | offset | tuple(float,float,float) | 绑定的偏移量 |
    | rot | tuple(float,float,float) | 绑定的旋转角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.BindToSkeleton(modelId, "root", (0, 1, 0), (0, 0, 0))
```



## SetLoop

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Effect.EffectObject.EffectObject

- 描述

    设置特效是否循环播放，默认为否，仅对序列帧有效

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | loop | bool | True表示循环播放 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 设置为循环播放
self.SetLoop(True)
```



## SetDeepTest

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Effect.EffectObject.EffectObject

- 描述

    设置序列帧是否透视，默认为否

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | deepTest | bool | False表示透视，则被物体/方块阻挡时仍然能看到序列帧 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 设置为透视
self.SetDeepTest(False)
```



## SetFaceCamera

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Effect.EffectObject.EffectObject

- 描述

    设置序列帧是否始终朝向摄像机，默认为是

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | face | bool | True表示朝摄像机 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 设置为不始终朝摄像机
self.SetFaceCamera(False)
```



