---
sidebarDepth: 1
---
# 实体零件EntityBasePart



## 概述

- 描述

    实体零件

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | engineType | str | 实体类型 |
    | autoCreate | bool | 是否在零件初始化时，自动创建关联实体，默认为True |
    | persistence | bool | 创建的实体是否持久化，默认为False，设为True时，创建完实体会将autoCreate重置为False |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CreateVirtualEntity](#createvirtualentity) | <span style="display:inline;color:#ff5555">服务端</span> | 手动创建关联实体，如果已创建会直接返回 |
| [DestroyVirtualEntity](#destroyvirtualentity) | <span style="display:inline;color:#ff5555">服务端</span> | 移除已创建的关联实体，引擎退出时会默认调用 |




## CreateVirtualEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Parts.EntityBasePart.EntityBasePart

- 描述

    手动创建关联实体，如果已创建会直接返回

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 返回创建的实体ID |



## DestroyVirtualEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Parts.EntityBasePart.EntityBasePart

- 描述

    移除已创建的关联实体，引擎退出时会默认调用

- 参数

    无

- 返回值

    无



