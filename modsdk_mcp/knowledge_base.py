# -*- coding: utf-8 -*-
"""
ModSDK MCP 内嵌知识库
包含核心组件列表、API 参考等，确保离线也能准确开发
"""

from typing import Dict, List, Any

# ============================================================================
# 物品组件列表 (Item Components)
# ============================================================================

ITEM_COMPONENTS = {
    # 基础组件
    "minecraft:max_stack_size": {
        "name": "最大堆叠大小",
        "type": "integer",
        "description": "决定物品的最大堆叠数目，范围 1-64",
        "example": 64
    },
    "minecraft:hand_equipped": {
        "name": "手持装备",
        "type": "boolean",
        "description": "是否是手持装备，影响渲染方向",
        "example": True
    },
    "minecraft:stacked_by_data": {
        "name": "按数据值堆叠",
        "type": "boolean",
        "description": "是否按照不同数据值分别堆叠",
        "example": True
    },
    "minecraft:damage": {
        "name": "伤害",
        "type": "integer",
        "description": "物品的攻击伤害值",
        "example": 5
    },
    "minecraft:use_duration": {
        "name": "使用时长",
        "type": "float",
        "description": "物品使用时的时间长度（秒）",
        "example": 1.6
    },
    "minecraft:use_animation": {
        "name": "使用动画",
        "type": "string",
        "description": "物品的使用动画类型",
        "values": ["eat", "drink", "bow", "crossbow", "spear", "block", "camera"],
        "example": "eat"
    },
    # 功能组件
    "minecraft:durability": {
        "name": "耐久",
        "type": "object",
        "description": "物品的耐久度",
        "properties": {
            "max_durability": "最大耐久值",
            "damage_chance": "损坏概率"
        }
    },
    "minecraft:armor": {
        "name": "盔甲",
        "type": "object",
        "description": "物品的护甲值",
        "properties": {"protection": "护甲值"}
    },
    "minecraft:food": {
        "name": "食物",
        "type": "object",
        "description": "允许物品被玩家食用",
        "properties": {
            "nutrition": "饥饿值",
            "saturation_modifier": "饱和度",
            "can_always_eat": "是否可随时食用"
        }
    },
    "minecraft:weapon": {
        "name": "武器",
        "type": "object",
        "description": "允许物品作为武器"
    },
    "minecraft:digger": {
        "name": "挖掘器",
        "type": "object",
        "description": "物品的挖掘属性",
        "properties": {"destroy_speeds": "挖掘速度列表"}
    },
    "minecraft:wearable": {
        "name": "可穿戴",
        "type": "object",
        "description": "允许物品被实体穿戴",
        "properties": {"slot": "穿戴槽位"}
    },
    "minecraft:throwable": {
        "name": "可投掷",
        "type": "object",
        "description": "允许物品作为投掷物"
    },
    "minecraft:projectile": {
        "name": "弹射物",
        "type": "object",
        "description": "允许物品发射弹射物"
    },
    "minecraft:shooter": {
        "name": "发射器",
        "type": "object",
        "description": "允许物品发射实体（如弓）"
    },
    "minecraft:cooldown": {
        "name": "冷却",
        "type": "object",
        "description": "物品使用后的冷却时间"
    },
    "minecraft:repairable": {
        "name": "可修复",
        "type": "object",
        "description": "允许物品被修复"
    },
    "minecraft:enchantable": {
        "name": "可附魔",
        "type": "object",
        "description": "物品的附魔属性"
    },
    "minecraft:fuel": {
        "name": "燃料",
        "type": "object",
        "description": "允许物品在熔炉中作为燃料"
    },
    "minecraft:block_placer": {
        "name": "方块放置器",
        "type": "object",
        "description": "允许物品放置方块"
    },
    "minecraft:entity_placer": {
        "name": "实体放置器",
        "type": "object",
        "description": "允许物品放置实体（如刷怪蛋）"
    },
    "minecraft:record": {
        "name": "唱片",
        "type": "object",
        "description": "允许物品作为唱片播放"
    },
}

# ============================================================================
# 方块组件列表 (Block Components)
# ============================================================================

