---
sidebarDepth: 1
---
# 触发器零件TriggerPart



## 概述

- 描述

    触发器零件，当实体进入时触发OnTriggerEntityEnter，当实体退出时触发OnTriggerEntityExit，当实体停留时触发OnTriggerEntityStay

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isTriggerEnter | bool | 是否监听实体进入，默认为True |
    | isTriggerExit | bool | 是否监听实体退出，默认为True |
    | isTriggerStay | bool | 是否监听实体进入，默认为False |
    | support | int | 支持客户端(1)/服务端(2)/双端(3)，默认为双端(3) |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetEntitiesInTrigger](#getentitiesintrigger) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前在触发器区域的实体列表 |




## GetEntitiesInTrigger

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Parts.TriggerPart.TriggerPart

- 描述

    获取当前在触发器区域的实体列表

- 参数

    无

- 返回值

    无



