# 国际版 - 过滤器列表

> 文档版本：2022.06.08

## 注意事项

1. 本文档内容来源于[我的世界基岩版国际版文档](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filterlist)，在此仅做翻译和补正，供各位开发者参考。
2. 本文档中少部分内容由于版本过高，尚无法在中国版中使用，请耐心等待中国版更新基岩版版本。
3. 本文档中极少部分内容需要开启**假日创作者功能**实验性玩法才可以正常使用，请各位开发者注意辨别。欲了解更多关于实验性玩法的内容，请访问[《我的世界》基岩版中的实验功能](https://learn.microsoft.com/zh-cn/minecraft/creator/documents/experimentalfeaturestoggle)。

## 列表

| 过滤器原名                                                   | 过滤器译名       | 描述                                                         |
| :----------------------------------------------------------- | ---------------- | :----------------------------------------------------------- |
| [clock_time](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/clock_time) | 时钟时间         | `clock_time`允许创作者将当前时间与一个范围`(0.0, 1.0)`中的一个浮点数比较。 |
| [distance_to_nearest_player](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/distance_to_nearest_player) | 与最近玩家的距离 | `distance_to_nearest_player`允许将最近的玩家的距离与一个浮点数比较。 |
| [has_ability](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/has_ability) | 具有能力         | `has_ability`当主体实体具有与给定的名字相同的能力时返回`true`。 |
| [has_biome_tag](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/has_biome_tag) | 具有生物群系标签 | `has_biome_tag`测试主体所在的生物群系是否有指定标签。        |
| [has_component](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/has_component) | 具有组件         | `has_component`当主体实体具有与给定的名字相同的组件时返回`true`。 |
| [has_container_open](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/has_container_open) | 具有打开的容器   | `has_container_open`当主体玩家实体打开了一个容器时返回`true`。 |
| [has_damage](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/has_damage) | 具有伤害         | `has_damage`当主体实体接受到一个与给定的名字相同的伤害类型的伤害时返回`true`。 |
| [has_equipment](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/has_equipment) | 具有装备         | `has_equipment`测试主体实体物品栏指定的槽位中是否存在与给定的名字相同的物品。 |
| [has_mob_effect](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/has_mob_effect) | 具有生物效果     | `has_mob_effect`测试主体是否有特定的生物效果（即状态效果）。 |
| [has_ranged_weapon](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/has_ranged_weapon) | 具有远程武器     | `has_ranged_weapon`当主体实体持有一个比如弓或弩的远程武器时返回`true`。 |
| [has_tag](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/has_tag) | 具有标签         | `has_tag`如果主体实体具有给定的标签，则返回`true`。          |
| [has_target](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/has_target) | 具有目标         | `has_target`如果主体实体具有有效的目标，则返回`true`。       |
| [has_trade_supply](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/has_trade_supply) | 具有交易供给     | `has_trade_supply`测试目标是否有任何交易供给，如果目标不能进行交易，则返回`false`。 |
| [hourly_clock_time](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/hourly_clock_time) | 小时制时钟时间   | `hourly_clock_time`允许将当前24小时时间与一个范围`[0, 24000]`中的一个整数比较。 |
| [in_block](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/in_block) | 在方块内         | `in_block`当主体实体在一个指定方块类型的方块内部时返回`true`。 |
| [in_caravan](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/in_caravan) | 在商队内         | `in_caravan`如果主体实体在商队内，则返回`true`。             |
| [in_clouds](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/in_clouds) | 在云内           | `in_clouds`当主体实体在云中时返回`true`。                    |
| [in_contact_with_water](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/in_contact_with_water) | 在与水接触       | `in_contact_with_water`当主体实体与任意水体接触时返回`true`，这包括水、雨、喷溅型水瓶。 |
| [in_lava](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/in_lava) | 在熔岩内         | `in_lava`当主体实体在熔岩中时返回`true`。                    |
| [in_nether](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/in_nether) | 在下界内         | `in_nether`当主体实体在下界时返回`true`。                    |
| [in_water_or_rain](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/in_water_or_rain) | 在水或雨内       | `in_water_or_rain`当主体实体在水或雨中时返回`true`。         |
| [in_water](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/in_water) | 在水内           | `in_water`当主体实体在水中时返回`true`。                     |
| [inactivity_timer](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/inactivity_timer) | 不活动计时器     | `inactivity_timer`测试是否已经经过指定秒数时长的不活动时间。 |
| [is_altitude](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_altitude) | 是海拔           | `is_altitude`测试当前海拔是否是指定的数字。                  |
| [is_avoiding_mobs](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_avoiding_mobs) | 是正在规避生物的 | `is_avoiding_mobs`如果主体实体正在逃离其他生物，则返回`true`。 |
| [is_biome](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_biome) | 是生物群系       | `is_biome`测试主体当前是否在与给定的名字相同的生物群系内。   |
| [is_block](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_block) | 是方块           | `is_block`当方块具有指定名称时返回`true`。                   |
| [is_brightness](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_brightness) | 是亮度           | `is_brightness`测试当前亮度是否与一个范围`(0.0, 1.0)`中的值相同。 |
| [is_climbing](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_climbing) | 是正在攀爬的     | `is_climbing`如果主体实体正在攀爬，则返回`true`。            |
| [is_color](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_color) | 是颜色           | `is_color`如果主体实体是与给定的名字相同的颜色的，则返回`true`。 |
| [is_daytime](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_daytime) | 是白天           | `is_daytime`在白天返回`true`。                               |
| [is_difficulty](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_difficulty) | 是难度           | `is_difficulty`测试游戏当前的难度级别。                      |
| [is_family](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_family) | 是族             | `is_family`当主体实体属于与给定的名字相同的族时返回`true`。  |
| [is_game_rule](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_game_rule) | 是游戏规则       | `is_game_rule`测试与给定的名字相同的的游戏规则当前是否已激活。 |
| [is_humid](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_humid) | 是湿度           | `is_humid`测试主体是否处于一个给定湿度的区域内。             |
| [is_immobile](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_immobile) | 是不可移动的     | `is_immobile`如果主体实体不可移动，则返回`true`。如果一个实体缺乏AI意向，刚刚切换了维度或作为一个生物却已没有生命值，则它是不可移动的。 |
| [is_in_village](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_in_village) | 是在村庄内的     | `is_in_village`测试主体是否在村庄边界之内。                  |
| [is_leashed](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_leashed) | 是被栓牵的       | `is_leashed`如果主体实体已被栓牵，则返回`true`。             |
| [is_leashed_to](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_leashed_to) | 是被栓牵于       | `is_leashed_to`如果主体实体已被调用的实体栓牵，则返回`true`。 |
| [is_mark_variant](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_mark_variant) | 是标注变体       | `is_mark_variant`如果主体实体是所提供数字对应的标注变体，则返回`true`。 |
| [is_moving](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_moving) | 是正在移动的     | `is_moving`如果主体实体正在移动，则返回`true`。              |
| [is_owner](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_owner) | 是主人           | `is_owner`如果主体实体是调用实体的主人，则返回`true`。       |
| [is_persistent](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_persistent) | 是宿存的         | `is_persistent`如果主体实体的宿存性与传入的布尔值匹配，则返回`true`。 |
| [is_riding](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_riding) | 是正在骑乘的     | `is_riding`如果主体实体正在骑乘另一个实体，则返回`true`。    |
| [is_skin_id](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_skin_id) | 是皮肤ID         | `is_skin_id`如果主体实体使用的皮肤ID与提供的数字相同，则返回`true`。 |
| [is_sleeping](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_sleeping) | 是正在睡觉的     | `is_sleeping`测试主体是否在睡觉。                            |
| [is_sneaking](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_sneaking) | 是正在潜行的     | `is_sneaking`测试主体是否在潜行。                            |
| [is_snow_covered](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_snow_covered) | 是被雪覆盖的     | `is_snow_covered`测试主体所在区域是否被雪覆盖。              |
| [is_target](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_target) | 是目标           | `is_target`如果主体实体是调用的实体的目标，则返回`true`。    |
| [is_temperature_type](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_temperature_type) | 是温度类型       | `is_temperature_type`测试当前温度是否是给定值。              |
| [is_temperature_value](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_temperature_value) | 是温度值         | `is_temperature_value`测试当前温度是否与提供的一个范围`(0.0, 1.0)`中的值相同，其中`0.0`代表最冷的温度，而`1.0`代表最热。 |
| [is_underground](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_underground) | 是地下           | `is_underground`当主体实体在地下时时返回`true`。如果一个实体顶部没有非固体方块，则其被认为是在地下的。 |
| [is_underwater](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_underwater) | 是水下           | `is_underwater`当主体实体在水下时时返回`true`。              |
| [is_variant](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_variant) | 是变体           | `is_variant`如果主体实体是所提供数字对应的变体，则返回`true`。 |
| [is_visible](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/is_visible) | 是可见的         | `is_visible`如果主体实体是可见的，则返回`true`。             |
| [light_level](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/light_level) | 光照级别         | `light_level`测试实体在指定光照级别范围之外，范围在`0`到`16`之间。 |
| [moon_intensity](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/moon_intensity) | 月强             | `moon_intensity`允许将月强与一个`0.0`到`1.0`之间的浮点数比较。 |
| [moon_phase](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/moon_phase) | 月相             | `moon_phase`允许将月相与一个`0`到`7`之间的整数比较。         |
| [on_ground](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/on_ground) | 在地面上         | `on_ground`当主体实体在地面上时返回`true`。                  |
| [on_ladder](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/on_ladder) | 在梯子上         | `on_ladder`当主体实体在梯子上时返回`true`。                  |
| [random_chance](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/random_chance) | 随机机会         | `random_chance`如果随机机会从一个指定的范围内摇出`0`，则返回`true`。 |
| [rider_count](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/rider_count) | 骑手计数         | `rider_count`返回该实体的骑手数目。                          |
| [surface_mob](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/surface_mob) | 地表生物         | `surface_mob`测试主体实体是否是一个地表生物。                |
| [trusts](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/trusts) | 信任             | `trusts`如果主体被实体信任，则返回`true`。                   |
| [weather_at_position](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/weather_at_position) | 天气于位置       | `weather_at_position`在实体的位置测试当前的天气是否与提供的天气值相同。 |
| [weather](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/entityreference/examples/filters/weather) | 天气             | `weather`测试当前实体正在经历的天气状态。                    |