BLOCK_COMPONENTS = {
    # 基础属性
    "minecraft:destructible_by_mining": {
        "name": "可挖掘破坏",
        "type": "object",
        "description": "方块的挖掘时间",
        "properties": {"seconds_to_destroy": "破坏时间（秒）"}
    },
    "minecraft:destructible_by_explosion": {
        "name": "可爆炸破坏",
        "type": "object",
        "description": "方块的爆炸抗性",
        "properties": {"explosion_resistance": "抗性值"}
    },
    "minecraft:friction": {
        "name": "摩擦力",
        "type": "float",
        "description": "方块表面摩擦系数（0.0-1.0）"
    },
    "minecraft:flammable": {
        "name": "可燃性",
        "type": "object",
        "description": "方块的可燃属性",
        "properties": {
            "catch_chance_modifier": "着火概率",
            "destroy_chance_modifier": "被火焰摧毁概率"
        }
    },
    "minecraft:map_color": {
        "name": "地图颜色",
        "type": "string",
        "description": "方块在地图上的颜色（十六进制）"
    },
    "minecraft:block_light_emission": {
        "name": "光照发射",
        "type": "float",
        "description": "方块发光等级（0.0-1.0，对应0-15）"
    },
    "minecraft:block_light_filter": {
        "name": "光照过滤",
        "type": "integer",
        "description": "光照过滤等级（0-15）"
    },
    # 几何与渲染
    "minecraft:geometry": {
        "name": "几何体",
        "type": "string/object",
        "description": "方块的自定义几何体"
    },
    "minecraft:material_instances": {
        "name": "材质实例",
        "type": "object",
        "description": "方块的材质和渲染方法"
    },
    "minecraft:unit_cube": {
        "name": "单位立方体",
        "type": "object",
        "description": "使用标准立方体渲染"
    },
    "minecraft:collision_box": {
        "name": "碰撞箱",
        "type": "object",
        "description": "方块的碰撞箱"
    },
    "minecraft:selection_box": {
        "name": "选择箱",
        "type": "object",
        "description": "方块的选择框"
    },
    # 事件触发
    "minecraft:on_interact": {
        "name": "交互事件",
        "type": "object",
        "description": "玩家与方块交互时触发"
    },
    "minecraft:on_step_on": {
        "name": "踩踏事件",
        "type": "object",
        "description": "实体踩到方块时触发"
    },
    "minecraft:on_step_off": {
        "name": "离开事件",
        "type": "object",
        "description": "实体离开方块时触发"
    },
    "minecraft:on_fall_on": {
        "name": "掉落事件",
        "type": "object",
        "description": "实体掉落到方块时触发"
    },
    "minecraft:on_placed": {
        "name": "放置事件",
        "type": "object",
        "description": "方块被放置时触发"
    },
    "minecraft:on_player_destroyed": {
        "name": "玩家破坏事件",
        "type": "object",
        "description": "玩家破坏方块时触发"
    },
    # Tick 相关
    "minecraft:random_ticking": {
        "name": "随机刻",
        "type": "object",
        "description": "方块随机刻事件"
    },
    "minecraft:queued_ticking": {
        "name": "计划刻",
        "type": "object",
        "description": "方块计划刻事件"
    },
    # 其他
    "minecraft:crafting_table": {
        "name": "工作台",
        "type": "object",
        "description": "使方块作为工作台"
    },
    "minecraft:placement_filter": {
        "name": "放置过滤",
        "type": "object",
        "description": "方块的放置条件"
    },
    "minecraft:loot": {
        "name": "战利品表",
        "type": "string",
        "description": "方块破坏时的掉落物"
    },
}

# ============================================================================
# 网易特有组件 (NetEase Components)
# ============================================================================

NETEASE_ITEM_COMPONENTS = {
    "netease:customtips": {
        "name": "自定义提示",
        "description": "物品的自定义悬停提示文本"
    },
    "netease:frame_animation": {
        "name": "帧动画",
        "description": "物品的帧动画"
    },
    "netease:show_in_hand": {
        "name": "手持显示",
        "description": "物品的手持显示设置"
    },
    "netease:liquid_clipped": {
        "name": "流体点击检测",
        "description": "ModSDK 3.8 新增物品组件；设置为 True 后，玩家点击原版流体或自定义流体时可触发 LiquidClippedServerEvent / LiquidClippedClientEvent",
        "type": "boolean",
        "example": True
    },
}

NETEASE_BLOCK_COMPONENTS = {
    "netease:aabb": {
        "name": "碰撞箱",
        "description": "方块的自定义碰撞箱"
    },
    "netease:pathable": {
        "name": "可寻路",
        "description": "AI 是否可通过此方块寻路"
    },
    "netease:tier": {
        "name": "挖掘等级",
        "description": "方块的挖掘等级要求"
    },
    "netease:block_entity": {
        "name": "方块实体",
        "description": "方块实体配置（tick、活塞等）"
    },
    "netease:random_tick": {
        "name": "随机刻",
        "description": "方块的随机刻配置"
    },
    "netease:redstone": {
        "name": "红石",
        "description": "方块的红石信号"
    },
    "netease:listen_block_remove": {
        "name": "监听移除",
        "description": "监听方块被移除事件"
    },
}

# ============================================================================
# 实体组件列表 (Entity Components)
# ============================================================================

