# 国际版 - 物品组件列表

> 文档版本：2023.01.24

## 注意事项

1. 本文档内容来源于[我的世界基岩版国际版文档](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponentlist)，在此仅做翻译和补正，供各位开发者参考。
2. 本文档中少部分内容由于版本过高，尚无法在中国版中使用，请耐心等待中国版更新基岩版版本。
3. 本文档中绝大部分内容需要开启**假日创作者功能**实验性玩法才可以正常使用，请各位开发者注意辨别。欲了解更多关于实验性玩法的内容，请访问[《我的世界》基岩版中的实验功能](https://learn.microsoft.com/zh-cn/minecraft/creator/documents/experimentalfeaturestoggle)。
4. 本文档中一些组件虽然不存在于原文中，但是在实际应用中确实存在，故特为补充。注意，本文档中仅补充了在格式版本大于或等于1.16.100时存在的组件。

## 列表

| 组件原名                                                     | 组件译名           | 类型              | 描述                                                         |
| :----------------------------------------------------------- | :----------------- | :---------------- | :----------------------------------------------------------- |
| minecraft:allow_off_hand                                     | 允许副手           | 布尔值            | `minecraft:allow_off_hand`允许物品装备至副手。               |
| minecraft:animates_in_toolbar                                | 在工具栏中播放动画 | 布尔值            | `minecraft:animates_in_toolbar`允许物品具有动态纹理。        |
| [minecraft:armor](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_armor) | 盔甲               | JSON对象          | `minecraft:armor`定义了物品的护甲值。                        |
| [minecraft:block_placer](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_block_placer) | 方块放置器         | JSON对象          | `minecraft:block_placer`允许物品放置一个方块。               |
| minecraft:can_destroy_in_creative                            | 可在创造中摧毁     | 布尔值            | `minecraft:can_destroy_in_creative`决定了物品的是否可以在创造模式中摧毁方块。 |
| [minecraft:chargeable](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_chargeable) | 可蓄力             | JSON对象          | `minecraft:chargeable`允许物品在被使用时经历一段蓄力时间。   |
| [minecraft:cooldown](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_cooldown) | 冷却               | JSON对象          | `minecraft:cooldown`定义了物品在使用后的冷却时间。在冷却时间内，物品无法再次使用。 |
| minecraft:creative_category                                  | 创造分类           | 布尔值 / JSON对象 | `minecraft:creative_category`决定了物品添加至物品栏的分类和分组。 |
| minecraft:damage                                             | 伤害               | 整数              | `minecraft:damage`决定了物品的攻击伤害。                     |
| [minecraft:digger](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_digger) | 挖掘器             | JSON对象          | `minecraft:digger`允许物品具备额外的挖掘性质。               |
| [minecraft:display_name](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_display_name) | 显示名称           | JSON对象          | `minecraft:display_name`用于指定物品显示的名称。             |
| [minecraft:durability](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_durability) | 耐久               | JSON对象          | `minecraft:durability`定义了物品的耐久，即在物品损毁之前需要经历的损坏次数。 |
| [minecraft:dye_powder](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_dye_powder) | 染料粉             | JSON对象          | `minecraft:dye_powder`定义了物品可以作为染料粉使用，一共 16 种染料类型。 |
| minecraft:enchantable                                        | 可附魔             | 布尔值 / JSON对象 | `minecraft:enchantable`决定了物品的是否可附魔或可进行哪些魔咒的附魔。 |
| [minecraft:entity_placer](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_entity_placer) | 实体放置器         | JSON对象          | `minecraft:entity_placer`允许物品在一个方块表面或通过发射器放出一个实体，你可以指定该物品放出时所允许的方块类型。 |
| minecraft:explodable                                         | 可爆炸             | 布尔值            | `minecraft:explodable`决定了物品对应的物品实体是否可以被爆炸破坏。 |
| [minecraft:foil](https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_foil) | 箔晕               | 布尔值            | `minecraft:foil`决定了物品是否天生具有箔晕。通常，附魔的物品具有箔晕光效。 |
| [minecraft:food](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_food) | 食物               | JSON对象          | `minecraft:food`允许物品被玩家食用。                         |
| minecraft:frame_count                                        | 帧计数             | 整数              | `minecraft:frame_count`决定了物品动态纹理的帧序数。          |
| [minecraft:fuel](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_fuel) | 燃料               | JSON对象          | `minecraft:fuel`允许物品在熔炉中烧炼。                       |
| minecraft:hand_equipped                                      | 手持装备           | 布尔值            | `minecraft:hand_equipped`决定了物品是否是手持装备。是手持装备的物品渲染时采用左下-右上对角线，而非左上-右下对角线。 |
| minecraft:hover_text_color                                   | 悬停文本颜色       | 字符串            | `minecraft:hover_text_color`决定了鼠标悬停在物品图标上时显示的文本的颜色。 |
| [minecraft:icon](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_icon) | 图标               | JSON对象          | `minecraft:icon`用于指定物品在 UI 或其它某些地方所显示的图标。 |
| minecraft:ignores_permission                                 | 忽略权限           | 布尔值            | `minecraft:ignores_permission`决定了物品使用时是否忽略权限。 |
| [minecraft:knockback_resistance](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_knockback_resistance) | 击退抗性           | JSON对象          | `minecraft:knockback_resistance`定义了物品的击退抗性。       |
| minecraft:liquid_clipped                                     | 液体裁剪           | 布尔值            | `minecraft:liquid_clipped`决定了物品是否是液体裁剪的。是液体裁剪的物品可以与液体交互，且具有液体表面交互渲染效果。 |
| minecraft:max_stack_size                                     | 最大堆叠大小       | 整数              | `minecraft:max_stack_size`决定了物品的最大堆叠数目。         |
| minecraft:mining_speed                                       | 开采速度           | 整数              | `minecraft:mining_speed`决定了物品的开采速度。               |
| minecraft:mirrored_art                                       | 镜像艺术           | 布尔值            | `minecraft:mirrored_art`决定了物品的纹理是否镜像反转。       |
| [minecraft:on_use](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_on_use) | 当使用时           | JSON对象          | `minecraft:on_use`允许你在物品被使用时接收到一个事件。       |
| [minecraft:on_use_on](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_on_use_on) | 当使用于时         | JSON对象          | `minecraft:on_use_on`允许你在物品被使用于一个方块表面上时接收到一个事件。 |
| [minecraft:projectile](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_projectile) | 弹射物             | JSON对象          | `minecraft:projectile`允许物品发射一个弹射物。               |
| [minecraft:record](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_record) | 唱片               | JSON对象          | `minecraft:record`允许物品作为一个唱片可以被播放。           |
| [minecraft:render_offsets](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_render_offsets) | 渲染偏移量         | JSON对象          | `minecraft:render_offsets`定义了物品在客户端第一人称或第三人称状态下渲染时与玩家的偏移量。 |
| [minecraft:repairable](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_repairable) | 可修复             | JSON对象          | `minecraft:repairable`允许物品被修复并定义了物品可以被修复的量。 |
| minecraft:requires_interact                                  | 要求交互           | 布尔值            | `minecraft:requires_interact`决定了物品是否不需要实体就可以交互。 |
| [minecraft:shooter](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_shooter) | 发射器             | JSON对象          | `minecraft:shooter`允许物品发射实体。                        |
| minecraft:should_despawn                                     | 应毁除             | 布尔值            | `minecraft:should_despawn`决定了物品对应的物品实体是否应跟随物品实体毁除规则毁除。 |
| minecraft:stacked_by_data                                    | 按照数据值堆叠     | 布尔值            | `minecraft:stacked_by_data`决定了物品是否按照不同数据值分别堆叠。 |
| [minecraft:throwable](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_throwable) | 可投掷             | JSON对象          | `minecraft:throwable`允许物品作为可投掷的弹射物投掷。        |
| minecraft:use_animation                                      | 使用动画           | 字符串            | `minecraft:use_animation`决定了物品的使用动画。              |
| minecraft:use_duration                                       | 使用时长           | 小数              | `minecraft:use_duration`决定了物品使用时的时间长度。         |
| [minecraft:weapon](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_weapon) | 武器               | JSON对象          | `minecraft:weapon`允许物品作为一个武器，例如斧、剑、三叉戟、弓、弩等。 |
| [minecraft:wearable](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_wearable) | 可穿戴             | JSON对象          | `minecraft:wearable`允许物品被实体穿戴。                     |
| tag:[a-zA-Z0-9_.:-]+                                         | 标签               | 空JSON对象        | `tag:[a-zA-Z0-9_.:-]+`指定了物品标签，其中`[a-zA-Z0-9_.:-]+`表示物品标签应满足的正则表达式规则。 |
