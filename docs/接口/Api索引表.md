---
sidebarDepth: 1
---
# API索引表

---

## 通用

- [Component](#component)
- [System](#system)
- [事件](#事件)
- [本地设备](#本地设备)
- [本地存储](#本地存储)
- [数学](#数学)
- [工具](#工具)
- [调试](#调试)
## 世界

- [地图](#地图)
- [实体管理](#实体管理)
- [方块管理](#方块管理)
- [生物生成](#生物生成)
- [配方](#配方)
- [方块组合](#方块组合)
- [渲染](#渲染)
- [时间](#时间)
- [天气](#天气)
- [游戏规则](#游戏规则)
- [自定义数据](#自定义数据)
- [指令](#指令)
- [消息](#消息)
- [记分板](#记分板)
- [行为](#行为)
## 实体

- [实体类型](#实体类型)
- [附加值](#附加值)
- [属性](#属性)
- [行为](#行为1)
- [状态效果](#状态效果)
- [渲染](#渲染1)
- [背包](#背包)
- [自定义属性](#自定义属性)
- [自定义数据](#自定义数据1)
- [molang](#molang)
- [标签](#标签)
- [抛射物](#抛射物)
- [经验球](#经验球)
- [官方伙伴](#官方伙伴)
- [官方聊天扩展](#官方聊天扩展)
- [魔法指令](#魔法指令)
## 玩家

- [属性](#属性1)
- [行为](#行为2)
- [渲染](#渲染2)
- [背包](#背包1)
- [摄像机](#摄像机)
- [动画](#动画)
- [游戏模式](#游戏模式)
- [权限](#权限)
- [导航](#导航)
## 方块

- [方块状态与附加值](#方块状态与附加值)
- [属性](#属性2)
- [方块实体](#方块实体)
- [方块几何体模型](#方块几何体模型)
- [方块调色板](#方块调色板)
- [渲染](#渲染3)
- [容器](#容器)
- [红石](#红石)
- [告示牌](#告示牌)
- [床](#床)
## 物品

- [物品](#物品-2)
## 特效

- [通用](#通用1)
- [文字面板](#文字面板)
- [序列帧](#序列帧)
- [粒子](#粒子)
- [模型特效](#模型特效)
- [微软粒子](#微软粒子)
## 模型

- [模型](#模型-2)
## 山头服务器

- [山头服务器](#山头服务器-2)

## 原生UI

- [原生UI](#原生ui-2)
## 自定义UI

- [通用](#通用2)
- [自定义书本](#自定义书本)
- [自定义成就系统](#自定义成就系统)
- [UI界面](#ui界面)
- [UI控件](#ui控件)
## 音效

- [音效](#音效-2)
## 控制

- [控制](#控制-2)
## 游戏设置

- [游戏设置](#游戏设置-2)
## 虚拟世界

- [世界](#世界1)
- [相机](#相机)
- [模型](#模型1)
- [其它对象](#其它对象)
## 后处理

- [渐晕](#渐晕)
- [模糊](#模糊)
- [色彩](#色彩)
- [镜头效果](#镜头效果)
- [自定义](#自定义)
## 联机大厅

- [联机大厅](#联机大厅-2)
## 成就

- [成就](#成就-2)
## 商城

- [商城](#商城-2)
## 渲染

- [渲染](#渲染-2)

#### Component
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CreateComponent](通用/Component.md#createcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 给实体创建服务端组件 |
| [CreateComponent](通用/Component.md#createcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 给实体创建客户端组件 |
| [DestroyComponent](通用/Component.md#destroycomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 删除实体的服务端组件 |
| [DestroyComponent](通用/Component.md#destroycomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 删除实体的客户端组件 |
| [GetComponent](通用/Component.md#getcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的服务端组件。一般用来判断某个组件是否创建过，其他情况请使用CreateComponent |
| [GetComponent](通用/Component.md#getcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体的客户端组件。一般用来判断某个组件是否创建过，其他情况请使用CreateComponent |
| [GetComponentCls](通用/Component.md#getcomponentcls) | <span style="display:inline;color:#ff5555">服务端</span> | 用于获取服务器component基类。实现新的component时，需要继承该接口返回的类 |
| [GetComponentCls](通用/Component.md#getcomponentcls) | <span style="display:inline;color:#7575f9">客户端</span> | 用于获取客户端component基类。实现新的component时，需要继承该接口返回的类 |
| [GetEngineCompFactory](通用/Component.md#getenginecompfactory) | <span style="display:inline;color:#ff5555">服务端</span> | 获取引擎组件的工厂，通过工厂可以创建服务端的引擎组件 |
| [GetEngineCompFactory](通用/Component.md#getenginecompfactory) | <span style="display:inline;color:#7575f9">客户端</span> | 获取引擎组件的工厂，通过工厂可以创建客户端的引擎组件 |
| [RegisterComponent](通用/Component.md#registercomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 用于将组件注册到引擎中 |
| [RegisterComponent](通用/Component.md#registercomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 用于将组件注册到引擎中 |
#### System
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetClientSystemCls](通用/System.md#getclientsystemcls) | <span style="display:inline;color:#7575f9">客户端</span> | 用于获取客户端system基类。实现新的system时，需要继承该接口返回的类 |
| [GetServerSystemCls](通用/System.md#getserversystemcls) | <span style="display:inline;color:#ff5555">服务端</span> | 用于获取服务器system基类。实现新的system时，需要继承该接口返回的类 |
| [GetSystem](通用/System.md#getsystem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取已注册的系统 |
| [GetSystem](通用/System.md#getsystem) | <span style="display:inline;color:#7575f9">客户端</span> | 用于获取其他系统实例 |
| [RegisterSystem](通用/System.md#registersystem) | <span style="display:inline;color:#ff5555">服务端</span> | 用于将系统注册到引擎中，引擎会创建一个该系统的实例，并在退出游戏时回收。系统可以执行我们引擎赋予的基本逻辑，例如监听事件、执行Tick函数、与客户端进行通讯等。 |
| [RegisterSystem](通用/System.md#registersystem) | <span style="display:inline;color:#7575f9">客户端</span> | 用于将系统注册到引擎中，引擎会创建一个该系统的实例，并在退出游戏时回收。系统可以执行我们引擎赋予的基本逻辑，例如监听事件、执行Tick函数、与服务端进行通讯等。 |
#### 事件
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [BroadcastEvent](通用/事件.md#broadcastevent) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 本地广播事件，客户端system广播的事件仅客户端system能监听，服务器system广播的事件仅服务端system能监听。 |
| [BroadcastToAllClient](通用/事件.md#broadcasttoallclient) | <span style="display:inline;color:#ff5555">服务端</span> | 服务器广播事件到所有客户端 |
| [CreateEventData](通用/事件.md#createeventdata) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 创建自定义事件的数据，eventData用于发送事件。创建的eventData可以理解为一个dict，可以嵌套赋值dict,list和基本数据类型，但不支持tuple |
| [GetEngineNamespace](通用/事件.md#getenginenamespace) | <span style="display:inline;color:#ff5555">服务端</span> | 获取引擎事件的命名空间。监听引擎事件时，namespace传该接口返回的namespace |
| [GetEngineNamespace](通用/事件.md#getenginenamespace) | <span style="display:inline;color:#7575f9">客户端</span> | 获取引擎事件的命名空间。监听引擎事件时，namespace传该接口返回的namespace |
| [GetEngineSystemName](通用/事件.md#getenginesystemname) | <span style="display:inline;color:#ff5555">服务端</span> | 获取引擎系统名。监听引擎事件时，systemName传该接口返回的systemName |
| [GetEngineSystemName](通用/事件.md#getenginesystemname) | <span style="display:inline;color:#7575f9">客户端</span> | 获取引擎系统名。监听引擎事件时，systemName传该接口返回的systemName |
| [ListenForEvent](通用/事件.md#listenforevent) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 注册监听某个系统抛出的事件。若监听引擎事件时，namespace和systemName分别为GetEngineNamespace()和GetEngineSystemName()。具体每个事件的详细事件data可以参考"事件"分类下的内容 |
| [NotifyToClient](通用/事件.md#notifytoclient) | <span style="display:inline;color:#ff5555">服务端</span> | 服务器发送事件到指定客户端 |
| [NotifyToMultiClients](通用/事件.md#notifytomulticlients) | <span style="display:inline;color:#ff5555">服务端</span> | 服务器发送事件到指定一批客户端，相比于在for循环内使用NotifyToClient性能更好 |
| [NotifyToServer](通用/事件.md#notifytoserver) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端发送事件到服务器 |
| [UnListenAllEvents](通用/事件.md#unlistenallevents) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 反注册监听某个系统抛出的所有事件，即不再监听。 |
| [UnListenForEvent](通用/事件.md#unlistenforevent) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 反注册监听某个系统抛出的事件，即不再监听。若是引擎事件，则namespace和systemName分别为[GetEngineNamespace](通用/事件.md#getenginenamespace)和[GetEngineSystemName](通用/事件.md#getenginesystemname)。与ListenForEvent对应。 |
#### 本地设备
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetEngineVersion](通用/本地设备.md#getengineversion) | <span style="display:inline;color:#7575f9">客户端</span> | 获取游戏版本-客户端。 |
| [GetIP](通用/本地设备.md#getip) | <span style="display:inline;color:#7575f9">客户端</span> | 获取本地玩家的ip地址 |
| [GetMinecraftVersion](通用/本地设备.md#getminecraftversion) | <span style="display:inline;color:#ff5555">服务端</span> | 获取Minecraft版本-服务端。 |
| [GetMinecraftVersion](通用/本地设备.md#getminecraftversion) | <span style="display:inline;color:#7575f9">客户端</span> | 获取Minecraft版本-客户端。 |
| [GetPlatform](通用/本地设备.md#getplatform) | <span style="display:inline;color:#ff5555">服务端</span> | 获取脚本运行的平台 |
| [GetPlatform](通用/本地设备.md#getplatform) | <span style="display:inline;color:#7575f9">客户端</span> | 获取脚本运行的平台 |
| [IsInApollo](通用/本地设备.md#isinapollo) | <span style="display:inline;color:#ff5555">服务端</span> | 返回当前游戏Mod是否运行在Apollo网络服 |
| [IsInServer](通用/本地设备.md#isinserver) | <span style="display:inline;color:#ff5555">服务端</span> | 获取当前游戏是否跑在服务器环境下 |
#### 本地存储
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetConfigData](通用/本地存储.md#getconfigdata) | <span style="display:inline;color:#7575f9">客户端</span> | 获取本地配置文件中存储的数据 |
| [SetConfigData](通用/本地存储.md#setconfigdata) | <span style="display:inline;color:#7575f9">客户端</span> | 以本地配置文件的方式存储数据 |
#### 数学
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetDirFromRot](通用/数学.md#getdirfromrot) | <span style="display:inline;color:#ff5555">服务端</span> | 通过旋转角度获取朝向 |
| [GetDirFromRot](通用/数学.md#getdirfromrot) | <span style="display:inline;color:#7575f9">客户端</span> | 通过旋转角度获取朝向 |
| [GetIntPos](通用/数学.md#getintpos) | <span style="display:inline;color:#ff5555">服务端</span> | 获取坐标所在方块的位置，即浮点数坐标向下取整后的整数坐标。 |
| [GetIntPos](通用/数学.md#getintpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取坐标所在方块的位置，即浮点数坐标向下取整后的整数坐标。 |
| [GetLocalPosFromWorld](通用/数学.md#getlocalposfromworld) | <span style="display:inline;color:#ff5555">服务端</span> | 获取基于实体的世界坐标对应的局部坐标 |
| [GetLocalPosFromWorld](通用/数学.md#getlocalposfromworld) | <span style="display:inline;color:#7575f9">客户端</span> | 获取基于实体的世界坐标对应的局部坐标 |
| [GetRotFromDir](通用/数学.md#getrotfromdir) | <span style="display:inline;color:#ff5555">服务端</span> | 通过朝向获取旋转角度 |
| [GetRotFromDir](通用/数学.md#getrotfromdir) | <span style="display:inline;color:#7575f9">客户端</span> | 通过朝向获取旋转角度 |
| [GetWorldPosFromLocal](通用/数学.md#getworldposfromlocal) | <span style="display:inline;color:#ff5555">服务端</span> | 获取基于实体的局部坐标对应的世界坐标 |
| [GetWorldPosFromLocal](通用/数学.md#getworldposfromlocal) | <span style="display:inline;color:#7575f9">客户端</span> | 获取基于实体的局部坐标对应的世界坐标 |
#### 工具
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddRepeatedTimer](通用/工具.md#addrepeatedtimer) | <span style="display:inline;color:#ff5555">服务端</span> | 添加服务端触发的定时器，重复执行 |
| [AddRepeatedTimer](通用/工具.md#addrepeatedtimer) | <span style="display:inline;color:#7575f9">客户端</span> | 添加客户端触发的定时器，重复执行 |
| [AddTimer](通用/工具.md#addtimer) | <span style="display:inline;color:#ff5555">服务端</span> | 添加服务端触发的定时器，非重复 |
| [AddTimer](通用/工具.md#addtimer) | <span style="display:inline;color:#7575f9">客户端</span> | 添加客户端触发的定时器，非重复 |
| [CancelTimer](通用/工具.md#canceltimer) | <span style="display:inline;color:#ff5555">服务端</span> | 取消定时器 |
| [CancelTimer](通用/工具.md#canceltimer) | <span style="display:inline;color:#7575f9">客户端</span> | 取消定时器 |
| [CheckNameValid](通用/工具.md#checknamevalid) | <span style="display:inline;color:#ff5555">服务端</span> | 检查昵称是否合法，即不包含敏感词 |
| [CheckNameValid](通用/工具.md#checknamevalid) | <span style="display:inline;color:#7575f9">客户端</span> | 检查昵称是否合法，即不包含敏感词 |
| [CheckWordsValid](通用/工具.md#checkwordsvalid) | <span style="display:inline;color:#ff5555">服务端</span> | 检查语句是否合法，即不包含敏感词 |
| [CheckWordsValid](通用/工具.md#checkwordsvalid) | <span style="display:inline;color:#7575f9">客户端</span> | 检查语句是否合法，即不包含敏感词 |
| [GetChinese](通用/工具.md#getchinese) | <span style="display:inline;color:#ff5555">服务端</span> | 获取langStr对应的中文，可参考PC开发包中\handheld\localization\handheld\data\resource_packs\vanilla\texts\zh_CN.lang |
| [GetChinese](通用/工具.md#getchinese) | <span style="display:inline;color:#7575f9">客户端</span> | 获取langStr对应的中文，可参考PC开发包中\handheld\localization\handheld\data\resource_packs\vanilla\texts\zh_CN.lang |
| [GetClipboardContent](通用/工具.md#getclipboardcontent) | <span style="display:inline;color:#7575f9">客户端</span> | 获取系统剪贴板内容 |
| [GetFps](通用/工具.md#getfps) | <span style="display:inline;color:#7575f9">客户端</span> | 获取fps |
| [GetHostPlayerId](通用/工具.md#gethostplayerid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取房主的entityId |
| [GetHostPlayerId](通用/工具.md#gethostplayerid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取房主的entityId |
| [GetMinecraftEnum](通用/工具.md#getminecraftenum) | <span style="display:inline;color:#ff5555">服务端</span> | 用于获取[枚举值文档](通用/../../枚举值/索引.md)中的枚举值 |
| [GetMinecraftEnum](通用/工具.md#getminecraftenum) | <span style="display:inline;color:#7575f9">客户端</span> | 用于获取[枚举值文档](通用/../../枚举值/索引.md)中的枚举值 |
| [GetModConfigJson](通用/工具.md#getmodconfigjson) | <span style="display:inline;color:#7575f9">客户端</span> | 以字典形式返回指定路径的json格式配置文件的内容，文件必须放置在资源包的/modconfigs目录下 |
| [GetServerTickTime](通用/工具.md#getserverticktime) | <span style="display:inline;color:#ff5555">服务端</span> | 获取服务端引擎上一帧的帧消耗时间 |
| [ImportModule](通用/工具.md#importmodule) | <span style="display:inline;color:#ff5555">服务端</span> | 使用字符串路径导入模块，作用与importlib.import_module类似，但只能导入当前加载的mod中的模块 |
| [ImportModule](通用/工具.md#importmodule) | <span style="display:inline;color:#7575f9">客户端</span> | 使用字符串路径导入模块，作用与importlib.import_module类似，但只能导入当前加载的mod中的模块 |
| [SetClipboardContent](通用/工具.md#setclipboardcontent) | <span style="display:inline;color:#7575f9">客户端</span> | 设置系统剪贴板内容 |
| [StartCoroutine](通用/工具.md#startcoroutine) | <span style="display:inline;color:#ff5555">服务端</span> | 开启服务端协程，实现函数分段式执行，可用于缓解复杂逻辑计算导致游戏卡顿问题 |
| [StartCoroutine](通用/工具.md#startcoroutine) | <span style="display:inline;color:#7575f9">客户端</span> | 开启客户端协程，实现函数分段式执行，可用于缓解复杂逻辑计算导致游戏卡顿问题 |
| [StopCoroutine](通用/工具.md#stopcoroutine) | <span style="display:inline;color:#ff5555">服务端</span> | 停止协程 |
| [StopCoroutine](通用/工具.md#stopcoroutine) | <span style="display:inline;color:#7575f9">客户端</span> | 停止客户端协程 |
#### 调试
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetEnableReconnectNetgame](通用/调试.md#getenablereconnectnetgame) | <span style="display:inline;color:#7575f9">客户端</span> | 获取是否允许断线重连 |
| [GetKeepResourceWhenTransfer](通用/调试.md#getkeepresourcewhentransfer) | <span style="display:inline;color:#7575f9">客户端</span> | 获取快速切服设置 |
| [GetMcpModLogCanPostDump](通用/调试.md#getmcpmodlogcanpostdump) | <span style="display:inline;color:#ff5555">服务端</span> | 获取是否可以打印错误信息到McpModLog日志。 |
| [GetMcpModLogCanPostDump](通用/调试.md#getmcpmodlogcanpostdump) | <span style="display:inline;color:#7575f9">客户端</span> | 获取是否可以打印错误信息到McpModLog日志。 |
| [GetResourceFastload](通用/调试.md#getresourcefastload) | <span style="display:inline;color:#7575f9">客户端</span> | 获取资源快速加载设置 |
| [PostMcpModDump](通用/调试.md#postmcpmoddump) | <span style="display:inline;color:#ff5555">服务端</span> | 主动打印信息到McpModLog日志，需要先调用 SetMcpModLogCanPostDump 接口进行设置，才能生效。 |
| [PostMcpModDump](通用/调试.md#postmcpmoddump) | <span style="display:inline;color:#7575f9">客户端</span> | 主动打印信息到McpModLog日志，需要先调用 SetMcpModLogCanPostDump 接口进行设置，才能生效。 |
| [ReloadAllMaterials](通用/调试.md#reloadallmaterials) | <span style="display:inline;color:#7575f9">客户端</span> | 重新加载所有材质文件 |
| [ReloadAllShaders](通用/调试.md#reloadallshaders) | <span style="display:inline;color:#7575f9">客户端</span> | 重新加载所有Shader文件 |
| [ReloadOneShader](通用/调试.md#reloadoneshader) | <span style="display:inline;color:#7575f9">客户端</span> | 重新加载某个Shader文件 |
| [SetEnableReconnectNetgame](通用/调试.md#setenablereconnectnetgame) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否允许断线重连 |
| [SetKeepResourceWhenTransfer](通用/调试.md#setkeepresourcewhentransfer) | <span style="display:inline;color:#7575f9">客户端</span> | 设置快速切服 |
| [SetMcpModLogCanPostDump](通用/调试.md#setmcpmodlogcanpostdump) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否可以打印错误信息到McpModLog日志。 |
| [SetMcpModLogCanPostDump](通用/调试.md#setmcpmodlogcanpostdump) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否可以打印错误信息到McpModLog日志。 |
| [SetResourceFastload](通用/调试.md#setresourcefastload) | <span style="display:inline;color:#7575f9">客户端</span> | 设置资源快速加载 |
| [StartMemProfile](通用/调试.md#startmemprofile) | <span style="display:inline;color:#ff5555">服务端</span> | 开始启动服务端脚本内存分析，启动后调用[StopMemProfile](通用/调试.md#stopMemProfile)即可在路径fileName生成函数内存火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。 |
| [StartMemProfile](通用/调试.md#startmemprofile) | <span style="display:inline;color:#7575f9">客户端</span> | 开始启动客户端脚本内存分析，启动后调用[StopMemProfile](通用/调试.md#stopMemProfile)即可在路径fileName生成函数内存火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。 |
| [StartMultiProfile](通用/调试.md#startmultiprofile) | <span style="display:inline;color:#ff5555">服务端</span> | 开始启动服务端与客户端双端脚本性能分析，启动后调用[StopMultiProfile](通用/调试.md#stopmultiprofile)即可在路径fileName生成函数性能火焰图。双端采集时数据误差较大，建议优先使用[StartProfile](通用/调试.md#startprofile)单端版本，此接口只支持PC端 |
| [StartMultiProfile](通用/调试.md#startmultiprofile) | <span style="display:inline;color:#7575f9">客户端</span> | 开始启动服务端与客户端双端脚本性能分析，启动后调用[StopMultiProfile](通用/调试.md#stopmultiprofile)即可在路径fileName生成函数性能火焰图。双端采集时数据误差较大，建议优先使用[StartProfile](通用/调试.md#startprofile)单端版本，此接口只支持PC端 |
| [StartProfile](通用/调试.md#startprofile) | <span style="display:inline;color:#ff5555">服务端</span> | 开始启动服务端脚本性能分析，启动后调用[StopProfile](通用/调试.md#stopprofile)即可在路径fileName生成函数性能火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。 |
| [StartProfile](通用/调试.md#startprofile) | <span style="display:inline;color:#7575f9">客户端</span> | 开始启动客户端脚本性能分析，启动后调用[StopProfile](通用/调试.md#stopprofile)即可在路径fileName生成函数性能火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。 |
| [StartRecordEvent](通用/调试.md#startrecordevent) | <span style="display:inline;color:#ff5555">Apollo</span> | 开始启动服务端与客户端之间的脚本事件收发统计，启动后调用[StopRecordEvent](通用/调试.md#stoprecordevent)即可获取两个函数调用之间脚本事件收发的统计信息，仅支持租赁服与Apollo网络服环境（不支持单机环境） |
| [StartRecordPacket](通用/调试.md#startrecordpacket) | <span style="display:inline;color:#ff5555">Apollo</span> | 开始启动服务端与客户端之间的引擎收发包统计，启动后调用[StopRecordPacket](通用/调试.md#stoprecordpacket)即可获取两个函数调用之间引擎收发包的统计信息，仅支持租赁服与Apollo网络服环境（不支持单机环境） |
| [StopMemProfile](通用/调试.md#stopmemprofile) | <span style="display:inline;color:#ff5555">服务端</span> | 停止服务端脚本内存分析并生成火焰图，与[StartMemProfile](通用/调试.md#startMemProfile)配合使用，此接口只支持PC端 |
| [StopMemProfile](通用/调试.md#stopmemprofile) | <span style="display:inline;color:#7575f9">客户端</span> | 停止客户端脚本内存分析并生成火焰图，与[StartMemProfile](通用/调试.md#startMemProfile)配合使用，此接口只支持PC端 |
| [StopMultiProfile](通用/调试.md#stopmultiprofile) | <span style="display:inline;color:#ff5555">服务端</span> | 停止双端脚本性能分析并生成火焰图，与[StartMultiProfile](通用/调试.md#startmultiprofile)配合使用，此接口只支持PC端 |
| [StopMultiProfile](通用/调试.md#stopmultiprofile) | <span style="display:inline;color:#7575f9">客户端</span> | 停止双端脚本性能分析并生成火焰图，与[StartMultiProfile](通用/调试.md#startmultiprofile)配合使用，此接口只支持PC端 |
| [StopProfile](通用/调试.md#stopprofile) | <span style="display:inline;color:#ff5555">服务端</span> | 停止服务端脚本性能分析并生成火焰图，与[StartProfile](通用/调试.md#startprofile)配合使用，此接口只支持PC端 |
| [StopProfile](通用/调试.md#stopprofile) | <span style="display:inline;color:#7575f9">客户端</span> | 停止客户端脚本性能分析并生成火焰图，与[StartProfile](通用/调试.md#startprofile)配合使用，此接口只支持PC端 |
| [StopRecordEvent](通用/调试.md#stoprecordevent) | <span style="display:inline;color:#ff5555">Apollo</span> | 停止服务端与客户端之间的脚本事件收发统计并输出结果，与[StartRecordEvent](通用/调试.md#startrecordevent)配合使用，输出结果为字典，key为网络包名，value字典中记录收发信息，具体见示例，仅支持租赁服与Apollo网络服环境（不支持单机环境） |
| [StopRecordPacket](通用/调试.md#stoprecordpacket) | <span style="display:inline;color:#ff5555">Apollo</span> | 停止服务端与客户端之间的引擎收发包统计并输出结果，与[StartRecordPacket](通用/调试.md#startrecordpacket)配合使用，输出结果为字典，key为网络包名，value字典中记录收发信息，具体见示例，仅支持租赁服与Apollo网络服环境（不支持单机环境） |
#### 地图
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CanSee](世界/地图.md#cansee) | <span style="display:inline;color:#ff5555">服务端</span> | 判断起始对象是否可看见目标对象,基于对象的Head位置判断 |
| [CanSee](世界/地图.md#cansee) | <span style="display:inline;color:#7575f9">客户端</span> | 判断起始对象是否可看见目标对象,基于对象的Head位置判断 |
| [CheckBlockToPos](世界/地图.md#checkblocktopos) | <span style="display:inline;color:#ff5555">服务端</span> | 判断位置之间是否有方块 |
| [CheckChunkState](世界/地图.md#checkchunkstate) | <span style="display:inline;color:#ff5555">服务端</span> | 判断指定位置的chunk是否加载完成 |
| [CreateDimension](世界/地图.md#createdimension) | <span style="display:inline;color:#ff5555">服务端</span> | 创建新的dimension |
| [CreateExplosion](世界/地图.md#createexplosion) | <span style="display:inline;color:#ff5555">服务端</span> | 用于生成爆炸 |
| [DeleteAllArea](世界/地图.md#deleteallarea) | <span style="display:inline;color:#ff5555">服务端</span> | 删除所有常加载区域 |
| [DeleteArea](世界/地图.md#deletearea) | <span style="display:inline;color:#ff5555">服务端</span> | 删除一个常加载区域 |
| [DetectStructure](世界/地图.md#detectstructure) | <span style="display:inline;color:#ff5555">服务端</span> | 检测自定义门的结构 |
| [DoTaskOnChunkAsync](世界/地图.md#dotaskonchunkasync) | <span style="display:inline;color:#ff5555">服务端</span> | 异步加载指定范围区块，加载完成后调用输入的回调函数。 |
| [GetAllAreaKeys](世界/地图.md#getallareakeys) | <span style="display:inline;color:#ff5555">服务端</span> | 获取所有常加载区域名称列表 |
| [GetBiomeInfo](世界/地图.md#getbiomeinfo) | <span style="display:inline;color:#ff5555">服务端</span> | 获取群系天气相关参数 |
| [GetBiomeName](世界/地图.md#getbiomename) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某一位置所属的生物群系信息 |
| [GetBiomeName](世界/地图.md#getbiomename) | <span style="display:inline;color:#7575f9">客户端</span> | 获取客户端当前维度已加载区域某一位置所属的生物群系信息 |
| [GetBlockLightLevel](世界/地图.md#getblocklightlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 获取方块位置的光照等级 |
| [GetChunkEntites](世界/地图.md#getchunkentites) | <span style="display:inline;color:#ff5555">服务端</span> | 获取指定位置的区块中，全部的实体和玩家的ID列表 |
| [GetChunkMaxPos](世界/地图.md#getchunkmaxpos) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某区块最大点的坐标 |
| [GetChunkMinPos](世界/地图.md#getchunkminpos) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某区块最小点的坐标 |
| [GetChunkMobNum](世界/地图.md#getchunkmobnum) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某区块中的生物数量（不包括玩家，但包括盔甲架） |
| [GetChunkPosFromBlockPos](世界/地图.md#getchunkposfromblockpos) | <span style="display:inline;color:#ff5555">服务端</span> | 通过方块坐标获得该方块所在区块坐标 |
| [GetChunkPosFromBlockPos](世界/地图.md#getchunkposfromblockpos) | <span style="display:inline;color:#7575f9">客户端</span> | 通过方块坐标获得该方块所在区块坐标 |
| [GetCurrentDimension](世界/地图.md#getcurrentdimension) | <span style="display:inline;color:#7575f9">客户端</span> | 获取客户端当前维度 |
| [GetEntitiesAround](世界/地图.md#getentitiesaround) | <span style="display:inline;color:#ff5555">服务端</span> | 获取区域内的entity列表 |
| [GetEntitiesAround](世界/地图.md#getentitiesaround) | <span style="display:inline;color:#7575f9">客户端</span> | 获取区域内的entity列表 |
| [GetEntitiesAroundByType](世界/地图.md#getentitiesaroundbytype) | <span style="display:inline;color:#ff5555">服务端</span> | 获取区域内的某类型的entity列表 |
| [GetEntitiesAroundByType](世界/地图.md#getentitiesaroundbytype) | <span style="display:inline;color:#7575f9">客户端</span> | 获取区域内的某类型的entity列表 |
| [GetEntitiesInSquareArea](世界/地图.md#getentitiesinsquarearea) | <span style="display:inline;color:#ff5555">服务端</span> | 获取区域内的entity列表 |
| [GetEntitiesInSquareArea](世界/地图.md#getentitiesinsquarearea) | <span style="display:inline;color:#7575f9">客户端</span> | 获取区域内的entity列表 |
| [GetLevelId](世界/地图.md#getlevelid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取levelId。某些组件需要levelId创建，可以用此接口获取levelId。其中level即为当前地图的游戏。 |
| [GetLevelId](世界/地图.md#getlevelid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取levelId。某些组件需要levelId创建，可以用此接口获取levelId。其中level即为当前地图的游戏。 |
| [GetLoadedChunks](世界/地图.md#getloadedchunks) | <span style="display:inline;color:#ff5555">服务端</span> | 获取指定维度当前已经加载完毕的全部区块的坐标列表 |
| [GetSpawnDimension](世界/地图.md#getspawndimension) | <span style="display:inline;color:#ff5555">服务端</span> | 获取世界出生维度 |
| [GetSpawnPosition](世界/地图.md#getspawnposition) | <span style="display:inline;color:#ff5555">服务端</span> | 获取世界出生点坐标 |
| [GetStructureSize](世界/地图.md#getstructuresize) | <span style="display:inline;color:#ff5555">服务端</span> | 获取结构体的长宽高 |
| [IsChunkGenerated](世界/地图.md#ischunkgenerated) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某个区块是否生成过。 |
| [IsSlimeChunk](世界/地图.md#isslimechunk) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某个区块是否是史莱姆区块。 |
| [LocateNeteaseFeatureRule](世界/地图.md#locateneteasefeaturerule) | <span style="display:inline;color:#ff5555">服务端</span> | 与[/locate指令](https://zh.minecraft.wiki/w/%E5%91%BD%E4%BB%A4/locate)相似，用于定位<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/4-自定义维度/4-自定义特征.html#特征规则（feature-rules）">网易自定义特征规则</a> |
| [LocateStructureFeature](世界/地图.md#locatestructurefeature) | <span style="display:inline;color:#ff5555">服务端</span> | 与[/locate指令](https://zh.minecraft.wiki/w/%E5%91%BD%E4%BB%A4/locate)相似，用于定位原版的部分结构，如海底神殿、末地城等。 |
| [MayPlace](世界/地图.md#mayplace) | <span style="display:inline;color:#ff5555">服务端</span> | 判断方块是否可以放置 |
| [MayPlaceOn](世界/地图.md#mayplaceon) | <span style="display:inline;color:#ff5555">服务端</span> | 判断物品是否可以放到指定的位置上 |
| [MirrorDimension](世界/地图.md#mirrordimension) | <span style="display:inline;color:#ff5555">服务端</span> | 复制不同dimension的地形 |
| [OpenClientChunkGeneration](世界/地图.md#openclientchunkgeneration) | <span style="display:inline;color:#ff5555">服务端</span> | 开启/关闭客户端区块生成功能，需要在LoadServerAddonScriptsAfter事件触发时调用。开启客户端区块生成功能时，如果使用了netease:structure_feature或修改了大部分地图，会导致客户端和服务端地图不一致的问题。此时可以通过关闭客户端区块生成功能解决该问题。 |
| [PlaceFeature](世界/地图.md#placefeature) | <span style="display:inline;color:#ff5555">服务端</span> | 放置特征，与[/placefeature指令](https://zh.minecraft.wiki/w/%E5%91%BD%E4%BB%A4/placefeature)相似 |
| [PlaceNeteaseLargeFeature](世界/地图.md#placeneteaselargefeature) | <span style="display:inline;color:#ff5555">服务端</span> | 放置<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/4-自定义维度/6-自定义大型特征.html#自定义大型特征">网易版大型结构特征</a> |
| [PlaceStructure](世界/地图.md#placestructure) | <span style="display:inline;color:#ff5555">服务端</span> | 放置结构 |
| [SetAddArea](世界/地图.md#setaddarea) | <span style="display:inline;color:#ff5555">服务端</span> | 设置区块的常加载 |
| [SetBiomeByPos](世界/地图.md#setbiomebypos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置某一位置所属的生物群系信息 |
| [SetBiomeByPosList](世界/地图.md#setbiomebyposlist) | <span style="display:inline;color:#ff5555">服务端</span> | 设置所有列表中位置所属的生物群系信息 |
| [SetBiomeByVolume](世界/地图.md#setbiomebyvolume) | <span style="display:inline;color:#ff5555">服务端</span> | 设置长方体空间中所属的生物群系信息 |
| [SetBiomeInfo](世界/地图.md#setbiomeinfo) | <span style="display:inline;color:#ff5555">服务端</span> | 设置群系天气相关参数 |
| [SetMergeSpawnItemRadius](世界/地图.md#setmergespawnitemradius) | <span style="display:inline;color:#ff5555">服务端</span> | 设置新生成的物品是否合堆 |
| [SetSpawnDimensionAndPosition](世界/地图.md#setspawndimensionandposition) | <span style="display:inline;color:#ff5555">服务端</span> | 设置世界出生点维度与坐标 |
| [UpgradeMapDimensionVersion](世界/地图.md#upgrademapdimensionversion) | <span style="display:inline;color:#ff5555">服务端</span> | 提升指定地图维度的版本号，版本号不符的维度，地图存档信息将被废弃。使用后存档的地图版本均会同步提升至最新版本，假如希望使用此接口清理指定维度的地图存档，需要在保证该维度区块都没有被加载时调用。 |
#### 实体管理
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CreateClientEntityByTypeStr](世界/实体管理.md#createcliententitybytypestr) | <span style="display:inline;color:#7575f9">客户端</span> | 创建客户端实体 |
| [CreateEngineEntityByNBT](世界/实体管理.md#createengineentitybynbt) | <span style="display:inline;color:#ff5555">服务端</span> | 根据nbt数据创建实体 |
| [CreateEngineEntityByTypeStr](世界/实体管理.md#createengineentitybytypestr) | <span style="display:inline;color:#ff5555">服务端</span> | 创建指定identifier的实体 |
| [CreateEngineItemEntity](世界/实体管理.md#createengineitementity) | <span style="display:inline;color:#ff5555">服务端</span> | 用于创建物品实体（即掉落物），返回物品实体的entityId |
| [CreateEntityAOI](世界/实体管理.md#createentityaoi) | <span style="display:inline;color:#ff5555">服务端</span> | 注册感应区域，有实体进入时和离开时会触发回调函数func |
| [CreateExperienceOrb](世界/实体管理.md#createexperienceorb) | <span style="display:inline;color:#ff5555">服务端</span> | 创建专属经验球 |
| [CreateProjectileEntity](世界/实体管理.md#createprojectileentity) | <span style="display:inline;color:#ff5555">服务端</span> | 创建抛射物（直接发射） |
| [DeleteEntityAOI](世界/实体管理.md#deleteentityaoi) | <span style="display:inline;color:#ff5555">服务端</span> | 删除使用[CreateEntityAOI](世界/实体管理.md#createentityaoi)注册的感应区 |
| [DestroyClientEntity](世界/实体管理.md#destroycliententity) | <span style="display:inline;color:#7575f9">客户端</span> | 销毁客户端实体 |
| [DestroyEntity](世界/实体管理.md#destroyentity) | <span style="display:inline;color:#ff5555">服务端</span> | 销毁实体 |
| [GetDroppedItem](世界/实体管理.md#getdroppeditem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取掉落物的物品信息 |
| [GetEngineActor](世界/实体管理.md#getengineactor) | <span style="display:inline;color:#ff5555">服务端</span> | 获取所有维度中已加载的所有实体（不包含玩家）。 |
| [GetEngineActor](世界/实体管理.md#getengineactor) | <span style="display:inline;color:#7575f9">客户端</span> | 获取客户端当前维度中已加载的所有实体（不包含玩家）。 |
| [GetLocalPlayerId](世界/实体管理.md#getlocalplayerid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取本地玩家的id |
| [GetLootItems](世界/实体管理.md#getlootitems) | <span style="display:inline;color:#ff5555">服务端</span> | 指定战利品表获取一次战利品，返回的物品与json定义的概率有关 |
| [GetPlayerList](世界/实体管理.md#getplayerlist) | <span style="display:inline;color:#ff5555">服务端</span> | 获取所有维度中的全部玩家的id列表 |
| [GetPlayerList](世界/实体管理.md#getplayerlist) | <span style="display:inline;color:#7575f9">客户端</span> | 获取所有维度中的全部玩家的id列表 |
| [HasEntity](世界/实体管理.md#hasentity) | <span style="display:inline;color:#7575f9">客户端</span> | 判断 entity 是否存在 |
| [IsEntityAlive](世界/实体管理.md#isentityalive) | <span style="display:inline;color:#ff5555">服务端</span> | 判断生物实体是否存活或非生物实体是否存在 |
| [IsEntityAlive](世界/实体管理.md#isentityalive) | <span style="display:inline;color:#7575f9">客户端</span> | 判断生物实体是否存活或非生物实体是否存在 |
| [KillEntity](世界/实体管理.md#killentity) | <span style="display:inline;color:#ff5555">服务端</span> | 杀死某个Entity |
| [SpawnLootTable](世界/实体管理.md#spawnloottable) | <span style="display:inline;color:#ff5555">服务端</span> | 使用生物类型模拟一次随机掉落，生成的物品与json定义的概率有关 |
| [SpawnLootTableWithActor](世界/实体管理.md#spawnloottablewithactor) | <span style="display:inline;color:#ff5555">服务端</span> | 使用生物实例模拟一次随机掉落，生成的物品与json定义的概率有关 |
| [SpawnResources](世界/实体管理.md#spawnresources) | <span style="display:inline;color:#ff5555">服务端</span> | 产生方块随机掉落（该方法不适用于实体方块） |
| [SpawnResourcesSilkTouched](世界/实体管理.md#spawnresourcessilktouched) | <span style="display:inline;color:#ff5555">服务端</span> | 模拟方块精准采集掉落 |
| [getEntitiesOrBlockFromRay](世界/实体管理.md#getentitiesorblockfromray) | <span style="display:inline;color:#ff5555">服务端</span> | 从指定位置发射一条射线，获取与射线相交的实体和方块 |
| [getEntitiesOrBlockFromRay](世界/实体管理.md#getentitiesorblockfromray) | <span style="display:inline;color:#7575f9">客户端</span> | 从指定位置发射一条射线，获取与射线相交的实体和方块 |
#### 方块管理
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetBlock](世界/方块管理.md#getblock) | <span style="display:inline;color:#7575f9">客户端</span> | 获取某一位置的block |
| [GetBlockClip](世界/方块管理.md#getblockclip) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某一位置方块当前<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html#netease-aabb">clip的aabb</a> |
| [GetBlockClip](世界/方块管理.md#getblockclip) | <span style="display:inline;color:#7575f9">客户端</span> | 获取指定位置方块当前clip的aabb |
| [GetBlockCollision](世界/方块管理.md#getblockcollision) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某一位置方块当前collision的aabb |
| [GetBlockCollision](世界/方块管理.md#getblockcollision) | <span style="display:inline;color:#7575f9">客户端</span> | 获取指定位置方块当前collision的aabb |
| [GetBlockNew](世界/方块管理.md#getblocknew) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某一位置的block |
| [GetDestroyTotalTime](世界/方块管理.md#getdestroytotaltime) | <span style="display:inline;color:#ff5555">服务端</span> | 获取使用物品破坏方块需要的时间 |
| [GetDestroyTotalTime](世界/方块管理.md#getdestroytotaltime) | <span style="display:inline;color:#7575f9">客户端</span> | 获取使用物品破坏方块需要的时间 |
| [GetLiquidBlock](世界/方块管理.md#getliquidblock) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某个位置的方块所含流体的信息 |
| [GetTopBlockHeight](世界/方块管理.md#gettopblockheight) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某一位置最高的非空气方块的高度 |
| [GetTopBlockHeight](世界/方块管理.md#gettopblockheight) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前维度某一位置最高的非空气方块的高度 |
| [SetBlockNew](世界/方块管理.md#setblocknew) | <span style="display:inline;color:#ff5555">服务端</span> | 设置某一位置的方块 |
| [SetJigsawBlock](世界/方块管理.md#setjigsawblock) | <span style="display:inline;color:#ff5555">服务端</span> | 在某一位置放置拼图方块 |
| [SetLiquidBlock](世界/方块管理.md#setliquidblock) | <span style="display:inline;color:#ff5555">服务端</span> | 设置某一位置的方块的extraBlock，可在此设置方块含水等 |
| [SetSnowBlock](世界/方块管理.md#setsnowblock) | <span style="display:inline;color:#ff5555">服务端</span> | 设置某一位置的方块含雪 |
#### 生物生成
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetEntityLimit](世界/生物生成.md#getentitylimit) | <span style="display:inline;color:#ff5555">服务端</span> | 获取世界最大可生成实体数量上限。可生成实体的含义见[SetEntityLimit](世界/生物生成.md#setentitylimit) |
| [SetEntityLimit](世界/生物生成.md#setentitylimit) | <span style="display:inline;color:#ff5555">服务端</span> | 设置世界最大可生成实体数量上限。可生成实体指具有spawnrule的实体。当前世界上被加载的可生成实体数量超过这个上限时，生物就不会再通过spawnrule刷出。 |
| [SpawnCustomModule](世界/生物生成.md#spawncustommodule) | <span style="display:inline;color:#ff5555">服务端</span> | 设置自定义刷怪 |
#### 配方
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddBrewingRecipes](世界/配方.md#addbrewingrecipes) | <span style="display:inline;color:#ff5555">服务端</span> | 添加酿造台配方的接口 |
| [AddRecipe](世界/配方.md#addrecipe) | <span style="display:inline;color:#ff5555">服务端</span> | 动态注册配方，支持配方类型详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/5-自定义配方.html#配方类型说明">[配方类型说明]</a> |
| [GetRecipeResult](世界/配方.md#getreciperesult) | <span style="display:inline;color:#ff5555">服务端</span> | 根据配方id获取配方结果。仅支持合成配方 |
| [GetRecipesByInput](世界/配方.md#getrecipesbyinput) | <span style="display:inline;color:#ff5555">服务端</span> | 通过输入物品查询配方 |
| [GetRecipesByInput](世界/配方.md#getrecipesbyinput) | <span style="display:inline;color:#7575f9">客户端</span> | 通过输入物品查询配方 |
| [GetRecipesByResult](世界/配方.md#getrecipesbyresult) | <span style="display:inline;color:#ff5555">服务端</span> | 通过输出物品查询配方所需要的输入材料 |
| [GetRecipesByResult](世界/配方.md#getrecipesbyresult) | <span style="display:inline;color:#7575f9">客户端</span> | 通过输出物品查询配方所需要的输入材料 |
| [RemoveRecipe](世界/配方.md#removerecipe) | <span style="display:inline;color:#ff5555">服务端</span> | 动态禁用配方 |
#### 方块组合
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CreateMicroBlockResStr](世界/方块组合.md#createmicroblockresstr) | <span style="display:inline;color:#ff5555">服务端</span> | 生成微缩方块资源Json字符串 |
| [GetBlankBlockPalette](世界/方块组合.md#getblankblockpalette) | <span style="display:inline;color:#ff5555">服务端</span> | 获取一个空白的方块调色板。 |
| [GetBlankBlockPalette](世界/方块组合.md#getblankblockpalette) | <span style="display:inline;color:#7575f9">客户端</span> | 获取一个空白的方块调色板。 |
| [GetBlockPaletteBetweenPos](世界/方块组合.md#getblockpalettebetweenpos) | <span style="display:inline;color:#ff5555">服务端</span> | 根据输入的两个方块位置创建并获取一个方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。这个方块调色板包含了这两个位置之间的所有方块及其相对位置。 |
| [GetBlockPaletteBetweenPos](世界/方块组合.md#getblockpalettebetweenpos) | <span style="display:inline;color:#7575f9">客户端</span> | 根据输入的两个位置创建并获取一个方块调色板，该接口会搜索这两个位置之间的所有方块创建方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。这个方块调色板包含了这两个位置之间的所有方块及其相对位置。 |
| [GetBlockPaletteFromPosList](世界/方块组合.md#getblockpalettefromposlist) | <span style="display:inline;color:#ff5555">服务端</span> | 根据输入的方块位置列表创建并获取一个方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。创建的方块调色板包含了这个位置列表中的所有方块及其相对位置。 |
| [GetBlockPaletteFromPosList](世界/方块组合.md#getblockpalettefromposlist) | <span style="display:inline;color:#7575f9">客户端</span> | 根据输入的方块位置列表创建并获取一个方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。创建的方块调色板包含了这个位置列表中的所有方块及其相对位置。 |
| [RegisterBlockPatterns](世界/方块组合.md#registerblockpatterns) | <span style="display:inline;color:#ff5555">服务端</span> | 注册特殊方块组合 |
| [SetBlockByBlockPalette](世界/方块组合.md#setblockbyblockpalette) | <span style="display:inline;color:#ff5555">服务端</span> | 根据输入的方块调色板内容，将调色板内记录的所有方块设置为实际的方块。 |
#### 渲染
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddTerrainDestroyParticleEffect](世界/渲染.md#addterraindestroyparticleeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 在指定位置播放指定方块被开始破坏时的粒子效果（如果有）。 |
| [AddUseItemParticleEffect](世界/渲染.md#adduseitemparticleeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 在指定位置播放指定物品被开始使用时的粒子效果（如果有）。 |
| [GetAmbientBrightness](世界/渲染.md#getambientbrightness) | <span style="display:inline;color:#7575f9">客户端</span> | 获取环境光亮度，影响天空亮度，不影响实体与方块光照 |
| [GetFogColor](世界/渲染.md#getfogcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前雾效颜色 |
| [GetFogLength](世界/渲染.md#getfoglength) | <span style="display:inline;color:#7575f9">客户端</span> | 获取雾效范围 |
| [GetMoonRot](世界/渲染.md#getmoonrot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取月亮角度 |
| [GetSkyColor](世界/渲染.md#getskycolor) | <span style="display:inline;color:#7575f9">客户端</span> | 获取天空颜色 |
| [GetSkyTextures](世界/渲染.md#getskytextures) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前维度天空盒贴图，天空盒共6张贴图 |
| [GetStarBrightness](世界/渲染.md#getstarbrightness) | <span style="display:inline;color:#7575f9">客户端</span> | 获取星星亮度 |
| [GetSunRot](世界/渲染.md#getsunrot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取太阳角度 |
| [GetUseAmbientBrightness](世界/渲染.md#getuseambientbrightness) | <span style="display:inline;color:#7575f9">客户端</span> | 判断是否在mod设置了环境光亮度 |
| [GetUseFogColor](世界/渲染.md#getusefogcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 判断当前是否开启设置雾效颜色，该值默认为False，使用mod传入的颜色值后为True |
| [GetUseFogLength](世界/渲染.md#getusefoglength) | <span style="display:inline;color:#7575f9">客户端</span> | 判断当前是否开启设置雾效范围,该值默认为False，使用mod传入的范围值后为True |
| [GetUseMoonRot](世界/渲染.md#getusemoonrot) | <span style="display:inline;color:#7575f9">客户端</span> | 判断是否在mod设置了月亮角度 |
| [GetUseSkyColor](世界/渲染.md#getuseskycolor) | <span style="display:inline;color:#7575f9">客户端</span> | 判断是否在mod设置了天空颜色 |
| [GetUseStarBrightness](世界/渲染.md#getusestarbrightness) | <span style="display:inline;color:#7575f9">客户端</span> | 判断是否在mod设置了星星亮度 |
| [GetUseSunRot](世界/渲染.md#getusesunrot) | <span style="display:inline;color:#7575f9">客户端</span> | 判断是否在mod设置了太阳角度 |
| [HideNameTag](世界/渲染.md#hidenametag) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏场景内所有名字，包括玩家名字，生物的自定义名称，物品展示框与命令方块的悬浮文本等 |
| [IsHideNameTag](世界/渲染.md#ishidenametag) | <span style="display:inline;color:#7575f9">客户端</span> | 获取是否隐藏场景内所有名字 |
| [RemoveTerrainDestroyParticleEffect](世界/渲染.md#removeterraindestroyparticleeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 停止指定位置播放的方块被开始破坏时的粒子效果。 |
| [RemoveUseItemParticleEffect](世界/渲染.md#removeuseitemparticleeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 停止指定位置播放的物品被开始使用时的粒子效果。 |
| [ResetAmbientBrightness](世界/渲染.md#resetambientbrightness) | <span style="display:inline;color:#7575f9">客户端</span> | 重置环境光亮度 |
| [ResetFogColor](世界/渲染.md#resetfogcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 重置雾效颜色 |
| [ResetFogLength](世界/渲染.md#resetfoglength) | <span style="display:inline;color:#7575f9">客户端</span> | 重置雾效范围 |
| [ResetMoonRot](世界/渲染.md#resetmoonrot) | <span style="display:inline;color:#7575f9">客户端</span> | 重置月亮角度 |
| [ResetSkyColor](世界/渲染.md#resetskycolor) | <span style="display:inline;color:#7575f9">客户端</span> | 重置天空颜色 |
| [ResetSkyTextures](世界/渲染.md#resetskytextures) | <span style="display:inline;color:#7575f9">客户端</span> | 重置当前维度天空盒贴图。如果有使用addon配置贴图则会使用配置的贴图，否则为游戏内默认无贴图的情况 |
| [ResetStarBrightness](世界/渲染.md#resetstarbrightness) | <span style="display:inline;color:#7575f9">客户端</span> | 重置星星亮度 |
| [ResetSunRot](世界/渲染.md#resetsunrot) | <span style="display:inline;color:#7575f9">客户端</span> | 重置太阳角度 |
| [SetAmbientBrightness](世界/渲染.md#setambientbrightness) | <span style="display:inline;color:#7575f9">客户端</span> | 设置环境光亮度，影响天空亮度，不影响实体与方块光照 |
| [SetFogColor](世界/渲染.md#setfogcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 设置雾效颜色 |
| [SetFogLength](世界/渲染.md#setfoglength) | <span style="display:inline;color:#7575f9">客户端</span> | 设置雾效范围 |
| [SetMoonRot](世界/渲染.md#setmoonrot) | <span style="display:inline;color:#7575f9">客户端</span> | 设置月亮所在角度 |
| [SetSkyColor](世界/渲染.md#setskycolor) | <span style="display:inline;color:#7575f9">客户端</span> | 设置天空颜色 |
| [SetSkyTextures](世界/渲染.md#setskytextures) | <span style="display:inline;color:#7575f9">客户端</span> | 设置当前维度天空盒贴图，天空盒需要6张贴图 |
| [SetStarBrightness](世界/渲染.md#setstarbrightness) | <span style="display:inline;color:#7575f9">客户端</span> | 设置星星亮度，白天也可以显示星星 |
| [SetSunRot](世界/渲染.md#setsunrot) | <span style="display:inline;color:#7575f9">客户端</span> | 设置太阳所在角度 |
| [SkyTextures](世界/渲染.md#skytextures) | <span style="display:inline;color:#7575f9">客户端</span> | 修改太阳、月亮、云层分布、天空盒的贴图。使用addon配置，非python接口。 |
#### 时间
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetLocalDoDayNightCycle](世界/时间.md#getlocaldodaynightcycle) | <span style="display:inline;color:#ff5555">服务端</span> | 获取维度是否打开昼夜更替 |
| [GetLocalTime](世界/时间.md#getlocaltime) | <span style="display:inline;color:#ff5555">服务端</span> | 获取维度的时间 |
| [GetLocalTime](世界/时间.md#getlocaltime) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前维度的时间 |
| [GetTime](世界/时间.md#gettime) | <span style="display:inline;color:#ff5555">服务端</span> | 获取当前世界时间 |
| [GetTime](世界/时间.md#gettime) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前世界时间 |
| [GetUseLocalTime](世界/时间.md#getuselocaltime) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某个维度是否设置了使用局部时间规则 |
| [SetLocalDoDayNightCycle](世界/时间.md#setlocaldodaynightcycle) | <span style="display:inline;color:#ff5555">服务端</span> | 设置使用局部时间规则的维度是否打开昼夜更替 |
| [SetLocalTime](世界/时间.md#setlocaltime) | <span style="display:inline;color:#ff5555">服务端</span> | 设置使用局部时间规则维度的时间 |
| [SetLocalTimeOfDay](世界/时间.md#setlocaltimeofday) | <span style="display:inline;color:#ff5555">服务端</span> | 设置使用局部时间规则维度在一天内所在的时间 |
| [SetTime](世界/时间.md#settime) | <span style="display:inline;color:#ff5555">服务端</span> | 设置当前世界时间 |
| [SetTimeOfDay](世界/时间.md#settimeofday) | <span style="display:inline;color:#ff5555">服务端</span> | 设置当前世界在一天内所在的时间 |
| [SetUseLocalTime](世界/时间.md#setuselocaltime) | <span style="display:inline;color:#ff5555">服务端</span> | 让某个维度拥有自己的局部时间规则，开启后该维度可以拥有与其他维度不同的时间与是否昼夜更替的规则 |
#### 天气
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetDimensionLocalWeatherInfo](世界/天气.md#getdimensionlocalweatherinfo) | <span style="display:inline;color:#ff5555">服务端</span> | 获取独立维度天气信息(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气) |
| [GetDimensionUseLocalWeather](世界/天气.md#getdimensionuselocalweather) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某个维度是否拥有自己的天气规则 |
| [IsRaining](世界/天气.md#israining) | <span style="display:inline;color:#ff5555">服务端</span> | 获取是否下雨 |
| [IsThunder](世界/天气.md#isthunder) | <span style="display:inline;color:#ff5555">服务端</span> | 获取是否打雷 |
| [SetDimensionLocalDoWeatherCycle](世界/天气.md#setdimensionlocaldoweathercycle) | <span style="display:inline;color:#ff5555">服务端</span> | 设置某个维度是否开启天气循环(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气) |
| [SetDimensionLocalRain](世界/天气.md#setdimensionlocalrain) | <span style="display:inline;color:#ff5555">服务端</span> | 设置某个维度下雨(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气) |
| [SetDimensionLocalThunder](世界/天气.md#setdimensionlocalthunder) | <span style="display:inline;color:#ff5555">服务端</span> | 设置某个维度打雷(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气) |
| [SetDimensionUseLocalWeather](世界/天气.md#setdimensionuselocalweather) | <span style="display:inline;color:#ff5555">服务端</span> | 设置某个维度拥有自己的天气规则，开启后该维度可以拥有与其他维度不同的天气和天气更替的规则 |
| [SetRaining](世界/天气.md#setraining) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否下雨 |
| [SetThunder](世界/天气.md#setthunder) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否打雷 |
#### 游戏规则
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddBannedItem](世界/游戏规则.md#addbanneditem) | <span style="display:inline;color:#ff5555">服务端</span> | 增加禁用物品 |
| [AddBlockProtectField](世界/游戏规则.md#addblockprotectfield) | <span style="display:inline;color:#ff5555">Apollo</span> | 设置一个方块无法被玩家/实体破坏的区域 |
| [CleanBlockProtectField](世界/游戏规则.md#cleanblockprotectfield) | <span style="display:inline;color:#ff5555">Apollo</span> | 取消全部已设置的方块无法被玩家/实体破坏的区域 |
| [ClearBannedItems](世界/游戏规则.md#clearbanneditems) | <span style="display:inline;color:#ff5555">服务端</span> | 清空禁用物品 |
| [DisableVineBlockSpread](世界/游戏规则.md#disablevineblockspread) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否禁用藤曼蔓延生长 |
| [ForbidLiquidFlow](世界/游戏规则.md#forbidliquidflow) | <span style="display:inline;color:#ff5555">服务端</span> | 禁止/允许地图中的流体流动 |
| [GetBannedItemList](世界/游戏规则.md#getbanneditemlist) | <span style="display:inline;color:#ff5555">服务端</span> | 获取禁用物品列表 |
| [GetGameDiffculty](世界/游戏规则.md#getgamediffculty) | <span style="display:inline;color:#ff5555">服务端</span> | 获取游戏难度 |
| [GetGameRulesInfoServer](世界/游戏规则.md#getgamerulesinfoserver) | <span style="display:inline;color:#ff5555">服务端</span> | 获取游戏规则 |
| [GetGameType](世界/游戏规则.md#getgametype) | <span style="display:inline;color:#ff5555">服务端</span> | 获取默认游戏模式 |
| [GetLevelGravity](世界/游戏规则.md#getlevelgravity) | <span style="display:inline;color:#ff5555">服务端</span> | 获取重力因子 |
| [GetPistonMaxInteractionCount](世界/游戏规则.md#getpistonmaxinteractioncount) | <span style="display:inline;color:#ff5555">服务端</span> | 获取活塞/粘性活塞最多推动的方块数量，默认为12个方块，可能被其他开发者修改。 |
| [GetPistonMaxInteractionCount](世界/游戏规则.md#getpistonmaxinteractioncount) | <span style="display:inline;color:#7575f9">客户端</span> | 获取活塞/粘性活塞最多推动的方块数量，默认为12个方块，可能被其他开发者修改。 |
| [GetSeed](世界/游戏规则.md#getseed) | <span style="display:inline;color:#ff5555">服务端</span> | 获取存档种子 |
| [IsDisableCommandMinecart](世界/游戏规则.md#isdisablecommandminecart) | <span style="display:inline;color:#ff5555">服务端</span> | 获取当前是否允许运行命令方块矿车内置逻辑指令，当前仅Apollo网络服可用 |
| [IsLockDifficulty](世界/游戏规则.md#islockdifficulty) | <span style="display:inline;color:#ff5555">服务端</span> | 获取当前世界的游戏难度是否被锁定 |
| [IsLockGameRulesInfo](世界/游戏规则.md#islockgamerulesinfo) | <span style="display:inline;color:#ff5555">服务端</span> | 获取当前世界的游戏规则是否被锁定 |
| [IsLockGameType](世界/游戏规则.md#islockgametype) | <span style="display:inline;color:#ff5555">服务端</span> | 获取当前世界的游戏类型是否被锁定，包括默认游戏类型和个人游戏类型 |
| [LockDifficulty](世界/游戏规则.md#lockdifficulty) | <span style="display:inline;color:#ff5555">服务端</span> | 锁定当前世界游戏难度（仅本次游戏有效），锁定后任何玩家在游戏内都无法通过指令或暂停菜单修改游戏难度 |
| [LockGameRulesInfo](世界/游戏规则.md#lockgamerulesinfo) | <span style="display:inline;color:#ff5555">服务端</span> | 锁定当前世界游戏规则（仅本次游戏有效），玩家无法通过指令、游戏菜单或api修改游戏规则（包括[SetGameRulesInfoServer](世界/游戏规则.md#setgamerulesinfoserver)示例中列举的规则） |
| [LockGameType](世界/游戏规则.md#lockgametype) | <span style="display:inline;color:#ff5555">服务端</span> | 锁定当前世界游戏类型（仅本次游戏有效），玩家无法通过指令、游戏菜单或相关api如[SetPlayerGameType](世界/../玩家/游戏模式.md#setplayergametype)和[SetDefaultGameType](世界/游戏规则.md#setdefaultgametype)修改游戏类型，包括默认游戏类型和个人游戏类型 |
| [OpenCityProtect](世界/游戏规则.md#opencityprotect) | <span style="display:inline;color:#ff5555">Apollo</span> | 开启城市保护，包括禁止破坏方块，禁止对方块使用物品，禁止怪物攻击玩家，禁止玩家之间互相攻击，禁止日夜切换，禁止天气变化，禁止怪物群落刷新 |
| [RemoveBannedItem](世界/游戏规则.md#removebanneditem) | <span style="display:inline;color:#ff5555">服务端</span> | 移除禁用物品 |
| [RemoveBlockProtectField](世界/游戏规则.md#removeblockprotectfield) | <span style="display:inline;color:#ff5555">Apollo</span> | 取消一个方块无法被玩家/实体破坏的区域 |
| [SetCanActorSetOnFireByLightning](世界/游戏规则.md#setcanactorsetonfirebylightning) | <span style="display:inline;color:#ff5555">服务端</span> | 禁止/允许闪电点燃实体 |
| [SetCanBlockSetOnFireByLightning](世界/游戏规则.md#setcanblocksetonfirebylightning) | <span style="display:inline;color:#ff5555">服务端</span> | 禁止/允许闪电点燃方块 |
| [SetDefaultGameType](世界/游戏规则.md#setdefaultgametype) | <span style="display:inline;color:#ff5555">服务端</span> | 设置默认游戏模式 |
| [SetDisableCommandMinecart](世界/游戏规则.md#setdisablecommandminecart) | <span style="display:inline;color:#ff5555">服务端</span> | 设置停止/开启运行命令方块矿车内置逻辑指令，当前仅Apollo网络服可用 |
| [SetDisableContainers](世界/游戏规则.md#setdisablecontainers) | <span style="display:inline;color:#ff5555">服务端</span> | 禁止所有容器界面的打开，包括玩家背包，各种包含背包界面的容器方块如工作台与箱子，以及包含背包界面的实体交互如马背包与村民交易 |
| [SetDisableDropItem](世界/游戏规则.md#setdisabledropitem) | <span style="display:inline;color:#ff5555">服务端</span> | 设置禁止丢弃物品 |
| [SetDisableGravityInLiquid](世界/游戏规则.md#setdisablegravityinliquid) | <span style="display:inline;color:#ff5555">服务端</span> | 是否屏蔽所有实体在液体（水、岩浆）中的重力 |
| [SetDisableHunger](世界/游戏规则.md#setdisablehunger) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否屏蔽饥饿度 |
| [SetGameDifficulty](世界/游戏规则.md#setgamedifficulty) | <span style="display:inline;color:#ff5555">服务端</span> | 设置游戏难度 |
| [SetGameRulesInfoServer](世界/游戏规则.md#setgamerulesinfoserver) | <span style="display:inline;color:#ff5555">服务端</span> | 设置游戏规则。所有参数均可选。 |
| [SetHurtCD](世界/游戏规则.md#sethurtcd) | <span style="display:inline;color:#ff5555">服务端</span> | 设置全局受击间隔CD |
| [SetLevelGravity](世界/游戏规则.md#setlevelgravity) | <span style="display:inline;color:#ff5555">服务端</span> | 设置重力因子 |
| [SetPistonMaxInteractionCount](世界/游戏规则.md#setpistonmaxinteractioncount) | <span style="display:inline;color:#ff5555">服务端</span> | 设置活塞/粘性活塞最多推动的方块数量，默认为12个方块。该设置不存档。 |
#### 自定义数据
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CleanExtraData](世界/自定义数据.md#cleanextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 清除实体的自定义数据或者世界的自定义数据，清除实体数据时使用对应实体id创建组件，清除世界数据时使用levelId创建组件 |
| [GetExtraData](世界/自定义数据.md#getextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的自定义数据或者世界的自定义数据，某个键所对应的值。获取实体数据时使用对应实体id创建组件，获取世界数据时使用levelId创建组件 |
| [GetWholeExtraData](世界/自定义数据.md#getwholeextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 获取完整的实体的自定义数据或者世界的自定义数据，获取实体数据时使用对应实体id创建组件，获取世界数据时使用levelId创建组件 |
| [SaveExtraData](世界/自定义数据.md#saveextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 用于保存实体的自定义数据或者世界的自定义数据 |
| [SetExtraData](世界/自定义数据.md#setextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 用于设置实体的自定义数据或者世界的自定义数据，数据以键值对的形式保存。设置实体数据时使用对应实体id创建组件，设置世界数据时使用levelId创建组件 |
#### 指令
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetCommandPermissionLevel](世界/指令.md#getcommandpermissionlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 返回设定使用/op命令时OP的权限等级（对应server.properties中的op-permission-level配置） |
| [GetDefaultPlayerPermissionLevel](世界/指令.md#getdefaultplayerpermissionlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 返回新玩家加入时的权限身份（对应server.properties中的default-player-permission-level配置） |
| [SetCommand](世界/指令.md#setcommand) | <span style="display:inline;color:#ff5555">服务端</span> | 使用游戏内指令 |
| [SetCommandPermissionLevel](世界/指令.md#setcommandpermissionlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 设置当玩家使用/op命令时OP的权限等级（对应server.properties中的op-permission-level配置） |
| [SetDefaultPlayerPermissionLevel](世界/指令.md#setdefaultplayerpermissionlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 设置新玩家加入时的权限身份（对应server.properties中的default-player-permission-level配置） |
#### 消息
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [NotifyOneMessage](世界/消息.md#notifyonemessage) | <span style="display:inline;color:#ff5555">服务端</span> | 给指定玩家发送聊天框消息 |
| [SendMsg](世界/消息.md#sendmsg) | <span style="display:inline;color:#ff5555">服务端</span> | 模拟玩家给所有人发送聊天栏消息 |
| [SendMsgToPlayer](世界/消息.md#sendmsgtoplayer) | <span style="display:inline;color:#ff5555">服务端</span> | 模拟玩家给另一个玩家发送聊天栏消息 |
| [SetLeftCornerNotify](世界/消息.md#setleftcornernotify) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端设置左上角通知信息 |
| [SetNotifyMsg](世界/消息.md#setnotifymsg) | <span style="display:inline;color:#ff5555">服务端</span> | 设置消息通知 |
| [SetOnePopupNotice](世界/消息.md#setonepopupnotice) | <span style="display:inline;color:#ff5555">服务端</span> | 在具体某个玩家的物品栏上方弹出popup类型通知，位置位于tip类型消息下方，此功能更建议客户端使用game组件的对应接口SetPopupNotice |
| [SetOneTipMessage](世界/消息.md#setonetipmessage) | <span style="display:inline;color:#ff5555">服务端</span> | 在具体某个玩家的物品栏上方弹出tip类型通知，位置位于popup类型通知上方，此功能更建议在客户端使用game组件的对应接口SetTipMessage |
| [SetPopupNotice](世界/消息.md#setpopupnotice) | <span style="display:inline;color:#ff5555">服务端</span> | 在所有玩家物品栏上方弹出popup类型通知，位置位于tip类型消息下方 |
| [SetPopupNotice](世界/消息.md#setpopupnotice) | <span style="display:inline;color:#7575f9">客户端</span> | 在本地玩家的物品栏上方弹出popup类型通知，位置位于tip类型消息下方 |
| [SetPopupState](世界/消息.md#setpopupstate) | <span style="display:inline;color:#7575f9">客户端</span> | 设置Popup消息栏状态 |
| [SetTipMessage](世界/消息.md#settipmessage) | <span style="display:inline;color:#ff5555">服务端</span> | 在所有玩家物品栏上方弹出tip类型通知，位置位于popup类型通知上方 |
| [SetTipMessage](世界/消息.md#settipmessage) | <span style="display:inline;color:#7575f9">客户端</span> | 在本地玩家的物品栏上方弹出tip类型通知，位置位于popup类型通知上方 |
#### 记分板
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetAllPlayerScoreboardObjects](世界/记分板.md#getallplayerscoreboardobjects) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家记分项 |
| [GetAllPlayerScoreboardObjects](世界/记分板.md#getallplayerscoreboardobjects) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家记分项 |
| [GetAllScoreboardObjects](世界/记分板.md#getallscoreboardobjects) | <span style="display:inline;color:#ff5555">服务端</span> | 获取所有记分板项 |
| [GetAllScoreboardObjects](世界/记分板.md#getallscoreboardobjects) | <span style="display:inline;color:#7575f9">客户端</span> | 获取所有记分板项 |
#### 行为
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [UseItemAttackEntity](世界/行为.md#useitemattackentity) | <span style="display:inline;color:#ff5555">服务端</span> | 使用指定物品攻击某个实体。 |
#### 实体类型
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetEngineType](实体/实体类型.md#getenginetype) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体类型，主要用于判断实体是否属于某一类型的生物。 |
| [GetEngineType](实体/实体类型.md#getenginetype) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体类型，主要用于判断实体是否属于某一类型的生物。 |
| [GetEngineTypeStr](实体/实体类型.md#getenginetypestr) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的类型名称 |
| [GetEngineTypeStr](实体/实体类型.md#getenginetypestr) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体的类型名称 |
| [GetEntityDefinitions](实体/实体类型.md#getentitydefinitions) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的命名空间ID及其当前和之前的定义组件群 |
| [GetEntityNBTTags](实体/实体类型.md#getentitynbttags) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的NBT标签 |
#### 附加值
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetAuxValue](实体/附加值.md#getauxvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 获取射出的弓箭或投掷出的药水的附加值 |
| [GetAuxValue](实体/附加值.md#getauxvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 获取射出的弓箭或投掷出的药水的附加值 |
#### 属性
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [ChangeEntityDimension](实体/属性.md#changeentitydimension) | <span style="display:inline;color:#ff5555">服务端</span> | 传送实体 |
| [GetAllComponentsName](实体/属性.md#getallcomponentsname) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体所拥有的原版组件list |
| [GetAttrMaxValue](实体/属性.md#getattrmaxvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的引擎属性的最大值 |
| [GetAttrMaxValue](实体/属性.md#getattrmaxvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 获取属性最大值，包括生命值，饥饿度，移速等 |
| [GetAttrValue](实体/属性.md#getattrvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的引擎属性 |
| [GetAttrValue](实体/属性.md#getattrvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 获取属性值，包括生命值，饥饿度，移速 |
| [GetBodyRot](实体/属性.md#getbodyrot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体的身体的角度 |
| [GetCurrentAirSupply](实体/属性.md#getcurrentairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 生物当前氧气储备值 |
| [GetCurrentAirSupply](实体/属性.md#getcurrentairsupply) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家当前氧气储备值 |
| [GetDeathTime](实体/属性.md#getdeathtime) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物死亡后持续的时间（刻，1秒20刻），用于控制死亡动画。0表示生物未死亡。 |
| [GetEntitiesBySelector](实体/属性.md#getentitiesbyselector) | <span style="display:inline;color:#ff5555">服务端</span> | 传入目标选择器，获取对应实体id (最大范围是所有已加载的实体) |
| [GetEntityDamage](实体/属性.md#getentitydamage) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物(包括玩家)的攻击力 |
| [GetEntityDimensionId](实体/属性.md#getentitydimensionid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体所在维度 |
| [GetEntityFallDistance](实体/属性.md#getentityfalldistance) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的坠落高度，越大的值会给予实体更大的坠落伤害，建议在[OnGroundServerEvent](实体/../../事件/实体.md#ongroundserverevent)事件中调用 |
| [GetEntityLinksTag](实体/属性.md#getentitylinkstag) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体相连接的实体，如获取entityId为马，会返回骑乘者的信息 |
| [GetEntityOwner](实体/属性.md#getentityowner) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的属主（包括可驯服生物的主人，或者掉落物的丢弃者，弹射物的发射者等） |
| [GetFootPos](实体/属性.md#getfootpos) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体脚所在的位置 |
| [GetFootPos](实体/属性.md#getfootpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体脚所在的位置 |
| [GetGravity](实体/属性.md#getgravity) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的重力因子，当生物重力因子为0时则应用世界的重力因子 |
| [GetLoadActors](实体/属性.md#getloadactors) | <span style="display:inline;color:#ff5555">服务端</span> | 获取已加载的实体id |
| [GetMarkVariant](实体/属性.md#getmarkvariant) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的标记变种属性值 |
| [GetMaxAirSupply](实体/属性.md#getmaxairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物最大氧气储备值 |
| [GetMaxAirSupply](实体/属性.md#getmaxairsupply) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家最大氧气储备值 |
| [GetMobColor](实体/属性.md#getmobcolor) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物的颜色，截止至网易2.9版本，只对羊和热带鱼有效 |
| [GetMobStrength](实体/属性.md#getmobstrength) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物的强度，截止至网易2.9版本，只对羊驼有效，强度越大羊驼驮运的箱子时格子数量越多 |
| [GetMobStrengthMax](实体/属性.md#getmobstrengthmax) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物强度的最大值，截止至网易2.9版本，只对羊驼有效，强度越大羊驼驮运的箱子时格子数量越多，[SetMobStrength](实体/属性.md#setstrength)无法超过SetMobStrengthMax的值 |
| [GetName](实体/属性.md#getname) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物的自定义名称（即使用命名牌或者SetName接口设置的名称），或者玩家的名字。 |
| [GetName](实体/属性.md#getname) | <span style="display:inline;color:#7575f9">客户端</span> | 获取生物的自定义名称（即使用命名牌或者SetName接口设置的名称），或者玩家的名字。 |
| [GetPos](实体/属性.md#getpos) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体位置 |
| [GetPos](实体/属性.md#getpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体位置 |
| [GetRiderId](实体/属性.md#getriderid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家坐骑entityid |
| [GetRot](实体/属性.md#getrot) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体头与水平方向的俯仰角度和竖直方向的旋转角度，获得角度后可用GetDirFromRot接口转换为朝向的单位向量 <a href="../../../mcguide/20-玩法开发/10-基本概念/10-Vector3.html">MC坐标系说明</a> |
| [GetRot](实体/属性.md#getrot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体头与水平方向的俯仰角度和竖直方向的旋转角度，获得角度后可用GetDirFromRot接口转换为朝向的单位向量 <a href="../../../mcguide/20-玩法开发/10-基本概念/10-Vector3.html">MC坐标系说明</a> |
| [GetSize](实体/属性.md#getsize) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的包围盒 |
| [GetSize](实体/属性.md#getsize) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体的包围盒 |
| [GetTradeLevel](实体/属性.md#gettradelevel) | <span style="display:inline;color:#ff5555">服务端</span> | 获取村民的交易等级 |
| [GetTypeFamily](实体/属性.md#gettypefamily) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物行为包字段 type_family |
| [GetUnitBubbleAirSupply](实体/属性.md#getunitbubbleairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 单位气泡数对应的氧气储备值 |
| [GetVariant](实体/属性.md#getvariant) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的变种属性值 |
| [HasChest](实体/属性.md#haschest) | <span style="display:inline;color:#ff5555">服务端</span> | 判断生物是否背负了箱子，截止至网易2.9版本，只对羊驼、驴、骡生效 |
| [HasComponent](实体/属性.md#hascomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 判断实体是否有原版组件 |
| [HasSaddle](实体/属性.md#hassaddle) | <span style="display:inline;color:#ff5555">服务端</span> | 判断实体是否装备了鞍 |
| [IsAngry](实体/属性.md#isangry) | <span style="display:inline;color:#ff5555">服务端</span> | 判断实体是否处于激怒状态 |
| [IsBaby](实体/属性.md#isbaby) | <span style="display:inline;color:#ff5555">服务端</span> | 判断实体是否为幼年 |
| [IsConsumingAirSupply](实体/属性.md#isconsumingairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物当前是否在消耗氧气 |
| [IsIllagerCaptain](实体/属性.md#isillagercaptain) | <span style="display:inline;color:#ff5555">服务端</span> | 判断实体是否为袭击队长，截止至网易2.9版本，只对掠夺者和卫道士有效 |
| [IsNaturallySpawned](实体/属性.md#isnaturallyspawned) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物是否为自然生成的 |
| [IsOutOfControl](实体/属性.md#isoutofcontrol) | <span style="display:inline;color:#ff5555">服务端</span> | 判断实体是否处于失控状态，截止至网易2.9版本，只对船有效 |
| [IsPregnant](实体/属性.md#ispregnant) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物是否怀孕，截止至网易2.9版本，只对海龟有效 |
| [IsSheared](实体/属性.md#issheared) | <span style="display:inline;color:#ff5555">服务端</span> | 判断实体是否被剃毛，截止至网易2.9版本，只对羊有效 |
| [IsSitting](实体/属性.md#issitting) | <span style="display:inline;color:#ff5555">服务端</span> | 判断实体是否处于坐下状态 |
| [IsTamed](实体/属性.md#istamed) | <span style="display:inline;color:#ff5555">服务端</span> | 判断实体是否被驯服 |
| [LockLocalPlayerRot](实体/属性.md#locklocalplayerrot) | <span style="display:inline;color:#7575f9">客户端</span> | 在分离摄像机时，锁定本地玩家的头部角度 |
| [PromoteToIllagerCaptain](实体/属性.md#promotetoillagercaptain) | <span style="display:inline;color:#ff5555">服务端</span> | 晋升实体为袭击队长，截止至网易2.9版本，只对掠夺者和卫道士有效 |
| [ResetToDefaultValue](实体/属性.md#resettodefaultvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 重置实体引擎属性到默认值 |
| [ResetToMaxValue](实体/属性.md#resettomaxvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 重置实体引擎属性到最大值 |
| [SetAngry](实体/属性.md#setangry) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否处于激怒状态 |
| [SetAsAdult](实体/属性.md#setasadult) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体为成年体 |
| [SetAttrMaxValue](实体/属性.md#setattrmaxvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的引擎属性的最大值 |
| [SetAttrValue](实体/属性.md#setattrvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的引擎属性 |
| [SetChest](实体/属性.md#setchest) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物是否背负了箱子，截止至网易2.9版本，只对羊驼、驴、骡生效 |
| [SetCurrentAirSupply](实体/属性.md#setcurrentairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物氧气储备值 |
| [SetEntityLookAtPos](实体/属性.md#setentitylookatpos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置非玩家的实体看向某个位置 |
| [SetEntityOwner](实体/属性.md#setentityowner) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的属主（包括可驯服生物的主人，或者掉落物的丢弃者，弹射物的发射者等） |
| [SetFootPos](实体/属性.md#setfootpos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体脚底所在的位置 |
| [SetGravity](实体/属性.md#setgravity) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的重力因子，当生物重力因子为0时则应用世界的重力因子 |
| [SetMarkVariant](实体/属性.md#setmarkvariant) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的标记变种属性值 |
| [SetMaxAirSupply](实体/属性.md#setmaxairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物最大氧气储备值 |
| [SetMobColor](实体/属性.md#setmobcolor) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物的颜色，截止至网易2.9版本，只对羊和热带鱼有效 |
| [SetMobStrength](实体/属性.md#setmobstrength) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物的强度，截止至网易2.9版本，只对羊驼有效，强度越大羊驼驮运的箱子时格子数量越多 |
| [SetMobStrengthMax](实体/属性.md#setmobstrengthmax) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物强度的最大值，截止至网易2.9版本，只对羊驼有效，强度越大羊驼驮运的箱子时格子数量越多，[SetMobStrength](实体/属性.md#setmobstrength)无法超过SetMobStrengthMax的值。由于引擎限制，在羊驼被打时候会reload组件，strengthMax会恢复成llama.json中的配置值(minecraft:strength) |
| [SetName](实体/属性.md#setname) | <span style="display:inline;color:#ff5555">服务端</span> | 用于设置生物的自定义名称，跟原版命名牌作用相同，玩家和新版流浪商人暂不支持 |
| [SetOutOfControl](实体/属性.md#setoutofcontrol) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否处于失控状态，截止至网易2.9版本，只对船有效 |
| [SetPersistent](实体/属性.md#setpersistent) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体不会因为离玩家太远而被[清除](https://zh.minecraft.wiki/w/%E7%94%9F%E6%88%90#%E6%B8%85%E9%99%A4) |
| [SetPlayerLookAtPos](实体/属性.md#setplayerlookatpos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置本地玩家看向某个位置 |
| [SetPos](实体/属性.md#setpos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体位置 |
| [SetRecoverTotalAirSupplyTime](实体/属性.md#setrecovertotalairsupplytime) | <span style="display:inline;color:#ff5555">服务端</span> | 设置恢复最大氧气量的时间，单位秒 |
| [SetRot](实体/属性.md#setrot) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体头与水平方向的俯仰角度和竖直方向的旋转角度 <a href="../../../mcguide/20-玩法开发/10-基本概念/10-Vector3.html">MC坐标系说明</a> |
| [SetRot](实体/属性.md#setrot) | <span style="display:inline;color:#7575f9">客户端</span> | 设置实体头与水平方向的俯仰角度和竖直方向的旋转角度 <a href="../../../mcguide/20-玩法开发/10-基本概念/10-Vector3.html">MC坐标系说明</a> |
| [SetSheared](实体/属性.md#setsheared) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否被剃毛，截止至网易2.9版本，只对羊有效 |
| [SetSitting](实体/属性.md#setsitting) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物是否坐下 |
| [SetSize](实体/属性.md#setsize) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的包围盒。设置过大会导致游戏卡顿。实体的scale的立方乘以包围盒的体积不可超过32768 |
| [SetTradeLevel](实体/属性.md#settradelevel) | <span style="display:inline;color:#ff5555">服务端</span> | 设置村民的交易等级 |
| [SetVariant](实体/属性.md#setvariant) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的变种属性值 |
| [isEntityInLava](实体/属性.md#isentityinlava) | <span style="display:inline;color:#7575f9">客户端</span> | 实体是否在岩浆中 |
| [isEntityOnGround](实体/属性.md#isentityonground) | <span style="display:inline;color:#7575f9">客户端</span> | 实体是否触地 |
#### 行为<span id = "行为1"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddActorComponent](实体/行为.md#addactorcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 给指定实体自定义添加实体Component |
| [AddActorComponentGroup](实体/行为.md#addactorcomponentgroup) | <span style="display:inline;color:#ff5555">服务端</span> | 给指定实体添加实体json中配置的ComponentGroup |
| [AddEntityAroundEntityMotion](实体/行为.md#addentityaroundentitymotion) | <span style="display:inline;color:#ff5555">服务端</span> | 给实体（不含玩家）添加对实体环绕运动器 |
| [AddEntityAroundPointMotion](实体/行为.md#addentityaroundpointmotion) | <span style="display:inline;color:#ff5555">服务端</span> | 给实体（不含玩家）添加对点环绕运动器 |
| [AddEntitySeat](实体/行为.md#addentityseat) | <span style="display:inline;color:#ff5555">服务端</span> | 增加坐骑座位 |
| [AddEntityTrackMotion](实体/行为.md#addentitytrackmotion) | <span style="display:inline;color:#ff5555">服务端</span> | 给实体（不含玩家）添加轨迹运动器 |
| [AddEntityVelocityMotion](实体/行为.md#addentityvelocitymotion) | <span style="display:inline;color:#ff5555">服务端</span> | 给实体（不含玩家）添加速度运动器 |
| [ChangeRiderSeat](实体/行为.md#changeriderseat) | <span style="display:inline;color:#ff5555">服务端</span> | 设置骑乘者在当前坐骑上的序号 |
| [DeleteEntitySeat](实体/行为.md#deleteentityseat) | <span style="display:inline;color:#ff5555">服务端</span> | 删除坐骑座位 |
| [GetAttackTarget](实体/行为.md#getattacktarget) | <span style="display:inline;color:#ff5555">服务端</span> | 获取仇恨目标 |
| [GetAttackTarget](实体/行为.md#getattacktarget) | <span style="display:inline;color:#7575f9">客户端</span> | 获取仇恨目标 |
| [GetBlockControlAi](实体/行为.md#getblockcontrolai) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物原生AI是否被屏蔽 |
| [GetComponents](实体/行为.md#getcomponents) | <span style="display:inline;color:#ff5555">服务端</span> | 获取指定实体的生效Components |
| [GetCustomGoalCls](实体/行为.md#getcustomgoalcls) | <span style="display:inline;color:#ff5555">服务端</span> | 用于获取服务器自定义行为节点的基类。实现新的行为节点时，需要继承该接口返回的类 |
| [GetEntityMotions](实体/行为.md#getentitymotions) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体（不含玩家）身上的所有运动器 |
| [GetJumpPower](实体/行为.md#getjumppower) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物跳跃力度，0.42表示正常水平 |
| [GetLeashHolder](实体/行为.md#getleashholder) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体被使用拴绳牵引时牵引者的ID |
| [GetMotion](实体/行为.md#getmotion) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物（含玩家）的瞬时移动方向向量 |
| [GetMotion](实体/行为.md#getmotion) | <span style="display:inline;color:#7575f9">客户端</span> | 获取生物的瞬时移动方向向量。与服务端不同，客户端不会计算摩擦等因素，获取到的是上一帧的向量，与服务器获取到的值会不相等 |
| [GetOwnerId](实体/行为.md#getownerid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取驯服生物的主人id |
| [GetOwnerId](实体/行为.md#getownerid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取驯服生物的主人id |
| [GetRiders](实体/行为.md#getriders) | <span style="display:inline;color:#ff5555">服务端</span> | 获取坐骑上的骑乘者信息 |
| [GetStepHeight](实体/行为.md#getstepheight) | <span style="display:inline;color:#ff5555">服务端</span> | 返回玩家前进非跳跃状态下能上的最大台阶高度 |
| [Hurt](实体/行为.md#hurt) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体伤害 |
| [ImmuneDamage](实体/行为.md#immunedamage) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否免疫伤害（该属性存档） |
| [IsEating](实体/行为.md#iseating) | <span style="display:inline;color:#ff5555">服务端</span> | 判断非玩家实体是否在进食 |
| [IsEntityOnFire](实体/行为.md#isentityonfire) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体是否着火 |
| [IsLootDropped](实体/行为.md#islootdropped) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物是否生成掉落物 |
| [IsPersistent](实体/行为.md#ispersistent) | <span style="display:inline;color:#ff5555">服务端</span> | 判断是否为持久性生物 |
| [IsRoaring](实体/行为.md#isroaring) | <span style="display:inline;color:#ff5555">服务端</span> | 判断是否处于咆哮状态，截止至网易2.9版本，仅对劫掠兽有效 |
| [IsStunned](实体/行为.md#isstunned) | <span style="display:inline;color:#ff5555">服务端</span> | 判断是否处于眩晕状态，截止至网易2.9版本，仅对劫掠兽有效 |
| [RemoveActorComponent](实体/行为.md#removeactorcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 删除指定实体的指定Component |
| [RemoveActorComponentGroup](实体/行为.md#removeactorcomponentgroup) | <span style="display:inline;color:#ff5555">服务端</span> | 移除指定实体在实体json中配置的ComponentGroup |
| [RemoveEntityMotion](实体/行为.md#removeentitymotion) | <span style="display:inline;color:#ff5555">服务端</span> | 移除实体（不含玩家）身上的运动器 |
| [ResetAttackTarget](实体/行为.md#resetattacktarget) | <span style="display:inline;color:#ff5555">服务端</span> | 清除仇恨目标 |
| [ResetMotion](实体/行为.md#resetmotion) | <span style="display:inline;color:#ff5555">服务端</span> | 重置生物（不含玩家）的瞬时移动方向向量 |
| [ResetStepHeight](实体/行为.md#resetstepheight) | <span style="display:inline;color:#ff5555">服务端</span> | 恢复引擎默认玩家前进非跳跃状态下能上的最大台阶高度 |
| [SetActorCollidable](实体/行为.md#setactorcollidable) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否可碰撞 |
| [SetActorPushable](实体/行为.md#setactorpushable) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否可推动 |
| [SetAttackTarget](实体/行为.md#setattacktarget) | <span style="display:inline;color:#ff5555">服务端</span> | 设置仇恨目标 |
| [SetBlockControlAi](实体/行为.md#setblockcontrolai) | <span style="display:inline;color:#ff5555">服务端</span> | 设置屏蔽生物原生AI |
| [SetCanOtherPlayerRide](实体/行为.md#setcanotherplayerride) | <span style="display:inline;color:#ff5555">服务端</span> | 设置其他玩家是否有权限骑乘，True表示每个玩家都能骑乘，False只有驯服者才能骑乘 |
| [SetControl](实体/行为.md#setcontrol) | <span style="display:inline;color:#ff5555">服务端</span> | 设置该生物无需装备鞍就可以控制行走跳跃 |
| [SetEntityInteractFilter](实体/行为.md#setentityinteractfilter) | <span style="display:inline;color:#ff5555">服务端</span> | 设置与生物可交互的条件 |
| [SetEntityLockRider](实体/行为.md#setentitylockrider) | <span style="display:inline;color:#ff5555">服务端</span> | 设置坐骑上的实体是否锁定序号 |
| [SetEntityOnFire](实体/行为.md#setentityonfire) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体着火 |
| [SetEntityRide](实体/行为.md#setentityride) | <span style="display:inline;color:#ff5555">服务端</span> | 驯服可骑乘生物 |
| [SetEntitySeat](实体/行为.md#setentityseat) | <span style="display:inline;color:#ff5555">服务端</span> | 设置坐骑座位的位置、旋转以及允许实体旋转范围 |
| [SetEntityShareablesItems](实体/行为.md#setentityshareablesitems) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物可分享/可拾取的物品列表 |
| [SetEntityTamed](实体/行为.md#setentitytamed) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物驯服，需要配合 entityEvent组件使用。该类驯服不包含骑乘功能。 |
| [SetJumpPower](实体/行为.md#setjumppower) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物跳跃力度，0.42表示正常水平 |
| [SetLeashHolder](实体/行为.md#setleashholder) | <span style="display:inline;color:#ff5555">服务端</span> | 为实体添加牵引者，与原版拴绳的作用相同，详见<a href="https://zh.minecraft.wiki/w/%E6%8B%B4%E7%BB%B3">基岩版栓绳介绍</a> |
| [SetLootDropped](实体/行为.md#setlootdropped) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物是否生成掉落物 |
| [SetMobKnockback](实体/行为.md#setmobknockback) | <span style="display:inline;color:#ff5555">服务端</span> | 设置击退的初始速度，需要考虑阻力的影响 |
| [SetMotion](实体/行为.md#setmotion) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物（不含玩家）的瞬时移动方向向量 |
| [SetMotion](实体/行为.md#setmotion) | <span style="display:inline;color:#7575f9">客户端</span> | 设置瞬时的移动方向向量，用于本地玩家 |
| [SetMoveSetting](实体/行为.md#setmovesetting) | <span style="display:inline;color:#ff5555">服务端</span> | 寻路组件 |
| [SetPersistence](实体/行为.md#setpersistence) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否持久化。 |
| [SetRidePos](实体/行为.md#setridepos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物骑乘位置 |
| [SetRiderRideEntity](实体/行为.md#setriderrideentity) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体骑乘生物（或者船与矿车） |
| [SetStepHeight](实体/行为.md#setstepheight) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家前进非跳跃状态下能上的最大台阶高度, 默认值为0.5625，1的话表示能上一个台阶 |
| [StartEntityMotion](实体/行为.md#startentitymotion) | <span style="display:inline;color:#ff5555">服务端</span> | 启动实体（不含玩家）身上的某个运动器 |
| [StopEntityMotion](实体/行为.md#stopentitymotion) | <span style="display:inline;color:#ff5555">服务端</span> | 停止实体（不含玩家）身上的某个运动器 |
| [StopEntityRiding](实体/行为.md#stopentityriding) | <span style="display:inline;color:#ff5555">服务端</span> | 强制骑乘者下坐骑。 |
| [TriggerCustomEvent](实体/行为.md#triggercustomevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发生物自定义事件 |
#### 状态效果
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddEffectToEntity](实体/状态效果.md#addeffecttoentity) | <span style="display:inline;color:#ff5555">服务端</span> | 为实体添加指定状态效果，如果添加的状态已存在则有以下集中情况：1、等级大于已存在则更新状态等级及持续时间；2、状态等级相等且剩余时间duration大于已存在则刷新剩余时间；3、等级小于已存在则不做修改；4、粒子效果以新的为准 |
| [GetAllEffects](实体/状态效果.md#getalleffects) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体当前所有状态效果 |
| [GetAllEffects](实体/状态效果.md#getalleffects) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体当前所有状态效果 |
| [GetLoadEffects](实体/状态效果.md#getloadeffects) | <span style="display:inline;color:#ff5555">服务端</span> | 获取所有已加载的状态效果 |
| [HasEffect](实体/状态效果.md#haseffect) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体是否存在当前状态效果 |
| [HasEffect](实体/状态效果.md#haseffect) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体是否存在当前状态效果 |
| [RemoveEffectFromEntity](实体/状态效果.md#removeeffectfromentity) | <span style="display:inline;color:#ff5555">服务端</span> | 为实体删除指定状态效果 |
#### 渲染<span id = "渲染1"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddActorAnimation](实体/渲染.md#addactoranimation) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物渲染动画 |
| [AddActorAnimationController](实体/渲染.md#addactoranimationcontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物渲染动画控制器 |
| [AddActorBlockGeometry](实体/渲染.md#addactorblockgeometry) | <span style="display:inline;color:#7575f9">客户端</span> | 为实体添加方块几何体模型。 |
| [AddActorGeometry](实体/渲染.md#addactorgeometry) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物渲染几何体 |
| [AddActorParticleEffect](实体/渲染.md#addactorparticleeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物特效资源 |
| [AddActorRenderController](实体/渲染.md#addactorrendercontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_7-自定义渲染控制器">渲染控制器</a> |
| [AddActorRenderControllerArray](实体/渲染.md#addactorrendercontrollerarray) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物渲染控制器列表中字典arrays元素 |
| [AddActorRenderMaterial](实体/渲染.md#addactorrendermaterial) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物渲染需要的<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_3-自定义材质">材质</a> |
| [AddActorScriptAnimate](实体/渲染.md#addactorscriptanimate) | <span style="display:inline;color:#7575f9">客户端</span> | 在生物的客户端实体定义（minecraft:client_entity）json中的scripts/animate节点添加动画/动画控制器 |
| [AddActorSoundEffect](实体/渲染.md#addactorsoundeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物音效资源 |
| [AddActorTexture](实体/渲染.md#addactortexture) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物渲染贴图 |
| [AddAnimationControllerToOneActor](实体/渲染.md#addanimationcontrollertooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 增加单个生物渲染动画控制器 |
| [AddAnimationToOneActor](实体/渲染.md#addanimationtooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 增加单个生物渲染动画 |
| [AddGeometryToOneActor](实体/渲染.md#addgeometrytooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 增加单个生物渲染几何体 |
| [AddParticleEffectToOneActor](实体/渲染.md#addparticleeffecttooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物特效资源 |
| [AddRenderControllerToOneActor](实体/渲染.md#addrendercontrollertooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 增加单个生物<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_7-自定义渲染控制器">的渲染控制器</a> |
| [AddRenderMaterialToOneActor](实体/渲染.md#addrendermaterialtooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 增加单个生物渲染需要的<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_3-自定义材质">材质</a> |
| [AddScriptAnimateToOneActor](实体/渲染.md#addscriptanimatetooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 在单个生物的客户端实体定义（minecraft:client_entity）json中的scripts/animate节点添加动画/动画控制器 |
| [AddSoundEffectToOneActor](实体/渲染.md#addsoundeffecttooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 增加单个生物的音效资源 |
| [AddTextureToOneActor](实体/渲染.md#addtexturetooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 增加单个生物的渲染贴图 |
| [BindEntityToEntity](实体/渲染.md#bindentitytoentity) | <span style="display:inline;color:#7575f9">客户端</span> | 绑定骨骼模型跟随其他entity,如果当前entity是本地玩家，摄像机也跟随其他entity |
| [ClearActorBlockGeometry](实体/渲染.md#clearactorblockgeometry) | <span style="display:inline;color:#7575f9">客户端</span> | 删除实体中所有的方块几何体模型。 |
| [CopyActorGeometryFromPlayer](实体/渲染.md#copyactorgeometryfromplayer) | <span style="display:inline;color:#7575f9">客户端</span> | 将渲染几何体从某个玩家拷贝到某类生物identifier上 |
| [CopyActorRenderMaterialFromPlayer](实体/渲染.md#copyactorrendermaterialfromplayer) | <span style="display:inline;color:#7575f9">客户端</span> | 将渲染<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_3-自定义材质">材质</a>从某个玩家拷贝到某类生物identifier上 |
| [CopyActorTextureFromPlayer](实体/渲染.md#copyactortexturefromplayer) | <span style="display:inline;color:#7575f9">客户端</span> | 将贴图从某个玩家拷贝到某类生物identifier上 |
| [CopyPlayerGeometryToOneActor](实体/渲染.md#copyplayergeometrytooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 将渲染几何体从某个玩家拷贝到某个生物上 |
| [CopyPlayerRenderMaterialToOneActor](实体/渲染.md#copyplayerrendermaterialtooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 将渲染<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_3-自定义材质">材质</a>从某个玩家拷贝到某个生物上 |
| [CopyPlayerTextureToOneActor](实体/渲染.md#copyplayertexturetooneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 将贴图从某个玩家拷贝到某个生物上 |
| [DeleteActorBlockGeometry](实体/渲染.md#deleteactorblockgeometry) | <span style="display:inline;color:#7575f9">客户端</span> | 删除实体中指定方块几何体模型。 |
| [GetActorRenderParams](实体/渲染.md#getactorrenderparams) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体（包括玩家）渲染参数 |
| [GetEntityExtraUniforms](实体/渲染.md#getentityextrauniforms) | <span style="display:inline;color:#7575f9">客户端</span> | 获取在实体shader当中使用的自定义变量的值。该自定义变量包含EXTRA_ACTOR_UNIFORM1,EXTRA_ACTOR_UNIFORM2,EXTRA_ACTOR_UNIFORM3,EXTRA_ACTOR_UNIFORM4，总共4组，每组为一个vec4(float, float, float ,float)类型的向量。 |
| [GetEntityRenderDistance](实体/渲染.md#getentityrenderdistance) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家的实体可渲染距离。玩家周围的实体指这个区块内的实体，也包含玩家自身。实体的渲染距离指，实体的位置到玩家相机位置的距离。可渲染距离指，如果实体的渲染距离在可渲染距离之内，则实体会被渲染出来，如果在距离以外，则实体不会被渲染出来。仅对本地玩家有效。 |
| [GetEntityUIExtraUniforms](实体/渲染.md#getentityuiextrauniforms) | <span style="display:inline;color:#7575f9">客户端</span> | 获取在实体shader当中使用的UI自定义变量的值，该变量可在微软UI纸娃娃（paperdoll）及网易版纸娃娃（neteasepaperdoll)上使用identifier渲染某一类生物实体时使用。该自定义变量包含EXTRA_ACTOR_UNIFORM1,EXTRA_ACTOR_UNIFORM2,EXTRA_ACTOR_UNIFORM3,EXTRA_ACTOR_UNIFORM4，总共4组，每组为一个vec4(float, float, float ,float)类型的向量。 |
| [GetNotRenderAtAll](实体/渲染.md#getnotrenderatall) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体是否不渲染 |
| [IsShowName](实体/渲染.md#isshowname) | <span style="display:inline;color:#7575f9">客户端</span> | 获取生物名字是否按照默认游戏逻辑显示（包括玩家） |
| [RebuildActorRender](实体/渲染.md#rebuildactorrender) | <span style="display:inline;color:#7575f9">客户端</span> | 重建生物的数据渲染器（该接口不支持玩家，玩家请使用RebuildPlayerRender） |
| [RebuildRenderForOneActor](实体/渲染.md#rebuildrenderforoneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 使用完entity类渲染接口后，重建单个生物渲染控制器（该接口不支持玩家，玩家请使用RebuildPlayerRender） |
| [RemoveActorAnimationController](实体/渲染.md#removeactoranimationcontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 移除生物渲染动画控制器 |
| [RemoveActorGeometry](实体/渲染.md#removeactorgeometry) | <span style="display:inline;color:#7575f9">客户端</span> | 删除生物渲染几何体 |
| [RemoveActorRenderController](实体/渲染.md#removeactorrendercontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 删除生物<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_7-自定义渲染控制器">渲染控制器</a> |
| [RemoveActorTexture](实体/渲染.md#removeactortexture) | <span style="display:inline;color:#7575f9">客户端</span> | 删除生物渲染贴图 |
| [RemoveAnimationControllerForOneActor](实体/渲染.md#removeanimationcontrollerforoneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 移除单个生物渲染动画控制器 |
| [RemoveGeometryForOneActor](实体/渲染.md#removegeometryforoneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 删除单个生物的渲染几何体 |
| [RemoveRenderControllerForOneActor](实体/渲染.md#removerendercontrollerforoneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 删除单个生物<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_7-自定义渲染控制器">的渲染控制器</a> |
| [RemoveTextureForOneActor](实体/渲染.md#removetextureforoneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 删除单个生物的渲染贴图 |
| [ResetActorRender](实体/渲染.md#resetactorrender) | <span style="display:inline;color:#7575f9">客户端</span> | 重置实体渲染接口，包括动画、动画控制器、渲染控制器、贴图、材质、特效资源、音效资源等。 |
| [ResetBindEntity](实体/渲染.md#resetbindentity) | <span style="display:inline;color:#7575f9">客户端</span> | 取消目标entity的绑定实体，取消后不再跟随任何其他entity |
| [ResetRenderForOneActor](实体/渲染.md#resetrenderforoneactor) | <span style="display:inline;color:#7575f9">客户端</span> | 将调用OneActor类渲染接口(CopyPlayerTextureToOneActor、CopyPlayerRenderMaterialToOneActor等)的生物重置回种群 |
| [SetActorAllBlockGeometryVisible](实体/渲染.md#setactorallblockgeometryvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 设置实体中所有的方块几何体模型是否显示。 |
| [SetActorBlockGeometryVisible](实体/渲染.md#setactorblockgeometryvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 设置实体中指定的方块几何体模型是否显示。 |
| [SetAlwaysShowName](实体/渲染.md#setalwaysshowname) | <span style="display:inline;color:#7575f9">客户端</span> | 设置生物名字是否一直显示，瞄准点不指向生物时也能显示 |
| [SetColor](实体/渲染.md#setcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 设置血条的颜色及背景色 |
| [SetEntityExtraUniforms](实体/渲染.md#setentityextrauniforms) | <span style="display:inline;color:#7575f9">客户端</span> | 设置可在实体shader当中使用的自定义变量的值。该自定义变量总共可设置EXTRA_ACTOR_UNIFORM1,EXTRA_ACTOR_UNIFORM2,EXTRA_ACTOR_UNIFORM3,EXTRA_ACTOR_UNIFORM4，总共4组，每组为一个vec4(float, float, float ,float)类型的向量，向量的默认值为(1.0,1.0,1.0,1.0)。 |
| [SetEntityRenderDistance](实体/渲染.md#setentityrenderdistance) | <span style="display:inline;color:#7575f9">客户端</span> | 设置玩家周围的实体的可渲染距离。玩家周围的实体指这个区块内的实体，也包含玩家自身。实体的渲染距离指，实体的位置到玩家相机位置的距离。可渲染距离指，如果实体的渲染距离在可渲染距离之内，则实体会被渲染出来，如果在距离以外，则实体不会被渲染出来。仅对本地玩家有效。 |
| [SetEntityUIExtraUniforms](实体/渲染.md#setentityuiextrauniforms) | <span style="display:inline;color:#7575f9">客户端</span> | 设置可在实体shader当中使用的UI自定义变量的值，可在微软UI纸娃娃（paperdoll）及网易版纸娃娃（neteasepaperdoll)上使用identifier渲染某一类生物实体时使用。该自定义变量总共可设置EXTRA_ACTOR_UNIFORM1,EXTRA_ACTOR_UNIFORM2,EXTRA_ACTOR_UNIFORM3,EXTRA_ACTOR_UNIFORM4，总共4组，每组为一个vec4(float, float, float ,float)类型的向量，向量的默认值为(1.0,1.0,1.0,1.0)。 |
| [SetHealthBarDeviation](实体/渲染.md#sethealthbardeviation) | <span style="display:inline;color:#7575f9">客户端</span> | 设置某个entity血条的相对高度 |
| [SetNameDeeptest](实体/渲染.md#setnamedeeptest) | <span style="display:inline;color:#7575f9">客户端</span> | 设置名字是否透视 |
| [SetNotRenderAtAll](实体/渲染.md#setnotrenderatall) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否关闭实体渲染 |
| [SetRenderLocalPlayer](实体/渲染.md#setrenderlocalplayer) | <span style="display:inline;color:#7575f9">客户端</span> | 设置本地玩家是否渲染 |
| [SetShowName](实体/渲染.md#setshowname) | <span style="display:inline;color:#7575f9">客户端</span> | 设置生物名字是否按照默认游戏逻辑显示（包括玩家） |
| [ShowHealth](实体/渲染.md#showhealth) | <span style="display:inline;color:#7575f9">客户端</span> | 设置某个entity是否显示血条，默认为显示 |
| [ShowHealthBar](实体/渲染.md#showhealthbar) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否显示血条 |
#### 背包
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetEntityItem](实体/背包.md#getentityitem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物物品，支持获取背包，盔甲栏，副手以及主手物品 |
| [GetEquItemEnchant](实体/背包.md#getequitemenchant) | <span style="display:inline;color:#ff5555">服务端</span> | 获取装备槽位中盔甲的附魔 |
| [GetEquItemModEnchant](实体/背包.md#getequitemmodenchant) | <span style="display:inline;color:#ff5555">服务端</span> | 获取装备槽位中盔甲的自定义附魔 |
| [SetEntityItem](实体/背包.md#setentityitem) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物物品，建议开发者根据生物特性来进行设置，部分生物设置装备后可能不显示但是死亡后仍然会掉落所设置的装备 |
#### 自定义属性
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetAttr](实体/自定义属性.md#getattr) | <span style="display:inline;color:#ff5555">服务端</span> | 获取SetAttr设置的属性值 |
| [GetAttr](实体/自定义属性.md#getattr) | <span style="display:inline;color:#7575f9">客户端</span> | 获取SetAttr设置的属性值 |
| [RegisterUpdateFunc](实体/自定义属性.md#registerupdatefunc) | <span style="display:inline;color:#7575f9">客户端</span> | 注册属性值变换时的回调函数，当属性变化时会调用该函数 |
| [SaveAttr](实体/自定义属性.md#saveattr) | <span style="display:inline;color:#ff5555">服务端</span> | 保存SetAttr设置的属性值 |
| [SetAttr](实体/自定义属性.md#setattr) | <span style="display:inline;color:#ff5555">服务端</span> | 设置属性值。服务端设置后会自动同步到客户端，可以用客户端的GetAttr获取。默认不会存档，需要存档的话可以设置needRestore=True。 |
| [SetAttr](实体/自定义属性.md#setattr) | <span style="display:inline;color:#7575f9">客户端</span> | 设置客户端属性值 |
| [UnRegisterUpdateFunc](实体/自定义属性.md#unregisterupdatefunc) | <span style="display:inline;color:#7575f9">客户端</span> | 反注册属性值变换时的回调函数 |
#### 自定义数据<span id = "自定义数据1"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CleanExtraData](实体/自定义数据.md#cleanextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 清除实体的自定义数据或者世界的自定义数据，清除实体数据时使用对应实体id创建组件，清除世界数据时使用levelId创建组件 |
| [GetExtraData](实体/自定义数据.md#getextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的自定义数据或者世界的自定义数据，某个键所对应的值。获取实体数据时使用对应实体id创建组件，获取世界数据时使用levelId创建组件 |
| [GetWholeExtraData](实体/自定义数据.md#getwholeextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 获取完整的实体的自定义数据或者世界的自定义数据，获取实体数据时使用对应实体id创建组件，获取世界数据时使用levelId创建组件 |
| [SaveExtraData](实体/自定义数据.md#saveextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 用于保存实体的自定义数据或者世界的自定义数据 |
| [SetExtraData](实体/自定义数据.md#setextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 用于设置实体的自定义数据或者世界的自定义数据，数据以键值对的形式保存。设置实体数据时使用对应实体id创建组件，设置世界数据时使用levelId创建组件 |
#### molang
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [EvalMolangExpression](实体/molang.md#evalmolangexpression) | <span style="display:inline;color:#ff5555">服务端</span> | 在实体上下文上执行molang表达式 |
| [EvalMolangExpression](实体/molang.md#evalmolangexpression) | <span style="display:inline;color:#7575f9">客户端</span> | 在实体上下文上执行molang表达式 |
| [Get](实体/molang.md#get) | <span style="display:inline;color:#7575f9">客户端</span> | 获取某一个实体计算节点的值，如果不存在返回注册时的默认值 |
| [GetAllProperties](实体/molang.md#getallproperties) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体属性列表 |
| [GetMolangValue](实体/molang.md#getmolangvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体molang变量的值 |
| [GetStringHash64](实体/molang.md#getstringhash64) | <span style="display:inline;color:#7575f9">客户端</span> | 返回字符串变量的hash64 |
| [Register](实体/molang.md#register) | <span style="display:inline;color:#7575f9">客户端</span> | 注册实体计算节点 |
| [Set](实体/molang.md#set) | <span style="display:inline;color:#7575f9">客户端</span> | 设置某一个实体计算节点的值 |
| [SetPropertyValue](实体/molang.md#setpropertyvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体属性的值 |
| [UnRegister](实体/molang.md#unregister) | <span style="display:inline;color:#7575f9">客户端</span> | 注销实体计算节点 |
#### 标签
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddEntityTag](实体/标签.md#addentitytag) | <span style="display:inline;color:#ff5555">服务端</span> | 增加实体标签 |
| [EntityHasTag](实体/标签.md#entityhastag) | <span style="display:inline;color:#ff5555">服务端</span> | 判断实体是否存在某个指定的标签 |
| [GetEntityTags](实体/标签.md#getentitytags) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体标签列表 |
| [RemoveEntityTag](实体/标签.md#removeentitytag) | <span style="display:inline;color:#ff5555">服务端</span> | 移除实体某个指定的标签 |
#### 抛射物
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetSourceEntityId](实体/抛射物.md#getsourceentityid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取抛射物发射者实体id |
#### 经验球
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetOrbExperience](实体/经验球.md#getorbexperience) | <span style="display:inline;color:#ff5555">服务端</span> | 获取经验球的经验 |
| [SetOrbExperience](实体/经验球.md#setorbexperience) | <span style="display:inline;color:#ff5555">服务端</span> | 设置经验球经验 |
#### 官方伙伴
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [Disable](实体/官方伙伴.md#disable) | <span style="display:inline;color:#ff5555">服务端</span> | 关闭官方伙伴功能，单人游戏以及本地联机不支持该接口 |
| [Enable](实体/官方伙伴.md#enable) | <span style="display:inline;color:#ff5555">服务端</span> | 启用官方伙伴功能，单人游戏以及本地联机不支持该接口 |
#### 官方聊天扩展
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddCommonPhrases](实体/官方聊天扩展.md#addcommonphrases) | <span style="display:inline;color:#ff5555">服务端</span> | 为官方聊天扩展功能添加常用短语。单人模式下单个模组最多添加12条，联机大厅和网络服无条数限制。 |
| [Disable](实体/官方聊天扩展.md#disable) | <span style="display:inline;color:#ff5555">服务端</span> | 关闭官方聊天扩展功能。需要在ClientLoadAddonsFinishServerEvent事件中调用。仅在联机大厅和网络服中生效。 |
| [Enable](实体/官方聊天扩展.md#enable) | <span style="display:inline;color:#ff5555">服务端</span> | 启用官方聊天扩展功能。需要在ClientLoadAddonsFinishServerEvent事件中调用。仅在联机大厅和网络服中生效。 |
| [RegisterChatPrefix](实体/官方聊天扩展.md#registerchatprefix) | <span style="display:inline;color:#ff5555">服务端</span> | 为游戏内指定玩家注册聊天前缀。仅在主界面消息框和聊天界面游戏频道生效。建议在AddServerPlayerEvent事件中调用，为新玩家添加前缀。 |
| [RemoveCommonPhrases](实体/官方聊天扩展.md#removecommonphrases) | <span style="display:inline;color:#ff5555">服务端</span> | 为官方聊天扩展功能移除常用短语。 |
| [SetShowOfficialPhrases](实体/官方聊天扩展.md#setshowofficialphrases) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否显示官方的常用聊天短语。仅在联机大厅和网络服中生效。 |
| [SetShowSocialNearbyInfo](实体/官方聊天扩展.md#setshowsocialnearbyinfo) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否显示官方聊天社交界面中同一游戏玩家是否在附近信息。 |
#### 魔法指令
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [Disable](实体/魔法指令.md#disable) | <span style="display:inline;color:#ff5555">服务端</span> | 关闭官方魔法指令功能。需要在ClientLoadAddonsFinishServerEvent事件中调用。仅在联机大厅中生效。 |
| [Enable](实体/魔法指令.md#enable) | <span style="display:inline;color:#ff5555">服务端</span> | 启用官方魔法指令功能。需要在ClientLoadAddonsFinishServerEvent事件中调用。仅在联机大厅中生效。 |
#### 属性<span id = "属性1"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddPlayerExperience](玩家/属性.md#addplayerexperience) | <span style="display:inline;color:#ff5555">服务端</span> | 增加玩家经验值 |
| [AddPlayerLevel](玩家/属性.md#addplayerlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 修改玩家等级 |
| [CollectOnlineClientData](玩家/属性.md#collectonlineclientdata) | <span style="display:inline;color:#ff5555">服务端</span> | 收集在线玩家客户端数据，用于判断玩家是否作弊 |
| [GetArmorValue](玩家/属性.md#getarmorvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家护甲值 |
| [GetEnchantmentSeed](玩家/属性.md#getenchantmentseed) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家的附魔种子，该种子会决定附魔台上准备附魔的装备的附魔项 |
| [GetPlayerCurLevelExp](玩家/属性.md#getplayercurlevelexp) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家当前等级需要的经验值 |
| [GetPlayerCurrentExhaustionValue](玩家/属性.md#getplayercurrentexhaustionvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家foodExhaustionLevel的当前消耗度。详见<a href="https://zh.minecraft.wiki/w/%E9%A5%A5%E9%A5%BF#%E6%9C%BA%E5%88%B6">消耗度介绍</a> |
| [GetPlayerExp](玩家/属性.md#getplayerexp) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家当前等级下的经验值 |
| [GetPlayerExp](玩家/属性.md#getplayerexp) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家当前等级下的经验值 |
| [GetPlayerHealthLevel](玩家/属性.md#getplayerhealthlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家健康临界值，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效。原版默认值为18 |
| [GetPlayerHealthTick](玩家/属性.md#getplayerhealthtick) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家自然恢复速度，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效。原版默认值为80刻（即每4秒）恢复1点血量 |
| [GetPlayerHunger](玩家/属性.md#getplayerhunger) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家饥饿度，展示在UI饥饿度进度条上，初始值为20，即每一个鸡腿代表2个饥饿度。 **饱和度(saturation)** ：玩家当前饱和度，初始值为5，最大值始终为玩家当前饥饿度(hunger)，该值直接影响玩家**饥饿度(hunger)**。<br>1）增加方法：吃食物。<br>2）减少方法：每触发一次**消耗事件**，该值减少1，如果该值不大于0，直接把玩家 **饥饿度(hunger)** 减少1。 |
| [GetPlayerHunger](玩家/属性.md#getplayerhunger) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家饥饿度，展示在UI饥饿度进度条上，初始值为20，即每一个鸡腿代表2个饥饿度。 **饱和度(saturation)** ：玩家当前饱和度，初始值为5，最大值始终为玩家当前饥饿度(hunger)，该值直接影响玩家**饥饿度(hunger)**。<br>1）增加方法：吃食物。<br>2）减少方法：每触发一次**消耗事件**，该值减少1，如果该值不大于0，直接把玩家 **饥饿度(hunger)** 减少1。 |
| [GetPlayerLevel](玩家/属性.md#getplayerlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家等级 |
| [GetPlayerMaxExhaustionValue](玩家/属性.md#getplayermaxexhaustionvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家foodExhaustionLevel的归零值，常量值，默认为4。**消耗度（exhaustion）**是指玩家当前消耗度水平，初始值为0，该值会随着玩家一系列动作（如跳跃）的影响而增加，当该值大于最大消耗度（maxExhaustion）后归零，并且把饱和度（saturation）减少1（为了说明饥饿度机制，我们将此定义为**消耗事件**） |
| [GetPlayerStarveLevel](玩家/属性.md#getplayerstarvelevel) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家饥饿临界值，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效。原版默认值为1 |
| [GetPlayerStarveTick](玩家/属性.md#getplayerstarvetick) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家饥饿掉血速度，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效。原版默认值为80刻（即每4秒）扣除1点血量 |
| [GetPlayerTotalExp](玩家/属性.md#getplayertotalexp) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家的总经验值 |
| [GetPlayerTotalExp](玩家/属性.md#getplayertotalexp) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家的总经验值 |
| [IsHighLevelMultiJointOfficialSkin](玩家/属性.md#ishighlevelmultijointofficialskin) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家穿戴的皮肤是否为史诗及以上的多关节官方4d皮肤 在接收到 UpdatePlayerSkinClientEvent 事件后调用 此事件在客户端接收到玩家皮肤信息同步后触发 参数仅playerId |
| [IsHighLevelOfficialSkin](玩家/属性.md#ishighlevelofficialskin) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家穿戴的皮肤是否为史诗及以上的官方4d皮肤 在接收到 UpdatePlayerSkinClientEvent 事件后调用 此事件在客户端接收到玩家皮肤信息同步后触发 参数仅playerId |
| [IsMultiJointOfficialSkin](玩家/属性.md#ismultijointofficialskin) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家穿戴的皮肤是否为多关节官方4d皮肤 在接收到 UpdatePlayerSkinClientEvent 事件后调用 此事件在客户端接收到玩家皮肤信息同步后触发 参数仅playerId |
| [IsOfficialSkin](玩家/属性.md#isofficialskin) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家穿戴的皮肤是否为官方4d皮肤 在接收到 UpdatePlayerSkinClientEvent 事件后调用 此事件在客户端接收到玩家皮肤信息同步后触发 参数仅playerId |
| [IsPlayerNaturalRegen](玩家/属性.md#isplayernaturalregen) | <span style="display:inline;color:#ff5555">服务端</span> | 是否开启玩家自然恢复，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效。原版默认开启 |
| [IsPlayerNaturalStarve](玩家/属性.md#isplayernaturalstarve) | <span style="display:inline;color:#ff5555">服务端</span> | 是否开启玩家饥饿掉血，当饥饿值小于饥饿临界值时会自动恢复血量，开启饥饿值且开启饥饿掉血时有效。原版默认开启 |
| [SetEnchantmentSeed](玩家/属性.md#setenchantmentseed) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家的附魔种子，该种子会决定附魔台上准备附魔的装备的附魔项 |
| [SetPlayerCurrentExhaustionValue](玩家/属性.md#setplayercurrentexhaustionvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家foodExhaustionLevel的当前消耗度。详见<a href="https://zh.minecraft.wiki/w/%E9%A5%A5%E9%A5%BF#%E6%9C%BA%E5%88%B6">消耗度介绍</a> |
| [SetPlayerHealthLevel](玩家/属性.md#setplayerhealthlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家健康临界值，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效.原版默认值为18 |
| [SetPlayerHealthTick](玩家/属性.md#setplayerhealthtick) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家自然恢复速度，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效.原版默认值为80刻（即每4秒）恢复1点血量 |
| [SetPlayerHunger](玩家/属性.md#setplayerhunger) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家饥饿度。 |
| [SetPlayerMaxExhaustionValue](玩家/属性.md#setplayermaxexhaustionvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家**最大消耗度(maxExhaustion)**，通过调整 **最大消耗度(maxExhaustion)** 的大小，就可以调整 **饥饿度(hunger)** 的消耗速度，当 **最大消耗度(maxExhaustion)** 很大时，饥饿度可以看似一直不下降 |
| [SetPlayerNaturalRegen](玩家/属性.md#setplayernaturalregen) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否开启玩家自然恢复，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效.原版默认开启 |
| [SetPlayerNaturalStarve](玩家/属性.md#setplayernaturalstarve) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否开启玩家饥饿掉血，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效.原版默认开启 |
| [SetPlayerPrefixAndSuffixName](玩家/属性.md#setplayerprefixandsuffixname) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家前缀和后缀名字 |
| [SetPlayerStarveLevel](玩家/属性.md#setplayerstarvelevel) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家饥饿临界值，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效。原版默认值为1 |
| [SetPlayerStarveTick](玩家/属性.md#setplayerstarvetick) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家饥饿掉血速度，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效.原版默认值为80刻（即每4秒）扣除1点血量 |
| [SetPlayerTotalExp](玩家/属性.md#setplayertotalexp) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家的总经验值 |
| [Swing](玩家/属性.md#swing) | <span style="display:inline;color:#7575f9">客户端</span> | 本地玩家播放原版攻击动作 |
| [getUid](玩家/属性.md#getuid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取本地玩家的uid |
#### 行为<span id = "行为2"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddPlayerAroundEntityMotion](玩家/行为.md#addplayeraroundentitymotion) | <span style="display:inline;color:#ff5555">服务端</span> | 给玩家添加对实体环绕运动器 |
| [AddPlayerAroundPointMotion](玩家/行为.md#addplayeraroundpointmotion) | <span style="display:inline;color:#ff5555">服务端</span> | 给玩家添加对点环绕运动器 |
| [AddPlayerTrackMotion](玩家/行为.md#addplayertrackmotion) | <span style="display:inline;color:#ff5555">服务端</span> | 给玩家添加轨迹运动器 |
| [AddPlayerVelocityMotion](玩家/行为.md#addplayervelocitymotion) | <span style="display:inline;color:#ff5555">服务端</span> | 给玩家添加速度运动器 |
| [BeginSprinting](玩家/行为.md#beginsprinting) | <span style="display:inline;color:#7575f9">客户端</span> | 使本地玩家进入并保持向前疾跑/冲刺状态 |
| [ChangePlayerDimension](玩家/行为.md#changeplayerdimension) | <span style="display:inline;color:#ff5555">服务端</span> | 传送玩家 |
| [ChangePlayerFlyState](玩家/行为.md#changeplayerflystate) | <span style="display:inline;color:#ff5555">服务端</span> | 给予/取消飞行能力, 并根据enterFly参数确定是否进入飞行状态 |
| [EnableKeepInventory](玩家/行为.md#enablekeepinventory) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家死亡不掉落物品 |
| [EndSprinting](玩家/行为.md#endsprinting) | <span style="display:inline;color:#7575f9">客户端</span> | 使本地玩家结束向前疾跑/冲刺状态 |
| [GetEntityRider](玩家/行为.md#getentityrider) | <span style="display:inline;color:#ff5555">服务端</span> | 获取骑乘者正在骑乘的实体的id。 |
| [GetEntityRider](玩家/行为.md#getentityrider) | <span style="display:inline;color:#7575f9">客户端</span> | 获取骑乘者正在骑乘的实体的id。 |
| [GetInteracteCenterOffset](玩家/行为.md#getinteractecenteroffset) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家[服务端交互中心](玩家/../../更新信息/2.8.md#玩家摄像机)的偏移 |
| [GetIsBlocking](玩家/行为.md#getisblocking) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家激活盾牌状态 |
| [GetPickCenterOffset](玩家/行为.md#getpickcenteroffset) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家设置的第三人称下客户端交互中心的偏移 |
| [GetPickRange](玩家/行为.md#getpickrange) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家客户端的交互距离 |
| [GetPlayerDestroyTotalTime](玩家/行为.md#getplayerdestroytotaltime) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家破坏方块需要的时间，受玩家状态（急迫、潮涌、挖掘疲劳）和手持物及手持物附魔（效率）影响 |
| [GetPlayerDestroyTotalTime](玩家/行为.md#getplayerdestroytotaltime) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家破坏方块需要的时间，受玩家状态（急迫、潮涌、挖掘疲劳）和手持物及手持物附魔（效率）影响 |
| [GetPlayerExhaustionRatioByType](玩家/行为.md#getplayerexhaustionratiobytype) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家某行为饥饿度消耗倍率 |
| [GetPlayerInteracteRange](玩家/行为.md#getplayerinteracterange) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家服务端的交互距离 |
| [GetPlayerMotions](玩家/行为.md#getplayermotions) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家身上的所有运动器 |
| [GetPlayerRespawnPos](玩家/行为.md#getplayerrespawnpos) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家复活点 |
| [GetRelevantPlayer](玩家/行为.md#getrelevantplayer) | <span style="display:inline;color:#ff5555">服务端</span> | 获取附近玩家id列表 |
| [IsEntityRiding](玩家/行为.md#isentityriding) | <span style="display:inline;color:#ff5555">服务端</span> | 检查玩家是否骑乘。 |
| [IsInScaffolding](玩家/行为.md#isinscaffolding) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否在脚手架中 |
| [IsOnLadder](玩家/行为.md#isonladder) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否在梯子/藤蔓上 |
| [IsPlayerCanFly](玩家/行为.md#isplayercanfly) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家能否飞行 |
| [IsPlayerFlying](玩家/行为.md#isplayerflying) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家是否在飞行 |
| [OpenNeteaseContainer](玩家/行为.md#openneteasecontainer) | <span style="display:inline;color:#ff5555">服务端</span> | 打开自定义容器界面，不依赖于方块。该界面的物品数据需由开发者自行维护。 |
| [OpenWorkBench](玩家/行为.md#openworkbench) | <span style="display:inline;color:#ff5555">服务端</span> | 在玩家当前位置打开工作台UI，不依赖于工作台方块 |
| [PickUpItemEntity](玩家/行为.md#pickupitementity) | <span style="display:inline;color:#ff5555">服务端</span> | 某个Player拾取物品ItemEntity |
| [PlayerAttackEntity](玩家/行为.md#playerattackentity) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家使用手持武器攻击某个生物 |
| [PlayerDestoryBlock](玩家/行为.md#playerdestoryblock) | <span style="display:inline;color:#ff5555">服务端</span> | 使用手上工具破坏方块 |
| [PlayerUseItemToEntity](玩家/行为.md#playeruseitemtoentity) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家使用手上物品对某个生物使用 |
| [PlayerUseItemToPos](玩家/行为.md#playeruseitemtopos) | <span style="display:inline;color:#ff5555">服务端</span> | 模拟玩家对某个坐标使用物品 |
| [RemovePlayerMotion](玩家/行为.md#removeplayermotion) | <span style="display:inline;color:#ff5555">服务端</span> | 移除玩家身上的运动器 |
| [SetBanPlayerFishing](玩家/行为.md#setbanplayerfishing) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否屏蔽玩家钓鱼功能，屏蔽后玩家可以正常抛甩鱼竿，但无法钓起任何物品 |
| [SetInteracteCenterOffset](玩家/行为.md#setinteractecenteroffset) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家服务端交互中心的偏移 |
| [SetPickCenterOffset](玩家/行为.md#setpickcenteroffset) | <span style="display:inline;color:#7575f9">客户端</span> | 设置第三人称下，玩家客户端交互中心的偏移 |
| [SetPickRange](玩家/行为.md#setpickrange) | <span style="display:inline;color:#7575f9">客户端</span> | 设置玩家客户端的交互距离 |
| [SetPickUpArea](玩家/行为.md#setpickuparea) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家的拾取物品范围，设置后该玩家的拾取物品范围会在原版拾取范围的基础上进行改变。 |
| [SetPlayerAttackSpeedAmplifier](玩家/行为.md#setplayerattackspeedamplifier) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家攻击速度倍数，1.0表示正常水平，1.2表示速度减益20%，0.8表示速度增益20% |
| [SetPlayerExhaustionRatioByType](玩家/行为.md#setplayerexhaustionratiobytype) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家某行为饥饿度消耗倍率 |
| [SetPlayerInteracteRange](玩家/行为.md#setplayerinteracterange) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家服务端的交互距离 |
| [SetPlayerJumpable](玩家/行为.md#setplayerjumpable) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家是否可跳跃 |
| [SetPlayerMotion](玩家/行为.md#setplayermotion) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家的瞬时移动方向向量(可解决SetMotion闪现问题) |
| [SetPlayerMovable](玩家/行为.md#setplayermovable) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家是否可移动 |
| [SetPlayerRespawnPos](玩家/行为.md#setplayerrespawnpos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家复活的位置与维度 |
| [StartPlayerMotion](玩家/行为.md#startplayermotion) | <span style="display:inline;color:#ff5555">服务端</span> | 启动玩家身上的某个运动器 |
| [StopPlayerMotion](玩家/行为.md#stopplayermotion) | <span style="display:inline;color:#ff5555">服务端</span> | 停止玩家身上的某个运动器 |
| [isGliding](玩家/行为.md#isgliding) | <span style="display:inline;color:#7575f9">客户端</span> | 是否鞘翅飞行 |
| [isInWater](玩家/行为.md#isinwater) | <span style="display:inline;color:#7575f9">客户端</span> | 是否在水中 |
| [isMoving](玩家/行为.md#ismoving) | <span style="display:inline;color:#7575f9">客户端</span> | 是否在行走 |
| [isRiding](玩家/行为.md#isriding) | <span style="display:inline;color:#7575f9">客户端</span> | 是否骑乘 |
| [isSneaking](玩家/行为.md#issneaking) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家是否处于潜行状态 |
| [isSneaking](玩家/行为.md#issneaking) | <span style="display:inline;color:#7575f9">客户端</span> | 是否潜行 |
| [isSprinting](玩家/行为.md#issprinting) | <span style="display:inline;color:#7575f9">客户端</span> | 是否在疾跑 |
| [isSwimming](玩家/行为.md#isswimming) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家是否处于游泳状态。 |
| [isSwimming](玩家/行为.md#isswimming) | <span style="display:inline;color:#7575f9">客户端</span> | 是否游泳 |
| [setMoving](玩家/行为.md#setmoving) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否行走，只能设置本地玩家（只适用于移动端） |
| [setSneaking](玩家/行为.md#setsneaking) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否潜行，只能设置本地玩家（只适用于移动端） |
| [setSprinting](玩家/行为.md#setsprinting) | <span style="display:inline;color:#7575f9">客户端</span> | 设置行走模式为疾跑/冲刺，只能设置本地玩家（只适用于移动端） |
| [setUsingShield](玩家/行为.md#setusingshield) | <span style="display:inline;color:#7575f9">客户端</span> | 激活盾牌状态 |
#### 渲染<span id = "渲染2"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddPlayerAnimation](玩家/渲染.md#addplayeranimation) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家渲染动画 |
| [AddPlayerAnimationController](玩家/渲染.md#addplayeranimationcontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家渲染动画控制器 |
| [AddPlayerAnimationIntoState](玩家/渲染.md#addplayeranimationintostate) | <span style="display:inline;color:#7575f9">客户端</span> | 在玩家的动画控制器中的状态添加动画或者动画控制器 |
| [AddPlayerGeometry](玩家/渲染.md#addplayergeometry) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家渲染几何体 |
| [AddPlayerParticleEffect](玩家/渲染.md#addplayerparticleeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家特效资源 |
| [AddPlayerRenderController](玩家/渲染.md#addplayerrendercontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_7-自定义渲染控制器">渲染控制器</a> |
| [AddPlayerRenderMaterial](玩家/渲染.md#addplayerrendermaterial) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家渲染需要的<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_3-自定义材质">材质</a> |
| [AddPlayerScriptAnimate](玩家/渲染.md#addplayerscriptanimate) | <span style="display:inline;color:#7575f9">客户端</span> | 在玩家的客户端实体定义（minecraft:client_entity）json中的scripts/animate节点添加动画/动画控制器 |
| [AddPlayerSoundEffect](玩家/渲染.md#addplayersoundeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家音效资源 |
| [AddPlayerTexture](玩家/渲染.md#addplayertexture) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家渲染贴图 |
| [RebuildPlayerRender](玩家/渲染.md#rebuildplayerrender) | <span style="display:inline;color:#7575f9">客户端</span> | 重建玩家的数据渲染器 |
| [RemovePlayerAnimationController](玩家/渲染.md#removeplayeranimationcontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 移除玩家渲染动画控制器 |
| [RemovePlayerGeometry](玩家/渲染.md#removeplayergeometry) | <span style="display:inline;color:#7575f9">客户端</span> | 删除玩家渲染几何体 |
| [RemovePlayerRenderController](玩家/渲染.md#removeplayerrendercontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 删除玩家<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_7-自定义渲染控制器">渲染控制器</a> |
| [ResetSkin](玩家/渲染.md#resetskin) | <span style="display:inline;color:#7575f9">客户端</span> | 还原默认皮肤 |
| [SetPlayerItemInHandVisible](玩家/渲染.md#setplayeriteminhandvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否隐藏玩家的手持物品模型显示 |
| [SetSkin](玩家/渲染.md#setskin) | <span style="display:inline;color:#7575f9">客户端</span> | 更换原版自定义皮肤 |
#### 背包<span id = "背包1"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddEnchantToInvItem](玩家/背包.md#addenchanttoinvitem) | <span style="display:inline;color:#ff5555">服务端</span> | 给物品栏的物品添加附魔信息 |
| [AddModEnchantToInvItem](玩家/背包.md#addmodenchanttoinvitem) | <span style="display:inline;color:#ff5555">服务端</span> | 给物品栏中物品添加自定义附魔信息 |
| [ChangePlayerItemTipsAndExtraId](玩家/背包.md#changeplayeritemtipsandextraid) | <span style="display:inline;color:#ff5555">服务端</span> | 修改玩家物品的自定义tips和自定义标识符 |
| [ChangeSelectSlot](玩家/背包.md#changeselectslot) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家当前选中快捷栏物品的index |
| [GetCarriedItem](玩家/背包.md#getcarrieditem) | <span style="display:inline;color:#7575f9">客户端</span> | 获取右手物品的信息 |
| [GetInvItemEnchantData](玩家/背包.md#getinvitemenchantdata) | <span style="display:inline;color:#ff5555">服务端</span> | 获取物品栏的物品附魔信息 |
| [GetInvItemModEnchantData](玩家/背包.md#getinvitemmodenchantdata) | <span style="display:inline;color:#ff5555">服务端</span> | 获取物品栏的物品自定义附魔信息 |
| [GetOffhandItem](玩家/背包.md#getoffhanditem) | <span style="display:inline;color:#7575f9">客户端</span> | 获取左手物品的信息 |
| [GetPlayerAllItems](玩家/背包.md#getplayerallitems) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家指定的槽位的批量物品信息 |
| [GetPlayerAllItems](玩家/背包.md#getplayerallitems) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家指定的槽位的批量物品信息，支持获取盔甲栏，副手以及主手物品，背包物品仅支持本地玩家 |
| [GetPlayerItem](玩家/背包.md#getplayeritem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家物品，支持获取背包，盔甲栏，副手以及主手物品 |
| [GetPlayerItem](玩家/背包.md#getplayeritem) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家物品，支持获取背包（本地玩家），盔甲栏，副手以及主手物品 |
| [GetSelectSlotId](玩家/背包.md#getselectslotid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家当前选中槽位 |
| [GetSlotId](玩家/背包.md#getslotid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前手持的快捷栏的槽id |
| [RemoveEnchantToInvItem](玩家/背包.md#removeenchanttoinvitem) | <span style="display:inline;color:#ff5555">服务端</span> | 给物品栏的物品移除附魔信息 |
| [RemoveModEnchantToInvItem](玩家/背包.md#removemodenchanttoinvitem) | <span style="display:inline;color:#ff5555">服务端</span> | 给物品栏中物品移除自定义附魔信息 |
| [SetInvItemExchange](玩家/背包.md#setinvitemexchange) | <span style="display:inline;color:#ff5555">服务端</span> | 交换玩家背包物品 |
| [SetInvItemNum](玩家/背包.md#setinvitemnum) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家背包物品数目 |
| [SetPlayerAllItems](玩家/背包.md#setplayerallitems) | <span style="display:inline;color:#ff5555">服务端</span> | 添加批量物品信息到指定槽位 |
| [SpawnItemToPlayerCarried](玩家/背包.md#spawnitemtoplayercarried) | <span style="display:inline;color:#ff5555">服务端</span> | 生成物品到玩家右手 |
| [SpawnItemToPlayerInv](玩家/背包.md#spawnitemtoplayerinv) | <span style="display:inline;color:#ff5555">服务端</span> | 生成物品到玩家背包 |
#### 摄像机
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddCameraAroundEntityMotion](玩家/摄像机.md#addcameraaroundentitymotion) | <span style="display:inline;color:#7575f9">客户端</span> | 给相机添加对实体环绕运动器 |
| [AddCameraAroundPointMotion](玩家/摄像机.md#addcameraaroundpointmotion) | <span style="display:inline;color:#7575f9">客户端</span> | 给相机添加对点环绕运动器 |
| [AddCameraTrackMotion](玩家/摄像机.md#addcameratrackmotion) | <span style="display:inline;color:#7575f9">客户端</span> | 给相机添加轨迹运动器 |
| [AddCameraVelocityMotion](玩家/摄像机.md#addcameravelocitymotion) | <span style="display:inline;color:#7575f9">客户端</span> | 给相机添加速度运动器 |
| [DepartCamera](玩家/摄像机.md#departcamera) | <span style="display:inline;color:#7575f9">客户端</span> | 分离玩家与摄像机 |
| [GetCameraAnchor](玩家/摄像机.md#getcameraanchor) | <span style="display:inline;color:#7575f9">客户端</span> | 获取相机锚点 |
| [GetCameraMotions](玩家/摄像机.md#getcameramotions) | <span style="display:inline;color:#7575f9">客户端</span> | 获取相机上的所有运动器 |
| [GetCameraOffset](玩家/摄像机.md#getcameraoffset) | <span style="display:inline;color:#7575f9">客户端</span> | 获取摄像机偏移量 |
| [GetCameraPitchLimit](玩家/摄像机.md#getcamerapitchlimit) | <span style="display:inline;color:#7575f9">客户端</span> | 获取摄像机上下角度限制值 |
| [GetCameraRotation](玩家/摄像机.md#getcamerarotation) | <span style="display:inline;color:#7575f9">客户端</span> | 获取摄像机的朝向 |
| [GetForward](玩家/摄像机.md#getforward) | <span style="display:inline;color:#7575f9">客户端</span> | 返回相机向前的方向 |
| [GetFov](玩家/摄像机.md#getfov) | <span style="display:inline;color:#7575f9">客户端</span> | 获取视野大小 |
| [GetFpHeight](玩家/摄像机.md#getfpheight) | <span style="display:inline;color:#7575f9">客户端</span> | 获取本地玩家当前状态下，第一人称视角时的摄像机高度偏移量。游泳时，滑翔时以及普通状态下会有所不同 |
| [GetPerspective](玩家/摄像机.md#getperspective) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前的视角模式 |
| [GetPosition](玩家/摄像机.md#getposition) | <span style="display:inline;color:#7575f9">客户端</span> | 返回相机中心 |
| [IsModCameraLockPitch](玩家/摄像机.md#ismodcameralockpitch) | <span style="display:inline;color:#7575f9">客户端</span> | 是否锁定摄像机上下角度 |
| [IsModCameraLockYaw](玩家/摄像机.md#ismodcameralockyaw) | <span style="display:inline;color:#7575f9">客户端</span> | 是否锁定摄像机左右角度 |
| [LockCamera](玩家/摄像机.md#lockcamera) | <span style="display:inline;color:#7575f9">客户端</span> | 锁定摄像机 |
| [LockModCameraPitch](玩家/摄像机.md#lockmodcamerapitch) | <span style="display:inline;color:#7575f9">客户端</span> | 锁定摄像机上下角度（第三人称下生效，锁定后不能上下调整视角） |
| [LockModCameraYaw](玩家/摄像机.md#lockmodcamerayaw) | <span style="display:inline;color:#7575f9">客户端</span> | 锁定摄像机左右角度（第三人称下生效，锁定后不能通过鼠标左右调整视角） |
| [LockPerspective](玩家/摄像机.md#lockperspective) | <span style="display:inline;color:#7575f9">客户端</span> | 锁定玩家的视角模式 |
| [RemoveCameraMotion](玩家/摄像机.md#removecameramotion) | <span style="display:inline;color:#7575f9">客户端</span> | 移除相机上的某个运动器 |
| [ResetCameraBindActorId](玩家/摄像机.md#resetcamerabindactorid) | <span style="display:inline;color:#7575f9">客户端</span> | 将摄像机重新绑定回主角身上 |
| [SetCameraAnchor](玩家/摄像机.md#setcameraanchor) | <span style="display:inline;color:#7575f9">客户端</span> | 设置相机锚点 |
| [SetCameraBindActorId](玩家/摄像机.md#setcamerabindactorid) | <span style="display:inline;color:#7575f9">客户端</span> | 将摄像机绑定到目标实体身上（调用者与目标必须在同一个dimension，同时需要在加载范围之内，若绑定后目标离开了范围或者死亡，则会自动解除绑定） |
| [SetCameraDistanceFixed](玩家/摄像机.md#setcameradistancefixed) | <span style="display:inline;color:#7575f9">客户端</span> | 设置相机弹簧臂固定，即设置当相机遇到阻挡时是否压缩与人物之间的距离 |
| [SetCameraOffset](玩家/摄像机.md#setcameraoffset) | <span style="display:inline;color:#7575f9">客户端</span> | 设置摄像机偏移量 |
| [SetCameraPitchLimit](玩家/摄像机.md#setcamerapitchlimit) | <span style="display:inline;color:#7575f9">客户端</span> | 设置摄像机上下角度限制值，默认是（-90，90） |
| [SetCameraPos](玩家/摄像机.md#setcamerapos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置相机中心的位置 |
| [SetCameraRotation](玩家/摄像机.md#setcamerarotation) | <span style="display:inline;color:#7575f9">客户端</span> | 设定摄像机的朝向 |
| [SetFov](玩家/摄像机.md#setfov) | <span style="display:inline;color:#7575f9">客户端</span> | 设置视野大小 |
| [SetPerspective](玩家/摄像机.md#setperspective) | <span style="display:inline;color:#7575f9">客户端</span> | 设置视角模式 |
| [SetPlayerFovScale](玩家/摄像机.md#setplayerfovscale) | <span style="display:inline;color:#7575f9">客户端</span> | 将渲染实际使用的fov变为设置中的fov乘以fovScale,fovScale越接近0，其效果越接近原版望远镜效果 |
| [SetSpeedFovLock](玩家/摄像机.md#setspeedfovlock) | <span style="display:inline;color:#7575f9">客户端</span> | 是否锁定相机视野fov，锁定后不随速度变化而变化 |
| [StartCameraMotion](玩家/摄像机.md#startcameramotion) | <span style="display:inline;color:#7575f9">客户端</span> | 启动相机上的某个运动器 |
| [StopCameraMotion](玩家/摄像机.md#stopcameramotion) | <span style="display:inline;color:#7575f9">客户端</span> | 停止相机上的某个运动器 |
| [UnDepartCamera](玩家/摄像机.md#undepartcamera) | <span style="display:inline;color:#7575f9">客户端</span> | 绑定玩家与摄像机 |
| [UnLockCamera](玩家/摄像机.md#unlockcamera) | <span style="display:inline;color:#7575f9">客户端</span> | 解除摄像机锁定 |
#### 动画
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [PlayTpAnimation](玩家/动画.md#playtpanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 第三人称视角播放玩家通用动作 |
| [StopAnimation](玩家/动画.md#stopanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 停止播放玩家通用动作 |
#### 游戏模式
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetPlayerGameType](玩家/游戏模式.md#getplayergametype) | <span style="display:inline;color:#ff5555">服务端</span> | 获取指定玩家的游戏模式 |
| [GetPlayerGameType](玩家/游戏模式.md#getplayergametype) | <span style="display:inline;color:#7575f9">客户端</span> | 获取指定玩家的游戏模式 |
| [SetPlayerGameType](玩家/游戏模式.md#setplayergametype) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家个人游戏模式 |
#### 权限
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetPlayerAbilities](玩家/权限.md#getplayerabilities) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家具体权限 |
| [GetPlayerOperation](玩家/权限.md#getplayeroperation) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家权限类型信息 |
| [SetAttackMobsAbility](玩家/权限.md#setattackmobsability) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家能否攻击生物 |
| [SetAttackPlayersAbility](玩家/权限.md#setattackplayersability) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家能否攻击其他玩家 |
| [SetBuildAbility](玩家/权限.md#setbuildability) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家能否放置方块，该接口的设置会存档，且只影响生存模式 |
| [SetMineAbility](玩家/权限.md#setmineability) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家能否摧毁方块，该接口的设置会存档，且只影响生存模式 |
| [SetOpenContainersAbility](玩家/权限.md#setopencontainersability) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家能否打开容器 |
| [SetOperateDoorsAndSwitchesAbility](玩家/权限.md#setoperatedoorsandswitchesability) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家能否与门和开关交互 |
| [SetOperatorCommandAbility](玩家/权限.md#setoperatorcommandability) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家是否具有操作员命令权限 |
| [SetPermissionLevel](玩家/权限.md#setpermissionlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家权限等级 |
| [SetPlayerMute](玩家/权限.md#setplayermute) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家是否禁言，该接口的设置不存档 |
| [SetTeleportAbility](玩家/权限.md#setteleportability) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家能否使用TP指令 |
#### 导航
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetNavPath](玩家/导航.md#getnavpath) | <span style="display:inline;color:#7575f9">客户端</span> | 获取本地玩家到目标点的寻路路径，开发者可以通过该接口定制自定义的导航系统。 |
| [StartNavTo](玩家/导航.md#startnavto) | <span style="display:inline;color:#7575f9">客户端</span> | 我们提供了一个基于GetNavPath的导航系统实现，做法是在路径上生成序列帧以引导玩家通向目标点，并且当玩家偏离路径会重新进行导航。 |
| [StopNav](玩家/导航.md#stopnav) | <span style="display:inline;color:#7575f9">客户端</span> | 终止当前的导航 |
#### 方块状态与附加值
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetBlockAuxValueFromStates](方块/方块状态与附加值.md#getblockauxvaluefromstates) | <span style="display:inline;color:#ff5555">服务端</span> | 根据方块名称和<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a>获取方块附加值AuxValue |
| [GetBlockStates](方块/方块状态与附加值.md#getblockstates) | <span style="display:inline;color:#ff5555">服务端</span> | 获取<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a> |
| [GetBlockStatesFromAuxValue](方块/方块状态与附加值.md#getblockstatesfromauxvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 根据方块名称和方块附加值AuxValue获取<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a> |
| [SetBlockStates](方块/方块状态与附加值.md#setblockstates) | <span style="display:inline;color:#ff5555">服务端</span> | 设置<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a> |
#### 属性<span id = "属性2"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetBlockBasicInfo](方块/属性.md#getblockbasicinfo) | <span style="display:inline;color:#ff5555">服务端</span> | 获取方块基本信息 |
| [GetBlockTags](方块/属性.md#getblocktags) | <span style="display:inline;color:#ff5555">服务端</span> | 获取方块在tags:*中定义的tags列表 |
| [GetLoadBlocks](方块/属性.md#getloadblocks) | <span style="display:inline;color:#ff5555">服务端</span> | 获取已经加载的方块id |
| [SetBlockBasicInfo](方块/属性.md#setblockbasicinfo) | <span style="display:inline;color:#ff5555">服务端</span> | 设置方块基本信息 |
| [SetChestLootTable](方块/属性.md#setchestloottable) | <span style="display:inline;color:#ff5555">服务端</span> | 设置箱子战利品表 |
#### 方块实体
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CleanBlockTileEntityCustomData](方块/方块实体.md#cleanblocktileentitycustomdata) | <span style="display:inline;color:#ff5555">服务端</span> | 清空指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。 |
| [CreateFrameEffectForBlockEntity](方块/方块实体.md#createframeeffectforblockentity) | <span style="display:inline;color:#7575f9">客户端</span> | 在自定义方块实体上创建序列帧特效，创建后该接口返回序列帧特效的Id，利用该Id可以使用特效/序列帧中的接口对该序列帧特效进行播放、设置位置、大小等操作。与实体的序列帧特效创建方式类似。 |
| [CreateParticleEffectForBlockEntity](方块/方块实体.md#createparticleeffectforblockentity) | <span style="display:inline;color:#7575f9">客户端</span> | 在自定义方块实体上创建粒子特效，创建后该接口返回粒子特效的Id，利用该Id可以使用特效/粒子中的接口对该粒子特效进行播放、设置位置、大小等操作。与实体的粒子特效创建方式类似。若自定义方块实体已存在键值名称相同的特效，则不会创建新的特效，接口返回已有的特效Id。 |
| [ExecuteCommandBlock](方块/方块实体.md#executecommandblock) | <span style="display:inline;color:#ff5555">服务端</span> | 执行一次命令方块 |
| [GetBlockEntityData](方块/方块实体.md#getblockentitydata) | <span style="display:inline;color:#ff5555">服务端</span> | 用于获取可操作某个自定义方块实体数据的对象，操作方式与dict类似 |
| [GetBlockEntityData](方块/方块实体.md#getblockentitydata) | <span style="display:inline;color:#ff5555">服务端</span> | 用于获取方块（包括自定义方块）的数据，如需修改，请使用setblockentitydata接口 |
| [GetBlockEntityData](方块/方块实体.md#getblockentitydata) | <span style="display:inline;color:#7575f9">客户端</span> | 用于获取客户端当前维度中方块（包括自定义方块）的数据，数据只读不可写，无法获取箱子内的物品信息。 |
| [GetBlockEntityMolangValue](方块/方块实体.md#getblockentitymolangvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 获取自定义方块实体的Molang变量的值。 |
| [GetBlockTileEntityCustomData](方块/方块实体.md#getblocktileentitycustomdata) | <span style="display:inline;color:#ff5555">服务端</span> | 读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据 |
| [GetBlockTileEntityWholeCustomData](方块/方块实体.md#getblocktileentitywholecustomdata) | <span style="display:inline;color:#ff5555">服务端</span> | 读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据字典。 |
| [GetCommandBlock](方块/方块实体.md#getcommandblock) | <span style="display:inline;color:#ff5555">服务端</span> | 获取命令方块的设置内容 |
| [GetFrameEffectIdInBlockEntity](方块/方块实体.md#getframeeffectidinblockentity) | <span style="display:inline;color:#7575f9">客户端</span> | 获取在自定义方块实体中已创建的指定序列帧特效的Id，已创建的特效分为两种：一是通过resource_pack/entity/下的实体json文件中使用“netease_frame_effects”所定义的特效；二是使用接口CreateFrameEffectForBlockEntity创建的特效。 返回的特效Id可以使用特效/序列帧中的接口对该序列帧特效进行播放、设置位置、大小等操作。与实体的序列帧特效创建方式类似。 |
| [GetFrameItem](方块/方块实体.md#getframeitem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取物品展示框的物品 |
| [GetFrameItemDropChange](方块/方块实体.md#getframeitemdropchange) | <span style="display:inline;color:#ff5555">服务端</span> | 获取物品展示框里物品的掉落几率 |
| [GetFrameRotation](方块/方块实体.md#getframerotation) | <span style="display:inline;color:#ff5555">服务端</span> | 获取物品展示框里物品的顺时针旋转角度 |
| [GetHopperSpeed](方块/方块实体.md#gethopperspeed) | <span style="display:inline;color:#ff5555">服务端</span> | 获取漏斗运输一个物品所需的时间（单位：刻） |
| [GetParticleEffectIdInBlockEntity](方块/方块实体.md#getparticleeffectidinblockentity) | <span style="display:inline;color:#7575f9">客户端</span> | 获取在自定义方块实体中已创建的指定粒子特效的Id，已创建的特效分为两种：一是通过resource_pack/entity/下的实体json文件中使用“netease_particle_effects”所定义的特效；二是使用接口CreateParticleEffectForBlockEntity创建的特效。 返回的特效Id可以使用特效/粒子中的接口对该粒子特效进行播放、设置位置、大小等操作。与实体的粒子特效创建方式类似。 |
| [RemoveFrameEffectInBlockEntity](方块/方块实体.md#removeframeeffectinblockentity) | <span style="display:inline;color:#7575f9">客户端</span> | 移除在自定义方块实体上创建的序列帧特效。移除后的特效Id将会失效。 |
| [RemoveParticleEffectInBlockEntity](方块/方块实体.md#removeparticleeffectinblockentity) | <span style="display:inline;color:#7575f9">客户端</span> | 移除在自定义方块实体上创建的粒子特效。移除后的特效Id将会失效。 |
| [SetBlockEntityData](方块/方块实体.md#setblockentitydata) | <span style="display:inline;color:#ff5555">服务端</span> | 用于设置方块（包括自定义方块）的数据 |
| [SetBlockEntityMolangValue](方块/方块实体.md#setblockentitymolangvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自定义方块实体的Molang变量，与实体的molang变量作用相同。目前主要用于控制自定义实体的动画状态转变。Molang变量的定义方式与原版实体的Molang变量定义方法相同。详细可参考自定义方块实体动画的教学文档。 |
| [SetBlockTileEntityCustomData](方块/方块实体.md#setblocktileentitycustomdata) | <span style="display:inline;color:#ff5555">服务端</span> | 设置指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。 |
| [SetCommandBlock](方块/方块实体.md#setcommandblock) | <span style="display:inline;color:#ff5555">服务端</span> | 对命令方块进行内容设置 |
| [SetEnableBlockEntityAnimations](方块/方块实体.md#setenableblockentityanimations) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否开启自定义方块实体的动画效果，开启之后，自定义实体方块会按照实体文件中animation_controller所定义的动画状态机进行动画播放。关闭之后，则会停止所有动画播放。 |
| [SetFrameItem](方块/方块实体.md#setframeitem) | <span style="display:inline;color:#ff5555">服务端</span> | 设置物品展示框的物品 |
| [SetFrameItemDropChange](方块/方块实体.md#setframeitemdropchange) | <span style="display:inline;color:#ff5555">服务端</span> | 设置点击物品展示框时生成掉落的几率，默认为1 |
| [SetFrameRotation](方块/方块实体.md#setframerotation) | <span style="display:inline;color:#ff5555">服务端</span> | 设置物品展示框里物品的顺时针旋转角度 |
| [SetHopperSpeed](方块/方块实体.md#sethopperspeed) | <span style="display:inline;color:#ff5555">服务端</span> | 设置漏斗运输一个物品所需的时间（单位：红石刻，1秒10刻），默认值为4刻，该设置存档 |
#### 方块几何体模型
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CombineBlockBetweenPosToGeometry](方块/方块几何体模型.md#combineblockbetweenpostogeometry) | <span style="display:inline;color:#7575f9">客户端</span> | 根据输入的两个位置，搜索这两个位置之间的所有方块，并将这些方块合并和转换为能用于实体的几何体模型。 |
| [CombineBlockFromPosListToGeometry](方块/方块几何体模型.md#combineblockfromposlisttogeometry) | <span style="display:inline;color:#7575f9">客户端</span> | 根据输入的方块位置列表，搜索这些位置的所有方块，并将这些方块合并和转换为能用于实体的几何体模型。 |
| [CombineBlockPaletteToGeometry](方块/方块几何体模型.md#combineblockpalettetogeometry) | <span style="display:inline;color:#7575f9">客户端</span> | 将BlockPalette中的所有方块合并并转换为能用于实体的几何体模型。 |
| [EnableActorBlockGeometryTransparent](方块/方块几何体模型.md#enableactorblockgeometrytransparent) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否允许实体的方块几何体模型产生透明度，允许开启后通过调节方块几何体的透明度将会使得方块几何体模型变得透明。 |
| [GetActorBlockGeometryScale](方块/方块几何体模型.md#getactorblockgeometryscale) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体的方块几何体模型的缩放倍率。 |
| [SetActorBlockGeometryOffset](方块/方块几何体模型.md#setactorblockgeometryoffset) | <span style="display:inline;color:#7575f9">客户端</span> | 设置实体的方块几何体模型的位置偏移。 |
| [SetActorBlockGeometryRotation](方块/方块几何体模型.md#setactorblockgeometryrotation) | <span style="display:inline;color:#7575f9">客户端</span> | 设置实体的方块几何体模型的旋转角度。 |
| [SetActorBlockGeometryScale](方块/方块几何体模型.md#setactorblockgeometryscale) | <span style="display:inline;color:#7575f9">客户端</span> | 设置实体的方块几何体模型的缩放倍率。 |
| [SetActorBlockGeometryTransparency](方块/方块几何体模型.md#setactorblockgeometrytransparency) | <span style="display:inline;color:#7575f9">客户端</span> | 设置实体的方块几何体模型的透明度。注意，只有调用接口EnableActorBlockGeometryTransparent开启了方块几何体模型的透明度后该接口才会生效。 |
#### 方块调色板
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [DeleteBlockInBlockPalette](方块/方块调色板.md#deleteblockinblockpalette) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 删除方块调色板BlockPalette中某个类型的方块。 |
| [DeserializeBlockPalette](方块/方块调色板.md#deserializeblockpalette) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 反序列化方块调色板数据字典中的数据，用于方块调色板在客户端及服务端的事件数据之间传输。 |
| [GetBlockCountInBlockPalette](方块/方块调色板.md#getblockcountinblockpalette) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 获取方块调色板BlockPalette中某个类型的方块的数量。 |
| [GetLocalPosListOfBlocks](方块/方块调色板.md#getlocalposlistofblocks) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 获取方块调色板中某种方块的相对位置列表。方块调色板记录了多个方块组成的一个三维空间下的方块组合，而相对位置则指的是，以这些方块中最小坐标的方块所在位置作为原点的坐标轴下的相对位置。 |
| [GetVolumeOfBlockPalette](方块/方块调色板.md#getvolumeofblockpalette) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 获取方块调色板BlockPalette所占据的长方体的长宽高。长指的是在方块调色板BlockPalette在世界坐标中占据的x轴方向的长度，宽指的是z轴方向的长度，高指的是y轴方向的长度。 |
| [ReplaceAirByStructureVoid](方块/方块调色板.md#replaceairbystructurevoid) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 设置是否将方块调色板BlockPalette中所有空气替换为结构空位。 |
| [ReplaceBlockInBlockPalette](方块/方块调色板.md#replaceblockinblockpalette) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 替换方块调色板BlockPalette中某个类型的方块。 |
| [SerializeBlockPalette](方块/方块调色板.md#serializeblockpalette) | <span style="display:inline;color:#ff5555">服务端</span><br><span style="display:inline;color:#7575f9">客户端</span> | 序列化方块调色板中的数据，用于方块调色板在客户端及服务端的事件数据之间传输。 |
#### 渲染<span id = "渲染3"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddDropItemToWorld](方块/渲染.md#adddropitemtoworld) | <span style="display:inline;color:#7575f9">客户端</span> | 在客户端添加一个掉落物渲染 |
| [ChangeBlockTextures](方块/渲染.md#changeblocktextures) | <span style="display:inline;color:#7575f9">客户端</span> | 替换方块贴图 |
| [DeleteClientDropItemEntity](方块/渲染.md#deleteclientdropitementity) | <span style="display:inline;color:#7575f9">客户端</span> | 删除AddDropItemToWorld创建的客户端掉落物 |
| [DestroyCrackFrame](方块/渲染.md#destroycrackframe) | <span style="display:inline;color:#7575f9">客户端</span> | 销毁特定方块位置上的破坏纹理（仅能销毁SetCrackFrame接口创建的破坏纹理）。 |
| [GetBlockEntityExtraUniforms](方块/渲染.md#getblockentityextrauniforms) | <span style="display:inline;color:#7575f9">客户端</span> | 获取在自定义方块实体的shader当中使用的自定义变量的值，该自定义变量总共可设置EXTRA_ACTOR_UNIFORM1,EXTRA_ACTOR_UNIFORM2,EXTRA_ACTOR_UNIFORM3,EXTRA_ACTOR_UNIFORM4，总共4组，每组为一个vec4(float, float, float ,float)类型的向量。 |
| [GetBlockRenderDistance](方块/渲染.md#getblockrenderdistance) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家周围的可渲染距离 |
| [GetBlockTextures](方块/渲染.md#getblocktextures) | <span style="display:inline;color:#7575f9">客户端</span> | 获取方块的初始贴图信息 |
| [GetClientDropItemEntityIdList](方块/渲染.md#getclientdropitementityidlist) | <span style="display:inline;color:#7575f9">客户端</span> | 获得所有通过AddDropItemToWorld创建的entityId的list |
| [SetBlockEntityExtraUniforms](方块/渲染.md#setblockentityextrauniforms) | <span style="display:inline;color:#7575f9">客户端</span> | 设置可在自定义方块实体的shader当中使用的自定义变量的值，该自定义变量总共可设置EXTRA_ACTOR_UNIFORM1,EXTRA_ACTOR_UNIFORM2,EXTRA_ACTOR_UNIFORM3,EXTRA_ACTOR_UNIFORM4，总共4组，每组为一个vec4(float, float, float ,float)类型的向量，向量的默认值为(1.0,1.0,1.0,1.0)。 |
| [SetBlockEntityFramePosOffset](方块/渲染.md#setblockentityframeposoffset) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自定义方块实体中序列帧特效位置偏移值，用于调整序列帧特效相对于方块位置的偏移。与特效/序列帧/SetPos接口不同，该接口调整的是相对于方块位置的位置偏移值，而不是世界坐标。 |
| [SetBlockEntityModelPosOffset](方块/渲染.md#setblockentitymodelposoffset) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自定义方块实体的实体模型位置偏移值，用于调整实体模型相对于方块位置的偏移。可通过该接口来调整自定义方块实体的实体模型的位置。只有自定义方块实体定义实体模型才生效，实体模型在resource_pack/entity/下定义，详细可参考自定义方块实体动画的教学文档。 |
| [SetBlockEntityModelRotation](方块/渲染.md#setblockentitymodelrotation) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自定义方块实体的实体模型在各个轴上的旋转值，可通过该接口来调整自定义方块实体的实体模型的旋转。只有自定义方块实体定义实体模型才生效，实体模型在resource_pack/entity/下定义，详细可参考自定义方块实体动画的教学文档。 |
| [SetBlockEntityModelScale](方块/渲染.md#setblockentitymodelscale) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自定义方块实体的实体模型大小的缩放值，可通过该接口来调整自定义方块实体的实体模型的大小。只有自定义方块实体定义实体模型才生效，实体模型在resource_pack/entity/下定义，详细可参考自定义方块实体动画的教学文档。 |
| [SetBlockEntityParticlePosOffset](方块/渲染.md#setblockentityparticleposoffset) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自定义方块实体中粒子特效位置偏移值，用于调整粒子特效相对于方块位置的偏移。与特效/粒子/SetPos接口不同，该接口调整的是相对于方块位置的位置偏移值，而不是世界坐标。 |
| [SetBlockRenderDistance](方块/渲染.md#setblockrenderdistance) | <span style="display:inline;color:#7575f9">客户端</span> | 设置玩家周围方块的可渲染距离 |
| [SetCrackFrame](方块/渲染.md#setcrackframe) | <span style="display:inline;color:#7575f9">客户端</span> | 仅客户端的破坏纹理的渲染，可自定义破坏阶段在第几帧。 |
| [SetDropItemTransform](方块/渲染.md#setdropitemtransform) | <span style="display:inline;color:#7575f9">客户端</span> | 设置通过AddDropItemToWorld添加的掉落物的位置、角度和缩放 |
#### 容器
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetBrewingStandSlotItem](方块/容器.md#getbrewingstandslotitem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取酿造台指定槽位物品 |
| [GetChestBoxSize](方块/容器.md#getchestboxsize) | <span style="display:inline;color:#ff5555">服务端</span> | 获取箱子容量大小 |
| [GetChestPairedPosition](方块/容器.md#getchestpairedposition) | <span style="display:inline;color:#ff5555">服务端</span> | 获取与箱子A合并成一个大箱子的箱子B的坐标 |
| [GetContainerItem](方块/容器.md#getcontaineritem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取容器内的物品 |
| [GetContainerSize](方块/容器.md#getcontainersize) | <span style="display:inline;color:#ff5555">服务端</span> | 获取容器容量大小 |
| [GetEnderChestItem](方块/容器.md#getenderchestitem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取末影箱内的物品 |
| [GetInputSlotItem](方块/容器.md#getinputslotitem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取熔炉输入栏物品, 支持使用下面参数清空特定槽位:itemDict为空，为{}, 或itemName为minecraft:air，或者count为0 |
| [GetOpenContainerItem](方块/容器.md#getopencontaineritem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取开放容器的物品 |
| [GetOutputSlotItem](方块/容器.md#getoutputslotitem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取熔炉输出栏物品 |
| [GetPlayerUIItem](方块/容器.md#getplayeruiitem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取合成容器的物品 |
| [SetBrewingStandSlotItem](方块/容器.md#setbrewingstandslotitem) | <span style="display:inline;color:#ff5555">服务端</span> | 设置酿造台指定槽位物品 |
| [SetChestBoxItemExchange](方块/容器.md#setchestboxitemexchange) | <span style="display:inline;color:#ff5555">服务端</span> | 交换箱子里物品的槽位 |
| [SetChestBoxItemNum](方块/容器.md#setchestboxitemnum) | <span style="display:inline;color:#ff5555">服务端</span> | 设置箱子槽位物品数目 |
| [SetInputSlotItem](方块/容器.md#setinputslotitem) | <span style="display:inline;color:#ff5555">服务端</span> | 设置熔炉输入栏物品 |
| [SetPlayerUIItem](方块/容器.md#setplayeruiitem) | <span style="display:inline;color:#ff5555">服务端</span> | 设置合成容器的物品 |
| [SpawnItemToContainer](方块/容器.md#spawnitemtocontainer) | <span style="display:inline;color:#ff5555">服务端</span> | 生成物品到容器方块的物品栏 |
| [SpawnItemToEnderChest](方块/容器.md#spawnitemtoenderchest) | <span style="display:inline;color:#ff5555">服务端</span> | 生成物品到末影箱 |
#### 红石
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetBlockPoweredState](方块/红石.md#getblockpoweredstate) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某个坐标方块的充能状态 |
| [GetStrength](方块/红石.md#getstrength) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某个坐标的红石信号强度 |
#### 告示牌
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetSignBlockText](方块/告示牌.md#getsignblocktext) | <span style="display:inline;color:#ff5555">服务端</span> | 获取告示牌（方块）的文本内容 |
| [GetSignTextStyle](方块/告示牌.md#getsigntextstyle) | <span style="display:inline;color:#ff5555">服务端</span> | 获取告示牌的文本样式信息 |
| [SetSignBlockText](方块/告示牌.md#setsignblocktext) | <span style="display:inline;color:#ff5555">服务端</span> | 设置告示牌（方块）的文本内容 |
| [SetSignTextStyle](方块/告示牌.md#setsigntextstyle) | <span style="display:inline;color:#ff5555">服务端</span> | 设置告示牌的文本样式 |
#### 床
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetBedColor](方块/床.md#getbedcolor) | <span style="display:inline;color:#ff5555">服务端</span> | 获取床（方块）的颜色 |
| [SetBedColor](方块/床.md#setbedcolor) | <span style="display:inline;color:#ff5555">服务端</span> | 设置床（方块）的颜色 |
#### 物品<span id = "物品2"></span>
| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CancelShearsDestoryBlockSpeed](物品.md#cancelshearsdestoryblockspeed) | <span style="display:inline;color:#ff5555">服务端</span> |  取消剪刀对某一方块的破坏速度设置 |
| [CancelShearsDestoryBlockSpeedAll](物品.md#cancelshearsdestoryblockspeedall) | <span style="display:inline;color:#ff5555">服务端</span> |  取消剪刀对全部方块的破坏速度设置 |
| [ChangeArmorTextures](物品.md#changearmortextures) | <span style="display:inline;color:#7575f9">客户端</span> | 修改盔甲在场景中显示和在UI中显示的贴图 |
| [ChangeItemTexture](物品.md#changeitemtexture) | <span style="display:inline;color:#7575f9">客户端</span> | 替换物品的贴图，修改后所有用到该贴图的物品都会被改变，后续创建的此类物品也会被改变。会同时修改物品在UI界面上的显示，手持时候的显示与场景掉落的显示。 |
| [GetAllEnchantsInfo](物品.md#getallenchantsinfo) | <span style="display:inline;color:#ff5555">服务端</span> | 获取目前已注册的所有附魔信息 |
| [GetAllEnchantsInfo](物品.md#getallenchantsinfo) | <span style="display:inline;color:#7575f9">客户端</span> | 获取目前已注册的所有附魔信息 |
| [GetCustomName](物品.md#getcustomname) | <span style="display:inline;color:#ff5555">服务端</span> | 获取物品的自定义名称，与铁砧修改的名称一致 |
| [GetItemBasicInfo](物品.md#getitembasicinfo) | <span style="display:inline;color:#ff5555">服务端</span> | 获取物品的基础信息 |
| [GetItemBasicInfo](物品.md#getitembasicinfo) | <span style="display:inline;color:#7575f9">客户端</span> | 获取物品的基础信息 |
| [GetItemDefenceAngle](物品.md#getitemdefenceangle) | <span style="display:inline;color:#ff5555">服务端</span> | 获取盾牌物品的抵挡角度范围 |
| [GetItemDurability](物品.md#getitemdurability) | <span style="display:inline;color:#ff5555">服务端</span> | 获取指定槽位的物品耐久 |
| [GetItemEffectName](物品.md#getitemeffectname) | <span style="display:inline;color:#7575f9">客户端</span> | 获取物品的状态描述，如：§7保护 0§r |
| [GetItemFormattedHoverText](物品.md#getitemformattedhovertext) | <span style="display:inline;color:#7575f9">客户端</span> | 获取物品的格式化hover文本，如：§f灾厄旗帜§r |
| [GetItemHoverName](物品.md#getitemhovername) | <span style="display:inline;color:#7575f9">客户端</span> | 获取物品的hover名称，如：灾厄旗帜§r |
| [GetItemInfoByBlockName](物品.md#getiteminfobyblockname) | <span style="display:inline;color:#ff5555">服务端</span> | 通过方块名称及aux值获取物品信息 |
| [GetItemLayer](物品.md#getitemlayer) | <span style="display:inline;color:#ff5555">服务端</span> | 获取物品的叠加贴图。物品叠加贴图详见SetItemLayer |
| [GetItemMaxDurability](物品.md#getitemmaxdurability) | <span style="display:inline;color:#ff5555">服务端</span> | 获取指定槽位的物品耐最大耐久 |
| [GetItemTags](物品.md#getitemtags) | <span style="display:inline;color:#ff5555">服务端</span> | 获取物品在minecraft:tags中定义的tags列表 |
| [GetItemTags](物品.md#getitemtags) | <span style="display:inline;color:#7575f9">客户端</span> | 获取物品在minecraft:tags中定义的tags列表 |
| [GetItemTexture](物品.md#getitemtexture) | <span style="display:inline;color:#7575f9">客户端</span> | 获取item_texture.json中物品的贴图路径。 |
| [GetLoadItems](物品.md#getloaditems) | <span style="display:inline;color:#ff5555">服务端</span> | 获取已经加载的物品id |
| [GetUserDataInEvent](物品.md#getuserdatainevent) | <span style="display:inline;color:#ff5555">服务端</span> | 使物品相关服务端事件的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>参数带有userData。在mod初始化时调用即可 |
| [GetUserDataInEvent](物品.md#getuserdatainevent) | <span style="display:inline;color:#7575f9">客户端</span> | 使物品相关客户端事件的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>参数带有userData。在mod初始化时调用即可 |
| [LookupItemByName](物品.md#lookupitembyname) | <span style="display:inline;color:#ff5555">服务端</span> | 判定指定identifier的物品是否存在 |
| [RemoveItemLayer](物品.md#removeitemlayer) | <span style="display:inline;color:#ff5555">服务端</span> | 移除物品的叠加贴图。物品叠加贴图详见SetItemLayer |
| [SetAttackDamage](物品.md#setattackdamage) | <span style="display:inline;color:#ff5555">服务端</span> |  设置物品的攻击伤害值 |
| [SetCompassEntity](物品.md#setcompassentity) | <span style="display:inline;color:#7575f9">客户端</span> | 设置指南针朝向的实体 |
| [SetCompassTarget](物品.md#setcompasstarget) | <span style="display:inline;color:#7575f9">客户端</span> | 设置指南针的朝向位置 |
| [SetCustomName](物品.md#setcustomname) | <span style="display:inline;color:#ff5555">服务端</span> | 设置物品的自定义名称，与使用铁砧重命名一致 |
| [SetItemDefenceAngle](物品.md#setitemdefenceangle) | <span style="display:inline;color:#ff5555">服务端</span> | 设置盾牌物品的抵挡角度范围 |
| [SetItemDurability](物品.md#setitemdurability) | <span style="display:inline;color:#ff5555">服务端</span> | 设置物品的耐久值 |
| [SetItemLayer](物品.md#setitemlayer) | <span style="display:inline;color:#ff5555">服务端</span> | 设置物品的叠加贴图，可以在物品的上层与下层叠加自定义贴图。具体使用可参考CustomItemsMod示例。 |
| [SetItemMaxDurability](物品.md#setitemmaxdurability) | <span style="display:inline;color:#ff5555">服务端</span> | 设置物品的最大耐久值 |
| [SetItemTierLevel](物品.md#setitemtierlevel) | <span style="display:inline;color:#ff5555">服务端</span> |  设置工具类物品的挖掘等级 |
| [SetItemTierSpeed](物品.md#setitemtierspeed) | <span style="display:inline;color:#ff5555">服务端</span> |  设置工具类物品的挖掘速度(可通过userData中的ModTierSpeed获取挖掘速度) |
| [SetMaxStackSize](物品.md#setmaxstacksize) | <span style="display:inline;color:#ff5555">服务端</span> |  设置物品的最大堆叠数量（存档） |
| [SetShearsDestoryBlockSpeed](物品.md#setshearsdestoryblockspeed) | <span style="display:inline;color:#ff5555">服务端</span> |  设置剪刀对某一方块的破坏速度 |

#### 通用<span id = "通用1"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [DestroyEntity](特效/通用.md#destroyentity) | <span style="display:inline;color:#7575f9">客户端</span> | 销毁特效 |
#### 文字面板
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CreateTextBoardInWorld](特效/文字面板.md#createtextboardinworld) | <span style="display:inline;color:#7575f9">客户端</span> | 创建文字面板 |
| [RemoveTextBoard](特效/文字面板.md#removetextboard) | <span style="display:inline;color:#7575f9">客户端</span> | 删除文字面板 |
| [SetBoardBackgroundColor](特效/文字面板.md#setboardbackgroundcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 修改背景颜色 |
| [SetBoardBindEntity](特效/文字面板.md#setboardbindentity) | <span style="display:inline;color:#7575f9">客户端</span> | 文字面板绑定实体对象 |
| [SetBoardDepthTest](特效/文字面板.md#setboarddepthtest) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否开启深度测试, 默认状态下是开启 |
| [SetBoardFaceCamera](特效/文字面板.md#setboardfacecamera) | <span style="display:inline;color:#7575f9">客户端</span> | 设置文字面板的朝向 |
| [SetBoardPos](特效/文字面板.md#setboardpos) | <span style="display:inline;color:#7575f9">客户端</span> | 修改位置 |
| [SetBoardRot](特效/文字面板.md#setboardrot) | <span style="display:inline;color:#7575f9">客户端</span> | 修改旋转角度, 若设置了文本朝向相机，则旋转角度的修改不会生效 |
| [SetBoardScale](特效/文字面板.md#setboardscale) | <span style="display:inline;color:#7575f9">客户端</span> | 内容整体缩放 |
| [SetBoardTextColor](特效/文字面板.md#setboardtextcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 修改字体颜色 |
| [SetText](特效/文字面板.md#settext) | <span style="display:inline;color:#7575f9">客户端</span> | 修改文字面板内容 |
#### 序列帧
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [Bind](特效/序列帧.md#bind) | <span style="display:inline;color:#7575f9">客户端</span> | 绑定entity |
| [Bind](特效/序列帧.md#bind) | <span style="display:inline;color:#7575f9">客户端</span> | 绑定骨骼模型 |
| [CreateEngineSfx](特效/序列帧.md#createenginesfx) | <span style="display:inline;color:#7575f9">客户端</span> | 创建序列帧特效 |
| [CreateEngineSfxFromEditor](特效/序列帧.md#createenginesfxfromeditor) | <span style="display:inline;color:#7575f9">客户端</span> | 指使用资源包中effects/xxx.json，按照编辑器中编辑好的参数创建序列帧。支持环状序列帧 |
| [GetPos](特效/序列帧.md#getpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取序列帧特效的位置 |
| [GetRot](特效/序列帧.md#getrot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取序列帧特效的旋转角度 |
| [GetScale](特效/序列帧.md#getscale) | <span style="display:inline;color:#7575f9">客户端</span> | 获取序列帧特效的缩放值 |
| [Pause](特效/序列帧.md#pause) | <span style="display:inline;color:#7575f9">客户端</span> | 暂停播放，序列帧定格在当前时刻，再次调用Play时继续播放 |
| [Play](特效/序列帧.md#play) | <span style="display:inline;color:#7575f9">客户端</span> | 播放序列帧 |
| [SetDeepTest](特效/序列帧.md#setdeeptest) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧是否透视，默认为否 |
| [SetFaceCamera](特效/序列帧.md#setfacecamera) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧是否始终朝向摄像机，默认为是 |
| [SetFadeDistance](特效/序列帧.md#setfadedistance) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧开始自动调整透明度的距离。序列帧与摄像机之间的距离小于该值时会自动调整序列帧的透明度，距离摄像机越近，序列帧越透明 |
| [SetGlobal](特效/序列帧.md#setglobal) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧是否是全局的，默认为否 |
| [SetLayer](特效/序列帧.md#setlayer) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧渲染层级，默认层级为1，当层级不为1时表示该特效开启特效分层渲染功能。特效（粒子和帧动画）分层渲染时，层级越高渲染越靠后，层级大的会遮挡层级低的，且同一层级的特效会根据特效的相对位置产生正确的相互遮挡关系。 |
| [SetLoop](特效/序列帧.md#setloop) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧是否循环播放，默认为否 |
| [SetMixColor](特效/序列帧.md#setmixcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧混合颜色 |
| [SetPos](特效/序列帧.md#setpos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧的位置 |
| [SetRot](特效/序列帧.md#setrot) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧的旋转 |
| [SetRotUseZXY](特效/序列帧.md#setrotusezxy) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧的旋转，旋转顺序按照绕z,x,y轴旋转 |
| [SetScale](特效/序列帧.md#setscale) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧的缩放 |
| [SetUsePointFiltering](特效/序列帧.md#setusepointfiltering) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧是否使用点滤波 |
| [Stop](特效/序列帧.md#stop) | <span style="display:inline;color:#7575f9">客户端</span> | 停止序列帧（不是暂停） |
#### 粒子
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [Bind](特效/粒子.md#bind) | <span style="display:inline;color:#7575f9">客户端</span> | 绑定entity |
| [Bind](特效/粒子.md#bind) | <span style="display:inline;color:#7575f9">客户端</span> | 绑定骨骼模型 |
| [CreateEngineParticle](特效/粒子.md#createengineparticle) | <span style="display:inline;color:#7575f9">客户端</span> | 用于创建粒子特效 |
| [GetParticleEmissionRate](特效/粒子.md#getparticleemissionrate) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器每帧发射粒子的频率。 |
| [GetParticleMaxNum](特效/粒子.md#getparticlemaxnum) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器包含的最大粒子数量。 |
| [GetParticleMaxSize](特效/粒子.md#getparticlemaxsize) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子特效中粒子大小的最大值。 |
| [GetParticleMinSize](特效/粒子.md#getparticleminsize) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子特效中粒子大小的最小值。 |
| [GetParticleVolumeSize](特效/粒子.md#getparticlevolumesize) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器的体积大小缩放值。 |
| [GetPos](特效/粒子.md#getpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器的世界坐标位置 |
| [GetRot](特效/粒子.md#getrot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器的旋转角度 |
| [Pause](特效/粒子.md#pause) | <span style="display:inline;color:#7575f9">客户端</span> | 暂停播放，粒子定格在当前时刻，再次调用Play时继续播放 |
| [Play](特效/粒子.md#play) | <span style="display:inline;color:#7575f9">客户端</span> | 播放粒子特效 |
| [SetFadeDistance](特效/粒子.md#setfadedistance) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子开始自动调整透明度的距离。粒子与摄像机之间的距离小于该值时会自动调整粒子的透明度，距离摄像机越近，粒子越透明 |
| [SetGlobal](特效/粒子.md#setglobal) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器是否为全局粒子发射器, 默认是False |
| [SetLayer](特效/粒子.md#setlayer) | <span style="display:inline;color:#7575f9">客户端</span> | 粒子默认层级为1，当层级不为1时表示该特效开启特效分层渲染功能。特效（粒子和帧动画）分层渲染时，层级越高渲染越靠后，层级大的会遮挡层级低的，且同一层级的特效会根据特效的相对位置产生正确的相互遮挡关系。 |
| [SetParticleEmissionRate](特效/粒子.md#setparticleemissionrate) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器每帧发射粒子的频率，频率越大则每帧发射的粒子数量越多，但粒子数量不会超过粒子发射器的粒子容量，同时由于性能考虑，每帧发射的粒子数量也不会超过100个。 |
| [SetParticleMaxNum](特效/粒子.md#setparticlemaxnum) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器的粒子容量，即粒子发射器所包含的最大粒子数量。该数量并不代表目前粒子发射器所发射的粒子数量，如需要增加发射的粒子数量，需同时改变粒子的发射频率。 |
| [SetParticleSize](特效/粒子.md#setparticlesize) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子特效中粒子大小的最小值及最大值。 |
| [SetParticleVolumeSize](特效/粒子.md#setparticlevolumesize) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器的体积大小缩放，不影响单个粒子的尺寸。粒子发射器的体积越大，则粒子的发射范围越大。 |
| [SetPos](特效/粒子.md#setpos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器的世界坐标位置 |
| [SetRelative](特效/粒子.md#setrelative) | <span style="display:inline;color:#7575f9">客户端</span> | 当粒子绑定了entity或骨骼模型时，发射出的粒子使用entity坐标系还是世界坐标系。与mcstudio特效编辑器中粒子的“相对挂点运动”选项功能相同。 |
| [SetRotUseZXY](特效/粒子.md#setrotusezxy) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器的旋转，旋转顺序按照绕z,x,y轴旋转 |
| [SetUsePointFiltering](特效/粒子.md#setusepointfiltering) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子材质的纹理滤波是否使用点滤波方法。默认为使用双线性滤波 |
| [Stop](特效/粒子.md#stop) | <span style="display:inline;color:#7575f9">客户端</span> | 停止粒子播放 |
#### 模型特效
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CreateEngineEffectBind](特效/模型特效.md#createengineeffectbind) | <span style="display:inline;color:#7575f9">客户端</span> | 指用编辑器保存资源包中models/bind/xxx_bind.json生成编辑好的所有挂点的所有特效。生成的特效会自动进行挂接及播放，编辑器中设为不可见的特效也会进行播放。并且使用这种方式创建的特效，开发者不用维护entity进出视野导致的挂接特效被移除，引擎会在entity每次进入视野时自动创建所有特效。 |
| [Pause](特效/模型特效.md#pause) | <span style="display:inline;color:#7575f9">客户端</span> | 暂停模型特效（即使用CreateEngineEffectBind创建的特效） |
| [Resume](特效/模型特效.md#resume) | <span style="display:inline;color:#7575f9">客户端</span> | 继续播放模型特效（即使用CreateEngineEffectBind创建的特效） |
#### 微软粒子
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [BindEntity](特效/微软粒子.md#bindentity) | <span style="display:inline;color:#7575f9">客户端</span> | 绑定粒子发射器到指定实体的指定骨骼上 |
| [BindModel](特效/微软粒子.md#bindmodel) | <span style="display:inline;color:#7575f9">客户端</span> | 绑定粒子发射器到指定骨骼模型的指定骨骼上 |
| [Create](特效/微软粒子.md#create) | <span style="display:inline;color:#7575f9">客户端</span> | 创建粒子发射器, 创建后立即播放 |
| [CreateBindEntityNew](特效/微软粒子.md#createbindentitynew) | <span style="display:inline;color:#7575f9">客户端</span> | 创建粒子发射器并绑定到指定实体的指定骨骼上, 创建后立即播放 |
| [EmitManually](特效/微软粒子.md#emitmanually) | <span style="display:inline;color:#7575f9">客户端</span> | 手动发射粒子一次 |
| [Exist](特效/微软粒子.md#exist) | <span style="display:inline;color:#7575f9">客户端</span> | 判断指定粒子发射器是否存在 |
| [GetActiveDuration](特效/微软粒子.md#getactiveduration) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器的激活周期 |
| [GetBindingID](特效/微软粒子.md#getbindingid) | <span style="display:inline;color:#7575f9">客户端</span> | 返回粒子绑定的实体id，没有则返回"0" |
| [GetBindingModelID](特效/微软粒子.md#getbindingmodelid) | <span style="display:inline;color:#7575f9">客户端</span> | 返回绑定的骨骼模型id 没有则返回-1 |
| [GetDuration](特效/微软粒子.md#getduration) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器的播放周期(激活+休眠时间) |
| [GetFacingMode](特效/微软粒子.md#getfacingmode) | <span style="display:inline;color:#7575f9">客户端</span> | 返回粒子发射器的粒子朝向模式 |
| [GetLoopAge](特效/微软粒子.md#getloopage) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器当前播放周期内已播放的时间 |
| [GetPos](特效/微软粒子.md#getpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器位置 |
| [GetRot](特效/微软粒子.md#getrot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器局部旋转 |
| [GetSleepDuration](特效/微软粒子.md#getsleepduration) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器的休眠周期 |
| [GetTimeScale](特效/微软粒子.md#gettimescale) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器的播放速度 |
| [GetVariable](特效/微软粒子.md#getvariable) | <span style="display:inline;color:#7575f9">客户端</span> | 获取粒子发射器的Molang变量值 |
| [Hide](特效/微软粒子.md#hide) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏粒子发射器(不渲染) |
| [IsHiding](特效/微软粒子.md#ishiding) | <span style="display:inline;color:#7575f9">客户端</span> | 返回粒子发射器是否正在被隐藏(不渲染) |
| [IsPausing](特效/微软粒子.md#ispausing) | <span style="display:inline;color:#7575f9">客户端</span> | 返回粒子发射器的逻辑是否正在被暂停 |
| [Pause](特效/微软粒子.md#pause) | <span style="display:inline;color:#7575f9">客户端</span> | 暂停粒子发射器的逻辑更新，但保持渲染状态 |
| [Play](特效/微软粒子.md#play) | <span style="display:inline;color:#7575f9">客户端</span> | 播放粒子发射器 |
| [PlayAt](特效/微软粒子.md#playat) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器播放时间点 |
| [Remove](特效/微软粒子.md#remove) | <span style="display:inline;color:#7575f9">客户端</span> | 销毁指定粒子发射器 |
| [RemoveByName](特效/微软粒子.md#removebyname) | <span style="display:inline;color:#7575f9">客户端</span> | 销毁场景中指定名称(粒子发射器json中的identifier)的所有粒子发射器 |
| [Replay](特效/微软粒子.md#replay) | <span style="display:inline;color:#7575f9">客户端</span> | 重播粒子发射器 |
| [Resume](特效/微软粒子.md#resume) | <span style="display:inline;color:#7575f9">客户端</span> | 恢复粒子发射器的逻辑更新，不影响渲染状态 |
| [SetPos](特效/微软粒子.md#setpos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器位置 |
| [SetRelative](特效/微软粒子.md#setrelative) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子是否在局部空间进行计算 |
| [SetRot](特效/微软粒子.md#setrot) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器局部旋转 |
| [SetRotUseZXY](特效/微软粒子.md#setrotusezxy) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器局部旋转，旋转顺序按照绕z,x,y轴旋转 |
| [SetTimeScale](特效/微软粒子.md#settimescale) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器的播放速度 |
| [SetVariable](特效/微软粒子.md#setvariable) | <span style="display:inline;color:#7575f9">客户端</span> | 设置粒子发射器的Molang变量值 |
| [Show](特效/微软粒子.md#show) | <span style="display:inline;color:#7575f9">客户端</span> | 显示粒子发射器(开启渲染) |
| [Stop](特效/微软粒子.md#stop) | <span style="display:inline;color:#7575f9">客户端</span> | 停止粒子发射器播放(不渲染且不更新逻辑) |
| [Unbind](特效/微软粒子.md#unbind) | <span style="display:inline;color:#7575f9">客户端</span> | 解除指定粒子发射器的绑定状态 |
#### 模型<span id = "模型2"></span>
| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [BindItemToBone](模型.md#binditemtobone) | <span style="display:inline;color:#7575f9">客户端</span> | 将使用了骨骼模型的玩家的手持物绑定到指定的骨骼上 |
| [BindModelToEntity](模型.md#bindmodeltoentity) | <span style="display:inline;color:#7575f9">客户端</span> | 实体替换骨骼模型后，再往上挂接其他骨骼模型。 |
| [BindModelToModel](模型.md#bindmodeltomodel) | <span style="display:inline;color:#7575f9">客户端</span> | 在骨骼模型上挂接其他骨骼模型 |
| [CancelAllBoneMask](模型.md#cancelallbonemask) | <span style="display:inline;color:#7575f9">客户端</span> | 取消动画中的所有骨骼屏蔽。 |
| [CreateFreeModel](模型.md#createfreemodel) | <span style="display:inline;color:#7575f9">客户端</span> | 创建自由的模型（无需绑定Entity） |
| [GetAllBindModelToEntity](模型.md#getallbindmodeltoentity) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体上某个骨骼上挂接的所有骨骼模型的id |
| [GetAnimLength](模型.md#getanimlength) | <span style="display:inline;color:#7575f9">客户端</span> | 获取某个骨骼动画的长度，单位为秒 |
| [GetBonePositionFromMinecraftObject](模型.md#getbonepositionfromminecraftobject) | <span style="display:inline;color:#7575f9">客户端</span> | 获取原版模型的骨骼世界坐标 |
| [GetBoneWorldPos](模型.md#getboneworldpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取骨骼的坐标 |
| [GetEntityBoneWorldPos](模型.md#getentityboneworldpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取换了骨骼模型的实体的骨骼坐标 |
| [GetEntityScale](模型.md#getentityscale) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的放缩比例大小 |
| [GetExtraUniformValue](模型.md#getextrauniformvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 获取在骨骼模型shader中使用的自定义变量Uniform的值 |
| [GetModelId](模型.md#getmodelid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取骨骼模型的Id，主要用于特效绑定骨骼模型 |
| [GetModelMaterial](模型.md#getmodelmaterial) | <span style="display:inline;color:#7575f9">客户端</span> | 获取骨骼模型的正在使用的材质名称，也可获取骨骼模型中指定骨骼所使用的<a href="../../../mcguide/16-美术/6-模型和动作/04-骨骼模型的使用.html#7.模型使用自定义材质及更多贴图">材质名称</a>。如果获取指定骨骼所使用的材质，需要先在netease_model.json下设置"useSplitMeshes"字段为true。 |
| [GetModelName](模型.md#getmodelname) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的模型名称 |
| [GetModelStyle](模型.md#getmodelstyle) | <span style="display:inline;color:#7575f9">客户端</span> | 获取模型类型 |
| [GetPlayingAnimList](模型.md#getplayinganimlist) | <span style="display:inline;color:#7575f9">客户端</span> | 获取指定的骨骼模型中正处于播放状态的骨骼动画名称列表 |
| [GetTexture](模型.md#gettexture) | <span style="display:inline;color:#7575f9">客户端</span> | 获取骨骼模型的贴图路径 |
| [HideModel](模型.md#hidemodel) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏纯模型 |
| [ModelPlayAni](模型.md#modelplayani) | <span style="display:inline;color:#7575f9">客户端</span> | 纯骨骼播放动作。 支持骨骼动画混合，可参考SetAnimationBoneMask接口以及RegisterAnim1DControlParam接口说明。 |
| [ModelStopAni](模型.md#modelstopani) | <span style="display:inline;color:#7575f9">客户端</span> | 暂停指定的骨骼动画 |
| [PlayAnim](模型.md#playanim) | <span style="display:inline;color:#7575f9">客户端</span> | 播放骨骼动画 |
| [RegisterAnim1DControlParam](模型.md#registeranim1dcontrolparam) | <span style="display:inline;color:#7575f9">客户端</span> | 当同时播放多个骨骼动画时，新建用于控制动画进行1D线性混合的参数。目前线性混合仅支持对两个动画进行混合。新建的参数值范围为[0,1]。指定的骨骼将会按照这个参数的值对两个动画进行线性混合。 |
| [RegisterAnim1DMultiControlParam](模型.md#registeranim1dmulticontrolparam) | <span style="display:inline;color:#7575f9">客户端</span> | 当同时播放多个骨骼动画时，注册用于根据权重控制多动画进行混合的参数 |
| [RemoveAnim1DMultiControlParam](模型.md#removeanim1dmulticontrolparam) | <span style="display:inline;color:#7575f9">客户端</span> | 删除用于根据权重控制多动画进行混合的参数 |
| [RemoveFreeModel](模型.md#removefreemodel) | <span style="display:inline;color:#7575f9">客户端</span> | 移除自由模型 |
| [ResetModel](模型.md#resetmodel) | <span style="display:inline;color:#7575f9">客户端</span> | 恢复实体为原版模型 |
| [SetAnim1DControlParam](模型.md#setanim1dcontrolparam) | <span style="display:inline;color:#7575f9">客户端</span> | 新建动画的1D控制参数后，使用该接口对相应的参数进行控制。 |
| [SetAnim1DMultiControlParam](模型.md#setanim1dmulticontrolparam) | <span style="display:inline;color:#7575f9">客户端</span> | 新建动画的1D控制参数后，设置用于根据权重控制多动画进行混合的参数 |
| [SetAnimLayer](模型.md#setanimlayer) | <span style="display:inline;color:#7575f9">客户端</span> | 设置骨骼动画的层级，动画层级越大，则优先度越高，骨骼模型的骨骼优先播放优先度最高的动画，相同层级的动画则优先播放率先播放的动画。 |
| [SetAnimSpeed](模型.md#setanimspeed) | <span style="display:inline;color:#7575f9">客户端</span> | 设置某个骨骼动画的播放速度 |
| [SetAnimationAllBoneMask](模型.md#setanimationallbonemask) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否屏蔽动画中所有骨骼的动画，若开启骨骼屏蔽后，该骨骼将不再播放该动画中的动作。该接口会对该动画中所有骨骼生效，可通过参数ignoreBoneList来指定不受影响的骨骼名称。通过屏蔽指定骨骼的动画可实现同一个骨骼模型同时在不同骨骼上播放不同的动作动画，从而实现快捷的动作融合。 |
| [SetAnimationBoneMask](模型.md#setanimationbonemask) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否屏蔽动画中指定的骨骼的动画，若开启骨骼屏蔽后，该骨骼将不再播放该动画中的动作。通过屏蔽指定骨骼的动画可实现同一个骨骼模型同时在不同骨骼上播放不同的动作动画，从而实现快捷的动作融合。 |
| [SetBrightness](模型.md#setbrightness) | <span style="display:inline;color:#7575f9">客户端</span> | 设置实体的亮度 |
| [SetEntityOpacity](模型.md#setentityopacity) | <span style="display:inline;color:#7575f9">客户端</span> | 设置骨骼模型的透明度，只能对骨骼模型生效，如果设置的是原版模型，则模型的影子会被隐藏。 |
| [SetEntityScale](模型.md#setentityscale) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的放缩比例大小，设置比例过大会导致游戏卡顿，建议控制在20倍以内。实体的scale的立方乘以包围盒的体积不可超过32768 |
| [SetEntityShadowShow](模型.md#setentityshadowshow) | <span style="display:inline;color:#7575f9">客户端</span> | 设置实体打开/关闭影子渲染 |
| [SetExtraUniformValue](模型.md#setextrauniformvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 设置shader中特定Uniform的值 |
| [SetFreeModelAniSpeed](模型.md#setfreemodelanispeed) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自由模型动画的播放速度 |
| [SetFreeModelBoundingBox](模型.md#setfreemodelboundingbox) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自由模型的包围盒 |
| [SetFreeModelPos](模型.md#setfreemodelpos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自由模型的位置 |
| [SetFreeModelRot](模型.md#setfreemodelrot) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自由模型的方向 |
| [SetFreeModelScale](模型.md#setfreemodelscale) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自由模型的大小 |
| [SetLegacyBindRot](模型.md#setlegacybindrot) | <span style="display:inline;color:#7575f9">客户端</span> | 用于修复特效挂接到骨骼时的方向 |
| [SetModel](模型.md#setmodel) | <span style="display:inline;color:#ff5555">服务端</span> | 设置骨骼模型 |
| [SetModel](模型.md#setmodel) | <span style="display:inline;color:#7575f9">客户端</span> | 替换实体的骨骼模型 |
| [SetModelMaterial](模型.md#setmodelmaterial) | <span style="display:inline;color:#7575f9">客户端</span> | 设置骨骼模型所使用的的材质，除了可以设置骨骼模型所使用的<a href="../../../mcguide/16-美术/6-模型和动作/04-骨骼模型的使用.html#7.模型使用自定义材质及更多贴图">自定义材质</a>以外，也可对单个骨骼设置所使用的<a href="../../../mcguide/16-美术/6-模型和动作/04-骨骼模型的使用.html#7.模型使用自定义材质及更多贴图">自定义材质</a>。如果需要设置单个骨骼所使用的材质，需要先在netease_model.json下设置"useSplitMeshes"字段为true。 |
| [SetModelMultiPassMaterial](模型.md#setmodelmultipassmaterial) | <span style="display:inline;color:#7575f9">客户端</span> | 设置骨骼模型多pass中使用到的<a href="../../../mcguide/16-美术/6-模型和动作/04-骨骼模型的使用.html#9.骨骼模型自定义多pass">材质列表</a>，也可对单个骨骼设置所使用的自定义多Pass材质。如果需要设置单个骨骼所使用的多Pass材质，需要先在netease_model.json下设置"useSplitMeshes"字段为true。 |
| [SetModelOffset](模型.md#setmodeloffset) | <span style="display:inline;color:#ff5555">服务端</span> | 设置骨骼模型相对于局部坐标系的偏移量，初始值为(0, 0, 0) |
| [SetModelOffset](模型.md#setmodeloffset) | <span style="display:inline;color:#7575f9">客户端</span> | 模型增加偏移量 |
| [SetModelPartVisible](模型.md#setmodelpartvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 对骨骼模型中指定的骨骼进行渲染屏蔽，屏蔽后该骨骼不会被渲染出来。 |
| [SetModelPerspectiveEffect](模型.md#setmodelperspectiveeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 设置模型透视效果。注：只对自定义骨骼模型生效 |
| [SetModelTexture](模型.md#setmodeltexture) | <span style="display:inline;color:#ff5555">服务端</span> | 设置骨骼模型贴图，该接口与SetTexture功能相同，但属于服务端接口。 |
| [SetShowArmModel](模型.md#setshowarmmodel) | <span style="display:inline;color:#7575f9">客户端</span> | 设置使用骨骼模型后切换至第一人称时是否显示手部模型。需要先为骨骼模型定义arm_model，arm_model的定义可参考demo示例-AwesomeMod中的resourcePack/models/netease_models.json中的大天狗模型定义 |
| [SetTexture](模型.md#settexture) | <span style="display:inline;color:#7575f9">客户端</span> | 设置骨骼模型的贴图，该接口与SetModelTexture功能相同，但属于客户端接口。 |
| [ShowCommonHurtColor](模型.md#showcommonhurtcolor) | <span style="display:inline;color:#ff5555">服务端</span> | 设置挂接骨骼模型的实体是否显示通用的受伤变红效果 |
| [ShowCommonHurtColor](模型.md#showcommonhurtcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 设置挂接骨骼模型的实体是否显示通用的受伤变红效果 |
| [ShowModel](模型.md#showmodel) | <span style="display:inline;color:#7575f9">客户端</span> | 显示纯模型 |
| [UnBindModelToEntity](模型.md#unbindmodeltoentity) | <span style="display:inline;color:#7575f9">客户端</span> | 取消实体上挂接的某个骨骼模型。取消挂接后，这个modelId的模型便会销毁，无法再使用，如果是临时隐藏可以使用HideModel |
| [UnBindModelToModel](模型.md#unbindmodeltomodel) | <span style="display:inline;color:#7575f9">客户端</span> | 取消骨骼模型上挂接的某个骨骼模型。取消挂接后，这个modelId的模型便会销毁，无法再使用，如果是临时隐藏可以使用HideModel |
#### 山头服务器<span id = "山头服务器2"></span>
| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetHostPlayerUid](山头服务器.md#gethostplayeruid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取服务器拥有者的uid。 |
#### 原生UI<span id = "原生UI2"></span>
| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [ChangeSneakState](原生UI.md#changesneakstate) | <span style="display:inline;color:#7575f9">客户端</span> | 切换潜行状态 |
| [ClickInteractGUI](原生UI.md#clickinteractgui) | <span style="display:inline;color:#7575f9">客户端</span> | 模拟点击交互按钮，交互按钮指的在喂食、钓鱼、交易等交互场景出现的按钮 |
| [GetOriginAreaOffset](原生UI.md#getoriginareaoffset) | <span style="display:inline;color:#7575f9">客户端</span> | 获取指定原生UI的offset,包括左上角和右下角 |
| [GetScreenSize](原生UI.md#getscreensize) | <span style="display:inline;color:#7575f9">客户端</span> | 获取游戏分辨率 |
| [GetScreenViewInfo](原生UI.md#getscreenviewinfo) | <span style="display:inline;color:#7575f9">客户端</span> | 获取游戏视角信息。首先获得当前分辨率下UI放大倍数，计算方式可参考<a href="../../../mcguide/18-界面与交互/1-界面编辑器使用说明.html#《我的世界》界面适配方法">《我的世界》界面适配方法</a>。则当前游戏视角的宽度的计算方式为：若当前分辨率的宽度能被该放大倍数整除，则等于当前分辨率，若不能，则等于当前分辨率加放大倍数再减去当前分辨率对放大倍数求余的结果，当前游戏视角的高度计算方法类似。例：以分辨率为1792，828的手机计算，画布是分辨率的3倍，所以x = 1792 + 3 - 1 = 1794；y = 828，该接口返回的结果为(1794.0, 828.0, 0.0, 0.0) |
| [GetWalkState](原生UI.md#getwalkstate) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家行走/潜行/跑步状态 |
| [HideAirSupplyGUI](原生UI.md#hideairsupplygui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏玩家氧气值界面 |
| [HideArmorGui](原生UI.md#hidearmorgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏hud界面的护甲值显示 |
| [HideChangePersonGui](原生UI.md#hidechangepersongui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏切换人称的按钮。隐藏后点击相应位置不会响应 |
| [HideChatGUI](原生UI.md#hidechatgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏聊天按钮原生UI。该接口在开启新版聊天时不生效 |
| [HideCrossHairGUI](原生UI.md#hidecrosshairgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏hud界面的十字准心显示 |
| [HideEmoteGUI](原生UI.md#hideemotegui) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否开启表情功能，默认PC端关闭，手机端开启，且该接口只能在手机端使用。该接口在开启新版聊天时不生效 |
| [HideExpGui](原生UI.md#hideexpgui) | <span style="display:inline;color:#7575f9">客户端</span> | 非创造者模式下隐藏经验条显示 |
| [HideFoldGUI](原生UI.md#hidefoldgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏下拉按钮原生UI。 |
| [HideHealthGui](原生UI.md#hidehealthgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏hud界面的血量显示 |
| [HideHorseHealthGui](原生UI.md#hidehorsehealthgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏hud界面的坐骑的血量显示 |
| [HideHudGUI](原生UI.md#hidehudgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏HUD游戏界面的游戏原生UI。与原版F1按钮效果一致，只隐藏显示，但点击跳跃键等位置依然会响应 |
| [HideHungerGui](原生UI.md#hidehungergui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏hud界面的饥饿值显示 |
| [HideInteractGui](原生UI.md#hideinteractgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏交互按钮。隐藏后点击相应位置不会响应 |
| [HideJumpGui](原生UI.md#hidejumpgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏游戏中右下角的跳跃按钮。隐藏后点击相应位置不会响应 |
| [HideMoveGui](原生UI.md#hidemovegui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏游戏中左下角的移动按钮。隐藏后点击相应位置不会响应 |
| [HideNeteaseStoreGui](原生UI.md#hideneteasestoregui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏游戏中的网易商店按钮。隐藏后点击相应位置不会响应 |
| [HidePauseGUI](原生UI.md#hidepausegui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏暂停按钮原生UI。 |
| [HideSlotBarGui](原生UI.md#hideslotbargui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏游戏中底部中间的物品栏界面 |
| [HideSneakGui](原生UI.md#hidesneakgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏游戏中左下角方向键的中心处潜行按钮。隐藏后点击相应位置不会响应 |
| [HideSwimGui](原生UI.md#hideswimgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏游戏中的浮潜按钮。隐藏后点击相应位置不会响应。 |
| [HideVoiceGUI](原生UI.md#hidevoicegui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏语音按钮原生UI。该接口在开启新版聊天时不生效 |
| [HideWalkGui](原生UI.md#hidewalkgui) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏游戏中跑/走按钮。隐藏后点击相应位置不会响应 |
| [OpenChatGui](原生UI.md#openchatgui) | <span style="display:inline;color:#7575f9">客户端</span> | 打开原版聊天栏 |
| [OpenEmoteGui](原生UI.md#openemotegui) | <span style="display:inline;color:#7575f9">客户端</span> | 打开表情界面 |
| [OpenFoldGui](原生UI.md#openfoldgui) | <span style="display:inline;color:#7575f9">客户端</span> | 打开原版下拉界面 |
| [OpenInventoryGui](原生UI.md#openinventorygui) | <span style="display:inline;color:#7575f9">客户端</span> | 打开原版背包界面，并支持选中某个分页(支持自定义分页名称) |
| [OpenNeteaseStoreGui](原生UI.md#openneteasestoregui) | <span style="display:inline;color:#7575f9">客户端</span> | 打开游戏中的网易商店购买商品界面 |
| [OpenPauseGui](原生UI.md#openpausegui) | <span style="display:inline;color:#7575f9">客户端</span> | 打开原版暂停界面 |
| [OpenReportGui](原生UI.md#openreportgui) | <span style="display:inline;color:#7575f9">客户端</span> | 打开原版举报界面 |
| [OpenVoiceGui](原生UI.md#openvoicegui) | <span style="display:inline;color:#7575f9">客户端</span> | 打开原版语音界面 |
| [PlayHudHeartBlinkAnim](原生UI.md#playhudheartblinkanim) | <span style="display:inline;color:#7575f9">客户端</span> | 播放原版受伤时血量变化的动效 |
| [SetCrossHair](原生UI.md#setcrosshair) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否使用“准星瞄准” |
| [SetEmoteSwitch](原生UI.md#setemoteswitch) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否开启表情功能，默认PC端关闭，手机端开启，且该接口只能在手机端使用，在原生UI初始化前调用设置 |
| [SetHudChatStackPosition](原生UI.md#sethudchatstackposition) | <span style="display:inline;color:#7575f9">客户端</span> | 设置HUD界面左上小聊天窗口位置 |
| [SetHudChatStackVisible](原生UI.md#sethudchatstackvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 设置HUD界面左上小聊天窗口可见性 |
| [SetResponse](原生UI.md#setresponse) | <span style="display:inline;color:#7575f9">客户端</span> | 设置原生UI是否响应 |
| [SimulateJump](原生UI.md#simulatejump) | <span style="display:inline;color:#7575f9">客户端</span> | 模拟跳跃 |

#### 通用<span id = "通用2"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CheckCanBindUI](自定义UI/通用.md#checkcanbindui) | <span style="display:inline;color:#7575f9">客户端</span> | 检查实体是否可以绑定头顶UI，如何将UI与实体绑定详见[CreateUI](自定义UI/通用.md#createui)接口 |
| [CreateUI](自定义UI/通用.md#createui) | <span style="display:inline;color:#7575f9">客户端</span> | 创建UI，详见<a href="../../../mcguide/18-界面与交互/30-UI说明文档.html#界面创建流程及生命周期">界面创建流程及生命周期</a> |
| [EnableFontBatchRender](自定义UI/通用.md#enablefontbatchrender) | <span style="display:inline;color:#7575f9">客户端</span> | 是否开启字体合批 |
| [GetCustomUIControlProxyCls](自定义UI/通用.md#getcustomuicontrolproxycls) | <span style="display:inline;color:#7575f9">客户端</span> | 获得原生界面自定义UI代理基类 |
| [GetMiniMapScreenNodeCls](自定义UI/通用.md#getminimapscreennodecls) | <span style="display:inline;color:#7575f9">客户端</span> | 获取小地图ScreenNode基类 |
| [GetNativeScreenManagerCls](自定义UI/通用.md#getnativescreenmanagercls) | <span style="display:inline;color:#7575f9">客户端</span> | 获得NativeScreenManager类 |
| [GetScreenNodeCls](自定义UI/通用.md#getscreennodecls) | <span style="display:inline;color:#7575f9">客户端</span> | 获得ScreenNode类 |
| [GetTopScreen](自定义UI/通用.md#gettopscreen) | <span style="display:inline;color:#7575f9">客户端</span> | 获取UI堆栈栈顶的UI节点 |
| [GetTopUI](自定义UI/通用.md#gettopui) | <span style="display:inline;color:#7575f9">客户端</span> | 获取UI栈顶的UI名称 |
| [GetTopUINode](自定义UI/通用.md#gettopuinode) | <span style="display:inline;color:#7575f9">客户端</span> | 获取Push进来的最顶层界面，包括原生界面，详见<a href="../../../mcguide/18-界面与交互/30-UI说明文档.html#界面创建流程及生命周期" rel="noopenner"> 界面创建流程及生命周期 </a> |
| [GetUI](自定义UI/通用.md#getui) | <span style="display:inline;color:#7575f9">客户端</span> | 获取UI节点，详见<a href="../../../mcguide/18-界面与交互/30-UI说明文档.html#界面创建流程及生命周期">界面创建流程及生命周期</a> |
| [GetUIScreenProxyCls](自定义UI/通用.md#getuiscreenproxycls) | <span style="display:inline;color:#7575f9">客户端</span> | 获得原生界面Screen代理基类 |
| [GetViewBinderCls](自定义UI/通用.md#getviewbindercls) | <span style="display:inline;color:#7575f9">客户端</span> | 获得ViewBinder类 |
| [GetViewViewRequestCls](自定义UI/通用.md#getviewviewrequestcls) | <span style="display:inline;color:#7575f9">客户端</span> | 获得ViewRequest类 |
| [OpenDeveloperHomeWindow](自定义UI/通用.md#opendeveloperhomewindow) | <span style="display:inline;color:#7575f9">客户端</span> | 打开网易资源中心开发者主页。该接口只能在横屏版本手机端使用 |
| [OpenResourceCenterDetailWindow](自定义UI/通用.md#openresourcecenterdetailwindow) | <span style="display:inline;color:#7575f9">客户端</span> | 打开网易资源中心组件详情界面。该接口只能在横屏版本手机端使用 |
| [PopScreen](自定义UI/通用.md#popscreen) | <span style="display:inline;color:#7575f9">客户端</span> | 使用堆栈管理的方式关闭UI |
| [PopTopUI](自定义UI/通用.md#poptopui) | <span style="display:inline;color:#7575f9">客户端</span> | 弹出UI栈顶的UI |
| [PushScreen](自定义UI/通用.md#pushscreen) | <span style="display:inline;color:#7575f9">客户端</span> | 使用堆栈管理的方式创建UI |
| [RegisterUI](自定义UI/通用.md#registerui) | <span style="display:inline;color:#7575f9">客户端</span> | 注册UI，创建UI前，需要先注册UI。同一UI只需要注册一次即可。详见<a href="../../../mcguide/18-界面与交互/30-UI说明文档.html#界面创建流程及生命周期">界面创建流程及生命周期</a> |
| [RegisterUIAnimations](自定义UI/通用.md#registeruianimations) | <span style="display:inline;color:#7575f9">客户端</span> | 注册UI动画 |
| [UnregisterUIAnimation](自定义UI/通用.md#unregisteruianimation) | <span style="display:inline;color:#7575f9">客户端</span> | 取消UI动画的注册 |
#### 自定义书本
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetBookManager](自定义UI/自定义书本.md#getbookmanager) | <span style="display:inline;color:#7575f9">客户端</span> | 获取书本管理对象 |
#### 自定义成就系统
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddNodeProgress](自定义UI/自定义成就系统.md#addnodeprogress) | <span style="display:inline;color:#ff5555">服务端</span> | 增加对应玩家的对应成就节点的成就进度 |
| [GetAchievementGatePosition](自定义UI/自定义成就系统.md#getachievementgateposition) | <span style="display:inline;color:#7575f9">客户端</span> | 获取自定义成就系统的入口按钮位置 |
| [GetChildrenNode](自定义UI/自定义成就系统.md#getchildrennode) | <span style="display:inline;color:#ff5555">服务端</span> | 获得该成就节点的下一级所有孩子节点的list |
| [GetNodeDetailInfo](自定义UI/自定义成就系统.md#getnodedetailinfo) | <span style="display:inline;color:#ff5555">服务端</span> | 获取对应玩家的对应节点信息 |
| [SetAchievementGatePosition](自定义UI/自定义成就系统.md#setachievementgateposition) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自定义成就系统的入口按钮位置 |
| [SetNodeFinish](自定义UI/自定义成就系统.md#setnodefinish) | <span style="display:inline;color:#ff5555">服务端</span> | 设置对应玩家的对应成就节点完成 |
#### UI界面
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [BindVirtualWorldModel](自定义UI/UI界面.md#bindvirtualworldmodel) | <span style="display:inline;color:#7575f9">客户端</span> | 绑定虚拟世界中的模型 |
| [ChangeBindAutoScale](自定义UI/UI界面.md#changebindautoscale) | <span style="display:inline;color:#7575f9">客户端</span> | 设置已绑定实体的UI是否根据绑定实体与本地玩家间的距离动态缩放，**只对已绑定实体的UI界面生效，如何将UI与实体绑定详见[CreateUI](自定义UI/通用.md#CreateUI)接口** |
| [ChangeBindEntityId](自定义UI/UI界面.md#changebindentityid) | <span style="display:inline;color:#7575f9">客户端</span> | 修改绑定的实体id，**只对已绑定实体的UI界面生效，如何将UI与实体绑定详见[CreateUI](自定义UI/通用.md#CreateUI)接口** |
| [ChangeBindOffset](自定义UI/UI界面.md#changebindoffset) | <span style="display:inline;color:#7575f9">客户端</span> | 修改与绑定实体之间的偏移量，**只对已绑定实体的UI界面生效，如何将UI与实体绑定详见[CreateUI](自定义UI/通用.md#CreateUI)接口** |
| [Clone](自定义UI/UI界面.md#clone) | <span style="display:inline;color:#7575f9">客户端</span> | 克隆一个已有的控件，修改它的名称，并将它挂接到指定的父节点上，目前文本、图片、按钮控件的克隆控件表现正常，其他复杂控件的克隆控件可能存在运行问题，建议在json编写的过程中，手动复制一份对应控件使用。 |
| [Create](自定义UI/UI界面.md#create) | <span style="display:inline;color:#7575f9">客户端</span> | UI生命周期函数，当UI创建成功时调用。 |
| [CreateChildControl](自定义UI/UI界面.md#createchildcontrol) | <span style="display:inline;color:#7575f9">客户端</span> | 在当前画布中创建子控件，如果该子控件已经存在则返回已存在的子控件 |
| [Destroy](自定义UI/UI界面.md#destroy) | <span style="display:inline;color:#7575f9">客户端</span> | UI生命周期函数，当UI销毁时调用。 |
| [GetAllChildrenPath](自定义UI/UI界面.md#getallchildrenpath) | <span style="display:inline;color:#7575f9">客户端</span> | 获取所有子节点的路径list |
| [GetBaseUIControl](自定义UI/UI界面.md#getbaseuicontrol) | <span style="display:inline;color:#7575f9">客户端</span> | 根据路径获取BaseUIControl实例 |
| [GetBindAutoScale](自定义UI/UI界面.md#getbindautoscale) | <span style="display:inline;color:#7575f9">客户端</span> | 获取该绑定实体的UI是否动态缩放，未绑定的UI将传回默认值1 |
| [GetBindEntityId](自定义UI/UI界面.md#getbindentityid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取该UI绑定的实体id，未绑定的UI将传回默认值None |
| [GetBindOffset](自定义UI/UI界面.md#getbindoffset) | <span style="display:inline;color:#7575f9">客户端</span> | 获取该UI绑定实体的偏移量，未绑定的UI将传回默认值(0, 0, 0) |
| [GetBindWorldPosition](自定义UI/UI界面.md#getbindworldposition) | <span style="display:inline;color:#7575f9">客户端</span> | 获取该UI绑定的worldPosition，未绑定返回默认值None |
| [GetChildrenName](自定义UI/UI界面.md#getchildrenname) | <span style="display:inline;color:#7575f9">客户端</span> | 获取子节点的名称list |
| [GetIsHud](自定义UI/UI界面.md#getishud) | <span style="display:inline;color:#7575f9">客户端</span> | 获得本界面的输入模式 |
| [GetRichTextItem](自定义UI/UI界面.md#getrichtextitem) | <span style="display:inline;color:#7575f9">客户端</span> | 返回一个富文本控件实例 |
| [GetScreenName](自定义UI/UI界面.md#getscreenname) | <span style="display:inline;color:#7575f9">客户端</span> | 获得本界面的名称 |
| [GetSelf](自定义UI/UI界面.md#getself) | <span style="display:inline;color:#7575f9">客户端</span> | 获取零件界面自身 |
| [OnActive](自定义UI/UI界面.md#onactive) | <span style="display:inline;color:#7575f9">客户端</span> | UI生命周期函数，当UI重新回到栈顶时调用。 |
| [OnDeactive](自定义UI/UI界面.md#ondeactive) | <span style="display:inline;color:#7575f9">客户端</span> | UI生命周期函数，当栈顶UI有其他UI入栈时调用。 |
| [RemoveChildControl](自定义UI/UI界面.md#removechildcontrol) | <span style="display:inline;color:#7575f9">客户端</span> | 移除当前画布中的子控件 |
| [RemoveComponent](自定义UI/UI界面.md#removecomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 动态删除某一控件 |
| [SetBindWorldPosition](自定义UI/UI界面.md#setbindworldposition) | <span style="display:inline;color:#7575f9">客户端</span> | 设置UI绑定的worldPosition |
| [SetIsHud](自定义UI/UI界面.md#setishud) | <span style="display:inline;color:#7575f9">客户端</span> | 设置本界面的输入模式 |
| [SetRemove](自定义UI/UI界面.md#setremove) | <span style="display:inline;color:#7575f9">客户端</span> | 删除本界面节点 |
| [SetScreenVisible](自定义UI/UI界面.md#setscreenvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否显示本界面 |
| [SetSelectControl](自定义UI/UI界面.md#setselectcontrol) | <span style="display:inline;color:#7575f9">客户端</span> | 设置当前焦点所在的控件,当设置控件为文本输入框时会弹出系统小键盘 |
| [SetStackGridCount](自定义UI/UI界面.md#setstackgridcount) | <span style="display:inline;color:#7575f9">客户端</span> | 设置StackGrid控件的大小 |
| [SetUiEntity](自定义UI/UI界面.md#setuientity) | <span style="display:inline;color:#7575f9">客户端</span> | 设置PaperDoll控件需要显示的生物模型,PaperDoll控件的配置方式详见<a href="../../../mcguide/18-界面与交互/30-UI说明文档.html#paperdoll">控件介绍PaperDoll</a> |
| [SetUiModel](自定义UI/UI界面.md#setuimodel) | <span style="display:inline;color:#7575f9">客户端</span> | 设置PaperDoll控件需要显示的模型,PaperDoll控件的配置方式详见<a href="../../../mcguide/18-界面与交互/30-UI说明文档.html#paperdoll">控件介绍PaperDoll</a> |
| [SetUiModelScale](自定义UI/UI界面.md#setuimodelscale) | <span style="display:inline;color:#7575f9">客户端</span> | 设置PaperDoll控件模型的缩放比例 |
| [Update](自定义UI/UI界面.md#update) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端每帧调用，1秒有30帧 |
| [UpdateScreen](自定义UI/UI界面.md#updatescreen) | <span style="display:inline;color:#7575f9">客户端</span> | 刷新界面，重新计算各个控件的相关数据 |
#### UI控件
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddEntityMarker](自定义UI/UI控件.md#addentitymarker) | <span style="display:inline;color:#7575f9">客户端</span> | 增加实体位置标记 |
| [AddEntityTextMarker](自定义UI/UI控件.md#addentitytextmarker) | <span style="display:inline;color:#7575f9">客户端</span> | 在小地图上增加实体文本标记 |
| [AddHoverEventParams](自定义UI/UI控件.md#addhovereventparams) | <span style="display:inline;color:#7575f9">客户端</span> | 开启按钮的悬浮回调功能，不调用该函数则按钮无悬浮回调 |
| [AddOption](自定义UI/UI控件.md#addoption) | <span style="display:inline;color:#7575f9">客户端</span> | 添加下拉框项，若添加成功则返回True，否则返回False |
| [AddStaticMarker](自定义UI/UI控件.md#addstaticmarker) | <span style="display:inline;color:#7575f9">客户端</span> | 增加地图上静态位置的标记 |
| [AddStaticTextMarker](自定义UI/UI控件.md#addstatictextmarker) | <span style="display:inline;color:#7575f9">客户端</span> | 在小地图上增加静态文本的标记 |
| [AddTouchEventParams](自定义UI/UI控件.md#addtoucheventparams) | <span style="display:inline;color:#7575f9">客户端</span> | 开启按钮回调功能，不调用该函数则按钮无回调 |
| [ClearOptions](自定义UI/UI控件.md#clearoptions) | <span style="display:inline;color:#7575f9">客户端</span> | 清空下拉框 |
| [ClearSelection](自定义UI/UI控件.md#clearselection) | <span style="display:inline;color:#7575f9">客户端</span> | 清除当前选中，使下拉框恢复未选中内容状态 |
| [DisableTextShadow](自定义UI/UI控件.md#disabletextshadow) | <span style="display:inline;color:#7575f9">客户端</span> | 关闭文本控件显示阴影 |
| [EnableTextShadow](自定义UI/UI控件.md#enabletextshadow) | <span style="display:inline;color:#7575f9">客户端</span> | 使文本控件显示阴影 |
| [GetAnchorFrom](自定义UI/UI控件.md#getanchorfrom) | <span style="display:inline;color:#7575f9">客户端</span> | 判断控件相对于父节点的哪个锚点来计算位置与大小 |
| [GetAnchorTo](自定义UI/UI控件.md#getanchorto) | <span style="display:inline;color:#7575f9">客户端</span> | 获取控件自身锚点位置信息 |
| [GetChildByName](自定义UI/UI控件.md#getchildbyname) | <span style="display:inline;color:#7575f9">客户端</span> | 根据子控件的名称获取BaseUIControl实例 |
| [GetChildByPath](自定义UI/UI控件.md#getchildbypath) | <span style="display:inline;color:#7575f9">客户端</span> | 根据相对路径获取BaseUIControl实例 |
| [GetClipDirection](自定义UI/UI控件.md#getclipdirection) | <span style="display:inline;color:#7575f9">客户端</span> | 获取图片控件的裁剪方向 |
| [GetClipOffset](自定义UI/UI控件.md#getclipoffset) | <span style="display:inline;color:#7575f9">客户端</span> | 获取控件的裁剪偏移信息 |
| [GetClipsChildren](自定义UI/UI控件.md#getclipschildren) | <span style="display:inline;color:#7575f9">客户端</span> | 根据控件路径返回某控件是否开启裁剪内容 |
| [GetCurrentSliceIndex](自定义UI/UI控件.md#getcurrentsliceindex) | <span style="display:inline;color:#7575f9">客户端</span> | 获取轮盘当前选择的切片的index，一般是在SetHoverCallback和SetTouchUpCallback中使用，表示当前鼠标悬浮或者点击的轮盘切片index |
| [GetEditText](自定义UI/UI控件.md#getedittext) | <span style="display:inline;color:#7575f9">客户端</span> | 获取edit_box输入框的文本信息，获取失败会返回None |
| [GetFullPosition](自定义UI/UI控件.md#getfullposition) | <span style="display:inline;color:#7575f9">客户端</span> | 获取控件的锚点坐标，支持比例值以及绝对值 |
| [GetFullSize](自定义UI/UI控件.md#getfullsize) | <span style="display:inline;color:#7575f9">客户端</span> | 获取控件的大小，支持百分比以及绝对值 |
| [GetGlobalPosition](自定义UI/UI控件.md#getglobalposition) | <span style="display:inline;color:#7575f9">客户端</span> | 获取控件全局坐标 |
| [GetGlobalRotateAngle](自定义UI/UI控件.md#getglobalrotateangle) | <span style="display:inline;color:#7575f9">客户端</span> | 获取图片通过RotateAround函数设置进去的角度值 |
| [GetGlobalRotatePoint](自定义UI/UI控件.md#getglobalrotatepoint) | <span style="display:inline;color:#7575f9">客户端</span> | 获取图片通过RotateAround函数设置进去的point值 |
| [GetGridItem](自定义UI/UI控件.md#getgriditem) | <span style="display:inline;color:#7575f9">客户端</span> | 根据网格位置获取元素控件 |
| [GetIsModal](自定义UI/UI控件.md#getismodal) | <span style="display:inline;color:#7575f9">客户端</span> | 判断当前面板是否为模态框 |
| [GetIsSwallow](自定义UI/UI控件.md#getisswallow) | <span style="display:inline;color:#7575f9">客户端</span> | 判断当前面板输入是否会吞噬事件，isSwallow为Ture时，点击时，点击事件不会穿透到世界。如破坏方块、镜头转向不会被响应 |
| [GetMaxSize](自定义UI/UI控件.md#getmaxsize) | <span style="display:inline;color:#7575f9">客户端</span> | 获取控件所允许的最大的大小值 |
| [GetMinSize](自定义UI/UI控件.md#getminsize) | <span style="display:inline;color:#7575f9">客户端</span> | 获取控件所允许的最小的大小值 |
| [GetModelId](自定义UI/UI控件.md#getmodelid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取渲染的骨骼模型Id |
| [GetOffsetDelta](自定义UI/UI控件.md#getoffsetdelta) | <span style="display:inline;color:#7575f9">客户端</span> | 获得点击面板的拖拽偏移量 |
| [GetOptionCount](自定义UI/UI控件.md#getoptioncount) | <span style="display:inline;color:#7575f9">客户端</span> | 获得选项数量 |
| [GetOptionIndexByShowName](自定义UI/UI控件.md#getoptionindexbyshowname) | <span style="display:inline;color:#7575f9">客户端</span> | 根据展示文本查找对应下拉框项的索引位置，若找不到返回-1 |
| [GetOptionShowNameByIndex](自定义UI/UI控件.md#getoptionshownamebyindex) | <span style="display:inline;color:#7575f9">客户端</span> | 根据索引位置查找当前栈式文本，若找不到返回None |
| [GetOrientation](自定义UI/UI控件.md#getorientation) | <span style="display:inline;color:#7575f9">客户端</span> | 获取stackPanel的排列方向 |
| [GetPath](自定义UI/UI控件.md#getpath) | <span style="display:inline;color:#7575f9">客户端</span> | 返回当前控件的相对路径，路径从画布节点开始算起 |
| [GetPosition](自定义UI/UI控件.md#getposition) | <span style="display:inline;color:#7575f9">客户端</span> | 获取控件相对父节点的坐标 |
| [GetPropertyBag](自定义UI/UI控件.md#getpropertybag) | <span style="display:inline;color:#7575f9">客户端</span> | 获取PropertyBag |
| [GetRotateAngle](自定义UI/UI控件.md#getrotateangle) | <span style="display:inline;color:#7575f9">客户端</span> | 获取图片相对自身的旋转锚点旋转的角度 |
| [GetRotatePivot](自定义UI/UI控件.md#getrotatepivot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取图片相对自身的旋转锚点 |
| [GetRotateRect](自定义UI/UI控件.md#getrotaterect) | <span style="display:inline;color:#7575f9">客户端</span> | 获取图片当前的四个边角点 |
| [GetScrollViewContentControl](自定义UI/UI控件.md#getscrollviewcontentcontrol) | <span style="display:inline;color:#7575f9">客户端</span> | 返回该scroll_view内容的BaseUIControl实例 |
| [GetScrollViewContentPath](自定义UI/UI控件.md#getscrollviewcontentpath) | <span style="display:inline;color:#7575f9">客户端</span> | 返回该scroll_view内容的路径 |
| [GetScrollViewPercentValue](自定义UI/UI控件.md#getscrollviewpercentvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前scroll_view内容的百分比位置 |
| [GetScrollViewPos](自定义UI/UI控件.md#getscrollviewpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获得当前scroll_view最上方内容的位置 |
| [GetSelectOptionIndex](自定义UI/UI控件.md#getselectoptionindex) | <span style="display:inline;color:#7575f9">客户端</span> | 获得当前选中项的索引，所无选中项则返回-1 |
| [GetSelectOptionShowName](自定义UI/UI控件.md#getselectoptionshowname) | <span style="display:inline;color:#7575f9">客户端</span> | 获得当前选中项的展示文本，所无选中项则返回None |
| [GetSize](自定义UI/UI控件.md#getsize) | <span style="display:inline;color:#7575f9">客户端</span> | 获取控件的大小 |
| [GetSliceCount](自定义UI/UI控件.md#getslicecount) | <span style="display:inline;color:#7575f9">客户端</span> | 获取轮盘可以选择的总切片数量 |
| [GetSliderValue](自定义UI/UI控件.md#getslidervalue) | <span style="display:inline;color:#7575f9">客户端</span> | 获取滑动条的值，失败返回0 |
| [GetText](自定义UI/UI控件.md#gettext) | <span style="display:inline;color:#7575f9">客户端</span> | 获取Label的文本信息，获取失败会返回None |
| [GetTextAlignment](自定义UI/UI控件.md#gettextalignment) | <span style="display:inline;color:#7575f9">客户端</span> | 获取文本控件的文本对齐方式 |
| [GetTextColor](自定义UI/UI控件.md#gettextcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 获取Label文本颜色 |
| [GetTextLinePadding](自定义UI/UI控件.md#gettextlinepadding) | <span style="display:inline;color:#7575f9">客户端</span> | 获取文本控件的行间距 |
| [GetToggleState](自定义UI/UI控件.md#gettogglestate) | <span style="display:inline;color:#7575f9">客户端</span> | 获取Toggle开关控件的状态 |
| [GetUiItem](自定义UI/UI控件.md#getuiitem) | <span style="display:inline;color:#7575f9">客户端</span> | 获取ItemRenderer控件显示的物品，ItemRenderer控件的配置方式详见<a href="../../../mcguide/18-界面与交互/30-UI说明文档.html#itemrenderer">控件介绍ItemRenderer</a> |
| [GetVisible](自定义UI/UI控件.md#getvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 根据控件路径返回某控件是否已显示 |
| [IsAnimEndCallbackRegistered](自定义UI/UI控件.md#isanimendcallbackregistered) | <span style="display:inline;color:#7575f9">客户端</span> | 控件是否对名称为animName的动画进行了注册回调 |
| [IsTextShadowEnabled](自定义UI/UI控件.md#istextshadowenabled) | <span style="display:inline;color:#7575f9">客户端</span> | 判断文本控件是否显示阴影 |
| [PauseAnimation](自定义UI/UI控件.md#pauseanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 暂停动画，暂停后的动画会停在当前的状态 |
| [PlayAnimation](自定义UI/UI控件.md#playanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 继续播放动画，从动画当前状态开始播放 |
| [RegisterCloseComboBoxCallback](自定义UI/UI控件.md#registerclosecomboboxcallback) | <span style="display:inline;color:#7575f9">客户端</span> | 注册关闭下拉框事件回调 |
| [RegisterOpenComboBoxCallback](自定义UI/UI控件.md#registeropencomboboxcallback) | <span style="display:inline;color:#7575f9">客户端</span> | 注册展开下拉框事件回调 |
| [RegisterSelectItemCallback](自定义UI/UI控件.md#registerselectitemcallback) | <span style="display:inline;color:#7575f9">客户端</span> | 注册选中下拉框内容事件回调 |
| [RemoveAnimEndCallback](自定义UI/UI控件.md#removeanimendcallback) | <span style="display:inline;color:#7575f9">客户端</span> | 移除动画播放结束后的回调 |
| [RemoveAnimation](自定义UI/UI控件.md#removeanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 删除单一属性的动画，删除后的值与当前状态有关，建议删除后重新设置该属性值 |
| [RemoveEntityMarker](自定义UI/UI控件.md#removeentitymarker) | <span style="display:inline;color:#7575f9">客户端</span> | 删除实体位置标记 |
| [RemoveEntityTextMarker](自定义UI/UI控件.md#removeentitytextmarker) | <span style="display:inline;color:#7575f9">客户端</span> | 在小地图上删除实体文本标记 |
| [RemoveOptionByIndex](自定义UI/UI控件.md#removeoptionbyindex) | <span style="display:inline;color:#7575f9">客户端</span> | 根据提供的索引移除对应下拉框项，移除成功则返回True，否则返回False |
| [RemoveOptionByShowName](自定义UI/UI控件.md#removeoptionbyshowname) | <span style="display:inline;color:#7575f9">客户端</span> | 根据提供的展示文本移除对应下拉框项，移除成功则返回True，否则返回False |
| [RemoveStaticMarker](自定义UI/UI控件.md#removestaticmarker) | <span style="display:inline;color:#7575f9">客户端</span> | 删除静态位置标记 |
| [RemoveStaticTextMarker](自定义UI/UI控件.md#removestatictextmarker) | <span style="display:inline;color:#7575f9">客户端</span> | 在小地图上删除静态文本标记 |
| [RenderBlockGeometryModel](自定义UI/UI控件.md#renderblockgeometrymodel) | <span style="display:inline;color:#7575f9">客户端</span> | 渲染网格体模型 |
| [RenderEntity](自定义UI/UI控件.md#renderentity) | <span style="display:inline;color:#7575f9">客户端</span> | 渲染实体 |
| [RenderSkeletonModel](自定义UI/UI控件.md#renderskeletonmodel) | <span style="display:inline;color:#7575f9">客户端</span> | 渲染骨骼模型（不依赖实体） |
| [RepaintMiniMap](自定义UI/UI控件.md#repaintminimap) | <span style="display:inline;color:#7575f9">客户端</span> | 重新绘制小地图 |
| [Rotate](自定义UI/UI控件.md#rotate) | <span style="display:inline;color:#7575f9">客户端</span> | 图片相对自身的旋转锚点进行旋转 |
| [RotateAround](自定义UI/UI控件.md#rotatearound) | <span style="display:inline;color:#7575f9">客户端</span> | 图片相对全局坐标系中某个固定的点进行旋转 |
| [SetAlpha](自定义UI/UI控件.md#setalpha) | <span style="display:inline;color:#7575f9">客户端</span> | 设置节点的透明度，仅对image和label控件生效 |
| [SetAnchorFrom](自定义UI/UI控件.md#setanchorfrom) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件相对于父节点的锚点 |
| [SetAnchorTo](自定义UI/UI控件.md#setanchorto) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件自身锚点位置 |
| [SetAnimEndCallback](自定义UI/UI控件.md#setanimendcallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置动画播放结束后的回调，每次设置都会覆盖上一次的设置 |
| [SetAnimation](自定义UI/UI控件.md#setanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 给单一属性设置动画，已有重复的会设置失败，需要先remove |
| [SetButtonHoverInCallback](自定义UI/UI控件.md#setbuttonhoverincallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置鼠标进入按钮时触发的悬浮回调函数 |
| [SetButtonHoverOutCallback](自定义UI/UI控件.md#setbuttonhoveroutcallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置鼠标退出按钮时触发的悬浮回调函数 |
| [SetButtonScreenExitCallback](自定义UI/UI控件.md#setbuttonscreenexitcallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置按钮所在画布退出时若鼠标仍未抬起时触发回调函数 |
| [SetButtonTouchCancelCallback](自定义UI/UI控件.md#setbuttontouchcancelcallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置触控在按钮范围外弹起时触发的回调函数 |
| [SetButtonTouchDownCallback](自定义UI/UI控件.md#setbuttontouchdowncallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置按钮按下时触发的回调函数 |
| [SetButtonTouchMoveCallback](自定义UI/UI控件.md#setbuttontouchmovecallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置按下后触控移动时触发的回调函数 |
| [SetButtonTouchMoveInCallback](自定义UI/UI控件.md#setbuttontouchmoveincallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置按下按钮后进入控件时触发的回调函数 |
| [SetButtonTouchMoveOutCallback](自定义UI/UI控件.md#setbuttontouchmoveoutcallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置按下按钮后退出控件时触发的回调函数 |
| [SetButtonTouchUpCallback](自定义UI/UI控件.md#setbuttontouchupcallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置触控在按钮范围内弹起时的回调函数 |
| [SetClipDirection](自定义UI/UI控件.md#setclipdirection) | <span style="display:inline;color:#7575f9">客户端</span> | 设置图片控件的裁剪方向 |
| [SetClipOffset](自定义UI/UI控件.md#setclipoffset) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件的裁剪偏移信息 |
| [SetClipsChildren](自定义UI/UI控件.md#setclipschildren) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件是否开启裁剪内容 |
| [SetCurrentSliceIndex](自定义UI/UI控件.md#setcurrentsliceindex) | <span style="display:inline;color:#7575f9">客户端</span> | 设置轮盘选择的切片 |
| [SetEditText](自定义UI/UI控件.md#setedittext) | <span style="display:inline;color:#7575f9">客户端</span> | 设置edit_box输入框的文本信息 |
| [SetEditTextMaxLength](自定义UI/UI控件.md#setedittextmaxlength) | <span style="display:inline;color:#7575f9">客户端</span> | 设置输入框的最大输入长度 |
| [SetFullPosition](自定义UI/UI控件.md#setfullposition) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件的锚点坐标（全局坐标），支持比例值以及绝对值 |
| [SetFullSize](自定义UI/UI控件.md#setfullsize) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件的大小，支持比例形式以及绝对值 |
| [SetGridDimension](自定义UI/UI控件.md#setgriddimension) | <span style="display:inline;color:#7575f9">客户端</span> | 设置Grid控件的大小 |
| [SetHighestY](自定义UI/UI控件.md#sethighesty) | <span style="display:inline;color:#7575f9">客户端</span> | 设置绘制地图的最大高度 |
| [SetHoverCallback](自定义UI/UI控件.md#sethovercallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置轮盘选择切片触发回调函数 |
| [SetImageAdaptionType](自定义UI/UI控件.md#setimageadaptiontype) | <span style="display:inline;color:#7575f9">客户端</span> | 设置图片控件的图片适配方式以及信息 |
| [SetIsModal](自定义UI/UI控件.md#setismodal) | <span style="display:inline;color:#7575f9">客户端</span> | 设置当前面板是否为模态框 |
| [SetIsSwallow](自定义UI/UI控件.md#setisswallow) | <span style="display:inline;color:#7575f9">客户端</span> | 设置当前面板输入是否会吞噬事件，isSwallow为Ture时，点击时，点击事件不会穿透到世界。如破坏方块、镜头转向不会被响应 |
| [SetLayer](自定义UI/UI控件.md#setlayer) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件节点的层级，可以通过传入空字符串（""）的方式来调整整个JSON的基础层级 |
| [SetMaxSize](自定义UI/UI控件.md#setmaxsize) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件所允许的最大的大小值 |
| [SetMinSize](自定义UI/UI控件.md#setminsize) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件所允许的最小的大小值 |
| [SetOffsetDelta](自定义UI/UI控件.md#setoffsetdelta) | <span style="display:inline;color:#7575f9">客户端</span> | 设置点击面板的拖拽偏移量 |
| [SetOrientation](自定义UI/UI控件.md#setorientation) | <span style="display:inline;color:#7575f9">客户端</span> | 设置stackPanel的排列方向 |
| [SetPosition](自定义UI/UI控件.md#setposition) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件相对父节点的坐标 |
| [SetPropertyBag](自定义UI/UI控件.md#setpropertybag) | <span style="display:inline;color:#7575f9">客户端</span> | 设置PropertyBag,将使用字典中的每个值来覆盖原本PropertyBag中的值 |
| [SetRotatePivot](自定义UI/UI控件.md#setrotatepivot) | <span style="display:inline;color:#7575f9">客户端</span> | 设置图片自身旋转锚点，该点并不是固定的点，而是相对于自身位置的点 |
| [SetScrollViewPercentValue](自定义UI/UI控件.md#setscrollviewpercentvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 设置当前scroll_view内容的百分比位置 |
| [SetScrollViewPos](自定义UI/UI控件.md#setscrollviewpos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置当前scroll_view内容的位置 |
| [SetSelectOptionByIndex](自定义UI/UI控件.md#setselectoptionbyindex) | <span style="display:inline;color:#7575f9">客户端</span> | 根据提供的索引选中对应下拉框项 |
| [SetSelectOptionByShowName](自定义UI/UI控件.md#setselectoptionbyshowname) | <span style="display:inline;color:#7575f9">客户端</span> | 根据提供的展示文本选中对应下拉框项 |
| [SetSize](自定义UI/UI控件.md#setsize) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件的大小 |
| [SetSliderValue](自定义UI/UI控件.md#setslidervalue) | <span style="display:inline;color:#7575f9">客户端</span> | 设置滑动条的值 |
| [SetSprite](自定义UI/UI控件.md#setsprite) | <span style="display:inline;color:#7575f9">客户端</span> | 给图片控件换指定贴图 |
| [SetSpriteClipRatio](自定义UI/UI控件.md#setspriteclipratio) | <span style="display:inline;color:#7575f9">客户端</span> | 设置图片的裁剪区域比例（不改变控件尺寸）。可以配合image控件的clip_ratio属性控制方向。 |
| [SetSpriteColor](自定义UI/UI控件.md#setspritecolor) | <span style="display:inline;color:#7575f9">客户端</span> | 设置图片颜色 |
| [SetSpriteGray](自定义UI/UI控件.md#setspritegray) | <span style="display:inline;color:#7575f9">客户端</span> | 给图片控件置灰，比直接SetSprite一张灰图片效率要高 |
| [SetSpritePlatformFrame](自定义UI/UI控件.md#setspriteplatformframe) | <span style="display:inline;color:#7575f9">客户端</span> | 设置图片为我的世界移动端启动器当前帐号的头像框 |
| [SetSpritePlatformHead](自定义UI/UI控件.md#setspriteplatformhead) | <span style="display:inline;color:#7575f9">客户端</span> | 设置图片为我的世界移动端启动器当前帐号的头像 |
| [SetSpriteUV](自定义UI/UI控件.md#setspriteuv) | <span style="display:inline;color:#7575f9">客户端</span> | 设置图片的起始uv，与json中的"uv"属性作用一致 |
| [SetSpriteUVSize](自定义UI/UI控件.md#setspriteuvsize) | <span style="display:inline;color:#7575f9">客户端</span> | 设置图片的uv大小，与json中的"uv_size"属性作用一致 |
| [SetText](自定义UI/UI控件.md#settext) | <span style="display:inline;color:#7575f9">客户端</span> | 设置Label的文本信息 |
| [SetTextAlignment](自定义UI/UI控件.md#settextalignment) | <span style="display:inline;color:#7575f9">客户端</span> | 设置文本控件的文本对齐方式 |
| [SetTextColor](自定义UI/UI控件.md#settextcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 设置Label文本的颜色 |
| [SetTextFontSize](自定义UI/UI控件.md#settextfontsize) | <span style="display:inline;color:#7575f9">客户端</span> | 设置Label中文本字体的大小 |
| [SetTextLinePadding](自定义UI/UI控件.md#settextlinepadding) | <span style="display:inline;color:#7575f9">客户端</span> | 设置文本控件的行间距 |
| [SetToggleState](自定义UI/UI控件.md#settogglestate) | <span style="display:inline;color:#7575f9">客户端</span> | 设置Toggle开关控件的值 |
| [SetTouchEnable](自定义UI/UI控件.md#settouchenable) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控件是否可点击交互 |
| [SetTouchUpCallback](自定义UI/UI控件.md#settouchupcallback) | <span style="display:inline;color:#7575f9">客户端</span> | 设置轮盘选择切片并且鼠标按下抬起后触发回调函数 |
| [SetUiItem](自定义UI/UI控件.md#setuiitem) | <span style="display:inline;color:#7575f9">客户端</span> | 设置ItemRenderer控件显示的物品，ItemRenderer控件的配置方式详见<a href="../../../mcguide/18-界面与交互/30-UI说明文档.html#itemrenderer">控件介绍ItemRenderer</a> |
| [SetValue](自定义UI/UI控件.md#setvalue) | <span style="display:inline;color:#7575f9">客户端</span> | 设置进度条的进度 |
| [SetVisible](自定义UI/UI控件.md#setvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 根据控件路径选择是否显示某控件，可以通过传入空字符串（""）的方式来调整整个JSON的显示/隐藏 |
| [StopAnimation](自定义UI/UI控件.md#stopanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 停止动画，动画将恢复到第一段动画片段的from状态 |
| [ZoomIn](自定义UI/UI控件.md#zoomin) | <span style="display:inline;color:#7575f9">客户端</span> | 放大地图 |
| [ZoomOut](自定义UI/UI控件.md#zoomout) | <span style="display:inline;color:#7575f9">客户端</span> | 缩小地图 |
| [ZoomReset](自定义UI/UI控件.md#zoomreset) | <span style="display:inline;color:#7575f9">客户端</span> | 恢复地图放缩大小为默认值 |
| [asButton](自定义UI/UI控件.md#asbutton) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为ButtonUIControl实例，如当前控件非button类型则返回None |
| [asGrid](自定义UI/UI控件.md#asgrid) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为GridUIControl实例，如当前控件非grid类型则返回None |
| [asImage](自定义UI/UI控件.md#asimage) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为ImageUIControl实例，如当前控件非image类型则返回None |
| [asInputPanel](自定义UI/UI控件.md#asinputpanel) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为InputPanelUIControl实例，如当前控件非inputPanel类型则返回None |
| [asItemRenderer](自定义UI/UI控件.md#asitemrenderer) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为ItemRenderer实例，如当前控件非custom类型则返回None |
| [asLabel](自定义UI/UI控件.md#aslabel) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为LabelUIControl实例，如当前控件非Label类型则返回None |
| [asMiniMap](自定义UI/UI控件.md#asminimap) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为MiniMapUIControl实例，如当前控件非小地图类型则返回None |
| [asNeteaseComboBox](自定义UI/UI控件.md#asneteasecombobox) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为NeteaseComboBoxUIControl实例，如当前控件非panel类型则返回None |
| [asNeteasePaperDoll](自定义UI/UI控件.md#asneteasepaperdoll) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为NeteasePaperDollUIControl实例，如当前控件非custom类型则返回None |
| [asProgressBar](自定义UI/UI控件.md#asprogressbar) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为ProgressBarUIControl实例，如当前控件非panel类型则返回None |
| [asScrollView](自定义UI/UI控件.md#asscrollview) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为ScrollViewUIControl实例，如当前控件非scrollview类型则返回None |
| [asSelectionWheel](自定义UI/UI控件.md#asselectionwheel) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为SelectionWheelUIControl实例，如当前控件非selectionWheel类型则返回None |
| [asSlider](自定义UI/UI控件.md#asslider) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为SliderUIControl实例，如当前控件非滑动条类型则返回None |
| [asStackPanel](自定义UI/UI控件.md#asstackpanel) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为StackPanelUIControl实例，如当前控件非stackPanel类型则返回None |
| [asSwitchToggle](自定义UI/UI控件.md#asswitchtoggle) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为SwitchToggleUIControl实例，如当前控件非panel类型或非toggle则返回None |
| [asTextEditBox](自定义UI/UI控件.md#astexteditbox) | <span style="display:inline;color:#7575f9">客户端</span> | 将当前BaseUIControl转换为TextEditBoxUIControl实例，如当前控件非editbox类型则返回None |
| [resetAnimation](自定义UI/UI控件.md#resetanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 重置该控件的动画 |
#### 音效<span id = "音效2"></span>
| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [DisableOriginMusic](音效.md#disableoriginmusic) | <span style="display:inline;color:#7575f9">客户端</span> | 停止原生背景音乐 |
| [PlayCustomMusic](音效.md#playcustommusic) | <span style="display:inline;color:#7575f9">客户端</span> | 播放场景音效，包括原版音效及自定义音效 |
| [PlayCustomUIMusic](音效.md#playcustomuimusic) | <span style="display:inline;color:#7575f9">客户端</span> | 播放UI音效，包括原版音效及自定义音效 |
| [PlayGlobalCustomMusic](音效.md#playglobalcustommusic) | <span style="display:inline;color:#7575f9">客户端</span> | 播放背景音乐 |
| [SetCustomMusicLoop](音效.md#setcustommusicloop) | <span style="display:inline;color:#7575f9">客户端</span> | 设定指定音乐是否循环播放，包括场景音效与背景音乐 |
| [SetCustomMusicLoopById](音效.md#setcustommusicloopbyid) | <span style="display:inline;color:#7575f9">客户端</span> | 设定指定音乐是否循环播放 |
| [StopCustomMusic](音效.md#stopcustommusic) | <span style="display:inline;color:#7575f9">客户端</span> | 停止音效，包括场景音效与背景音乐，将依据fadeOutTime触发OnMusicStopClientEvent事件 |
| [StopCustomMusicById](音效.md#stopcustommusicbyid) | <span style="display:inline;color:#7575f9">客户端</span> | 停止场景音效 |

#### 控制<span id = "控制2"></span>
| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddPickBlacklist](控制.md#addpickblacklist) | <span style="display:inline;color:#7575f9">客户端</span> | 添加使用camera组件（例如GetChosen接口、PickFacing接口）选取实体时的黑名单，即该实体不会被选取到 |
| [ClearPickBlacklist](控制.md#clearpickblacklist) | <span style="display:inline;color:#7575f9">客户端</span> | 清除使用camera组件（例如GetChosen接口、PickFacing接口）选取实体的黑名单 |
| [GetChosen](控制.md#getchosen) | <span style="display:inline;color:#7575f9">客户端</span> | 获取屏幕点击位置的实体或方块信息，通常与GetEntityByCoordEvent配合使用 |
| [GetChosenEntity](控制.md#getchosenentity) | <span style="display:inline;color:#7575f9">客户端</span> | 获取屏幕点击位置的实体id，通常与GetEntityByCoordEvent配合使用 |
| [GetHoldTimeThresholdInMs](控制.md#getholdtimethresholdinms) | <span style="display:inline;color:#7575f9">客户端</span> | 获取长按判定时间，即按着屏幕多长时间会触发长按操作 |
| [GetInputVector](控制.md#getinputvector) | <span style="display:inline;color:#7575f9">客户端</span> | 获取方向键（移动轮盘）的输入 |
| [GetMousePosition](控制.md#getmouseposition) | <span style="display:inline;color:#7575f9">客户端</span> | 获取鼠标位置 |
| [GetTouchPos](控制.md#gettouchpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取点击的屏幕坐标。可以监听TapBeforeClientEvent或TapOrHoldReleaseClientEvent事件，调用本API获取点击坐标。 |
| [IsCanAttack](控制.md#iscanattack) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否响应攻击 |
| [IsCanChat](控制.md#iscanchat) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否响应聊天按钮 |
| [IsCanDrag](控制.md#iscandrag) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否响应屏幕拖动 |
| [IsCanInair](控制.md#iscaninair) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否响应打上升下降按钮 |
| [IsCanJump](控制.md#iscanjump) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否响应跳跃（以及在水中浮起） |
| [IsCanMove](控制.md#iscanmove) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否响应移动 |
| [IsCanOpenInv](控制.md#iscanopeninv) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否响应打开背包按钮 |
| [IsCanPause](控制.md#iscanpause) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否响应暂停按钮 |
| [IsCanPauseScreen](控制.md#iscanpausescreen) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否可以打开暂停界面 |
| [IsCanPerspective](控制.md#iscanperspective) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否响应切换视角 |
| [IsCanScreenShot](控制.md#iscanscreenshot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否响应截图按钮 |
| [IsCanWalkMode](控制.md#iscanwalkmode) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家是否响应切换行走模式 |
| [IsTouchWithMouse](控制.md#istouchwithmouse) | <span style="display:inline;color:#7575f9">客户端</span> | 获取是否正在使用鼠标点击模拟触屏 |
| [LockInputVector](控制.md#lockinputvector) | <span style="display:inline;color:#7575f9">客户端</span> | 锁定本地玩家方向键（移动轮盘）的输入，可使本地玩家持续向指定方向前行，且不会再受玩家输入影响 |
| [LockVerticalMove](控制.md#lockverticalmove) | <span style="display:inline;color:#7575f9">客户端</span> | 模拟上升或下降，调用后一直上升或下降 |
| [PickFacing](控制.md#pickfacing) | <span style="display:inline;color:#7575f9">客户端</span> | 获取准星选中的实体或者方块 |
| [SetCanAll](控制.md#setcanall) | <span style="display:inline;color:#7575f9">客户端</span> | 同时设置SetCanMove，SetCanJump，SetCanAttack，SetCanWalkMode，SetCanPerspective，SetCanPause，SetCanChat，SetCanScreenShot，SetCanOpenInv，SetCanDrag，SetCanInair |
| [SetCanAttack](控制.md#setcanattack) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否响应攻击 |
| [SetCanChat](控制.md#setcanchat) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否响应聊天按钮 |
| [SetCanDrag](控制.md#setcandrag) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否响应屏幕拖动 |
| [SetCanInair](控制.md#setcaninair) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否响应上升下降按钮（飞在空中时右下角的三个按钮） |
| [SetCanJump](控制.md#setcanjump) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否响应跳跃（以及在水中浮起） |
| [SetCanMove](控制.md#setcanmove) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否响应移动 |
| [SetCanOpenInv](控制.md#setcanopeninv) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否响应打开背包按钮 |
| [SetCanPause](控制.md#setcanpause) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否响应暂停按钮 |
| [SetCanPauseScreen](控制.md#setcanpausescreen) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否可以打开暂停界面 |
| [SetCanPerspective](控制.md#setcanperspective) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否响应切换视角 |
| [SetCanScreenShot](控制.md#setcanscreenshot) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否响应截图按钮 |
| [SetCanWalkMode](控制.md#setcanwalkmode) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否响应切换行走模式 |
| [SetControlMode](控制.md#setcontrolmode) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控制模式 |
| [SetControlModeLock](控制.md#setcontrolmodelock) | <span style="display:inline;color:#7575f9">客户端</span> | 设置控制模式是否可以被改变 |
| [SetDeviceVibrate](控制.md#setdevicevibrate) | <span style="display:inline;color:#7575f9">客户端</span> | 设置设备震动 |
| [SetGyroSensorReportRate](控制.md#setgyrosensorreportrate) | <span style="display:inline;color:#7575f9">客户端</span> | 设置陀螺仪传感器(上报/触发)频率 |
| [SetHoldTimeThreshold](控制.md#setholdtimethreshold) | <span style="display:inline;color:#7575f9">客户端</span> | 设置长按判定时间，即按着屏幕多长时间会触发长按操作 |
| [SetMoveLock](控制.md#setmovelock) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否锁住移动。实际上为是否响应十字键与遥感的操作。 |
| [SetShowRideUI](控制.md#setshowrideui) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否显示马匹的UI界面 |
| [SimulateTouchWithMouse](控制.md#simulatetouchwithmouse) | <span style="display:inline;color:#7575f9">客户端</span> | 模拟使用鼠标控制UI（PC F11快捷键） |
| [ToggleGyroSensor](控制.md#togglegyrosensor) | <span style="display:inline;color:#7575f9">客户端</span> | 开启或关闭陀螺仪传感器采集 |
| [UnLockVerticalMove](控制.md#unlockverticalmove) | <span style="display:inline;color:#7575f9">客户端</span> | 解除上升或下降状态 |
| [UnlockInputVector](控制.md#unlockinputvector) | <span style="display:inline;color:#7575f9">客户端</span> | 解锁本地玩家方向键（移动轮盘）的输入 |

#### 游戏设置<span id = "游戏设置2"></span>
| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetControllerLayout](游戏设置.md#getcontrollerlayout) | <span style="display:inline;color:#7575f9">客户端</span> | 获取玩家控制器绑定映射 |
| [GetSliderOption](游戏设置.md#getslideroption) | <span style="display:inline;color:#7575f9">客户端</span> | 获得某个滑动条设置选项的值 |
| [GetToggleOption](游戏设置.md#gettoggleoption) | <span style="display:inline;color:#7575f9">客户端</span> | 获得某个开关设置值的接口 |
| [GetUIProfile](游戏设置.md#getuiprofile) | <span style="display:inline;color:#7575f9">客户端</span> | 获取"UI 档案"模式 |
| [HighlightBoxSelection](游戏设置.md#highlightboxselection) | <span style="display:inline;color:#7575f9">客户端</span> | 镜头移动时高亮当前视角中心所指的方块 |
| [SetSliderOption](游戏设置.md#setslideroption) | <span style="display:inline;color:#7575f9">客户端</span> | 设置某个滑动条设置选项的值 |
| [SetSplitControlCanChange](游戏设置.md#setsplitcontrolcanchange) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否允许使用准星瞄准按钮 |
| [SetToggleOption](游戏设置.md#settoggleoption) | <span style="display:inline;color:#7575f9">客户端</span> | 修改开关型设置的接口 |
| [SetUIProfile](游戏设置.md#setuiprofile) | <span style="display:inline;color:#7575f9">客户端</span> | 设置"UI 档案"模式 |

#### 世界<span id = "世界1"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [VirtualWorldCreate](虚拟世界/世界.md#virtualworldcreate) | <span style="display:inline;color:#7575f9">客户端</span> | 创建虚拟世界，虚拟世界只允许存在一个，已经存在虚拟世界的情况下再调用此方法则无效 |
| [VirtualWorldDestroy](虚拟世界/世界.md#virtualworlddestroy) | <span style="display:inline;color:#7575f9">客户端</span> | 销毁虚拟世界 |
| [VirtualWorldSetCollidersVisible](虚拟世界/世界.md#virtualworldsetcollidersvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 设置虚拟世界中模型的包围盒是否显示,主要用于调试,默认为不显示 |
| [VirtualWorldSetSkyBgColor](虚拟世界/世界.md#virtualworldsetskybgcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 设置虚拟世界中天空背景的颜色 |
| [VirtualWorldSetSkyTexture](虚拟世界/世界.md#virtualworldsetskytexture) | <span style="display:inline;color:#7575f9">客户端</span> | 设置虚拟世界中天空的贴图 |
| [VirtualWorldToggleVisibility](虚拟世界/世界.md#virtualworldtogglevisibility) | <span style="display:inline;color:#7575f9">客户端</span> | 设置虚拟世界是否显示 |
#### 相机
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CameraGetClickModel](虚拟世界/相机.md#cameragetclickmodel) | <span style="display:inline;color:#7575f9">客户端</span> | 获取相机当前指向的模型的id，会返回离相机最近的，通常与GetEntityByCoordEvent配合使用 |
| [CameraGetFov](虚拟世界/相机.md#cameragetfov) | <span style="display:inline;color:#7575f9">客户端</span> | 获取相机视野大小 |
| [CameraGetPos](虚拟世界/相机.md#cameragetpos) | <span style="display:inline;color:#7575f9">客户端</span> | 返回相机位置 |
| [CameraGetZoom](虚拟世界/相机.md#cameragetzoom) | <span style="display:inline;color:#7575f9">客户端</span> | 获取相机的缩放值 |
| [CameraLookAt](虚拟世界/相机.md#cameralookat) | <span style="display:inline;color:#7575f9">客户端</span> | 修改相机朝向 |
| [CameraMoveTo](虚拟世界/相机.md#cameramoveto) | <span style="display:inline;color:#7575f9">客户端</span> | 设置相机移动动画, 会根据当前相机状态与传入参数按时间进行插值显示 |
| [CameraSetFov](虚拟世界/相机.md#camerasetfov) | <span style="display:inline;color:#7575f9">客户端</span> | 设置相机视野大小 |
| [CameraSetPos](虚拟世界/相机.md#camerasetpos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置相机位置 |
| [CameraSetZoom](虚拟世界/相机.md#camerasetzoom) | <span style="display:inline;color:#7575f9">客户端</span> | 设置相机缩放 |
| [CameraStopActions](虚拟世界/相机.md#camerastopactions) | <span style="display:inline;color:#7575f9">客户端</span> | 停止相机移动动画 |
#### 模型<span id = "模型1"></span>
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [ModelCancelAllBoneMask](虚拟世界/模型.md#modelcancelallbonemask) | <span style="display:inline;color:#7575f9">客户端</span> | 取消动画中的所有骨骼屏蔽。 |
| [ModelCreateMinecraftObject](虚拟世界/模型.md#modelcreateminecraftobject) | <span style="display:inline;color:#7575f9">客户端</span> | 在虚拟世界中创建微软原版模型 |
| [ModelCreateObject](虚拟世界/模型.md#modelcreateobject) | <span style="display:inline;color:#7575f9">客户端</span> | 在虚拟世界中创建网易骨骼模型 |
| [ModelGetPos](虚拟世界/模型.md#modelgetpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取模型的坐标 |
| [ModelGetRot](虚拟世界/模型.md#modelgetrot) | <span style="display:inline;color:#7575f9">客户端</span> | 返回模型的旋转角度 |
| [ModelIsVisible](虚拟世界/模型.md#modelisvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 返回模型可见性 |
| [ModelMoveTo](虚拟世界/模型.md#modelmoveto) | <span style="display:inline;color:#7575f9">客户端</span> | 设置模型平移运动 |
| [ModelPlayAnimation](虚拟世界/模型.md#modelplayanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 模型播放动画，支持动作融合，其功能与模型接口ModelPlayAni相同。 |
| [ModelRegisterAnim1DControlParam](虚拟世界/模型.md#modelregisteranim1dcontrolparam) | <span style="display:inline;color:#7575f9">客户端</span> | 当同时播放多个骨骼动画时，新建用于控制动画进行1D线性混合的参数。目前线性混合仅支持对两个动画进行混合。新建的参数值范围为[0,1]。指定的骨骼将会按照这个参数的值对两个动画进行线性混合。 |
| [ModelRemove](虚拟世界/模型.md#modelremove) | <span style="display:inline;color:#7575f9">客户端</span> | 销毁虚拟世界中的模型 |
| [ModelRotate](虚拟世界/模型.md#modelrotate) | <span style="display:inline;color:#7575f9">客户端</span> | 模型绕某个轴旋转多少度 |
| [ModelRotateTo](虚拟世界/模型.md#modelrotateto) | <span style="display:inline;color:#7575f9">客户端</span> | 设置模型旋转运动 |
| [ModelSetAnim1DControlParam](虚拟世界/模型.md#modelsetanim1dcontrolparam) | <span style="display:inline;color:#7575f9">客户端</span> | 新建动画的1D控制参数后，使用该接口对相应的参数进行控制。 |
| [ModelSetAnimAllBoneMask](虚拟世界/模型.md#modelsetanimallbonemask) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否屏蔽动画中所有骨骼的动画，若开启骨骼屏蔽后，该骨骼将不再播放该动画中的动作。该接口会对该动画中所有骨骼生效，可通过参数ignoreBoneList来指定不受影响的骨骼名称。通过屏蔽指定骨骼的动画可实现同一个骨骼模型同时在不同骨骼上播放不同的动作动画，从而实现快捷的动作融合。 |
| [ModelSetAnimBoneMask](虚拟世界/模型.md#modelsetanimbonemask) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否屏蔽动画中指定的骨骼的动画，若开启骨骼屏蔽后，该骨骼将不再播放该动画中的动作。通过屏蔽指定骨骼的动画可实现同一个骨骼模型同时在不同骨骼上播放不同的动作动画，从而实现快捷的动作融合。 |
| [ModelSetAnimLayer](虚拟世界/模型.md#modelsetanimlayer) | <span style="display:inline;color:#7575f9">客户端</span> | 设置骨骼动画的层级，动画层级越大，则优先度越高，骨骼模型的骨骼优先播放优先度最高的动画，相同层级的动画则优先播放率先播放的动画。 |
| [ModelSetBoxCollider](虚拟世界/模型.md#modelsetboxcollider) | <span style="display:inline;color:#7575f9">客户端</span> | 设置模型的包围盒 |
| [ModelSetPos](虚拟世界/模型.md#modelsetpos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置模型坐标 |
| [ModelSetRot](虚拟世界/模型.md#modelsetrot) | <span style="display:inline;color:#7575f9">客户端</span> | 设置模型的旋转角度 |
| [ModelSetScale](虚拟世界/模型.md#modelsetscale) | <span style="display:inline;color:#7575f9">客户端</span> | 设置模型的缩放值 |
| [ModelSetVisible](虚拟世界/模型.md#modelsetvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 设置模型可见性 |
| [ModelStopActions](虚拟世界/模型.md#modelstopactions) | <span style="display:inline;color:#7575f9">客户端</span> | 停止模型的移动和旋转运动 |
| [ModelStopAnimation](虚拟世界/模型.md#modelstopanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 停止播放指定的模型动画。 |
| [ModelUpdateAnimationMolangVariable](虚拟世界/模型.md#modelupdateanimationmolangvariable) | <span style="display:inline;color:#7575f9">客户端</span> | 更新微软原版模型表达式变量，可控制动作的改变 |
#### 其它对象
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [BindModel](虚拟世界/其它对象.md#bindmodel) | <span style="display:inline;color:#7575f9">客户端</span> | 把对象绑定到模型上, 支持绑定序列帧，粒子，文本和其它模型 |
| [MoveToVirtualWorld](虚拟世界/其它对象.md#movetovirtualworld) | <span style="display:inline;color:#7575f9">客户端</span> | 把对象从主世界移到虚拟世界, 非绑定的序列帧，文本，粒子需要调用该方法后才会出现在虚拟世界中，绑定的可以省略调用该方法。 |
#### 渐晕
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CheckVignetteEnabled](后处理/渐晕.md#checkvignetteenabled) | <span style="display:inline;color:#7575f9">客户端</span> | 检测是否开启了屏幕渐晕（Vignette）效果。 |
| [SetEnableVignette](后处理/渐晕.md#setenablevignette) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否开启屏幕渐晕（Vignette）效果，开启后玩家屏幕周围将出现渐晕，可通过Vignette其他接口设置效果参数。 |
| [SetVignetteCenter](后处理/渐晕.md#setvignettecenter) | <span style="display:inline;color:#7575f9">客户端</span> | 设置渐晕（Vignette）的渐晕中心位置，可改变屏幕渐晕的位置。 |
| [SetVignetteRGB](后处理/渐晕.md#setvignettergb) | <span style="display:inline;color:#7575f9">客户端</span> | 设置渐晕（Vignette）的渐晕颜色，可改变屏幕渐晕的颜色。 |
| [SetVignetteRadius](后处理/渐晕.md#setvignetteradius) | <span style="display:inline;color:#7575f9">客户端</span> | 设置渐晕（Vignette）的渐晕半径，半径越大，渐晕越小，玩家的视野范围越大。 |
| [SetVignetteSmoothness](后处理/渐晕.md#setvignettesmoothness) | <span style="display:inline;color:#7575f9">客户端</span> | 设置渐晕（Vignette）的渐晕模糊系数，模糊系数越大，则渐晕边缘越模糊，模糊的范围也越大 |
#### 模糊
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CheckGaussianBlurEnabled](后处理/模糊.md#checkgaussianblurenabled) | <span style="display:inline;color:#7575f9">客户端</span> | 检测是否开启了高斯模糊效果。 |
| [SetEnableGaussianBlur](后处理/模糊.md#setenablegaussianblur) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否开启高斯模糊效果，开启后玩家屏幕周围被模糊，可通过高斯模糊其他接口设置效果参数。 |
| [SetGaussianBlurRadius](后处理/模糊.md#setgaussianblurradius) | <span style="display:inline;color:#7575f9">客户端</span> | 设置高斯模糊效果的模糊半径，半径越大，模糊程度越大，反之则模糊程度越小。 |
#### 色彩
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CheckColorAdjustmentEnabled](后处理/色彩.md#checkcoloradjustmentenabled) | <span style="display:inline;color:#7575f9">客户端</span> | 检测是否开启了色彩校正效果。 |
| [SetColorAdjustmentBrightness](后处理/色彩.md#setcoloradjustmentbrightness) | <span style="display:inline;color:#7575f9">客户端</span> | 调整屏幕色彩亮度，亮度值越大，屏幕越亮，反之则越暗。 |
| [SetColorAdjustmentContrast](后处理/色彩.md#setcoloradjustmentcontrast) | <span style="display:inline;color:#7575f9">客户端</span> | 调整屏幕色彩对比度，屏幕对比度值越大，色彩差异则越明显，反之则色彩差异越小。 |
| [SetColorAdjustmentSaturation](后处理/色彩.md#setcoloradjustmentsaturation) | <span style="display:inline;color:#7575f9">客户端</span> | 调整屏幕色彩饱和度，屏幕饱和度值越大，色彩则越明显，反之则越灰暗。 |
| [SetColorAdjustmentTint](后处理/色彩.md#setcoloradjustmenttint) | <span style="display:inline;color:#7575f9">客户端</span> | 调整屏幕色彩的色调，根据输入的色调和强度来调整屏幕色彩，当强度越大时，屏幕整体颜色越偏向输入的色调。 |
| [SetEnableColorAdjustment](后处理/色彩.md#setenablecoloradjustment) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否开启色彩校正效果，开启后可进行屏幕色彩调整，可通过色彩校正效果其他接口设置效果参数。 |
#### 镜头效果
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CheckDepthOfFieldEnabled](后处理/镜头效果.md#checkdepthoffieldenabled) | <span style="display:inline;color:#7575f9">客户端</span> | 检测是否开启了景深效果。 |
| [CheckLensStainEnabled](后处理/镜头效果.md#checklensstainenabled) | <span style="display:inline;color:#7575f9">客户端</span> | 检测是否开启了镜头污迹效果。 |
| [ResetLensStainTexture](后处理/镜头效果.md#resetlensstaintexture) | <span style="display:inline;color:#7575f9">客户端</span> | 重置污迹效果使用的贴图为系统默认贴图。 |
| [SetDepthOfFieldBlurRadius](后处理/镜头效果.md#setdepthoffieldblurradius) | <span style="display:inline;color:#7575f9">客户端</span> | 调整景深效果模糊半径，模糊半径越大，模糊程度越大，反之则越小。 |
| [SetDepthOfFieldFarBlurScale](后处理/镜头效果.md#setdepthoffieldfarblurscale) | <span style="display:inline;color:#7575f9">客户端</span> | 调整景深效果远景模糊大小，远景模糊大小越大，远景的模糊程度越大，反之则越小。注意，远景模糊程度的调节依赖于焦点距离，如果焦点处于较近的距离，那么此时远景处于较清晰的状态，模糊程度大小调节不会很明显。 |
| [SetDepthOfFieldFocusDistance](后处理/镜头效果.md#setdepthoffieldfocusdistance) | <span style="display:inline;color:#7575f9">客户端</span> | 调整景深效果焦点距离，距离越小，则远处模糊，近处清晰；距离越大，则远处清晰，近处模糊。该距离为实际距离，即以玩家相机为起点的世界坐标距离。 |
| [SetDepthOfFieldNearBlurScale](后处理/镜头效果.md#setdepthoffieldnearblurscale) | <span style="display:inline;color:#7575f9">客户端</span> | 调整景深效果近景模糊大小，近景模糊大小越大，近景的模糊程度越大，反之则越小。注意，近景模糊程度的调节依赖于焦点距离，如果焦点处于较近的距离，那么此时近景处于较清晰的状态，模糊程度大小调节不会很明显。 |
| [SetDepthOfFieldUseCenterFocus](后处理/镜头效果.md#setdepthoffieldusecenterfocus) | <span style="display:inline;color:#7575f9">客户端</span> | 设置景深效果是否开启屏幕中心聚焦模式，开启后聚焦距离将被自动设置为屏幕中心所对应的物体所在的距离。在第一人称视角下，聚焦距离将被自动设置为屏幕准心所对应的物体与相机的距离，即自动聚焦准心所对应的物体。在第三人称视角下，由于屏幕中心总是对应着玩家，因此聚焦距离将被自动设置为玩家与相机的距离，即自动聚焦在玩家自己。 |
| [SetEnableDepthOfField](后处理/镜头效果.md#setenabledepthoffield) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否开启景深效果，开启后屏幕出现景深效果，根据焦点距离呈现远处模糊近处清晰或者近处模糊远处清晰的效果。 |
| [SetEnableLensStain](后处理/镜头效果.md#setenablelensstain) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否开启镜头污迹效果，开启后镜头出现污迹效果，可改变使用的污迹贴图及污迹颜色。 |
| [SetLensStainColor](后处理/镜头效果.md#setlensstaincolor) | <span style="display:inline;color:#7575f9">客户端</span> | 调整镜头污迹颜色，根据输入的颜色和强度来调整污迹色彩，当强度越大时，污迹颜色越偏向输入的颜色。 |
| [SetLensStainIntensity](后处理/镜头效果.md#setlensstainintensity) | <span style="display:inline;color:#7575f9">客户端</span> | 调整镜头污迹强度，强度越大，污迹越明显，反之则越透明。 |
| [SetLensStainTexture](后处理/镜头效果.md#setlensstaintexture) | <span style="display:inline;color:#7575f9">客户端</span> | 开启镜头污迹效果后，污迹效果使用的为系统默认贴图。该接口可改变镜头污迹所使用的贴图。注意贴图最好使用透明背景，否则屏幕将被贴图覆盖。 |
#### 自定义
| 接口| <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddPostProcess](后处理/自定义.md#addpostprocess) | <span style="display:inline;color:#7575f9">客户端</span> | 添加后处理效果，与graphics_settings/post_process.json定义的process等效 |
| [CheckEnabledByName](后处理/自定义.md#checkenabledbyname) | <span style="display:inline;color:#7575f9">客户端</span> | 查询是否开启了自定义后处理效果 |
| [GetParameter](后处理/自定义.md#getparameter) | <span style="display:inline;color:#7575f9">客户端</span> | 获取指定自定义后处理参数的值 |
| [GetPostProcessOrder](后处理/自定义.md#getpostprocessorder) | <span style="display:inline;color:#7575f9">客户端</span> | 获取后处理效果的渲染顺序 |
| [InsertPassToPostprocess](后处理/自定义.md#insertpasstopostprocess) | <span style="display:inline;color:#7575f9">客户端</span> | 往自定义后处理的多pass中的指定位置插入自定义pass。多pass指定的是graphics_settings/post_process.json中的"pass_array"渲染pass数组。这个后处理会按照这个数组所定义的pass来逐个渲染，每个pass之间的像素输入输出相互连接，即pass数组中第一个pass所使用的fragment shader中的TEXTURE_0为游戏原始输出到屏幕的像素信息。下一个pass所使用的fragment shader中的TEXTURE_0为上一个Pass的fragment shader的输出。最后一个pass的fragment shader的输出即为输出到游戏屏幕的像素信息。 |
| [PopBackPassInPostprocess](后处理/自定义.md#popbackpassinpostprocess) | <span style="display:inline;color:#7575f9">客户端</span> | 删除自定义后处理的多pass的最末尾的pass。多pass指定的是graphics_settings/post_process.json中的"pass_array"渲染pass数组。这个后处理会按照这个数组所定义的pass来逐个渲染，每个pass之间的像素输入输出相互连接，即pass数组中第一个pass所使用的fragment shader中的TEXTURE_0为游戏原始输出到屏幕的像素信息。下一个pass所使用的fragment shader中的TEXTURE_0为上一个Pass的fragment shader的输出。最后一个pass的fragment shader的输出即为输出到游戏屏幕的像素信息。 |
| [PostPassResultToOtherPass](后处理/自定义.md#postpassresulttootherpass) | <span style="display:inline;color:#7575f9">客户端</span> | 将自定义pass的纹理结果传递到其他自定义pass的fragmentShader指定纹理单元槽位 |
| [PushBackPassToPostprocess](后处理/自定义.md#pushbackpasstopostprocess) | <span style="display:inline;color:#7575f9">客户端</span> | 往自定义后处理的多pass最末尾插入自定义pass。多pass指定的是graphics_settings/post_process.json中的"pass_array"渲染pass数组。这个后处理会按照这个数组所定义的pass来逐个渲染，每个pass之间的像素输入输出相互连接，即pass数组中第一个pass所使用的fragment shader中的TEXTURE_0为游戏原始输出到屏幕的像素信息。下一个pass所使用的fragment shader中的TEXTURE_0为上一个Pass的fragment shader的输出。最后一个pass的fragment shader的输出即为输出到游戏屏幕的像素信息。 |
| [RemovePassInPostprocess](后处理/自定义.md#removepassinpostprocess) | <span style="display:inline;color:#7575f9">客户端</span> | 删除自定义后处理的多pass中指定位置的pass。多pass指定的是graphics_settings/post_process.json中的"pass_array"渲染pass数组。这个后处理会按照这个数组所定义的pass来逐个渲染，每个pass之间的像素输入输出相互连接，即pass数组中第一个pass所使用的fragment shader中的TEXTURE_0为游戏原始输出到屏幕的像素信息。下一个pass所使用的fragment shader中的TEXTURE_0为上一个Pass的fragment shader的输出。最后一个pass的fragment shader的输出即为输出到游戏屏幕的像素信息。 |
| [SetEnableByName](后处理/自定义.md#setenablebyname) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否开启自定义后处理效果 |
| [SetParameter](后处理/自定义.md#setparameter) | <span style="display:inline;color:#7575f9">客户端</span> | 设置自定义后处理shader的自定义参数值 |
#### 联机大厅<span id = "联机大厅2"></span>
| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetPlayerUid](联机大厅.md#getplayeruid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家的uid。只有在线玩家才可获取 |
| [LobbyGetStorage](联机大厅.md#lobbygetstorage) | <span style="display:inline;color:#ff5555">服务端</span> | 获取存储的数据。仅联机大厅可用 |
| [LobbyGetStorageBySort](联机大厅.md#lobbygetstoragebysort) | <span style="display:inline;color:#ff5555">服务端</span> | 排序获取存储的数据。仅联机大厅可用 |
| [LobbySetStorageAndUserItem](联机大厅.md#lobbysetstorageanduseritem) | <span style="display:inline;color:#ff5555">服务端</span> | 设置订单已发货或者存数据。仅联机大厅可用 |
| [QueryLobbyUserItem](联机大厅.md#querylobbyuseritem) | <span style="display:inline;color:#ff5555">服务端</span> | 查询还没发货的订单。仅联机大厅可用 |

#### 成就<span id = "成就2"></span>
| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [LobbyGetAchievementStorage](成就.md#lobbygetachievementstorage) | <span style="display:inline;color:#ff5555">服务端</span> | 获取成就节点的存储的数据。 |
| [LobbySetAchievementStorage](成就.md#lobbysetachievementstorage) | <span style="display:inline;color:#ff5555">服务端</span> | 添加成就节点的进度。 |

#### 商城<span id = "商城2"></span>
| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [CloseShopWindow](商城.md#closeshopwindow) | <span style="display:inline;color:#7575f9">客户端</span> | 关闭网易商城窗口 |
| [HideShopGate](商城.md#hideshopgate) | <span style="display:inline;color:#7575f9">客户端</span> | 隐藏网易商城入口 |
| [OpenItemDetailWindow](商城.md#openitemdetailwindow) | <span style="display:inline;color:#7575f9">客户端</span> | 打开特定商品的详情界面 |
| [OpenShopWindow](商城.md#openshopwindow) | <span style="display:inline;color:#7575f9">客户端</span> | 打开网易商城窗口。PC端无效（Apollo的PC端请使用商城插件） |
| [ShowShopGate](商城.md#showshopgate) | <span style="display:inline;color:#7575f9">客户端</span> | 显示网易商城入口 |

#### 渲染<span id = "渲染2"></span>
| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddArrowShape](渲染.md#addarrowshape) | <span style="display:inline;color:#7575f9">客户端</span> | 新建箭头形状 |
| [AddBoxShape](渲染.md#addboxshape) | <span style="display:inline;color:#7575f9">客户端</span> | 新建盒子形状 |
| [AddCircleShape](渲染.md#addcircleshape) | <span style="display:inline;color:#7575f9">客户端</span> | 新建圆形状 |
| [AddLineShape](渲染.md#addlineshape) | <span style="display:inline;color:#7575f9">客户端</span> | 新建线条形状 |
| [AddSphereShape](渲染.md#addsphereshape) | <span style="display:inline;color:#7575f9">客户端</span> | 新建球形状 |
| [AddTextShape](渲染.md#addtextshape) | <span style="display:inline;color:#7575f9">客户端</span> | 新建文本形状 |
| [GetBoxScale](渲染.md#getboxscale) | <span style="display:inline;color:#7575f9">客户端</span> | 获取BoxShape的大小 |
| [GetColor](渲染.md#getcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 获取Shape的颜色 |
| [GetEndPos](渲染.md#getendpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取LineShape或ArrowShape的结束位置 |
| [GetLength](渲染.md#getlength) | <span style="display:inline;color:#7575f9">客户端</span> | 获取ArrowShape的头部长度 |
| [GetPos](渲染.md#getpos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取Shape的位置 |
| [GetPriority](渲染.md#getpriority) | <span style="display:inline;color:#7575f9">客户端</span> | 获取Shape的优先级 |
| [GetRadius](渲染.md#getradius) | <span style="display:inline;color:#7575f9">客户端</span> | 获取CircleShape或ArrowShape或SphereShape的半径 |
| [GetSegments](渲染.md#getsegments) | <span style="display:inline;color:#7575f9">客户端</span> | 获取CircleShape或ArrowShape头部的分段数 |
| [GetText](渲染.md#gettext) | <span style="display:inline;color:#7575f9">客户端</span> | 获取TextShape的文本 |
| [GetType](渲染.md#gettype) | <span style="display:inline;color:#7575f9">客户端</span> | 获取Shape的类型 |
| [GetVisible](渲染.md#getvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 获取Shape是否可见 |
| [Remove](渲染.md#remove) | <span style="display:inline;color:#7575f9">客户端</span> | 删除Shape |
| [RemoveAll](渲染.md#removeall) | <span style="display:inline;color:#7575f9">客户端</span> | 删除当前所有Shape |
| [SetBoxScale](渲染.md#setboxscale) | <span style="display:inline;color:#7575f9">客户端</span> | 设置BoxShape的大小 |
| [SetColor](渲染.md#setcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 设置Shape的颜色 |
| [SetEndPos](渲染.md#setendpos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置LineShape或ArrowShape的结束位置 |
| [SetLength](渲染.md#setlength) | <span style="display:inline;color:#7575f9">客户端</span> | 设置组成ArrowShape头部的长度 |
| [SetPos](渲染.md#setpos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置Shape的位置 |
| [SetPriority](渲染.md#setpriority) | <span style="display:inline;color:#7575f9">客户端</span> | 设置Shape的渲染优先级, 同一像素点处优先渲染优先级高的Shape, 默认为0 |
| [SetRadius](渲染.md#setradius) | <span style="display:inline;color:#7575f9">客户端</span> | 设置CircleShape或ArrowShape或SphereShape的半径 |
| [SetSegments](渲染.md#setsegments) | <span style="display:inline;color:#7575f9">客户端</span> | 设置组成ArrowShape头部的网格数量, 最小为3 |
| [SetText](渲染.md#settext) | <span style="display:inline;color:#7575f9">客户端</span> | 设置TextShape的文本内容 |
| [SetVisible](渲染.md#setvisible) | <span style="display:inline;color:#7575f9">客户端</span> | 设置Shape是否可见 |

