---
sidebarDepth: 1
---
# 玩家预设PlayerPreset



## 概述

- 继承关系

```mermaid
classDiagram
EntityPreset <|-- PlayerPreset
link EntityPreset "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E5%AE%9E%E4%BD%93%E9%A2%84%E8%AE%BEEntityPreset.html"
PlayerObject <|-- PlayerPreset
link PlayerObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E7%8E%A9%E5%AE%B6%E5%AF%B9%E8%B1%A1PlayerObject.html"
PresetBase <|-- EntityPreset
link PresetBase "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E9%A2%84%E8%AE%BE%E5%9F%BA%E7%B1%BBPresetBase.html"
EntityObject <|-- EntityPreset
link EntityObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E5%AE%9E%E4%BD%93%E5%AF%B9%E8%B1%A1EntityObject.html"
TransformObject <|-- PresetBase
link TransformObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E5%8F%98%E6%8D%A2%E5%AF%B9%E8%B1%A1TransformObject.html"
SdkInterface <|-- PresetBase
link SdkInterface "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/SDK%E6%8E%A5%E5%8F%A3%E5%B0%81%E8%A3%85SdkInterface.html"
GameObject <|-- TransformObject
link GameObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E6%B8%B8%E6%88%8F%E5%AF%B9%E8%B1%A1GameObject.html"
PlayerPreset: 玩家预设
PlayerObject: 玩家对象
PlayerObject: (点击跳转)
EntityPreset: 实体预设
EntityPreset: (点击跳转)
GameObject: 游戏对象
GameObject: (点击跳转)
EntityObject: 实体对象
EntityObject: (点击跳转)
SdkInterface: SDK接口封装
SdkInterface: (点击跳转)
TransformObject: 变换对象
TransformObject: (点击跳转)
PresetBase: 预设基类
PresetBase: (点击跳转)
```

- 描述

    PlayerPreset（玩家预设）是一类特殊的实体预设，玩家预设与玩家实体进行绑定。每个AddOn（编辑器作品）只允许创建一个玩家预设。如果玩家同时启用了多个使用了玩家预设的AddOn，只会加载第一个玩家预设。

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 玩家ID |