ENTITY_COMPONENTS = {
    # 基础属性
    "minecraft:health": {
        "name": "生命值",
        "description": "实体的生命值",
        "properties": {"value": "当前值", "max": "最大值"}
    },
    "minecraft:movement": {
        "name": "移动速度",
        "description": "实体的移动速度",
        "properties": {"value": "速度值"}
    },
    "minecraft:collision_box": {
        "name": "碰撞箱",
        "description": "实体的碰撞箱大小",
        "properties": {"width": "宽度", "height": "高度"}
    },
    "minecraft:physics": {
        "name": "物理",
        "description": "实体的物理属性"
    },
    "minecraft:pushable": {
        "name": "可推动",
        "description": "实体是否可被推动"
    },
    "minecraft:type_family": {
        "name": "类型家族",
        "description": "实体所属的类型家族"
    },
    # 行为组件
    "minecraft:behavior.melee_attack": {
        "name": "近战攻击",
        "description": "实体的近战攻击行为"
    },
    "minecraft:behavior.nearest_attackable_target": {
        "name": "最近可攻击目标",
        "description": "寻找最近的可攻击目标"
    },
    "minecraft:behavior.hurt_by_target": {
        "name": "被攻击目标",
        "description": "攻击伤害自己的目标"
    },
    "minecraft:behavior.random_stroll": {
        "name": "随机漫步",
        "description": "随机漫步行为"
    },
    "minecraft:behavior.look_at_player": {
        "name": "看向玩家",
        "description": "看向附近的玩家"
    },
    "minecraft:behavior.random_look_around": {
        "name": "随机环顾",
        "description": "随机环顾四周"
    },
    # 寻路
    "minecraft:navigation.walk": {
        "name": "步行寻路",
        "description": "步行寻路组件"
    },
    "minecraft:navigation.fly": {
        "name": "飞行寻路",
        "description": "飞行寻路组件"
    },
    "minecraft:navigation.swim": {
        "name": "游泳寻路",
        "description": "游泳寻路组件"
    },
    # 战斗
    "minecraft:attack": {
        "name": "攻击",
        "description": "实体的攻击伤害",
        "properties": {"damage": "伤害值"}
    },
    "minecraft:knockback_resistance": {
        "name": "击退抗性",
        "description": "实体的击退抗性"
    },
    # 特殊
    "minecraft:is_baby": {
        "name": "是否幼年",
        "description": "标记实体为幼年状态"
    },
    "minecraft:is_tamed": {
        "name": "是否驯服",
        "description": "标记实体为已驯服"
    },
    "minecraft:loot": {
        "name": "战利品表",
        "description": "实体死亡时的掉落物"
    },
    "minecraft:spawn_entity": {
        "name": "生成实体",
        "description": "实体可以生成其他实体"
    },
    # ---- Tier 1: 必备行为组件 (12个) ----
    "minecraft:rideable": {
        "name": "可骑乘",
        "description": "使实体可以被骑乘，常用于马、猪、船等载具型实体",
        "properties": {
            "seat_count": "座位数量",
            "family_types": "允许骑乘的生物类型家族列表",
            "interact_text": "骑乘交互提示文本"
        }
    },
    "minecraft:tameable": {
        "name": "可驯服",
        "description": "使实体可以被玩家驯服，常用于狼、猫、鹦鹉等宠物型生物",
        "properties": {
            "probability": "每次喂食的驯服成功概率",
            "tame_items": "可用于驯服的物品列表",
            "tame_event": "驯服成功时触发的事件"
        }
    },
    "minecraft:damage_sensor": {
        "name": "伤害感应器",
        "description": "对实体受到的伤害进行过滤或修改，可按伤害来源类型执行不同逻辑",
        "properties": {
            "triggers": "伤害触发器列表，定义不同伤害类型的处理方式",
            "deals_damage": "是否实际造成伤害",
            "cause": "伤害类型过滤条件"
        }
    },
    "minecraft:behavior.follow_owner": {
        "name": "跟随主人",
        "description": "驯服后的实体跟随其主人移动，是宠物系统的核心行为组件",
        "properties": {
            "speed_multiplier": "跟随时的移动速度倍率",
            "start_distance": "开始跟随的最小距离",
            "stop_distance": "停止跟随的距离阈值"
        }
    },
    "minecraft:behavior.owner_hurt_by_target": {
        "name": "主人被攻击时反击",
        "description": "当主人被其他实体攻击时，将攻击者设为自己的攻击目标，实现宠物护主",
        "properties": {
            "priority": "行为优先级"
        }
    },
    "minecraft:behavior.owner_hurt_target": {
        "name": "协助主人攻击",
        "description": "当主人攻击某个目标时，宠物也会攻击同一目标，实现协同作战",
        "properties": {
            "priority": "行为优先级"
        }
    },
    "minecraft:behavior.ranged_attack": {
        "name": "远程攻击",
        "description": "使实体具备远程攻击能力，常用于骷髅、女巫等远程攻击型生物",
        "properties": {
            "charge_charged_trigger": "蓄力完成触发事件",
            "charge_shoot_trigger": "射击触发事件",
            "attack_interval_min": "最小攻击间隔(秒)",
            "attack_interval_max": "最大攻击间隔(秒)",
            "attack_radius": "攻击半径(方块)"
        }
    },
    "minecraft:behavior.tempt": {
        "name": "物品吸引",
        "description": "实体被玩家手持的特定物品吸引并跟随，常用于动物的喂食引导机制",
        "properties": {
            "items": "能吸引该实体的物品列表",
            "speed_multiplier": "被吸引时的移动速度倍率",
            "within_radius": "吸引生效的最大半径"
        }
    },
    "minecraft:behavior.breed": {
        "name": "繁殖",
        "description": "使实体可以进行繁殖行为，喂食特定物品后进入求爱状态并产生后代",
        "properties": {
            "speed_multiplier": "寻找配偶时的移动速度倍率",
            "love_item_list": "触发繁殖的物品列表"
        }
    },
    "minecraft:behavior.flee_sun": {
        "name": "躲避阳光",
        "description": "使实体在阳光下主动寻找阴影躲避，常用于僵尸、骷髅等亡灵生物",
        "properties": {
            "speed_multiplier": "逃离阳光时的移动速度倍率"
        }
    },
    "minecraft:behavior.avoid_mob_type": {
        "name": "回避特定生物",
        "description": "使实体主动远离指定类型的生物，如苦力怕躲避猫、兔子躲避狼",
        "properties": {
            "entity_types": "需要回避的实体类型过滤器",
            "max_dist": "触发回避的最大检测距离",
            "walk_speed_multiplier": "行走回避时的速度倍率",
            "sprint_speed_multiplier": "冲刺回避时的速度倍率"
        }
    },
    "minecraft:behavior.float": {
        "name": "水中漂浮",
        "description": "使实体在水中时自动浮向水面，几乎所有陆生生物都需要此组件防止溺水",
        "properties": {
            "priority": "行为优先级"
        }
    },
    # ---- Tier 2: 高频行为组件 (18个) ----
    "minecraft:behavior.move_to_block": {
        "name": "移动到方块",
        "description": "使实体移动到指定类型的方块位置，如村民前往工作站点或农田",
        "properties": {
            "goal_radius": "到达目标的判定半径",
            "search_range": "搜索目标方块的范围",
            "target_blocks": "目标方块类型列表"
        }
    },
    "minecraft:behavior.move_towards_target": {
        "name": "向目标移动",
        "description": "使实体向当前攻击目标移动，是近战攻击前的基础移动行为",
        "properties": {
            "speed_multiplier": "移动速度倍率",
            "within_radius": "开始移动的触发距离"
        }
    },
    "minecraft:behavior.leap_at_target": {
        "name": "跳跃扑击",
        "description": "使实体跳跃扑向攻击目标，常用于蜘蛛、狼等具有扑击动作的生物",
        "properties": {
            "must_be_on_ground": "是否必须站在地面才能起跳",
            "yd": "跳跃的垂直高度"
        }
    },
    "minecraft:behavior.stomp_attack": {
        "name": "踩踏攻击",
        "description": "使实体进行范围踩踏攻击，对一定区域内的目标造成伤害",
        "properties": {
            "stomp_range_x": "踩踏范围X轴",
            "stomp_range_z": "踩踏范围Z轴",
            "no_damage_range_percentage": "无伤害区域占比"
        }
    },
    "minecraft:behavior.knockback_roar": {
        "name": "击退咆哮",
        "description": "使实体发出咆哮击退周围目标，如劫掠兽的范围击退技能",
        "properties": {
            "knockback_damage": "咆哮造成的伤害",
            "knockback_range": "击退范围",
            "knockback_strength": "击退力度"
        }
    },
    "minecraft:behavior.summon_entity": {
        "name": "召唤实体",
        "description": "使实体能够召唤其他实体，如唤魔者召唤恼鬼",
        "properties": {
            "summon_choices": "可召唤的实体配置列表"
        }
    },
    "minecraft:behavior.pickup_items": {
        "name": "拾取物品",
        "description": "使实体拾取地面上的掉落物品，如狐狸叼起物品、僵尸捡起装备",
        "properties": {
            "max_dist": "拾取物品的最大检测距离",
            "speed_multiplier": "前往拾取时的速度倍率",
            "goal_radius": "到达物品的判定半径"
        }
    },
    "minecraft:behavior.panic": {
        "name": "恐慌逃跑",
        "description": "使实体在受到伤害后进入恐慌状态并四处逃跑，常用于被动型动物",
        "properties": {
            "speed_multiplier": "恐慌逃跑时的速度倍率",
            "prefer_water": "是否优先逃入水中"
        }
    },
    "minecraft:behavior.find_mount": {
        "name": "寻找坐骑",
        "description": "使实体寻找可骑乘的目标并骑上去，如小僵尸骑鸡",
        "properties": {
            "within_radius": "搜索坐骑的范围",
            "avoid_water": "是否避免水中的坐骑"
        }
    },
    "minecraft:behavior.lay_egg": {
        "name": "下蛋",
        "description": "使实体在特定方块上产卵，如海龟在沙滩上产卵",
        "properties": {
            "speed_multiplier": "前往产卵地点的速度倍率",
            "search_range": "搜索产卵方块的范围",
            "goal_radius": "到达产卵位置的判定半径",
            "target_blocks": "可产卵的目标方块列表"
        }
    },
    "minecraft:behavior.door_interact": {
        "name": "门交互",
        "description": "使实体可以开关门，常用于村民和僵尸攻城行为",
        "properties": {
            "priority": "行为优先级"
        }
    },
    "minecraft:behavior.delayed_attack": {
        "name": "延迟攻击",
        "description": "使实体的攻击带有延迟效果，攻击动画播放到特定进度时才造成伤害",
        "properties": {
            "attack_duration": "攻击动画持续时间",
            "hit_delay_pct": "伤害触发的时间点占比(0-1)",
            "speed_multiplier": "攻击时的移动速度倍率"
        }
    },
    "minecraft:behavior.charge_attack": {
        "name": "冲锋攻击",
        "description": "使实体向目标发起冲锋攻击，如疣猪兽的冲撞行为",
        "properties": {
            "speed_multiplier": "冲锋时的速度倍率",
            "max_distance": "发起冲锋的最大距离"
        }
    },
    "minecraft:behavior.circle_around_anchor": {
        "name": "锚点盘旋",
        "description": "使实体围绕一个锚点进行盘旋飞行，如幻翼围绕玩家盘旋",
        "properties": {
            "radius_range": "盘旋半径范围",
            "height_offset_range": "盘旋高度偏移范围",
            "goal_radius": "到达锚点的判定半径"
        }
    },
    "minecraft:behavior.slime_attack": {
        "name": "史莱姆攻击",
        "description": "史莱姆特有的跳跃撞击攻击行为，通过跳跃接触目标造成伤害",
        "properties": {
            "set_persistent": "攻击后是否设为持久化实体"
        }
    },
    "minecraft:behavior.silverfish_merge_with_stone": {
        "name": "蠹虫钻入石头",
        "description": "蠹虫特有的行为，使其钻入石头方块变为被虫蛀的石头",
        "properties": {
            "priority": "行为优先级"
        }
    },
    "minecraft:behavior.stalk_and_pounce_on_target": {
        "name": "潜行扑杀",
        "description": "使实体先潜行接近目标再发起突然扑击，如猫捕猎和狐狸捕食的行为模式",
        "properties": {
            "stalk_speed": "潜行接近时的移动速度",
            "pounce_max_dist": "发起扑击的最大距离",
            "interest_time": "锁定猎物后保持兴趣的时间(秒)"
        }
    },
    "minecraft:behavior.guardian_attack": {
        "name": "守卫者光束攻击",
        "description": "守卫者和远古守卫者特有的光束攻击行为，持续照射目标造成伤害",
        "properties": {
            "x_max_rotation": "X轴最大旋转角度",
            "y_max_head_rotation": "Y轴头部最大旋转角度"
        }
    },
}

