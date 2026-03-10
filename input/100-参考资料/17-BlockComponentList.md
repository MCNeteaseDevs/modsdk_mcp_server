# 国际版 - 方块组件列表

> 文档版本：2022.10.26

## 注意事项

1. 本文档内容来源于[我的世界基岩版国际版文档](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/blockcomponentslist)，在此仅做翻译和补正，供各位开发者参考。
2. 本文档中少部分内容由于版本过高，尚无法在中国版中使用，请耐心等待中国版更新基岩版版本。
3. 本文档中大部分内容需要开启**假日创作者功能**或**即将到来的创作者功能**实验性玩法才可以正常使用，请各位开发者注意辨别。欲了解更多关于实验性玩法的内容，请访问[《我的世界》基岩版中的实验功能](https://learn.microsoft.com/zh-cn/minecraft/creator/documents/experimentalfeaturestoggle)。
4. 本文档中关于方块标签的描述虽然不存在于原文中，但是在实际应用中确实存在，故特为补充。

## 列表

| 组件原名                                                     | 组件译名     | 类型              | 描述                                                         |
| :----------------------------------------------------------- | :----------- | :---------------- | :----------------------------------------------------------- |
| [minecraft:collision_box](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_collision_box) | 碰撞箱       | 布尔值 / JSON对象 | `minecraft:collision_box`决定了方块与实体碰撞用的区域。如果设置为`true`，会自动应用默认值，如果设置为`false`，方块与实体的碰撞将被禁用。如果该组件在编写时被忽略，依旧会应用默认值。 |
| [minecraft:crafting_table](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_crafting_table) | 工作台       | JSON对象          | `minecraft:crafting_table`允许该方块成为一个可以启用工作台UI并具备合成功能的工作台。 |
| [minecraft:destructible_by_explosion](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_destructible_by_explosion) | 可被爆炸摧毁 | 布尔值 / JSON对象 | `minecraft:destructible_by_explosion`决定了方块的爆炸性质中的可摧毁性。如果设置为`true`，方块将具备默认的爆炸抗性，如果设置为`false`，方块将不可被爆炸摧毁。如果该组件在编写时被忽略，方块依旧会拥有默认的爆炸抗性。 |
| [minecraft:destructible_by_mining](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_destructible_by_mining) | 可被开采摧毁 | 布尔值 / JSON对象 | `minecraft:destructible_by_mining`决定了方块的开采性质中的可摧毁性。如果设置为`true`，方块将具备默认的摧毁时间数，如果设置为`false`，方块将不可被开采摧毁。如果该组件在编写时被忽略，方块依旧会拥有默认的摧毁时间数。 |
| [minecraft:display_name](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_display_name) | 显示名称     | 本地化字符串      | `minecraft:display_name`指定了当指针悬停在物品栏或快捷栏中方块上方时显示的文本对应的语言文件键名。如果给定的字符串无法被解析成本地化字符串，则将直接应用原始文本作为显示文本。如果该组件在编写时被忽略，方块的名称本身将被用于显示名称。 |
| [minecraft:flammable](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_flammable) | 可燃         | 布尔值 / JSON对象 | `minecraft:flammable`决定了方块的可燃性质。如果设置为`true`，将应用默认值，如果设置为`false`或在编写时被忽略，方块将不能自然地从毗邻传播着火，不过依旧能够被直接点燃。 |
| [minecraft:friction](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_friction) | 摩擦         | 小数              | `minecraft:friction`决定了方块的摩擦，范围取自`(0.0, 0.9)`。摩擦影响实体在方块上行进时的移动速度。越大的值会导致越大的摩擦。 |
| [minecraft:geometry](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_geometry) | 几何         | 标识符字符串      | `minecraft:geometry`指定用于渲染方块的几何的描述标识符。标识符必须与任意一个当前已加载的资源包中现有的几何标识符相匹配。 |
| [minecraft:light_dampening](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_light_dampening) | 光线隔除     | 整数              | `minecraft:light_dampening`决定了当光线通过方块时被隔除的量，范围为`(0, 15)`。越高的值意味着光线被隔除得越多。 |
| [minecraft:light_emission](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_light_emission) | 光线发射     | 整数              | `minecraft:light_emission`决定了方块将会发射的光线的量，范围为`(0, 15)`。越高的值将意味着发射越多的光线。 |
| [minecraft:loot](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_loot) | 战利品       | 路径字符串        | `minecraft:loot`决定了方块破坏时略取的战利品表，填入战利品表相对于行为包根目录的路径。 |
| [minecraft:map_color](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_map_color) | 地图颜色     | 字符串            | `minecraft:map_color`决定了方块渲染至地图时的颜色。颜色以`#RRGGBB`的16进制格式表示，也可以以`[R, G, B]`的数组形式表示。如果该组件在编写时被忽略，方块将不会显示在地图上。 |
| [minecraft:material_instances](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_material_instances) | 材质实例     | JSON对象          | `minecraft:material_instances`决定了方块的材质实例，将一个面或者材质实例名映射到真实的材质实例上。你可以将一个材质实例对象赋值给这些面中的任意一面：`up`、`down`、`north`、`south`、`east`、`west`或`*`，你也可以将一个你选择的名称给予该实例，例如`my_instance`，并在之后将其赋给一个面，例如`"north":"my_instance"`。 |
| [minecraft:part_visibility](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_part_visibility) | 部件可见     | 布尔值            | `minecraft:part_visibility`将几何文件中的骨骼名映射到一个可以开关渲染的条件上。条件需要是一个使用方块属性来决定`true`或`false`的Molang查询。 |
| [minecraft:placement_filter](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_placement_filter) | 放置过滤器   | JSON对象          | `minecraft:placement_filter`决定了方块在什么条件下可以被放置或存活。 |
| [minecraft:rotation](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_rotation) | 旋转         | 向量 [a, b, c]    | `minecraft:rotation`决定了方块围绕立方体中心的旋转角度。旋转顺序是`[x, y, z]`，角度必须是90的倍数。 |
| [minecraft:selection_box](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_selection_box) | 选择箱       | 布尔值 / JSON对象 | `minecraft:selection_box`决定了方块可以被玩家的指针选中的区域。如果设置为`true`，会自动应用默认值，如果设置为`false`，方块将无法被玩家选中。如果该组件在编写时被忽略，依旧会应用默认值。 |
| [minecraft:unit_cube](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockcomponents/minecraftblock_unit_cube) | 单位立方体   | JSON对象          | `minecraft:unit_cube`指定方块在镶嵌（或被称作曲面细分）时使用一个单位立方体。 |
| tag:[a-zA-Z0-9_.:-]+                                         | 标签         | 空JSON对象        | `tag:[a-zA-Z0-9_.:-]+`指定了方块标签，其中`[a-zA-Z0-9_.:-]+`表示方块标签应满足的正则表达式规则。标签可以用在基组件或置换中任意的位置，用于配方中或其余接受方块作为参数的组件中查询。 |
