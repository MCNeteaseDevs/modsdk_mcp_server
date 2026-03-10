---
sidebarDepth: 1
---
# SDK接口封装SdkInterface



## 概述

- 描述

    SdkInterface是对SDK接口封装的基类。

- 成员变量

    | 变量名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 关联实体ID |
    | isClient | bool | 是否客户端 |



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetEntityId](#getentityid) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取对象实体ID |
| [ToPlayerPreset](#toplayerpreset) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 强制类型转换为玩家预设 |
| [ToEntityPreset](#toentitypreset) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 强制类型转换为实体预设 |
| [ToEffectPreset](#toeffectpreset) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 强制类型转换为特效预设 |
| [ToBlockPreset](#toblockpreset) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 强制类型转换为方块预设 |
| [ToUIPreset](#touipreset) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 强制类型转换为UI预设 |
| [GetServerSystem](#getserversystem) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 返回当前对象可使用的服务端system |
| [GetClientSystem](#getclientsystem) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 返回当前对象可使用的客户端system |
| [GetSystem](#getsystem) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 返回当前对象可使用的system |
| [GetLevelId](#getlevelid) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前对象所在的level_id |
| [CreateComponent](#createcomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 给实体创建组件 |
| [GetMinecraftEnum](#getminecraftenum) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 用于获取枚举值文档中的枚举值 |
| [DestroyEntity](#destroyentity) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 销毁实体 |
| [CreateActionComponent](#createactioncomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建action组件 |
| [SetEntityAttackTarget](#setentityattacktarget) | <span style="display:inline;color:#ff5555">服务端</span> | 设置仇恨目标 |
| [ResetEntityAttackTarget](#resetentityattacktarget) | <span style="display:inline;color:#ff5555">服务端</span> | 清除仇恨目标 |
| [GetEntityAttackTarget](#getentityattacktarget) | <span style="display:inline;color:#ff5555">服务端</span> | 获取仇恨目标 |
| [SetMobKnockback](#setmobknockback) | <span style="display:inline;color:#ff5555">服务端</span> | 设置击退的初始速度，需要考虑阻力的影响 |
| [CreateActorLootComponent](#createactorlootcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建actorLoot组件 |
| [SpawnLootTable](#spawnloottable) | <span style="display:inline;color:#ff5555">服务端</span> | 使用生物类型模拟一次随机掉落，生成的物品与json定义的概率有关 |
| [SpawnLootTableWithActor](#spawnloottablewithactor) | <span style="display:inline;color:#ff5555">服务端</span> | 使用生物实例模拟一次随机掉落，生成的物品与json定义的概率有关 |
| [CreateActorMotionComponent](#createactormotioncomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建actorMotion组件 |
| [GetDirFromRot](#getdirfromrot) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 通过旋转角度获取朝向 |
| [SetEntityMotion](#setentitymotion) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置生物的瞬时移动方向向量，服务端只能对非玩家使用，客户端只能对本地玩家使用 |
| [GetEntityMotion](#getentitymotion) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取生物（含玩家）的瞬时移动方向向量 |
| [GetInputVector](#getinputvector) | <span style="display:inline;color:#7575f9">客户端</span> | 获取本地玩家方向键（移动轮盘）的输入 |
| [LockInputVector](#lockinputvector) | <span style="display:inline;color:#7575f9">客户端</span> | 锁定本地玩家方向键（移动轮盘）的输入，可使本地玩家持续向指定方向前行，且不会再受玩家输入影响 |
| [UnlockInputVector](#unlockinputvector) | <span style="display:inline;color:#7575f9">客户端</span> | 解锁本地玩家方向键（移动轮盘）的输入 |
| [CreateActorOwnerComponent](#createactorownercomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建actorOwner组件 |
| [SetEntityOwner](#setentityowner) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的属主 |
| [GetEntityOwner](#getentityowner) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的属主 |
| [CreateActorPushableComponent](#createactorpushablecomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建actorPushable组件 |
| [SetActorPushable](#setactorpushable) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否可推动 |
| [CreateAttrComponent](#createattrcomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建attr组件 |
| [IsEntityOnFire](#isentityonfire) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体是否着火 |
| [SetEntityOnFire](#setentityonfire) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体着火 |
| [GetEntityAttrValue](#getentityattrvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 获取属性值，包括生命值，饥饿度，移速 |
| [GetEntityAttrMaxValue](#getentityattrmaxvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 获取属性最大值，包括生命值，饥饿度，移速 |
| [SetEntityAttrValue](#setentityattrvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 设置属性值，包括生命值，饥饿度，移速 |
| [SetEntityAttrMaxValue](#setentityattrmaxvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 设置属性最大值，包括生命值，饥饿度，移速 |
| [SetPlayerStepHeight](#setplayerstepheight) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家前进非跳跃状态下能上的最大台阶高度, 默认值为0.5625，1的话表示能上一个台阶 |
| [GetPlayerStepHeight](#getplayerstepheight) | <span style="display:inline;color:#ff5555">服务端</span> | 返回玩家前进非跳跃状态下能上的最大台阶高度 |
| [ResetPlayerStepHeight](#resetplayerstepheight) | <span style="display:inline;color:#ff5555">服务端</span> | 恢复引擎默认玩家前进非跳跃状态下能上的最大台阶高度 |
| [IsEntityInLava](#isentityinlava) | <span style="display:inline;color:#7575f9">客户端</span> | 实体是否在岩浆中 |
| [IsEntityOnGround](#isentityonground) | <span style="display:inline;color:#7575f9">客户端</span> | 实体是否触地 |
| [CreateAuxValueComponent](#createauxvaluecomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建auxValue组件 |
| [GetEntityAuxValue](#getentityauxvalue) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取射出的弓箭或投掷出的药水的附加值 |
| [CreateBiomeComponent](#createbiomecomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建biome组件 |
| [GetBiomeName](#getbiomename) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某一位置所属的生物群系信息 |
| [CreateBlockComponent](#createblockcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建block组件 |
| [RegisterBlockPatterns](#registerblockpatterns) | <span style="display:inline;color:#ff5555">服务端</span> | 注册特殊方块组合 |
| [CreateMicroBlockResStr](#createmicroblockresstr) | <span style="display:inline;color:#ff5555">服务端</span> | 生成微缩方块资源Json字符串 |
| [CreateBlockEntityData](#createblockentitydata) | <span style="display:inline;color:#ff5555">服务端</span> | 创建blockEntityData组件 |
| [GetCustomBlockEntityData](#getcustomblockentitydata) | <span style="display:inline;color:#ff5555">服务端</span> | 用于获取可操作某个自定义方块实体数据的对象，操作方式与dict类似 |
| [CreateBlockInfoComponent](#createblockinfocomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建blockInfo组件 |
| [GetBlock](#getblock) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取某一位置的block |
| [SetBlock](#setblock) | <span style="display:inline;color:#ff5555">服务端</span> | 设置某一位置的方块 |
| [GetTopBlockHeight](#gettopblockheight) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取当前维度某一位置最高的非空气方块的高度 |
| [GetBlockDestroyTime](#getblockdestroytime) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取使用物品破坏方块需要的时间 |
| [GetBlockEntityData](#getblockentitydata) | <span style="display:inline;color:#ff5555">服务端</span> | 用于获取方块（包括自定义方块）的数据，数据只读不可写 |
| [CreateBlockStateComponent](#createblockstatecomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建blockState组件 |
| [GetBlockStates](#getblockstates) | <span style="display:inline;color:#ff5555">服务端</span> | 获取<a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态" rel="noopenner"> 方块状态 </a> |
| [SetBlockStates](#setblockstates) | <span style="display:inline;color:#ff5555">服务端</span> | 设置<a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态" rel="noopenner"> 方块状态 </a> |
| [GetBlockAuxValueFromStates](#getblockauxvaluefromstates) | <span style="display:inline;color:#ff5555">服务端</span> | 根据方块名称和<a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态" rel="noopenner"> 方块状态 </a>获取方块附加值AuxValue |
| [GetBlockStatesFromAuxValue](#getblockstatesfromauxvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 根据方块名称和方块附加值AuxValue获取<a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态" rel="noopenner"> 方块状态 </a> |
| [CreateBlockUseEventWhiteList](#createblockuseeventwhitelist) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建blockUseEventWhiteList组件 |
| [AddBlockItemListenForUseEvent](#addblockitemlistenforuseevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 增加blockName方块对ServerBlockUseEvent事件的脚本层监听 |
| [RemoveBlockItemListenForUseEvent](#removeblockitemlistenforuseevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 移除blockName方块对ServerBlockUseEvent事件的脚本层监听 |
| [ClearAllListenForBlockUseEventItems](#clearalllistenforblockuseeventitems) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 清空所有已添加方块对ServerBlockUseEvent事件的脚本层监听 |
| [CreateBreathComponent](#createbreathcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建breath组件 |
| [GetUnitBubbleAirSupply](#getunitbubbleairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 单位气泡数对应的氧气储备值 |
| [GetEntityCurrentAirSupply](#getentitycurrentairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 生物当前氧气储备值 |
| [GetEntityMaxAirSupply](#getentitymaxairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物最大氧气储备值 |
| [SetEntityCurrentAirSupply](#setentitycurrentairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物氧气储备值 |
| [SetEntityMaxAirSupply](#setentitymaxairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物最大氧气储备值 |
| [IsEntityConsumingAirSupply](#isentityconsumingairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物当前是否在消耗氧气 |
| [SetEntityRecoverTotalAirSupplyTime](#setentityrecovertotalairsupplytime) | <span style="display:inline;color:#ff5555">服务端</span> | 设置恢复最大氧气量的时间，单位秒 |
| [CreateBulletAttributesComponent](#createbulletattributescomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建bulletAttributes组件 |
| [GetEntitySourceId](#getentitysourceid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取抛射物发射者实体id |
| [CreateChestBlockComponent](#createchestblockcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建chestBlock组件 |
| [GetChestBoxSize](#getchestboxsize) | <span style="display:inline;color:#ff5555">服务端</span> | 获取箱子容量大小 |
| [SetChestBoxItemNum](#setchestboxitemnum) | <span style="display:inline;color:#ff5555">服务端</span> | 设置箱子槽位物品数目 |
| [SetChestBoxItemExchange](#setchestboxitemexchange) | <span style="display:inline;color:#ff5555">服务端</span> | 交换箱子里物品的槽位 |
| [CreateChunkSourceComponent](#createchunksourcecomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建chunkSource组件 |
| [SetAddArea](#setaddarea) | <span style="display:inline;color:#ff5555">服务端</span> | 设置区块的常加载 |
| [DeleteArea](#deletearea) | <span style="display:inline;color:#ff5555">服务端</span> | 删除一个常加载区域 |
| [DeleteAllArea](#deleteallarea) | <span style="display:inline;color:#ff5555">服务端</span> | 删除所有常加载区域 |
| [GetAllAreaKeys](#getallareakeys) | <span style="display:inline;color:#ff5555">服务端</span> | 获取所有常加载区域名称列表 |
| [CheckChunkState](#checkchunkstate) | <span style="display:inline;color:#ff5555">服务端</span> | 判断指定位置的chunk是否加载完成 |
| [GetLoadedChunks](#getloadedchunks) | <span style="display:inline;color:#ff5555">服务端</span> | 获取指定维度当前已经加载完毕的全部区块的坐标列表 |
| [GetChunkEntities](#getchunkentities) | <span style="display:inline;color:#ff5555">服务端</span> | 获取指定位置的区块中，全部的实体和玩家的ID列表 |
| [GetChunkMobNum](#getchunkmobnum) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某区块中的生物数量（不包括玩家，但包括盔甲架） |
| [IsChunkGenerated](#ischunkgenerated) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某个区块是否生成过。 |
| [CreateCollisionBoxComponent](#createcollisionboxcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建collisionBox组件 |
| [SetEntityCollisionBoxSize](#setentitycollisionboxsize) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的包围盒 |
| [GetEntityCollisionBoxSize](#getentitycollisionboxsize) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的包围盒 |
| [CreateCommandComponent](#createcommandcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建command组件 |
| [SetCommand](#setcommand) | <span style="display:inline;color:#ff5555">服务端</span> | 使用游戏内指令 |
| [GetCommandPermissionLevel](#getcommandpermissionlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 返回设定使用/op命令时OP的权限等级（对应server.properties中的op-permission-level配置） |
| [SetCommandPermissionLevel](#setcommandpermissionlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 设置当玩家使用/op命令时OP的权限等级（对应server.properties中的op-permission-level配置） |
| [GetDefaultPlayerPermissionLevel](#getdefaultplayerpermissionlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 返回新玩家加入时的权限身份（对应server.properties中的default-player-permission-level配置） |
| [SetDefaultPlayerPermissionLevel](#setdefaultplayerpermissionlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 设置新玩家加入时的权限身份（对应server.properties中的default-player-permission-level配置） |
| [CreateControlAiComponent](#createcontrolaicomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建controlAi组件 |
| [SetEntityBlockControlAi](#setentityblockcontrolai) | <span style="display:inline;color:#ff5555">服务端</span> | 设置屏蔽生物原生AI |
| [CreateDimensionComponent](#createdimensioncomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建dimension组件 |
| [GetEntityDimensionId](#getentitydimensionid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体所在维度 |
| [ChangeEntityDimension](#changeentitydimension) | <span style="display:inline;color:#ff5555">服务端</span> | 传送玩家以外的实体 |
| [ChangePlayerDimension](#changeplayerdimension) | <span style="display:inline;color:#ff5555">服务端</span> | 传送玩家 |
| [MirrorDimension](#mirrordimension) | <span style="display:inline;color:#ff5555">服务端</span> | 复制不同dimension的地形 |
| [CreateDimension](#createdimension) | <span style="display:inline;color:#ff5555">服务端</span> | 创建新的dimension |
| [RegisterEntityAOIEvent](#registerentityaoievent) | <span style="display:inline;color:#ff5555">服务端</span> | 注册感应区域，有实体进入时和离开时会有消息通知 |
| [UnRegisterEntityAOIEvent](#unregisterentityaoievent) | <span style="display:inline;color:#ff5555">服务端</span> | 反注册感应区域 |
| [SetUseLocalTime](#setuselocaltime) | <span style="display:inline;color:#ff5555">服务端</span> | 让某个维度拥有自己的局部时间规则，开启后该维度可以拥有与其他维度不同的时间与是否昼夜更替的规则 |
| [GetUseLocalTime](#getuselocaltime) | <span style="display:inline;color:#ff5555">服务端</span> | 获取某个维度是否设置了使用局部时间规则 |
| [SetLocalTime](#setlocaltime) | <span style="display:inline;color:#ff5555">服务端</span> | 设置使用局部时间规则维度的时间 |
| [SetLocalTimeOfDay](#setlocaltimeofday) | <span style="display:inline;color:#ff5555">服务端</span> | 设置使用局部时间规则维度在一天内所在的时间 |
| [GetLocalTime](#getlocaltime) | <span style="display:inline;color:#ff5555">服务端</span> | 获取维度的时间 |
| [SetLocalDoDayNightCycle](#setlocaldodaynightcycle) | <span style="display:inline;color:#ff5555">服务端</span> | 设置使用局部时间规则的维度是否打开昼夜更替 |
| [GetLocalDoDayNightCycle](#getlocaldodaynightcycle) | <span style="display:inline;color:#ff5555">服务端</span> | 获取维度是否打开昼夜更替 |
| [CreateEffectComponent](#createeffectcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建effect组件 |
| [RemoveEffectFromEntity](#removeeffectfromentity) | <span style="display:inline;color:#ff5555">服务端</span> | 为实体删除指定状态效果 |
| [AddEffectToEntity](#addeffecttoentity) | <span style="display:inline;color:#ff5555">服务端</span> | 为实体添加指定状态效果，如果添加的状态已存在则有以下集中情况：1、等级大于已存在则更新状态等级及持续时间；2、状态等级相等且剩余时间duration大于已存在则刷新剩余时间；3、等级小于已存在则不做修改；4、粒子效果以新的为准 |
| [GetEntityEffects](#getentityeffects) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体当前所有状态效果 |
| [CreateEngineTypeComponent](#createenginetypecomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建engineType组件 |
| [GetEntityEngineTypeStr](#getentityenginetypestr) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取实体的类型名称 |
| [GetEntityEngineType](#getentityenginetype) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取实体类型 |
| [CreateEntityEventComponent](#createentityeventcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建entityEvent组件 |
| [TriggerEntityCustomEvent](#triggerentitycustomevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发生物自定义事件 |
| [CreateExtraDataComponent](#createextradatacomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建extraData组件 |
| [GetExtraData](#getextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的自定义数据或者世界的自定义数据，某个键所对应的值。获取实体数据传入对应实体id |
| [SaveExtraData](#saveextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 用于保存实体的自定义数据或者世界的自定义数据 |
| [SetExtraData](#setextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 用于设置实体的自定义数据或者世界的自定义数据，数据以键值对的形式保存。设置实体数据时使用对应实体id创建组件，设置世界数据时使用levelId创建组件 |
| [CleanExtraData](#cleanextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 清除实体的自定义数据或者世界的自定义数据，清除实体数据时使用对应实体id创建组件，清除世界数据时使用levelId创建组件 |
| [GetWholeExtraData](#getwholeextradata) | <span style="display:inline;color:#ff5555">服务端</span> | 获取完整的实体的自定义数据或者世界的自定义数据，获取实体数据时使用对应实体id创建组件，获取世界数据时使用levelId创建组件 |
| [CreateExpComponent](#createexpcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建exp组件 |
| [GetPlayerExp](#getplayerexp) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家当前等级下的经验值 |
| [AddPlayerExp](#addplayerexp) | <span style="display:inline;color:#ff5555">服务端</span> | 增加玩家经验值 |
| [GetPlayerTotalExp](#getplayertotalexp) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家的总经验值 |
| [SetPlayerTotalExp](#setplayertotalexp) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家的总经验值 |
| [GetOrbExperience](#getorbexperience) | <span style="display:inline;color:#ff5555">服务端</span> | 获取经验球的经验 |
| [SetOrbExperience](#setorbexperience) | <span style="display:inline;color:#ff5555">服务端</span> | 设置经验球经验 |
| [CreateExperienceOrb](#createexperienceorb) | <span style="display:inline;color:#ff5555">服务端</span> | 创建专属经验球 |
| [CreateExplosionComponent](#createexplosioncomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建explosion组件 |
| [CreateExplosion](#createexplosion) | <span style="display:inline;color:#ff5555">服务端</span> | 用于生成爆炸 |
| [CreateFeatureComponent](#createfeaturecomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建feature组件 |
| [AddNeteaseFeatureWhiteList](#addneteasefeaturewhitelist) | <span style="display:inline;color:#ff5555">服务端</span> | 添加结构对PlaceNeteaseStructureFeatureEvent事件的脚本层监听 |
| [RemoveNeteaseFeatureWhiteList](#removeneteasefeaturewhitelist) | <span style="display:inline;color:#ff5555">服务端</span> | 移除structureName对PlaceNeteaseStructureFeatureEvent事件的脚本层监听 |
| [ClearAllNeteaseFeatureWhiteList](#clearallneteasefeaturewhitelist) | <span style="display:inline;color:#ff5555">服务端</span> | 清空所有已添加Netease Structure Feature对PlaceNeteaseStructureFeatureEvent事件的脚本层监听 |
| [LocateStructureFeature](#locatestructurefeature) | <span style="display:inline;color:#ff5555">服务端</span> | 与[/locate指令](https://zh.minecraft.wiki/w/%E5%91%BD%E4%BB%A4/locate)相似，用于定位原版的部分结构，如海底神殿、末地城等。 |
| [LocateNeteaseFeatureRule](#locateneteasefeaturerule) | <span style="display:inline;color:#ff5555">服务端</span> | 与[/locate指令](https://zh.minecraft.wiki/w/%E5%91%BD%E4%BB%A4/locate)相似，用于定位<a href="../../../../15-自定义游戏内容/4-自定义维度/4-自定义特征.html#特征规则（feature-rules）" rel="noopenner"> 网易自定义特征规则 </a> |
| [CreateFlyComponent](#createflycomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建fly组件 |
| [IsPlayerFlying](#isplayerflying) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家是否在飞行 |
| [ChangePlayerFlyState](#changeplayerflystate) | <span style="display:inline;color:#ff5555">服务端</span> | 给予/取消飞行能力，并且进入飞行/非飞行状态 |
| [CreateGameComponent](#creategamecomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建game组件 |
| [AddBlockProtectField](#addblockprotectfield) | <span style="display:inline;color:#ff5555">服务端</span> | 设置一个方块无法被玩家/实体破坏的区域 |
| [RemoveBlockProtectField](#removeblockprotectfield) | <span style="display:inline;color:#ff5555">服务端</span> | 取消一个方块无法被玩家/实体破坏的区域 |
| [CleanBlockProtectField](#cleanblockprotectfield) | <span style="display:inline;color:#ff5555">服务端</span> | 取消全部已设置的方块无法被玩家/实体破坏的区域 |
| [KillEntity](#killentity) | <span style="display:inline;color:#ff5555">服务端</span> | 杀死某个Entity |
| [CreateEngineEntityByTypeStr](#createengineentitybytypestr) | <span style="display:inline;color:#ff5555">服务端</span> | 创建指定identifier的实体 |
| [PlaceStructure](#placestructure) | <span style="display:inline;color:#ff5555">服务端</span> | 放置结构 |
| [AddTimer](#addtimer) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 添加定时器，非重复 |
| [AddRepeatedTimer](#addrepeatedtimer) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 添加服务端触发的定时器，重复执行 |
| [CancelTimer](#canceltimer) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 取消定时器 |
| [GetEntitiesInArea](#getentitiesinarea) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取区域内的entity列表 |
| [GetEntitiesAround](#getentitiesaround) | <span style="display:inline;color:#ff5555">服务端</span> | 获取区域内的entity列表 |
| [ShowHealthBar](#showhealthbar) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否显示血条 |
| [SetNameDeeptest](#setnamedeeptest) | <span style="display:inline;color:#7575f9">客户端</span> | 设置名字是否透视 |
| [GetScreenSize](#getscreensize) | <span style="display:inline;color:#7575f9">客户端</span> | 获取游戏分辨率 |
| [SetRenderLocalPlayer](#setrenderlocalplayer) | <span style="display:inline;color:#7575f9">客户端</span> | 设置本地玩家是否渲染 |
| [AddPickBlacklist](#addpickblacklist) | <span style="display:inline;color:#7575f9">客户端</span> | 添加使用camera组件选取实体时的黑名单，即该实体不会被选取到 |
| [ClearPickBlacklist](#clearpickblacklist) | <span style="display:inline;color:#7575f9">客户端</span> | 清除使用camera组件选取实体的黑名单 |
| [CheckWordsValid](#checkwordsvalid) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 检查语句是否合法，即不包含敏感词 |
| [CheckNameValid](#checknamevalid) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 检查昵称是否合法，即不包含敏感词 |
| [GetScreenViewInfo](#getscreenviewinfo) | <span style="display:inline;color:#7575f9">客户端</span> | 获取游戏视角信息。分辨率为1313，618时，画布是376，250的2倍，所以viewport得到的是1313 + (2-(1313%2))，y值类似，可参考<a href="../../../../../18-界面与交互/1-界面编辑器使用说明.html#《我的世界》界面适配方法" rel="noopenner"> 《我的世界》界面适配方法 </a> |
| [SimulateTouchWithMouse](#simulatetouchwithmouse) | <span style="display:inline;color:#7575f9">客户端</span> | 模拟使用鼠标控制UI（PC F11快捷键） |
| [GetCurrentDimension](#getcurrentdimension) | <span style="display:inline;color:#7575f9">客户端</span> | 获取客户端当前维度 |
| [GetChinese](#getchinese) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取langStr对应的中文，可参考PC开发包中\handheld\bed-loc\handheld\data\resource_packs\vanilla\texts\zh_CN.lang |
| [SetDisableHunger](#setdisablehunger) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否屏蔽饥饿度 |
| [SetOneTipMessage](#setonetipmessage) | <span style="display:inline;color:#ff5555">服务端</span> | 在具体某个玩家的物品栏上方弹出tip类型通知，位置位于popup类型通知上方，此功能更建议在客户端使用game组件的对应接口SetTipMessage |
| [SetPopupNotice](#setpopupnotice) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 在物品栏上方弹出popup类型通知，位置位于tip类型消息下方，服务端调用是针对全体玩家，客户端调用只影响本地玩家 |
| [SetTipMessage](#settipmessage) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 在物品栏上方弹出tip类型通知，位置位于popup类型通知上方，服务端调用是针对全体玩家，客户端调用只影响本地玩家 |
| [SetNotifyMsg](#setnotifymsg) | <span style="display:inline;color:#ff5555">服务端</span> | 设置消息通知 |
| [GetPlayerGameType](#getplayergametype) | <span style="display:inline;color:#ff5555">服务端</span> | 获取指定玩家的游戏模式 |
| [HasEntity](#hasentity) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 判断 entity 是否存在 |
| [IsEntityAlive](#isentityalive) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 判断生物实体是否存活或非生物实体是否存在 |
| [CreateGravityComponent](#creategravitycomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建gravity组件 |
| [GetEntityGravity](#getentitygravity) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的重力因子，当生物重力因子为0时则应用世界的重力因子 |
| [SetEntityGravity](#setentitygravity) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的重力因子，当生物重力因子为0时则应用世界的重力因子 |
| [CreateHurtComponent](#createhurtcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建hurt组件 |
| [SetHurtByEntity](#sethurtbyentity) | <span style="display:inline;color:#ff5555">服务端</span> | 对实体造成伤害 |
| [SetHurtByEntityNew](#sethurtbyentitynew) | <span style="display:inline;color:#ff5555">服务端</span> | 对实体造成伤害 |
| [SetEntityImmuneDamage](#setentityimmunedamage) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否免疫伤害（该属性存档） |
| [CreateItemBannedComponent](#createitembannedcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建itembanned组件 |
| [AddBannedItem](#addbanneditem) | <span style="display:inline;color:#ff5555">服务端</span> | 增加禁用物品 |
| [GetBannedItemList](#getbanneditemlist) | <span style="display:inline;color:#ff5555">服务端</span> | 获取禁用物品列表 |
| [RemoveBannedItem](#removebanneditem) | <span style="display:inline;color:#ff5555">服务端</span> | 移除禁用物品 |
| [ClearBannedItems](#clearbanneditems) | <span style="display:inline;color:#ff5555">服务端</span> | 清空禁用物品 |
| [CreateItemComponent](#createitemcomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建item组件 |
| [GetItemBasicInfo](#getitembasicinfo) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取物品的基础信息 |
| [GetLocalPlayerId](#getlocalplayerid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取本地玩家的id |
| [ClearPlayerOffHand](#clearplayeroffhand) | <span style="display:inline;color:#ff5555">服务端</span> | 清除玩家左手物品 |
| [GetPlayerItem](#getplayeritem) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家物品，支持获取背包，盔甲栏，副手以及主手物品 |
| [ChangePlayerItemTipsAndExtraId](#changeplayeritemtipsandextraid) | <span style="display:inline;color:#ff5555">服务端</span> | 修改玩家物品的自定义tips和自定义标识符 |
| [AddEnchantToInvItem](#addenchanttoinvitem) | <span style="display:inline;color:#ff5555">服务端</span> | 给物品栏的物品添加附魔信息 |
| [GetInvItemEnchantData](#getinvitemenchantdata) | <span style="display:inline;color:#ff5555">服务端</span> | 获取物品栏的物品附魔信息 |
| [GetOffhandItem](#getoffhanditem) | <span style="display:inline;color:#7575f9">客户端</span> | 获取左手物品的信息 |
| [SetInvItemNum](#setinvitemnum) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家背包物品数目 |
| [SpawnItemToLevel](#spawnitemtolevel) | <span style="display:inline;color:#ff5555">服务端</span> | 生成物品掉落物，如果需要获取物品的entityId，可以调用服务端系统接口CreateEngineItemEntity |
| [SpawnItemToPlayerInv](#spawnitemtoplayerinv) | <span style="display:inline;color:#ff5555">服务端</span> | 生成物品到玩家背包 |
| [SpawnItemToPlayerCarried](#spawnitemtoplayercarried) | <span style="display:inline;color:#ff5555">服务端</span> | 生成物品到玩家右手 |
| [GetCarriedItem](#getcarrieditem) | <span style="display:inline;color:#7575f9">客户端</span> | 获取右手物品的信息 |
| [GetSlotId](#getslotid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前手持的快捷栏的槽id |
| [GetItemFormattedHoverText](#getitemformattedhovertext) | <span style="display:inline;color:#7575f9">客户端</span> | 获取物品的格式化hover文本，如：§f灾厄旗帜§r |
| [GetItemHoverName](#getitemhovername) | <span style="display:inline;color:#7575f9">客户端</span> | 获取物品的hover名称，如：灾厄旗帜§r |
| [GetItemEffectName](#getitemeffectname) | <span style="display:inline;color:#7575f9">客户端</span> | 获取物品的状态描述，如：§7保护 0§r |
| [GetUserDataInEvent](#getuserdatainevent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 使物品相关客户端事件的<a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典" rel="noopenner"> 物品信息字典 </a>参数带有userData。在mod初始化时调用即可 |
| [ChangeItemTexture](#changeitemtexture) | <span style="display:inline;color:#7575f9">客户端</span> | 替换物品的贴图，修改后所有用到该贴图的物品都会被改变，后续创建的此类物品也会被改变。会同时修改物品在UI界面上的显示，手持时候的显示与场景掉落的显示。 |
| [CreateLvComponent](#createlvcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建lv组件 |
| [GetPlayerLevel](#getplayerlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家等级 |
| [AddPlayerLevel](#addplayerlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 修改玩家等级 |
| [CreateMobSpawnComponent](#createmobspawncomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建mobSpawn组件 |
| [SpawnCustomModule](#spawncustommodule) | <span style="display:inline;color:#ff5555">服务端</span> | 设置自定义刷怪 |
| [CreateModAttrComponent](#createmodattrcomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建modAttr组件 |
| [SetEntityModAttr](#setentitymodattr) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置属性值 |
| [GetEntityModAttr](#getentitymodattr) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取属性值 |
| [RegisterEntityModAttrUpdateFunc](#registerentitymodattrupdatefunc) | <span style="display:inline;color:#7575f9">客户端</span> | 注册属性值变换时的回调函数，当属性变化时会调用该函数 |
| [UnRegisterEntityModAttrUpdateFunc](#unregisterentitymodattrupdatefunc) | <span style="display:inline;color:#7575f9">客户端</span> | 反注册属性值变换时的回调函数 |
| [CreateModelComponent](#createmodelcomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建model组件 |
| [SetEntityOpacity](#setentityopacity) | <span style="display:inline;color:#7575f9">客户端</span> | 设置生物模型的透明度 |
| [PlayEntityAnim](#playentityanim) | <span style="display:inline;color:#7575f9">客户端</span> | 播放骨骼动画 |
| [GetEntityModelId](#getentitymodelid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取骨骼模型的Id，主要用于特效绑定骨骼模型 |
| [SetEntityModel](#setentitymodel) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置骨骼模型 |
| [ResetEntityModel](#resetentitymodel) | <span style="display:inline;color:#7575f9">客户端</span> | 恢复实体为原版模型 |
| [BindModelToEntity](#bindmodeltoentity) | <span style="display:inline;color:#7575f9">客户端</span> | 实体替换骨骼模型后，再往上其他挂接骨骼模型。 |
| [UnBindModelToEntity](#unbindmodeltoentity) | <span style="display:inline;color:#7575f9">客户端</span> | 取消实体上挂接的某个骨骼模型。取消挂接后，这个modelId的模型便会销毁，无法再使用，如果是临时隐藏可以使用HideModel |
| [CreateMoveToComponent](#createmovetocomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建moveTo组件 |
| [SetEntityMoveSetting](#setentitymovesetting) | <span style="display:inline;color:#ff5555">服务端</span> | 寻路组件 |
| [CreateMsgComponent](#createmsgcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建msg组件 |
| [SendMsg](#sendmsg) | <span style="display:inline;color:#ff5555">服务端</span> | 模拟玩家给所有人发送聊天栏消息 |
| [SendMsgToPlayer](#sendmsgtoplayer) | <span style="display:inline;color:#ff5555">服务端</span> | 模拟玩家给另一个玩家发送聊天栏消息 |
| [NotifyOneMessage](#notifyonemessage) | <span style="display:inline;color:#ff5555">服务端</span> | 给指定玩家发送聊天框消息 |
| [CreateNameComponent](#createnamecomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建name组件 |
| [GetEntityName](#getentityname) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物的自定义名称，即使用命名牌或者SetName接口设置的名称 |
| [SetEntityName](#setentityname) | <span style="display:inline;color:#ff5555">服务端</span> | 用于设置生物的自定义名称，跟原版命名牌作用相同，玩家和新版流浪商人暂不支持 |
| [SetPlayerPrefixAndSuffixName](#setplayerprefixandsuffixname) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家前缀和后缀名字 |
| [SetEntityShowName](#setentityshowname) | <span style="display:inline;color:#7575f9">客户端</span> | 设置生物名字是否按照默认游戏逻辑显示 |
| [SetEntityAlwaysShowName](#setentityalwaysshowname) | <span style="display:inline;color:#7575f9">客户端</span> | 设置生物名字是否一直显示，瞄准点不指向生物时也能显示 |
| [CreatePersistenceComponent](#createpersistencecomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建persistence组件 |
| [SetEntityPersistence](#setentitypersistence) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否存盘 |
| [CreatePetComponent](#createpetcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建pet组件 |
| [DisablePet](#disablepet) | <span style="display:inline;color:#ff5555">服务端</span> | 关闭官方伙伴功能，单人游戏以及本地联机不支持该接口 |
| [EnablePet](#enablepet) | <span style="display:inline;color:#ff5555">服务端</span> | 启用官方伙伴功能，单人游戏以及本地联机不支持该接口 |
| [CreatePlayerComponent](#createplayercomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建player组件 |
| [EnablePlayerKeepInventory](#enableplayerkeepinventory) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置玩家死亡不掉落物品 |
| [CreatePortalComponent](#createportalcomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建portal组件 |
| [CreatePosComponent](#createposcomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建pos组件 |
| [GetEntityPos](#getentitypos) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取实体位置 |
| [GetEntityFootPos](#getentityfootpos) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取实体脚所在的位置 |
| [SetEntityPos](#setentitypos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体位置 |
| [SetEntityFootPos](#setentityfootpos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体脚底所在的位置 |
| [CreateProjectileComponent](#createprojectilecomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建projectile组件 |
| [CreateProjectileEntity](#createprojectileentity) | <span style="display:inline;color:#ff5555">服务端</span> | 创建抛射物（直接发射） |
| [CreateRecipeComponent](#createrecipecomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建recipe组件 |
| [GetRecipeResult](#getreciperesult) | <span style="display:inline;color:#ff5555">服务端</span> | 根据配方id获取配方结果。仅支持合成配方 |
| [GetRecipesByResult](#getrecipesbyresult) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 通过输出物品查询配方所需要的输入材料 |
| [GetRecipesByInput](#getrecipesbyinput) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 通过输入物品查询配方 |
| [CreateRedStoneComponent](#createredstonecomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建redStone组件 |
| [CreateRideComponent](#createridecomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建ride组件 |
| [CreateRotComponent](#createrotcomponent) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 创建rot组件 |
| [GetEntityRot](#getentityrot) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取实体角度 |
| [SetEntityRot](#setentityrot) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置实体的头的角度 |
| [SetEntityLookAtPos](#setentitylookatpos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置非玩家的实体看向某个位置 |
| [GetBodyRot](#getbodyrot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取实体的身体的角度 |
| [LockLocalPlayerRot](#locklocalplayerrot) | <span style="display:inline;color:#7575f9">客户端</span> | 在分离摄像机时，锁定本地玩家的头部角度 |
| [SetPlayerLookAtPos](#setplayerlookatpos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置本地玩家看向某个位置 |
| [CreateScaleComponent](#createscalecomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建scale组件 |
| [CreateTameComponent](#createtamecomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建tame组件 |
| [CreateTimeComponent](#createtimecomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建time组件 |
| [GetTime](#gettime) | <span style="display:inline;color:#ff5555">服务端</span> | 获取当前世界时间 |
| [CreateWeatherComponent](#createweathercomponent) | <span style="display:inline;color:#ff5555">服务端</span> | 创建weather组件 |
| [CreateActorCollidableComponent](#createactorcollidablecomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建actorCollidable组件 |
| [CreateActorRenderComponent](#createactorrendercomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建actorRender组件 |
| [CreateCustomAudioComponent](#createcustomaudiocomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建customAudio组件 |
| [CreateBrightnessComponent](#createbrightnesscomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建brightness组件 |
| [SetEntityBrightness](#setentitybrightness) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置实体的亮度 |
| [CreateCameraComponent](#createcameracomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建camera组件 |
| [PickFacing](#pickfacing) | <span style="display:inline;color:#7575f9">客户端</span> | 获取准星选中的实体或者方块 |
| [CreateFogComponent](#createfogcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建fog组件 |
| [CreateFrameAniControlComponent](#createframeanicontrolcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建frameAniControl组件 |
| [SetFrameAniLoop](#setframeaniloop) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧是否循环播放，默认为否 |
| [SetFrameAniFaceCamera](#setframeanifacecamera) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧是否始终朝向摄像机，默认为是 |
| [SetFrameAniDeepTest](#setframeanideeptest) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧是否透视，默认为否 |
| [CreateFrameAniEntityBindComponent](#createframeanientitybindcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建frameAniEntityBind组件 |
| [BindFrameAniToEntity](#bindframeanitoentity) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 绑定entity |
| [CreateFrameAniSkeletonBindComponent](#createframeaniskeletonbindcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建frameAniSkeletonBind组件 |
| [BindFrameAniToSkeleton](#bindframeanitoskeleton) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 绑定骨骼模型 |
| [CreateFrameAniTransComponent](#createframeanitranscomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建frameAniTrans组件 |
| [GetFrameAniPos](#getframeanipos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取序列帧位置 |
| [GetFrameAniRot](#getframeanirot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取序列帧的角度 |
| [GetFrameAniScale](#getframeaniscale) | <span style="display:inline;color:#7575f9">客户端</span> | 获取序列帧的缩放 |
| [SetFrameAniPos](#setframeanipos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧位置 |
| [SetFrameAniRot](#setframeanirot) | <span style="display:inline;color:#7575f9">客户端</span> | 设置特效的角度 |
| [SetFrameAniScale](#setframeaniscale) | <span style="display:inline;color:#7575f9">客户端</span> | 设置序列帧的缩放 |
| [CreateHealthComponent](#createhealthcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建health组件 |
| [ShowEntityHealth](#showentityhealth) | <span style="display:inline;color:#7575f9">客户端</span> | 设置某个entity是否显示血条，默认为显示 |
| [CreateOperationComponent](#createoperationcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建operation组件 |
| [SetCanAll](#setcanall) | <span style="display:inline;color:#7575f9">客户端</span> | 同时设置SetCanMove，SetCanJump，SetCanAttack，SetCanWalkMode，SetCanPerspective，SetCanPause，SetCanChat，SetCanScreenShot，SetCanOpenInv，SetCanDrag，SetCanInair |
| [CreateDeviceComponent](#createdevicecomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建device组件 |
| [CreateParticleControlComponent](#createparticlecontrolcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建particleControl组件 |
| [CreateParticleEntityBindComponent](#createparticleentitybindcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建particleEntityBind组件 |
| [BindParticleToEntity](#bindparticletoentity) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 粒子特效绑定entity |
| [CreateParticleSkeletonBindComponent](#createparticleskeletonbindcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建particleSkeletonBind组件 |
| [BindParticleToSkeleton](#bindparticletoskeleton) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 绑定粒子特效到骨骼模型 |
| [CreateParticleTransComponent](#createparticletranscomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建particleTrans组件 |
| [GetParticlePos](#getparticlepos) | <span style="display:inline;color:#7575f9">客户端</span> | 获取特效位置 |
| [GetParticleRot](#getparticlerot) | <span style="display:inline;color:#7575f9">客户端</span> | 获取特效角度 |
| [SetParticlePos](#setparticlepos) | <span style="display:inline;color:#7575f9">客户端</span> | 设置特效位置 |
| [SetParticleRot](#setparticlerot) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置特效的角度 |
| [CreatePlayerViewComponent](#createplayerviewcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建playerView组件 |
| [GetPlayerPerspective](#getplayerperspective) | <span style="display:inline;color:#7575f9">客户端</span> | 获取当前的视角模式 |
| [SetPlayerPerspective](#setplayerperspective) | <span style="display:inline;color:#7575f9">客户端</span> | 设置视角模式 |
| [LockPlayerPerspective](#lockplayerperspective) | <span style="display:inline;color:#7575f9">客户端</span> | 锁定玩家的视角模式 |
| [CreateQueryVariableComponent](#createqueryvariablecomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建queryVariable组件 |
| [CreateSkyRenderComponent](#createskyrendercomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建skyRender组件 |
| [CreateTextBoardComponent](#createtextboardcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建textBoard组件 |
| [CreateTextNotifyClientComponent](#createtextnotifyclientcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建textNotifyClient组件 |
| [CreateConfigClientComponent](#createconfigclientcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建config组件 |
| [CreateVirtualWorldComponent](#createvirtualworldcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建virtualWorld组件实例组件 |
| [CreatePlayerAnimComponent](#createplayeranimcomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建玩家动画组件 |
| [CreatePostProcessComponent](#createpostprocesscomponent) | <span style="display:inline;color:#7575f9">客户端</span> | 创建PostProcess组件 |




## GetEntityId

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取对象实体ID

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str或int | 实体ID或None |



## ToPlayerPreset

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    强制类型转换为玩家预设

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PlayerPreset | 玩家预设或None |



## ToEntityPreset

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    强制类型转换为实体预设

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EntityPreset | 实体预设或None |



## ToEffectPreset

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    强制类型转换为特效预设

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EffectPreset | 特效预设或None |



## ToBlockPreset

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    强制类型转换为方块预设

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockPreset | 方块预设或None |



## ToUIPreset

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    强制类型转换为UI预设

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | UIPreset | UI预设或None |



## GetServerSystem

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    返回当前对象可使用的服务端system

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ServerSystem | 服务端system，客户端返回空 |



## GetClientSystem

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    返回当前对象可使用的客户端system

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ClientSystem | 客户端system，服务端返回空 |



## GetSystem

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    返回当前对象可使用的system

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ClientSystem或ServerSystem | 返回当前对象可使用的system |



## GetLevelId

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取当前对象所在的level_id

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | level_id |



## CreateComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    给实体创建组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseComponent | 组件实例 |



## GetMinecraftEnum

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    用于获取枚举值文档中的枚举值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | minecraftEnum | 枚举集合类 |

- 示例

```python
self.GetMinecraftEnum().GameType.Survival
```



## DestroyEntity

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    销毁实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 销毁的实体ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否销毁成功 |



## CreateActionComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建action组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ActionCompServer | action组件实例 |



## SetEntityAttackTarget

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置仇恨目标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | targetId | str | 目标实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetEntityAttackTarget(entityId, targetId)
```



## ResetEntityAttackTarget

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    清除仇恨目标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.ResetEntityAttackTarget(entityId)
```



## GetEntityAttackTarget

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取仇恨目标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 仇恨目标的实体id |

- 示例

```python
self.GetEntityAttackTarget(entityId)
```



## SetMobKnockback

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置击退的初始速度，需要考虑阻力的影响

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | xd | float | x轴方向，用來控制角度 |
    | zd | float | z轴方向，用來控制角度 |
    | power | float | 用来控制水平方向的初速度 |
    | height | float | 竖直方向的初速度 |
    | heightCap | float | 向上速度阈值，当实体本身已经有向上的速度时需要考虑这个值，用来确保最终向上的速度不会超过heightCap |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | None | 无返回值 |

- 示例

```python
self.SetMobKnockback(entityId, 0.1, 0.1, 1.0, 1.0, 1.0)
```



## CreateActorLootComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建actorLoot组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ActorLootComponentServer | actorLoot组件实例 |



## SpawnLootTable

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    使用生物类型模拟一次随机掉落，生成的物品与json定义的概率有关

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 掉落位置 |
    | identifier | str | 实体identifier，如minecraft:guardian |
    | playerKillerId | str | 玩家杀手（只能是玩家），不设置则会随机在一个玩家维度掉落 |
    | damageCauseEntityId | str | 伤害来源实体Id（掉落与该实体手持物品的抢夺附魔等级有关），默认None |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功生成掉落 |

- 备注
    - 需要在对应的player实体附近生成，否则会生成失败。对于某些特殊的生物，如minecraft:sheep，需要使用SpawnLootTableWithActor接口来模拟随机掉落。

- 示例

```python
result = self.SpawnEntityLootTable((1, 4, 5), 'minecraft:guardian')
```



## SpawnLootTableWithActor

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    使用生物实例模拟一次随机掉落，生成的物品与json定义的概率有关

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 掉落位置 |
    | entityId | str | 模拟生物的生物Id |
    | playerKillerId | str | 玩家杀手（只能是玩家），不设置则会随机在一个玩家维度掉落 |
    | damageCauseEntityId | str | 伤害来源实体Id（掉落与该实体手持物品的抢夺附魔等级有关），默认None |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功生成掉落 |

- 备注
    - 需要在对应的player实体附近生成，否则会生成失败

- 示例

```python
result = self.SpawnLootTableWithActor((1, 4, 5), '-335007449086')
```



## CreateActorMotionComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建actorMotion组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ActorMotionComponentServer或ActorMotionComponentClient | actorMotion组件实例 |



## GetDirFromRot

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    通过旋转角度获取朝向

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rot | tuple(float,float) | 俯仰角度及绕竖直方向的角度，单位是角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 玩家朝向的单位向量 |

- 示例

```python
direction = self.GetDirFromRot((0, 0))
```



## SetEntityMotion

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置生物的瞬时移动方向向量，服务端只能对非玩家使用，客户端只能对本地玩家使用

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | motion | tuple(float,float,float) | 世界坐标系下的向量，该方向为世界坐标系下的向量，以x,z,y三个轴的正方向为正值，可以通过当前生物的rot组件判断目前玩家面向的方向，可在开发模式下打开F3观察数值变化。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 使生物向准星的方向突进一段距离
rot = self.GetEntityRot(entityId)
x, y, z = self.GetDirFromRot(rot)
self.SetMotion(entityId, (x * 5, y * 5, z * 5))
# rot 和 世界坐标系关系
#           ^ x -90°
#           |
# 180°/-180  ----------> z 0°
#           | 90°
```



## GetEntityMotion

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取生物（含玩家）的瞬时移动方向向量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(int,int,int) | 瞬时移动方向向量，异常时返回None |

- 示例

```python
self.GetEntityMotion(entityId)
```



## GetInputVector

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取本地玩家方向键（移动轮盘）的输入

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 返回一个单位向量，向量第一项为向左的大小，第二项为向前的大小 |

- 示例

```python
left, up = self.GetInputVector()
```



## LockInputVector

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    锁定本地玩家方向键（移动轮盘）的输入，可使本地玩家持续向指定方向前行，且不会再受玩家输入影响

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | inputVector | tuple(float,float) | 输入向量，第一项控制向左的大小，第二项控制向前的大小。传入(0, 0)时玩家将会被强制固定在原地，不允许移动。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否锁定成功，True:成功  False:失败 |

- 备注
    - 传入的向量会被转化为单位向量，因此传入(10, 0)与传入(0.1, 0)效果相同

- 示例

```python
# 使玩家向左前方持续移动
self.LockInputVector((1, 1))
```



## UnlockInputVector

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    解锁本地玩家方向键（移动轮盘）的输入

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否解锁成功，True:成功  False:失败 |



## CreateActorOwnerComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建actorOwner组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ActorOwnerComponentServer | actorOwner组件实例 |



## SetEntityOwner

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置实体的属主

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | ownerId | str | 属主实体id，为None时设置实体的属主为空 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功，True表示设置成功 |

- 示例

```python
result = self.SetEntityOwner(entityId, ownerId)
```



## GetEntityOwner

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体的属主

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 实体属主id |

- 示例

```python
ownerId = self.GetEntityOwner(entityId)
```



## CreateActorPushableComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建actorPushable组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ActorPushableCompServer | actorPushable组件实例 |



## SetActorPushable

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置实体是否可推动

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | isPushable | int | 0:不可推动  1:可推动 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示设置成功 |

- 示例

```python
success = self.SetActorPushable(entityId, 1)
```



## CreateAttrComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建attr组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | AttrCompServer或AttrCompClient | attr组件实例 |



## IsEntityOnFire

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体是否着火

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否着火 |

- 示例

```python
isOnFire = self.IsEntityOnFire(entityId)
```



## SetEntityOnFire

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置实体着火

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | seconds | int | 着火时间（单位：秒） |
    | burn_damage | int | 着火状态下每秒扣的血量,不传的话默认是1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 在水中或者雨中不会生效，着火时间受生物装备、生物的状态影响。burn_damage取值范围是0~1000,小于0将取0，大于1000将取1000

- 示例

```python
self.SetEntityOnFire(entityId, 1, 2)
```



## GetEntityAttrValue

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取属性值，包括生命值，饥饿度，移速

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | attrType | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/AttrType.html">AttrType枚举</a> |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 属性结果 |

- 示例

```python
self.GetEntityAttrValue(entityId, self.GetMinecraftEnum().AttrType.HEALTH)
```



## GetEntityAttrMaxValue

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取属性最大值，包括生命值，饥饿度，移速

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | attrType | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/AttrType.html">AttrType枚举</a> |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 属性值结果 |

- 示例

```python
self.GetEntityAttrMaxValue(entityId, self.GetMinecraftEnum().AttrType.HEALTH)
```



## SetEntityAttrValue

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置属性值，包括生命值，饥饿度，移速

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | attrType | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/AttrType.html">AttrType枚举</a> |
    | value | float | 属性值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 设置接口暂不支持 ABSORPTION

- 示例

```python
self.SetEntityAttrValue(entityId, self.GetMinecraftEnum().AttrType.HEALTH, 20)
```



## SetEntityAttrMaxValue

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置属性最大值，包括生命值，饥饿度，移速

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | attrType | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/AttrType.html">AttrType枚举</a> |
    | value | float | 属性值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 设置的最大饱和度不能超过当前的饥饿值; 食用食物后，最大饱和度会被原版游戏机制修改
    - 设置接口暂不支持 ABSORPTION

- 示例

```python
self.SetEntityAttrMaxValue(entityId, serverApi.GetMinecraftEnum().AttrType.SPEED, 0.2)
```



## SetPlayerStepHeight

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置玩家前进非跳跃状态下能上的最大台阶高度, 默认值为0.5625，1的话表示能上一个台阶

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |
    | stepHeight | float | 最大高度，需要大于0 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 为了避免因浮点数误差导致错误，设置的时候通常会增加1/16个方块大小，即0.0625。所以此处我们设置2.0625。游戏中默认值是0.5625，即半格高度。
    - 只对玩家生效，无法修改其它实体该属性
    - 修改后不影响跳跃逻辑及跳跃高度，并不会因此而跳到更高，因此在某些特定情况下，你可以走上方块但跳不上去。

- 示例

```python
#如果前面放置有两格高的方块，玩家按前进能直接上去，无须跳跃
self.SetPlayerStepHeight(playerId, 2.0625)
```



## GetPlayerStepHeight

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    返回玩家前进非跳跃状态下能上的最大台阶高度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 台阶高度 |



## ResetPlayerStepHeight

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    恢复引擎默认玩家前进非跳跃状态下能上的最大台阶高度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |



## IsEntityInLava

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    实体是否在岩浆中

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否在岩浆中，True为在岩浆中，False为不在岩浆中 |

- 备注
    - 只能获取到本地客户端已加载的实体是否在岩浆中，若实体在其他维度或未加载（距离本地玩家太远），将获取失败

- 示例

```python
isInLava = self.isEntityInLava(entityId)
```



## IsEntityOnGround

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    实体是否触地

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否触地，True为触地，False为不触地 |

- 备注
    - 客户端实体刚创建时引擎计算还没完成，此时获取该实体是否着地将返回默认值True，需要延迟一帧进行获取才能获取到正确的数据
    - 生物处于骑乘状态时，如玩家骑在猪身上，也视作触地
    - 只能获取到本地客户端已加载的实体是否触地，若实体在其他维度或未加载（距离本地玩家太远），将获取失败

- 示例

```python
isOnGound = self.isEntityOnGround(entityId)
```



## CreateAuxValueComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建auxValue组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | AuxValueComponentServer或AuxValueComponentClient | auxValue组件实例 |



## GetEntityAuxValue

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取射出的弓箭或投掷出的药水的附加值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | auxValue |

- 示例

```python
self.GetAuxValue(entityId)
```



## CreateBiomeComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建biome组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BiomeCompServer | biome组件实例 |



## GetBiomeName

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取某一位置所属的生物群系信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 指定位置 |
    | dimId | int | 维度id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 该位置所属生物群系name |

- 备注
    - 如果在自定义群系中没有重写原版带hills_transformation，mutate_transformation组件的群系，那么这些没有被重写的相关群系获取名称可能不正确。

- 示例

```python
biomeName = self.GetBiomeName((0, 80, 0), 0)
```



## CreateBlockComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建block组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockCompServer | block组件实例 |



## RegisterBlockPatterns

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    注册特殊方块组合

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pattern | list(str) | 方块组合位置 |
    | defines | dict | 方块组合类型 |
    | result_actor_name | str | 合成结果 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
pattern = [
    ' # ',
    'XXX',
    ' X '
    ]
defines ={
    '#': 'minecraft:gold_block',
    'X': 'minecraft:iron_block'
}
self.RegisterBlockPatterns(pattern, defines, 'minecraft:chicken')
#该例子左中右下放铁块，上面放金块，会生成一只鸡
```



## CreateMicroBlockResStr

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    生成微缩方块资源Json字符串

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | identifier | str | 微缩方块唯一标识 |
    | start | tuple(int,int,int) | 微缩起始坐标 |
    | end | tuple(int,int,int) | 微缩结束坐标 |
    | colorMap | dict | 默认为None，微缩方块颜色对应表 |
    | isMerge | bool | 默认为False，是否合并同类型方块 |
    | icon | str | 默认为空字符串，微缩方块图标，需要定义在 terrain_texture.json 中 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 生成的微缩方块的资源字符串 |

- 示例

```python
result = self.CreateMicroBlockResStr("x", (12, 60, 12), (26, 76, 26), colorMap={'minecraft:grass': [12, 22, 123, 255]}, isMerge=True, icon="micro_block_datiangou")
with open("micro_block_x.json", "w+") as f:
    f.write(result)
#该例子中，方块将以 (12 60 12) 为起点，以 (26 76 26) 为终点进行微缩，最终微缩方块里所有草方块的颜色为 rgba(12,22,123,255)，实际显示颜色会依据环境光照微调，物品栏里的图标为 terrain_texture.json 里 micro_block_datiangou 对应的图片。
```



## CreateBlockEntityData

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建blockEntityData组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockEntityExDataCompServer | blockEntityData组件实例 |



## GetCustomBlockEntityData

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    用于获取可操作某个自定义方块实体数据的对象，操作方式与dict类似

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度 |
    | pos | tuple(int,int,int) | 方块所在位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockEntityData或None | 可操作该方块实体内数据的对象 |

- 备注
    - GetBlockEntityData返回None通常是由于该方块所在区块未加载、正在退出游戏、该方块不是自定义方块或该自定义方块的json中并未配置netease:block_entity组件。<br>在对GetBlockEntityData返回对象进行操作前，请先判断它是否为空，否则会导致```'NoneType' object has no attribute '__getitem__'```错误。
    - 支持python基本数据类型(int/float/string/bool/dict/list)，不支持tuple且**dict的key必须为字符串**
    - **存储list时，list内各项的数据类型应相同，否则将存储失败**。如[True, False]可成功存储，[True, 1, 0.5]会存储失败
    - **虽然返回的对象操作与dict相似，但并不支持嵌套存储，只允许形如blockEntityData['key'] = value的直接赋值。如blockEntityData["value5"] ["v1"] = 9或blockEntityData["value6"].append(True)的操作将无法成功存储数据。**
    - 存储整数时，若数值范围超过int所能表示的最大范围，将无法成功存储。建议将此类数值转为字符串进行存储。

- 示例

```python
dimension = 0
pos = (4, 3, 2)
# GetBlockEntityData在某些情况下会返回None，对返回结果进行操作前务必先判断它是否为空
blockEntityData = self.GetCustomBlockEntityData(dimension, pos)
# 存储数据
# 支持存储python基本数据类型(int/float/string/bool/dict/list)，不支持tuple，并且key必须为字符串
# 存储list时，list内各项的数据类型应相同，否则将存储失败
if blockEntityData:
    blockEntityData['value1'] = 10
    blockEntityData['value2'] = 3.5
    blockEntityData['value3'] = True
    blockEntityData['value4'] = "hello"
    blockEntityData['value5'] = {"v1": 10, "v2": 3.5, "v3": [0,1,2]}
    blockEntityData['value6'] = [True, False]
# 读取数据
if blockEntityData:
    value1 = blockEntityData['value1']
    value5 = blockEntityData['value5']
    # 不存在于方块实体中的数据将返回None
    valueNone = blockEntityData['valueNone']
```



## CreateBlockInfoComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建blockInfo组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockInfoComponentServer或BlockInfoComponentClient | blockInfo组件实例 |



## GetBlock

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取某一位置的block

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |
    | dimensionId | int | 方块所在维度，服务端可在对应维度的常加载区块获取方块，对客户端无效，客户端只能获取当前维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../10-基本概念/1-我的世界基础概念.html#方块信息字典" rel="noopenner"> 方块信息字典 </a> |

- 备注
    - 已经加载的地形才能获取方块信息，支持获取对应维度的常加载区块内方块信息
    - 对于有多种状态的方块，aux计算比较复杂，推荐使用GetBlockStates获取方块状态字典

- 示例

```python
blockDict = self.GetBlock((0, 5, 0), 0)
```



## SetBlock

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置某一位置的方块

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |
    | blockDict | dict | <a href="../../../../10-基本概念/1-我的世界基础概念.html#方块信息字典" rel="noopenner"> 方块信息字典 </a> |
    | oldBlockHandling | int | 0：替换，1：销毁，2：保留，默认为0 |
    | dimensionId | int | 方块所在维度，必需参数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 已经加载的地形才能设置方块，支持在对应维度的常加载区块内设置方块
    - **若使用SetBlockNew接口替换含方块实体的方块，除自定义方块实体外，当替换前后方块实体类型相同时，其方块实体内数据不会发生改变。**
        例如在箱子中放置了物品，使用SetBlockNew接口将箱子方块替换为箱子方块后，新的箱子中依然保留旧箱子内的物品。<br>
        要避免这种情况，中间添加一次不同方块实体类型（或不含方块实体）的方块替换即可。比如先将箱子替换为空气，再将空气替换为箱子。
    - 对于有多种状态的方块，aux计算方式比较复杂，推荐先设置完方块后再使用SetBlockStates设置方块状态字典

- 示例

```python
blockDict = {
    'name': 'minecraft:wool',
    'aux': 5
}
self.SetBlock((0, 5, 0), blockDict, 0, 0)
```



## GetTopBlockHeight

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取当前维度某一位置最高的非空气方块的高度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int) | x轴与z轴位置 |
    | dimension | int | 维度id，默认为0，对客户端无效，服务端可在获取常加载区块内最高非空气方块高度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或None | 高度。若位置上无无非空气方块返回-1。若区块未加载返回None |

- 示例

```python
height = self.GetTopBlockHeight((5, 5))
```



## GetBlockDestroyTime

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取使用物品破坏方块需要的时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，格式[namespace:name:auxvalue]，auxvalue默认为0 |
    | itemName | str | 物品标识符，格式[namespace:name:auxvalue]，auxvalue默认为0，默认为None（不使用物品） |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 需要消耗的时间 |

- 示例

```python
self.GetBlockDestroyTime("minecraft:diamond_block", "minecraft:stone_pickaxe")
```



## GetBlockEntityData

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    用于获取方块（包括自定义方块）的数据，数据只读不可写

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度 |
    | pos | tuple(int,int,int) | 方块所在位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict或None | 方块实体内数据的对象 |

- 备注
    - **随着版本更迭，方块中包含的数据结构可能被微软团队调整，并且不会公告，使用该接口的开发者需注意版本更新时做好测试和兼容。数据编码为UTF-8
        适用于：[方块实体](https://zh.minecraft.wiki/w/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93)
        特殊情况：末影箱的物品信息不能通过该接口获取

- 示例

```python
blockEntityData = self.GetBlockEntityData(0, (4, 3, 2))
```



## CreateBlockStateComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建blockState组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockStateComponentServer | blockState组件实例 |



## GetBlockStates

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取<a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态" rel="noopenner"> 方块状态 </a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 方块位置 |
    | dimensionId | int | 方块所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 方块状态，异常时为None |

- 备注
    - 仅可获取到已加载区块内的方块状态，支持获取对应维度的常加载区块内方块状态

- 示例

```python
self.GetBlockStates((4,4,3), 0)
```



## SetBlockStates

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置<a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态" rel="noopenner"> 方块状态 </a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 方块位置 |
    | data | dict | 方块状态 |
    | dimensionId | int | 方块所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 仅可设置已加载区块内的方块状态，支持设置对应维度的常加载区块内方块状态

- 示例

```python
# 将白色羊毛设置为橙色羊毛
pos = (4,4,3)
state = self.GetBlockStates(pos, 0) # state = { 'color': 'white' }
state['color'] = 'orange'
self.SetBlockStates(pos, state, 0)
```



## GetBlockAuxValueFromStates

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    根据方块名称和<a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态" rel="noopenner"> 方块状态 </a>获取方块附加值AuxValue

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称 |
    | states | dict | 方块状态 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 方块附加值AuxValue，异常时为-1 |

- 示例

```python
states = self.GetBlockAuxValueFromStates("minecraft:hopper", {"facing_direction": 0, "toggle_bit": 0})
```



## GetBlockStatesFromAuxValue

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    根据方块名称和方块附加值AuxValue获取<a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态" rel="noopenner"> 方块状态 </a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称 |
    | auxValue | int | 方块附加值AuxValue |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 方块状态，异常时为None |

- 示例

```python
states = self.GetBlockStatesFromAuxValue('minecraft:sapling', 9)
```



## CreateBlockUseEventWhiteList

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建blockUseEventWhiteList组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockUseEventWhiteListComponentServer或BlockUseEventWhiteListComponentClient | blockUseEventWhiteList组件实例 |



## AddBlockItemListenForUseEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    增加blockName方块对ServerBlockUseEvent事件的脚本层监听

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称，格式：namespace:name:auxvalue，其中namespace:name:*匹配所有的auxvalue |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否增加成功 |

- 示例

```python
self.AddBlockItemListenForUseEvent("minecraft:nether_brick_stairs:2")
# 注意blockName格式为namespace:name:auxvalue，如果不填auxvalue，则默认为0
# auxValue详细值详见官方wiki，如https://zh.minecraft.wiki/w/楼梯 中的‘方块数据值’
```



## RemoveBlockItemListenForUseEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    移除blockName方块对ServerBlockUseEvent事件的脚本层监听

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称，格式：namespace:name:auxvalue，其中namespace:name:*匹配所有的auxvalue |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否移除成功 |

- 示例

```python
self.RemoveBlockItemListenForUseEvent("minecraft:nether_brick_stairs:2")
# 注意blockName格式为namespace:name:auxvalue，如果不填auxvalue，则默认为0
# auxValue详细值详见官方wiki，如https://zh.minecraft.wiki/w/楼梯 中的‘方块数据值’
```



## ClearAllListenForBlockUseEventItems

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    清空所有已添加方块对ServerBlockUseEvent事件的脚本层监听

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否清空成功 |



## CreateBreathComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建breath组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BreathCompServer | breath组件实例 |



## GetUnitBubbleAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    单位气泡数对应的氧气储备值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 单位气泡数对应的氧气储备值 |



## GetEntityCurrentAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    生物当前氧气储备值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 生物当前氧气储备值 |

- 备注
    - 注意：该值返回的是当前氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）

- 示例

```python
self.GetCurrentAirSupply(entityId)
```



## GetEntityMaxAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取生物最大氧气储备值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 最大氧气储备值 |

- 备注
    - 注意：该值返回的是最大氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）

- 示例

```python
self.GetEntityMaxAirSupply(entityId)
```



## SetEntityCurrentAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置生物氧气储备值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | data | int | 设置生物当前氧气值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 注意：该值设置的是当前氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）

- 示例

```python
self.SetEntityCurrentAirSupply(entityId, 300)
```



## SetEntityMaxAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置生物最大氧气储备值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | data | int | 设置生物最大氧气值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 注意：该值设置的是最大氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）

- 示例

```python
self.SetEntityMaxAirSupply(entityId, 400)
```



## IsEntityConsumingAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取生物当前是否在消耗氧气

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否消耗氧气 |

- 示例

```python
self.IsEntityConsumingAirSupply(entityId)
```



## SetEntityRecoverTotalAirSupplyTime

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置恢复最大氧气量的时间，单位秒

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | timeSec | float | 恢复生物最大氧气值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注意：当设置的最大氧气值小于（timeSec*10）时，生物每帧恢复氧气量的值为0

- 示例

```python
self.SetEntityRecoverTotalAirSupplyTime(entityId, 10)
```



## CreateBulletAttributesComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建bulletAttributes组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BulletAttributesComponentServer | bulletAttributes组件实例 |



## GetEntitySourceId

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取抛射物发射者实体id

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 抛射物发射者实体id |

- 示例

```python
self.GetEntitySourceId(entityId)
```



## CreateChestBlockComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建chestBlock组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ChestContainerCompServer | chestBlock组件实例 |



## GetChestBoxSize

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取箱子容量大小

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 箱子位置 |
    | dimensionId | int | 箱子所在维度，可获取对应维度的常加载区块内箱子容量 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 箱子大小，错误值-1 |

- 示例

```python
self.GetChestBoxSize((x, y, z), 0)
```



## SetChestBoxItemNum

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置箱子槽位物品数目

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 箱子位置 |
    | slotPos | int | 箱子槽位 |
    | num | int | 物品数目 |
    | dimensionId | int | 方块所在维度，可在对应维度的常加载区块设置方块 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetChestBoxItemNum((x,y,z), 0, 10, 0)
```



## SetChestBoxItemExchange

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    交换箱子里物品的槽位

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | pos | tuple(int,int,int) | 箱子位置 |
    | slotPos1 | int | 箱子槽位1 |
    | slotPos2 | int | 箱子槽位2 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置成功返回True，失败返回False |

- 示例

```python
self.SetChestBoxItemExchange(playerId, (x,y,z), 0, 1)
```



## CreateChunkSourceComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建chunkSource组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ChunkSourceCompServer或ChunkSourceCompClient | chunkSource组件实例 |



## SetAddArea

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置区块的常加载

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 常加载区域的名称 |
    | dimensionId | int | 区块所在的维度 |
    | minPos | tuple(int,int,int) | 加载区域的最小坐标 |
    | maxPos | tuple(int,int,int) | 加载区域的最大坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - key必须唯一，若添加区域时key已存在将添加失败。
    - 该方式创建的常加载区域不会tick，即实体，方块实体，随机刻都不会进行更新。若需要区域被tick，请使用原版[tickingarea指令](https://zh.minecraft.wiki/w/%E5%91%BD%E4%BB%A4/tickingarea)。
    - 将当前未加载的区块设置为常加载区块时，不会从存档加载生物。但如果是当前已加载的区块，则玩家远离区块后，区块内的实体会一直保持加载。
    - 常加载区块内可以使用api创建实体、放置方块、放置结构、修改方块实体数据。但由于区块加载的特性，需要将操作位置的四周外延80格的区域都设置为常加载，例如需要在(0,5,0)的位置生成生物/放置方块，需要将(-80,0,-80)到(80,0,80)的区域设置为常加载。

- 示例

```python
self.SetAddArea('Area0', 0, (0,0,0), (60,0,60))
```



## DeleteArea

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    删除一个常加载区域

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 常加载区域的名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 删除是否成功 |

- 示例

```python
self.DeleteArea('Area0')
```



## DeleteAllArea

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    删除所有常加载区域

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 删除的区域数目，错误时为None |



## GetAllAreaKeys

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取所有常加载区域名称列表

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 名称列表list |



## CheckChunkState

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    判断指定位置的chunk是否加载完成

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | chunk所在维度 |
    | pos | tuple(int,int,int) | 指定位置的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 加载是否完成 |

- 示例

```python
self.CheckChunkState(0, (0, 0, 0))
```



## GetLoadedChunks

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取指定维度当前已经加载完毕的全部区块的坐标列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | None或list(tuple(int,int)) | 区块坐标的列表（区块坐标为(x,z)），当指定维度不存在或尚未创建时，返回None |

- 示例

```python
result = self.GetLoadedChunks(0)
print "dimension {} has chunk {}".format(0, result)
```



## GetChunkEntities

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取指定位置的区块中，全部的实体和玩家的ID列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度 |
    | pos | tuple(int,int,int) | 指定位置的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | None或list(str) | 实体和玩家的ID的列表，当指定位置的区块不存在或尚未加载时，返回None |

- 示例

```python
entityList = self.GetChunkEntites(0, (0, 0, 0))
print "GetChunkEntities entityList={}".format(entityList)
```



## GetChunkMobNum

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取某区块中的生物数量（不包括玩家，但包括盔甲架）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 区块所在维度 |
    | chunkPos | tuple(int,int) | 指定区块的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 该区块中的生物数量 |

- 备注
    - 返回值为-1通常是由于该维度未加载、该区块未加载

- 示例

```python
mobNum = self.GetChunkMobNum(0, (1, 3))
```



## IsChunkGenerated

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取某个区块是否生成过。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 区块所在维度 |
    | chunkPos | tuple(int,int) | 指定区块的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 该区块是否生成过 |

- 备注
    - 玩家探索过（以玩家为中心，模拟距离（在游戏的设置页面内）为半径内的区块），或者使用SetAddArea设置常加载区块附近的区块，都是生成过的区块。这些区块会保存到存档里，再次探索时会从存档读取，不会重新生成。

- 示例

```python
# 获取主世界(10000,0,10000)坐标所在的区块是否生成过
result = self.IsChunkGenerated(0, comp.GetChunkPosFromBlockPos((10000, 0, 10000)))
```



## CreateCollisionBoxComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建collisionBox组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | CollisionBoxComponentServer | collisionBox组件实例 |



## SetEntityCollisionBoxSize

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置实体的包围盒

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | size | tuple(float,float) | 第一位表示宽度和长度，第二位表示高度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 对新生产的实体需要经过5帧之后再设置包围盒的大小才会生效

- 示例

```python
self.SetEntityCollisionBoxSize(entityId, (2,3))
```



## GetEntityCollisionBoxSize

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体的包围盒

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 包围盒大小 |

- 示例

```python
self.GetEntityCollisionBoxSize(entityId)
```



## CreateCommandComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建command组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | CommandCompServer | command组件实例 |



## SetCommand

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    使用游戏内指令

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cmdStr | str | 指令 |
    | playerId | str | 玩家id（可选），如果playerId不设置，则随机选择玩家 |
    | showOutput | bool | 是否输出到聊天窗口：可选，默认False，如果为True的话会和聊天窗口输入原生指令一样输出返回信息。只有当该参数为True的时候会触发OnCommandOutputServerEvent与OnCommandOutputClientEvent |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 命令是否执行成功 |

- 示例

```python
# 传送指令
self.SetCommand("/tp @p 100 5 100")
```



## GetCommandPermissionLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    返回设定使用/op命令时OP的权限等级（对应server.properties中的op-permission-level配置）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 权限等级：1-OP可以绕过重生点保护；2-OP可以使用所有单人游戏作弊命令；3-OP可以使用大多数多人游戏中独有的命令；4-OP可以使用所有命令 |

- 示例

```python
opLevel = self.GetCommandPermissionLevel()
print "GetCommandPermissionLevel oplevel={}".format(opLevel)
```



## SetCommandPermissionLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置当玩家使用/op命令时OP的权限等级（对应server.properties中的op-permission-level配置）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | opLevel | int | 权限等级：1-OP可以绕过重生点保护；2-OP可以使用所有单人游戏作弊命令；3-OP可以使用大多数多人游戏中独有的命令；4-OP可以使用所有命令 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 命令是否执行成功 |

- 备注
    - 此API不会修改已经获取了op的玩家的权限等级，仅影响调用API之后才获取op的玩家，建议在游戏初始化时调用此API

- 示例

```python
opLevel = 4
suc = self.SetCommandPermissionLevel(opLevel)
print "SetCommandPermissionLevel to {} suc={}".format(opLevel, suc)
```



## GetDefaultPlayerPermissionLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    返回新玩家加入时的权限身份（对应server.properties中的default-player-permission-level配置）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 权限身份：0-Visitor；1-Member；2-Operator；3-自定义 |

- 示例

```python
opLevel = self.GetDefaultPlayerPermissionLevel()
print "GetDefaultPlayerPermissionLevel oplevel={}".format(opLevel)
```



## SetDefaultPlayerPermissionLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置新玩家加入时的权限身份（对应server.properties中的default-player-permission-level配置）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | opLevel | int | 权限身份：0-Visitor；1-Member；2-Operator；3-自定义 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 命令是否执行成功 |

- 备注
    - 此API不会修改已经加入过游戏的玩家的权限身份，仅影响调用API之后才新加入的玩家，建议在游戏初始化时调用此API

- 示例

```python
opLevel = 1
suc = self.SetDefaultPlayerPermissionLevel(opLevel)
print "SetDefaultPlayerPermissionLevel to {} suc={}".format(opLevel, suc)
```



## CreateControlAiComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建controlAi组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ControlAiCompServer | controlAi组件实例 |



## SetEntityBlockControlAi

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置屏蔽生物原生AI

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | isBlock | bool | 是否保留AI，False为屏蔽 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 屏蔽AI后的生物无法行动，不受重力且不会被推动。但是可以受到伤害，也可以被玩家交互（例如马被骑或村民被交易）

- 示例

```python
self.SetBlockControlAi(entityId, False)
```



## CreateDimensionComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建dimension组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | DimensionCompServer | dimension组件实例 |



## GetEntityDimensionId

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体所在维度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 维度id，0-主世界; 1-下界; 2-末地; 或其他自定义维度 |



## ChangeEntityDimension

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    传送玩家以外的实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | dimensionId | int | 维度id，0-主世界; 1-下界; 2-末地; 或其他自定义维度 |
    | pos | tuple(int,int,int) | 传送的坐标，假如输入None，那么就优先选择目标维度的传送门作为目的地，其次使用维度坐标映射逻辑确定目的地 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 该接口无法对玩家使用，玩家请使用ChangePlayerDimension

- 示例

```python
self.ChangeEntityDimension(entityId, 0, (0,4,0))
```



## ChangePlayerDimension

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    传送玩家

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |
    | dimensionId | int | 维度，0-overWorld; 1-nether; 2-theEnd |
    | pos | tuple(int,int,int) | 传送的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 该接口在成功切换维度时pos位置为玩家头的位置，即比设定位置低1.62

- 示例

```python
self.ChangePlayerDimension(playerId, 0, (0,4,0))
```



## MirrorDimension

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    复制不同dimension的地形

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fromId | int | 原dimensionId |
    | toId | int | 目标dimensionId |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 仅复制源维度已经生成的区块信息到新的维度，对于未生成的源维度区块无法完全复制生成逻辑，可能采用部分新维度自己的信息。

- 示例

```python
self.MirrorDimension(0, 1)
```



## CreateDimension

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建新的dimension

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 维度，0/1/2维度是不需要创建的。创建大于20的维度，需要在dimension_config.json中注册，注意，维度21是不可用的 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否创建成功 |

- 备注
    - 建议在mod初始化时统一调用

- 示例

```python
self.CreateDimension(3)
```



## RegisterEntityAOIEvent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    注册感应区域，有实体进入时和离开时会有消息通知

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | name | str | 注册的感应区域名 |
    | aabb | tuple(float,float,float,float,float,float) | 感应区域的坐标范围，依次为minX, minY, minZ, maxX, maxY, maxZ |
    | ignoredEntities | list(str) | 忽略的实体id列表 |
    | entityType | int | 期望响应的实体类型，不传则响应所有的实体类型<a href="../../../../../../mcdocs/1-ModAPI/枚举值/EntityType.html">EntityType枚举</a> |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 备注
    - 注册完感应区域后，需通过监听OnEntityAreaEvent或NewOnEntityAreaEvent事件来获取感应事件

- 示例

```python
self.RegisterEntityAOIEvent(0, "test", (0, 0, 0, 1, 1, 1), None)
```



## UnRegisterEntityAOIEvent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    反注册感应区域

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | name | str | 需要反注册的感应区域名 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 示例

```python
self.UnRegisterEntityAOIEvent(0, "test")
```



## SetUseLocalTime

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    让某个维度拥有自己的局部时间规则，开启后该维度可以拥有与其他维度不同的时间与是否昼夜更替的规则

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | value | bool | 是否开启局部时间规则 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 我们对主世界以及自定义维度新增了“局部时间规则”的概念。在此之前，所有的维度会共享一个“全局时间”，即设置时间或dodaynightcycle规则时，会对所有维度生效。
        现在，我们可以将某个维度使用局部时间规则，并且单独设置他的时间（见[SetLocalTime](#setlocaltime)）与dodaynightcycle规则（见[SetLocalDoDayNightCycle](#setlocaldodaynightcycle)）。
        在下文中，我们会将使用局部时间规则的维度称为“局部维度”，而使用全局时间的维度称为“全局维度”。默认情况下，维度都是全局维度。
        原版的time指令，gamerule dodaylightcycle指令与开启昼夜更替的设置，daylock指令与终为白日的设置，均不会对局部维度生效。
        当世界上同时存在局部维度与全局维度时，只有以下两种情况可以睡觉来跳过黑夜：
        1. 所有玩家都在全局维度睡觉。这时会将全局时间跳到第二天早上。
        2. 所有玩家都在同一个局部维度睡觉。这时会将该局部维度的时间跳到第二天早上。
    - 启用局部时间规则时，默认继承全局的时间与昼夜更替规则
    - 时间规则对原版的下界与末地无效，这两个维度永远为黑夜且没有昼夜更替
    - 建议统一在游戏启动时调用
    - 在pc开发包下，可以在聊天栏键入`dmtime on`或`dmtime off`来测试开启与关闭当前维度的局部时间

- 示例

```python
self.SetUseLocalTime(3, True)
```



## GetUseLocalTime

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取某个维度是否设置了使用局部时间规则

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否使用局部时间规则 |

- 备注
    - 关于“局部时间规则”，见[SetUseLocalTime](#setuselocaltime)

- 示例

```python
self.GetUseLocalTime(3)
```



## SetLocalTime

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置使用局部时间规则维度的时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | time | int | 时间，单位为帧数。表示该存档从新建起经过的时间，而非当前游戏天内的时间。mc中一个游戏天相当于现实的20分钟，即24000帧 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 游戏有天数的概念，使用时需要进行考虑。您也可以直接使用[SetLocalTimeOfDay](#setlocaltimeofday)设置一天内所在的时间而不用计算天数。
    - 只有使用局部时间规则维度才能设置
    - 关于“局部时间规则”，见[SetUseLocalTime](#setuselocaltime)

- 示例

```python
# 获取当前的时间
passedTime = self.GetLocalTime(3)
# 获取当前的天数
day = passedTime / 24000
# 设置为当天的正午
self.SetLocalTime(3, day * 24000 + 6000)
# 设置为次日的日出
self.SetLocalTime(3, (day + 1) * 24000 + 0)
```



## SetLocalTimeOfDay

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置使用局部时间规则维度在一天内所在的时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | timeOfDay | int | 时间，单位为帧数，表示游戏天内的时间，范围为0到24000。mc中一个游戏天相当于现实的20分钟，即24000帧 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 具体的逻辑与time指令相同，若timeOfDay比当前时间晚，则设置到当天的timeOfDay；若timeOfDay比当前时间早，则设置到次日的timeOfDay
    - 在pc开发包下，可以在聊天栏键入`dmtime time <int:帧数>`来测试设置当前维度的局部时间

- 示例

```python
# 设置为正午
self.SetLocalTimeOfDay(3, 6000)
```



## GetLocalTime

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取维度的时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 时间，单位为帧数，表示该存档从新建起经过的时间，而非当前游戏天内的时间。mc中一个游戏天相当于现实的20分钟，即24000帧 |

- 备注
    - 维度使用局部时间规则时，返回局部时间；没有使用时返回全局时间
    - 关于“局部时间规则”，见[SetUseLocalTime](#setuselocaltime)

- 示例

```python
# 从游戏开始经过的总帧数
passedTime = self.GetLocalTime(3)
# 当前游戏天内的帧数
timeOfDay = passedTime % 24000
# 从游戏开始经过的游戏天数
day = passedTime / 24000
```



## SetLocalDoDayNightCycle

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置使用局部时间规则的维度是否打开昼夜更替

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | value | bool | 是否打开昼夜更替 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 只有使用局部时间规则维度才能设置
    - 关于“局部时间规则”，见[SetUseLocalTime](#setuselocaltime)
    - 在pc开发包下，可以在聊天栏键入`dmtime cycle on`或`dmtime cycle off`来测试开启与关闭当前维度的昼夜更替

- 示例

```python
self.SetLocalDoDayNightCycle(3, False)
```



## GetLocalDoDayNightCycle

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取维度是否打开昼夜更替

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否打开昼夜更替 |

- 备注
    - 维度使用局部时间规则时，返回维度自身的昼夜更替规则；没有使用时返回全局的昼夜更替规则
    - 关于“局部时间规则”，见[SetUseLocalTime](#setuselocaltime)

- 示例

```python
self.GetLocalDoDayNightCycle(3)
```



## CreateEffectComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建effect组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EffectComponentServer | effect组件实例 |



## RemoveEffectFromEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    为实体删除指定状态效果

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | effectName | str | 状态效果名称字符串，包括自定义状态效果和原版状态效果，原版状态效果可在wiki查询 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示删除成功 |

- 示例

```python
res = self.RemoveEffectFromEntity(entityId, "speed")
```



## AddEffectToEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    为实体添加指定状态效果，如果添加的状态已存在则有以下集中情况：1、等级大于已存在则更新状态等级及持续时间；2、状态等级相等且剩余时间duration大于已存在则刷新剩余时间；3、等级小于已存在则不做修改；4、粒子效果以新的为准

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | effectName | str | 状态效果名称字符串，包括自定义状态效果和原版状态效果，原版状态效果可在wiki查询 |
    | duration | int | 状态效果持续时间，单位秒 |
    | amplifier | int | 状态效果的额外等级。必须在0至255之间（含）。若未指定，默认为0。注意，状态效果的第一级（如生命恢复 I）对应为0，因此第二级状态效果，如生命回复 II，应指定强度为1。部分效果及自定义状态效果没有强度之分，如夜视 |
    | showParticles | bool | 是否显示粒子效果，True显示，False不显示 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示设置成功 |

- 示例

```python
res = self.AddEffectToEntity(entityId, "speed", 30, 2, True)
```



## GetEntityEffects

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体当前所有状态效果

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(dict) | 状态效果信息字典的list |

- 备注
    - 状态效果信息字典 effectDict
        | 关键字     | 数据类型              | 说明     |
        | ----------| --------------------- | ---------|
        | effectName | str | 状态效果名称 |
        | duration  | int | 状态效果剩余持续时间，单位秒 |
        | amplifier  | int | 状态效果额外等级 |

- 示例

```python
effectDictList = self.GetEntityEffects(entityId)
```



## CreateEngineTypeComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建engineType组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EngineTypeComponentServer或EngineTypeComponentClient | engineType组件实例 |



## GetEntityEngineTypeStr

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体的类型名称

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 实体类型名称，如minecraft:husk |

- 示例

```python
engineType = self.GetEntityEngineTypeStr(entityId)
```



## GetEntityEngineType

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体类型

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 详见<a href="../../../../../../mcdocs/1-ModAPI/枚举值/EntityType.html">EntityType枚举</a> |

- 示例

```python
entityType = self.GetEntityEngineType(entityId)
# 以判断是否是 Mob 为例，如果要判断是否为弹射物，找到对应的类型Projectile修改即可
if entityType & self.GetMinecraftEnum().EntityType.Mob == self.GetMinecraftEnum().EntityType.Mob:
    logger.info("{} is Mod".format(self.GetEngineTypeStr(entityId)))
```



## CreateEntityEventComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建entityEvent组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EntityEventComponentServer | entityEvent组件实例 |



## TriggerEntityCustomEvent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    触发生物自定义事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 生物Id |
    | eventName | str | 事件名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 触发苦力怕爆炸
        在苦力怕的entity json文件中`events`字段下增加如下事件,然后在mod中运行示例代码：
        ```json
        "netease:custom_exploading":{
                  "sequence": [
                    {
                      "filters": {
                    "test": "has_component",
                        "operator": "!=",
                        "value": "minecraft:is_charged"
                      },
                      "add": {
                        "component_groups": [
                          "minecraft:forced_exploding"
                        ]
                      }
                    },
                    {
                      "filters": {
                        "test": "has_component",
                        "value": "minecraft:is_charged"
                      },
                      "add": {
                        "component_groups": [
                          "minecraft:forced_charged_exploding"
                        ]
                      }
                    }
                  ]
                }
        ```

- 示例

```python
#触发entity自定义event
eventName = "netease:custom_exploading"
self.TriggerCustomEvent(entityId, eventName)
```



## CreateExtraDataComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建extraData组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id，不传则使用LevelId |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ExDataCompServer | extraData组件实例 |



## GetExtraData

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体的自定义数据或者世界的自定义数据，某个键所对应的值。获取实体数据传入对应实体id

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 自定义key |
    | entityId | str或int | 实体id，不传则使用LevelId |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | any | key对应的值 |

- 示例

```python
self.GetExtraData("globalMsg")
```



## SaveExtraData

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    用于保存实体的自定义数据或者世界的自定义数据

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id，不传则使用LevelId |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 保存结果 |

- 示例

```python
# 保存自定义数据
self.SaveExtraData()
```



## SetExtraData

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    用于设置实体的自定义数据或者世界的自定义数据，数据以键值对的形式保存。设置实体数据时使用对应实体id创建组件，设置世界数据时使用levelId创建组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 自定义key |
    | value | any | key对应的值，支持python基本数据类型 |
    | entityId | str或int | 实体id，不传则使用LevelId |
    | autoSave | bool | 默认自动保存，默认为True，如果批量设置数据，请将该参数设置为False，同时在设置数据完毕时调用SaveExtraData接口 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetExtraData("globalMsg", "helloWorld")
```



## CleanExtraData

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    清除实体的自定义数据或者世界的自定义数据，清除实体数据时使用对应实体id创建组件，清除世界数据时使用levelId创建组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 自定义key |
    | entityId | str或int | 实体id，不传则使用LevelId |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
suc = self.CleanExtraData("globalMsg")
print "CleanExtraData for level suc=%s" % suc
```



## GetWholeExtraData

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取完整的实体的自定义数据或者世界的自定义数据，获取实体数据时使用对应实体id创建组件，获取世界数据时使用levelId创建组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id，不传则使用LevelId |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict或None | 获取指定实体或者全局的额外存储数据字典，假如没有任何额外存储数据，那么返回None或者空字典 |

- 示例

```python
dataDict = self.GetWholeExtraData()
if dataDict:
    for key, value in dataDict.iteritems():
        print "key=%s value=%s" % (key, str(value))
```



## CreateExpComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建exp组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ExpComponentServer | exp组件实例 |



## GetPlayerExp

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取玩家当前等级下的经验值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |
    | isPercent | bool | 是否为百分比 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 玩家经验值 |

- 备注
    - 如果设置返回百分比为False，则返回玩家当前等级下经验的绝对值（非当前玩家总经验值）。

- 示例

```python
print(self.GetPlayerExp(playerId, False))
```



## AddPlayerExp

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    增加玩家经验值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |
    | exp | int | 玩家经验值，可设置负数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 如果设置的exp值为负数，且超过当前等级已有的经验值，调用接口后，该玩家等级不会下降但是经验值会置为最小值

- 示例

```python
self.AddPlayerExp(entityId, 25)
```



## GetPlayerTotalExp

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取玩家的总经验值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 总经验值，正整数。获取失败的情况下返回-1。 |

- 示例

```python
print(self.GetPlayerTotalExp(playerId))
```



## SetPlayerTotalExp

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置玩家的总经验值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |
    | exp | int | 总经验值，正整数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 根据总经验值会重新计算等级，该接口可引起等级的变化
    - 内部运算采用浮点数，数值较大时会出现误差

- 示例

```python
self.SetPlayerTotalExp(playerId, 25)
```



## GetOrbExperience

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取经验球的经验

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 经验球实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 经验值，正整数。获取失败的情况下返回-1。 |

- 示例

```python
print(self.GetOrbExperience(entityId))
```



## SetOrbExperience

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置经验球经验

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 经验球实体id |
    | exp | int | 经验球经验 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 设置经验球经验，entityId是经验球的entityId,如果经验小于等于0，拾取后不再加经验

- 示例

```python
self.SetOrbExperience(entityId, 25)
```



## CreateExperienceOrb

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建专属经验球

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | int | 专属玩家ID，只有该玩家可以拾取生成的经验球 |
    | exp | int | 经验球经验 |
    | position | tuple(float,float,float) | 创建的位置 |
    | isSpecial | bool | 是否专属经验球 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.CreateExperienceOrb(playerId, 25, (10,10,10), False)
```



## CreateExplosionComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建explosion组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ExplosionComponentServer | explosion组件实例 |



## CreateExplosion

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    用于生成爆炸

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 爆炸位置 |
    | radius | int | 爆炸威力，具体含义可参考[wiki](https://zh.minecraft.wiki/w/%E7%88%86%E7%82%B8)对爆炸的解释 |
    | fire | bool | 是否带火 |
    | breaks | bool | 是否破坏方块 |
    | sourceId | str | 爆炸伤害源的实体id |
    | playerId | str | 爆炸创造的实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.CreateExplosion((50,50,50),10,True,True,sourceId,playerId)
```



## CreateFeatureComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建feature组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | FeatureCompServer | feature组件实例 |



## AddNeteaseFeatureWhiteList

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    添加结构对PlaceNeteaseStructureFeatureEvent事件的脚本层监听

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | structureName | str | 结构的identifier |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否增加成功 |

- 示例

```python
# 注意structureName格式为floderName:structureName
self.AddNeteaseFeatureWhiteList("test:pumpkins")
```



## RemoveNeteaseFeatureWhiteList

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    移除structureName对PlaceNeteaseStructureFeatureEvent事件的脚本层监听

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | structureName | str | 结构名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否移除成功 |

- 示例

```python
# 注意structureName格式为floderName:structureName
self.RemoveNeteaseFeatureWhiteList("test:pumpkins")
```



## ClearAllNeteaseFeatureWhiteList

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    清空所有已添加Netease Structure Feature对PlaceNeteaseStructureFeatureEvent事件的脚本层监听

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否清空成功 |

- 示例

```python
self.ClearAllNeteaseFeatureWhiteList()
```



## LocateStructureFeature

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    与[/locate指令](https://zh.minecraft.wiki/w/%E5%91%BD%E4%BB%A4/locate)相似，用于定位原版的部分结构，如海底神殿、末地城等。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | featureType | int | 原版的结构类型，<a href="../../../../../../mcdocs/1-ModAPI/枚举值/StructureFeatureType.html">StructureFeatureType</a>枚举 |
    | dimensionId | int | 结构所在维度，**要求该维度已加载** |
    | pos | tuple(int,int,int) | 以该位置为中心来查找最近的结构 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float)或None | 最近的结构所在区块位置(x坐标,z坐标)，y坐标不定，若定位失败则返回None |

- 备注
    - 定位失败通常是由于该维度不存在、该维度未加载、该维度中不存在该结构、该结构距离传入位置过远等
    - 该接口返回值为对应结构所在区块的坐标，与结构实际生成位置可能相距一定距离

- 示例

```python
pos = self.LocateStructureFeature(self.GetMinecraftEnum().StructureFeatureType.Village, 0, (0, 64, 0))
```



## LocateNeteaseFeatureRule

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    与[/locate指令](https://zh.minecraft.wiki/w/%E5%91%BD%E4%BB%A4/locate)相似，用于定位<a href="../../../../15-自定义游戏内容/4-自定义维度/4-自定义特征.html#特征规则（feature-rules）" rel="noopenner"> 网易自定义特征规则 </a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | ruleName | str | 特征规则名称，形式为namespace:featureRuleIdentifier，如custombiomes:overworld_pumpkins_feature_rule |
    | dimensionId | int | 查找维度，**要求该维度已加载** |
    | pos | tuple(int,int,int) | 以该位置为中心来查找满足网易自定义特征规则分布条件的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float)或None | 最近的满足网易自定义特征规则分布条件的坐标，定位失败则返回None |

- 备注
    - 定位失败通常是由于传入维度不存在、维度未加载、没有满足该自定义特征规则分布条件的坐标、目标坐标距离传入位置过远（以该位置为中心，半径100个区块内无法找到）等
    - 若在feature rules中"conditions"内的"minecraft:biome_filter"中**填写了判断维度以外的过滤规则，将有概率无法定位到满足该自定义特征规则分布条件的坐标**。建议开发者在"distribution"的"iterations"中使用query.is_biome代替
    - 定位原理是根据网易自定义特征规则分布条件寻找可能的位置，因此**有可能会定位到在PlaceNeteaseStructureFeatureEvent事件中被取消生成的结构位置**。开发者应注意甄别，尽量避免对可能在PlaceNeteaseStructureFeatureEvent事件中被取消放置的结构对应特征规则文件调用定位函数

- 示例

```python
pos = self.LocateNeteaseFeatureRule("custombiomes:overworld_pumpkins_feature_rule", 0, (0, 64, 0))
```



## CreateFlyComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建fly组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | FlyComponentServer | fly组件实例 |



## IsPlayerFlying

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取玩家是否在飞行

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:是 False:否 |

- 示例

```python
self.IsPlayerFlying(playerId)
```



## ChangePlayerFlyState

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    给予/取消飞行能力，并且进入飞行/非飞行状态

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |
    | isFly | bool | 飞行状态，True：飞行模式，False：正常行走模式 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:是 False:否 |

- 示例

```python
self.ChangePlayerFlyState(playerId, True)
```



## CreateGameComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建game组件

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | GameComponentServer或GameComponentClient | game组件实例 |



## AddBlockProtectField

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置一个方块无法被玩家/实体破坏的区域

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 不可破坏区域所在维度 |
    | startPos | tuple(int,int,int) | 初始位置，不可破坏区域AABB包围盒的最小点 |
    | endPos | tuple(int,int,int) | 结束位置，不可破坏区域AABB包围盒的最大点 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 成功时返回区域的唯一ID，可用于取消不可破坏区域，失败时返回-1 |

- 示例

```python
field = self.AddBlockProtectField(0, (-20, 0, -20), (20, 255, 20))
if field > 0:
    print "AddBlockProtectField success field={}".format(field)
else:
    print "AddBlockProtectField fail"
```



## RemoveBlockProtectField

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    取消一个方块无法被玩家/实体破坏的区域

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | field | int | 不可破坏区域的唯一ID，AddBlockProtectField的返回值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | success True为取消成功，False为取消失败 |



## CleanBlockProtectField

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    取消全部已设置的方块无法被玩家/实体破坏的区域

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | success True为取消成功，False为取消失败 |



## KillEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    杀死某个Entity

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 要杀死的目标的entityId |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否杀死成功 |

- 示例

```python
self.KillEntity(entityId)
```



## CreateEngineEntityByTypeStr

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建指定identifier的实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | engineTypeStr | str | 实体identifier，例如'minecraft:husk' |
    | pos | tuple(float,float,float) | 生成坐标 |
    | rot | tuple(float,float) | （上下角度，左右角度）实体水平方向的俯仰角度和竖直方向的旋转角度，单位是角度而不是弧度。<a href="../../../../10-基本概念/10-Vector3.html">MC坐标系说明</a> |
    | dimensionId | int | 生成的维度，默认值为0（0为主世界，1为地狱，2为末地） |
    | isNpc | bool | 是否为npc，默认值为False。npc不会移动、转向、存盘。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str或None | 实体Id或者None |

- 备注
    - 在未加载的chunk无法创建
        生成村民请使用"minecraft:villager_v2"

- 示例

```python
self.CreateEngineEntityByTypeStr('minecraft:husk', (0, 5, 0), (0, 0), 0)
```



## PlaceStructure

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    放置结构

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 放置结构的位置 |
    | structureName | str | 结构名称 |
    | dimensionId | int | 希望放置结构的维度，可在对应维度的常加载区块放置结构，默认为-1 |
    | rotation | int | 放置结构的旋转角度，默认为0(只可旋转90，180，270度) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否放置成功，True为放置成功，False为放置失败 |

- 备注
    - 放置时需要确保所放置的区块都已加载，否则会放置失败或者部分缺失
    - 该接口是同步执行的，请勿在一帧内放置大量结构，会造成游戏卡顿

- 示例

```python
self.PlaceStructure((100, 70, 100), "test:structureName", 0)
```



## AddTimer

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    添加定时器，非重复

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | delay | float | 延迟时间，单位秒 |
    | func | function | 定时器触发函数 |
    | *args | any | 变长参数，可以不设置 |
    | **kwargs | any | 字典变长参数，可以不设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | CallLater | 返回单次触发的定时器实例 |



## AddRepeatedTimer

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    添加服务端触发的定时器，重复执行

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | delay | float | 延迟时间，单位秒 |
    | func | function | 定时器触发函数 |
    | *args | any | 变长参数，可以不设置 |
    | **kwargs | any | 字典变长参数，可以不设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | CallLater | 返回触发的定时器实例 |



## CancelTimer

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    取消定时器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | timer | CallLater | AddTimer和AddRepeatedTimer时返回的定时器实例 |

- 返回值

    无



## GetEntitiesInArea

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取区域内的entity列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | startPos | tuple(int,int,int) | 初始位置 |
    | endPos | tuple(int,int,int) | 结束位置 |
    | dimensionId | int | 区域所在维度，仅服务端有效，可获取对应维度的常加载区块内的实体列表 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 返回entityId的list |

- 示例

```python
self.GetEntitiesInSquareArea((0,0,0), (100,100,100), 0)
```



## GetEntitiesAround

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取区域内的entity列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 某个entityId |
    | radius | int | 正方体区域半径 |
    | filters | dict | 过滤设置字典 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 返回entityId的list |

- 示例

```python
#利用过滤器获取玩家身边的entity
#样例中的过滤器表示满足“是玩家”或者“没有头戴南瓜帽”的entity
filters = {
    "any_of": [
        {
            "subject" : "other",
            "test" :  "is_family",
            "value" :  "player"
        },
        {
            "test" :  "has_equipment",
            "domain": "head",
            "subject" : "other",
            "operator" : "not",
            "value" : "carved_pumpkin"
        }
    ]
}
self.GetEntitiesAround(entityId, 100, filters)
```



## ShowHealthBar

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置是否显示血条

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | show | bool | True为显示。开启后可用health组件单独设置某个实体的血条颜色及是否显示 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.ShowHealthBar(True)
```



## SetNameDeeptest

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置名字是否透视

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | deeptest | bool | True为不透视。默认情况下为透视 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 设置为不透视
self.SetNameDeeptest(True)
```



## GetScreenSize

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取游戏分辨率

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 宽高（像素） |

- 示例

```python
width, height = self.GetScreenSize()
```



## SetRenderLocalPlayer

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置本地玩家是否渲染

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | render | bool | True为渲染 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 不渲染本地玩家
self.SetRenderLocalPlayer(False)
```



## AddPickBlacklist

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    添加使用camera组件选取实体时的黑名单，即该实体不会被选取到

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 添加黑名单
self.AddPickBlacklist(entityId)
```



## ClearPickBlacklist

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    清除使用camera组件选取实体的黑名单

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 清除黑名单中所有实体
self.ClearPickBlacklist()
```



## CheckWordsValid

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    检查语句是否合法，即不包含敏感词

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | words | str | 语句 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:语句合法<br>False:语句非法 |

- 示例

```python
isValid = self.CheckWordsValid("creeper? Aww man")
```



## CheckNameValid

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    检查昵称是否合法，即不包含敏感词

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 昵称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:昵称合法 False:昵称非法 |

- 示例

```python
isValid = self.CheckNameValid("史蒂夫")
```



## GetScreenViewInfo

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取游戏视角信息。分辨率为1313，618时，画布是376，250的2倍，所以viewport得到的是1313 + (2-(1313%2))，y值类似，可参考<a href="../../../../../18-界面与交互/1-界面编辑器使用说明.html#《我的世界》界面适配方法" rel="noopenner"> 《我的世界》界面适配方法 </a>

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float,float) | 依次为宽、高、x偏移、y偏移 |

- 示例

```python
width, height, offsetX, offsetY= self.GetScreenViewInfo()
```



## SimulateTouchWithMouse

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    模拟使用鼠标控制UI（PC F11快捷键）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | touch | bool | True:进入鼠标模式，False:退出鼠标模式 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 模拟结果 |

- 示例

```python
self.SimulateTouchWithMouse(True)
```



## GetCurrentDimension

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取客户端当前维度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 维度id。客户端未登录完成或正在切维度时返回-1 |

- 示例

```python
dimId = self.GetCurrentDimension()
```



## GetChinese

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取langStr对应的中文，可参考PC开发包中\handheld\bed-loc\handheld\data\resource_packs\vanilla\texts\zh_CN.lang

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | langStr | str | 传入的langStr |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | langStr对应的中文，若找不到对应的中文，则会返回langStr本身 |

- 示例

```python
# 获取"entity.wolf.name"对应的中文（"狼"）
Chinese = self.GetChinese("entity.wolf.name")
```



## SetDisableHunger

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置是否屏蔽饥饿度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isDisable | bool | 是否屏蔽饥饿度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 如需隐藏饥饿度请使用extraClientApi的HideHungerGui

- 示例

```python
self.SetDisableHunger(True)
```



## SetOneTipMessage

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    在具体某个玩家的物品栏上方弹出tip类型通知，位置位于popup类型通知上方，此功能更建议在客户端使用game组件的对应接口SetTipMessage

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 具体玩家Id |
    | message | str | 消息内容,可以在消息前增加extraServerApi.GenerateColor("RED")字符来设置颜色，具体参考样例 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# playerId 变量改为具体的玩家Id
self.SetOneTipMessage(playerId, serverApi.GenerateColor("RED") + "tip提示")
```



## SetPopupNotice

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    在物品栏上方弹出popup类型通知，位置位于tip类型消息下方，服务端调用是针对全体玩家，客户端调用只影响本地玩家

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | message | str | 消息内容,可以在消息前增加extraClientApi.GenerateColor("RED")字符来设置颜色，具体参考样例 |
    | subtitle | str | 消息子标题内容,效果同message，也可设置颜色，位置位于message上方 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.SetPopupNotice(clientApi.GenerateColor("RED") + "消息通知", "消息子标题")
```



## SetTipMessage

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    在物品栏上方弹出tip类型通知，位置位于popup类型通知上方，服务端调用是针对全体玩家，客户端调用只影响本地玩家

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | message | str | 消息内容,可以在消息前增加extraServerApi.GenerateColor("RED")字符来设置颜色，具体参考样例 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.SetTipMessage(serverApi.GenerateColor("RED") + "tip提示")
```



## SetNotifyMsg

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置消息通知

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | msg | str | 消息内容 |
    | color | str | ColorCode，默认为白色 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.SetNotifyMsg("消息通知", self.GetMinecraftEnum().ColorCode.BLUE))
```



## GetPlayerGameType

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取指定玩家的游戏模式

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/GameType.html">GameType枚举</a> |

- 示例

```python
gameType = self.GetPlayerGameType(playerId)
```



## HasEntity

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    判断 entity 是否存在

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 0表示不存在，1表示存在 |

- 示例

```python
exist = self.HasEntity(entityId)
```



## IsEntityAlive

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    判断生物实体是否存活或非生物实体是否存在

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | false表示生物实体已死亡或非生物实体已销毁，true表示生物实体存活或非生物实体存在 |

- 备注
    - 注意，如果检测的实体所在的区块被卸载，则该接口返回False。因此，需要注意实体所在的区块是否被加载。
    - 区块卸载：游戏只会加载玩家周围的区块，玩家移动到别的区域时，原来所在区域的区块会被卸载，参考[区块介绍](https://zh.minecraft.wiki/w/%E5%8C%BA%E5%9D%97)

- 示例

```python
alive = self.IsEntityAlive(entityId)
```



## CreateGravityComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建gravity组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | GravityComponentServer | gravity组件实例 |



## GetEntityGravity

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体的重力因子，当生物重力因子为0时则应用世界的重力因子

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 重力因子 |

- 示例

```python
self.GetEntityGravity(entityId)
```



## SetEntityGravity

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置实体的重力因子，当生物重力因子为0时则应用世界的重力因子

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | gravity | float | 负数，表示每帧向下的速度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetEntityGravity(entityId, -0.08)
```



## CreateHurtComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建hurt组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | HurtCompServer | hurt组件实例 |



## SetHurtByEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    对实体造成伤害

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | attackerId | str | 伤害来源的实体id |
    | damage | int | 伤害值 |
    | byPassArmor | bool | 是否忽略护甲 |
    | knocked | bool | 实体是否被击退，可缺损，缺损时默认值为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |



## SetHurtByEntityNew

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    对实体造成伤害

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | damage | int | 伤害值 |
    | cause | str | 伤害来源，详见Minecraft枚举值文档的<a href="../../../../../../mcdocs/1-ModAPI/枚举值/ActorDamageCause.html">ActorDamageCause枚举</a> |
    | attackerId | str | 伤害来源的实体id，默认为None |
    | childAttackerId | str | 伤害来源的子实体id，默认为None，比如玩家使用抛射物对实体造成伤害，该值应为抛射物Id |
    | knocked | bool | 实体是否被击退，默认值为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |



## SetEntityImmuneDamage

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置实体是否免疫伤害（该属性存档）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | immune | bool | 是否免疫伤害 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetEntityImmuneDamage(entityId, True)
```



## CreateItemBannedComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建itembanned组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ItemBannedCompServer | itembanned组件实例 |



## AddBannedItem

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    增加禁用物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemName | str | 物品标识符，格式[namespace:name:auxvalue]，auxvalue默认为0，auxvalue为*时候匹配任意auxvalue值。例如：minecraft:egg（也可以通过填写配置文件config/banned_items.json进行启动禁用） |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否增加成功 |

- 示例

```python
self.AddBannedItem("minecraft:egg")
```



## GetBannedItemList

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取禁用物品列表

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str)或None | 禁用物品列表或者None(异常情况),list元素为物品标识符,格式[namespace:name:auxvalue]，auxvalue默认为0，auxvalue为*时候匹配任意auxvalue值。 |



## RemoveBannedItem

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    移除禁用物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemName | str | 物品标识符，格式[namespace:name:auxvalue]，auxvalue默认为0，auxvalue为*时候匹配任意auxvalue值。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否移除成功 |

- 示例

```python
self.RemoveBannedItem("minecraft:stained_glass:2")
```



## ClearBannedItems

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    清空禁用物品

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否清空成功 |



## CreateItemComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建item组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ItemCompServer或ItemCompClient | item组件实例 |



## GetItemBasicInfo

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取物品的基础信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemName | str | item的identifier |
    | auxValue | int | 物品的附加值auxvalue，默认为0 |
    | isEnchanted | bool | 是否附魔，默认为False。用于返回的idAux |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 基础信息字典，见备注 |

- 备注
    - auxValue默认值是0，可以不设置。如果物品不存在，返回值为None
        | 关键字     | 数据类型              | 说明     |
        | ----------| --------------------- | ---------|
        | itemName       | str | 本地化的物品名字 |
        | maxStackSize |int| 物品最大堆叠数目 |
        | maxDurability |int| 物品最大耐久值 |
        | idAux |int| 主要用于客户端的ui绑定，详见客户端接口 |
        | tierDict |dict| 自定义方块定义的挖掘相关的属性 netease:tier,没有设置时返回None |
        | itemCategory |str| 创造栏分类 |
        | itemType |str| 物品类型 |
        | itemTierLevel |int| 工具等级 |
    - 自定义物品的itemCategory值为json文件中的category字段值，客户端读取resource包的json文件，服务端读取behavior包中的json文件，两个json文件中的category字段需要保持一致，否则会报错
    - 创造栏分类说明
        | 创造栏分类 | 意义 |
        | --------- | -----|
        | construction | 建筑 |
        | nature | 自然 |
        | equipment | 装备 |
        | items | 物品 |
        | custom | 自定义 |
        | 空字符串 | 不在创造栏 |
    - 物品类型，值为空字符串或者下列类型名之一:
        | 类型名 | 意义 |
        | ----- | ----- |
        | book | 书 |
        | sword | 剑 |
        | shears | 剪刀 |
        | axe | 斧头 |
        | clock | 时钟 |
        | bucket | 桶 |
        | fishing_rod | 钓鱼竿 |
        | hoe | 锄头 |
        | shovel | 锹 |
        | pickaxe | 镐 |
        | dye | 骨粉 |
    - 工具等级代表不同的材质，没有工具等级时为值-1，工具等级与材质对应关系如下
        | 工具等级 | 材质 |
        | ------- | ---- |
        | 0 | 木制/金制工具 |
        | 1 | 石制工具 |
        | 2 | 铁制工具 |
        | 3 | 钻石工具 |

- 示例

```python
self.GetItemBasicInfo("minecraft:bow")
```



## GetLocalPlayerId

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取本地玩家的id

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 客户端玩家Id |



## ClearPlayerOffHand

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    清除玩家左手物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.ClearPlayerOffHand(playerId)
```



## GetPlayerItem

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取玩家物品，支持获取背包，盔甲栏，副手以及主手物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家ID |
    | posType | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/ItemPosType.html">ItemPosType枚举</a> |
    | slotPos | int | 槽位，获取INVENTORY及ARMOR时需要设置，其他情况写0即可 |
    | getUserData | bool | 是否获取userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典" rel="noopenner"> 物品信息字典 </a>，没有物品则返回None |

- 示例

```python
self.GetPlayerItem(playerId, self.GetMinecraftEnum().ItemPosType.INVENTORY, 0)
```



## ChangePlayerItemTipsAndExtraId

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    修改玩家物品的自定义tips和自定义标识符

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家ID |
    | posType | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/ItemPosType.html">ItemPosType枚举</a> |
    | slotPos | int | 箱子槽位 |
    | customTips | str | 物品的自定义tips |
    | extraId | str | 物品的自定义标识符 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.ChangePlayerItemTipsAndExtraId(playerId, self.GetMinecraftEnum().ItemPosType.INVENTORY, 0, "自定义tips", "自定义标识符")
```



## AddEnchantToInvItem

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    给物品栏的物品添加附魔信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家ID |
    | slotPos | int | 物品栏槽位 |
    | enchantType | int | 附魔类型，可以查看枚举值文档 |
    | level | int | 附魔等级 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.AddEnchantToInvItem(playerId, 0, serverApi.GetMinecraftEnum().EnchantType.BowDamage, 2)
```



## GetInvItemEnchantData

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取物品栏的物品附魔信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家ID |
    | slotPos | int | 物品栏槽位 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(tuple(int,int)) | list中每个tuple由附魔类型(<a href="../../../../../../mcdocs/1-ModAPI/枚举值/EnchantType.html">EnchantType枚举</a>)和附魔等级组成。没有附魔则为空list |

- 示例

```python
self.GetInvItemEnchantData(playerId, 0)
```



## GetOffhandItem

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取左手物品的信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家ID |
    | getUserData | bool | 是否获取物品的userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典" rel="noopenner"> 物品信息字典 </a>，没有物品则返回None |

- 示例

```python
offhandData = self.GetOffhandItem(entityId)
```



## SetInvItemNum

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置玩家背包物品数目

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家ID |
    | slotPos | int | 物品栏槽位 |
    | num | int | 物品数目，可以通过设置数量为0来达到清除背包物品的效果 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetInvItemNum(playerId, 0, 10)
```



## SpawnItemToLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    生成物品掉落物，如果需要获取物品的entityId，可以调用服务端系统接口CreateEngineItemEntity

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | <a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典" rel="noopenner"> 物品信息字典 </a> |
    | dimensionId | int | 设置dimension |
    | pos | tuple(float,float,float) | 生成位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
itemDict = {
    'itemName': 'minecraft:bow',
    'count': 1,
    'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1),],
    'auxValue': 0,
    'customTips':'§c new item §r',
    'extraId': 'abc',
    'userData': {},
}
self.SpawnItemToLevel(itemDict, 0, (0,80,20))
# 当最大生成数量为 1 时，可以继续调用生成 2 个物品
self.SpawnItemToLevel(itemDict, 0, (0,80,20))
```



## SpawnItemToPlayerInv

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    生成物品到玩家背包

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | <a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典" rel="noopenner"> 物品信息字典 </a> |
    | playerId | str | 玩家id |
    | slotPos | int | 背包槽位(可选) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 当slotPos不设置时，当设置的数量超过单个槽位堆叠的上限时，会将多余的物品设置到另外的空闲槽位.如果生成的物品与背包中有的槽位的物品种类一致，该接口也会将物品增加到这些槽位中。注意：如果背包中剩余的物品数目和增加的物品数目之和大于64，则会生成物品数目到64，但是接口返回失败。

- 示例

```python
itemDict = {
    'itemName': 'minecraft:bow',
    'count': 1,
    'enchantData': [(self.GetMinecraftEnum().EnchantType.BowDamage, 1),],
    'auxValue': 0,
    'customTips':'§c new item §r',
    'extraId': 'abc',
    'userData': { },
}
self.SpawnItemToPlayerInv(itemDict, playerId, 0)
```



## SpawnItemToPlayerCarried

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    生成物品到玩家右手

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | <a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典" rel="noopenner"> 物品信息字典 </a> |
    | playerId | str | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
itemDict = {
    'itemName': 'minecraft:bow',
    'count': 1,
    'enchantData': [(self.GetMinecraftEnum().EnchantType.BowDamage, 1),],
    'auxValue': 0,
    'customTips':'§c new item §r',
    'extraId': 'abc',
    'userData': { },
}
self.SpawnItemToPlayerCarried(itemDict, playerId)
```



## GetCarriedItem

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取右手物品的信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | getUserData | bool | 是否获取物品的userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典" rel="noopenner"> 物品信息字典 </a>，没有物品则返回None |



## GetSlotId

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取当前手持的快捷栏的槽id

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 0到8 |

- 示例

```python
slotId = self.GetSlotId()
```



## GetItemFormattedHoverText

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取物品的格式化hover文本，如：§f灾厄旗帜§r

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemName | str | item的identifier |
    | auxValue | int | 物品的附加值auxValue，默认为不指定auxValue（0） |
    | showCategory | bool | 是否包括item的类别信息，默认False |
    | userData | dict | 物品userData，默认为None |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 物品的格式化hover文本 |

- 示例

```python
# 灾厄旗帜
self.GetItemFormattedHoverText("minecraft:banner", 15, True, {'Type': 1})
```



## GetItemHoverName

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取物品的hover名称，如：灾厄旗帜§r

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemName | str | item的identifier |
    | auxValue | int | 物品的附加值auxValue，默认为不指定auxValue（0） |
    | userData | dict | 物品userData，默认为None |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 物品hover名称 |

- 示例

```python
# 灾厄旗帜
self.GetItemHoverName("minecraft:banner", 15, {'Type': 1})
```



## GetItemEffectName

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取物品的状态描述，如：§7保护 0§r

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemName | str | item的identifier |
    | auxValue | int | 物品的附加值auxValue，默认为不指定auxValue（0） |
    | userData | dict | 物品userData，默认为None |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 物品的状态描述 |

- 示例

```python
# 灾厄旗帜
self.GetItemEffectName("minecraft:banner", 15, {'Type': 1})
```



## GetUserDataInEvent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    使物品相关客户端事件的<a href="../../../../10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典" rel="noopenner"> 物品信息字典 </a>参数带有userData。在mod初始化时调用即可

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 引擎事件名 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
# 这样调用之后，ActorAcquiredItemClientEvent事件的itemDict参数会带有userData字段
self.GetUserDataInEvent("ActorAcquiredItemClientEvent")
```



## ChangeItemTexture

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    替换物品的贴图，修改后所有用到该贴图的物品都会被改变，后续创建的此类物品也会被改变。会同时修改物品在UI界面上的显示，手持时候的显示与场景掉落的显示。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | identifier | str | 物品标识符，格式[namespace:name:auxvalue]，auxvalue默认为0 |
    | texturePath | str | 贴图路径 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否修改成功（因为采用延迟加载，此处返回成功不代表贴图路径正确，路径错误会导致渲染时贴图丢失显示异常） |

- 备注
    - 因为会同时修改用到此贴图的所有物品，所以使用的时候尽量谨慎，不建议改原版的物品，建议只用于修改用到自已定义的新贴图的物品。
    - 序列帧贴图物品暂不支持动态修改贴图
    - 部分物品有特殊逻辑无法修改：箱子，旗帜，生物头颅，盾牌，三叉戟，鱼杆

- 示例

```python
print(self.ChangeItemTexture("mytool:hatchet_1:0", "textures/items/hatchet_1"))
```



## CreateLvComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建lv组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | LevelComponentServer | lv组件实例 |



## GetPlayerLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取玩家等级

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 玩家等级 |

- 示例

```python
self.GetPlayerLevel(playerId)
```



## AddPlayerLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    修改玩家等级

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |
    | level | int | 玩家等级，可设置负数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.AddPlayerLevel(playerId, 2)
```



## CreateMobSpawnComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建mobSpawn组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | MobSpawnComponentServer | mobSpawn组件实例 |



## SpawnCustomModule

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置自定义刷怪

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | biomeType | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/BiomeType.html">BiomeType枚举</a> |
    | change | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/Change.html">Change枚举</a> |
    | entityType | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/EntityType.html">EntityType枚举</a> |
    | probability | int | 生成的权重[1, 10] |
    | minCount | int | 最小生成数量[0, 10] |
    | maxCount | int | 最大生成数量[0, 10] |
    | environment | int | 1:生成在表面；2:生成在水里 |
    | minBrightness | int | 生成该生物时的最小光照[1, 15]，不设置时使用默认值 |
    | maxBrightness | int | 生成该生物时的最大光照[1, 15]，不设置时使用默认值 |
    | minHeight | int | 生成该生物时最小的海拔高度[0, 256]，不设置时使用默认值 |
    | maxHeight | int | 生成该生物时最大的海拔高度[0, 256]，不设置时使用默认值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SpawnCustomModule(BiomeType.river,Change.Add,EntityType.Dolphin,10,1,10,2)
```



## CreateModAttrComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建modAttr组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ModAttrComponentServer或ModAttrComponentClient | modAttr组件实例 |



## SetEntityModAttr

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置属性值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | paramName | str | 属性名称，str的名称建议以mod命名为前缀，避免多个mod之间冲突 |
    | paramValue | any | 属性值，支持python基础数据 |

- 返回值

    无

- 备注
    - 注意：tuple、set在同步时会转成list。建议优先使用数字和字符串等非集合类型。

- 示例

```python
self.SetEntityModAttr(entityId, 'health', 1)
self.SetEntityModAttr(entityId, 'testDict', {'key':'value'})
```



## GetEntityModAttr

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取属性值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | paramName | str | 属性名称，str的名称建议以mod命名为前缀，避免多个mod之间冲突 |
    | defaultValue | any | 属性默认值，属性不存在时返回该默认值，此时属性值依然未设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | any | 返回属性值 |

- 备注
    - defaultValue不传的时候默认为None

- 示例

```python
# 如果直接修改GetAttr出来的集合类型，需要重新调用一遍SetAttr确保有进行更新
testDict = self.GetEntityModAttr(entityId, 'testDict')
testDict['key'] = 'newValue'
self.SetEntityModAttr(entityId, 'testDict', testDict)
```



## RegisterEntityModAttrUpdateFunc

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    注册属性值变换时的回调函数，当属性变化时会调用该函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | paramName | str | 监听的属性名称 |
    | func | function | 监听的回调函数 |

- 返回值

    无

- 备注
    - 回调函数需要接受一个参数，参数是dict，具体数据示例：{'oldValue': 0, 'newValue': 1, 'entityId': ’-433231231231‘}

- 示例

```python
# 这个entityId传的是所需要监听的对象的Id
self.RegisterEntityModAttrUpdateFunc(entityId, 'health', self.jumpingText)
# 当脚本层的health属性变化时则会调用self.jumpingText
def jumpingText(self, data):
    entityId = data['entityId']
    oldValue = data['oldValue']
    newValue = data['newValue']
```



## UnRegisterEntityModAttrUpdateFunc

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    反注册属性值变换时的回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | paramName | str | 监听的属性名称 |
    | func | function | 监听的回调函数 |

- 返回值

    无

- 备注
    - 需要传注册时的同一个函数作为参数

- 示例

```python
self.UnRegisterEntityModAttrUpdateFunc(entityId, 'health', self.jumpingText)
```



## CreateModelComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建model组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ModelComponentServer或ModelComponentClient | model组件实例 |



## SetEntityOpacity

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置生物模型的透明度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | opacity | float | 透明度值，取值范围为[0, 1]，值越小越透明 |

- 返回值

    无

- 示例

```python
self.SetEntityOpacity(entityId, 0.2)
```



## PlayEntityAnim

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    播放骨骼动画

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | aniName | str | 动画名称 |
    | isLoop | bool | 是否循环播放 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.PlayEntityAnim(entityId, "run", True)
```



## GetEntityModelId

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取骨骼模型的Id，主要用于特效绑定骨骼模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 当前骨骼模型实例的id |

- 示例

```python
modelId = self.GetEntityModelId(entityId)
```



## SetEntityModel

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置骨骼模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | modelName | str | 模型名称,值为""时重置模型 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetModel(entityId, "xuenv")
```



## ResetEntityModel

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    恢复实体为原版模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.ResetModel(entityId)
```



## BindModelToEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    实体替换骨骼模型后，再往上其他挂接骨骼模型。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | boneName | str | 挂接的骨骼名称 |
    | modelName | str | 要挂接的骨骼模型名称 |
    | offset | tuple(float,float,float) | 偏移量 |
    | rot | tuple(float,float,float) | 旋转 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 挂到骨骼上的骨骼模型的Id，失败返回-1 |

- 示例

```python
# 把名称为gun的骨骼模型挂接到rightHand骨骼上
gunModelId = self.BindModelToEntity(entityId, "rightHand", "gun")
```



## UnBindModelToEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    取消实体上挂接的某个骨骼模型。取消挂接后，这个modelId的模型便会销毁，无法再使用，如果是临时隐藏可以使用HideModel

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | modelId | int | 要取消挂接的骨骼模型的id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 取消挂接是否成功 |



## CreateMoveToComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建moveTo组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | MoveToComponentServer | moveTo组件实例 |



## SetEntityMoveSetting

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    寻路组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | pos | tuple(float,float,float) | 寻路目标位置 |
    | speed | float | 移动速度 |
    | maxIteration | int | 寻路算法最大迭代次数 默认200 |
    | callback | function | 寻路结束回调函数 |

- 返回值

    无

- 备注
    - 使用该接口时，需要在生物中配置有寻路的json组件。配置寻路json组件后，该接口会自动选择相应类型的寻路
        目前支持的寻路json组件包括：
        - minecraft:navigation.walk
            陆地寻路，与原版僵尸的寻路相同
        - minecraft:navigation.generic
            水陆寻路，支持陆地与水中，与原版溺尸的寻路相同
        - minecraft:navigation.climb
            陆地寻路，但是支持爬墙，与原版蜘蛛的寻路相同。这种寻路可能会被头顶方块阻挡，一直无法抵达目的地
        - minecraft:navigation.fly
            空中寻路，与原版鹦鹉的寻路相同
        以上的寻路都需要搭配一些其他json组件（例如movement）使用，具体可以参考NavigationMod的示例
        上面没有提到的navigation类型暂不支持，例如minecraft:navigation.float（如原版恶魂），minecraft:navigation.hover（如原版蜜蜂）
    - 不同的生物拥有不同的默认最大跟随距离，若要寻路的目标点距离大于此值引擎会拒绝寻路，要修改该距离可以通过在entity的json中配置.
        ```json
        {
          "format_version": "1.8.0",
          "minecraft:entity": {
              "components": {
                  "minecraft:follow_range": {
                    "value": 48,
                    "max": 48
                  }
              }
          }
        }
        ```
    - 关于maxIteration参数
        该参数会影响实际寻到路径的长度。若寻路算法迭代一定次数后，未寻到目标点，会返回局部最优解，即生物只会走到半路。

        在无大型障碍物的情况下，参数对应的参考寻路距离如下：该参数默认值200，最大值2000,请开发者根据实际情况选择。
        | maxIteration | 与目标点直线距离 |
        | ------------ | ---------------- |
        | 200          | 13               |
        | 500          | 20               |
        | 1000         | 30               |
        | 2000         | 43               |
    - 关于callback函数
        该函数需要接受两个参数，第一个参数为寻路的entityId，类型str，第二个参数为寻路结果，类型int

        （玩家获取到的位置比地面会高1.62格，若以玩家位置为目标点需要先把y轴减去1.62，否则callback会一直返回1）
        | 结果 | 说明                                                         |
        | ---- | ------------------------------------------------------------ |
        | -3   | 寻路失败，大于跟随距离，或者对正在寻路的飞行系生物使用       |
        | -2   | 寻路失败，生物没有寻路组件（指minecraft:navigation）         |
        | -1   | 寻路失败，参数错误，或生物不存在                             |
        | 0    | 寻路完成。到达设定的目标点                                   |
        | 1    | 寻路完成，但未到达目标点（可能由于maxIteration参数偏小）     |
        | 2    | 寻路中断。中途遇到障碍物被阻碍                               |
        | 3    | 寻路中断。被生物原版寻路行为覆盖，或寻路未结束时重复调用moveTo组件 |
    - demo简介：
        聊天栏输入walk/generic/climb/fly会原地生成一个使用对应navigation json组件的生物，然后跑到其他位置，再输入go，会将刚才生成的生物导航到玩家当前位置。
        这4种示例生物的行为json可以在NavigationMod_behavior/entities目录查看。
        4种示例生物的最大寻路距离都设置为了48格。

- 示例

```python
def myCallback(entityId, result):
    if result in (-1,-2,-3):
        self.LogError('[SetMoveSetting] failed')
    elif result==0:
        self.LogInfo('[SetMoveSetting] success')
    elif result in (1,2,3):
        self.LogError('[SetMoveSetting] terminated')

self.SetMoveSetting(entityId, (x,y,z),2.0,200,myCallback)
```



## CreateMsgComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建msg组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | MsgComponentServer | msg组件实例 |



## SendMsg

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    模拟玩家给所有人发送聊天栏消息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 发送者玩家的名字 |
    | msg | str | 消息内容 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - name参数需要设置玩家的名字(可通过name组件获取)，如果设置的玩家名字不存在，则随机找一个玩家发出该消息

- 示例

```python
self.SendMsg("playerName","test")
```



## SendMsgToPlayer

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    模拟玩家给另一个玩家发送聊天栏消息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fromEntityId | str | 发送者玩家ID |
    | toEntityId | str | 接受者玩家ID |
    | msg | str | 消息内容 |

- 返回值

    无

- 示例

```python
self.SendMsgToPlayer(fromEntityId, toEntityId, "test")
```



## NotifyOneMessage

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    给指定玩家发送聊天框消息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 指定玩家id |
    | msg | str | 消息内容 |
    | color | str | 颜色样式代码字符串，可参考wiki[样式代码](https://zh.minecraft.wiki/w/%E6%A0%B7%E5%BC%8F%E4%BB%A3%E7%A0%81)，默认为白色 |

- 返回值

    无

- 示例

```python
self.NotifyOneMessage(playerId, "test", "§c")
```



## CreateNameComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建name组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | NameComponentServer或NameComponentClient | name组件实例 |



## GetEntityName

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取生物的自定义名称，即使用命名牌或者SetName接口设置的名称

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 生物的自定义名称 |

- 示例

```python
name = self.GetEntityName(entityId)
```



## SetEntityName

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    用于设置生物的自定义名称，跟原版命名牌作用相同，玩家和新版流浪商人暂不支持

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | name | str | 名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetEntityName(entityId, "new Name")
```



## SetPlayerPrefixAndSuffixName

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置玩家前缀和后缀名字

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |
    | prefix | str | 前缀内容 |
    | prefixColor | str | 前缀内容颜色描述，可以使用GenerateColor接口传入参数 |
    | suffix | str | 后缀内容 |
    | suffixColor | str | 后缀内容颜色描述，可以使用GenerateColor接口传入参数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
color = self.GetMinecraftEnum().ColorCode.RED
self.SetPlayerPrefixAndSuffixName(playerId, "红队", color, '肉盾', color)
```



## SetEntityShowName

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置生物名字是否按照默认游戏逻辑显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | show | bool | True为显示 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 备注
    - 当设置为True时，生物的名字显示遵循游戏默认的渲染逻辑，即普通生物需要中心点指向生物才显示名字，玩家则是会一直显示名字

- 示例

```python
# 不显示头上的名字
self.SetEntityShowName(entityId, False)
```



## SetEntityAlwaysShowName

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置生物名字是否一直显示，瞄准点不指向生物时也能显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | show | bool | True为显示 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 备注
    - 该接口只对普通生物生效，对玩家设置不起作用

- 示例

```python
# 不显示头上的名字
self.SetEntityAlwaysShowName(entityId, False)
```



## CreatePersistenceComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建persistence组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PersistenceCompServer | persistence组件实例 |



## SetEntityPersistence

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置实体是否存盘

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | isPersistent | bool | True为存盘，False为不存盘 |

- 返回值

    无

- 备注
    - 实体默认都会存盘。设置为不存盘的实体，在区块卸载与退出游戏时不会存档。

- 示例

```python
self.SetEntityPersistence(entityId, True)
```



## CreatePetComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建pet组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PetComponentServer | pet组件实例 |



## DisablePet

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    关闭官方伙伴功能，单人游戏以及本地联机不支持该接口

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 关闭结果 |



## EnablePet

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    启用官方伙伴功能，单人游戏以及本地联机不支持该接口

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 启用结果 |



## CreatePlayerComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建player组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PlayerCompServer | player组件实例 |



## EnablePlayerKeepInventory

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置玩家死亡不掉落物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 实体id |
    | enable | bool | 是否开启“保留物品栏” |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.EnablePlayerKeepInventory(playerId, True)
```



## CreatePortalComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建portal组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PortalComponentServer | portal组件实例 |



## CreatePosComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建pos组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PosComponentServer或PosComponentClient | pos组件实例 |



## GetEntityPos

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 位置信息 |

- 备注
    - 对于非玩家，获取到的是脚底部位的位置
    - 对于玩家，如果处于行走，站立，游泳，潜行，滑翔状态，获得的位置比脚底位置高1.62；如果处于睡觉状态，获得的位置比最低位置高0.2



## GetEntityFootPos

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体脚所在的位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 位置信息 |



## SetEntityPos

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置实体位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | pos | tuple(int,int,int) | xyz值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 行为与使用tp命令一致，实体会瞬移到目标点
    - 对于所有类型的实体都是设置脚底位置，与[SetFootPos](#setfootpos)等价
    - 在床上时调用该接口会返回False

- 示例

```python
self.SetEntityPos(entityId, (1,2,3))
```



## SetEntityFootPos

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置实体脚底所在的位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | pos | tuple(float,float,float) | 实体脚所在的位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 行为与使用tp命令一致，实体会瞬移到目标点
    - 在床上时调用该接口会返回False

- 示例

```python
self.SetEntityFootPos(entityId, (0, 4, 0))
```



## CreateProjectileComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建projectile组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ProjectileComponentServer | projectile组件实例 |



## CreateProjectileEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建抛射物（直接发射）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | spawnerId | str | 创建者Id |
    | entityIdentifier | str | 创建抛射物的类别，如minecraft:snowball |
    | param | dict | 默认为None，详细说明请见备注 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 创建抛射物的Id，失败时为“-1” |

- 备注
    - param参数解释如下：
        | 参数              | 类型  | 解释                                                         |
        | ----------------- | ----- | ------------------------------------------------------------ |
        | position      | tuple(float,float,float) | 初始位置                                           |
        | direction     | tuple(float,float,float) | 初始朝向                                     |
        | power         | float   | 投掷的力量值            |
        | gravity       | float   | 抛射物重力因子，默认为json配置中的值 |
        | damage        | float   | 抛射物伤害值，默认为json配置中的值               |
        | targetId      | str     | 抛射物目标（指定了target之后，会和潜影贝生物发射的跟踪导弹的那个投掷物是一个效果），默认不指定                                |
        | isDamageOwner | bool    | 对创建者是否造成伤害，默认不造成伤害                                |

- 示例

```python
param = {
    'position': (1,1,1),
    'direction': (1,1,1)
}
self.CreateProjectileEntity(playerId, "minecraft:snowball", param)
```



## CreateRecipeComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建recipe组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | RecipeCompServer或RecipeCompClient | recipe组件实例 |



## GetRecipeResult

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    根据配方id获取配方结果。仅支持合成配方

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | recipeId | str | 配方id,对应配方json文件中的identifier字段 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(dict) | list的元素resultDict字典见备注 |

- 备注
    - resultDict字典内容如下
        | 关键字     | 数据类型              | 说明     |
        | ----------| --------------------- | ---------|
        | itemName  | str | 物品名称id |
        |auxValue| int | 物品附加值 |
        |num| int | 物品数目 |

- 示例

```python
self.GetRecipeResult(recipe1)
```



## GetRecipesByResult

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    通过输出物品查询配方所需要的输入材料

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | resultIdentifier | str | 输出物品的标识符 |
    | tag | str | 对应配方json中的tags字段里面的值 |
    | aux | int | 输出物品的附加值, 不传参的话默认为0 |
    | maxResultNum | int | 最大输出条目数，若大于等于0时，结果超过maxResultNum，则只返回maxResultNum条。默认-1，表示返回全部 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(dict) | 返回符合条件的配方列表 |

- 备注
    - 在获取酿造台配方时，不匹配tag标签与aux值，药水的identifier需要输入全称，例如：minecraft:potion_type:long_turtle_master，否则无法获取正确的配方。

- 示例

```python
print(self.GetRecipesByResult("minecraft:boat", "crafting_table", 4, -1))
```



## GetRecipesByInput

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    通过输入物品查询配方

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | inputIdentifier | str | 输入物品的标识符 |
    | tag | str | 对应配方json中的tags字段里面的值 |
    | aux | int | 输出物品的附加值, 不传参的话默认为0 |
    | maxResultNum | int | 最大输出条目数，若大于等于0时，结果超过maxResultNum，则只返回maxResultNum条。默认-1，表示返回全部 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(dict) | 返回符合条件的配方列表 |

- 备注
    - 在获取酿造台配方时，不匹配tag标签与aux值，药水的identifier需要输入全称，例如：minecraft:potion_type:long_turtle_master，否则无法获取正确的配方。
    - 需要遍历较多数据，不建议频繁调用

- 示例

```python
print(self.GetRecipesByInput("minecraft:log", "crafting_table", 0, -1))
```



## CreateRedStoneComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建redStone组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | RedStoneComponentServer | redStone组件实例 |



## CreateRideComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建ride组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | RideCompServer | ride组件实例 |



## CreateRotComponent

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建rot组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | RotComponentServer或RotComponentClient | rot组件实例 |



## GetEntityRot

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | （上下角度，左右角度）单位是角度而不是弧度 |



## SetEntityRot

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置实体的头的角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | rot | tuple(float,float) | 俯仰角度及绕竖直方向的角度，单位是角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 建议只用来设置本地玩家。如果设置其他生物，会被生物自身行为覆盖。

- 示例

```python
# 设为向上仰视45度，并朝向世界z轴正方向
self.SetEntityRot(entityId, (-45, 0))
```



## SetEntityLookAtPos

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置非玩家的实体看向某个位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | targetPos | tuple(float,float,float) | 要看向的目标位置 |
    | minTime | float | 凝视行为最短维持时间，单位为秒 |
    | maxTime | float | 凝视行为最长维持时间，单位为秒，最大值为60<br>实际行为维持时间将在minTime和maxTime之间取随机值 |
    | reject | bool | 在进行凝视行为时，是否禁止触发其他行为<br>True为禁止其他行为<br>False为允许其他行为（此时凝视行为可能表现不明显） |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功，True为成功，False为失败 |

- 备注
    - 调用本接口会打断该生物正在进行的行为，且该生物不会立刻看向目标位置，而是逐渐看向目标位置
    - 对部分不会转向的实体调用此接口，可能会返回失败或返回成功但实际无表现

- 示例

```python
# 设置该实体看向(0,78,0)这个位置，该凝视行为最少持续2秒，最多持续3秒，凝视过程中禁止触发其他行为
self.SetEntityLookAtPos(entityId, (0,78,0), 2, 3, True)
```



## GetBodyRot

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取实体的身体的角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 身体绕竖直方向的角度，单位是角度，如果没有身体，返回为0 |

- 示例

```python
y = self.GetBodyRot(entityId)
```



## LockLocalPlayerRot

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    在分离摄像机时，锁定本地玩家的头部角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | lock | bool | 传入True为锁定本地玩家头部角度<br>传入False为解锁本地玩家头部角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True：设置成功<br>False：设置失败 |

- 备注
    - 只能设置localplayer，即本地玩家自己
    - 玩家重生、切换维度时会重置头部角度
    - 锁定本地玩家头部角度时第一人称视角下可以旋转镜头，但玩家头部角度不会发生改变，下次切换到第一人称视角时镜头角度仍为锁定时的角度
    - 锁定本地玩家头部角度后，玩家划船时头部角度会尽量靠近锁定时的角度，若无法转到该角度，则会向左或向右看（视哪边距离目标角度更近而定）

- 示例

```python
# 分离摄像机
self.DepartCamera()
# 锁定本地玩家的头部角度
self.LockLocalPlayerRot(True)
```



## SetPlayerLookAtPos

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置本地玩家看向某个位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetPos | tuple(float,float,float) | 要看向的目标位置 |
    | pitchStep | float | 俯仰角方向旋转的角速度（每帧），最小为0.2 |
    | yawStep | float | 偏航角方向旋转的角速度（每帧），最小为0.2 |
    | blockInput | bool | 转向目标角度时是否屏蔽玩家操作，默认为True<br>True:屏蔽玩家操作，此时玩家无法转向、移动<br>False:不屏蔽玩家操作，此时如果玩家有移动、镜头转向操作将会打断通过本接口设置的转向 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功，True为成功，False为失败 |

- 备注
    - 当本地玩家未与摄像机分离时，调用本接口会导致摄像机一同看向指定位置<br>当本地玩家与摄像机分离时，调用本接口将只改变本地玩家模型的朝向

- 示例

```python
# 设置本地玩家以0.2度每帧的俯仰角速度、1度每帧的偏航角速度看向(0,78,0)这个位置，转向过程中屏蔽玩家操作
self.SetPlayerLookAtPos((0,78,0), 0.2, 1, True)
```



## CreateScaleComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建scale组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ScaleComponentServer | scale组件实例 |



## CreateTameComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建tame组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | TameComponentServer | tame组件实例 |



## CreateTimeComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建time组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | TimeComponentServer | time组件实例 |



## GetTime

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取当前世界时间

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 当前时间，单位为帧数，表示该存档从新建起经过的时间，而非当前游戏天内的时间。mc中一个游戏天相当于现实的20分钟，即24000帧 |

- 示例

```python
# 从游戏开始经过的总帧数
passedTime = self.GetTime()
# 当前游戏天内的帧数
timeOfDay = passedTime % 24000
# 从游戏开始经过的游戏天数
day = passedTime / 24000
```



## CreateWeatherComponent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建weather组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | WeatherComponentServer | weather组件实例 |



## CreateActorCollidableComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建actorCollidable组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ActorCollidableCompClient | actorCollidable组件实例 |



## CreateActorRenderComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建actorRender组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ActorRenderCompClient | actorRender组件实例 |



## CreateCustomAudioComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建customAudio组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | AudioCustomComponentClient | customAudio组件实例 |



## CreateBrightnessComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建brightness组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BrightnessCompClient | brightness组件实例 |



## SetEntityBrightness

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置实体的亮度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | brightness | float | 0：纯黑<br>1：正常亮度<br>1-14：较亮甚至纯白<br>超过14：通常为纯白，即使数值改变也没有明显变化 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:设置成功  False:设置失败 |

- 备注
    - 目前只支持修改替换了骨骼模型的实体亮度，使用游戏原生模型的实体暂不予支持。

- 示例

```python
success = self.SetEntityBrightness(entityId, 0.5)
```



## CreateCameraComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建camera组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | CameraComponentClient | camera组件实例 |



## PickFacing

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取准星选中的实体或者方块

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 选中目标的数据，详见备注 |

- 备注
    - 选中目标为实体时，返回值为：
        ```python
        {
            "type": "Entity",
            "entityId":  entityId
        }
        ```
    - 选中目标为方块时，返回值为：
        ```python
        {
            "type": "Block",
            "x":  x,
            "y":  y,
            "z":  z,
            "face": face
        }
        ```
    - 没有选中目标时，返回值为：
        ```python
        {
            "type": "None"
        }
        ```

- 示例

```python
pickData = self.PickFacing()
```



## CreateFogComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建fog组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | FogCompClient | fog组件实例 |



## CreateFrameAniControlComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建frameAniControl组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | frameEntityId | str或int | 序列帧实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | FrameAniControlComp | frameAniControl组件实例 |



## SetFrameAniLoop

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置序列帧是否循环播放，默认为否

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | frameEntityId | str或int | 序列帧实体id |
    | loop | bool | True表示循环播放 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 设置为循环播放
self.SetFrameAniLoop(frameEntityId, True)
```



## SetFrameAniFaceCamera

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置序列帧是否始终朝向摄像机，默认为是

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | frameEntityId | str或int | 序列帧实体id |
    | face | bool | True表示朝摄像机 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 设置为不始终朝摄像机
self.SetFaceCamera(frameEntityId, False)
```



## SetFrameAniDeepTest

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置序列帧是否透视，默认为否

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | frameEntityId | str或int | 序列帧实体id |
    | deepTest | bool | False表示透视，则被物体/方块阻挡时仍然能看到序列帧 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 设置为透视
self.SetDeepTest(frameEntityId, False)
```



## CreateFrameAniEntityBindComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建frameAniEntityBind组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | FrameAniEntityBindComp | frameAniEntityBind组件实例 |



## BindFrameAniToEntity

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    绑定entity

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | frameEntityId | int | 序列帧entity的ID |
    | bindEntityId | str | 绑定的entity的ID |
    | offset | tuple(float,float,float) | 绑定的偏移量 |
    | rot | tuple(float,float,float) | 绑定的旋转角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.BindFrameAniToEntity(frameEntityId, entityId, (0, 1, 0), (0, 0, 0))
```



## CreateFrameAniSkeletonBindComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建frameAniSkeletonBind组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | FrameAniSkeletonBindComp | frameAniSkeletonBind组件实例 |



## BindFrameAniToSkeleton

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    绑定骨骼模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | frameEntityId | int | 序列帧entity的ID |
    | modelId | int | 绑定的骨骼模型的ID（见model组件的GetModelId） |
    | boneName | str | 绑定具体骨骼的名称 |
    | offset | tuple(float,float,float) | 绑定的偏移量 |
    | rot | tuple(float,float,float) | 绑定的旋转角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.BindFrameAniToSkeleton(frameEntityId, modelId, "root", (0, 1, 0), (0, 0, 0))
```



## CreateFrameAniTransComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建frameAniTrans组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | FrameAniTransComp | frameAniTrans组件实例 |



## GetFrameAniPos

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取序列帧位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 位置信息 |



## GetFrameAniRot

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取序列帧的角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | （上下角度，左右角度）单位是角度而不是弧度 |



## GetFrameAniScale

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取序列帧的缩放

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 对于平面序列帧，第一个参数为贴图横向上的缩放，第二个参数为纵向上的缩放，第三个参数无用。对于环状序列帧，为三个坐标轴上的缩放 |



## SetFrameAniPos

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置序列帧位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | pos | tuple(int,int,int) | xyz值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |



## SetFrameAniRot

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置特效的角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | rot | tuple(float,float) | 俯仰角度及绕竖直方向的角度，单位是角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |



## SetFrameAniScale

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置序列帧的缩放

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | scale | tuple(float,float,float) | 对于平面序列帧，第一个参数为贴图横向上的缩放，第二个参数为纵向上的缩放，第三个参数无用。对于环状序列帧，为三个坐标轴上的缩放 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 横向拉伸为2倍，纵向不变
self.SetFrameAniScale(frameEntityId, (2, 1, 1))
```



## CreateHealthComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建health组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | HealthComponentClient | health组件实例 |



## ShowEntityHealth

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置某个entity是否显示血条，默认为显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | show | bool | 设置是否显示 |

- 返回值

    无

- 备注
    - 必须先设置ShowHealthBar

- 示例

```python
# 设置该entity不显示血条
self.ShowHealth(entityId, False)
```



## CreateOperationComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建operation组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | OperationCompClient | operation组件实例 |



## SetCanAll

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    同时设置SetCanMove，SetCanJump，SetCanAttack，SetCanWalkMode，SetCanPerspective，SetCanPause，SetCanChat，SetCanScreenShot，SetCanOpenInv，SetCanDrag，SetCanInair

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | flag | bool | True为全部响应 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 要在其他属性设置之前设置，不然在all之前设置的会被覆盖掉

- 示例

```python
# 全部设置为不响应
self.SetCanAll(False)
```



## CreateDeviceComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建device组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | DeviceCompClient | device组件实例 |



## CreateParticleControlComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建particleControl组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ParticleControlComp | particleControl组件实例 |



## CreateParticleEntityBindComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建particleEntityBind组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ParticleEntityBindComp | particleEntityBind组件实例 |



## BindParticleToEntity

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    粒子特效绑定entity

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | particleId | int | 特效ID |
    | bindEntityId | str | 绑定的entity的ID |
    | offset | tuple(float,float,float) | 绑定的偏移量，相对绑定entity脚下中心 |
    | rot | tuple(float,float,float) | 绑定的旋转角度 |
    | correction | bool | 默认不开启，开启后可以使特效的旋转角度准确设置为参照玩家的相对角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.BindParticleToEntity(particleId, entityId, (0, 1, 0), (0, 0, 0))
```



## CreateParticleSkeletonBindComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建particleSkeletonBind组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ParticleSkeletonBindComp | particleSkeletonBind组件实例 |



## BindParticleToSkeleton

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    绑定粒子特效到骨骼模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | particleId | int | 特效ID |
    | modelId | int | 绑定的骨骼模型的ID（见model组件的GetModelId） |
    | boneName | str | 绑定具体骨骼的名称 |
    | offset | tuple(float,float,float) | 绑定的偏移量 |
    | rot | tuple(float,float,float) | 绑定的旋转角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.BindParticleToEntity(particleId, modelId, "root", (0, 1, 0), (0, 0, 0))
```



## CreateParticleTransComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建particleTrans组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ParticleTransComp | particleTrans组件实例 |



## GetParticlePos

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取特效位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 位置信息 |



## GetParticleRot

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取特效角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | （上下角度，左右角度）单位是角度而不是弧度 |



## SetParticlePos

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置特效位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | pos | tuple(int,int,int) | xyz值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |



## SetParticleRot

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置特效的角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |
    | rot | tuple(float,float) | 俯仰角度及绕竖直方向的角度，单位是角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |



## CreatePlayerViewComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建playerView组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PlayerViewCompClient | playerView组件实例 |



## GetPlayerPerspective

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    获取当前的视角模式

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 0：第一人称视角；1：第三人称视角；2：前视第三人称视角 |

- 示例

```python
persp = self.GetPlayerPerspective(playerId)
```



## SetPlayerPerspective

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    设置视角模式

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 实体id |
    | persp | int | 0：第一人称视角；1：第三人称视角；2：前视第三人称视角 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.SetPlayerPerspective(playerId, 1)
```



## LockPlayerPerspective

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    锁定玩家的视角模式

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str或int | 实体id |
    | persp | int | 0：第一人称视角；1：第三人称视角；2：前视第三人称视角 其他值：解除锁定 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否锁定成功 |

- 示例

```python
self.LockPlayerPerspective(playerId, 1)
```



## CreateQueryVariableComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建queryVariable组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | QueryVariableComponentClient | queryVariable组件实例 |



## CreateSkyRenderComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建skyRender组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | SkyRenderCompClient | skyRender组件实例 |



## CreateTextBoardComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建textBoard组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | TextBoardComponentClient | textBoard组件实例 |



## CreateTextNotifyClientComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建textNotifyClient组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | TextNotifyComponet | textNotifyClient组件实例 |



## CreateConfigClientComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建config组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | levelId | str | 存档Id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ConfigCompClient | config组件实例 |



## CreateVirtualWorldComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建virtualWorld组件实例组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | levelId | str | 存档Id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | VirtualWorldCompClient | virtualWorld组件实例 |



## CreatePlayerAnimComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建玩家动画组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家Id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PlayerAnimCompClient | 玩家动画组件实例 |



## CreatePostProcessComponent

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.SdkInterface.SdkInterface

- 描述

    创建PostProcess组件

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | PostProcessComponent | 后处理效果组件实例 |



