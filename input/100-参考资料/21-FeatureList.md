# 国际版 - 地物（*特征*）模式列表

> 文档版本：2022.10.26

## 注意事项

1. 本文档内容来源于[我的世界基岩版国际版文档](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/featurelist)，在此仅做翻译和补正，供各位开发者参考。
2. 本文档中少部分内容由于版本过高，尚无法在中国版中使用，请耐心等待中国版更新基岩版版本。
3. 本文档的内容如依照国际版写法，需要开启**自定义生物群系**实验性玩法才可以正常使用，其中部分内容可以通过中国版写法避免实验性玩法的开启，请各位开发者注意辨别。欲了解更多关于实验性玩法的内容，请访问[《我的世界》基岩版中的实验功能](https://learn.microsoft.com/zh-cn/minecraft/creator/documents/experimentalfeaturestoggle)。
4. 本文档中一些模式类型虽然不存在于原文中，但是在实际应用中确实存在，故特为补充。

## 列表

| 模式原名                                                     | 模式译名                     | 描述                                                         |
| :----------------------------------------------------------- | :--------------------------- | :----------------------------------------------------------- |
| [minecraft:aggregate_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftAggregate_feature) | 聚合地物（*特征*）           | `minecraft:aggregate_feature`用于以随机顺序放置一系列地物（*特征*）。 |
| [minecraft:beards_and_shavers](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftBeards_and_shavers) | 胡须与剃刀                   | `minecraft:beards_and_shavers`用于通过放置“胡须”并使用“剃刀”的形式来提供一个可在后续放置其他地物（*特征*）的平台。 |
| [minecraft:cave_carver_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftCave_carver_feature) | 洞穴雕刻器地物（*特征*）     | `minecraft:cave_carver_feature`用于在当前区块和周围每一个区块中以8向放射状雕刻一个洞穴。 |
| [minecraft:conditional_list](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftConditional_list) | 条件列表                     | `minecraft:conditional_list`用于放置一系列地物（*特征*）中第一个合适的地物（*特征*）。 |
| minecraft:fossil_feature                                     | 化石地物（*特征*）           | `minecraft:fossil_feature`用于生成由骨块和矿石组成的化石。   |
| [minecraft:geode_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftGeode_feature) | 晶洞地物（*特征*）           | `minecraft:geode_feature`用于通过生成一个岩层球模拟晶洞。    |
| [minecraft:growing_plant_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftGrowing_plant_feature) | 生长植物地物（*特征*）       | `minecraft:growing_plant_feature`用于在世界中放置一个生长植物。 |
| [minecraft:hell_cave_carver_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftHell_cave_carver_feature) | 地狱洞穴雕刻器               | `minecraft:hell_cave_carver_feature`用于在下界的当前区块和周围每一个区块中以8向放射状雕刻一个洞穴。 |
| [minecraft:multiface_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftMultiface_feature) | 多面向地物（*特征*）         | `minecraft:multiface_feature`用于在地板、墙面、天花板上放置一个或多个多面向方块。 |
| [minecraft:ore_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftOre_feature) | 矿石地物（*特征*）           | `minecraft:ore_feature`用于放置一个方块脉来模拟一个矿床。    |
| minecraft:partially_exposed_blob_feature                     | 部分暴露点斑地物（*特征*）   | `minecraft:partially_exposed_blob_feature`用于生成指定尺寸和方块的点斑。 |
| [minecraft:rect_layout](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftRect_layout) | 矩形布局                     | `minecraft:rect_layout`用于根据矩形区域的空白空间率放置地物（*特征*）。 |
| [minecraft:scan_surface](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftScan_surface) | 扫描表面                     | `minecraft:scan_surface`用于扫描一个区块的表面并在每个方块柱的上表面调用`place()`。 |
| [minecraft:scatter_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftScatter_feature) | 散植地物（*特征*）           | `minecraft:scatter_feature`用于在一个区块中散植一个地物（*特征*）。 |
| minecraft:sculk_patch_feature                                | 幽匿斑块地物（*特征*）       | `minecraft:sculk_patch_feature`用于生成幽匿斑块。            |
| [minecraft:search_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftSearch_feature) | 搜索地物（*特征*）           | `minecraft:search_feature`用于在区域中搜索一个目标地物（*特征*）的有效放置地点。 |
| [minecraft:sequence_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftSequence_feature) | 序列地物（*特征*）           | `minecraft:sequence_feature`用于根据数据中的顺序依次放置一系列地物（*特征*）。 |
| [minecraft:single_block_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftSingle_block_feature) | 单方块地物（*特征*）         | `minecraft:single_block_feature`用于在世界中方式一个单个方块。 |
| [minecraft:snap_to_surface_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftSnap_to_surface_feature) | 对齐至表面地物（*特征*）     | `minecraft:snap_to_surface_feature`用于将地物（*特征*）的Y轴放置位置对齐至由`vertical_search_range`提供的地板或天花板上。 |
| [minecraft:structure_template_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftStructure_template_feature) | 结构模板地物（*特征*）       | `minecraft:structure_template_feature`用于在世界中放置一个结构。结构必须以`.mcstructure`文件格式存储在行为包的`structures`子文件夹中。 |
| minecraft:tree_feature                                       | 树地物（*特征*）             | `minecraft:tree_feature`用于放置一棵树。                     |
| [minecraft:underwater_cave_carver_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftUnderwater_cave_carver) | 水下洞穴雕刻器地物（*特征*） | `minecraft:underwater_cave_carver_feature`用于在当前区块和周围每一个区块中以8向放射状雕刻一个含水洞穴。 |
| minecraft:vegetation_patch_feature                           | 植被斑块地物（*特征*）       | `minecraft:vegetation_patch_feature`用于生成植被斑块。       |
| [minecraft:weighted_random_feature](https://learn.microsoft.com/zh-cn/minecraft/creator/reference/content/featuresreference/examples/features/minecraftWeighted_random_feature) | 加权随机地物（*特征*）       | `minecraft:weighted_random_feature`用于基于一个加权的值随机生成一个地物（*特征*）。 |
