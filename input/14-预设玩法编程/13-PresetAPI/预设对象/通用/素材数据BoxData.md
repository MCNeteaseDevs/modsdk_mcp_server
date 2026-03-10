---
sidebarDepth: 1
---
# 素材数据BoxData



## 概述

- 继承关系

```mermaid
classDiagram
TransformObject <|-- BoxData
link TransformObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E5%8F%98%E6%8D%A2%E5%AF%B9%E8%B1%A1TransformObject.html"
GameObject <|-- TransformObject
link GameObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E6%B8%B8%E6%88%8F%E5%AF%B9%E8%B1%A1GameObject.html"
BoxData: 素材数据
GameObject: 游戏对象
GameObject: (点击跳转)
TransformObject: 变换对象
TransformObject: (点击跳转)
```

- 描述

    BoxData（素材数据）与素材类似，可以挂接在预设下使用。BoxData在编辑器中不会实际生成，可以重叠放置。

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | filePath | str | 素材相对于BoxData目录的相对路径 |



