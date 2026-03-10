---
sidebarDepth: 1
---
# UI控件

## AddEntityMarker

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    增加实体位置标记

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体Id |
    | texturePath | str | 头顶ICON贴图，如textures/blocks/border |
    | size | tuple(float,float) | 贴图大小，默认为(4,4) |
    | enableRotation | bool | 是否启用实体朝向，默认为False |
    | isRevertZRot | bool | 是否翻转实体Z轴旋转，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否增加成功 |

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.AddEntityMarker(entityId, "textures/ui/custom_head")
```



## AddEntityTextMarker

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    在小地图上增加实体文本标记

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体Id |
    | text | str | 文本的内容，可以支持[样式代码](https://zh.minecraft.wiki/w/%E6%A0%BC%E5%BC%8F%E5%8C%96%E4%BB%A3%E7%A0%81)（§可以设置文字的颜色、格式等，该种用法更加灵活多变） |
    | scale | float | 文本缩放倍数，等于文本控件json中的font_scale_factor参数，默认缩放倍数为1.0 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否增加成功 |

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.AddEntityTextMarker(entityId, "just test", 1.0)
```



## AddHoverEventParams

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.buttonUIControl.ButtonUIControl

- 描述

    开启按钮的悬浮回调功能，不调用该函数则按钮无悬浮回调

- 参数

    无

- 返回值

    无

- 备注
    - 只有PC能生效，且只有PushScreen生成UI时生成的鼠标能产生悬浮回调！

- 示例

```python
buttonPath = "/panel/test_btn"
buttonUIControl = uiNode.GetBaseUIControl("/panel/test_btn").asButton()
buttonUIControl.AddHoverEventParams()
```



## AddOption

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    添加下拉框项，若添加成功则返回True，否则返回False

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | showName | str | 显示文本，必填参数 |
    | icon | str | 贴图路径，若填写则在下拉框项前端会显示该icon，默认为None |
    | userData | any | 自定义数据，在选中该下拉框项时会跟随回调函数传回，默认为None |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否添加成功 |

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
success = comboBoxUIControl.AddOption("测试项", "textures/ui/test_icon", {"mydata": "netease"})
```



## AddStaticMarker

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    增加地图上静态位置的标记

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 标记Id |
    | vec2 | tuple(float,float) | 地图位置二维坐标(x,z) |
    | texturePath | str | 贴图路径 |
    | size | tuple(float,float) | 贴图大小，默认为(4,4) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否增加成功 |

- 备注
    - 如使用该接口请勿将地图缩小倍数设置过大（建议ZoomOut设置后的地图倍数不小于原地图大小的0.5倍），以免造成地图缩小后静态标记位置失效等问题。

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.AddStaticMarker("this_is_marker_key", (10,2), "textures/blocks/border", (3,3))
```



