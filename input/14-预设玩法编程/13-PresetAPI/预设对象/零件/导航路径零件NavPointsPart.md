---
sidebarDepth: 1
---
# 导航路径零件NavPointsPart



## 概述

- 描述

    导航路径零件, 在编辑器内可以选定一系列相对于该零件的坐标点，当零件运行时可以获得这些坐标点的世界坐标列表

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | patrolsPath | list(tuple(float,float,float)) | 路径点列表 |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetNavigationPoints](#getnavigationpoints) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获得路径点的世界坐标列表 |
| [GetNavigationRadius](#getnavigationradius) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获得路径点的随机半径列表 |




## GetNavigationPoints

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Parts.NavPointsPart.NavPointsPart

- 描述

    获得路径点的世界坐标列表

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(tuple(float,float,float)) | 路径点的世界坐标列表 |



## GetNavigationRadius

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Parts.NavPointsPart.NavPointsPart

- 描述

    获得路径点的随机半径列表

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(float) | 路径点的随机半径列表 |