# ============================================================================
# 最佳实践规则
# ============================================================================

# 3.8 尚未纳入当前版本 profile，仅保留原有历史兼容摘要。
_LEGACY_BEST_PRACTICES = {
    "modsdk_38_migration": {
        "name": "ModSDK 3.8 历史迁移",
        "rules": [
            "manifest.json 使用 format_version: 2，避免 3.8 新生物蛋贴图异常",
            "PlayerDestoryBlock 已废弃，使用 PlayerDestroyBlock",
            "EntityUseItemToPos 已废弃，使用 UseItemToPos",
            "Set/CancelShearsDestoryBlockSpeed 系列已废弃，使用 Destroy 拼写的新接口",
            "SetCameraPos 前先调用 DepartCamera()，恢复跟随使用 ResetCameraPos()",
            "SetToggleOption 不再支持 GRAPHICS 选项",
            "物品信息字典 getUserData 可覆盖收纳袋场景，相关背包/容器接口需要按 3.8 文档核对",
        ],
    },
}


def search_component(query: str, component_type: str = "all") -> List[Dict]:
    """搜索组件（带评分排序：精确ID > ID子串 > 名称匹配 > 描述匹配）。"""
    scored_results = []
    query_lower = query.lower()

    sources = []
    if component_type in ["all", "item"]:
        sources.append(("item", ITEM_COMPONENTS))
    if component_type in ["all", "block"]:
        sources.append(("block", BLOCK_COMPONENTS))
    if component_type in ["all", "entity"]:
        sources.append(("entity", ENTITY_COMPONENTS))
    if component_type in ["all", "netease", "netease_item"]:
        sources.append(("netease_item", NETEASE_ITEM_COMPONENTS))
    if component_type in ["all", "netease", "netease_block"]:
        sources.append(("netease_block", NETEASE_BLOCK_COMPONENTS))

    for source_type, components in sources:
        for comp_id, comp_data in components.items():
            score = 0
            comp_id_lower = comp_id.lower()
            comp_name_lower = comp_data.get("name", "").lower()
            comp_desc_lower = comp_data.get("description", "").lower()

            if query_lower == comp_id_lower:
                score = 100
            elif query_lower in comp_id_lower:
                score = 20
            elif query_lower in comp_name_lower:
                score = 15
            elif query_lower in comp_desc_lower:
                score = 10

            if score > 0:
                scored_results.append((score, {
                    "id": comp_id,
                    "type": source_type,
                    **comp_data
                }))

    scored_results.sort(key=lambda item: item[0], reverse=True)
    return [item[1] for item in scored_results]


