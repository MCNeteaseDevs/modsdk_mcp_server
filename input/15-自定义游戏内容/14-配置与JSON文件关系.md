---
front:
hard: 入门
time: 分钟
---
# 配置与Json文件关系
## 配套文件

使用编辑器的配置功能和直接修改Json文件制作Addon的本质是一样的，每个不同类型的配置都对应着不同的配套文件，修改配置，对应的Json文件也会实时改变。

这里我们以实体配置举例，当我们新建好实体配置后，选中即可在属性面板的配套文件处看到其对应的Json文件路径，点击右侧的打开文件（下图红框内）按钮，即可打开Json

![image](./images/open_json_file.png)

Json支持多种软件打开和查看，这里我们使用vscode进行查看。

![image](./images/openjsonfile2.gif)

此时我们在配置界面增加字段，文件也会实时更新，如下图所示

![image](./images/editjsonfile.gif)

<br/>

关于如何进行配置的创建和使用可参考[配置的使用](./0-配置.md)，下面为你列出了当前编辑器支持的所有配置及其对应的文件:
>**点击标题的链接可以从Json文件层面深入了解自定义游戏内容的原理和作用：**

<br/>

## [自定义实体](./3-自定义生物/01-自定义基础生物.md)配置对应文件

>  行为包json：behavior_pack_xxxxxx/entities/实体名称.json
>
>  资源包json：resource_pack_xxxxxx/entity/实体名称.json
>
>  语言文件(单个模组唯一)：resource_pack_xxxxxx/texts/zh_CN.lang

<br/>

## [自定义物品](./1-自定义物品/1-自定义基础物品.md)配置对应文件

>  行为包json：***behavior_pack_xxxxxx/netease_items_beh/物品名称.json***
>
>  资源包json：***resource_pack_xxxxxx/netease_items_res/物品名称.json***
>
>  语言文件(单个模组唯一)：***resource_pack_xxxxxx/texts/zh_CN.lang***
>
>  盔甲穿戴属性文件：***resource_pack_xxxxxx/textures/物品名称.json***
>
>  物品贴图文件(单个模组唯一)：***resource_pack_xxxxxx/textures/item_texture.json***

<br/>

## [自定义方块](./2-自定义方块/0-自定义方块概述.md)配置对应文件

>  行为包json：***behavior_pack_xxxxxx/netease_blocks/方块名称.json***
>
>  方块贴图文件(单个模组唯一):***resource_pack_xxxxxx/textures/item_texture.json***
>
>  方块列表文件：***resource_pack_xxxxxx/block.json***
>
>  语言文件(单个模组唯一)：***resource_pack_xxxxxx/texts/zh_CN.lang***

<br/>

## [自定义配方](./5-自定义配方.md)配置对应文件

>  行为包json：***behavior_pack_xxxxxx/netease_recipes/配方名称.json***

<br/>

## <a href="../../../mconline/20-玩法地图教程/第05章：设置NPC的基本状态和交易表/课程03.给NPC添加对应的交易表.html" rel="noopenner"> 自定义交易表 </a>配置对应文件

>  行为包json：***behavior_pack_xxxxxx/trading/交易表名称.json***

<br/>

## <a href="../../../mconline/10-addon教程/第12章：更完善的自定义掉落物/课程01.更完善的自定义掉落物.html" rel="noopenner"> 自定义掉落表 </a>配置对应文件

>  行为包json：***behavior_pack_xxxxxx/loot_tables/掉落表名称.json***

<br/>

## [自定义生成规则](./4-自定义维度/3-生物生成.md)配置对应文件

>  行为包json：***behavior_pack_xxxxxx/spawn_rules/生成规则名称.json***
>
>  语言文件(单个模组唯一)：***resource_pack_xxxxxx/texts/zh_CN.lang***

<br/>

## [自定义维度](./4-自定义维度/1-自定义维度.md)配置对应文件

>  行为包json：***behavior_pack_xxxxxx/netease_dimension/维度配置名称.json***
>
>  语言文件(单个模组唯一)：***resource_pack_xxxxxx/texts/zh_CN.lang***

<br/>

## [自定义生物群系](./4-自定义维度/2-群系地貌.md)配置对应文件
>  行为包json：***behavior_pack_xxxxxx/netease_biomes/生物群系配置名称.json***
>
>  语言文件(单个模组唯一)：***resource_pack_xxxxxx/texts/zh_CN.lang***

<br/>

## [自定义特征](./4-自定义维度/4-自定义特征.md)配置对应文件

>  行为包json：***behavior_pack_xxxxxx/netease_features/特征名称.json***
>
>  语言文件(单个模组唯一)：***resource_pack_xxxxxx/texts/zh_CN.lang***

<br/>

## [自定义特征生成](./4-自定义维度/4-自定义特征.md)配置对应文件
 >  行为包json：***behavior_pack_xxxxxx/netease_feature_rules/特征生成规则.json***
 >
 >  语言文件(单个模组唯一)： ***resource_pack_xxxxxx/texts/zh_CN.lang***