## AddStaticTextMarker

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    在小地图上增加静态文本的标记

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 标记Id |
    | vec2 | tuple(float,float) | 地图位置二维坐标(x,z) |
    | text | str | 文本的内容，可以支持[样式代码](https://zh.minecraft.wiki/w/%E6%A0%BC%E5%BC%8F%E5%8C%96%E4%BB%A3%E7%A0%81)（§可以设置文字的颜色、格式等，该种用法更加灵活多变） |
    | scale | float | 文本缩放倍数，等于文本控件json中的font_scale_factor参数，默认缩放倍数为1.0 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否增加成功 |

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.AddStaticTextMarker("this_is_marker_key", (10,2), "just test", 1.0)
```



## AddTouchEventParams

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.buttonUIControl.ButtonUIControl

- 描述

    开启按钮回调功能，不调用该函数则按钮无回调

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | args | dict | 默认为None，详细说明请见备注。 |

- 返回值

    无

- 备注
    - AddTouchEventParams参数args说明：
        | 关键字     | 数据类型              | 说明     |
        | ----------| --------------------- | ---------|
        | isSwallow | bool | 默认为True, 按钮是否吞噬事件；或为Ture时，点击按钮时，点击事件不会穿透到世界。如破坏方块、镜头转向不会被响应|

- 示例

```python
buttonPath = "/panel/test_btn"
buttonUIControl = uiNode.GetBaseUIControl("/panel/test_btn").asButton()
buttonUIControl.AddTouchEventParams({"isSwallow":True})
```



## ClearOptions

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    清空下拉框

- 参数

    无

- 返回值

    无

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
comboBoxUIControl.ClearOptions()
```



## ClearSelection

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    清除当前选中，使下拉框恢复未选中内容状态

- 参数

    无

- 返回值

    无

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
comboBoxUIControl.ClearSelection()
```



## DisableTextShadow

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    关闭文本控件显示阴影

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# we want to diable text2 textShadow
text2Path = "/panel/text2"
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
ret = labelUIControl.DisableTextShadow()
```



## EnableTextShadow

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    使文本控件显示阴影

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# we want to enable text2 textShadow
text2Path = "/panel/text2"
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
ret = labelUIControl.EnableTextShadow()
```



## GetAnchorFrom

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    判断控件相对于父节点的哪个锚点来计算位置与大小

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 控件计算位置大小所依赖的父节点锚点位置信息，具体返回值的意义可参考SetAnchorFrom接口的备注 |

- 示例

```python
# we want to get image1 anchorFrom
imagePath = "/panel/image1"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
anchorFrom = baseUIControl.GetAnchorFrom()
```



## GetAnchorTo

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    获取控件自身锚点位置信息

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 该控件自身锚点位置信息，具体返回值的意义可参考SetAnchorTo接口的备注 |

- 示例

```python
# we want to get image1 anchorTo
imagePath = "/panel/image1"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
anchorTo = baseUIControl.GetAnchorTo()
```



## GetChildByName

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    根据子控件的名称获取BaseUIControl实例

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | childName | str | 子节点名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseUIControl | 子控件的BaseUIControl实例 |

- 示例

```python
# text1的BaseUIControl实例获得text2的BaseUIControl实例
text1Path = "/text1"
text1Control = uiNode.GetBaseUIControl(text1Path)
text2Control = text1Control.GetChildByName("text2")
```



## GetChildByPath

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    根据相对路径获取BaseUIControl实例

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | childPath | str | 相对当前BaseUIControl路径的路径 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseUIControl | 子控件的BaseUIControl实例 |

- 示例

```python
# 根据路径"/text1"的BaseUIControl实例获得路径为"/text1/text2/text3"的BaseUIControl实例
text1Path = "/text1"
text1Control = uiNode.GetBaseUIControl(text1Path)
text3Control = text1Control.GetChildByPath("/text2/text3")
```



## GetClipDirection

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    获取图片控件的裁剪方向

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 图片控件的裁剪方向，返回值的意义可见SetClipDirection接口的备注 |

- 示例

```python
imagePath = "/image"
imageUIControl = uiNode.GetBaseUIControl(imagePath).asImage()
imageUIControl.GetClipDirection()
```



## GetClipOffset

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    获取控件的裁剪偏移信息

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 该控件的裁剪偏移信息，第一项为横轴，第二项为纵轴 |

- 示例

```python
# we want to get image1 clipOffset
imagePath = "/panel/image1"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
clipOffset = baseUIControl.GetClipOffset()
```



## GetClipsChildren

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    根据控件路径返回某控件是否开启裁剪内容

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 该控件是否已开启裁剪内容 |

- 示例

```python
# we want to know whether image1 enables clipsChildren
imagePath = "/panel/image1"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
clipsChildrenEnabled = baseUIControl.GetClipsChildren()
```



## GetCurrentSliceIndex

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.selectionWheelUIControl.SelectionWheelUIControl

- 描述

    获取轮盘当前选择的切片的index，一般是在SetHoverCallback和SetTouchUpCallback中使用，表示当前鼠标悬浮或者点击的轮盘切片index

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 轮盘当前选择的切片的index，-1表示轮盘当前没有选择任何切片 |

- 示例

```python
selectionWheelPath = "/selectionWheel"
selectionWheelControl = uiNode.GetBaseUIControl(selectionWheelPath).asSelectionWheel()
selectionWheelControl.GetCurrentSliceIndex()
```



## GetEditText

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.textEditBoxUIControl.TextEditBoxUIControl

- 描述

    获取edit_box输入框的文本信息，获取失败会返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 文本信息 |

- 备注
    - 获取失败通常是由于路径填写错误，或该控件不是edit_box类型

- 示例

```python
# we want to get edit2 content
editBoxPath = "/panel/edit2"
textEditBoxUIControl = uiNode.GetBaseUIControl(editBoxPath).asTextEditBox()
text = textEditBoxUIControl.GetEditText()
```



## GetFullPosition

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    获取控件的锚点坐标，支持比例值以及绝对值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | axis | str | 要获取的轴向，可选的值有["x","y"]，"x"表示获取控件的x坐标，"y"表示获取控件的y坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 控件的大小信息，详见备注 |

- 备注
    - 参见SetFullPosition接口，控件的大小信息描述可由 absoluteValue， followType， relativeValue三个属性描述
        因此返回值的结构如下：
        | 键值     | 类型      |
        | ----------------| -------------|
        | "absoluteValue"  | float |
        | "followType"    | str |
        | "relativeValue"     | float |

- 示例

```python
imagePath = "/panel/image1"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
# 获取image1的锚点x坐标
ret = baseUIControl.GetFullPosition(axis="x")
```



## GetFullSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    获取控件的大小，支持百分比以及绝对值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | axis | str | 要获取的轴向，可选的值有["x","y"]，"x"表示获取控件的宽度，"y"表示获取控件的高度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 控件的大小信息，详见备注 |

- 备注
    - 参见SetFullSize接口，控件的大小信息描述可由 absoluteValue， followType， relativeValue， fit四个属性描述
        因此返回值的结构如下：
        | 键值     | 类型      |
        | ----------------| -------------|
        | "absoluteValue"  | float |
        | "followType"    | str |
        | "relativeValue"     | float |
        | "fit"   | bool |

- 示例

```python
imagePath = "/panel/image1"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
# 获取image1的宽度信息
ret = baseUIControl.GetFullSize(axis="x")
```



## GetGlobalPosition

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    获取控件全局坐标

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 该控件全局坐标信息，第一项为横轴，第二项为纵轴 |

- 示例

```python
# we want to get text2 global position
text2Path = "/panel/text2"
baseUIControl = uiNode.GetBaseUIControl(text2Path)
textPosition = baseUIControl.GetGlobalPosition()
```



## GetGlobalRotateAngle

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    获取图片通过RotateAround函数设置进去的角度值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 获取图片通过RotateAround函数设置进去的角度值 |

- 示例

```python
imagePath = "/imagePath"
imageControl = uiNode.GetBaseUIControl(imagePath).asImage()
print imageControl.GetGlobalRotateAngle()
```



## GetGlobalRotatePoint

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    获取图片通过RotateAround函数设置进去的point值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 获取图片通过RotateAround函数设置进去的point值 |

- 示例

```python
imagePath = "/imagePath"
imageControl = uiNode.GetBaseUIControl(imagePath).asImage()
print imageControl.GetGlobalRotatePoint()
```



## GetGridItem

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.gridUIControl.GridUIControl

- 描述

    根据网格位置获取元素控件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | x | int | 元素在网格的横坐标 |
    | y | int | 元素在网格的纵坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseUIControl | 网格的子节点控件 |

- 备注
    - 获取网格子节点需要注意一些细节，详见《开发指南-界面与交互-UI说明文档》中对Grid控件的描述

- 示例

```python
# we want to get element positioned at (0, 0)
gridPath = "/grid1"
gridUIControl = uiNode.GetBaseUIControl(gridPath).asGrid()
gridItem_0 = gridUIControl.GetGridItem(0, 0)
if gridItem_0:
    print gridItem_0.GetSize()
```



## GetIsModal

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.inputPanelUIControl.InputPanelUIControl

- 描述

    判断当前面板是否为模态框

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 当前面板是否为模态框 |

- 示例

```python
# we want to know whether inputPanel1 isModal
inputPanelPath = "/inputPanel1"
inputPanel = uiNode.GetBaseUIControl(inputPanelPath).asInputPanel()
inputPanel.GetIsModal()
```



## GetIsSwallow

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.inputPanelUIControl.InputPanelUIControl

- 描述

    判断当前面板输入是否会吞噬事件，isSwallow为Ture时，点击时，点击事件不会穿透到世界。如破坏方块、镜头转向不会被响应

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 当前当前面板输入是否会吞噬事件 |

- 示例

```python
# we want to know whether inputPanel1 isSwallow
inputPanelPath = "/inputPanel1"
inputPanel = uiNode.GetBaseUIControl(inputPanelPath).asInputPanel()
inputPanel.GetIsSwallow()
```



## GetMaxSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    获取控件所允许的最大的大小值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 该控件所允许的最大的大小值，第一项为横轴，第二项为纵轴 |

- 备注
    - 返回值为(0, 0)表示无限制

- 示例

```python
# we want to get image1 maxSize
imagePath = "/panel/image1"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
imageMaxSize = baseUIControl.GetMaxSize()
```



## GetMinSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    获取控件所允许的最小的大小值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 该控件所允许的最小的大小值，第一项为横轴，第二项为纵轴 |

- 备注
    - 返回值为(0, 0)表示无限制

- 示例

```python
# we want to get image1 minSize
imagePath = "/panel/image1"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
imageMinSize = baseUIControl.GetMinSize()
```



## GetModelId

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteasePaperDollUIControl.NeteasePaperDollUIControl

- 描述

    获取渲染的骨骼模型Id

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 骨骼模型Id，失败或者不存在返回-1 |

- 备注
    - 注意：请不要在RenderEntity/RenderSkeletonModel调用之后立即执行。
        骨骼模型Id可用于一下情形：
        1.绑定一个另外的骨骼模型；
        2.绑定序列帧动画；
        3.绑定特效粒子动画

- 示例

```python
import mod.client.extraClientApi as clientApi
path = '/demoPanel/paper_doll'
doll = uiNode.GetBaseUIControl(path).asNeteasePaperDoll()
modelId = doll.GetModelId()
if modelId == -1:
    return
#用途1：绑定一个另外的骨骼模型
modelComp = clientApi.GetEngineCompFactory().CreateModel(modelId)
newModelId = modelComp.BindModelToModel("rightHand", "gun") # 把名称为gun的骨骼模型挂接到rightHand骨骼上
#用途2：绑定序列帧动画
sfxId = clientSystem.CreateEngineSfxFromEditor("effects/example_sfx.json") # 创建特效
comp = clientApi.GetEngineCompFactory().CreateFrameAniSkeletonBind(sfxId)
comp.Bind(modelId, "root", (0, 1, 0), (0, 0, 0)) # 把特效绑定到骨骼模型的骨骼节点上
frameComp = clientApi.GetEngineCompFactory().CreateFrameAniControl(sfxId)
frameComp.Play() # 播放动画
clientSystem.DestroyEntity(sfxId) # 销毁动画
#用途3：绑定特效粒子动画
particleEntityId = clientSystem.CreateEngineParticle("effects/example_particle.json", (0,0,0)) # 创建特效
comp = clientApi.GetEngineCompFactory().CreateParticleSkeletonBind(particleEntityId)
comp.Bind(modelId, "root", (0, 1, 0), (0, 0, 0)) # 把特效绑定到骨骼模型的骨骼节点上
particleComp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
particleComp.Play() # 播放动画
clientSystem.DestroyEntity(particleEntityId) # 销毁动画
```



## GetOffsetDelta

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.inputPanelUIControl.InputPanelUIControl

- 描述

    获得点击面板的拖拽偏移量

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 该控件的拖拽偏移量，第一项为横轴，第二项为纵轴 |

- 备注
    - 点击面板拖拽功能及拖拽偏移量相关，详见<a href="../../../../mcguide/18-界面与交互/30-UI说明文档.html#InputPanel">InputPanel</a>

- 示例

```python
# we want to get inputPanel1's offset_delta
inputPanelPath = "/inputPanel1"
inputPanel = uiNode.GetBaseUIControl(inputPanelPath).asInputPanel()
offset_delta = inputPanel.GetOffsetDelta()
```



## GetOptionCount

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    获得选项数量

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 当前下拉框选项数量 |

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
totalNum = comboBoxUIControl.GetOptionCount()
```



## GetOptionIndexByShowName

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    根据展示文本查找对应下拉框项的索引位置，若找不到返回-1

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 显示文本 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 索引位置 |

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
index = comboBoxUIControl.GetOptionIndexByShowName("测试项")
```



## GetOptionShowNameByIndex

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    根据索引位置查找当前栈式文本，若找不到返回None

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | index | int | 索引位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 显示文本 |

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
text = comboBoxUIControl.GetOptionShowNameByIndex(0)
```



## GetOrientation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.stackPanelUIControl.StackPanelUIControl

- 描述

    获取stackPanel的排列方向

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | stackPanel的排列方向，取值有限为["vertical", "horizontal"]，分别表示垂直方向，水平方向 |

- 示例

```python
# we want to get stackPanel1 orientation
stackPanelPath = "/stackPanel1"
stackPanel = uiNode.GetBaseUIControl(stackPanelPath).asStackPanel()
stackPanel.GetOrientation()
```



## GetPath

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    返回当前控件的相对路径，路径从画布节点开始算起

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 当前控件的相对路径，路径从画布节点开始算起 |

- 示例

```python
text2Path = "/panel/text2"
baseUIControl = uiNode.GetBaseUIControl(text2Path)
path = baseUIControl.GetPath()
```



## GetPosition

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    获取控件相对父节点的坐标

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 该控件相对父节点的坐标信息，第一项为横轴，第二项为纵轴 |

- 示例

```python
# we want to get text2 position
text2Path = "/panel/text2"
baseUIControl = uiNode.GetBaseUIControl(text2Path)
textPosition = baseUIControl.GetPosition()
```



## GetPropertyBag

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    获取PropertyBag

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | PropertyBag |

- 示例

```python
text2Path = "/panel/text2"
baseUIControl = uiNode.GetBaseUIControl(text2Path)
propertyBag = baseUIControl.GetPropertyBag()
```



## GetRotateAngle

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    获取图片相对自身的旋转锚点旋转的角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 获取图片相对自身的旋转锚点旋转的角度 |

- 示例

```python
imagePath = "/imagePath"
imageControl = uiNode.GetBaseUIControl(imagePath).asImage()
print imageControl.GetRotateAngle()
```



## GetRotatePivot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    获取图片相对自身的旋转锚点

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 获取图片相对自身的旋转锚点，第一项为横轴，第二项为纵轴 |

- 示例

```python
imagePath = "/imagePath"
imageControl = uiNode.GetBaseUIControl(imagePath).asImage()
print imageControl.GetRotatePivot()
```



## GetRotateRect

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    获取图片当前的四个边角点

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(tuple(float,float),tuple(float,float),tuple(float,float),tuple(float,float)) | 获取图片当前的四个边角点(每个点都是一个tuple) |

- 示例

```python
imagePath = "/imagePath"
imageControl = uiNode.GetBaseUIControl(imagePath).asImage()
print imageControl.GetRotateRect()
```



## GetScrollViewContentControl

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.scrollViewUIControl.ScrollViewUIControl

- 描述

    返回该scroll_view内容的BaseUIControl实例

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseUIControl | 该scroll_view内容的BaseUIControl实例 |

- 示例

```python
# we want get scroll_view content
scrollViewPath = "/scroll_view0"
scrollViewUIControl = uiNode.GetBaseUIControl(scrollViewPath).asScrollView()
contentUIControl = scrollViewUIControl.GetScrollViewContentControl()
```



## GetScrollViewContentPath

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.scrollViewUIControl.ScrollViewUIControl

- 描述

    返回该scroll_view内容的路径

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 该scroll_view内容的路径 |

- 备注
    - scroll_view的路径是动态的，在触控模式和键鼠模式（按f11可切换的两种操作方式）下的路径不同，每次使用scroll_view及其子控件的路径，都应该重新调用一次本接口。
    如果不想让路径随操作模式变化，可以指定$touch变量为true，此时路径将固定为touch_path。
    ```json
    "scroll_view0@common.scrolling_panel": {
        // 手动指定$touch变量为true
        "$touch": true
        ...
    }
    ```

- 示例

```python
# we want get scroll_view content path
scrollViewPath = "/scroll_view0"
scrollViewUIControl = uiNode.GetBaseUIControl(scrollViewPath).asScrollView()
path = scrollViewUIControl.GetScrollViewContentPath()
```



## GetScrollViewPercentValue

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.scrollViewUIControl.ScrollViewUIControl

- 描述

    获取当前scroll_view内容的百分比位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 当前scroll_view内容的百分比位置 |

- 示例

```python
# we want get scroll_view percent
scrollViewPath = "/scroll_view0"
scrollViewUIControl = uiNode.GetBaseUIControl(scrollViewPath).asScrollView()
scrollViewUIControl.GetScrollViewPercentValue()
```



## GetScrollViewPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.scrollViewUIControl.ScrollViewUIControl

- 描述

    获得当前scroll_view最上方内容的位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 当前scroll_view最上方内容的位置 |

- 示例

```python
# we want get scroll_view pos
scrollViewPath = "/scroll_view0"
scrollViewUIControl = uiNode.GetBaseUIControl(scrollViewPath).asScrollView()
scrollViewUIControl.GetScrollViewPos()
```



## GetSelectOptionIndex

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    获得当前选中项的索引，所无选中项则返回-1

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 当前下拉框选中项索引 |

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
currentIndex = comboBoxUIControl.GetSelectOptionIndex()
```



## GetSelectOptionShowName

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    获得当前选中项的展示文本，所无选中项则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 当前选中项的展示文本 |

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
currentText = comboBoxUIControl.GetSelectOptionShowName()
```



## GetSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    获取控件的大小

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 该控件的大小信息，第一项为横轴，第二项为纵轴 |

- 示例

```python
# we want to get text2 size
text2Path = "/panel/text2"
baseUIControl = uiNode.GetBaseUIControl(text2Path)
text2Size = baseUIControl.GetSize()
```



## GetSliceCount

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.selectionWheelUIControl.SelectionWheelUIControl

- 描述

    获取轮盘可以选择的总切片数量

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 轮盘可以选择的总切片数量 |

- 示例

```python
selectionWheelPath = "/selectionWheel"
selectionWheelControl = uiNode.GetBaseUIControl(selectionWheelPath).asSelectionWheel()
selectionWheelControl.GetSliceCount()
```



## GetSliderValue

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.sliderUIControl.SliderUIControl

- 描述

    获取滑动条的值，失败返回0

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 滑动条的值 |

- 示例

```python
# we want to get slider value
sliderPath = "/panel/slider0"
sliderUIControl = uiNode.GetBaseUIControl(sliderPath).asSlider()
value = sliderUIControl.GetSliderValue()
```



## GetText

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    获取Label的文本信息，获取失败会返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 文本信息 |

- 备注
    - 获取失败通常是由于路径填写错误，或该控件不是Label类型

- 示例

```python
# we want to get text2 content
text2Path = "/panel/text2"
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
labelUIControl.GetText()
```



## GetTextAlignment

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    获取文本控件的文本对齐方式

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 文本控件的文本对齐方式，具体返回值的意义可参考SetTextAlignment接口的备注 |

- 示例

```python
# we want to get text2 textAlignment
text2Path = "/panel/text2"
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
labelUIControl.GetTextAlignment()
```



## GetTextColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    获取Label文本颜色

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float,float) | 获取文本的颜色信息(r, g, b, a), 取值[0, 1] |