def get_component_info(component_id: str) -> Dict:
    """获取组件详情。"""
    for components in [
        ITEM_COMPONENTS,
        BLOCK_COMPONENTS,
        ENTITY_COMPONENTS,
        NETEASE_ITEM_COMPONENTS,
        NETEASE_BLOCK_COMPONENTS,
    ]:
        if component_id in components:
            return {"id": component_id, **components[component_id]}
    return {}


_BEST_PRACTICE_CATEGORY_SPECS = {
    "python27_compatibility": {
        "name": "Python 2.7 兼容性",
        "domains": ("python",),
    },
    "client_server_separation": {
        "name": "客户端/服务端分离",
        "rule_ids": (
            "ARCH-SIDE-001",
            "ARCH-CROSS-001",
            "MULTIPLAYER-AUTHORITY-001",
        ),
    },
    "performance": {
        "name": "性能优化",
        "domains": ("performance",),
    },
    "ui_development": {
        "name": "JSON UI 开发",
        "domains": ("json_ui",),
    },
    "modsdk_39_migration": {
        "name": "ModSDK 3.9 / BE 1.21.120 历史迁移",
        "target_version": "3.9",
        "rule_ids": (
            "ARCH-API-001",
            "JSON-BIOME-001",
            "JSON-BLOCK-FORMAT-001",
            "JSON-FORMAT-001",
            "JSON-ID-001",
            "JSON-ITEM-FORMAT-001",
            "PY-COMPAT-001",
            "PY-EVENT-001",
            "PY-IMPORT-001",
            "UI-SCROLL-001",
        ),
    },
    "modsdk_310_migration": {
        "name": "ModSDK 3.10 / BE 1.21.130 迁移",
        "target_version": "3.10",
        "rule_ids": (
            "SDK-RELEASE-310", "PHYSX-EXPERIMENTAL-001", "PHYSX-SHAPE-001",
            "PHYSX-FORCE-001", "PHYSX-JOINT-001", "PHYSX-SIMULATION-001",
            "CAMERA-PROJECTION-001", "ROOM-METADATA-001", "ROOM-HOST-001",
            "TAG-LOOKUP-001", "RENDER-ATLAS-001", "RENDER-CLOUD-001",
            "MODEL-DIMENSION-001", "ENCHANT-ENUM-001",
        ),
    },
}


