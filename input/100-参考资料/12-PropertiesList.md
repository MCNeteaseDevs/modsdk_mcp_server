# 国际版 - 实体属性列表

> 文档版本：2022.04.21

## 注意事项

1. 本文档内容来源于[我的世界基岩版国际版文档](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/propertieslist)，在此仅做翻译和补正，供各位开发者参考。
2. 本文档中少部分内容由于版本过高，尚无法在中国版中使用，请耐心等待中国版更新基岩版版本。
3. 本文档中极少部分内容需要开启**假日创作者功能**实验性玩法才可以正常使用，请各位开发者注意辨别。欲了解更多关于实验性玩法的内容，请访问[《我的世界》基岩版中的实验功能](https://learn.microsoft.com/zh-cn/minecraft/creator/documents/experimentalfeaturestoggle)。

## 列表

| 属性原名                                                     | 属性译名           | 描述                                                         |
| :----------------------------------------------------------- | ------------------ | :----------------------------------------------------------- |
| [minecraft:ambient_sound_interval](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_ambient_sound_interval) | 环境声音间隔       | `minecraft:ambient_sound_interval`用于设置实体播放环境声音之间的间隔。 |
| [minecraft:can_climb](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_can_climb) | 能够攀爬           | `minecraft:can_climb`允许实体攀爬梯子。                      |
| [minecraft:can_fly](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_can_fly) | 能够飞行           | `minecraft:can_fly`允许实体具备飞行的能力，此时寻路器不会限制实体的路径下方的方块是固体方块。 |
| [minecraft:can_power_jump](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_can_power_jump) | 能够充能跳跃       | `minecraft:can_power_jump`允许实体像马那样充能跳跃。         |
| [minecraft:collision_box](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_collision_box) | 碰撞箱             | `minecraft:collision_box`用于设置实体碰撞箱的宽度和高度。    |
| [minecraft:color](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_color) | 颜色               | `minecraft:color`定义了实体的主要纹理颜色。                  |
| [minecraft:color2](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_color2) | 颜色2              | `minecraft:color2`定义了实体的次要纹理颜色。                 |
| [minecraft:default_look_angle](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_default_look_angle) | 默认看向角度       | `minecraft:default_look_angle`设置实体的默认头部旋转角度。   |
| [minecraft:equipment](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_equipment) | 装备               | `minecraft:equipment`设置该实体使用的装备表。                |
| [minecraft:fire_immune](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_fire_immune) | 火焰免疫           | `minecraft:fire_immune`允许实体在火中不受伤害。              |
| [minecraft:floats_in_liquid](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_floats_in_liquid) | 漂浮在液体中       | `minecraft:floats_in_liquid`允许实体具有在水中漂浮的能力。   |
| [minecraft:flying_speed](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_flying_speed) | 飞行速度           | `minecraft:flying_speed`设置实体飞行的速度，以方块为单位。   |
| [minecraft:friction_modifier](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_friction_modifier) | 摩擦修饰符         | `minecraft:friction_modifier`定义了摩擦对实体的影响幅度。    |
| [minecraft:ground_offset](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_ground_offset) | 地面偏移量         | `minecraft:ground_offset`设置实体的真实位置相对于地面的偏移量。 |
| [minecraft:input_ground_controlled](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_input_ground_controlled) | 输入地面控制       | `minecraft:input_ground_controlled`允许一个可骑乘的实体在被玩家骑乘时可以通过键盘控制来控制移动。 |
| [minecraft:is_baby](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_baby) | 是幼体             | `minecraft:is_baby`设置该实体为幼体。                        |
| [minecraft:is_charged](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_charged) | 是已蓄力的         | `minecraft:is_charged`设置该实体已蓄力。                     |
| [minecraft:is_chested](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_chested) | 是已安装箱子的     | `minecraft:is_chested`设置该实体当前身持箱子。               |
| [minecraft:is_dyeable](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_dyeable) | 是可染色的         | `minecraft:is_dyeable`允许实体与染料交互并改变其颜色。       |
| [minecraft:is_hidden_when_invisible](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_hidden_when_invisible) | 是在不可见时隐身的 | `minecraft:is_hidden_when_invisible`设置该实体在不可见时（即隐身状态效果下）可以从敌对生物眼中隐身。 |
| [minecraft:is_ignited](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_ignited) | 是已点燃的         | `minecraft:is_ignited`设置该实体当前正在着火。               |
| [minecraft:is_illager_captain](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_illager_captain) | 是灾厄村民队长     | `minecraft:is_illager_captain`设置该实体是一个灾厄村民队长。 |
| [minecraft:is_saddled](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_saddled) | 是已上鞍的         | `minecraft:is_saddled`设置该实体当前已上鞍。                 |
| [minecraft:is_shaking](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_shaking) | 是正在颤抖的       | `minecraft:is_shaking`设置该实体当前正在颤抖。               |
| [minecraft:is_sheared](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_sheared) | 是已修剪的         | `minecraft:is_sheared`设置该实体当前已修剪。                 |
| [minecraft:is_stackable](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_stackable) | 是可堆叠的         | `minecraft:is_stackable`设置该实体可以堆叠。                 |
| [minecraft:is_stunned](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_stunned) | 是已眩晕的         | `minecraft:is_stunned`设置该实体当前已眩晕。                 |
| [minecraft:is_tamed](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_is_tamed) | 是已驯服的         | `minecraft:is_tamed`设置该实体当前已驯服。                   |
| [minecraft:item_controllable](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_item_controllable) | 可物品控制         | `minecraft:item_controllable`允许实体在被骑乘时可以被物品控制。 |
| [minecraft:loot](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_loot) | 战利品             | `minecraft:loot`设置该实体死亡时掉落的物品的战利品表。       |
| [minecraft:mark_variant](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_mark_variant) | 标注变体           | `minecraft:mark_variant`设置该实体被使用的变体。             |
| [minecraft:push_through](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_push_through) | 推动               | `minecraft:push_through`设置该实体可以推动的距离。           |
| [minecraft:scale](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_scale) | 缩放               | `minecraft:scale`通过缩放模型大小来设置实体的视觉大小。      |
| [minecraft:skin_id](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_skin_id) | 皮肤ID             | `minecraft:skin_id`设置实体的皮肤ID值，可以被用到不同的皮肤上，例如村民的基皮肤。 |
| [minecraft:sound_volume](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_sound_volume) | 音量               | `minecraft:sound_volume`设置该实体声音效果的基音量。         |
| [minecraft:type_family](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_type_family) | 类型族             | `minecraft:type_family`定义实体属于的族。                    |
| [minecraft:variant](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_variant) | 变体               | `minecraft:variant`用于区分一个实体中不同变体的组件组，例如豹猫、村民和马。 |
| [minecraft:walk_animation_speed](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_walk_animation_speed) | 行走动画速度       | `minecraft:walk_animation_speed`设置该实体行走动画速度的速度乘子。 |
| [minecraft:wants_jockey](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_wants_jockey) | 期望成为骑士       | `minecraft:wants_jockey`设置该实体期望成为一个骑士。         |