- 示例

```python
# we want to get text2 color
text2Path = "/panel/text2"
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
labelUIControl.GetTextColor()
```



## GetTextLinePadding

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    获取文本控件的行间距

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 文本控件的行间距，单位为像素 |

- 示例

```python
# we want to get text2 textLinePadding
text2Path = "/panel/text2"
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
labelUIControl.GetTextLinePadding()
```



## GetToggleState

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.switchToggleUIControl.SwitchToggleUIControl

- 描述

    获取Toggle开关控件的状态

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | toggle_path | str | 实际toggle控件相对路径，由UI编辑器生成的开关控件该参数即为默认值"/this_toggle" |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否处于开启状态 True:开启状态 False:关闭状态 |

- 示例

```python
togglePath = "/toggle1"
switchToggleUIControl = uiNode.GetBaseUIControl(togglePath).asSwitchToggle()
print switchToggleUIControl.GetToggleState()
```



## GetUiItem

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.itemRendererUIControl.ItemRendererUIControl

- 描述

    获取ItemRenderer控件显示的物品，ItemRenderer控件的配置方式详见<a href="../../../../mcguide/18-界面与交互/30-UI说明文档.html#itemrenderer">控件介绍ItemRenderer</a>

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 物品字典，详见备注（包含itemName:物品identifier, auxValue:物品附加值, isEnchanted:是否附魔) |

- 备注
    - 返回值具体如下：
        | 键值     | 类型      | 内容      |
        | ----------------| -------------| ---------------------|
        | "itemName"  | str | 物品identifier |
        | "auxValue"  | int | 物品附加值 |
        | "isEnchanted"  | bool | 是否显示附魔效果 |

- 示例

```python
#获取木板block信息
itemRenderPath = "/panel/item_renderer"
itemRendererBaseControl = uiNode.GetBaseUIControl(itemRenderPath)
itemRendererControl = itemRendererBaseControl.asItemRenderer()
itemInfoDict = itemRendererControl.GetUiItem()
```



## GetVisible

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    根据控件路径返回某控件是否已显示

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 该控件是否已显示 |

- 示例

```python
# 我们获得panel下面的text2是否显示
text2Path = "/panel/text2"
baseUIControl = uiNode.GetBaseUIControl(text2Path)
textVisible = baseUIControl.GetVisible()
```



## IsAnimEndCallbackRegistered

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    控件是否对名称为animName的动画进行了注册回调

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animName | str | 动画的名称，请不要包含动画的命名空间 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否对名称为animName的动画进行了注册回调 |

- 备注
    - UI属性动画相关，详见<a href="../../../../mcguide/18-界面与交互/19-控件属性动画.html">属性动画</a>

- 示例

```python
# 获取控件
control = uiNode.GetBaseUIControl("/image")
print control.IsAnimEndCallbackRegistered("offset_animation")
```



## IsTextShadowEnabled

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    判断文本控件是否显示阴影

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 文本控件是否显示阴影 |

- 示例

```python
# we want to know whether text2 has shadow
text2Path = "/panel/text2"
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
labelUIControl.IsTextShadowEnabled()
```



## PauseAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    暂停动画，暂停后的动画会停在当前的状态

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | propertyName | str | 动画的属性名称，默认值为"all"，表示暂停所有动画，不为"all"的时候表示单个动画的暂停，比如propertyName=="size"时，表示暂停尺寸属性上的动画 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否暂停成功 |

- 备注
    - UI属性动画相关，详见<a href="../../../../mcguide/18-界面与交互/19-控件属性动画.html">属性动画</a>

- 示例

```python
# 获取控件
control = uiNode.GetBaseUIControl("/image")
# 暂停所有动画
control.PauseAnimation()
# 暂停尺寸动画
# control.PauseAnimation("size")
# 暂停位移动画
# control.PauseAnimation("offset")
# 其他属性也是支持暂停的，具体可参见备注
```



## PlayAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    继续播放动画，从动画当前状态开始播放

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | propertyName | str | 动画的属性名称，默认值为"all"，表示播放所有动画，不为"all"的时候表示单个动画的播放，比如propertyName=="size"时，表示播放尺寸属性上的动画 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否播放成功 |

- 备注
    - UI属性动画相关，详见<a href="../../../../mcguide/18-界面与交互/19-控件属性动画.html">属性动画</a>

- 示例

```python
# 获取控件
control = uiNode.GetBaseUIControl("/image")
# 播放所有动画
control.PlayAnimation()
# 播放尺寸动画
# control.PlayAnimation("size")
# 播放位移动画
# control.PlayAnimation("offset")
# 其他属性也是支持播放的，具体可参见备注
```



## RegisterCloseComboBoxCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    注册关闭下拉框事件回调

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callback | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 示例

```python
# 注册关闭下拉框事件回调，在点击关闭下拉框时会调用注册的回调函数
def onCloseComboBoxCallback(args):
    pass

comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
comboBoxUIControl.RegisterCloseComboBoxCallback(onCloseComboBoxCallback)
```



## RegisterOpenComboBoxCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    注册展开下拉框事件回调

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callback | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 示例

```python
# 注册展开下拉框事件回调，在点击展开下拉框时会调用注册的回调函数
def onOpenComboBoxCallback(args):
    pass

comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
comboBoxUIControl.RegisterOpenComboBoxCallback(onOpenComboBoxCallback)
```



## RegisterSelectItemCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    注册选中下拉框内容事件回调

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callback | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 备注
    - onSelectItemCallback参数说明：
        | 参数              | 类型  | 解释                                                         |
        | ----------------- | ----- | ------------------------------------------------------------ |
        | index  | int   | 当前选中项的索引  |
        | showName | str   | 当前选中项的显示文本 |
        | userData       |  Unknown  | 当前选中项的自定义数据，若添加下拉框项时未传入自定义数据则此处为None |

- 示例

```python
# 注册选中下拉框内容事件回调，在点击关闭下拉框时会调用注册的回调函数
def onSelectItemCallback(index, showName, userData):
    pass

comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
comboBoxUIControl.RegisterSelectItemCallback(onSelectItemCallback)
```



## RemoveAnimEndCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    移除动画播放结束后的回调

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animName | str | 动画的名称，请不要包含动画的命名空间 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否移除成功 |

- 备注
    - UI属性动画相关，详见<a href="../../../../mcguide/18-界面与交互/19-控件属性动画.html">属性动画</a>

- 示例

```python
# 获取控件
control = uiNode.GetBaseUIControl("/image")
# 移除属性动画offset_animation播放结束后的回调
control.RemoveAnimEndCallback("offset_animation")
```



## RemoveAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    删除单一属性的动画，删除后的值与当前状态有关，建议删除后重新设置该属性值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | propertyName | str | 要删除动画的属性名称，无默认值，值必须为单一属性（不能填"all"） |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 备注
    - UI属性动画相关，详见<a href="../../../../mcguide/18-界面与交互/19-控件属性动画.html">属性动画</a>

- 示例

```python
# 获取控件
control = uiNode.GetBaseUIControl("/image")
# 删除 位移 属性上的动画
control.RemoveAnimation("offset")
```



## RemoveEntityMarker

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    删除实体位置标记

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体Id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.RemoveEntityMarker(entityId)
```



## RemoveEntityTextMarker

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    在小地图上删除实体文本标记

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体Id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.RemoveEntityTextMarker(entityId)
```



## RemoveOptionByIndex

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    根据提供的索引移除对应下拉框项，移除成功则返回True，否则返回False

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | index | int | 索引 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否移除成功 |

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
success = comboBoxUIControl.RemoveOptionByIndex(0)
```



## RemoveOptionByShowName

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    根据提供的展示文本移除对应下拉框项，移除成功则返回True，否则返回False

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | showName | str | 展示文本 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否移除成功 |

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
success = comboBoxUIControl.RemoveOptionByShowName("测试项")
```



## RemoveStaticMarker

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    删除静态位置标记

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 标记的Id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.RemoveStaticMarker(entityId)
```



## RemoveStaticTextMarker

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    在小地图上删除静态文本标记

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 标记Id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.RemoveStaticTextMarker("this_is_marker_key")
```



## RenderBlockGeometryModel

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteasePaperDollUIControl.NeteasePaperDollUIControl