def _format_registry_practice(rule: Dict) -> str:
    """将结构化规则投影为旧工具可显示的一行文本。"""
    parts = [
        "[{}][{}/{}] {}".format(
            rule["id"], rule["enforcement"], rule["authority"], rule["title"]
        )
    ]
    if rule.get("do"):
        parts.append("应做：{}".format("；".join(rule["do"])))
    if rule.get("avoid"):
        parts.append("避免：{}".format("；".join(rule["avoid"])))
    parts.append("来源：{}".format(", ".join(rule["source_ids"])))
    return "；".join(parts)


def _project_best_practice_category(category: str) -> Dict:
    """从唯一注册表生成旧 category 的兼容视图。"""
    from .standards import get_version_profile, list_standard_rules

    if category == "modsdk_38_migration":
        legacy = _LEGACY_BEST_PRACTICES[category]
        return {
            "name": legacy["name"],
            "rules": list(legacy["rules"]),
            "projection": "legacy_3.8_compatibility",
            "target_version": "3.8",
        }

    spec = _BEST_PRACTICE_CATEGORY_SPECS.get(category)
    if spec is None:
        return {}

    target_version = spec.get("target_version", "current")
    profile = get_version_profile(target_version)
    rules = list_standard_rules(
        version=profile["version"],
        domains=spec.get("domains"),
        rule_ids=spec.get("rule_ids"),
    )
    projected = {
        "name": spec["name"],
        "rules": [_format_registry_practice(rule) for rule in rules],
        "rule_ids": [rule["id"] for rule in rules],
        "projection": "standard_registry",
        "target_version": profile["version"],
    }
    projected["source_boundary"] = profile["source_boundary"]
    return projected


