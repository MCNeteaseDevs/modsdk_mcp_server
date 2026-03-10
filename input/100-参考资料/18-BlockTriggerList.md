# 国际版 - 方块触发器列表

> 文档版本：2022.10.26

## 注意事项

1. 本文档内容来源于[我的世界基岩版国际版文档](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blocktriggers/blocktriggerlist)，在此仅做翻译和补正，供各位开发者参考。
2. 本文档中少部分内容由于版本过高，尚无法在中国版中使用，请耐心等待中国版更新基岩版版本。
3. 本文档中绝大部分内容需要开启**假日创作者功能**实验性玩法才可以正常使用，请各位开发者注意辨别。欲了解更多关于实验性玩法的内容，请访问[《我的世界》基岩版中的实验功能](https://learn.microsoft.com/zh-cn/minecraft/creator/documents/experimentalfeaturestoggle)。

## 列表

| 组件原名                                                     | 组件译名       | 类型     | 描述                                                         |
| :----------------------------------------------------------- | :------------- | :------- | :----------------------------------------------------------- |
| [minecraft:on_fall_on](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blocktriggers/minecraftblock_on_fall_on) | 当跌落于时     | JSON对象 | `minecraft:on_fall_on`当一个活动对象（实体）跌落或降落至方块上时触发。 |
| [minecraft:on_interact](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blocktriggers/minecraftblock_on_interact) | 当交互时       | JSON对象 | `minecraft:on_interact`当一个活动对象（实体）与方块交互时触发。 |
| [minecraft:on_placed](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blocktriggers/minecraftblock_on_placed) | 当被放置时     | JSON对象 | `minecraft:on_placed`当一个活动对象（实体）在世界中放置方块时触发。 |
| [minecraft:on_player_destroyed](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blocktriggers/minecraftblock_on_player_destroyed) | 当被玩家摧毁时 | JSON对象 | `minecraft:on_player_destroyed`当一个标签为玩家的活动对象（实体）摧毁方块时触发。 |
| [minecraft:on_player_placing](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blocktriggers/minecraftblock_on_player_placing) | 当被玩家放置中 | JSON对象 | `minecraft:on_player_placing`当一个标签为玩家的活动对象（实体）在世界中放置方块时触发。 |
| [minecraft:on_step_off](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blocktriggers/minecraftblock_on_step_off) | 当步出时       | JSON对象 | `minecraft:on_step_off`当一个活动对象（实体）步出方块时触发。 |
| [minecraft:on_step_on](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blocktriggers/minecraftblock_on_step_on) | 当步入时       | JSON对象 | `minecraft:on_step_on`当一个活动对象（实体）步入方块时触发。 |
| [minecraft:queued_ticking](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blocktriggers/minecraftblock_queued_ticking) | 队列滴答       | JSON对象 | `minecraft:queued_ticking`单次或以由`interval_range`指定的区间中随机选择的刻数作为时间间隔触发指定事件。 |
| [minecraft:random_ticking](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/blockreference/examples/blocktriggers/minecraftblock_random_ticking) | 随机滴答       | JSON对象 | `minecraft:random_ticking`以基于“随机刻速度”游戏规则随机选择的时间间隔触发指定事件。随机刻速度决定了方块多快更新一次。 |