- 描述

    渲染网格体模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | params | dict | 渲染参数，详细说明请见备注 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 网格体模型使用[CombineBlockPaletteToGeometry](../方块/方块几何体模型.md#combineblockpalettetogeometry)生成
    - 每次进入游戏需要重新调用本接口渲染网格体模型，可使用[SerializeBlockPalette](../方块/方块调色板.md#serializeblockpalette)和[DeserializeBlockPalette](../方块/方块调色板.md#deserializeblockpalette)实现调色板保存并重载调色板，重新生成网格体模型进行渲染。
    - RenderBlockGeometryModel参数params说明：
        params参数解释如下：
        | 参数              | 类型  | 解释                                                         |
        | ----------------- | ----- | ------------------------------------------------------------ |
        | block_geometry_model_name         | str | 网格体模型名称, 可用CombineBlockPaletteToGeometry返回值                               |                                |
        | scale | float   | 渲染缩放比例，默认为1.0                                     |           |
        | init_rot_y        | float   | 初始Y方向的朝向 |
        | init_rot_x        | float   | 初始x方向的朝向 |
        | init_rot_z        | float   | 初始z方向的朝向 |
        | molang_dict  | dict   | molang表达式字典，其中key为str，value为float               |
        | rotation_axis  | tuple   | 选择旋转环绕的轴，如(0,1,0)依次代表x、y、z轴，此为绕y轴旋转，该属性只在netease_paper_doll_renderer控件的rotation属性为“freedom_gesture”时起效        |

- 示例

```python
import mod.client.extraClientApi as clientApi
path = '/demoPanel/paper_doll'
param = {
    "block_geometry_model_name": "my_geometry_model",
    "scale": 0.5,
    "init_rot_y": 60,
    "rotation_axis":(0,1,1),
    "molang_dict": {"variable.liedownamount": 1}
}
doll = uiNode.GetBaseUIControl(path).asNeteasePaperDoll()
doll.RenderBlockGeometryModel(param)
```



## RenderEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteasePaperDollUIControl.NeteasePaperDollUIControl

- 描述

    渲染实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | params | dict | 渲染参数，详细说明请见备注 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - RenderEntity参数params说明：
        params参数解释如下：
        | 参数              | 类型  | 解释                                                         |
        | ----------------- | ----- | ------------------------------------------------------------ |
        | entity_id  | str   | 渲染生物的实体Id，与实体的identifier二者选其一即可。如果与entity_identifier同时定义，则优先使用entity_id。          |
        | entity_identifier | str   | 渲染生物的identifier，与实体Id二者选其一即可。如果与entity_id同时定义，则优先使用entity_id。              |
        | scale | float   | 渲染缩放比例，默认为1.0                                     |
        | render_depth       | int   | 渲染深度，对于玩家默认-50，普通生物-15，该参数可解决UI遮挡剔除问题            |
        | init_rot_y        | float   | 初始Y方向的朝向 |
        | init_rot_x        | float   | 初始x方向的朝向 |
        | init_rot_z        | float   | 初始z方向的朝向 |
        | molang_dict  | dict   | molang表达式字典，其中key为str，value为float               |
        | rotation_axis  | tuple   | 选择旋转环绕的轴，如(0,1,0)依次代表x、y、z轴，此为绕y轴旋转，该属性只在netease_paper_doll_renderer控件的rotation属性为“freedom_gesture”时起效        |

- 示例

```python
path = '/demoPanel/paper_doll'
# 使用entity_id进行渲染
param = {
    "entity_id": "-8589934591",
    "scale": 0.5,
    "render_depth": -50,
    "init_rot_y": 60,
    "rotation_axis":(0,1,1),
    "molang_dict": {"variable.liedownamount": 1}
}
doll = uiNode.GetBaseUIControl(path).asNeteasePaperDoll()
doll.RenderEntity(param)
# 使用identifier进行渲染
param = {
    "entity_identifier": "minecraft:cow",
    "scale": 0.5,
    "render_depth": -50,
    "init_rot_y": 60,
    "rotation_axis":(0,1,1),
    "molang_dict": {"variable.liedownamount": 1}
}
doll = uiNode.GetBaseUIControl(path).asNeteasePaperDoll()
doll.RenderEntity(param)
```



## RenderSkeletonModel

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteasePaperDollUIControl.NeteasePaperDollUIControl

- 描述

    渲染骨骼模型（不依赖实体）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | params | dict | 渲染参数，详细说明请见备注 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - RenderSkeletonModel参数params说明：
        params参数解释如下：
        | 参数              | 类型  | 解释                                                         |
        | ----------------- | ----- | ------------------------------------------------------------ |
        | skeleton_model_name         | str | 骨骼模型名称                                |
        | animation         | str | 骨骼动作名称，默认为idle                                |
        | animation_looped        | bool   | 骨骼动作是否循环播放，默认True                                  |
        | scale | float   | 渲染缩放比例，默认为1.0                                     |
        | render_depth       | int   | 渲染深度，对于玩家默认-50，普通生物-15，该参数可解决UI遮挡剔除问题            |
        | init_rot_y        | float   | 初始Y方向的朝向 |
        | init_rot_x        | float   | 初始x方向的朝向 |
        | init_rot_z        | float   | 初始z方向的朝向 |
        | molang_dict  | dict   | molang表达式字典，其中key为str，value为float               |
        | rotation_axis  | tuple   | 选择旋转环绕的轴，如(0,1,0)依次代表x、y、z轴，此为绕y轴旋转，该属性只在netease_paper_doll_renderer控件的rotation属性为“freedom_gesture”时起效        |
        | light_direction  | tuple   | 可选参数。控制骨骼模型在纸娃娃中显示时的光照方向，x控制光照的左右方向，y控制光照的上下方向，z控制光照的前后方向，取值为-1,0,1。不填写该参数时模型默认从底部打光。该属性仅对没有自定义材质的骨骼模型生效。如果该骨骼模型定义了自定义材质，则无效。如需要对使用自定义材质的骨骼模型控制其光照方向，可以参考官方骨骼模型vertex shader中getLightColor使用到HIDE_COLOR的这部分代码。该参数对部分安卓低端设备，极低端设备无效。    |

- 示例

```python
import mod.client.extraClientApi as clientApi
path = '/demoPanel/paper_doll'
param = {
    "skeleton_model_name": "ty_yuanshenghuli_0_0",
    "animation": "idle_stand",
    "scale": 0.5,
    "render_depth": -50,
    "init_rot_y": 60,
    "rotation_axis":(0,1,1),
    "molang_dict": {"variable.liedownamount": 1},
    # 控制光照方向为从模型的正右边往左边打光，以及从模型的正前方往后打光
    "light_direction": ( 1.0, 0.0, 1.0 )
}
doll = uiNode.GetBaseUIControl(path).asNeteasePaperDoll()
doll.RenderSkeletonModel(param)
```



## RepaintMiniMap

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    重新绘制小地图

- 参数

    无

- 返回值

    无

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.RepaintMiniMap()
```



## Rotate

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    图片相对自身的旋转锚点进行旋转

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | angle | float | 旋转角度 |

- 返回值

    无

- 示例

```python
imagePath = "/imagePath"
imageControl = uiNode.GetBaseUIControl(imagePath).asImage()
imageControl.Rotate(30)
```



## RotateAround

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    图片相对全局坐标系中某个固定的点进行旋转

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | point | tuple(float,float) | 全局坐标点 |
    | angle | float | 旋转角度 |

- 返回值

    无

- 示例

```python
imagePath = "/imagePath"
imageControl = uiNode.GetBaseUIControl(imagePath).asImage()
imageControl.RotateAround((50, 50), 30)
```



## SetAlpha

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置节点的透明度，仅对image和label控件生效

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | alpha | float | 透明度，取值0-1之间，0表示完全透明，1表示完全不透明 |

- 返回值

    无

- 示例

```python
# 设置text2的透明度为半透明
text2Path = "/panel/text2"
baseUIControl = uiNode.GetBaseUIControl(text2Path)
baseUIControl.SetAlpha(0.5)
```



## SetAnchorFrom

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件相对于父节点的锚点

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | anchorFrom | str | 相对于父节点的锚点，可选的值详见备注 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - anchorFrom可选的值
        | 值              | 解释                                                         |
        | ----------------| ------------------------------------------------------------ |
        | "top_left"      | 相对于父节点的左上角 |
        | "top_middle"    | 相对于父节点的上边中间 |
        | "top_right"     | 相对于父节点的右上角 |
        | "left_middle"   | 相对于父节点的左边中间 |
        | "center"        | 相对于父节点的中间 |
        | "right_middle"  | 相对于父节点的右边中间 |
        | "bottom_left"   | 相对于父节点的底部左边 |
        | "bottom_middle" | 相对于父节点的部中间 |
        | "bottom_right"  | 相对于父节点的底部右边 |

- 示例

```python
# 设置image1控件相对于父节点的左上角
imagePath = "/panel/image1"
anchorFrom = "top_left"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
ret = baseUIControl.SetAnchorFrom(anchorFrom)
```



## SetAnchorTo

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件自身锚点位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | anchorTo | str | 控件自身锚点位置，可选的值详见备注 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - anchorTo可选的值
        | 值              | 解释                                                         |
        | ----------------| ------------------------------------------------------------ |
        | "top_left"      | 自身锚点位于左上角 |
        | "top_middle"    | 自身锚点位于上边中间 |
        | "top_right"     | 自身锚点位于右上角 |
        | "left_middle"   | 自身锚点位于左边中间 |
        | "center"        | 自身锚点位于中间 |
        | "right_middle"  | 自身锚点位于右边中间 |
        | "bottom_left"   | 自身锚点位于底部左边 |
        | "bottom_middle" | 自身锚点位于底部中间 |
        | "bottom_right"  | 自身锚点位于底部右边 |

- 示例

```python
# 设置image1控件锚点到自身中间
imagePath = "/panel/image1"
anchorTo = "center"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
ret = baseUIControl.SetAnchorTo(anchorTo)
```



## SetAnimEndCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置动画播放结束后的回调，每次设置都会覆盖上一次的设置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animName | str | 动画的名称，请不要包含动画的命名空间 |
    | func | function | 回调，无参数无返回值的函数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - UI属性动画相关，详见<a href="../../../../mcguide/18-界面与交互/19-控件属性动画.html">属性动画</a>

- 示例

```python
# 获取控件
control = uiNode.GetBaseUIControl("/image")

def callback():
    print "offset_animation end"

# 设置属性动画offset_animation播放结束后的回调
control.SetAnimEndCallback("offset_animation", callback)
```



## SetAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    给单一属性设置动画，已有重复的会设置失败，需要先remove

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | propertyName | str | 要设置的动画的属性名称，无默认值，值必须为单一属性（不能填"all"） |
    | namespace | str | 动画的命名空间，类似于自定义控件，动画也是可以定义到某个命名空间的，详见备注 |
    | animName | str | 动画的名称，详见备注 |
    | autoPlay | bool | 动画添加后是否自动播放，默认值为False，表示不进行播放 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否添加成功 |

- 备注
    - UI属性动画相关，详见<a href="../../../../mcguide/18-界面与交互/19-控件属性动画.html">属性动画</a>
    - 需要注意，设置动画本质上是拷贝动画数据到控件的动画组件里面，所以如果动画数据发生了改变（比如通过接口RegisterUIAnimations修改了动画数据），如果想要控件应用修改需要再次调用setAnimation进行更新

- 示例

```python
# 获取控件
control = uiNode.GetBaseUIControl("/image")

# 如果动画不在json中定义，也可以通过接口进行动态注册
data = {
    "namespace": "CustomAnimations",
    "alpha_animation_1": {
        "anim_type": "alpha",
        "duration": 1.5,
        "from": 0,
        "to": 1,
        "next": "@namespace.alpha_animation_2"
    },
    "alpha_animation_2": {
        "anim_type": "alpha",
        "duration": 1.5,
        "from": 1,
        "to": 0,
        "next": "@namespace.alpha_animation_1"
    }
}
import mod.client.extraClientApi as clientApi
clientApi.RegisterUIAnimations(data, True)

# 给 alpha属性 添加 透明度动画
control.SetAnimation("alpha", "CustomAnimations", "alpha_animation_1")
```



## SetButtonHoverInCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.buttonUIControl.ButtonUIControl

- 描述

    设置鼠标进入按钮时触发的悬浮回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callbackFunc | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 备注
    - 将鼠标移入添加了悬浮回调的控件中会触发该事件，该鼠标指PushScreen生成UI后显示的鼠标，F11生成的鼠标无法生效
    - OnButtonHoverInCallback接收到的参数：
        | 参数              | 类型  | 解释                                                         |
        | ----------------- | ----- | ------------------------------------------------------------ |
        | isHoverIn        | int   | 鼠标是否为进入悬浮回调，1为移入，0为移出   |
        | PrevButtonDownID  | str   | 上一个被点击Down的按钮的ID，如果没有取值为"-1"               |
        | TouchPosX         | float | 鼠标进入按钮时屏幕上的UI坐标X值                                |
        | TouchPosY         | float | 鼠标进入按钮时屏幕上的UI坐标Y值                                |
        | ButtonPath        | str   | 鼠标进入的按钮的ComponentPath                                  |
        | AddHoverEventParams| dict   |  在调用AddHoverEventParams接口时传入的参数字典                                |
        

- 示例

```python
def onButtonHoveInCallback(args):
    pass

buttonPath = "/panel/test_btn"
buttonUIControl = uiNode.GetBaseUIControl("/panel/test_btn").asButton()
buttonUIControl.AddHoverEventParams()
buttonUIControl.SetButtonHoverInCallback(onButtonHoveInCallback)
```



## SetButtonHoverOutCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.buttonUIControl.ButtonUIControl

- 描述

    设置鼠标退出按钮时触发的悬浮回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callbackFunc | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 备注
    - 将鼠标移出添加了悬浮回调的控件中会触发该事件，该鼠标指PushScreen生成UI后显示的鼠标，F11生成的鼠标无法生效
    - OnButtonHoverInCallback接收到的参数：
        | 参数              | 类型  | 解释                                                         |
        | ----------------- | ----- | ------------------------------------------------------------ |
        | isHoverIn        | int   | 鼠标是否为进入悬浮回调，1为移入，0为移出  |
        | PrevButtonDownID  | str   | 上一个被点击Down的按钮的ID，如果没有取值为"-1"               |
        | ButtonPath        | str   | 鼠标退出的按钮的ComponentPath                                  |
        | AddHoverEventParams| dict   |  在调用AddHoverEventParams接口时传入的参数字典                                |
        

- 示例

```python
def OnButtonHoverOutCallback(args):
    pass

buttonPath = "/panel/test_btn"
buttonUIControl = uiNode.GetBaseUIControl("/panel/test_btn").asButton()
buttonUIControl.AddHoverEventParams()
buttonUIControl.SetButtonHoverOutCallback(OnButtonHoverOutCallback)
```



## SetButtonScreenExitCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.buttonUIControl.ButtonUIControl

- 描述

    设置按钮所在画布退出时若鼠标仍未抬起时触发回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callbackFunc | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 备注
    - 其他相关说明见SetButtonTouchDownCallback接口：

- 示例

```python
def onButtonScreenExitCallback(args):
    pass

buttonPath = "/panel/test_btn"
buttonUIControl = uiNode.GetBaseUIControl("/panel/test_btn").asButton()
buttonUIControl.AddTouchEventParams({"isSwallow":True})
buttonUIControl.SetButtonScreenExitCallback(onButtonScreenExitCallback)
```



## SetButtonTouchCancelCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.buttonUIControl.ButtonUIControl

- 描述

    设置触控在按钮范围外弹起时触发的回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callbackFunc | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 备注
    - 其他相关说明见SetButtonTouchDownCallback接口：

- 示例

```python
def onButtonTouchCancelCallback(args):
    pass

buttonPath = "/panel/test_btn"
buttonUIControl = uiNode.GetBaseUIControl("/panel/test_btn").asButton()
buttonUIControl.AddTouchEventParams({"isSwallow":True})
buttonUIControl.SetButtonTouchCancelCallback(onButtonTouchCancelCallback)
```



## SetButtonTouchDownCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.buttonUIControl.ButtonUIControl

- 描述

    设置按钮按下时触发的回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callbackFunc | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 备注
    - onButtonTouchDownCallback参数args说明：
        | 参数              | 类型  | 解释                                                         |
        | ----------------- | ----- | ------------------------------------------------------------ |
        | #collection_name  | str   | 按钮所属的集合名称                                           |
        | #collection_index | int   | 按钮在集合所属的集合序号                                     |
        | ButtonState       | int   | 按钮的状态：Up为0，Down为1，默认是-1，建议使用New            |
        | TouchEvent        | int   | 按钮的状态新版本：Up为0，Down为1，Cancel为3，Move为4，默认是-1 |
        | PrevButtonDownID  | str   | 上一个被点击Down的按钮的ID，如果没有取值为"-1"               |
        | TouchPosX         | float | 按钮被点击时屏幕上的UI坐标X值                                |
        | TouchPosY         | float | 按钮被点击时屏幕上的UI坐标Y值                                |
        | ButtonPath        | str   | 被点击的按钮的ComponentPath                                  |
        | AddTouchEventParams| dict   |  在调用AddTouchEventParams接口时传入的参数字典                                |
        
        事件之间的关系如下图所示：
        ![事件说明](../../picture/touch_event.png)

- 示例

```python
def onButtonTouchDownCallback(args):
    pass

buttonPath = "/panel/test_btn"
buttonUIControl = uiNode.GetBaseUIControl("/panel/test_btn").asButton()
buttonUIControl.AddTouchEventParams({"isSwallow":True})
buttonUIControl.SetButtonTouchDownCallback(onButtonTouchDownCallback)
```



## SetButtonTouchMoveCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.buttonUIControl.ButtonUIControl

- 描述

    设置按下后触控移动时触发的回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callbackFunc | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 备注
    - 其他相关说明见SetButtonTouchDownCallback接口：
    - 该事件只在触屏模式下触发

- 示例

```python
def onButtonTouchMoveCallback(args):
    pass

buttonPath = "/panel/test_btn"
buttonUIControl = uiNode.GetBaseUIControl("/panel/test_btn").asButton()
buttonUIControl.AddTouchEventParams({"isSwallow":True})
buttonUIControl.SetButtonTouchMoveCallback(onButtonTouchMoveCallback)
```



## SetButtonTouchMoveInCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.buttonUIControl.ButtonUIControl

- 描述

    设置按下按钮后进入控件时触发的回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callbackFunc | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 备注
    - 其他相关说明见SetButtonTouchDownCallback接口：
    - 键鼠模式下，鼠标移入会触发该事件。触屏模式下，鼠标按下按钮会触发该事件

- 示例

```python
def onButtonTouchMoveInCallback(args):
    pass

buttonPath = "/panel/test_btn"
buttonUIControl = uiNode.GetBaseUIControl("/panel/test_btn").asButton()
buttonUIControl.AddTouchEventParams({"isSwallow":True})
buttonUIControl.SetButtonTouchMoveInCallback(onButtonTouchMoveInCallback)
```



## SetButtonTouchMoveOutCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.buttonUIControl.ButtonUIControl

- 描述

    设置按下按钮后退出控件时触发的回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callbackFunc | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 备注
    - 其他相关说明见SetButtonTouchDownCallback接口：
    - 键鼠模式下，鼠标移出会触发该事件。触屏模式下，鼠标松开按钮会触发该事件

- 示例

```python
def onButtonTouchMoveOutCallback(args):
    pass

buttonPath = "/panel/test_btn"
buttonUIControl = uiNode.GetBaseUIControl("/panel/test_btn").asButton()
buttonUIControl.AddTouchEventParams({"isSwallow":True})
buttonUIControl.SetButtonTouchMoveOutCallback(onButtonTouchMoveOutCallback)
```



## SetButtonTouchUpCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.buttonUIControl.ButtonUIControl

- 描述

    设置触控在按钮范围内弹起时的回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callbackFunc | function | 回调函数，必须是UI的类函数 |

- 返回值

    无

- 备注
    - 其他相关说明见SetButtonTouchDownCallback接口：

- 示例

```python
def onButtonTouchUpCallback(args):
    pass

buttonPath = "/panel/test_btn"
buttonUIControl = uiNode.GetBaseUIControl("/panel/test_btn").asButton()
buttonUIControl.AddTouchEventParams({"isSwallow":True})
buttonUIControl.SetButtonTouchUpCallback(onButtonTouchUpCallback)
```



## SetClipDirection

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    设置图片控件的裁剪方向

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | clipDirection | str | 图片控件的裁剪方向，可选的值详见备注 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - clipDirection可选的值
        | 值                      | 解释                                          |
        | ------------------------| --------------------------------------------- |
        | "fromLeftToRight"       | 从左到右 |
        | "fromRightToLeft"       | 从右到左 |
        | "fromOutsideToInside"   | 从外到内 |
        | "fromTopToBottom"       | 从上到下 |
        | "fromBottomToTop"       | 从下到上 |

- 示例

```python
imagePath = "/image"
imageUIControl = uiNode.GetBaseUIControl(imagePath).asImage()
clipDirection = "fromOutsideToInside"
ret = imageUIControl.SetClipDirection(clipDirection)
```



## SetClipOffset

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件的裁剪偏移信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | clipOffset | tuple(float,float) | 该控件的裁剪偏移信息，第一项为横轴，第二项为纵轴 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# we want to set image1 maxSize
imagePath = "/panel/image1"
clipOffset = (20, 20)
baseUIControl = uiNode.GetBaseUIControl(imagePath)
ret = baseUIControl.SetClipOffset(clipOffset)
```



## SetClipsChildren

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件是否开启裁剪内容

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | clipsChildren | bool | True表示开启，False表示关闭 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# we want to enable image1 clipsChildren
imagePath = "/panel/image1"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
ret = baseUIControl.SetClipsChildren(True)
```



## SetCurrentSliceIndex

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.selectionWheelUIControl.SelectionWheelUIControl

- 描述

    设置轮盘选择的切片

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | index | int | 轮盘选择的切片的index，取值范围为 [-1, GetSliceCount() - 1]，-1表示轮盘无选择 |

- 返回值

    无

- 示例

```python
selectionWheelPath = "/selectionWheel"
selectionWheelControl = uiNode.GetBaseUIControl(selectionWheelPath).asSelectionWheel()
selectionWheelControl.SetCurrentSliceIndex(-1)
```



## SetEditText

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.textEditBoxUIControl.TextEditBoxUIControl

- 描述

    设置edit_box输入框的文本信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | text | str | 文本的内容 |

- 返回值

    无

- 示例

```python
# we want to clear edit2 content
editBoxPath = "/panel/edit2"
text = ""
textEditBoxUIControl = uiNode.GetBaseUIControl(editBoxPath).asTextEditBox()
textEditBoxUIControl.SetEditText(text)
```



## SetEditTextMaxLength

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.textEditBoxUIControl.TextEditBoxUIControl

- 描述

    设置输入框的最大输入长度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | maxLength | int | 输入框可输入的最大长度，取值[0, +∞) |

- 返回值

    无

- 示例

```python
# we want to set text_edit_box max input length 10
editTextPath = "/panel2/text_edit_box"
textEditBoxUIControl = uiNode.GetBaseUIControl(editBoxPath).asTextEditBox()
textEditBoxUIControl.SetEditTextMaxLength(10)
```



## SetFullPosition

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件的锚点坐标（全局坐标），支持比例值以及绝对值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | axis | str | 设置的轴向，可选的值有["x","y"]，"x"表示设置控件锚点的x坐标，"y"表示设置控件锚点的y坐标 |
    | paramDict | dict | 设置的参数，具体见备注 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - paramDict的键值
        | 参数名       |  参数类型       | 解释                                                         |
        | ----------------| --------------|---------------------------------------------- |
        | "followType"| str | 跟随类型，默认值为"none"，可以不写该键值|
        | "relativeValue"| float | 相对于跟随控件的比例值，默认值为0，可以不写该键值|
        | "absoluteValue"| float | 设置的绝对值，默认值为0，可以不写该键值 |
    - 控件的大小支持复杂的计算来实现自适应布局，形式为“absoluteValue + relativeValue * 跟随值”。
        其中跟随值由跟随的控件以及当前设置的属性共同决定。比如当前设置的是控件的x坐标，并且跟随控件为父控件，而跟随值为父控件的宽度。
        而跟随的控件是特定的，是与控件本身有一定关系的，比如控件的父控件，子控件等，可以通过设置followType的值来指定。
    - followType可选的值
        | 值              | 解释                                                         |
        | ----------------| ------------------------------------------------------------ |
        | "none"      | 无跟随，实际计算的时候只考虑absoluteValue |
        | "parent"    | 跟随控件为父控件 |
        | "maxChildren"     | 跟随控件为最大子控件（设置x则为最大宽度，设置y则为最大高度），relativeValue无论如何设置都为1.0 |
        | "maxSibling"   | 跟随控件为最大兄弟控件（设置x则为最大宽度，设置y则为最大高度），relativeValue无论如何设置都为1.0 |
        | "children"        | 跟随值等于所有子节点之和（如果是x则计算的是子节点的宽度之和，如果是y则计算的是子节点的高度之和） |
        | "x"  | 跟随值等于控件本身的宽度，该值仅当 axis == "y" 才生效|
        | "y"  | 跟随值等于控件本身的高度，该值仅当 axis == "x" 才生效|
    - 设置跟随类型的时候请务必小心，不要造成依赖循环，比如父控件x坐标依赖子控件的宽度，而子控件的宽度又依赖于父控件这类情况，这样即使设置成功，结果也是未知的

- 示例

```python
imagePath = "/panel/image1"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
# 设置image1的位置在父控件的中间
ret = baseUIControl.SetFullPosition(axis="x", paramDict={"followType":"parent", "relativeValue":0.5})
ret = baseUIControl.SetFullPosition(axis="y", paramDict={"followType":"parent", "relativeValue":0.5})
```



## SetFullSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件的大小，支持比例形式以及绝对值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | axis | str | 设置的轴向，可选的值有["x","y"]，"x"表示设置控件的宽度，"y"表示设置控件的高度 |
    | paramDict | dict | 设置的参数，具体见备注 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - paramDict的键值
        | 参数名       |  参数类型       | 解释                                                         |
        | ----------------| --------------|---------------------------------------------- |
        | "fit"| bool | 是否自适应父控件，默认值为False，可以不写该键值|
        | "followType"| str | 跟随类型，默认值为"none"，可以不写该键值|
        | "relativeValue"| float | 相对于跟随控件的比例值，默认值为0，可以不写该键值|
        | "absoluteValue"| float | 设置的绝对值，默认值为0，可以不写该键值 |
    - 控件的大小支持复杂的计算来实现自适应布局，形式为“absoluteValue + relativeValue * 跟随值”。
        其中跟随值由跟随的控件以及当前设置的属性共同决定。比如当前设置的是控件的宽度，并且跟随控件为父控件，则跟随值为父控件的宽度。
        而跟随的控件是特定的，是与控件本身有一定关系的，比如控件的父控件，子控件等，可以通过设置followType的值来指定。
    - followType可选的值
        | 值              | 解释                                                         |
        | ----------------| ------------------------------------------------------------ |
        | "none"      | 无跟随，实际计算的时候只考虑absoluteValue |
        | "parent"    | 跟随控件为父控件 |
        | "maxChildren"     | 跟随控件为最大子控件（设置宽度则为最大宽度，设置高度则为最大高度），relativeValue无论如何设置都为1.0 |
        | "maxSibling"   | 跟随控件为最大兄弟控件（设置宽度则为最大宽度，设置高度则为最大高度），relativeValue无论如何设置都为1.0  |
        | "children"        | 跟随值等于所有子节点之和 |
        | "x"  | 跟随值等于控件本身的宽度，该值仅当 axis == "y" 才生效|
        | "y"  | 跟随值等于控件本身的高度，该值仅当 axis == "x" 才生效|
    - fit参数用来指定是否自适应父控件，如果是自适应父控件，则absoluteValue，followType，relativeValue参数均会失效，控件的值直接取自父控件的值
    - 设置跟随类型的时候请务必小心，不要造成依赖循环，比如父控件宽度依赖子控件的宽度，而子控件的宽度又依赖于父控件这类情况，这样即使设置成功，结果也是未知的

- 示例

```python
imagePath = "/panel/image1"
baseUIControl = uiNode.GetBaseUIControl(imagePath)
# 设置image1的宽度为父节点的一半，
ret = baseUIControl.SetFullSize(axis="x", paramDict={"followType":"parent", "relativeValue":0.5})
# 设置image1的高度为所有子节点的高度的2倍并且多20像素
ret = baseUIControl.SetFullSize(axis="y", paramDict={"absoluteValue":20, "followType":"children", "relativeValue":2})
# 设置image1的宽，高为父亲节点的宽，高
ret = baseUIControl.SetFullSize(axis="x", {"fit":True})
ret = baseUIControl.SetFullSize(axis="y", {"fit":True})
```



## SetGridDimension

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.gridUIControl.GridUIControl

- 描述

    设置Grid控件的大小

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | tuple(int,int) | 设置网格的横向与纵向大小 |

- 返回值

    无

- 示例

```python
# we want change grid dimension
gridPath = "/grid1"
gridUIControl = uiNode.GetBaseUIControl(gridPath).asGrid()
gridUIControl.SetGridDimension((2, 2))
```



## SetHighestY

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    设置绘制地图的最大高度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | highestY | int | 绘制高度值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 动态调整高度值后，已经绘制过的区块不会刷新为新的高度值，只有没有绘制过的区块会以新的高度值来绘制。

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.SetHighestY(255)
```



## SetHoverCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.selectionWheelUIControl.SelectionWheelUIControl

- 描述

    设置轮盘选择切片触发回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callbackFunc | function | 回调函数，必须是UI的类函数，并且无参数 |

- 返回值

    无

- 示例

```python
def onSelectionWheelHover():
    pass

selectionWheelPath = "/selectionWheel"
selectionWheelControl = uiNode.GetBaseUIControl(selectionWheelPath).asSelectionWheel()
selectionWheelControl.SetHoverCallback(onSelectionWheelHover)
```



## SetImageAdaptionType

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    设置图片控件的图片适配方式以及信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | imageAdaptionType | str | 图片控件的图片适配方式，可选的值详见备注 |
    | imageAdaptionData | tuple(float,float,float,float) | 如果图片不是九宫适配方式，无需传该值，否则需要设置，tuple的每个值分别代表九宫格切割的四个参数：左，右，上，下 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - imageAdaptionType可选的值如下
        | 值                      | 解释                                          |
        | ------------------------| --------------------------------------------- |
        | "normal"       | 普通适配，不开启九宫并保持宽高比 |
        | "filled"       | 填充适配，不开启九宫并保持宽高比 |
        | "oldNineSlice"   | 旧版九宫格适配 |
        | "originNineSlice"       | 原版九宫格适配 |

- 示例

```python
imagePath = "/image"
imageUIControl = uiNode.GetBaseUIControl(imagePath).asImage()
# 普通适配
ret = imageUIControl.SetImageAdaptionType("normal")
# 原版九公格适配，并设置边距
ret = imageUIControl.SetImageAdaptionType("originNineSlice", (0, 0, 0, 0))
```



## SetIsModal

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.inputPanelUIControl.InputPanelUIControl

- 描述

    设置当前面板是否为模态框

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isModal | bool | 当前面板是否为模态框 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# we want to set inputPanel1 isModal
inputPanelPath = "/inputPanel1"
inputPanel = uiNode.GetBaseUIControl(inputPanelPath).asInputPanel()
ret = inputPanel.SetIsModal(True)
```



## SetIsSwallow

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.inputPanelUIControl.InputPanelUIControl

- 描述

    设置当前面板输入是否会吞噬事件，isSwallow为Ture时，点击时，点击事件不会穿透到世界。如破坏方块、镜头转向不会被响应

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isSwallow | bool | 设置当前面板输入是否会吞噬事件 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# we want to set inputPanel1 isSwallow
inputPanelPath = "/inputPanel1"
inputPanel = uiNode.GetBaseUIControl(inputPanelPath).asInputPanel()
ret = inputPanel.SetIsSwallow(True)
```



## SetLayer

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件节点的层级，可以通过传入空字符串（""）的方式来调整整个JSON的基础层级

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | layer | int | 设置层级 |
    | syncRefresh | bool | 是否需要同步刷新，默认值为True。置True为游戏在同一帧根据该控件的层级进行相关计算，置False则在下一帧进行计算。如同一帧有大量SetLayer操作建议置False，操作结束后调用一次ScreenNode.UpdateScreen接口刷新界面及相关控件数据 |
    | forceUpdate | bool | 是否需要强制刷新，默认值为True。置True则按照syncRefresh逻辑进行同步或者下一帧刷新，置False则当前帧和下一帧均不刷新，需要手动调用UpdateScreen进行刷新。如有大量SetLayer操作且非在同一帧执行，建议设置为False,需要更新时再调用UpdateScreen接口刷新界面及相关控件数据 |

- 返回值

    无

- 示例

```python
# 设置text2的控件的层级
text2Path = "/panel/text2"
baseUIControl = uiNode.GetBaseUIControl(text2Path)
baseUIControl.SetLayer(2)
# 同一帧设置若干控件的层级
text1Path = "/panel/text1"
uiNode.GetBaseUIControl(text1Path).SetLayer(1,False)
text2Path = "/panel/text2"
uiNode.GetBaseUIControl(text2Path).SetLayer(2,False)
text3Path = "/panel/text3"
uiNode.GetBaseUIControl(text3Path).SetLayer(3,False)
# 不同帧设置若干控件的层级
def _setLyerText1(path, layer):
    uiNode.GetBaseUIControl(text1Path).SetLayer(1,False,False)
def _updateScreen():
    uiNode.UpdateScreen(True)
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
comp.AddTimer(100, _setLyerText1, "/panel/text1", 1)
comp.AddTimer(200, _setLyerText1, "/panel/text2", 2)
comp.AddTimer(300, _setLyerText1, "/panel/text3", 3)
comp.AddTimer(300, _updateScreen)
```



## SetMaxSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件所允许的最大的大小值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | maxSize | tuple(float,float) | 该控件所允许的最大的大小值，第一项为横轴，第二项为纵轴 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - maxSize = (0, 0)表示无限制

- 示例

```python
# we want to set image1 maxSize
imagePath = "/panel/image1"
imageMaxSize = (10, 10)
baseUIControl = uiNode.GetBaseUIControl(imagePath)
ret = baseUIControl.SetMaxSize(imageMaxSize)
```



## SetMinSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件所允许的最小的大小值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | minSize | tuple(float,float) | 该控件所允许的大小值，第一项为横轴，第二项为纵轴 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - minSize = (0, 0)表示无限制

- 示例

```python
# we want to set image1 minSize
imagePath = "/panel/image1"
imageMinSize = (10, 10)
baseUIControl = uiNode.GetBaseUIControl(imagePath)
ret = baseUIControl.SetMinSize(imageMinSize)
```



## SetOffsetDelta

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.inputPanelUIControl.InputPanelUIControl

- 描述

    设置点击面板的拖拽偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | offset_delta | tuple(float,float) | 该控件的拖拽偏移量，第一项为横轴，第二项为纵轴 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 点击面板拖拽功能及拖拽偏移量相关，详见<a href="../../../../mcguide/18-界面与交互/30-UI说明文档.html#InputPanel">InputPanel</a>

- 示例

```python
# we want to set inputPanel's offset_delta
inputPanelPath = "/inputPanel1"
inputPanel = uiNode.GetBaseUIControl(inputPanelPath).asInputPanel()
success = inputPanel.SetOffsetDelta((100, 100))
```



## SetOrientation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.stackPanelUIControl.StackPanelUIControl

- 描述

    设置stackPanel的排列方向

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | orientation | str | stackPanel的排列方向，取值有限为["vertical", "horizontal"]，分别表示垂直方向，水平方向 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# we want to set stackPanel1 orientation
stackPanelPath = "/stackPanel1"
stackPanel = uiNode.GetBaseUIControl(stackPanelPath).asStackPanel()
orientation = "vertical"
stackPanel.SetOrientation(orientation)
```



## SetPosition

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件相对父节点的坐标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float) | 该控件相对父节点的坐标信息，第一项为横轴，第二项为纵轴 |

- 返回值

    无

- 示例

```python
# we want to set text2 position
text2Path = "/panel/text2"
pos = (10, 10)
baseUIControl = uiNode.GetBaseUIControl(text2Path)
baseUIControl.SetPosition(pos)
```



## SetPropertyBag

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置PropertyBag,将使用字典中的每个值来覆盖原本PropertyBag中的值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | params | dict | 需要设置的属性字典，字典键值对的值仅支持设置字符串、数字、布尔值类型，其余类型会导致设置失败 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
text2Path = "/panel/text2"
baseUIControl = uiNode.GetBaseUIControl(text2Path)
params = {"text": "hello world", "number": 123, "boolean": True}
success = baseUIControl.SetPropertyBag(params)
```



## SetRotatePivot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    设置图片自身旋转锚点，该点并不是固定的点，而是相对于自身位置的点

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pivot | tuple(float,float) | 相对于自身位置的锚点，第一项为横轴x，第二项为纵轴y，锚点实际坐标=图片的position + anchor * (width, height) |

- 返回值

    无

- 备注
    - 自身的旋转锚点是一个相对坐标，它是根据图片当前所在位置和大小进行计算的，所以一旦设置后，就会每帧都进行位置的计算。如果不调用该函数，默认状态下图片的旋转锚点是 (0.5, 0.5)

- 示例

```python
imagePath = "/imagePath"
imageControl = uiNode.GetBaseUIControl(imagePath).asImage()
# 设置旋转锚点为图片的左上角
imageControl.SetRotatePivot((0, 0))
# 设置旋转锚点为图片的右上角
imageControl.SetRotatePivot((1, 0))
# 设置旋转锚点为图片的右下角
imageControl.SetRotatePivot((1, 1))
# 设置旋转锚点为图片的左下角
imageControl.SetRotatePivot((0, 1))
```



## SetScrollViewPercentValue

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.scrollViewUIControl.ScrollViewUIControl

- 描述

    设置当前scroll_view内容的百分比位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | percent_value | int | 需要跳转到的百分比位置，一般设置的位置会出现在scroll_view的最上方。该值取值范围0-100 |

- 返回值

    无

- 示例

```python
# we want set scroll_view percent pos
scrollViewPath = "/scroll_view0"
scrollViewUIControl = uiNode.GetBaseUIControl(scrollViewPath).asScrollView()
scrollViewUIControl.SetScrollViewPercentValue(20)
```



## SetScrollViewPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.scrollViewUIControl.ScrollViewUIControl

- 描述

    设置当前scroll_view内容的位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | float | 需要跳转到的位置，一般设置的位置会出现在scroll_view的最上方。 |

- 返回值

    无

- 示例

```python
# we want set scroll_view pos
scrollViewPath = "/scroll_view0"
scrollViewUIControl = uiNode.GetBaseUIControl(scrollViewPath).asScrollView()
scrollViewUIControl.SetScrollViewPos(100)
```



## SetSelectOptionByIndex

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    根据提供的索引选中对应下拉框项

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | index | int | 索引 |

- 返回值

    无

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
comboBoxUIControl.SetSelectOptionByIndex(0)
```



## SetSelectOptionByShowName

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.neteaseComboBoxUIControl.NeteaseComboBoxUIControl

- 描述

    根据提供的展示文本选中对应下拉框项

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 索引 |

- 返回值

    无

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
comboBoxUIControl.SetSelectOptionByShowName("测试项")
```



## SetSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件的大小

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | size | tuple(float,float) | 该控件的大小信息，第一项为横轴，第二项为纵轴 |
    | resizeChildren | bool | 是否同时调整子控件尺寸，默认为False |

- 返回值

    无

- 示例

```python
# we want to set text2 size
text2Path = "/panel/text2"
text2Size = (10, 10)
baseUIControl = uiNode.GetBaseUIControl(text2Path)
baseUIControl.SetSize(text2Size)
```



## SetSliderValue

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.sliderUIControl.SliderUIControl

- 描述

    设置滑动条的值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | float | 滑动条的值 |

- 返回值

    无

- 示例

```python
# we want to set slider value
sliderPath = "/panel/slider0"
sliderUIControl = uiNode.GetBaseUIControl(sliderPath).asSlider()
sliderUIControl.SetSliderValue(0.5) # 百分比滑动条
# sliderUIControl.SetSliderValue(5) # 固定格类型滑动条
```



## SetSprite

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    给图片控件换指定贴图

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | texturePath | str | 贴图的路径，需要从resource_pack下面的textures目录开始 |

- 返回值

    无

- 备注
    - 给ImageButton换贴图的时候注意使用子控件路径(default / hover / pressed)获得ImageUIControl

- 示例

```python
# we want to set image_button textures
imageButtonPath = "/image_button"
buttonUIControl = uiNode.GetBaseUIControl(imageButtonPath).asButton()
buttonDefaultUIControl = buttonUIControl.GetChildByName("default").asImage()
buttonHoverUIControl = buttonUIControl.GetChildByName("hover").asImage()
buttonPressedUIControl = buttonUIControl.GetChildByName("pressed").asImage()
buttonDefaultUIControl.SetSprite("textures/button01_default")
buttonHoverUIControl.SetSprite("textures/button01_hover")
buttonPressedUIControl.SetSprite("textures/button01_pressed")
```



## SetSpriteClipRatio

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    设置图片的裁剪区域比例（不改变控件尺寸）。可以配合image控件的clip_ratio属性控制方向。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | clipRatio | float | 图片的裁剪比例（范围0到1），裁剪精度与图片分辨率相关 |

- 返回值

    无

- 示例

```python
# 我们想对UI编辑器创建的进度条设置进度
# 编辑器进度条包含两个image控件（名为empty_progress_bar和filled_progress_bar）
progress = 0.8  # 用于模拟进度时，下面的裁剪比例需设为(1-进度)，才能得到正确的视觉效果
imagePath = "/progress_bar0/filled_progress_bar"
imageUIControl = uiNode.GetBaseUIControl(imagePath).asImage()
imageUIControl.SetSpriteClipRatio(1.0 - progress)
```



## SetSpriteColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    设置图片颜色

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | color | tuple(float,float,float) | 图片颜色rgb，取值[0, 1] |

- 返回值

    无

- 示例

```python
# 我们想对耐久度条随耐久度变化颜色，满的时候为绿色，空的时候为红色，其中barPath为耐久度条路径
durabilityRatio = 0.8  # 耐久度比例，1为满耐久
barPath = "/image_bar"
imageUIControl = uiNode.GetBaseUIControl(barPath).asImage()
imageUIControl.SetSpriteColor((1 - durabilityRatio, durabilityRatio, 0))
```



## SetSpriteGray

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    给图片控件置灰，比直接SetSprite一张灰图片效率要高

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | gray | bool | True为将图片置灰，False为恢复原色 |

- 返回值

    无

- 示例

```python
# we want set image gray
imagePath = "/image"
imageUIControl = uiNode.GetBaseUIControl(imagePath).asImage()
imageUIControl.SetSpriteGray(True)
```



## SetSpritePlatformFrame

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    设置图片为我的世界移动端启动器当前帐号的头像框

- 参数

    无

- 返回值

    无

- 备注
    - 该接口仅支持移动端调用，其他平台该接口无效：
    - 当我的世界移动端启动器账号的头像框是动态头像框时，该头像框图片将无法被加载，该问题将在下个版本修复：

- 示例

```python
# 我们想将当前图片控件设置为我的世界移动端启动器当前帐号的头像框
imagePath = "/image"
imageUIControl = uiNode.GetBaseUIControl(imagePath).asImage()
imageUIControl.SetSpritePlatformFrame()
```



## SetSpritePlatformHead

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    设置图片为我的世界移动端启动器当前帐号的头像

- 参数

    无

- 返回值

    无

- 备注
    - 该接口仅支持移动端调用，其他平台该接口无效：

- 示例

```python
# 我们想将当前图片控件设置为我的世界移动端启动器当前帐号的头像
imagePath = "/image"
imageUIControl = uiNode.GetBaseUIControl(imagePath).asImage()
imageUIControl.SetSpritePlatformHead()
```



## SetSpriteUV

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    设置图片的起始uv，与json中的"uv"属性作用一致

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | uv | tuple(float,float) | 图片的左上角为(0,0)，向右为x轴，向下为y轴 |

- 返回值

    无

- 示例

```python
imagePath = "/image"
imageUIControl = uiNode.GetBaseUIControl(imagePath).asImage()
imageUIControl.SetSpriteUV((10, 0))
```



## SetSpriteUVSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.imageUIControl.ImageUIControl

- 描述

    设置图片的uv大小，与json中的"uv_size"属性作用一致

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | uvSize | tuple(float,float) | 图片向右为x轴，向下为y轴 |

- 返回值

    无

- 示例

```python
imagePath = "/image"
imageUIControl = uiNode.GetBaseUIControl(imagePath).asImage()
imageUIControl.SetSpriteUVSize((40, 30))
```



## SetText

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    设置Label的文本信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | text | str | 文本的内容，可以支持[样式代码](https://zh.minecraft.wiki/w/%E6%A0%BC%E5%BC%8F%E5%8C%96%E4%BB%A3%E7%A0%81)（§可以设置文字的颜色、格式等，该种用法更加灵活多变） |
    | syncSize | bool | 是否设置文本时同步更新文本框大小，默认值为False |

- 返回值

    无

- 示例

```python
# we want to set text2 content
text2Path = "/panel/text2"
text = "Hello World!"
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
labelUIControl.SetText(text)
```



## SetTextAlignment

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    设置文本控件的文本对齐方式

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | textAlignment | str | 文本控件的文本对齐方式，可选的值详见备注 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - textAlignment可选的值
        | 值              | 解释                                                         |
        | ----------------| ------------------------------------------------------------ |
        | "left"          | 文本左对齐（水平方向）  |
        | "right"         | 文本右对齐（水平方向）  |
        | "center"        | 文本居中对齐（水平方向）|

- 示例

```python
# we want to align text2 to center
text2Path = "/panel/text2"
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
textAlignment = "center"
ret = labelUIControl.SetTextAlignment(textAlignment)
```



## SetTextColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    设置Label文本的颜色

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | color | tuple(float,float,float) | 文本的颜色信息(r, g, b)，取值[0, 1] |

- 返回值

    无

- 备注
    - 该接口不支持传入alpha通道改变透明度，建议使用SetAlpha接口

- 示例

```python
# we want to set text2 green
text2Path = "/panel/text2"
color = (0, 1, 0)
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
labelUIControl.SetTextColor(color)
```



## SetTextFontSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    设置Label中文本字体的大小

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | scale | float | label的font_size的作用是Label中的默认字体大小，取值有限为[small normal large]，这个scale是在这个默认字体的基础上进行缩放字体大小，默认字体大小为1.0 |

- 返回值

    无

- 示例

```python
# set text font size
text2Path = "/panel/text2"
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
labelUIControl.SetTextFontSize(0.8)
```



## SetTextLinePadding

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.labelUIControl.LabelUIControl

- 描述

    设置文本控件的行间距

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | textLinePadding | float | 文本控件的行间距，单位为像素 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# we want to set text2 textLinePadding
text2Path = "/panel/text2"
labelUIControl = uiNode.GetBaseUIControl(text2Path).asLabel()
textLinePadding = 20
ret = labelUIControl.SetTextLinePadding(textLinePadding)
```



## SetToggleState

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.switchToggleUIControl.SwitchToggleUIControl

- 描述

    设置Toggle开关控件的值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | is_on | bool | 设置Toggle开关控件是打开还是关闭状态 |
    | toggle_path | str | 实际toggle控件相对路径，由UI编辑器生成的开关控件该参数即为默认值"/this_toggle" |

- 返回值

    无

- 示例

```python
togglePath = "/toggle1"
switchToggleUIControl = uiNode.GetBaseUIControl(togglePath).asSwitchToggle()
switchToggleUIControl.SetToggleState(True)
```



## SetTouchEnable

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    设置控件是否可点击交互

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | False为不响应，True为恢复响应 |

- 返回值

    无

- 示例

```python
# we want to set image_button unable
imageButtonPath = "/image_button"
baseUIControl = uiNode.GetBaseUIControl(imageButtonPath)
baseUIControl.SetTouchEnable(False)
```



## SetTouchUpCallback

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.selectionWheelUIControl.SelectionWheelUIControl

- 描述

    设置轮盘选择切片并且鼠标按下抬起后触发回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | callbackFunc | function | 回调函数，必须是UI的类函数，并且无参数 |

- 返回值

    无

- 示例

```python
def onSelectionWheelTouchUp():
    pass

selectionWheelPath = "/selectionWheel"
selectionWheelControl = uiNode.GetBaseUIControl(selectionWheelPath).asSelectionWheel()
selectionWheelControl.SetTouchUpCallback(onSelectionWheelTouchUp)
```



## SetUiItem

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.itemRendererUIControl.ItemRendererUIControl

- 描述

    设置ItemRenderer控件显示的物品，ItemRenderer控件的配置方式详见<a href="../../../../mcguide/18-界面与交互/30-UI说明文档.html#itemrenderer">控件介绍ItemRenderer</a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemName | str | 物品identifier |
    | auxValue | int | 物品附加值 |
    | isEnchanted | bool | 可选参数，是否显示附魔效果，默认为False不显示 |
    | userData | dict | 可选参数，如果是灾厄旗帜或焰火之星等带有userData的需要传入该参数才能正确显示，目前已知仅有灾厄旗帜和焰火之星需要传 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置结果，True为成功 |

- 示例

```python
#设置显示为羊毛wool
itemRenderPath = "/panel/item_renderer"
itemName = "minecraft:wool"
auxValue = 0
itemRendererBaseControl = uiNode.GetBaseUIControl(itemRenderPath)
itemRendererControl = itemRendererBaseControl.asItemRenderer()
itemRendererControl.SetUiItem(itemName, auxValue)
```



## SetValue

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.progressBarUIControl.ProgressBarUIControl

- 描述

    设置进度条的进度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | progress | float | 进度，取值[0, 1] |

- 返回值

    无

- 示例

```python
# we want to set progress
progressBarPath = "/panel/progress_bar"
progressBarUIControl = uiNode.GetBaseUIControl(progressBarPath).asProgressBar()
progressBarUIControl.SetValue(0.8)
```



## SetVisible

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    根据控件路径选择是否显示某控件，可以通过传入空字符串（""）的方式来调整整个JSON的显示/隐藏

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | visible | bool | False为隐藏该控件，True为显示该控件 |
    | forceUpdate | bool | 是否需要强制刷新，默认值为True。置True则按照马上进行刷新，新的visible状态生效。置False，则需要再次调用UpdateScreen使新状态生效。如有大量SetVisible操作且非在同一帧执行，建议设置为False,需要更新时再调用UpdateScreen接口刷新界面及相关控件数据 |

- 返回值

    无

- 备注
    - 特殊情况说明：
        当该接口的调用来自滚动列表内容控件中的按钮回调，且调用目的是隐藏滚动列表控件或其父节点控件时，将forceUpdate参数置True会导致滚动列表数据异常。若没有刷新界面的必要请将forceUpdate参数置False，若有请使用定时器延迟执行手动UpdateScreen接口。

- 示例

```python
# 隐藏panel的子控件text2
text2Path = "/panel/text2"
baseUIControl = uiNode.GetBaseUIControl(text2Path)
baseUIControl.SetVisible(False)
# 在非同一帧，隐藏panel的子控件text1, text2, text3
parentPath = "/panel"
textPrefabPath = "/panel/text_prefab"
def _tickSetVisible(pathName):
    baseUIControl = uiNode.GetBaseUIControl(pathName)
    baseUIControl.SetVisible(False, False)
def _tickUpdateScreen():
    uiNode.UpdateScreen(True)
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
comp.AddTimer(100, _tickSetVisible, "/panel/text1")
comp.AddTimer(200, _tickSetVisible, "/panel/text2")
comp.AddTimer(300, _tickSetVisible, "/panel/text3")
comp.AddTimer(300, _tickUpdateScreen)
```



## StopAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    停止动画，动画将恢复到第一段动画片段的from状态

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | propertyName | str | 动画的属性名称，默认值为"all"，表示停止所有动画，不为"all"的时候表示单个动画的停止，比如propertyName=="size"时，表示停止尺寸属性上的动画 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否停止成功 |

- 备注
    - UI属性动画相关，详见<a href="../../../../mcguide/18-界面与交互/19-控件属性动画.html">属性动画</a>

- 示例

```python
# 获取控件
control = uiNode.GetBaseUIControl("/image")
# 停止所有动画
control.StopAnimation()
# 停止尺寸动画
# control.StopAnimation("size")
# 停止位移动画
# control.StopAnimation("offset")
# 其他属性也是支持停止的，具体可参见备注
```



## ZoomIn

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    放大地图

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | float | 在原有基础上的增量值，可以控制放大速度，默认为0.05 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.ZoomIn(0.2)
```



## ZoomOut

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    缩小地图

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | float | 在原有基础上的减少值，可以控制缩小速度，默认为0.05 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 客户端地图区块加载有限，如果地图UI界面太大或者缩小地图倍数太大，会导致小地图无法显示未加载的区块。

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.ZoomOut(0.2)
```



## ZoomReset

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.minimapUIControl.MiniMapUIControl

- 描述

    恢复地图放缩大小为默认值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
path = "/demoPanel/netease_mini_map"
map = uiNode.GetBaseUIControl(path).asMiniMap()
map.ZoomReset(0.2)
```



## asButton

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为ButtonUIControl实例，如当前控件非button类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ButtonUIControl | ButtonUIControl实例 |

- 示例

```python
buttonPath = "/button"
buttonBaseControl = uiNode.GetBaseUIControl(buttonPath)
buttonControl = buttonBaseControl.asButton()
```



## asGrid

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为GridUIControl实例，如当前控件非grid类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | GridUIControl | GridUIControl实例 |

- 示例

```python
gridPath = "/grid"
gridBaseControl = uiNode.GetBaseUIControl(gridPath)
gridControl = gridBaseControl.asGrid()
```



## asImage

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为ImageUIControl实例，如当前控件非image类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ImageUIControl | ImageUIControl实例 |

- 示例

```python
imagePath = "/image"
imageBaseControl = uiNode.GetBaseUIControl(imagePath)
imageControl = imageBaseControl.asImage()
```



## asInputPanel

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为InputPanelUIControl实例，如当前控件非inputPanel类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | InputPanelUIControl | InputPanelUIControl实例 |

- 示例

```python
inputPanelPath = "/inputPanel"
inputPanelUIControl = uiNode.GetBaseUIControl(inputPanelPath).asInputPanel()
```



## asItemRenderer

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为ItemRenderer实例，如当前控件非custom类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ItemRendererUIControl | ItemRendererUIControl实例 |

- 示例

```python
itemRendererPath = "/item_renderer"
itemRendererBaseControl = uiNode.GetBaseUIControl(itemRendererPath)
itemRendererControl = itemRendererBaseControl.asItemRenderer()
```



## asLabel

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为LabelUIControl实例，如当前控件非Label类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | LabelUIControl | LabelUIControl实例 |

- 示例

```python
text1Path = "/text1"
text1BaseControl = uiNode.GetBaseUIControl(text1Path)
text1LabelControl = text1BaseControl.asLabel()
```



## asMiniMap

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为MiniMapUIControl实例，如当前控件非小地图类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | MiniMapUIControl | MiniMapUIControl实例 |

- 示例

```python
path = "/mini_map"
miniMapBaseControl = uiNode.GetBaseUIControl(path)
miniMapControl = miniMapBaseControl.asMiniMap()
```



## asNeteaseComboBox

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为NeteaseComboBoxUIControl实例，如当前控件非panel类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | NeteaseComboBoxUIControl | NeteaseComboBoxUIControl实例 |

- 示例

```python
comboBoxPath = "/panel/comboBoxPanel"
comboBoxUIControl = uiNode.GetBaseUIControl(comboBoxPath).asNeteaseComboBox()
```



## asNeteasePaperDoll

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为NeteasePaperDollUIControl实例，如当前控件非custom类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | NeteasePaperDollUIControl | NeteasePaperDollUIControl实例 |

- 示例

```python
paperDollPath = "/paper_doll"
paperDollBaseControl = uiNode.GetBaseUIControl(paperDollPath)
paperDollControl = paperDollBaseControl.asNeteasePaperDoll()
```



## asProgressBar

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为ProgressBarUIControl实例，如当前控件非panel类型则返回None

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fillImagePath | str | 进度条填充图片路径，默认为"/filled_progress_bar",该参数影响该控件API的效果 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ProgressBarUIControl | ProgressBarUIControl实例 |

- 示例

```python
progressBarPath = "/progress_bar"
progressBarBaseControl = uiNode.GetBaseUIControl(progressBarPath)
progressBarControl = progressBarBaseControl.asProgressBar()
```



## asScrollView

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为ScrollViewUIControl实例，如当前控件非scrollview类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ScrollViewUIControl | ScrollViewUIControl实例 |

- 示例

```python
scrollViewPath = "/scroll_view"
scrollViewBaseControl = uiNode.GetBaseUIControl(scrollViewPath)
scrollViewControl = scrollviewBaseControl.asScrollView()
```



## asSelectionWheel

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为SelectionWheelUIControl实例，如当前控件非selectionWheel类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | SelectionWheelUIControl | SelectionWheelUIControl实例 |

- 示例

```python
selectionWheelPath = "/selectionWheel"
selectionWheelControl = uiNode.GetBaseUIControl(selectionWheelPath).asSelectionWheel()
```



## asSlider

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为SliderUIControl实例，如当前控件非滑动条类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | SliderUIControl | SliderUIControl |

- 示例

```python
path = "/slider0"
sliderBaseControl = uiNode.GetBaseUIControl(path)
sliderControl = sliderBaseControl.asSlider()
```



## asStackPanel

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为StackPanelUIControl实例，如当前控件非stackPanel类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | StackPanelUIControl | StackPanelUIControl实例 |

- 示例

```python
stackPanelPath = "/stackPanel"
stackPanelUIControl = uiNode.GetBaseUIControl(stackPanelPath).asStackPanel()
```



## asSwitchToggle

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为SwitchToggleUIControl实例，如当前控件非panel类型或非toggle则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | SwitchToggleUIControl | SwitchToggleUIControl实例 |

- 示例

```python
switchTogglePath = "/switch_toggle"
switchToggleBaseControl = uiNode.GetBaseUIControl(switchTogglePath)
switchToggleControl = switchToggleBaseControl.asSwitchToggle()
```



## asTextEditBox

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    将当前BaseUIControl转换为TextEditBoxUIControl实例，如当前控件非editbox类型则返回None

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | TextEditBoxUIControl | TextEditBoxUIControl实例 |

- 示例

```python
textEditBoxPath = "/text_edit_box"
textEditBoxBaseControl = uiNode.GetBaseUIControl(textEditBoxPath)
textEditBoxControl = textEditBoxBaseControl.asTextEditBox()
```



## resetAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.ui.controls.baseUIControl.BaseUIControl

- 描述

    重置该控件的动画

- 参数

    无

- 返回值

    无

- 备注
    - UI属性动画相关，详见<a href="../../../../mcguide/18-界面与交互/19-控件属性动画.html">属性动画</a>

- 示例

```python
# 重置/text1控件上的属性动画
text1Path = "/text1"
text1Control = uiNode.GetBaseUIControl(text1Path)
text1Control.resetAnimation()
```



