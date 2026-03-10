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
}

# ============================================================================
# ModSDK Python API 参考
# ============================================================================

MODSDK_SERVER_API = {
    "GetEngineCompFactory": {
        "description": "获取组件工厂",
        "usage": "CF = serverApi.GetEngineCompFactory()",
        "important": "必须在文件顶部缓存，禁止在函数内调用"
    },
    "GetLevelId": {
        "description": "获取世界ID",
        "usage": "levelId = serverApi.GetLevelId()"
    },
    "CreateComponent": {
        "description": "创建组件实例",
        "usage": "comp = CF.CreateComponent(entityId, ModName, 'ComponentName')"
    },
    "GetComponent": {
        "description": "获取组件实例",
        "usage": "comp = CF.GetComponent(entityId, ModName, 'ComponentName')"
    },
    "DestroyComponent": {
        "description": "销毁组件实例",
        "usage": "CF.DestroyComponent(entityId, ModName, 'ComponentName')"
    },
}

MODSDK_EVENTS = {
    # 玩家事件
    "ServerPlayerTryDestroyBlockEvent": {
        "side": "server",
        "description": "玩家尝试破坏方块时触发",
        "args": ["playerId", "x", "y", "z", "face", "blockName", "auxValue"],
        "cancel": True
    },
    "PlayerAttackEntityEvent": {
        "side": "server",
        "description": "玩家攻击实体时触发",
        "args": ["playerId", "victimId", "damage", "isKnockBack"],
        "cancel": True
    },
    "PlayerDieEvent": {
        "side": "server",
        "description": "玩家死亡时触发",
        "args": ["playerId", "attacker"],
        "cancel": False
    },
    "OnScriptTickServer": {
        "side": "server",
        "description": "服务端每帧触发",
        "args": [],
        "important": "必须降帧处理，避免性能问题"
    },
    # 方块事件
    "ServerBlockEntityTickEvent": {
        "side": "server",
        "description": "方块实体 Tick",
        "args": ["blockName", "dimension", "posX", "posY", "posZ"],
        "important": "必须使用坐标加盐错开执行"
    },
    "BlockNeighborChangedServerEvent": {
        "side": "server",
        "description": "方块邻居变化",
        "args": ["posX", "posY", "posZ", "blockName", "neighborPosX", "neighborPosY", "neighborPosZ"],
        "cancel": False
    },
    # 实体事件
    "EntityRemoveEvent": {
        "side": "server",
        "description": "实体移除时触发",
        "args": ["entityId"],
        "cancel": False
    },
    "MobDieEvent": {
        "side": "server",
        "description": "生物死亡时触发",
        "args": ["entityId", "attacker"],
        "cancel": False
    },
}

# ============================================================================
# 最佳实践规则
# ============================================================================

