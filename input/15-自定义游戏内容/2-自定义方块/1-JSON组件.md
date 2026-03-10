---
front: 
hard: 入门
time: 分钟
---

# JSON组件

## format_version

基岩版自定义方块的json结构曾经过多次调整，当填写format_version时，需要按照对应版本的json结构编写components。

例如`minecraft:destroy_time`，在1.10.0中为

```json
"minecraft:destroy_time": {
    "value": 4.0
}
```

而在1.16.0的版本中为

```json
"minecraft:destroy_time": 4.0
```

而在1.19.20以上的版本中为

```json
"minecraft:destructible_by_mining": {
    "seconds_to_destroy": 4.0
}
```

## description

| 键                      | 类型 | 默认值 | 解释                                                         |
| ----------------------- | ---- | ------ | ------------------------------------------------------------ |
| identifier              | str  |        | 包括命名空间及物品名。需要全局唯一。建议使用mod名称作为命名空间 |
| register_to_create_menu | bool | false  | 是否注册到创造栏                                             |
| category                | str  | Nature | 注册到创造栏的分类，可选的值有：<br/>Construction<br/>Nature<br/>Equipment<br/>Items |

## components

目前行为包中自定义方块json中支持的component包括原版component和网易独有的component。minecraft开头的为原版component，netease开头的为网易独有component。

对于原版component，你可以在上方的format_version解释中找到更多的参数及解释。

<span id="minecraft_loot"></span>

### minecraft:loot

可用于使用loot table控制掉落物

