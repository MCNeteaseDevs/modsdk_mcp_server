---
sidebarDepth: 1
---
# 实体预设EntityPreset



## 概述

- 继承关系

```mermaid
classDiagram
PresetBase <|-- EntityPreset
link PresetBase "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E9%A2%84%E8%AE%BE%E5%9F%BA%E7%B1%BBPresetBase.html"
EntityObject <|-- EntityPreset
link EntityObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E5%AE%9E%E4%BD%93%E5%AF%B9%E8%B1%A1EntityObject.html"
SdkInterface <|-- PresetBase
link SdkInterface "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/SDK%E6%8E%A5%E5%8F%A3%E5%B0%81%E8%A3%85SdkInterface.html"
TransformObject <|-- PresetBase
link TransformObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E5%8F%98%E6%8D%A2%E5%AF%B9%E8%B1%A1TransformObject.html"
GameObject <|-- TransformObject
link GameObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E6%B8%B8%E6%88%8F%E5%AF%B9%E8%B1%A1GameObject.html"
EntityPreset: 实体预设
EntityObject: 实体对象
EntityObject: (点击跳转)
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

    EntityPreset（实体预设）是一类特殊的预设，实体预设通常会绑定MC的某类实体，实体预设实例与MC的某一个实体绑定，因此可以使用实体预设来进行一些实体相关的逻辑的编程。如果玩家同时启用了多个AddOn，且这些AddOn中均包含与同一种MC原版实体绑定的实体预设，那么只会加载第一个这种实体预设。

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | engineTypeStr | str | 实体的类型ID |
    | entityId | str | 实体ID |
    | updateTransformInterval | int | 实体预设子节点的变换更新间隔，0表示永不更新 |