def get_best_practices(category: str = "all") -> Dict:
    """从规范注册表返回旧 get_best_practices 的兼容投影。"""
    categories = (
        "python27_compatibility",
        "client_server_separation",
        "performance",
        "ui_development",
        "modsdk_38_migration",
        "modsdk_39_migration",
        "modsdk_310_migration",
    )
    if category == "all":
        return {name: _project_best_practice_category(name) for name in categories}
    return _project_best_practice_category(category)


# ============================================================================
# 架构模式 (Architecture Patterns)
# ============================================================================

ARCHITECTURE_PATTERNS: Dict[str, Dict[str, str]] = {
    "跨端通信": {
        "title": "客户端/服务端跨端通信",
        "description": "ModSDK 是 C/S 双端架构，客户端事件无法直接调用服务端API。必须通过事件系统通信。",
        "artifacts": {
            "server.py": """# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()

class MyServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        # 监听客户端发来的事件
        self.ListenForEvent('myMod', 'myClientSystem', 'ClientRequestEvent', self, self.OnClientRequest)

    def OnClientRequest(self, args):
        playerId = args['playerId']
        # 处理完后通知客户端
        self.NotifyToClient(playerId, 'ServerResponseEvent', {'result': 'ok'})
""",
            "client.py": """# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()

class MyClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.ListenForEvent('myMod', 'myServerSystem', 'ServerResponseEvent', self, self.OnServerResponse)

    def OnKeyPress(self, args):
        # 客户端按键 → 通知服务端处理
        self.NotifyToServer('ClientRequestEvent', {'action': 'sort_inventory'})

    def OnServerResponse(self, args):
        # 收到服务端响应
        pass
""",
        },
    },
    "组件使用": {
        "title": "GetEngineCompFactory 组件创建模式",
        "description": "引擎组件通过 CompFactory 创建；高频路径可复用工厂和稳定组件。",
        "pattern": """
# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

# 高频路径复用工厂
CF = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()

# 使用组件
def get_player_pos(playerId):
    posComp = CF.CreatePos(playerId)
    return posComp.GetPos()

def set_player_health(playerId, value):
    attrComp = CF.CreateAttr(playerId)
    attrComp.SetAttrValue(0, value)  # AttrType: HEALTH=0

def create_particle(pos):
    particleComp = CF.CreateParticleControl(levelId)
    particleId = particleComp.CreateEngineParticle('effects/my_particle.json', pos)
    return particleId
""",
    },
    "UI开发流程": {
        "title": "自定义UI完整开发流程",
        "description": "UI开发需要：JSON定义 → _ui_defs注册 → Python注册 → 创建 → 控件操作",
        "pattern": """
# -*- coding: utf-8 -*-
# === Step 1: 资源包 resource_pack/ui/myUI.json ===
# {
#     "namespace": "myUI",
#     "main": {
#         "type": "screen",
#         "controls": [
#             {"bg@common.bg": {}},
#             {"title": {
#                 "type": "label", "text": "标题",
#                 "offset": [0, 10], "anchor_from": "top_middle"
#             }},
#             {"close_btn": {
#                 "type": "button", "size": [30, 30],
#                 "$pressed_button_name": "button.close"
#             }}
#         ]
#     }
# }

# === Step 2: resource_pack/ui/_ui_defs.json ===
# {"ui_defs": ["ui/myUI.json"]}

# === Step 3: Python 客户端代码 ===
import mod.client.extraClientApi as clientApi

# UiInitFinished 是常见注册时机；硬约束是 RegisterUI 先于 CreateUI。
def OnUiInitFinished(self, args):
    clientApi.RegisterUI('myMod', 'myUI', 'myMod.MyUIScreen', 'myUI.main')

# 打开UI
def OpenMyUI(self, playerId):
    clientApi.CreateUI('myMod', 'myUI', {'playerId': playerId})

# === Step 4: ScreenNode 控件操作 ===
ScreenNode = clientApi.GetScreenNodeCls()

class MyUIScreen(ScreenNode):
    def Create(self):
        button = self.GetBaseUIControl('/close_btn').asButton()
        button.AddTouchEventParams({"isSwallow": True})
        button.SetButtonTouchUpCallback(self.OnCloseClick)

    def OnCloseClick(self, args):
        # 该节点由 CreateUI 创建，按对应生命周期移除。
        self.SetRemove()

    def UpdateTitle(self, text):
        ctrl = self.GetBaseUIControl('/title')
        ctrl.asLabel().SetText(text)
""",
    },
    "实体创建与管理": {
        "title": "自定义实体创建完整流程",
        "description": "创建实体 → 设置属性 → 防清除 → 监听死亡",
        "pattern": """
# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

CF = serverApi.GetEngineCompFactory()

def spawn_boss(pos, dimensionId):
    entityId = CF.CreateEngineEntityByTypeStr(
        'mymod:dark_boss',  # 对应 behavior_pack/entities/ 中的JSON
        pos, (0, 0), dimensionId,
        isNpc=False, isGlobal=True  # 全局实体不会被卸载
    )
    if not entityId:
        return None

    # 设置不会被自然清除
    CF.CreateModAttr(entityId).SetPersistent(True)

    # 设置血量
    attrComp = CF.CreateAttr(entityId)
    attrComp.SetAttrMaxValue(0, 500)   # HEALTH max
    attrComp.SetAttrValue(0, 500)       # HEALTH current

    # 设置自定义名称
    nameComp = CF.CreateName(entityId)
    nameComp.SetName('暗影巨龙')

    return entityId
""",
    },
    "定时任务": {
        "title": "定时器与Tick降帧",
        "description": "使用官方 GameComponent 定时器，或按业务精度降低 Tick 中耗时逻辑频率",
        "pattern": """
# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

CF = serverApi.GetEngineCompFactory()
gameComp = CF.CreateGame(serverApi.GetLevelId())

# 方式1: AddTimer（一次性延时）
timer = gameComp.AddTimer(3.0, self.OnTimerEnd)  # 3秒后执行

# 方式2: AddRepeatedTimer（重复定时）
timer = gameComp.AddRepeatedTimer(1.0, self.OnRepeat)  # 每秒执行

# 取消定时器
gameComp.CancelTimer(timer)

# 方式3: 仅对耗时 Tick 逻辑按业务精度降频
def OnTickServer(self):
    self.tick += 1
    if self.tick % 7 == 0:  # 每7帧执行
        self.DoExpensiveWork()
""",
    },
    "物品掉落与生成": {
        "title": "在世界中生成掉落物品",
        "description": "生成世界中的物品实体（掉落物）或直接放入玩家背包",
        "pattern": """
# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

CF = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()

# 方式1: 在世界中生成物品实体（掉落物）
def drop_item_at(pos, dimensionId, itemName, count=1, auxValue=0):
    itemComp = CF.CreateItem(levelId)
    itemDict = {
        'itemName': itemName,     # 如 'minecraft:diamond'
        'count': count,
        'auxValue': auxValue,
    }
    return itemComp.SpawnItemToLevel(itemDict, dimensionId, pos)

# 方式2: 直接放入玩家背包
def give_item(playerId, itemName, count=1):
    itemComp = CF.CreateItem(playerId)
    itemDict = {'itemName': itemName, 'count': count, 'auxValue': 0}
    return itemComp.SpawnItemToPlayerInv(itemDict, playerId)

# 方式3: 使用战利品表随机掉落
def spawn_loot(pos, entityIdentifier, playerId, killerId=None):
    comp = CF.CreateActorLoot(playerId)
    return comp.SpawnLootTable(pos, entityIdentifier, killerId)
""",
    },
}


