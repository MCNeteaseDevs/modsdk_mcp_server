---
sidebarDepth: 1
---
# 文字面板预设TextboardPreset



## 概述

- 继承关系

```mermaid
classDiagram
PresetBase <|-- TextboardPreset
link PresetBase "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E9%A2%84%E8%AE%BE%E5%9F%BA%E7%B1%BBPresetBase.html"
TextboardObject <|-- TextboardPreset
link TextboardObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF%E5%AF%B9%E8%B1%A1TextboardObject.html"
SdkInterface <|-- PresetBase
link SdkInterface "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/SDK%E6%8E%A5%E5%8F%A3%E5%B0%81%E8%A3%85SdkInterface.html"
TransformObject <|-- PresetBase
link TransformObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E5%8F%98%E6%8D%A2%E5%AF%B9%E8%B1%A1TransformObject.html"
GameObject <|-- TransformObject
link GameObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E6%B8%B8%E6%88%8F%E5%AF%B9%E8%B1%A1GameObject.html"
TextboardPreset: 文字面板预设
TextboardObject: 文字面板对象
TextboardObject: (点击跳转)
PresetBase: 预设基类
PresetBase: (点击跳转)
GameObject: 游戏对象
GameObject: (点击跳转)
TransformObject: 变换对象
TransformObject: (点击跳转)
SdkInterface: SDK接口封装
SdkInterface: (点击跳转)
```

- 描述

    TextboardPreset（文字面板预设）与文字面板实体绑定，以面向对象的形式提供文字面板相关属性修改接口。

- 成员变量

    无



