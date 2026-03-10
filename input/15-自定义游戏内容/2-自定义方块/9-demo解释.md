---
front:
hard: 入门
time: 分钟
---

# demo解释

[CustomBlocksMod](../../13-模组SDK编程/60-Demo示例.md#CustomBlocksMod)中定义了以下自定义方块：

- customblocks:customblocks_test0

上表面与其他面不同的方块。

在`resource/blocks.json`中将isotropic的up设置为true，使其上表面在放置时会随机旋转，可以达到视觉上没有明显的贴图重复的效果，属于微软自定义方块的功能

演示了构成自定义群系，村民交易，自定义配方，方块组合的功能

- customblocks:customblocks_test_ore

性质与矿物相似的自定义方块

演示了挖掘，掉落物的功能

- customblocks:customblocks_test_face4

拥有4个面向的方块

演示了多面向中四面向的功能

- customblocks:customblocks_test_face6

拥有6个面向的方块

演示了多面向中六面向的功能

- customblocks:customblocks_test_mobspawner

自定义刷怪箱方块-原生生物

演示了“特殊方块-自定义刷怪箱”中生成原生生物的功能

- customblocks:customblocks_test_mobspawner1

自定义刷怪箱方块-微软自定义生物

演示了“特殊方块-自定义刷怪箱”中生成微软自定义生物的功能

- customblocks:customblocks_test_portal_blue

前往维度3的自定义传送门方块

演示了“特殊方块-自定义传送门方块”的功能

- customblocks:customblocks_test_block_entity<span id="demo解释_block_entity"></span>

含自定义方块实体的自定义方块

演示了自定义方块实体相关功能，详细解释见[自定义方块实体](./4-自定义方块实体.md#demo)文档

- customblocks:customblocks_model_flower

花形状的自定义方块

演示了自定义方块模型，亮度，碰撞盒，渲染材质，是否实心，是否可寻路的功能

- customblocks:customblocks_flower_extend

除了涵盖customblocks_model_flower（花形状的自定义方块）的基本功能外，额外拓展了实体穿过时减速、重力方块下落时被破坏等功能。

- customblocks:customblocks_model_decoration

四面向的使用自定义模型的方块

- customblocks:customblocks_model_wire

电线形状的自定义方块，可与旁边的其他电线，熔炉或草方块相连

演示了可变模型与可变碰撞箱

- customblocks:customblocks_test_heavy


演示了自定义重力方块

- customblocks:customblocks_slime

利用netease:block_properties组件和python事件复刻了一个原版粘液块特性

演示了自定义实体方块外观功能

- customblocks:custom_block_squirrel

包含了自定义实体方块的实体模型配置，网易版粒子、序列帧特效、微软原版粒子特效及音效配置。