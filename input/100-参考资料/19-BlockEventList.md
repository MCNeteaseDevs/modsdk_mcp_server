# 国际版 - 事件响应列表

> 文档版本：2022.10.26

## 注意事项

1. 本文档内容来源于[我的世界基岩版国际版文档](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/blockeventlist)，在此仅做翻译和补正，供各位开发者参考。
2. 本文档中少部分内容由于版本过高，尚无法在中国版中使用，请耐心等待中国版更新基岩版版本。
3. 本文档中绝大部分内容需要开启**假日创作者功能**实验性玩法才可以正常使用，请各位开发者注意辨别。欲了解更多关于实验性玩法的内容，请访问[《我的世界》基岩版中的实验功能](https://learn.microsoft.com/zh-cn/minecraft/creator/documents/experimentalfeaturestoggle)。
4. 同一种事件响应可能会被实体、物品和方块共用，文档中的【仅XX】意味着该事件响应只能在XX中使用，【非XX】意味着该事件响应可以在XX之外的另外两种中使用，【皆可行】意味着该事件响应在三种中都可以使用。
5. 本文档中一些事件响应虽然不存在于原文中，但是在实际应用中确实存在，故特为补充。

## 列表

| 事件响应原名                                                 | 事件响应译名   | 类型     | 描述                                                         |
| :----------------------------------------------------------- | :------------- | :------- | :----------------------------------------------------------- |
| [add_mob_effect](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_add_mob_effect) | 添加生物效果   | JSON对象 | 【非实体】`add_mob_effect`向目标添加一个状态效果。           |
| [damage](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_damage) | 伤害/损坏      | JSON对象 | 【非实体】`damage`对目标造成伤害/损坏。                      |
| [decrement_stack](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_decrement_stack) | 自减堆叠       | JSON对象 | 【非实体】`decrement_stack`自减物品堆叠数。                  |
| [die](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_die) | 致死           | JSON对象 | 【非实体】`die`杀死目标。如果目标是`self`且运行自一个方块，则摧毁该方块。 |
| [play_effect](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_play_effect) | 播放特效       | JSON对象 | 【非实体】`play_effect`相对于目标位置播放一个旧版粒子效果。  |
| [play_sound](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_play_sound) | 播放声音       | JSON对象 | 【非实体】`play_sound`相对于目标位置播放一个系统声音效果（或作存档声音事件）。 |
| [remove_mob_effect](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_remove_mob_effect) | 移除生物效果   | JSON对象 | 【非实体】`remove_mob_effect`从目标移除一个状态效果。        |
| [run_command](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_run_command) | 运行命令       | JSON对象 | 【皆可行】`run_command`触发一个或一列斜杠命令。              |
| [set_block](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_set_block) | 放置方块       | JSON对象 | 【仅方块】`set_block`将当前方块类型设置为其他方块类型。      |
| [set_block_at_pos](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_set_block_at_pos) | 放置方块于位置 | JSON对象 | 【仅方块】`set_block_at_pos`将相对于当前方块的一个方块设置为其他方块类型。 |
| [set_block_property](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_set_block_property) | 设置方块属性   | JSON对象 | 【非实体】`set_block_property`设置当前方块的一个方块属性。   |
| set_property                                                 | 设置属性       | JSON对象 | 【仅实体】`set_property`设置当前实体的一个实体属性。         |
| shoot                                                        | 发射           | JSON对象 | 【仅物品】`shoot`发射一个弹射物。                            |
| [spawn_loot](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_spawn_loot) | 生成战利品     | JSON对象 | 【仅方块】`spawn_loot`为方块生成战利品                       |
| [swing](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_swing) | 摆臂           | JSON对象 | 【非实体】`swing`使当前上下文中的活动对象（实体）摆臂。      |
| [teleport](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_teleport) | 传送           | JSON对象 | 【非实体】`teleport`将目标随机传送至目的地周围。             |
| [transform_item](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blockevents/minecraftblock_transform_item) | 转化物品       | JSON对象 | 【非实体】`transform_item`将一个物品转化为另一个物品。       |
