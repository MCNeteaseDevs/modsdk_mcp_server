---
sidebarDepth: 1
---
# 界面预设UIPreset



## 概述

- 继承关系

```mermaid
classDiagram
PresetBase <|-- UIPreset
link PresetBase "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E9%A2%84%E8%AE%BE%E5%9F%BA%E7%B1%BBPresetBase.html"
TransformObject <|-- PresetBase
link TransformObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E5%8F%98%E6%8D%A2%E5%AF%B9%E8%B1%A1TransformObject.html"
SdkInterface <|-- PresetBase
link SdkInterface "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/SDK%E6%8E%A5%E5%8F%A3%E5%B0%81%E8%A3%85SdkInterface.html"
GameObject <|-- TransformObject
link GameObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/%E6%B8%B8%E6%88%8F%E5%AF%B9%E8%B1%A1GameObject.html"
UIPreset: 界面预设
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

    UIPreset（界面预设）是一类绑定界面资源的预设。

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | uiNodeScreen | str | UI画布路径，为"UI文件名.UI画布名"的字符串形式 |
    | uiNodeModulePath | str | 继承自ScreenNode的UI逻辑文件模块路径 |
    | uiNodeModule | str | 继承自ScreenNode的UI逻辑文件类名 |
    | uiName | str | UI名称，需保证在单个addon中唯一 |
    | autoCreate | bool | 在界面预设创建完成后是否自动创建UI |
    | isHud | bool | 该界面是否屏蔽游戏操作 |
    | createUIMethod | str | 创建界面接口 |
    | isBindParent | bool | 是否绑定父预设，仅当父预设为实体预设时生效 |
    | bindParentOffset | tuple | 当绑定父预设时生效，修改与绑定实体之间的偏移量 |
    | bindParentAutoScale | bool | 当绑定父预设时生效，设置已绑定实体的UI是否根据绑定实体与本地玩家间的距离动态缩放 |
    | showInEditor | bool | 是否在预设编辑器中创建UI |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [SetUiActive](#setuiactive) | <span style="display:inline;color:#7575f9">客户端</span> | 设置UI激活 |
| [GetUiActive](#getuiactive) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前UI是否激活 |
| [SetUiVisible](#setuivisible) | <span style="display:inline;color:#7575f9">客户端</span> | 设置UI显隐 |
| [GetUiVisible](#getuivisible) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前UI是否显示 |
| [GetScreenNode](#getscreennode) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前ScreenNode实例 |




## SetUiActive

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.UI.UIPreset.UIPreset

- 描述

    设置UI激活

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | active | bool | 是否激活 |

- 返回值

    无



## GetUiActive

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.UI.UIPreset.UIPreset

- 描述

    获取当前UI是否激活

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | UI是否激活 |



## SetUiVisible

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.UI.UIPreset.UIPreset

- 描述

    设置UI显隐

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | visible | bool | 是否显示 |

- 返回值

    无



## GetUiVisible

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.UI.UIPreset.UIPreset

- 描述

    获取当前UI是否显示

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | UI是否显示 |



## GetScreenNode

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.UI.UIPreset.UIPreset

- 描述

    获取当前ScreenNode实例

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ScreenNode | 当前ScreenNode实例 |