BEST_PRACTICES = {
    "python27_compatibility": {
        "name": "Python 2.7 兼容性",
        "rules": [
            "禁止使用 f-string（f\"...\"），使用 \"{}\".format() 或 % 格式化",
            "禁止使用 print() 函数，使用 print 语句",
            "禁止使用 type hints（类型注解）",
            "禁止使用 async/await 语法",
            "文件顶部添加: # -*- coding: utf-8 -*-"
        ]
    },
    "client_server_separation": {
        "name": "客户端/服务端分离",
        "rules": [
            "ServerSystem 禁止 import clientApi",
            "ClientSystem 禁止 import serverApi",
            "跨端通信只能使用事件系统"
        ]
    },
    "performance": {
        "name": "性能优化",
        "rules": [
            "GetEngineCompFactory 必须缓存在文件顶部",
            "Tick 事件必须降帧（使用质数间隔）",
            "ServerBlockEntityTickEvent 必须使用坐标加盐",
            "点对点通信优先，谨慎使用 BroadcastToAllClient",
            "禁止在函数内 import"
        ]
    },
    "ui_development": {
        "name": "UI 界面开发",
        "rules": [
            "_ui_defs.json 必须放在 resource_pack/ui/ 目录下，不是根目录",
            "_ui_defs.json 必须使用对象格式 {\"ui_defs\": [...]}，不能是纯数组",
            "RegisterUI 必须在 UiInitFinished 事件回调中调用，不能在 __init__ 中",
            "GetBaseUIControl 返回 BaseUIControl，需要 asButton()/asLabel() 转换后才能调用特定方法",
            "按钮事件绑定使用 asButton().AddTouchEventParams() 和 SetButtonTouchUpCallback()",
            "文本设置使用 asLabel().SetText()",
            "关闭界面使用 self.SetRemove()，不要用 clientApi.PopScreen()",
            "从 ScreenNode 发送事件到服务端需要先 GetSystem() 获取 ClientSystem 再 NotifyToServer()",
            "防止点击穿透使用 input_panel + modal:true，但不要设置 is_swallow:true 否则子控件无法点击",
            "UI JSON 中 uiScreenDef 格式为 namespace.screenName（如 territory_list.main）",
            "【重要】PushScreen 必须延迟执行，建议延迟 0.05 秒，避免与其他 UI 操作冲突导致弹出错误界面",
            "【重要】PopScreen 会弹出栈顶的 PushScreen UI，如果有多个 Mod UI 可能误弹，建议使用延迟 PushScreen 来保证栈顺序正确"
        ],
        "common_errors": {
            "get_screen_def error": "UI 注册时机过早，需要在 UiInitFinished 事件后注册",
            "PushScreen returns None": "_ui_defs.json 路径或格式错误，或未正确注册 UI",
            "ui_def is not a list": "_ui_defs.json 格式应为 {\"ui_defs\": [...]} 而非纯数组",
            "no attribute AddTouchEventParams": "需要先调用 asButton() 转换为 ButtonUIControl",
            "no attribute SetText": "需要先调用 asLabel() 转换为 LabelUIControl",
            "no attribute BroadcastEvent": "clientApi 没有 BroadcastEvent，使用 GetSystem().NotifyToServer()",
            "关闭UI影响原版界面": "使用 self.SetRemove() 而非 PopScreen()",
            "点击穿透到游戏世界": "使用 input_panel + modal:true",
            "子控件按钮无法点击": "不要在根 input_panel 上设置 is_swallow:true"
        },
        "file_structure": {
            "resource_pack/ui/_ui_defs.json": "UI 定义清单，格式: {\"ui_defs\": [\"ui/xxx.json\"]}",
            "resource_pack/ui/xxx.json": "UI 布局文件，定义 namespace 和控件",
            "behavior_pack/ModName_Script/scripts/ModName/client.py": "ClientSystem，注册 UI 和监听事件",
            "behavior_pack/ModName_Script/scripts/ModName/xxx_ui.py": "ScreenNode 子类，UI 逻辑"
        },
        "code_examples": {
            "register_ui": """
# 在 ClientSystem 中
def __init__(self, namespace, systemName):
    ClientSystem.__init__(self, namespace, systemName)
    # 监听 UI 初始化完成事件
    self.ListenForEvent(clientApi.engineNamespace, clientApi.engineSystemName, 
                        "UiInitFinished", self, self.on_ui_init_finished)

def on_ui_init_finished(self, args):
    # UI 系统初始化完成后才能注册
    clientApi.RegisterUI("ModNamespace", "UIKey", 
                         "ModName.ui_file.ScreenClass", "namespace.main")
""",
            "button_bindining": """
# 在 ScreenNode 子类中
def _bind_button(self):
    btn_base = self.GetBaseUIControl("/path/to/button")
    if btn_base:
        btn = btn_base.asButton()  # 转换为 ButtonUIControl
        if btn:
            btn.AddTouchEventParams({"isSwallow": True})
            btn.SetButtonTouchUpCallback(self._on_click)
""",
            "notify_server": """
# 从 ScreenNode 发送事件到服务端
def _notify_server(self, event_name, data):
    client_system = clientApi.GetSystem("ModNamespace", "ClientSystemName")
    if client_system:
        client_system.NotifyToServer(event_name, data)
""",
            "close_ui": """
# 安全关闭当前界面
def _on_close_click(self, args):
    self.SetRemove()  # 不要用 clientApi.PopScreen()
""",
            "delayed_push_screen": """
# 【重要】PushScreen 必须延迟执行，避免与其他 UI 冲突
def _open_my_ui(self, data):
    ui_data = data  # 保存数据供回调使用
    
    def do_push_screen():
        screen = clientApi.PushScreen("ModNamespace", "UIKey")
        if screen:
            self._current_ui = screen
            # 设置数据需要再延迟一帧
            def set_data():
                if self._current_ui:
                    self._current_ui.SetData(ui_data)
            gameComp.AddTimer(0.05, set_data)
    
    # 延迟 0.05 秒执行 PushScreen
    gameComp = CF.CreateGame(levelId)
    if gameComp:
        gameComp.AddTimer(0.05, do_push_screen)
""",
            "ui_json_structure": """
{
    "namespace": "my_ui",
    "main": {
        "type": "screen",
        "is_showing_menu": true,
        "controls": [{ "root@my_ui.root_panel": {} }]
    },
    "root_panel": {
        "type": "input_panel",
        "size": ["100%", "100%"],
        "modal": true,  // 模态框，限制输入
        "controls": [
            { "bg@my_ui.bg_image": {} },
            { "content@my_ui.content_panel": {} }
        ]
    },
    "bg_image": {
        "type": "image",
        "texture": "textures/ui/Black",
        "size": ["100%", "100%"],
        "alpha": 0.6
    }
}
"""
        }
    },
}

# ============================================================================
# 查询函数
# ============================================================================

def search_component(query: str, component_type: str = "all") -> List[Dict]:
    """搜索组件"""
    results = []
    query_lower = query.lower()
    
    sources = []
    if component_type in ["all", "item"]:
        sources.append(("item", ITEM_COMPONENTS))
    if component_type in ["all", "block"]:
        sources.append(("block", BLOCK_COMPONENTS))
    if component_type in ["all", "entity"]:
        sources.append(("entity", ENTITY_COMPONENTS))
    if component_type in ["all", "netease"]:
        sources.append(("netease_item", NETEASE_ITEM_COMPONENTS))
        sources.append(("netease_block", NETEASE_BLOCK_COMPONENTS))
    
    for source_type, components in sources:
        for comp_id, comp_data in components.items():
            if query_lower in comp_id.lower() or query_lower in comp_data.get("name", "").lower():
                results.append({
                    "id": comp_id,
                    "type": source_type,
                    **comp_data
                })
    
    return results


def get_component_info(component_id: str) -> Dict:
    """获取组件详情"""
    for components in [ITEM_COMPONENTS, BLOCK_COMPONENTS, ENTITY_COMPONENTS, 
                       NETEASE_ITEM_COMPONENTS, NETEASE_BLOCK_COMPONENTS]:
        if component_id in components:
            return {"id": component_id, **components[component_id]}
    return {}


def get_best_practices(category: str = "all") -> Dict:
    """获取最佳实践"""
    if category == "all":
        return BEST_PRACTICES
    return BEST_PRACTICES.get(category, {})
