---
front:
hard: 入门
time: 分钟
---

# 自定义熔炉Demo

### 概述

[CustomFurnaceMod](../../13-模组SDK编程/60-Demo示例.md#CustomFurnaceMod)利用自定义方块以及ModSDK相关事件及接口复刻了原版熔炉的UI及逻辑。

**注：在该demo中采用的是PE的尺寸，在PC上更改窗口大小可能会造成背包界面一定的显示误差**



### 已支持功能

- 一个自定义方块
- 点击该方块会打开熔炉界面
- 界面包含以下功能：
  - 界面和原版熔炉一致
  - 界面的背包可以正常显示玩家背包的物品
  - 点击背包格子，再点击输入格子，可以交换两个格子的物品
  - 点击背包格子，再点击燃料格子，可以交换两个格子的物品
  - 当燃料格子和输入格子中都有物品，且物品组合在配置中存在时，隔一定时间消耗燃料和输入，在输出格子生成1个物品
  - 交换物品时有飞行动画
  - 燃烧时有对应的火焰燃烧动画和进度动画
- 输出格子物品达到叠加上限时，停止生成
- 输入格子和燃料格子、输出格子中的物品会存储在blockentity中，即使没有打开熔炉也会继续烧炼



### 1.18新增功能

- 长按分堆操作
- 双击合堆操作
- 点击物品格子显示tips
- 装备耐久度显示
- 物品附魔状态显示
- 正确显示灾厄旗帜及各种经织布机织过的旗帜
- 点选物品格子之后点击其他地方丢弃物品
- 方块破坏后会掉落方块中的物品
- 方块被破坏、玩家死后正确关闭UI
- 在打开UI的情况下获取物品能够正确更新UI
- 生成物品时不需要再由开发者控制生成的最大堆叠数，由相应的接口直接获取



### Demo主要文件介绍

- recipeMgrBase.py
  - 实现烧炼配方基类的管理，一类自定义熔炉方块对应一个熔炉配方类，熔炉配方类继承自该基类，需实现如下基础接口：
    - `GetFurnaceResult(self, inputItem)`：根据原料返回生成物
    - `GetBurnDuration(self, fuelItem)`：根据燃料返回燃料燃烧时间
    - `IsFuelItem(self, item)`：根据传入item判断是否为燃料
  - 烧炼配方及燃烧列表在各子类中初始化的时候配置，如果燃料不在烧炼列表中将无法放置到燃料槽
- furnaceMgrBase.py
  - 熔炉管理基类，实现熔炉的烧炼逻辑，需要在ServerBlockEntityTickEvent事件中对自定义熔炉方块进行Tick，主要烧炼判断在Tick函数中进行，如果Tick结束有UI或者数据发生变动，需要更新客户端UI以及服务端blockEntityData
  - 一类自定义熔炉方块对应一个熔炉管理类，熔炉管理类继承自该类，需实现如下接口：
    - `CanBurn(self)`：判断是否能够烧炼
    - `Burn(self)`：烧炼过程，消耗原料生成烧料物
    - `CanSet(self, slotName, item)`：传入槽名和物品，返回是否可以放置
- customFurnaceServer.py
  - 自定义熔炉服务端，继承自CustomContainerServerSystem，基类实现了打开容器、破坏容器以及基础的交换物品和丢弃物品功能，需在子类实现如下接口
    - `GetCustomContainerItems(self, dimension, blockName, blockPos)`传入自定义容器方块的数据，返回容器中所有item信息
    - `OnCustomContainerItemSwap(self, playerId, fromSlot, fromItem, toSlot, toItem)`当交换的物品涉及自定义容器时调用，返回True表示允许交换，返回False禁止交换，交换成功时需要更新对应容器方块的blockEntityData
    - `ResetCustomContainer(self, dimension, blockName, blockPos)`当自定义熔炉被摧毁的时候调用，需要在该函数下删除对应的furnaceManager
    - `OnCustomContainerItemDrop(self, playerId, slot)`当丢弃自定义容器的物品时调用，返回True表示允许丢弃，返回False禁止丢弃，丢弃成功时需要更新对应容器方块的blockEntityData
  - OnBlockEntityTick:在该事件下实现自定义熔炉的tick逻辑
- customFurnaceClient.py
  - OnCustomFurnaceChanged处理服务端发来的烧炼状态发生变化的事件，包括燃烧状态发生变化以及熔炉数据发生变化，更新UI显示
  - OpenCustomFurnace处理服务端发来的打开UI事件
  - OnItemSwap处理服务端发来的物品交换事件
- customFurnaceUI.py
  - 对熔炉界面进行管理，继承自CustomContainerUIScreenBase，需实现以下接口
    - `InitCustomContainerUI(self, args)`：初始化自定义容器的UI，demo中是初始化自定义熔炉中输入、燃料和生成三个槽的UI
    - `UpdateCustomContainerUI(self, args)`：更新自定义容器的UI，demo中更新了燃烧状态、燃料数据以及自定义槽位的UI
  - `Update(self)`：该函数每帧调用，需先执行父类的Update，然后再实现自己的Update逻辑。其中父类的Update实现了交换物品时的飞行动画，
- modConfig.py
  - 需在该文件配置以下数据
    - BURN_INTERVAL：燃烧时间间隔，int，单位秒，每经过该间隔可烧炼生成物品，目前是所有熔炉统一的，如有需求开发者可以自行修改
    - FLY_ANIMATION_DURATION：飞行动画时间间隔，int，单位帧，开发者可以根据自己想要的表现形式来配置该帧数
    - CUSTOM_CONTAINER_LIST：list，存放所有自定义熔炉方块的identifier
    - FURNACE_SLOT_NUM_DICT：dict，存放所有自定义熔炉方块对应的自定义槽数，至少3个（原料槽、燃料槽和生成槽各一个），目前架构仅支持1个生成槽+1个燃料槽+n个原料槽（大于等于1）
    - FURNACE_SLOT_PREFIX：自定义熔炉槽前缀，用于UI文件中命名，必须严格满足“前缀+数字”的格式，比如`furnaceSlot0`，在本demo中，序号0为生成槽，1为燃料槽，大于1为原料槽
    - UI_DEFS：自定义容器的UI对应关系，为字典类型，key是自定义容器对应的自定义方块的identifier，value为其配置，包括以下几个字段
      - `uiName`，对应ui的json文件名（不含.json）
      - `uiClassPath`，对应容器的ui管理类
      - `uiScreenDef`，对应UI的根节点
- furnaceManagerFactory.py
  - 熔炉管理工厂类，根据方块名称创建不同的熔炉管理类，如果开发者有创建不同自定义熔炉的需求需要在这里加上对应的工厂生成方法



### UI实现细节

- neteaseCommonUI.json
  - 该文件提供了一些模板控件，比如itemBtn，可以作为背包格子或者熔炉格子
  - 可以通过继承来使用这些控件，参考customFurnaceUI.json中的`furnaceSlot0`
- 背包界面
  - 采用ScrollView滑动窗口
  - 窗口内容采用Grid网格排列
  - Grid的模板组件主要分为4部分，可复用该控件模板，参考自定义熔炉槽位
    - Button负责相应点击
    - Image负责显示点击状态
    - Label负责显示堆叠数
    - ItemRenderer负责显示物品渲染
  - 点选时候的物品信息Tips使用了alpha属性来控制透明度，同时通过binding绑定来控制该alpha属性以实现渐隐效果
- 熔炉界面
  - 熔炉槽实现同Grid模板组件
  - 火焰及烧炼进度调用SetSpriteClipRatio新图片裁剪接口实现燃烧动画
- 飞行动画
  - 通过一个imagePool来管理飞行的ItemRenderer，在交换物品时显示其他时候隐藏，并在Update中调用SetPosition来更新其位置实现飞行动画效果
- 其他
  - 背景图片采用Image原生九宫格裁剪



### 基于Demo扩展开发流程（参考）

假设我们的需求是开发一个使用不同配方的自定义熔炉

1. 创建一个自定义方块，并把其identifier添加到modConfig.py的CUSTOM_FURNACE_LIST和FURNACE_SLOT_NUM_DICT中，因为UI没有做改动，FURNACE_SLOT_NUM_DICT中对应的槽数同样是3
2. 创建一个newFurnaceRecipeMgr.py，继承自RecipeManagerBase配方管理基类，并实现GetFurnaceResult、GetBurnDuration、IsFuelItem三个接口，在初始化函数中配置对应的配方列表及燃料列表，可参考furnaceRecipeManager.py
3. 创建一个newFurnaceManagerGas.py，继承自FurnaceManagerBase熔炉管理基类，在初始化函数中初始化对应的配方管理类，使用第二步中创建的配方管理类`self.recipeMgr = NewFurnaceRecipeManager()`，并实现CanBurn、Burn、CanSet三个接口，可参考furnaceManagerGas.py
4. 在furnaceManagerFactory.py中添加自定义方块名对应的工厂创建方法

注：目前所有自定义熔炉使用同一个UI，如果有添加原料槽的需求除了需要改动上述地方外，还需要修改customFurnaceUI.json文件，增加对应槽的UI，命名方式必须严格满足“前缀+数字”的格式，比如`furnaceSlot3`（0、1、2依次为生成槽、燃料槽和默认原料槽，新增的槽编号从3开始逐个添加），槽位UI可以直接继承`neteaseCommonUI.itemBtn`，并将该控件节点放置于`rightPanel`下即可，代码如下：

```json
"furnaceSlot0@neteaseCommonUI.itemBtn" : {
    "$item_button_layer" : 14,
    "$item_button_offset" : [ 42, -16 ],
    "$item_button_size" : [ 32.0, 32.0 ],
    "$item_button_anchor_from" : "center",
    "$item_button_anchor_to" : "center"
}
```

其中各字段数据解释如下：

|          字段名          |          描述          |  默认值  |
| :----------------------: | :--------------------: | :------: |
|    $item_button_layer    |        显示层级        |    1     |
|   $item_button_offset    |          偏移          |  [0, 0]  |
|    $item_button_size     |          尺寸          | [28, 28] |
| $item_button_anchor_from | 挂接在父节点锚点的位置 | "center" |
|  $item_button_anchor_to  |   自身挂接锚点的位置   | "center" |

### 基于Demo扩展开发流程（新）

现在我们的自定义熔炉demo可以用于任何需要背包实现的容器，比如我们现在创建一个自定义箱子，没有其他逻辑，仅用于保存物品，其参考开发流程如下：

1. 创建一个自定义方块，并把其identifier添加到modConfig.py的CUSTOM_CONTAINER_LIST

2. 参考customFurnaceUI.json文件，修改其rightPanel下的控件以实现一个箱子的UI

3. 实现对应的UI控制器，需继承CustomContainerUIScreenBase类，可参考CustomFurnaceUIScreen.py，其中下列两个函数必须实现：

   1. `InitCustomContainerUI()`，用于初始化自定义容器的UI，需要把所有物品格子的信息保存至两个变量，存放该信息后会自动注册对应槽位的按键监听事件，物品格子的UI需继承自neteaseCommonUI中的itemBtn，可参考customFurnaceUI.json中furnaceSlot0的实现
      1. `self.mBagInfo`以字典形式存放所有物品格子的信息，其中key为`slotPath`也就是ui控件的路径，value有两个，一个是"slot"槽位名，约定背包槽位名用int，自定义熔炉的槽位名用str，**需严格遵守**；另一个是"itme"存放该物品格子中物品的itemDict。
      2. `self.mSlotToPath`以字典形式存放槽位名到ui控件的路径的映射，key为槽位名，value为ui控件的路径
   2. `UpdateCustomContainerUI()`，用于更新自定义容器中的UI，需结合对应的服务端事件实现

4. 实现对应的服务端系统，需继承CustomContainerServerSystem，可参考CustomFurnaceServerSystem.py，其中下列几点必须实现

   1. 在初始化函数中需初始化可以进行右键打开的容器列表，这里使用了modConfig中的CUSTOM_CONTAINER_LIST来进行初始化

      ```python
      self.mCustomContainer = modConfig.CUSTOM_CONTAINER_LIST
      ```

   2. `GetCustomContainerItems()`，该函数会在父类中调用，需要在这里实现从blockEntityData中获取自定义容器的所有物品的信息，返回一个dict，其中key为槽位名（上面第3点中有说约定为str），value为该槽位的物品信息也就是其itemDict

   3. `ResetCustomContainer(self, dimension, blockName, blockPos)`，该函数会在已放置的自定义容器被破坏时调用，需要处理一些重置操作，比如自定义熔炉需要在这个时候删除对应的熔炉管理器

   4. `UpdateCustomContainer()`，该函数会在右键打开自定义容器以及发生相关交换物品操作时调用，用于更新自定义容器除物品槽以外的其他状态信息，比如自定义熔炉通过该函数更新燃烧状态及燃烧动画，并通过modConfig.OnCustomContainerChangedEvent该事件通知客户端调用`UpdateCustomContainerUI()`去更新自定义容器的UI，传的参数可由开发者自定义

   5. `OnCustomContainerItemSwap()`，该函数会在自定义容器和背包之间发生物品交换的时候调用，之前的槽位名约定就是用于此处分辨是哪个容器的物品。需要在该函数中返回False表示禁止交换，如果返回True允许交换需要先调用`SpawnItemToPlayerInv()`或`SetInvItemNum()`更新对应背包槽位的物品，同时更新blockEntityData中的数据。如果有其他逻辑相关的比如自定义熔炉需要熔炉管理器来tick物品的生成与消耗，还需要在此函数中更新对应管理器的数据。

   6. `OnCustomContainerItemDrop()`，该函数会在丢弃自定义容器中的物品的时候触发，返回False表示禁止丢弃，返回True允许丢弃前需要先更新blockEntityData中的数据。如果有其他逻辑相关的比如自定义熔炉需要熔炉管理器来tick物品的生成与消耗，还需要在此函数中更新对应管理器的数据。

