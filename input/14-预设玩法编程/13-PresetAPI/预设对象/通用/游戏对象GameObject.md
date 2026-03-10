---
sidebarDepth: 1
---
# 游戏对象GameObject



## 概述

- 描述

    GameObject（游戏对象）是所有预设对象的基类，即API文档中Preset API - 预设对象下的所有类都继承自GameObject。

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | int | 对象ID |
    | classType | str | 对象类名 |
    | isClient | bool | 对象运行于客户端还是服务端 |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [LoadFile](#loadfile) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 加载指定路径的非python脚本文件内容，如配置文件 |
| [fromDict](#fromdict) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 将字典根据classType字段转换为对应类型的对象，该类型必须使用@registerGenericClass装饰 |




## LoadFile

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.GameObject.GameObject

- 描述

    加载指定路径的非python脚本文件内容，如配置文件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | path | str | 指定相对路径 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 文件内容 |



## fromDict

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.GameObject.type

- 描述

    将字典根据classType字段转换为对应类型的对象，该类型必须使用@registerGenericClass装饰

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | data | dict | 要转换的字典 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | GameObject或dict | 转换成功返回对象，否则返回字典本身 |



