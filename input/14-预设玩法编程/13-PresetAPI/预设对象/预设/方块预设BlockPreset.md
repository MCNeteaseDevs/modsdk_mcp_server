---
sidebarDepth: 1
---
# 方块预设BlockPreset



## 概述

- 继承关系

```mermaid
classDiagram
PresetBase <|-- BlockPreset
link PresetBase "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E9%A2%84%E8%AE%BE%E5%9F%BA%E7%B1%BBPresetBase.html"
SdkInterface <|-- PresetBase
link SdkInterface "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/SDK%E6%8E%A5%E5%8F%A3%E5%B0%81%E8%A3%85SdkInterface.html"
TransformObject <|-- PresetBase
link TransformObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E5%8F%98%E6%8D%A2%E5%AF%B9%E8%B1%A1TransformObject.html"
GameObject <|-- TransformObject
link GameObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E6%B8%B8%E6%88%8F%E5%AF%B9%E8%B1%A1GameObject.html"
BlockPreset: 方块预设
SdkInterface: SDK接口封装
SdkInterface: (点击跳转)
PresetBase: 预设基类
PresetBase: (点击跳转)
TransformObject: 变换对象
TransformObject: (点击跳转)
GameObject: 游戏对象
GameObject: (点击跳转)
```

- 描述

    BlockPreset（方块预设）是一类绑定方块的预设。由于MC的方块数量巨大，将方块预设与MC的原生方块绑定，尤其是地图中常见的原生方块可能对性能造成重大影响。

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | engineTypeStr | str | 方块类型ID |
    | blockId | str | 方块类型数字ID |
    | auxValue | int | 附加值 |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetEngineTypeStr](#getenginetypestr) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取方块预设的方块类型ID |




## GetEngineTypeStr

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Block.BlockPreset.BlockPreset

- 描述

    获取方块预设的方块类型ID

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 方块类型ID |