可参考[CustomBlocksMod](../../13-模组SDK编程/60-Demo示例.md#CustomBlocksMod)的customblocks:customblocks_test_ore方块

<span id="minecraft_friction"></span>

### minecraft:friction

可用于设置方块的摩擦力，取值范围为(0.0-0.9)。`注意此摩擦力和原版方块的摩擦力不是同一个摩擦力`

<span id="minecraft_max_stack_size"></span>

### minecraft:max_stack_size

可用于设置方块物品最大堆叠数量，`注意：该值不能超过64`

<span id="minecraft_destroy_time"></span>

### minecraft:destroy_time

可用于控制挖掘所需的时间。该值的含义与[官方wiki](https://minecraft-zh.gamepedia.com/%E6%8C%96%E6%8E%98#.E6.96.B9.E5.9D.97.E7.A1.AC.E5.BA.A6)的“硬度”一致

主要用于[挖掘](./2-功能.md#wajue)的功能

<span id="minecraft_destructible_by_mining"></span>

### minecraft:destructible_by_mining

可用于控制挖掘所需的时间。该值的含义与[官方wiki](https://minecraft-zh.gamepedia.com/%E6%8C%96%E6%8E%98#.E6.96.B9.E5.9D.97.E7.A1.AC.E5.BA.A6)的“硬度”一致

- 如果设置为 `true`，方块会采用默认的破坏时间。
- 如果设置为 `false`，方块将不可被挖掘破坏。
- 如果省略该组件，则方块同样会使用默认的破坏时间。
- 如果类型为object，则是以下参数：

| 键                 | 类型| 默认值 | 解释|
|------------------|--------|----------------|-------------|
| seconds_to_destroy| 浮点数| `0.0`         |设置方块的硬度，实际破坏时间 = 1.5 × seconds_to_destroy。 |

此组件需要在`format_version`大于等于1.19.20的方块行为中代替[minecraft:destroy_time](./1-JSON组件.md###minecraft:destroy_time)使用。

主要用于[挖掘](./2-功能.md#wajue)的功能

<span id="minecraft_block_light_emission"></span>

### minecraft:block_light_emission

可用于设置方块亮度，取值范围为[0, 1]。关于亮度及方块光源可参考[官方wiki](https://minecraft-zh.gamepedia.com/%E4%BA%AE%E5%BA%A6)

主要用于[亮度](./2-功能.md#liangdu)的功能

<span id="minecraft_light_emission"></span>

### minecraft:light_emission

可用于设置方块亮度, 取值范围为[0, 15]。此组件需要在`format_version`大于等于1.19.20的方块行为中代替
[minecraft:block_light_emission](./1-JSON组件.md###minecraft:block_light_emission)使用。
关于亮度及方块光源可参考[官方wiki](https://minecraft-zh.gamepedia.com/%E4%BA%AE%E5%BA%A6)

主要用于[亮度](./2-功能.md#liangdu)的功能

<span id="minecraft_explosion_resistance"></span>

### minecraft:explosion_resistance

可用于设置爆炸抗性。原版方块的爆炸抗性见[官方wiki](https://minecraft-zh.gamepedia.com/%E7%88%86%E7%82%B8#.E7.88.86.E7.82.B8.E6.8A.97.E6.80.A7)

<span id="minecraft_destructible_by_explosion"></span>

### minecraft:destructible_by_explosion

可用于控制挖掘所需的时间。该值的含义与[官方wiki](https://minecraft-zh.gamepedia.com/%E6%8C%96%E6%8E%98#.E6.96.B9.E5.9D.97.E7.A1.AC.E5.BA.A6)的“硬度”一致

- 如果设置为 `true`，方块会采用默认的爆炸抗性。
- 如果设置为 `false`，方块将不可被爆炸破坏。
- 如果省略该组件，则方块同样会使用默认的爆炸抗性。
- 如果类型为object，则是以下参数：

| 键                 | 类型| 默认值 | 解释|
|------------------|--------|----------------|-------------|
| explosion_resistance| 浮点数| `0.0`         |设置方块的爆炸抗性，实际爆炸抗性 = 5 × explosion_resistance。 |

此组件需要在`format_version`大于等于1.19.20的方块行为中代替[minecraft:explosion_resistance](./1-JSON组件.md###minecraft:explosion_resistance)使用。

原版方块的爆炸抗性见[官方wiki](https://minecraft-zh.gamepedia.com/%E7%88%86%E7%82%B8#.E7.88.86.E7.82.B8.E6.8A.97.E6.80.A7)


<span id="minecraft_block_light_absorption"></span>

### minecraft:block_light_absorption

可用于设置方块的透光率。具体可参考[官方wiki](https://minecraft-zh.gamepedia.com/%E4%BA%AE%E5%BA%A6#.E9.98.BB.E7.A2.8D.E5.85.89.E7.85.A7.E7.9A.84.E6.96.B9.E5.9D.97)

默认为不透光。

主要用于[亮度](./2-功能.md#liangdu)的功能

<span id="minecraft_light_dampening"></span>

### minecraft:light_dampening

可用于设置方块吸光程度, 取值范围为[0, 15]。此组件需要在  `format_version`大于等于1.19.20的方块行为中代替[minecraft:block_light_absorption](./1-JSON组件.md###minecraft:block_light_absorption)使用。
关于亮度及方块光源可参考[官方wiki](https://minecraft-zh.gamepedia.com/%E4%BA%AE%E5%BA%A6)

主要用于[亮度](./2-功能.md#liangdu)的功能

<span id="minecraft_map_color"></span>

### minecraft:map_color

可用于设置方块显示在地图上的颜色

<span id="minecraft_display_name"></span>

### minecraft:display_name

指定语言文件键，用于映射鼠标悬停在物品栏和快捷栏中的方块物品上时显示的文本。如果给定的字符串无法解析为本地字符串，则将显示给定的原始字符串。使用需要方块行为的 `format_version`大于等于1.19.60。

<span id="netease_tier"></span>

### netease:tier

用于设置与挖掘相关的属性

主要用于[挖掘](./2-功能.md#wajue)的功能

|       键       |  类型  | 默认值 | 解释                                                                                                                                                                                                                                               |
| :-------------: | :----: | :----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     digger     | string |        | 必须设置。表示方块使用此工具挖掘时有速度加成。<br/>可选的值有：    <br/>shovel：铲    <br/>pickaxe：镐    <br/>hatchet：斧    <br/>hoe：锄                                                                                     |
| destroy_special |  bool  | false | 可选。当设置为true时，表示只有使用digger设置的工具进行挖掘才会产生掉落物。                                                                                                                                                                     |
|      level      |  int  |   0   | 可选。当destroy_special为true时才会生效。表示挖掘所需的工具等级，若手持工具等级小于该值，则不会产生掉落物。<br/>原版工具的等级：   <br/>空手/其他非工具物品：0<br/>木制/金制工具：0<br/>石制工具：1  <br/>铁制工具：2 <br/>钻石工具：3 |

<span id="netease_aabb"></span>

### netease:aabb

用于设置方块的碰撞盒

**注意事项：**

1. 无碰撞箱的方块请将collision的每个项都设置为0
2. 有碰撞箱的方块，clip的范围需要小于或等于collision的范围，否则弹射物命中时会异常
3. aabb的min不要小于[-1, -1, -1]，max不要大于[2, 2, 2]

可参考[CustomBlocksMod](../../13-模组SDK编程/60-Demo示例.md#CustomBlocksMod)的customblocks_model_flower及customblocks_model_wire方块。

| 键        | 类型          | 默认值 | 解释                                                                                                           |
| --------- | ------------- | ------ | -------------------------------------------------------------------------------------------------------------- |
| collision | object或array |        | 计算与物体碰撞时用的碰撞盒                                                                                     |
| clip      | object或array |        | 计算射线检测时用的碰撞盒。如准心选取及弹射物碰撞。（那么当该AABB没有体积时，准心与弹射物都会无视这个方块） |

当collision或clip为object时，用于表示恒定大小的单一碰撞盒，结构为：

| 键  | 类型         | 默认值    | 解释                               |
| --- | ------------ | --------- | ---------------------------------- |
| min | array(float) | [0, 0, 0] | min的三个值必须小于等于max的三个值 |
| max | array(float) | [1, 1, 1] |                                    |

当collision或clip为array时，用于可变化的多个碰撞盒的组合，通常用于可变化的自定义方块模型。元素的结构为：

|        | 类型         | 默认值    | 解释                                                                                             |
| ------ | ------------ | --------- | ------------------------------------------------------------------------------------------------ |
| enable | molang       | true      | 控制是否开启该碰撞箱目前仅支持is_connect查询，详见[netease:connection](#netease_connection) |
| min    | array(float) | [0, 0, 0] | min的三个值必须小于等于max的三个值                                                               |
| max    | array(float) | [1, 1, 1] |                                                                                                  |

<span id="netease_face_directional"></span>

### netease:face_directional

用于设置方块的多面向

主要用于[多面向](./2-功能.md#duomianxiang)的功能

| 键   | 类型   | 默认值 | 解释                                                  |
| ---- | ------ | ------ | ----------------------------------------------------- |
| type | string |        | direction：四面向方块facing_direction：六面向方块 |

<span id="netease:fuel "></span>

### netease:fuel

可燃类物品组件。允许该方块物品作为燃料在熔炉中燃烧

| 键       | 类型  | 默认值 | 解释                                      |
| -------- | ----- | ------ | ----------------------------------------- |
| duration | float | 0      | 可填， 该物品可提供的熔炉燃烧时长（秒）。 |

<span id="netease_render_layer"></span>

### netease:render_layer

用于设置方块渲染时使用的材质

可参考[CustomBlocksMod](../../13-模组SDK编程/60-Demo示例.md#CustomBlocksMod)的customblocks:customblocks_model_flower方块。

| 键    | 类型   | 默认值 | 解释                                                         |
| ----- | ------ | ------ | ------------------------------------------------------------ |
| value | string |        | 目前支持的材质有：<br>opaque：不透明，即“terrain_opaque”材质。默认为此项<br/>alpha：全透明，即“terrain_alpha”材质，如火焰，该材质用于异形方块，用在方块类上但与其他方块重合时会出现闪烁，可以使用no_crop_face_block组件避免闪烁。<br/>blend：半透明，即“terrain_blend”材质，如彩色玻璃。<br/>optionalAlpha：局部透明，与alpha不同，alpha超过一定距离将不渲染，而optionalAlpha不会，能配合no_crop_face_block组件实现原版叶子效果。 |

<span id="netease_solid"></span>

### netease:solid

用于设置方块是否为实心方块主要与生物在方块内时是否受到窒息伤害有关。

使用了这个组件，自定义方块将不会产生阴影。

可参考[CustomBlocksMod](../../13-模组SDK编程/60-Demo示例.md#CustomBlocksMod)的customblocks:customblocks_model_flower方块。

| 键    | 类型 | 默认值 | 解释                                                                            |
| ----- | ---- | ------ | ------------------------------------------------------------------------------- |
| value | bool | true   | 为true时，生物在方块内会受到窒息伤害为false时，生物在方块内不会受到窒息伤害 |

<span id="netease_pathable"></span>

### netease:pathable

用于设置游戏内AI在进行寻路时，方块是否被当作障碍物。

可参考[CustomBlocksMod](../../13-模组SDK编程/60-Demo示例.md#CustomBlocksMod)的customblocks:customblocks_model_flower方块。

| 键    | 类型 | 默认值 | 解释                                                                            |
| ----- | ---- | ------ | ------------------------------------------------------------------------------- |
| value | bool | false  | 为true时，寻路时被当作空气为false时，寻路时被当作障碍物，并且可在其上方行走 |

<span id="netease_block_entity"></span>

### netease:block_entity

用于给自定义方块添加[自定义方块实体](./4-自定义方块实体.md)。

可参考[CustomBlocksMod](../../13-模组SDK编程/60-Demo示例.md#CustomBlocksMod)的customblocks:customblocks_test_block_entity方块。

| 键          | 类型 | 默认值 | 解释                                                         |
| ----------- | ---- | ------ | ------------------------------------------------------------ |
| tick        | bool | false  | 为true时，当玩家进入方块tick范围时，该方块每秒会发送**20次**ServerBlockEntityTickEvent事件<br/>为false时，该方块不会发送ServerBlockEntityTickEvent事件 |
| client_tick | bool | false  | 为true时，当玩家进入方块tick范围时，该方块每秒会发送**20次**ModBlockEntityTickClientEvent事件<br/>为false时，该方块不会发送ModBlockEntityTickClientEvent事件 |
| movable     | bool | true   | 为true时，该方块可被粘性活塞拉回为false时，该方块不可被粘性活塞拉回 |

<span id="netease_random_tick"></span>

### netease:random_tick

用于给自定义方块定义是否可以随机tick，并且设置该tick事件是否发送到脚本层。

| 键             | 类型 | 默认值 | 解释                                                                                                                                                     |
| -------------- | ---- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enable         | bool | false  | 方块是否随机tick                                                                                                                                         |
| tick_to_script | bool | false  | 是否发送事件 BlockRandomTickServerEvent 到python脚本 |

### netease:block_animate_random_tick

频率更高的方块tick，用于实现类似樱花树叶的方块特效。给自定义方块配置该组件后，开发者可以在**客户端**监听<a href="../../../../mcdocs/1-ModAPI/事件/方块.html#blockanimaterandomtickevent" rel="noopenner"> BlockAnimateRandomTickEvent </a>事件给方块附加逻辑。

| 键           | 类型  | 默认值 | 解释   |
| ------------ | ----- | ------ | ------ |
| trigger_rate | float | 0.1    | 触发率 |
| send_event | bool | true    | 触发BlockAnimateRandomTickEvent事件 |

该组件采用了和原版樱花树叶/末地烛相同的逻辑，支持无需方块实体即可tick，且性能开销低。不建议在事件里将数据传给服务端，因为每个玩家客户端tick到的方块都是随机的，可能相同也可能不同。

**方块离玩家越近，触发频率越大**，当方块距离玩家16个方块以内时，如果设置trigger_rate为1，几乎每秒都能触发，原版樱花树叶的触发率为0.1，约等于总是10%的概率触发落叶。随着方块离玩家越远，触发几率也会递减。最大触发距离为32-40格，32是玩家静止不动时的值，玩家移动时，最多可能有8个方块距离的偏移。

**设备性能越好，触发频率越大**，游戏引擎会记录帧耗时，超时的tick不会触发Python事件，避免大量方块同时tick导致卡顿。


### netease:redstone_property

用于给自定义方块设置红石属性

| 键    | 类型 | 默认值 | 解释                                                                                            |
| ----- | ---- | ------ | ----------------------------------------------------------------------------------------------- |
| value | str  | None   | 目前只支持break_on_push，设置之后，方块可以被活塞破坏变成掉落物，否则，方块会被活塞推动而不破坏 |

### netease:neighborchanged_sendto_script

| 键    | 类型 | 默认值 | 解释                                                                                                                                                                                                           |
| ----- | ---- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value | bool | false  | 方块周围环境变化是否发送事件 BlockNeighborChangedServerEvent 到脚本层 |

<span id="netease_connection"></span>

### netease:connection

用于给自定义方块定义“连接”属性

使用枚举的方式配置该方块与哪些方块具有“连接”属性，并且此属性是单向的。不支持附加值。

由于方块更新的特性，“床”和“旗帜”方块在区块边缘放置时，与其他方块会出现连接失败。

可参考[CustomBlocksMod](../../13-模组SDK编程/60-Demo示例.md#CustomBlocksMod)的customblocks_model_wire方块。

| 键     | 类型          | 解释                       |
| ------ | ------------- | -------------------------- |
| blocks | array(string) | 数组元素为方块的identifier |

目前该属性只用于[netease:aabb](#netease_aabb)及[自定义方块模型](./5-自定义方块模型.md)的is_connect查询：

| 名称             | 解释                                                         |
| ---------------- | ------------------------------------------------------------ |
| query.is_connect | 传入一个参数，返回该方块与对应临面上的方块是否有connection属性参数取值与对应的面：<br/>0-down面，<br/>1-up面，<br/>2-north面，<br/>3-south面，<br/>4-west面，<br/>5-east面。 |

<span id="netease_redstone"></span>

### netease:redstone

用于配置自定义红石源与自定义红石机械元件；

可以配置自定义红石的类型，如红石源或者红石机械元件；

可以配置初始信号强度，默认为15。

| 键       | 类型 | 默认值 | 说明                                                       |
| -------- | ---- | ------ | ---------------------------------------------------------- |
| type     | str  |        | 红石类型：<br/>producer：红石源<br/>consumer：红石机械元件 |
| strength | int  | 15     | 红石信号值，范围[0,15]                                     |

<span id="listen_block_remove"></span>

### netease:listen_block_remove

用于配置自定义方块是否监听方块的<a href="../../../../mcdocs/1-ModAPI/事件/方块.html#blockremoveserverevent" rel="noopenner"> BlockRemoveServerEvent </a>事件

| 键    | 类型 | 默认值 | 说明         |
| ----- | ---- | ------ | ------------ |
| value | bool | false  | 是否监听事件 |

<span id="netease_may_place_on"></span>

### netease:may_place_on

用于配置自定义方块可存在于哪些方块的上面。

会生效于玩家右键放置方块时；以及已存在的方块下方的方块发生改变时。

可参考CustomBlocksMod示例中的customblocks_model_flower

| 键              | 类型         | 默认值 | 说明                                                                                                                                                                                                                       |
| --------------- | ------------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| block           | list(str)    |        | 方块identifier的列表。这些方块的所有[方块状态](../../10-基本概念/1-我的世界基础概念.md#方块状态)都可放置                                                                                                                   |
| block_state     | list(object) |        | [方块状态](../../10-基本概念/1-我的世界基础概念.md#方块状态)的列表。每个元素只对应一个特定的方块状态，如果方块有多个种类的状态，需要考虑排列组合的所有情况最终可在上面放置的方块是block字段与block_state字段的并集 |
| spawn_resources | bool         | true   | 已存在的方块因下方的方块发生改变而被破坏时，是否生成掉落物                                                                                                                                                                 |

<span id="netease_fire_resistant"></span>

### netease:fire_resistant

用于配置自定义方块是否防火。

设置为防火时，方块的掉落物会与下界合金一样，不会被火烧毁，掉进岩浆时会弹走。

可参考CustomBlocksMod示例中的customblocks_test_ore

| 键    | 类型 | 默认值 | 说明     |
| ----- | ---- | ------ | -------- |
| value | bool |        | 是否防火 |

### netease:block_properties

用于配置自定义方块的方块属性

这些方块属性可以叠加，主要用于引擎对一些方块特性逻辑的判断

可参考CustomBlocksMod示例中的customblocks_slime、customblocks_flower_extend

| 键         | 类型  | 默认值 | 说明           |
| ---------- | ----- | ------ | -------------- |
| properties | array |        | 所有属性字符串 |

其中properties数组目前支持以下字符串填充

| 键                             | 说明                                                     |
| ------------------------------ | -------------------------------------------------------- |
| piston_block_grabber           | 被活塞推动时是否带动旁边方块                             |
| slime                          | 主要用于变为移动方块（例如被活塞推）时修改对实体力的计算 |
| breaks_when_fallen_on_by_heavy | 当重力方块结束下落在该方块位置后，自身是否被毁坏         |

如果方块碰撞盒体积使用netease:aabb或minecraft:entity_collision改小可能会导致无法触发（目前可参考范围是边长0.4以下不会触发）。

### netease:on_stand_on

用于触发实体站在方块上的事件

可参考CustomBlocksMod示例中的customblocks_slime，利用了该事件组合做出了个模拟原版粘液块的效果。

| 键                | 类型 | 默认值 | 说明                 |
| ----------------- | ---- | ------ | -------------------- |
| send_python_event | bool |        | 是否发送事件至python |

当send_python_event为true时，该方块会触发OnStandOnBlockClientEvent、OnStandOnBlockServerEvent事件。

如果方块碰撞盒体积使用netease:aabb或minecraft:entity_collision改小可能会导致无法触发（目前可参考范围是边长0.4以下不会触发）。

### netease:on_before_fall_on

用于触发实体刚下落至方块的事件，主要用于伤害计算

可参考CustomBlocksMod示例中的customblocks_slime，利用了该事件组合做出了个模拟原版粘液块的效果。

如果方块碰撞盒体积使用netease:aabb或minecraft:entity_collision改小可能会导致无法触发（目前可参考范围是边长0.4以下不会触发）。

### netease:on_after_fall_on

用于触发实体下落至方块后的事件，主要用于力的计算

可参考CustomBlocksMod示例中的customblocks_slime，利用了该事件组合做出了个模拟原版粘液块的效果。

如果方块碰撞盒体积使用netease:aabb或minecraft:entity_collision改小可能会导致无法触发（目前可参考范围是边长0.4以下不会触发）。

### netease:on_entity_inside

用于触发实体碰撞盒所在位置有方块时的事件（判断位置逻辑有无方块，与方块碰撞盒大小无关）。

当send_python_event为true时，该方块会触发OnEntityInsideBlockClientEvent、OnEntityInsideBlockServerEvent事件。

### netease:on_step_on

用于触发实体刚移动至一个实心方块上的事件

可参考CustomBlocksMod示例中的customblocks_slime，在触发该事件时进行了日志打印

### netease:on_step_off

用于触发实体刚离开一个实心方块上的事件

可参考CustomBlocksMod示例中的customblocks_slime，在触发该事件时进行了日志打印

<span id="netease_offset"></span>

### netease:block_random_offset

用于设置方块的偏移，能实现原版花朵的偏移效果。

注意：制作可偏移方块时，请尽量配套使用方块模型，当使用贴图方块随机偏移时，若相邻方块是不透明方块，则该方块对应的面会被裁切渲染！！普通贴图方块的物品栏渲染也可能会有异常！！

该组件会把方块的材质设置为透明，且不可与netease:render_layer的不透明材质一起共用，否则会出现渲染错误

| 键      | 类型          | 默认值 | 解释                                                                           |
| ------- | ------------- | ------ | ------------------------------------------------------------------------------ |
| x_scope | [float,float] | [0,0]  | x轴方向的偏移范围，size为2的array，取值范围为0.0~1.0，如果两个值相同则为指定点 |
| z_scope | [float,float] | [0,0]  | z轴方向的偏移范围，size为2的array，取值范围为0.0~1.0，如果两个值相同则为指定点 |

<span id="block_chest"></span>

### netease:block_chest

用于给方块添加箱子功能，使用了该组件会创建一个block_entity方块，会与其他block_entity逻辑有冲突，请谨慎使用。

该组件会覆盖带有base_block及其相关组件的功能。

使用了这个组件后请勿再配置netease:face_directional。

使用SetBlockNew接口创建自定义箱子的时候，需要先调用一次SetBlockNew将目标位置方块设置为Air，再使用AddTimer延后调用SetBlockNew创建自定义箱子

| 键                 | 类型 | 默认值 | 解释                                                                                       |
| ------------------ | ---- | ------ | ------------------------------------------------------------------------------------------ |
| custom_description | str  |        | 箱子UI上面显示的箱子名称，不填为空                                                         |
| chest_capacity     | int  |        | 必填，箱子的容量行数，取值范围1-8，如果can_pair取值为true且该值大于4，将自动变为4          |
| can_pair           | bool | false  | 是否可以与隔壁箱子组合，合成一个大箱子                                                     |
| is_shulker_box     | bool | false  | 是否为潜影盒箱子，如果开启摧毁方块将不会掉落，与原版潜影盒功能相同，无法与隔壁箱子进行组合 |
| mute               | bool | true   | 是否关闭箱子开启与关闭时的音效                                                             |
| can_be_blocked     | bool | false  | 是否能被阻挡，即箱子上面有阻挡的方块时能否打开箱子                                         |
<span id="block_container"></span>

### netease:block_container

[自定义容器](./3-特殊方块/11-自定义容器.md)组件，使用时需要将base_block设为netease_container。相比[netease:block_chest](#netease-block-chest)，该组件支持使用资源包UI Json配置方块打开后的UI界面，方便开发者制作自定义熔炉等界面，而无需考虑复杂的交互逻辑，数据同步逻辑等。

| 键                 | 类型 | 默认值 | 解释                                       |
| ------------------ | ---- | ----- | ------------------------------------------ |
| custom_description | str  |       | 容器ui打开时的title（复用原版ui时生效）       |
| screen_name        | str  |       | 交互方块时打开的ui，形如namespace.screenName |
| container_size     | int  |       | 方块容器能够存放的物品槽位数量，取值范围1-108，需与ui槽位匹配。若ui槽位大于配置容量，超过配置的部分无法放入物品；若ui槽位小于配置容量，按shift可放入，但无法在ui中显示 |

<span id="no_crop_face_block"></span>

### netease:no_crop_face_block

该组件能实现当两个方块相邻时，相邻面渲染其中一个方块的一面，与原版2个叶子方块相邻效果一致，不会把相邻面都裁剪掉

为了避免相邻面变黑需要在配置中新增minecraft:block_light_absorption组件并将值设置为0。

需要配合netease:render_layer使用，使用 optionalAlpha 能实现原版的叶子方块效果，使用 alpha 超过一定距离后方块将不渲染。

该组件无参数，直接在JSON按下面格式写即可调用：

```json
"components": {
   "netease:no_crop_face_block":{}
 }
```

<span id="custom_tips"></span>

### netease:custom_tips

该组件用于自定义方块Item的物品信息描述，与自定义物品中的 netease:customtips 作用相同

| 键    | 类型 | 默认值   | 解释           |
| ----- | ---- | -------- | -------------- |
| value | str  | 物品名称 | 物品的描述信息 |
