---
sidebarDepth: 1
---
# 特效预设EffectPreset



## 概述

- 继承关系

```mermaid
classDiagram
PresetBase <|-- EffectPreset
link PresetBase "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E9%A2%84%E8%AE%BE%E5%9F%BA%E7%B1%BBPresetBase.html"
EffectObject <|-- EffectPreset
link EffectObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E7%89%B9%E6%95%88%E5%AF%B9%E8%B1%A1EffectObject.html"
SdkInterface <|-- PresetBase
link SdkInterface "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/SDK%E6%8E%A5%E5%8F%A3%E5%B0%81%E8%A3%85SdkInterface.html"
TransformObject <|-- PresetBase
link TransformObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E5%8F%98%E6%8D%A2%E5%AF%B9%E8%B1%A1TransformObject.html"
GameObject <|-- TransformObject
link GameObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E6%B8%B8%E6%88%8F%E5%AF%B9%E8%B1%A1GameObject.html"
EffectPreset: 特效预设
SdkInterface: SDK接口封装
SdkInterface: (点击跳转)
PresetBase: 预设基类
PresetBase: (点击跳转)
TransformObject: 变换对象
TransformObject: (点击跳转)
EffectObject: 特效对象
EffectObject: (点击跳转)
GameObject: 游戏对象
GameObject: (点击跳转)
```

- 描述

    EffectPreset（特效预设）是一类绑定特效资源的预设。

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | resource | str | 特效json的相对路径，不含后缀.json |
    | effectType | str | 特效类型，frame/particle |
    | effectId | int | 特效ID |
    | auto | bool | 是否自动播放 |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetResource](#getresource) | <span style="display:inline;color:#7575f9">客户端</span> | 获取绑定的json资源 |
| [SetResource](#setresource) | <span style="display:inline;color:#7575f9">客户端</span> | 设置绑定的json资源 |




## GetResource

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Effect.EffectPreset.EffectPreset

- 描述

    获取绑定的json资源

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | json资源相对路径，不含.json后缀 |



## SetResource

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Effect.EffectPreset.EffectPreset

- 描述

    设置绑定的json资源

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | resource | str | json资源相对路径，不含.json后缀 |

- 返回值

    无



