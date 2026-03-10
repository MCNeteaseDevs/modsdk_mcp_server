---
sidebarDepth: 1
---
# 玩家对象PlayerObject



## 概述

- 继承关系

```mermaid
classDiagram
EntityObject <|-- PlayerObject
link EntityObject "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%A2%84%E8%AE%BE/%E5%AE%9E%E4%BD%93%E5%AF%B9%E8%B1%A1EntityObject.html"
SdkInterface <|-- EntityObject
link SdkInterface "../../../../mcguide/20-玩法开发/14-预设玩法编程/13-PresetAPI/%E9%A2%84%E8%AE%BE%E5%AF%B9%E8%B1%A1/%E9%80%9A%E7%94%A8/SDK%E6%8E%A5%E5%8F%A3%E5%B0%81%E8%A3%85SdkInterface.html"
PlayerObject: 玩家对象
SdkInterface: SDK接口封装
SdkInterface: (点击跳转)
EntityObject: 实体对象
EntityObject: (点击跳转)
```

- 描述

    PlayerObject（玩家对象）是对玩家对象封装的基类，它为实体提供了面向对象的使用方式。

- 成员变量

    无



## 索引

| 接口 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [GetPlayerId](#getplayerid) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 获取玩家预设的玩家ID |
| [IsLocalPlayer](#islocalplayer) | <span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span> | 判断当前玩家对象是否本地玩家 |
| [IsSneaking](#issneaking) | <span style="display:inline;color:#ff5555">服务端</span> | 是否潜行 |
| [GetHunger](#gethunger) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家饥饿度，展示在UI饥饿度进度条上，初始值为20，即每一个鸡腿代表2个饥饿度。 **饱和度(saturation)** ：玩家当前饱和度，初始值为5，最大值始终为玩家当前饥饿度(hunger)，该值直接影响玩家**饥饿度(hunger)**。<br>1）增加方法：吃食物。<br>2）减少方法：每触发一次**消耗事件**，该值减少1，如果该值不大于0，直接把玩家 **饥饿度(hunger)** 减少1。 |
| [SetHunger](#sethunger) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家饥饿度。 |
| [SetStepHeight](#setstepheight) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家前进非跳跃状态下能上的最大台阶高度, 默认值为0.5625，1的话表示能上一个台阶 |
| [GetStepHeight](#getstepheight) | <span style="display:inline;color:#ff5555">服务端</span> | 返回玩家前进非跳跃状态下能上的最大台阶高度 |
| [ResetStepHeight](#resetstepheight) | <span style="display:inline;color:#ff5555">服务端</span> | 恢复引擎默认玩家前进非跳跃状态下能上的最大台阶高度 |
| [GetExp](#getexp) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家当前等级下的经验值 |
| [AddExp](#addexp) | <span style="display:inline;color:#ff5555">服务端</span> | 增加玩家经验值 |
| [GetTotalExp](#gettotalexp) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家的总经验值 |
| [SetTotalExp](#settotalexp) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家的总经验值 |
| [IsFlying](#isflying) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家是否在飞行 |
| [ChangeFlyState](#changeflystate) | <span style="display:inline;color:#ff5555">服务端</span> | 给予/取消飞行能力，并且进入飞行/非飞行状态 |
| [GetLevel](#getlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 获取玩家等级 |
| [AddLevel](#addlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 修改玩家等级 |
| [SetPrefixAndSuffixName](#setprefixandsuffixname) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家前缀和后缀名字 |
| [EnableKeepInventory](#enablekeepinventory) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家死亡不掉落物品 |
| [AddAnimation](#addanimation) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家渲染动画 |
| [SetHealthLevel](#sethealthlevel) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家健康临界值，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效.原版默认值为18 |
| [SetStarveLevel](#setstarvelevel) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家饥饿临界值，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效。原版默认值为1 |
| [SetNaturalStarve](#setnaturalstarve) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否开启玩家饥饿掉血，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效.原版默认开启 |
| [SetStarveTick](#setstarvetick) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家饥饿掉血速度，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效 |
| [SetNaturalRegen](#setnaturalregen) | <span style="display:inline;color:#ff5555">服务端</span> | 设置是否开启玩家自然恢复 |
| [SetHealthTick](#sethealthtick) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家自然恢复速度 |
| [SetMaxExhaustionValue](#setmaxexhaustionvalue) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家最大消耗度(maxExhaustion) |
| [SetPickUpArea](#setpickuparea) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家的拾取物品范围 |
| [SetJumpable](#setjumpable) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家是否可跳跃 |
| [SetMovable](#setmovable) | <span style="display:inline;color:#ff5555">服务端</span> | 设置玩家是否可移动 |
| [AddAnimationController](#addanimationcontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家渲染动画控制器 |
| [AddAnimationIntoState](#addanimationintostate) | <span style="display:inline;color:#7575f9">客户端</span> | 在玩家的动画控制器中的状态添加动画 |
| [AddGeometry](#addgeometry) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家渲染几何体 |
| [AddParticleEffect](#addparticleeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家特效资源 |
| [AddRenderController](#addrendercontroller) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家渲染控制器 |
| [AddRenderMaterial](#addrendermaterial) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家渲染需要的材质 |
| [AddSoundEffect](#addsoundeffect) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家音效资源 |
| [AddTexture](#addtexture) | <span style="display:inline;color:#7575f9">客户端</span> | 增加玩家渲染贴图 |
| [SetSkin](#setskin) | <span style="display:inline;color:#7575f9">客户端</span> | 更换原版自定义皮肤 |




## GetPlayerId

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    获取玩家预设的玩家ID

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 玩家ID |



## IsLocalPlayer

<span style="display:inline;color:#7575f9">客户端</span>/<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    判断当前玩家对象是否本地玩家

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是本地玩家则返回True，否则返回False，服务端也返回False |



## IsSneaking

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    是否潜行

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否潜行 |

- 示例

```python
self.IsSneaking()
```



## GetHunger

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    获取玩家饥饿度，展示在UI饥饿度进度条上，初始值为20，即每一个鸡腿代表2个饥饿度。 **饱和度(saturation)** ：玩家当前饱和度，初始值为5，最大值始终为玩家当前饥饿度(hunger)，该值直接影响玩家**饥饿度(hunger)**。<br>1）增加方法：吃食物。<br>2）减少方法：每触发一次**消耗事件**，该值减少1，如果该值不大于0，直接把玩家 **饥饿度(hunger)** 减少1。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 玩家饥饿度 |

- 示例

```python
self.GetPlayerHunger(playerId)
```



## SetHunger

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家饥饿度。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | float | 饥饿度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetPlayerHunger(playerId, 10)
```



## SetStepHeight

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家前进非跳跃状态下能上的最大台阶高度, 默认值为0.5625，1的话表示能上一个台阶

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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



## GetStepHeight

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    返回玩家前进非跳跃状态下能上的最大台阶高度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 台阶高度 |



## ResetStepHeight

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    恢复引擎默认玩家前进非跳跃状态下能上的最大台阶高度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |



## GetExp

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    获取玩家当前等级下的经验值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isPercent | bool | 是否为百分比 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 玩家经验值 |

- 备注
    - 如果设置返回百分比为False，则返回玩家当前等级下经验的绝对值（非当前玩家总经验值）。

- 示例

```python
print(self.GetExp(False))
```



## AddExp

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    增加玩家经验值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | exp | int | 玩家经验值，可设置负数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 如果设置的exp值为负数，且超过当前等级已有的经验值，调用接口后，该玩家等级不会下降但是经验值会置为最小值

- 示例

```python
self.AddExp(25)
```



## GetTotalExp

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    获取玩家的总经验值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 总经验值，正整数。获取失败的情况下返回-1。 |

- 示例

```python
print(self.GetTotalExp())
```



## SetTotalExp

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家的总经验值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
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
self.SetTotalExp(25)
```



## IsFlying

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    获取玩家是否在飞行

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:是 False:否 |



## ChangeFlyState

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    给予/取消飞行能力，并且进入飞行/非飞行状态

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isFly | bool | 飞行状态，True：飞行模式，False：正常行走模式 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:是 False:否 |

- 示例

```python
self.ChangeFlyState(True)
```



## GetLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    获取玩家等级

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 玩家等级 |



## AddLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    修改玩家等级

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | level | int | 玩家等级，可设置负数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.AddLevel(2)
```



## SetPrefixAndSuffixName

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家前缀和后缀名字

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | prefix | str | 前缀内容 |
    | prefixColor | str | 前缀内容颜色描述，如 'RED' |
    | suffix | str | 后缀内容 |
    | suffixColor | str | 后缀内容颜色描述，如 'RED' |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
self.SetPrefixAndSuffixName(playerId, "红队", 'RED', '肉盾', 'RED')
```



## EnableKeepInventory

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家死亡不掉落物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | 是否开启“保留物品栏” |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.EnableKeepInventory(True)
```



## AddAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    增加玩家渲染动画

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animationKey | str | 动画键 |
    | animationName | str | 动画名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.AddAnimation("move.arms", "animation.player.move.arms_custom")
```



## SetHealthLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家健康临界值，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效.原版默认值为18

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | healthLevel | int | 健康临界值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetHealthLevel(16)
```



## SetStarveLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家饥饿临界值，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效。原版默认值为1

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | starveLevel | int | 饥饿临界值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetStarveLevel(2)# 饥饿值小于等于2就会进入饥饿掉血状态，默认每隔4秒掉1点血量
```



## SetNaturalStarve

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置是否开启玩家饥饿掉血，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效.原版默认开启

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | bool | True开启，False关闭 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetNaturalStarve(False)# # 关闭饥饿掉血，即使饥饿值小于饥饿临界值时也不会扣除血量
```



## SetStarveTick

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家饥饿掉血速度，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | starveTick | int | 饥饿掉血速度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetStarveTick(40) # 饥饿掉血状态下每隔2（40/20）秒扣除1点血量
```



## SetNaturalRegen

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置是否开启玩家自然恢复

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | bool | True开启，False关闭 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetNaturalRegen(False) # 关闭自然恢复，即使饥饿值大于健康临界值时也不会恢复血量
```



## SetHealthTick

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家自然恢复速度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | healthTick | int | 自然恢复速度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetHealthTick(40) # 自然恢复状态下每隔2（40/20）秒恢复1点血量
```



## SetMaxExhaustionValue

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家最大消耗度(maxExhaustion)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | float | 最大消耗度(maxExhaustion) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetMaxExhaustionValue(10.0)
```



## SetPickUpArea

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家的拾取物品范围

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | area | tuple(float,float,float) | 拾取物品范围，传入(0, 0, 0)时视作取消设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetPickUpArea((5, 0, 3))
```



## SetJumpable

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家是否可跳跃

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isJumpable | bool | 是否可跳跃,True允许跳跃，False禁止跳跃 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetJumpable(False)
```



## SetMovable

<span style="display:inline;color:#ff5555">服务端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    设置玩家是否可移动

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isMovable | bool | 是否可移动,True允许移动，False禁止移动 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetMovable(False)
```



## AddAnimationController

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    增加玩家渲染动画控制器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animationControllerKey | str | 动画控制器键 |
    | animationControllerName | str | 动画控制器名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.AddAnimationController("root", "controller.animation.player.root_custom")
```



## AddAnimationIntoState

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    在玩家的动画控制器中的状态添加动画

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animationControllerName | str | 动画控制器名称 |
    | stateName | str | 动画控制器名称 |
    | animationName | str | 添加的动画名称或动画控制器名称 |
    | condition | str | 动画控制表达式 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
self.AddAnimationIntoState("root", "first_person", "first_person_attack_controller_new", "query.mod.index > 0")
```



## AddGeometry

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    增加玩家渲染几何体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryKey | str | 渲染几何体键 |
    | geometryName | str | 渲染几何体名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
self.AddGeometry("default", "geometry.player.custom")
```



## AddParticleEffect

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    增加玩家特效资源

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

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    增加玩家渲染控制器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | renderControllerName | str | 渲染控制器名称 |
    | condition | str | 渲染控制器条件 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
self.AddRenderController('custom_render_controller_name', 'query.mod.condition')
```



## AddRenderMaterial

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    增加玩家渲染需要的材质

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | materialKey | str | 材质key |
    | materialName | str | 材质名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
self.AddRenderMaterial('custom_material_key', 'custom_material_name')
```



## AddSoundEffect

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    增加玩家音效资源

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | soundKey | str | 音效资源Key |
    | soundName | str | 音效资源名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
self.AddSoundEffect("sound_thunder", "ambient.weather.thunder")
```



## AddTexture

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    增加玩家渲染贴图

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryKey | str | 贴图键 |
    | geometryName | str | 贴图路径 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 调用该接口后需要调用RebuildPlayerRender才会生效

- 示例

```python
self.AddTexture("default", "textures/misc/missing_texture")
```



## SetSkin

<span style="display:inline;color:#7575f9">客户端</span>

method in Preset.Model.Player.PlayerObject.PlayerObject

- 描述

    更换原版自定义皮肤

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | skin | str | 贴图路径，以textures\models为当前路径的相对路径 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
self.SetSkin("kagura")
```