def get_architecture_pattern_artifacts(pattern_name: str) -> Dict[str, str]:
    """返回匹配架构模式的可独立校验 Python 产物。"""
    pattern_lower = pattern_name.lower()
    for key, val in ARCHITECTURE_PATTERNS.items():
        if pattern_lower in key.lower() or pattern_lower in val.get("title", "").lower():
            if val.get("artifacts"):
                return dict(val["artifacts"])
            return {"example.py": val["pattern"]}
    return {}


def get_architecture_pattern(pattern_name: str = "") -> str:
    """获取架构模式"""
    if not pattern_name:
        # 返回所有模式的标题列表
        result = "## 可用架构模式\n\n"
        for key, val in ARCHITECTURE_PATTERNS.items():
            result += "- **{}** — {}\n".format(key, val["description"])
        result += "\n使用 `get_architecture_pattern(pattern_name)` 获取具体模式的代码示例。"
        return result

    # 模糊匹配
    pattern_lower = pattern_name.lower()
    for key, val in ARCHITECTURE_PATTERNS.items():
        if pattern_lower in key.lower() or pattern_lower in val.get("title", "").lower():
            if val.get("artifacts"):
                parts = []
                for filename, code in val["artifacts"].items():
                    parts.append("### `{}`\n\n```python\n{}\n```".format(filename, code.strip()))
                pattern_text = "\n\n".join(parts)
            else:
                pattern_text = "```python\n{}\n```".format(val["pattern"].strip())
            result = "## {}\n\n{}\n\n{}".format(
                val["title"], val["description"], pattern_text)
            return result

    return "未找到模式 '{}'。可用模式：{}".format(
        pattern_name, "、".join(ARCHITECTURE_PATTERNS.keys()))
