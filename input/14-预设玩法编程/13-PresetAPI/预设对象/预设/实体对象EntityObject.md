---
sidebarDepth: 1
---
# 实体对象EntityObject



## 概述

- 继承关系

```mermaid
classDiagram
SdkInterface <|-- EntityObject
link SdkInterface "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/SDK%E6%8E%A5%E5%8F%A3%E5%B0%81%E8%A3%85SdkInterface.html"
EntityObject: 实体对象
SdkInterface: SDK接口封装
SdkInterface: (点击跳转)
```

- 描述

    EntityObject（实体对象）是对实体对象封装的基类，它为实体提供了面向对象的使用方式。

- 成员变量

    无



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetPos](#getpos) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取实体位置 |
| [GetFootPos](#getfootpos) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取实体脚所在的位置 |
| [SetPos](#setpos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体位置 |
| [SetFootPos](#setfootpos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体脚底所在的位置 |
| [GetRot](#getrot) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取实体角度 |
| [SetRot](#setrot) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置实体的头的角度 |
| [GetEngineTypeStr](#getenginetypestr) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取实体的类型名称 |
| [GetEngineType](#getenginetype) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取实体类型 |
| [GetModelId](#getmodelid) | <span style="display:inline;color:#7575f9">客户端</span> | 获取骨骼模型的Id，主要用于特效绑定骨骼模型 |
| [PlayAnim](#playanim) | <span style="display:inline;color:#7575f9">客户端</span> | 播放骨骼动画 |
| [SetAnimSpeed](#setanimspeed) | <span style="display:inline;color:#7575f9">客户端</span> | 设置某个骨骼动画的播放速度 |
| [GetAnimLength](#getanimlength) | <span style="display:inline;color:#7575f9">客户端</span> | 获取某个骨骼动画的长度，单位为秒 |
| [SetBrightness](#setbrightness) | <span style="display:inline;color:#7575f9">客户端</span> | 设置实体的亮度 |
| [SetOpacity](#setopacity) | <span style="display:inline;color:#7575f9">客户端</span> | 设置生物模型的透明度 |
| [GetHealth](#gethealth) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体预设的生命值 |
| [SetHealth](#sethealth) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体预设的生命值 |
| [GetMaxHealth](#getmaxhealth) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体预设的最大生命值 |
| [SetMaxHealth](#setmaxhealth) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体预设的最大生命值 |
| [GetSpeed](#getspeed) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体预设的速度 |
| [SetSpeed](#setspeed) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体预设的速度 |
| [GetMaxSpeed](#getmaxspeed) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体预设的最大速度 |
| [SetMaxSpeed](#setmaxspeed) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体预设的最大速度 |
| [GetDamage](#getdamage) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体预设的伤害 |
| [SetDamage](#setdamage) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体预设的伤害 |
| [GetMaxDamage](#getmaxdamage) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体预设的最大伤害 |
| [SetMaxDamage](#setmaxdamage) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体预设的最大伤害 |
| [ShowHealth](#showhealth) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否显示血条，默认为显示 |
| [SetAttackTarget](#setattacktarget) | <span style="display:inline;color:#ff5555">服务端</span> | 设置仇恨目标 |
| [ResetAttackTarget](#resetattacktarget) | <span style="display:inline;color:#ff5555">服务端</span> | 清除仇恨目标 |
| [GetAttackTarget](#getattacktarget) | <span style="display:inline;color:#ff5555">服务端</span> | 获取仇恨目标 |
| [SetKnockback](#setknockback) | <span style="display:inline;color:#ff5555">服务端</span> | 设置击退的初始速度，需要考虑阻力的影响 |
| [SetOwner](#setowner) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的属主 |
| [GetOwner](#getowner) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的属主 |
| [IsOnFire](#isonfire) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体是否着火 |
| [SetOnFire](#setonfire) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体着火 |
| [GetAttrValue](#getattrvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 获取属性值，包括生命值，饥饿度，移速 |
| [GetAttrMaxValue](#getattrmaxvalue) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取属性最大值，包括生命值，饥饿度，移速 |
| [SetAttrValue](#setattrvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 设置属性值，包括生命值，饥饿度，移速 |
| [SetAttrMaxValue](#setattrmaxvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 设置属性最大值，包括生命值，饥饿度，移速 |
| [IsInLava](#isinlava) | <span style="display:inline;color:#7575f9">客户端</span> | 实体是否在岩浆中 |
| [IsOnGround](#isonground) | <span style="display:inline;color:#7575f9">客户端</span> | 实体是否触地 |
| [GetAuxValue](#getauxvalue) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取射出的弓箭或投掷出的药水的附加值 |
| [GetCurrentAirSupply](#getcurrentairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 生物当前氧气储备值 |
| [GetMaxAirSupply](#getmaxairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物最大氧气储备值 |
| [SetCurrentAirSupply](#setcurrentairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物氧气储备值 |
| [SetMaxAirSupply](#setmaxairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物最大氧气储备值 |
| [IsConsumingAirSupply](#isconsumingairsupply) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物当前是否在消耗氧气 |
| [SetRecoverTotalAirSupplyTime](#setrecovertotalairsupplytime) | <span style="display:inline;color:#ff5555">服务端</span> | 设置恢复最大氧气量的时间，单位秒 |
| [GetSourceId](#getsourceid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取抛射物发射者实体id |
| [SetCollisionBoxSize](#setcollisionboxsize) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的包围盒 |
| [GetCollisionBoxSize](#getcollisionboxsize) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的包围盒 |
| [SetBlockControlAi](#setblockcontrolai) | <span style="display:inline;color:#ff5555">服务端</span> | 设置屏蔽生物原生AI |
| [GetDimensionId](#getdimensionid) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体所在维度 |
| [ChangeDimension](#changedimension) | <span style="display:inline;color:#ff5555">服务端</span> | 传送实体 |
| [RemoveEffect](#removeeffect) | <span style="display:inline;color:#ff5555">服务端</span> | 为实体删除指定状态效果 |
| [AddEffect](#addeffect) | <span style="display:inline;color:#ff5555">服务端</span> | 为实体添加指定状态效果，如果添加的状态已存在则有以下集中情况：1、等级大于已存在则更新状态等级及持续时间；2、状态等级相等且剩余时间duration大于已存在则刷新剩余时间；3、等级小于已存在则不做修改；4、粒子效果以新的为准 |
| [GetEffects](#geteffects) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体当前所有状态效果 |
| [TriggerCustomEvent](#triggercustomevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发生物自定义事件 |
| [IsAlive](#isalive) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 判断生物实体是否存活或非生物实体是否存在 |
| [GetGravity](#getgravity) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体的重力因子，当生物重力因子为0时则应用世界的重力因子 |
| [SetGravity](#setgravity) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体的重力因子，当生物重力因子为0时则应用世界的重力因子 |
| [SetHurt](#sethurt) | <span style="display:inline;color:#ff5555">服务端</span> | 对实体造成伤害 |
| [SetImmuneDamage](#setimmunedamage) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否免疫伤害（该属性存档） |
| [SetModAttr](#setmodattr) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置属性值 |
| [GetModAttr](#getmodattr) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取属性值 |
| [RegisterModAttrUpdateFunc](#registermodattrupdatefunc) | <span style="display:inline;color:#7575f9">客户端</span> | 注册属性值变换时的回调函数，当属性变化时会调用该函数 |
| [UnRegisterModAttrUpdateFunc](#unregistermodattrupdatefunc) | <span style="display:inline;color:#7575f9">客户端</span> | 反注册属性值变换时的回调函数 |
| [GetName](#getname) | <span style="display:inline;color:#ff5555">服务端</span> | 获取生物的自定义名称，即使用命名牌或者SetName接口设置的名称 |
| [SetName](#setname) | <span style="display:inline;color:#ff5555">服务端</span> | 用于设置生物的自定义名称，跟原版命名牌作用相同，玩家和新版流浪商人暂不支持 |
| [SetShowName](#setshowname) | <span style="display:inline;color:#7575f9">客户端</span> | 设置生物名字是否按照默认游戏逻辑显示 |
| [SetAlwaysShowName](#setalwaysshowname) | <span style="display:inline;color:#7575f9">客户端</span> | 设置生物名字是否一直显示，瞄准点不指向生物时也能显示 |
| [SetPersistence](#setpersistence) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否存盘 |
| [SetMotion](#setmotion) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置生物的瞬时移动方向向量，服务端只能对非玩家使用，客户端只能对本地玩家使用 |
| [GetMotion](#getmotion) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取生物（含玩家）的瞬时移动方向向量 |
| [SetItem](#setitem) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物物品 |
| [SetCanOtherPlayerRide](#setcanotherplayerride) | <span style="display:inline;color:#ff5555">服务端</span> | 设置其他玩家是否有权限骑乘 |
| [SetControl](#setcontrol) | <span style="display:inline;color:#ff5555">服务端</span> | 设置该生物无需装备鞍就可以控制行走跳跃 |
| [SetRidePos](#setridepos) | <span style="display:inline;color:#ff5555">服务端</span> | 设置生物骑乘位置 |
| [SetNotRender](#setnotrender) | <span style="display:inline;color:#7575f9">客户端</span> | 设置是否关闭实体渲染 |
| [SetCollidable](#setcollidable) | <span style="display:inline;color:#7575f9">客户端</span> | 设置实体是否可碰撞 |
| [SetHealthColor](#sethealthcolor) | <span style="display:inline;color:#7575f9">客户端</span> | 设置血条的颜色及背景色, 必须用game组件设置ShowHealthBar时才能显示血条！！ |
| [AddAnimation](#addanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物渲染动画 |
| [AddAnimationController](#addanimationcontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物渲染动画控制器 |
| [AddScriptAnimate](#addscriptanimate) | <span style="display:inline;color:#7575f9">客户端</span> | 在生物的客户端实体定义（minecraft:client_entity）json中的scripts/animate节点添加动画/动画控制器 |
| [AddParticleEffect](#addparticleeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物特效资源 |
| [AddRenderController](#addrendercontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物渲染控制器 |
| [AddRenderMaterial](#addrendermaterial) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物渲染需要的材质,调用该接口后需要调用RebuildActorRender才会生效 |
| [AddSoundEffect](#addsoundeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 增加生物音效资源 |
| [SetPushable](#setpushable) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体是否可推动 |
| [SetModel](#setmodel) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 设置骨骼模型 |
| [GetLavaSpeed](#getlavaspeed) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体预设岩浆里的移速 |
| [SetLavaSpeed](#setlavaspeed) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体预设岩浆里的移速 |
| [GetMaxLavaSpeed](#getmaxlavaspeed) | <span style="display:inline;color:#ff5555">服务端</span> | 获取实体预设岩浆里的最大移速 |
| [SetMaxLavaSpeed](#setmaxlavaspeed) | <span style="display:inline;color:#ff5555">服务端</span> | 设置实体预设岩浆里的最大移速 |




## GetPos

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 位置信息 |

- 备注
    - 对于非玩家，获取到的是脚底部位的位置
    - 对于玩家，如果处于行走，站立，游泳，潜行，滑翔状态，获得的位置比脚底位置高1.62；如果处于睡觉状态，获得的位置比最低位置高0.2



## GetFootPos

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体脚所在的位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 位置信息 |



## SetPos

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
self.SetPos((1,2,3))
```



## SetFootPos

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体脚底所在的位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
self.SetFootPos((0, 4, 0))
```



## GetRot

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | （上下角度，左右角度）单位是角度而不是弧度 |



## SetRot

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体的头的角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
self.SetRot((-45, 0))
```



## GetEngineTypeStr

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体的类型名称

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 实体类型名称，如minecraft:husk |

- 示例

```python
entity = self.GetEntityObject(entityId)
engineType = entity.GetEngineTypeStr()
```



## GetEngineType

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

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
entity = self.GetEntityObject(entityId)
# 以判断是否是 Mob 为例，如果要判断是否为弹射物，找到对应的类型Projectile修改即可
if entity.GetEngineType() & self.GetMinecraftEnum().EntityType.Mob == self.GetMinecraftEnum().EntityType.Mob:
    logger.info("{} is Mod".format(self.GetEngineTypeStr(entityId)))
```



## GetModelId

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取骨骼模型的Id，主要用于特效绑定骨骼模型

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 当前骨骼模型实例的id |



## PlayAnim

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    播放骨骼动画

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | aniName | str | 动画名称 |
    | isLoop | bool | 是否循环播放 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.PlayAnim("run", True)
```



## SetAnimSpeed

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置某个骨骼动画的播放速度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | aniName | str | 骨骼动画名称 |
    | speed | float | 速度倍率 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# run动作三倍速
self.SetAnimSpeed("run", 3.0)
```



## GetAnimLength

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取某个骨骼动画的长度，单位为秒

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | aniName | str | 骨骼动画名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 骨骼动画长度 |

- 示例

```python
# 获取run动画的长度
animLength = self.GetAnimLength('run')
```



## SetBrightness

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体的亮度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | brightness | float | 0：纯黑<br>1：正常亮度<br>1-14：较亮甚至纯白<br>超过14：通常为纯白，即使数值改变也没有明显变化 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:设置成功  False:设置失败 |

- 备注
    - 目前只支持修改替换了骨骼模型的实体亮度，使用游戏原生模型的实体暂不予支持。

- 示例

```python
success = self.SetBrightness(0.5)
```



## SetOpacity

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置生物模型的透明度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | opacity | float | 透明度值，取值范围为[0, 1]，值越小越透明 |

- 返回值

    无

- 示例

```python
self.SetOpacity(0.2)
```



## GetHealth

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体预设的生命值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 生命值 |



## SetHealth

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体预设的生命值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | hp | float | 生命值 |

- 返回值

    无



## GetMaxHealth

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体预设的最大生命值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 生命值 |



## SetMaxHealth

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体预设的最大生命值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | hp | float | 生命值 |

- 返回值

    无



## GetSpeed

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体预设的速度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 速度 |



## SetSpeed

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体预设的速度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | speed | float | 速度 |

- 返回值

    无



## GetMaxSpeed

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体预设的最大速度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 速度 |



## SetMaxSpeed

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体预设的最大速度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | speed | float | 速度 |

- 返回值

    无



## GetDamage

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体预设的伤害

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 伤害 |



## SetDamage

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体预设的伤害

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | hp | float | 伤害 |

- 返回值

    无



## GetMaxDamage

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体预设的最大伤害

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 伤害 |



## SetMaxDamage

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体预设的最大伤害

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | damage | float | 伤害 |

- 返回值

    无



## ShowHealth

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置是否显示血条，默认为显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | show | bool | 设置是否显示 |

- 返回值

    无

- 备注
    - 必须先设置ShowHealthBar

- 示例

```python
# 设置该entity不显示血条
self.ShowHealth(False)
```



## SetAttackTarget

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置仇恨目标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetId | str | 目标实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetAttackTarget(targetId)
```



## ResetAttackTarget

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    清除仇恨目标

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.ResetAttackTarget()
```



## GetAttackTarget

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取仇恨目标

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 仇恨目标的实体id |

- 示例

```python
self.GetAttackTarget()
```



## SetKnockback

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置击退的初始速度，需要考虑阻力的影响

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
self.SetKnockback(0.1, 0.1, 1.0, 1.0, 1.0)
```



## SetOwner

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体的属主

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | ownerId | str | 属主实体id，为None时设置实体的属主为空 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功，True表示设置成功 |

- 示例

```python
result = self.SetOwner(ownerId)
```



## GetOwner

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体的属主

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 实体属主id |

- 示例

```python
ownerId = self.GetOwner()
```



## IsOnFire

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体是否着火

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否着火 |

- 示例

```python
isOnFire = self.IsEntityOnFire(entityId)
```



## SetOnFire

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体着火

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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



## GetAttrValue

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取属性值，包括生命值，饥饿度，移速

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | attrType | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/AttrType.html">AttrType枚举</a> |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 属性结果 |

- 示例

```python
self.GetAttrValue(self.GetMinecraftEnum().AttrType.HEALTH)
```



## GetAttrMaxValue

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取属性最大值，包括生命值，饥饿度，移速

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | attrType | int | <a href="../../../../../../mcdocs/1-ModAPI/枚举值/AttrType.html">AttrType枚举</a> |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 属性值结果 |

- 示例

```python
self.GetAttrMaxValue(self.GetMinecraftEnum().AttrType.HEALTH)
```



## SetAttrValue

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置属性值，包括生命值，饥饿度，移速

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
self.SetAttrValue(self.GetMinecraftEnum().AttrType.HEALTH, 20)
```



## SetAttrMaxValue

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置属性最大值，包括生命值，饥饿度，移速

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
self.SetAttrMaxValue(serverApi.GetMinecraftEnum().AttrType.SPEED, 0.2)
```



## IsInLava

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    实体是否在岩浆中

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否在岩浆中，True为在岩浆中，False为不在岩浆中 |

- 备注
    - 只能获取到本地客户端已加载的实体是否在岩浆中，若实体在其他维度或未加载（距离本地玩家太远），将获取失败



## IsOnGround

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    实体是否触地

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否触地，True为触地，False为不触地 |

- 备注
    - 客户端实体刚创建时引擎计算还没完成，此时获取该实体是否着地将返回默认值True，需要延迟一帧进行获取才能获取到正确的数据
    - 生物处于骑乘状态时，如玩家骑在猪身上，也视作触地
    - 只能获取到本地客户端已加载的实体是否触地，若实体在其他维度或未加载（距离本地玩家太远），将获取失败



## GetAuxValue

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取射出的弓箭或投掷出的药水的附加值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | auxValue |

- 示例

```python
self.GetAuxValue()
```



## GetCurrentAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    生物当前氧气储备值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 生物当前氧气储备值 |

- 备注
    - 注意：该值返回的是当前氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）



## GetMaxAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取生物最大氧气储备值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 最大氧气储备值 |

- 备注
    - 注意：该值返回的是最大氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）



## SetCurrentAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置生物氧气储备值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | data | int | 设置生物当前氧气值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 注意：该值设置的是当前氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）

- 示例

```python
self.SetCurrentAirSupply(300)
```



## SetMaxAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置生物最大氧气储备值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | data | int | 设置生物最大氧气值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 注意：该值设置的是最大氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）

- 示例

```python
self.SetMaxAirSupply(400)
```



## IsConsumingAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取生物当前是否在消耗氧气

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否消耗氧气 |



## SetRecoverTotalAirSupplyTime

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置恢复最大氧气量的时间，单位秒

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | timeSec | float | 恢复生物最大氧气值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注意：当设置的最大氧气值小于（timeSec*10）时，生物每帧恢复氧气量的值为0

- 示例

```python
self.SetRecoverTotalAirSupplyTime(10)
```



## GetSourceId

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取抛射物发射者实体id

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 抛射物发射者实体id |



## SetCollisionBoxSize

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体的包围盒

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | size | tuple(float,float) | 第一位表示宽度和长度，第二位表示高度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 对新生产的实体需要经过5帧之后再设置包围盒的大小才会生效

- 示例

```python
self.SetCollisionBoxSize((2,3))
```



## GetCollisionBoxSize

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体的包围盒

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 包围盒大小 |



## SetBlockControlAi

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置屏蔽生物原生AI

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isBlock | bool | 是否保留AI，False为屏蔽 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 屏蔽AI后的生物无法行动，不受重力且不会被推动。但是可以受到伤害，也可以被玩家交互（例如马被骑或村民被交易）

- 示例

```python
self.SetBlockControlAi(False)
```



## GetDimensionId

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体所在维度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 维度id，0-主世界; 1-下界; 2-末地; 或其他自定义维度 |

- 示例

```python
self.GetDimensionId()
```



## ChangeDimension

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    传送实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 维度id，0-主世界; 1-下界; 2-末地; 或其他自定义维度 |
    | pos | tuple(int,int,int) | 传送的坐标，假如输入None，那么就优先选择目标维度的传送门作为目的地，其次使用维度坐标映射逻辑确定目的地 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.ChangeDimension(0, (0,4,0))
```



## RemoveEffect

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    为实体删除指定状态效果

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | effectName | str | 状态效果名称字符串，包括自定义状态效果和原版状态效果，原版状态效果可在wiki查询 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示删除成功 |

- 示例

```python
res = self.RemoveEffect(entityId, "speed")
```



## AddEffect

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    为实体添加指定状态效果，如果添加的状态已存在则有以下集中情况：1、等级大于已存在则更新状态等级及持续时间；2、状态等级相等且剩余时间duration大于已存在则刷新剩余时间；3、等级小于已存在则不做修改；4、粒子效果以新的为准

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
res = self.AddEffect("speed", 30, 2, True)
```



## GetEffects

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体当前所有状态效果

- 参数

    无

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
effectDictList = self.GetEffects()
```



## TriggerCustomEvent

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

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

- 示例

```python
eventName = "netease:custom_exploading"
self.TriggerCustomEvent(eventName)
```



## IsAlive

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    判断生物实体是否存活或非生物实体是否存在

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | false表示生物实体已死亡或非生物实体已销毁，true表示生物实体存活或非生物实体存在 |

- 备注
    - 注意，如果检测的实体所在的区块被卸载，则该接口返回False。因此，需要注意实体所在的区块是否被加载。
    - 区块卸载：游戏只会加载玩家周围的区块，玩家移动到别的区域时，原来所在区域的区块会被卸载，参考[区块介绍](https://zh.minecraft.wiki/w/%E5%8C%BA%E5%9D%97)

- 示例

```python
alive = self.IsEntityAlive()
```



## GetGravity

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体的重力因子，当生物重力因子为0时则应用世界的重力因子

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 重力因子 |



## SetGravity

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体的重力因子，当生物重力因子为0时则应用世界的重力因子

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | gravity | float | 负数，表示每帧向下的速度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetGravity(-0.08)
```



## SetHurt

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    对实体造成伤害

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | damage | int | 伤害值 |
    | cause | str | 伤害来源，详见Minecraft枚举值文档的<a href="../../../../../../mcdocs/1-ModAPI/枚举值/ActorDamageCause.html">ActorDamageCause枚举</a> |
    | attackerId | str | 伤害来源的实体id，默认为None |
    | childAttackerId | str | 伤害来源的子实体id，默认为None，比如玩家使用抛射物对实体造成伤害，该值应为抛射物Id |
    | knocked | bool | 实体是否被击退，默认值为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |



## SetImmuneDamage

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体是否免疫伤害（该属性存档）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | immune | bool | 是否免疫伤害 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetImmuneDamage(True)
```



## SetModAttr

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置属性值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | paramName | str | 属性名称，str的名称建议以mod命名为前缀，避免多个mod之间冲突 |
    | paramValue | any | 属性值，支持python基础数据 |

- 返回值

    无

- 备注
    - 注意：tuple、set在同步时会转成list。建议优先使用数字和字符串等非集合类型。

- 示例

```python
self.SetModAttr('health', 1)
self.SetModAttr('testDict', {'key':'value'})
```



## GetModAttr

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取属性值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
testDict = self.GetModAttr('testDict')
testDict['key'] = 'newValue'
self.SetModAttr('testDict', testDict)
```



## RegisterModAttrUpdateFunc

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    注册属性值变换时的回调函数，当属性变化时会调用该函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | paramName | str | 监听的属性名称 |
    | func | function | 监听的回调函数 |

- 返回值

    无

- 备注
    - 回调函数需要接受一个参数，参数是dict，具体数据示例：{'oldValue': 0, 'newValue': 1, 'entityId': ’-433231231231‘}

- 示例

```python
# 这个entityId传的是所需要监听的对象的Id
self.RegisterModAttrUpdateFunc('health', self.jumpingText)
# 当脚本层的health属性变化时则会调用self.jumpingText
def jumpingText(self, data):
    entityId = data['entityId']
    oldValue = data['oldValue']
    newValue = data['newValue']
```



## UnRegisterModAttrUpdateFunc

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    反注册属性值变换时的回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | paramName | str | 监听的属性名称 |
    | func | function | 监听的回调函数 |

- 返回值

    无

- 备注
    - 需要传注册时的同一个函数作为参数

- 示例

```python
self.UnRegisterModAttrUpdateFunc('health', self.jumpingText)
```



## GetName

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取生物的自定义名称，即使用命名牌或者SetName接口设置的名称

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 生物的自定义名称 |



## SetName

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    用于设置生物的自定义名称，跟原版命名牌作用相同，玩家和新版流浪商人暂不支持

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetName("new Name")
```



## SetShowName

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置生物名字是否按照默认游戏逻辑显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
self.SetShowName(False)
```



## SetAlwaysShowName

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置生物名字是否一直显示，瞄准点不指向生物时也能显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
self.SetAlwaysShowName(False)
```



## SetPersistence

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体是否存盘

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isPersistent | bool | True为存盘，False为不存盘 |

- 返回值

    无

- 备注
    - 实体默认都会存盘。设置为不存盘的实体，在区块卸载与退出游戏时不会存档。

- 示例

```python
self.SetPersistence(True)
```



## SetMotion

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置生物的瞬时移动方向向量，服务端只能对非玩家使用，客户端只能对本地玩家使用

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
self.SetMotion((x * 5, y * 5, z * 5))
# rot 和 世界坐标系关系
#           ^ x -90°
#           |
# 180°/-180  ----------> z 0°
#           | 90°
```



## GetMotion

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取生物（含玩家）的瞬时移动方向向量

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(int,int,int) | 瞬时移动方向向量，异常时返回None |



## SetItem

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置生物物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | posType | int | ItemPosType枚举 |
    | itemDict | dict | 生物身上不同位置的物品信息字典列表，如果传入None将清除当前位置的物品/装备 |
    | slotPos | int | 容器槽位 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置成功返回True |

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
self.SetItem(serverApi.GetMinecraftEnum().ItemPosType.OFFHAND, None, 0)
```



## SetCanOtherPlayerRide

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置其他玩家是否有权限骑乘

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | canRide | bool | 是否控制 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetCanOtherPlayerRide(entityId,False)
```



## SetControl

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置该生物无需装备鞍就可以控制行走跳跃

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isControl | bool | 是否控制 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetControl(entityId,False)
```



## SetRidePos

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置生物骑乘位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 骑乘时挂接点 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
self.SetRidePos(entityId,(1, 1, 1))
```



## SetNotRender

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置是否关闭实体渲染

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | notRender | bool | True表示不渲染该实体 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.SetNotRender(True) # 停止渲染该实体
```



## SetCollidable

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体是否可碰撞

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isCollidable | bool | False:不可碰撞 True:可碰撞 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示设置成功 |

- 示例

```python
self.SetCollidable(True) # 设为可碰撞
```



## SetHealthColor

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置血条的颜色及背景色, 必须用game组件设置ShowHealthBar时才能显示血条！！

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | front | tuple(float,float,float,float) | 血条颜色的RGBA值，范围0-1 |
    | back | tuple(float,float,float,float) | 背景颜色的RGBA值，范围0-1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | None | 无返回值 |

- 示例

```python
self.SetHealthColor((0, 0, 0, 1), (1, 1, 1, 1))
```



## AddAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    增加生物渲染动画

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animationKey | str | 动画键 |
    | animationName | str | 动画名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
self.AddAnimation("custom_move", "animation.pig.custom_move")
```



## AddAnimationController

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    增加生物渲染动画控制器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animationControllerKey | str | 动画控制器键 |
    | animationControllerName | str | 动画控制器名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
self.AddAnimationController("controller__use_item_progress", "controller.animation.humanoid.use_item_progress")
```



## AddScriptAnimate

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    在生物的客户端实体定义（minecraft:client_entity）json中的scripts/animate节点添加动画/动画控制器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animateName | str | 动画/动画控制器名称，如look_at_targe |
    | condition | str | 动画/动画控制器控制表达式，默认为空，如query.mod.index > 0 |
    | autoReplace | bool | 是否覆盖已存在的动画/动画控制器，默认值为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
self.AddScriptAnimate("animation_controller_short_name", "query.mod.index > 0")
```



## AddParticleEffect

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    增加生物特效资源

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | effectKey | str | 特效资源Key |
    | effectName | str | 特效资源名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
self.AddParticleEffect("nectar_dripping", "minecraft:nectar_drip_particle")
```



## AddRenderController

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    增加生物渲染控制器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | renderControllerName | str | 渲染控制器名称 |
    | condition | str | 渲染控制器条件 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 添加是否成功 |

- 示例

```python
self.AddRenderController('custom_render_controller_name', 'query.mod.condition')
```



## AddRenderMaterial

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    增加生物渲染需要的材质,调用该接口后需要调用RebuildActorRender才会生效

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | materialKey | str | 材质key |
    | materialName | str | 材质名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 添加是否成功 |

- 示例

```python
self.AddRenderMaterial('custom_material_key', 'custom_material_name')
```



## AddSoundEffect

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    增加生物音效资源

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | soundKey | str | 音效资源Key |
    | soundName | str | 音效资源名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 添加是否成功 |

- 示例

```python
self.AddSoundEffect("sound_thunder", "ambient.weather.thunder")
```



## SetPushable

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体是否可推动

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isPushable | bool | False:不可推动 True:可推动 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示设置成功 |

- 示例

```python
self.SetPushable(True)
```



## SetModel

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置骨骼模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | modelName | str | 模型名称,值为""时重置模型 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 要恢复原版模型请使用ResetModel接口
    - 使用客户端组件更换模型不会同步及存盘，仅是纯客户端表现，如需要同步及存盘，请使用服务器的model组件

- 示例

```python
self.SetModel("xuenv")
```



## GetLavaSpeed

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体预设岩浆里的移速

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 岩浆里的移速 |



## SetLavaSpeed

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体预设岩浆里的移速

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | float | 岩浆里的移速 |

- 返回值

    无



## GetMaxLavaSpeed

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    获取实体预设岩浆里的最大移速

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 岩浆里的最大移速 |



## SetMaxLavaSpeed

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Entity.EntityObject.EntityObject

- 描述

    设置实体预设岩浆里的最大移速

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | float | 岩浆里的最大移速 |

- 返回值

    无



