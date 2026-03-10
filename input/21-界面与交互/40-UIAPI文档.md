---
front:
hard: 入门
time: 分钟
sidebarDepth: 1
---

# <span id="UI API"></span>UI API

下面是UI的一些API接口文档，关于UI的使用请参照[UI使用文档](30-UI说明文档.html)。

下面的文档分为两个部分，一部分是在extraClientApi中，另一部分是ScreenNode基类的成员函数。

<span id="extraClientApi"></span>
## extraClientApi

有一部分UI相关的接口分布在<a href="../../mcdocs/1-ModAPI/接口/自定义UI/通用.html" rel="noopenner"> extraClientApi的通用UI接口 </a>中。

<span id="ScreenNode"></span>

## ScreenNode

ScreenNode的一些有用的函数，界面Node节点的获取方式在[UI使用文档](30-UI说明文档.html)中有详细说明。

```python
import mod.client.extraClientApi as clientApi
uiNode = clientApi.GetUI("myModName", "myUIName")
```

假设下文中的函数，uiNode为获取到的ScreenNode继承类，调用的UI界面是按下面的节点树组织结构的

```
my_namespace
| main
	| image
	| image_button
	| text1
	| panel
		| text2
	| panel2
		| text_edit_box
```

#### ScreenNode的相关接口可参见<a href="../../mcdocs/1-ModAPI/接口/自定义UI/UI界面.html#screennode" rel="noopenner"> 这里 </a>


<span id="MiniMapBaseScreen"></span>
## MiniMapBaseScreen

MiniMapBaseScreen继承于ScreenNode，实现了小地图基本的功能，并且封装了一些操作小地图的接口。
备注：该功能属于[实验性功能](../20-玩法开发/13-模组SDK编程/10-实验性功能.md)，目前在低端机可能会出现性能问题，建议开发者合理地使用该功能。
注意事项：
1）不建议在飞行模式或者跑图模式下开启小地图；
2）如果重写了Create接口，请先调用一下MiniMapBaseScreen.Create(self)；
3）如果重写了Destroy接口，请先调用一下MiniMapBaseScreen.Destroy(self)；

#### MiniMapBaseScreen的相关接口可参见<a href="../../mcdocs/1-ModAPI/接口/自定义UI/UI界面.html#minimapbasescreen" rel="noopenner"> 这里 </a>

