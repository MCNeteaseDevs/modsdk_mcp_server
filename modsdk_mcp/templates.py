"""
代码模板生成器
生成我的世界中国版 ModSDK 的代码模板

【NetEase ModSDK 项目结构规范】
1. 模组脚本文件夹命名：{modName}_Script
2. 每个 Python 文件夹必须包含 __init__.py
3. modMain.py 中的 name 与脚本文件夹名同步
"""

from typing import Dict, Any, Optional


# ============================================================================
# 项目结构帮助函数
# ============================================================================

def get_project_folder_name(mod_id: str) -> str:
    """
    获取项目根目录名称（modMain.py 所在文件夹）
    
    规范：使用 {modName}_Script 格式
    例如：myMod -> myMod_Script
    """
    return "{}_Script".format(mod_id)


def to_camel_case(mod_id: str) -> str:
    """
    将 mod_id 转换为 CamelCase 类名
    
    例如：my_mod -> MyMod
    """
    return "".join(word.capitalize() for word in mod_id.replace("-", "_").split("_"))


# ============================================================================
# Mod 项目模板
# ============================================================================
MOD_PROJECT_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{mod_name} - 我的世界中国版 Mod
作者: {author}
描述: {description}
"""
from __future__ import print_function

# modMain.py - Mod 入口文件

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi

@Mod.Binding(name="{project_folder}", version="{version}")
class {class_name}(object):
    def __init__(self):
        pass
    
    @Mod.InitServer()
    def initServer(self):
        """服务端初始化"""
        serverApi.RegisterSystem("{mod_id}", "server", "{project_folder}.scripts.{mod_id}.server.{class_name}ServerSystem")
    
    @Mod.DestroyServer()
    def destroyServer(self):
        """服务端销毁"""
        pass
    
    @Mod.InitClient()
    def initClient(self):
        """客户端初始化"""
        clientApi.RegisterSystem("{mod_id}", "client", "{project_folder}.scripts.{mod_id}.client.{class_name}ClientSystem")
    
    @Mod.DestroyClient()
    def destroyClient(self):
        """客户端销毁"""
        pass
'''


SERVER_SYSTEM_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{mod_name} 服务端系统

【重要】本代码遵循 NetEase ModSDK 开发规范：
- ✅ 仅导入 serverApi，禁止导入 clientApi
- ✅ GetEngineCompFactory 在模块级缓存
- ✅ 所有 import 在文件顶部
- ✅ Tick 逻辑使用质数降帧
- ✅ 使用 .get() 安全访问字典
- ✅ Python 2.7 兼容语法
"""
from __future__ import print_function

import mod.server.extraServerApi as serverApi
# ⚠️ 禁止在 ServerSystem 中导入 clientApi
# 如需与客户端通信，请使用 self.NotifyToClient()

# ============================================================================
# 【规范】模块级缓存 - 避免重复调用 GetEngineCompFactory()
# ============================================================================
CF = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()

# ============================================================================
# 【规范】常量定义 - 避免魔法数字
# ============================================================================
TICK_INTERVAL = 7  # Tick 降帧间隔（使用质数）

ServerSystem = serverApi.GetServerSystemCls()


class {class_name}ServerSystem(ServerSystem):
    """服务端系统"""
    
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.tick = 0  # Tick 计数器
        self._init_events()
    
    def _init_events(self):
        """初始化事件监听"""
        namespace = serverApi.GetEngineNamespace()
        systemName = serverApi.GetEngineSystemName()
        
        # 监听玩家加入事件
        self.ListenForEvent(namespace, systemName, "AddServerPlayerEvent", self, self.on_player_join)
        
        # 监听玩家离开事件
        self.ListenForEvent(namespace, systemName, "DelServerPlayerEvent", self, self.on_player_leave)
        
        # 监听 Tick 事件（如需每帧逻辑）
        # self.ListenForEvent(namespace, systemName, "OnScriptTickServer", self, self.on_tick)
    
    def Destroy(self):
        """系统销毁时调用"""
        pass
    
    # ========== 事件处理方法 ==========
    
    def on_player_join(self, args):
        """玩家加入事件处理"""
        # 【规范】使用 .get() 安全访问
        player_id = args.get("id")
        if not player_id:
            return
        
        # 【规范】使用缓存的 CF 而非 serverApi.GetEngineCompFactory()
        nameComp = CF.CreateName(player_id)
        playerName = nameComp.GetName() if nameComp else player_id
        
        # 【规范】Python 2.7 兼容，使用 .format()
        print("[{mod_name}] 玩家加入: {{}} ({{}})".format(playerName, player_id))
        
        # 【规范】点对点通信，使用描述性事件名
        self.NotifyToClient(player_id, "PlayerWelcome", {{"message": "欢迎加入服务器！"}})
    
    def on_player_leave(self, args):
        """玩家离开事件处理"""
        player_id = args.get("id")
        if not player_id:
            return
        print("[{mod_name}] 玩家离开: {{}}".format(player_id))
    
    def on_tick(self, args=None):
        """
        Tick 事件处理
        
        【规范】必须使用降帧，避免每帧执行耗时操作
        """
        self.tick += 1
        
        # 【规范】使用质数降帧
        if self.tick % TICK_INTERVAL != 0:
            return
        
        # 在这里添加需要定时执行的逻辑
        pass
'''


CLIENT_SYSTEM_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{mod_name} 客户端系统

【重要】本代码遵循 NetEase ModSDK 开发规范：
- ✅ 仅导入 clientApi，禁止导入 serverApi
- ✅ GetEngineCompFactory 在模块级缓存
- ✅ 所有 import 在文件顶部
- ✅ 使用 .get() 安全访问字典
- ✅ Python 2.7 兼容语法
"""
from __future__ import print_function

import mod.client.extraClientApi as clientApi
# ⚠️ 禁止在 ClientSystem 中导入 serverApi
# 如需与服务端通信，请使用 self.NotifyToServer()

# ============================================================================
# 【规范】模块级缓存 - 避免重复调用 GetEngineCompFactory()
# ============================================================================
CF = clientApi.GetEngineCompFactory()

ClientSystem = clientApi.GetClientSystemCls()


class {class_name}ClientSystem(ClientSystem):
    """客户端系统"""
    
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self._init_events()
    
    def _init_events(self):
        """初始化事件监听"""
        namespace = clientApi.GetEngineNamespace()
        systemName = clientApi.GetEngineSystemName()
        
        # 监听 UI 初始化完成事件
        self.ListenForEvent(namespace, systemName, "UiInitFinished", self, self.on_ui_init_finished)
        
        # 监听来自服务端的自定义事件
        # self.ListenForEvent("YourModNamespace", "YourModSystem", "YourCustomEvent", self, self.on_custom_event)
    
    def Destroy(self):
        """系统销毁时调用"""
        pass
    
    # ========== 事件处理方法 ==========
    
    def on_ui_init_finished(self, args):
        """UI 初始化完成"""
        print("[{mod_name}] 客户端 UI 初始化完成")
    
    def on_custom_event(self, args):
        """
        处理来自服务端的自定义事件
        
        【规范】使用 .get() 安全访问
        """
        data = args.get("data")
        if data:
            # 处理数据
            pass
'''


INIT_FILE_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{mod_name} 模块初始化文件
"""
'''


EVENT_LISTENER_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
事件监听器示例
"""
from __future__ import print_function

import mod.server.extraServerApi as serverApi


def register_event_listeners(system):
    """注册事件监听器
    
    Args:
        system: ServerSystem 实例
    """
    namespace = serverApi.GetEngineNamespace()
    system_name = serverApi.GetEngineSystemName()
    
    # {event_description}
    system.ListenForEvent(
        namespace,
        system_name,
        "{event_name}",
        system,
        system.on_{event_handler}
    )


class EventHandlers:
    """事件处理器集合"""
    
    def on_{event_handler}(self, args):
        """
        {event_description}
        
        Args:
            args: 事件参数
{event_params}
        """
        # TODO: 实现事件处理逻辑
        pass
'''


CUSTOM_COMMAND_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
自定义命令示例
"""
from __future__ import print_function

import mod.server.extraServerApi as serverApi

# 模块级缓存
CF = serverApi.GetEngineCompFactory()


class CommandManager:
    """命令管理器"""
    
    def __init__(self, level_id):
        self.level_id = level_id
        self.commands = {{}}
    
    def register_command(self, name, callback, permission=0):
        """注册自定义命令
        
        Args:
            name: 命令名称
            callback: 回调函数
            permission: 权限等级 (0=所有人, 1=管理员)
        """
        self.commands[name] = {{
            "callback": callback,
            "permission": permission
        }}
    
    def on_chat(self, args):
        """处理聊天消息，检测命令"""
        message = args.get("message", "")
        player_id = args.get("playerId")
        
        if message.startswith("/"):
            parts = message[1:].split(" ")
            cmd_name = parts[0]
            cmd_args = parts[1:]
            
            if cmd_name in self.commands:
                cmd = self.commands[cmd_name]
                cmd["callback"](player_id, cmd_args)
                return True
        
        return False


# 示例命令
def cmd_{command_name}(player_id, args):
    """
    /{command_name} 命令
    
    Args:
        player_id: 执行命令的玩家ID
        args: 命令参数列表
    """
    # TODO: 实现命令逻辑
    comp = CF.CreateMsg(player_id)
    comp.NotifyOneMessage(player_id, "命令执行成功", "§a")
'''


CUSTOM_ITEM_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
自定义物品示例
物品需要在 behavior_pack 中定义 JSON 文件
"""
from __future__ import print_function

# behavior_pack_{ID}/netease_items_beh/{item_id}.json
ITEM_BEHAVIOR_JSON = """
{{
    "format_version": "1.16.0",
    "minecraft:item": {{
        "description": {{
            "identifier": "{namespace}:{item_id}",
            "category": "Items"
        }},
        "components": {{
            "minecraft:max_stack_size": {max_stack},
            "minecraft:hand_equipped": {hand_equipped}
        }}
    }}
}}
"""

# resource_pack/netease_items_res/{item_id}.json  
ITEM_RESOURCE_JSON = """
{{
    "format_version": "1.16.0",
    "minecraft:item": {{
        "description": {{
            "identifier": "{namespace}:{item_id}",
            "category": "Items"
        }},
        "components": {{
            "minecraft:icon": "{item_id}",
            "minecraft:display_name": {{
                "value": "{display_name}"
            }}
        }}
    }}
}}
"""

# 物品使用事件处理
import mod.server.extraServerApi as serverApi

# 模块级缓存
CF = serverApi.GetEngineCompFactory()


def on_item_use(args):
    """物品使用事件
    
    在 ServerSystem 中监听 ServerItemUseOnEvent 事件
    """
    player_id = args.get("playerId")
    item_dict = args.get("itemDict")
    
    if item_dict and item_dict.get("itemName") == "{namespace}:{item_id}":
        # 自定义物品使用逻辑
        print("玩家 {{}} 使用了自定义物品".format(player_id))
        return True
    
    return False
'''


CUSTOM_BLOCK_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
自定义方块示例
方块需要在 behavior_pack 中定义 JSON 文件
"""
from __future__ import print_function

# behavior_pack_{ID}/netease_blocks_beh/{block_id}.json
BLOCK_BEHAVIOR_JSON = """
{{
    "format_version": "1.16.0",
    "minecraft:block": {{
        "description": {{
            "identifier": "{namespace}:{block_id}"
        }},
        "components": {{
            "minecraft:destroy_time": {destroy_time},
            "minecraft:explosion_resistance": {explosion_resistance},
            "minecraft:friction": 0.6,
            "minecraft:map_color": "#FFFFFF"
        }}
    }}
}}
"""

# 方块交互事件处理
import mod.server.extraServerApi as serverApi

# 模块级缓存
CF = serverApi.GetEngineCompFactory()


def on_block_interact(args):
    """方块交互事件
    
    在 ServerSystem 中监听 ServerBlockUseEvent 事件
    """
    player_id = args.get("playerId")
    block_name = args.get("blockName")
    pos = (args.get("x"), args.get("y"), args.get("z"))
    
    if block_name == "{namespace}:{block_id}":
        # 自定义方块交互逻辑
        print("玩家 {{}} 与自定义方块交互，位置: {{}}".format(player_id, pos))
        return True
    
    return False
'''


class TemplateGenerator:
    """模板生成器"""
    
    @staticmethod
    def generate_mod_project(
        mod_name: str,
        mod_id: str,
        author: str = "Author",
        description: str = "A Minecraft mod",
        version: str = "1.0.0"
    ) -> Dict[str, str]:
        """生成 Mod 项目模板
        
        【规范】
        1. 脚本文件夹命名：{mod_id}_Script
        2. 每个 Python 文件夹包含 __init__.py
        3. modMain.py 的 name 与脚本文件夹名同步
        
        Returns:
            文件名到内容的映射
        """
        class_name = to_camel_case(mod_id)
        project_folder = get_project_folder_name(mod_id)  # 项目根目录：{mod_id}_Script
        
        # 脚本目录必须放在 behavior_pack 的 developer_mods 下
        script_base = "behavior_pack_{}/developer_mods/{}/".format(mod_id, project_folder)
        
        files = {
            # 根目录 __init__.py（modMain.py 所在目录）
            "{}__init__.py".format(script_base): INIT_FILE_TEMPLATE.format(mod_name=mod_name),
            
            # modMain.py - 入口文件
            # 注意：@Mod.Binding(name=...) 应该和项目根目录名一致
            "{}modMain.py".format(script_base): MOD_PROJECT_TEMPLATE.format(
                mod_name=mod_name,
                mod_id=mod_id,
                project_folder=project_folder,  # @Mod.Binding(name=...) 使用 {mod_id}_Script
                author=author,
                description=description,
                version=version,
                class_name=class_name
            ),
            
            # scripts 文件夹的 __init__.py
            "{}scripts/__init__.py".format(script_base): INIT_FILE_TEMPLATE.format(mod_name=mod_name),
            
            # 模组脚本文件夹的 __init__.py（scripts/{mod_id}/）
            "{}scripts/{}/__init__.py".format(script_base, mod_id): INIT_FILE_TEMPLATE.format(mod_name=mod_name),
            
            # 服务端系统
            "{}scripts/{}/server.py".format(script_base, mod_id): SERVER_SYSTEM_TEMPLATE.format(
                mod_name=mod_name,
                class_name=class_name
            ),
            
            # 客户端系统
            "{}scripts/{}/client.py".format(script_base, mod_id): CLIENT_SYSTEM_TEMPLATE.format(
                mod_name=mod_name,
                class_name=class_name
            ),
        }
        
        return files
    
    @staticmethod
    def generate_server_system(mod_name: str, class_name: str) -> str:
        """生成服务端系统代码"""
        return SERVER_SYSTEM_TEMPLATE.format(
            mod_name=mod_name,
            class_name=class_name
        )
    
    @staticmethod
    def generate_client_system(mod_name: str, class_name: str) -> str:
        """生成客户端系统代码"""
        return CLIENT_SYSTEM_TEMPLATE.format(
            mod_name=mod_name,
            class_name=class_name
        )
    
    @staticmethod
    def generate_event_listener(
        event_name: str,
        event_description: str = "事件处理",
        params: Optional[Dict[str, str]] = None
    ) -> str:
        """生成事件监听器代码"""
        event_handler = event_name.lower().replace("event", "")
        
        params_doc = ""
        if params:
            for name, desc in params.items():
                params_doc += "                {}: {}\n".format(name, desc)
        
        return EVENT_LISTENER_TEMPLATE.format(
            event_name=event_name,
            event_description=event_description,
            event_handler=event_handler,
            event_params=params_doc
        )
    
    @staticmethod
    def generate_custom_command(command_name: str) -> str:
        """生成自定义命令代码"""
        return CUSTOM_COMMAND_TEMPLATE.format(
            command_name=command_name
        )
    
    @staticmethod
    def generate_custom_item(
        item_id: str,
        namespace: str = "mymod",
        display_name: str = "自定义物品",
        max_stack: int = 64,
        hand_equipped: bool = False
    ) -> str:
        """生成自定义物品代码"""
        return CUSTOM_ITEM_TEMPLATE.format(
            item_id=item_id,
            namespace=namespace,
            display_name=display_name,
            max_stack=max_stack,
            hand_equipped=str(hand_equipped).lower()
        )
    
    @staticmethod
    def generate_custom_block(
        block_id: str,
        namespace: str = "mymod",
        destroy_time: float = 1.0,
        explosion_resistance: float = 1.0
    ) -> str:
        """生成自定义方块代码"""
        return CUSTOM_BLOCK_TEMPLATE.format(
            block_id=block_id,
            namespace=namespace,
            destroy_time=destroy_time,
            explosion_resistance=explosion_resistance
        )


# ============================================================================
# 便捷函数
# ============================================================================

def generate_mod_project(**kwargs) -> Dict[str, str]:
    """生成 Mod 项目模板"""
    return TemplateGenerator.generate_mod_project(**kwargs)


def generate_server_system(**kwargs) -> str:
    """生成服务端系统"""
    return TemplateGenerator.generate_server_system(**kwargs)


def generate_client_system(**kwargs) -> str:
    """生成客户端系统"""
    return TemplateGenerator.generate_client_system(**kwargs)


def generate_event_listener(**kwargs) -> str:
    """生成事件监听器"""
    return TemplateGenerator.generate_event_listener(**kwargs)


def generate_custom_command(**kwargs) -> str:
    """生成自定义命令"""
    return TemplateGenerator.generate_custom_command(**kwargs)


def generate_custom_item(**kwargs) -> str:
    """生成自定义物品"""
    return TemplateGenerator.generate_custom_item(**kwargs)


def generate_custom_block(**kwargs) -> str:
    """生成自定义方块"""
    return TemplateGenerator.generate_custom_block(**kwargs)


# ============================================================================
# Bedrock JSON 模板 - 数据驱动内容生成
# 注意：所有 JSON 中的花括号需要双写 {{ }} 以在 .format() 中转义
# 支持：国际版（标准 Bedrock）+ 网易中国版（NetEase）组件
# ============================================================================

# ============================================================================
# 国际版物品组件常量定义 (Bedrock 1.16.100+)
# ============================================================================
ITEM_COMPONENTS_BEDROCK = {
    # 基础组件
    "max_stack_size": "minecraft:max_stack_size",
    "hand_equipped": "minecraft:hand_equipped",
    "allow_off_hand": "minecraft:allow_off_hand",
    "damage": "minecraft:damage",
    "use_duration": "minecraft:use_duration",
    "use_animation": "minecraft:use_animation",
    "mining_speed": "minecraft:mining_speed",
    "foil": "minecraft:foil",
    "stacked_by_data": "minecraft:stacked_by_data",
    "can_destroy_in_creative": "minecraft:can_destroy_in_creative",
    
    # 复杂组件（需要 JSON 对象）
    "durability": "minecraft:durability",
    "armor": "minecraft:armor",
    "food": "minecraft:food",
    "weapon": "minecraft:weapon",
    "cooldown": "minecraft:cooldown",
    "wearable": "minecraft:wearable",
    "projectile": "minecraft:projectile",
    "throwable": "minecraft:throwable",
    "shooter": "minecraft:shooter",
    "digger": "minecraft:digger",
    "block_placer": "minecraft:block_placer",
    "entity_placer": "minecraft:entity_placer",
    "repairable": "minecraft:repairable",
    "chargeable": "minecraft:chargeable",
    "record": "minecraft:record",
    "render_offsets": "minecraft:render_offsets",
    "on_use": "minecraft:on_use",
    "on_use_on": "minecraft:on_use_on",
    "knockback_resistance": "minecraft:knockback_resistance",
    "enchantable": "minecraft:enchantable",
    "display_name": "minecraft:display_name",
    "icon": "minecraft:icon",
    "dye_powder": "minecraft:dye_powder",
    "fuel": "minecraft:fuel",
    "creative_category": "minecraft:creative_category",
}

# 网易特有物品组件
ITEM_COMPONENTS_NETEASE = {
    "customtips": "netease:customtips",
    "fuel": "netease:fuel",
    "cooldown": "netease:cooldown",
    "enchant_material": "netease:enchant_material",
    "frame_animation": "netease:frame_animation",
    "render_offset": "netease:render_offset",
    "show_in_hand": "netease:show_in_hand",
    "initial_user_data": "netease:initial_user_data",
}

# 行为包物品 JSON 模板（网易基岩版格式 1.10）
# 【重要】网易版物品必须使用 format_version: "1.10"
ITEM_BEHAVIOR_JSON_TEMPLATE = '''{{
    "format_version": "1.10",
    "minecraft:item": {{
        "description": {{
            "identifier": "{namespace}:{item_id}",
            "category": "{category}"
        }},
        "components": {{
            "minecraft:max_stack_size": {max_stack_size}{additional_components}
        }}
    }}
}}'''

# 行为包物品 JSON 模板（国际版格式 1.16.100+ - 仅限国际版使用）
# 注意：此模板不适用于网易版！
ITEM_BEHAVIOR_JSON_TEMPLATE_INTERNATIONAL = '''{{
    "format_version": "1.16.100",
    "minecraft:item": {{
        "description": {{
            "identifier": "{namespace}:{item_id}",
            "category": "{category}"
        }},
        "components": {{
            "minecraft:max_stack_size": {max_stack_size}{additional_components}
        }}
    }}
}}'''

# 资源包物品 JSON 模板
ITEM_RESOURCE_JSON_TEMPLATE = '''{{
    "format_version": "1.10",
    "minecraft:item": {{
        "description": {{
            "identifier": "{namespace}:{item_id}"
        }},
        "components": {{
            "minecraft:icon": "{icon_name}"
        }}
    }}
}}'''

# item_texture.json 条目模板
ITEM_TEXTURE_ENTRY_TEMPLATE = '''        "{texture_name}": {{
            "textures": "textures/items/{texture_path}"
        }}'''

# 行为包方块 JSON 模板 (网易版 1.10.0)
# 【重要】网易版方块必须使用 format_version: "1.10.0" 和旧版组件格式
BLOCK_BEHAVIOR_JSON_TEMPLATE = '''{{
    "format_version": "1.10.0",
    "minecraft:block": {{
        "description": {{
            "identifier": "{namespace}:{block_id}",
            "register_to_create_menu": {register_to_menu},
            "category": "{category}"
        }},
        "components": {{
            "minecraft:destroy_time": {{
                "value": {destroy_time}
            }},
            "minecraft:explosion_resistance": {{
                "value": {explosion_resistance}
            }},
            "minecraft:block_light_emission": {{
                "emission": {light_emission}
            }},
            "minecraft:block_light_absorption": {{
                "value": {light_dampening}
            }}{additional_components}
        }}
    }}
}}'''

# 行为包方块 JSON 模板 (国际版 1.19.20+ - 仅限国际版使用)
# 注意：此模板不适用于网易版！
BLOCK_BEHAVIOR_JSON_TEMPLATE_INTERNATIONAL = '''{{
    "format_version": "1.19.20",
    "minecraft:block": {{
        "description": {{
            "identifier": "{namespace}:{block_id}",
            "register_to_create_menu": {register_to_menu},
            "category": "{category}"
        }},
        "components": {{
            "minecraft:destructible_by_mining": {{
                "seconds_to_destroy": {destroy_time}
            }},
            "minecraft:destructible_by_explosion": {{
                "explosion_resistance": {explosion_resistance}
            }},
            "minecraft:light_emission": {light_emission},
            "minecraft:light_dampening": {light_dampening},
            "minecraft:map_color": "{map_color}"{additional_components}
        }}
    }}
}}'''

# blocks.json 条目模板
BLOCKS_JSON_ENTRY_TEMPLATE = '''    "{namespace}:{block_id}": {{
        "textures": "{texture_name}",
        "sound": "{sound}"
    }}'''

# terrain_texture.json 条目模板
TERRAIN_TEXTURE_ENTRY_TEMPLATE = '''        "{texture_name}": {{
            "textures": "textures/blocks/{texture_path}"
        }}'''

# 有序配方 JSON 模板
SHAPED_RECIPE_JSON_TEMPLATE = '''{{
    "format_version": "1.20.10",
    "minecraft:recipe_shaped": {{
        "description": {{
            "identifier": "{namespace}:{recipe_id}"
        }},
        "tags": ["{recipe_tag}"],
        "pattern": [
            "{row1}",
            "{row2}",
            "{row3}"
        ],
        "key": {{
{keys}
        }},
        "unlock": {{"context": "AlwaysUnlocked"}},
        "result": {{
            "item": "{result_item}",
            "count": {result_count}
        }}
    }}
}}'''

# 无序配方 JSON 模板
SHAPELESS_RECIPE_JSON_TEMPLATE = '''{{
    "format_version": "1.12",
    "minecraft:recipe_shapeless": {{
        "description": {{
            "identifier": "{namespace}:{recipe_id}"
        }},
        "tags": ["{recipe_tag}"],
        "ingredients": [
{ingredients}
        ],
        "result": {{
            "item": "{result_item}",
            "count": {result_count}
        }}
    }}
}}'''

# 熔炉配方 JSON 模板
FURNACE_RECIPE_JSON_TEMPLATE = '''{{
    "format_version": "1.12",
    "minecraft:recipe_furnace": {{
        "description": {{
            "identifier": "{namespace}:{recipe_id}"
        }},
        "tags": ["{recipe_tag}"],
        "input": "{input_item}",
        "output": "{output_item}"
    }}
}}'''

# 行为包 manifest.json 模板
BEHAVIOR_PACK_MANIFEST_TEMPLATE = '''{{
    "format_version": 2,
    "header": {{
        "name": "{pack_name}",
        "description": "{description}",
        "uuid": "{header_uuid}",
        "version": [{version_major}, {version_minor}, {version_patch}],
        "min_engine_version": [1, 19, 0]
    }},
    "modules": [
        {{
            "type": "data",
            "uuid": "{module_uuid}",
            "version": [{version_major}, {version_minor}, {version_patch}]
        }}
    ]{dependencies}
}}'''

# 资源包 manifest.json 模板
RESOURCE_PACK_MANIFEST_TEMPLATE = '''{{
    "format_version": 2,
    "header": {{
        "name": "{pack_name}",
        "description": "{description}",
        "uuid": "{header_uuid}",
        "version": [{version_major}, {version_minor}, {version_patch}],
        "min_engine_version": [1, 19, 0]
    }},
    "modules": [
        {{
            "type": "resources",
            "uuid": "{module_uuid}",
            "version": [{version_major}, {version_minor}, {version_patch}]
        }}
    ]
}}'''

# 本地化文件模板
LANG_FILE_TEMPLATE = '''## {mod_name} 本地化文件
## 物品名称格式: item.namespace:item_id.name=显示名称
## 方块名称格式: tile.namespace:block_id.name=显示名称

{entries}
'''


class BedrockJsonGenerator:
    """
    Bedrock JSON 生成器
    
    用于生成 NetEase 我的世界数据驱动内容的 JSON 文件
    """
    
    @staticmethod
    def generate_item_behavior_json(
        namespace: str,
        item_id: str,
        category: str = "items",
        max_stack_size: int = 64,
        components: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        生成行为包物品 JSON
        
        Args:
            namespace: 命名空间（建议使用 mod 名缩写，全小写）
            item_id: 物品ID（全小写+下划线）
            category: 创造栏分类 (items/equipment/construction/nature/commands/none)
            max_stack_size: 最大堆叠数 (1-64)
            components: 额外组件字典
            
        Returns:
            格式化的 JSON 字符串
        """
        additional = ""
        if components:
            for key, value in components.items():
                if isinstance(value, bool):
                    additional += ",\n            \"{}\": {}".format(key, str(value).lower())
                elif isinstance(value, dict):
                    import json
                    additional += ",\n            \"{}\": {}".format(key, json.dumps(value, ensure_ascii=False))
                elif isinstance(value, str):
                    additional += ",\n            \"{}\": \"{}\"".format(key, value)
                else:
                    additional += ",\n            \"{}\": {}".format(key, value)
        
        return ITEM_BEHAVIOR_JSON_TEMPLATE.format(
            namespace=namespace.lower(),
            item_id=item_id.lower(),
            category=category,
            max_stack_size=max_stack_size,
            additional_components=additional
        )
    
    @staticmethod
    def generate_item_resource_json(
        namespace: str,
        item_id: str,
        icon_name: str
    ) -> str:
        """
        生成资源包物品 JSON
        
        Args:
            namespace: 命名空间
            item_id: 物品ID
            icon_name: 图标名称（对应 item_texture.json 中的 texture_name）
        """
        return ITEM_RESOURCE_JSON_TEMPLATE.format(
            namespace=namespace.lower(),
            item_id=item_id.lower(),
            icon_name=icon_name
        )
    
    @staticmethod
    def generate_block_behavior_json(
        namespace: str,
        block_id: str,
        destroy_time: float = 1.5,
        explosion_resistance: float = 10.0,
        light_emission: int = 0,
        light_dampening: int = 15,
        map_color: str = "#FFFFFF",
        category: str = "Nature",
        register_to_menu: bool = True,
        components: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        生成行为包方块 JSON (format_version 1.19.20)
        
        Args:
            namespace: 命名空间
            block_id: 方块ID
            destroy_time: 挖掘时间（秒）
            explosion_resistance: 爆炸抗性
            light_emission: 发光等级 [0-15]
            light_dampening: 遮光等级 [0-15]
            map_color: 地图颜色（十六进制）
            category: 创造栏分类 (Construction/Nature/Equipment/Items)
            register_to_menu: 是否注册到创造栏
            components: 额外组件字典
        """
        additional = ""
        if components:
            for key, value in components.items():
                if isinstance(value, bool):
                    additional += ",\n            \"{}\": {}".format(key, str(value).lower())
                elif isinstance(value, dict):
                    import json
                    additional += ",\n            \"{}\": {}".format(key, json.dumps(value, ensure_ascii=False))
                elif isinstance(value, str):
                    additional += ",\n            \"{}\": \"{}\"".format(key, value)
                else:
                    additional += ",\n            \"{}\": {}".format(key, value)
        
        return BLOCK_BEHAVIOR_JSON_TEMPLATE.format(
            namespace=namespace.lower(),
            block_id=block_id.lower(),
            destroy_time=destroy_time,
            explosion_resistance=explosion_resistance,
            light_emission=light_emission,
            light_dampening=light_dampening,
            map_color=map_color,
            category=category,
            register_to_menu=str(register_to_menu).lower(),
            additional_components=additional
        )
    
    @staticmethod
    def generate_shaped_recipe_json(
        namespace: str,
        recipe_id: str,
        pattern: list,  # ["ABC", "DEF", "GHI"]
        keys: Dict[str, str],  # {"A": "minecraft:diamond", "B": "minecraft:stick"}
        result_item: str,
        result_count: int = 1,
        recipe_tag: str = "crafting_table"
    ) -> str:
        """
        生成有序合成配方 JSON
        
        Args:
            namespace: 命名空间
            recipe_id: 配方ID
            pattern: 合成图案（3行字符串列表）
            keys: 字符到物品ID的映射
            result_item: 结果物品ID
            result_count: 结果数量
            recipe_tag: 配方标签 (crafting_table/stonecutter 等)
        """
        # 补齐 pattern 到 3 行
        while len(pattern) < 3:
            pattern.append("   ")
        
        # 生成 keys JSON
        key_lines = []
        for char, item in keys.items():
            if ":" in item and "data" not in item:
                key_lines.append('            \"{}\": {{\"item\": \"{}\"}}'.format(char, item))
            else:
                key_lines.append('            \"{}\": {{\"item\": \"{}\"}}'.format(char, item))
        
        return SHAPED_RECIPE_JSON_TEMPLATE.format(
            namespace=namespace.lower(),
            recipe_id=recipe_id.lower(),
            row1=pattern[0],
            row2=pattern[1],
            row3=pattern[2],
            keys=",\n".join(key_lines),
            result_item=result_item,
            result_count=result_count,
            recipe_tag=recipe_tag
        )
    
    @staticmethod
    def generate_shapeless_recipe_json(
        namespace: str,
        recipe_id: str,
        ingredients: list,  # ["minecraft:diamond", "minecraft:stick"]
        result_item: str,
        result_count: int = 1,
        recipe_tag: str = "crafting_table"
    ) -> str:
        """
        生成无序合成配方 JSON
        
        Args:
            namespace: 命名空间
            recipe_id: 配方ID
            ingredients: 材料物品ID列表
            result_item: 结果物品ID
            result_count: 结果数量
            recipe_tag: 配方标签
        """
        ingredient_lines = []
        for item in ingredients:
            ingredient_lines.append('            {{\"item\": \"{}\"}}'.format(item))
        
        return SHAPELESS_RECIPE_JSON_TEMPLATE.format(
            namespace=namespace.lower(),
            recipe_id=recipe_id.lower(),
            ingredients=",\n".join(ingredient_lines),
            result_item=result_item,
            result_count=result_count,
            recipe_tag=recipe_tag
        )
    
    @staticmethod
    def generate_furnace_recipe_json(
        namespace: str,
        recipe_id: str,
        input_item: str,
        output_item: str,
        recipe_tag: str = "furnace"
    ) -> str:
        """
        生成熔炉配方 JSON
        
        Args:
            namespace: 命名空间
            recipe_id: 配方ID
            input_item: 输入物品ID
            output_item: 输出物品ID
            recipe_tag: 配方标签 (furnace/blast_furnace/smoker/campfire)
        """
        return FURNACE_RECIPE_JSON_TEMPLATE.format(
            namespace=namespace.lower(),
            recipe_id=recipe_id.lower(),
            input_item=input_item,
            output_item=output_item,
            recipe_tag=recipe_tag
        )
    
    @staticmethod
    def generate_behavior_pack_manifest(
        pack_name: str,
        description: str,
        header_uuid: str,
        module_uuid: str,
        version: tuple = (1, 0, 0),
        resource_pack_uuid: Optional[str] = None
    ) -> str:
        """
        生成行为包 manifest.json
        
        Args:
            pack_name: 包名称
            description: 描述
            header_uuid: header UUID
            module_uuid: module UUID
            version: 版本元组 (major, minor, patch)
            resource_pack_uuid: 依赖的资源包 UUID（可选）
        """
        dependencies = ""
        if resource_pack_uuid:
            dependencies = ''',
    "dependencies": [
        {{
            "uuid": "{}",
            "version": [{}, {}, {}]
        }}
    ]'''.format(resource_pack_uuid, version[0], version[1], version[2])
        
        return BEHAVIOR_PACK_MANIFEST_TEMPLATE.format(
            pack_name=pack_name,
            description=description,
            header_uuid=header_uuid,
            module_uuid=module_uuid,
            version_major=version[0],
            version_minor=version[1],
            version_patch=version[2],
            dependencies=dependencies
        )
    
    @staticmethod
    def generate_resource_pack_manifest(
        pack_name: str,
        description: str,
        header_uuid: str,
        module_uuid: str,
        version: tuple = (1, 0, 0)
    ) -> str:
        """
        生成资源包 manifest.json
        """
        return RESOURCE_PACK_MANIFEST_TEMPLATE.format(
            pack_name=pack_name,
            description=description,
            header_uuid=header_uuid,
            module_uuid=module_uuid,
            version_major=version[0],
            version_minor=version[1],
            version_patch=version[2]
        )
    
    @staticmethod
    def generate_lang_entry(
        entry_type: str,  # "item" or "tile"
        identifier: str,  # "namespace:id"
        display_name: str
    ) -> str:
        """
        生成本地化条目
        
        Args:
            entry_type: 条目类型 ("item" 表示物品, "tile" 表示方块)
            identifier: 完整标识符 (namespace:id)
            display_name: 显示名称
        """
        return "{}.{}.name={}".format(entry_type, identifier, display_name)


# 便捷函数
def generate_item_json(namespace: str, item_id: str, **kwargs) -> Dict[str, str]:
    """
    生成完整的物品 JSON 文件集
    
    Returns:
        包含 behavior 和 resource JSON 的字典
    """
    return {
        "behavior": BedrockJsonGenerator.generate_item_behavior_json(namespace, item_id, **kwargs),
        "resource": BedrockJsonGenerator.generate_item_resource_json(
            namespace, item_id, 
            icon_name=kwargs.get("icon_name", item_id)
        )
    }


def generate_block_json(namespace: str, block_id: str, **kwargs) -> str:
    """生成方块行为包 JSON"""
    return BedrockJsonGenerator.generate_block_behavior_json(namespace, block_id, **kwargs)


def generate_recipe_json(
    recipe_type: str,
    namespace: str,
    recipe_id: str,
    **kwargs
) -> str:
    """
    生成配方 JSON
    
    Args:
        recipe_type: 配方类型 ("shaped", "shapeless", "furnace")
        namespace: 命名空间
        recipe_id: 配方ID
        **kwargs: 配方特定参数
    """
    if recipe_type == "shaped":
        return BedrockJsonGenerator.generate_shaped_recipe_json(namespace, recipe_id, **kwargs)
    elif recipe_type == "shapeless":
        return BedrockJsonGenerator.generate_shapeless_recipe_json(namespace, recipe_id, **kwargs)
    elif recipe_type == "furnace":
        return BedrockJsonGenerator.generate_furnace_recipe_json(namespace, recipe_id, **kwargs)
    else:
        raise ValueError("Unknown recipe type: {}".format(recipe_type))


# ============================================================================
# 实体 JSON 模板 - Entity
# 注意：所有 JSON 中的花括号需要双写 {{ }} 以在 .format() 中转义
# ============================================================================

ENTITY_BEHAVIOR_JSON_TEMPLATE = '''{{
    "format_version": "1.10.0",
    "minecraft:entity": {{
        "description": {{
            "identifier": "{namespace}:{entity_id}",
            "is_spawnable": {is_spawnable},
            "is_summonable": {is_summonable},
            "runtime_identifier": "{runtime_identifier}"
        }},
        "component_groups": {{
            "default": {{}}
        }},
        "components": {{
            "minecraft:type_family": {{"family": [{family}]}},
            "minecraft:collision_box": {{"width": {collision_width}, "height": {collision_height}}},
            "minecraft:health": {{"value": {health}, "max": {health}}},
            "minecraft:movement": {{"value": {movement_speed}}},
            "minecraft:navigation.walk": {{"can_walk": true, "avoid_water": true}},
            "minecraft:movement.basic": {{}},
            "minecraft:jump.static": {{}},
            "minecraft:physics": {{}}{additional_components}
        }},
        "events": {{
            "minecraft:entity_spawned": {{"add": {{"component_groups": ["default"]}}}}
        }}
    }}
}}'''

ENTITY_RESOURCE_JSON_TEMPLATE = '''{{
    "format_version": "1.10.0",
    "minecraft:client_entity": {{
        "description": {{
            "identifier": "{namespace}:{entity_id}",
            "materials": {{"default": "entity_alphatest"}},
            "textures": {{"default": "textures/entity/{entity_id}/{entity_id}"}},
            "geometry": {{"default": "geometry.{entity_id}"}},
            "render_controllers": ["controller.render.default"],
            "spawn_egg": {{
                "base_color": "{spawn_egg_base_color}",
                "overlay_color": "{spawn_egg_overlay_color}"
            }}
        }}
    }}
}}'''

# ============================================================================
# 战利品表 JSON 模板 - Loot Table
# ============================================================================

LOOT_TABLE_JSON_TEMPLATE = '''{{
    "pools": [
{pools}
    ]
}}'''

SPAWN_RULES_JSON_TEMPLATE = '''{{
    "format_version": "1.8.0",
    "minecraft:spawn_rules": {{
        "description": {{
            "identifier": "{namespace}:{entity_id}",
            "population_control": "{population_control}"
        }},
        "conditions": [{conditions}]
    }}
}}'''


# ============================================================================
# 扩展生成器类
# ============================================================================

class EntityJsonGenerator:
    """实体 JSON 生成器
    
    遵循 NetEase ModSDK 3.7 官方文档规范：
    - format_version: 1.10.0
    - runtime_identifier: 基于哪个原版实体构建
    - 支持 component_groups 和 events
    """
    
    @staticmethod
    def generate_entity_behavior_json(
        namespace: str,
        entity_id: str,
        health: int = 20,
        movement_speed: float = 0.25,
        collision_width: float = 0.6,
        collision_height: float = 1.8,
        family: list = None,
        is_spawnable: bool = True,
        is_summonable: bool = True,
        runtime_identifier: str = None,
        components: Optional[Dict[str, Any]] = None
    ) -> str:
        """生成实体行为包 JSON
        
        Args:
            namespace: 命名空间
            entity_id: 实体ID
            health: 生命值
            movement_speed: 移动速度
            collision_width: 碰撞箱宽度
            collision_height: 碰撞箱高度
            family: 实体家族列表
            is_spawnable: 是否可用刷怪蛋生成
            is_summonable: 是否可用命令召唤
            runtime_identifier: 基于哪个原版实体构建（如 minecraft:pig）
            components: 额外组件字典
        """
        import json
        
        if family is None:
            family = [entity_id]
        family_str = ", ".join(['"{}"'.format(f) for f in family])
        
        # 默认 runtime_identifier 使用 minecraft:{entity_id}
        if runtime_identifier is None:
            runtime_identifier = "minecraft:{}".format(entity_id.lower())
        
        additional = ""
        if components:
            for key, value in components.items():
                if isinstance(value, bool):
                    additional += ',\n            "{}": {}'.format(key, str(value).lower())
                elif isinstance(value, dict):
                    additional += ',\n            "{}": {}'.format(key, json.dumps(value, ensure_ascii=False))
                elif isinstance(value, str):
                    additional += ',\n            "{}": "{}"'.format(key, value)
                else:
                    additional += ',\n            "{}": {}'.format(key, value)
        
        return ENTITY_BEHAVIOR_JSON_TEMPLATE.format(
            namespace=namespace.lower(),
            entity_id=entity_id.lower(),
            health=health,
            movement_speed=movement_speed,
            collision_width=collision_width,
            collision_height=collision_height,
            family=family_str,
            is_spawnable=str(is_spawnable).lower(),
            is_summonable=str(is_summonable).lower(),
            runtime_identifier=runtime_identifier,
            additional_components=additional
        )
    
    @staticmethod
    def generate_entity_resource_json(
        namespace: str,
        entity_id: str,
        spawn_egg_base_color: str = "#FFFFFF",
        spawn_egg_overlay_color: str = "#000000"
    ) -> str:
        """生成实体资源包 JSON"""
        return ENTITY_RESOURCE_JSON_TEMPLATE.format(
            namespace=namespace.lower(),
            entity_id=entity_id.lower(),
            spawn_egg_base_color=spawn_egg_base_color,
            spawn_egg_overlay_color=spawn_egg_overlay_color
        )
    
    @staticmethod
    def generate_spawn_rules_json(
        namespace: str,
        entity_id: str,
        population_control: str = "animal",
        spawn_weight: int = 8,
        min_size: int = 2,
        max_size: int = 4
    ) -> str:
        """生成生成规则 JSON"""
        conditions = '''
            {
                "minecraft:spawns_on_surface": {},
                "minecraft:spawns_on_block_filter": "minecraft:grass",
                "minecraft:brightness_filter": {"min": 7, "max": 15, "adjust_for_weather": false},
                "minecraft:weight": {"default": ''' + str(spawn_weight) + '''},
                "minecraft:herd": {"min_size": ''' + str(min_size) + ''', "max_size": ''' + str(max_size) + '''}
            }
        '''
        return SPAWN_RULES_JSON_TEMPLATE.format(
            namespace=namespace.lower(),
            entity_id=entity_id.lower(),
            population_control=population_control,
            conditions=conditions
        )


class LootTableGenerator:
    """战利品表生成器"""
    
    @staticmethod
    def generate_loot_table_json(pools: list) -> str:
        """生成战利品表 JSON"""
        import json
        
        pool_strs = []
        for pool in pools:
            rolls = pool.get("rolls", 1)
            entries = pool.get("entries", [])
            
            entry_strs = []
            for entry in entries:
                item_name = entry.get("item", "minecraft:air")
                weight = entry.get("weight", 1)
                
                functions = ""
                if "count" in entry:
                    count = entry["count"]
                    if isinstance(count, list):
                        functions = ', "functions": [{"function": "set_count", "count": {"min": ' + str(count[0]) + ', "max": ' + str(count[1]) + '}}]'
                    else:
                        functions = ', "functions": [{"function": "set_count", "count": ' + str(count) + '}]'
                
                entry_str = '                {"type": "item", "name": "' + item_name + '", "weight": ' + str(weight) + functions + '}'
                entry_strs.append(entry_str)
            
            pool_str = '        {\n            "rolls": ' + str(rolls) + ',\n            "entries": [\n' + ",\n".join(entry_strs) + '\n            ]\n        }'
            pool_strs.append(pool_str)
        
        return LOOT_TABLE_JSON_TEMPLATE.format(pools=",\n".join(pool_strs))
    
    @staticmethod
    def generate_simple_loot_table(items: list) -> str:
        """生成简单战利品表"""
        entries = []
        for item in items:
            entry = {"item": item.get("item", "minecraft:air"), "weight": item.get("weight", 1)}
            if "count" in item:
                entry["count"] = item["count"]
            entries.append(entry)
        return LootTableGenerator.generate_loot_table_json([{"rolls": 1, "entries": entries}])


# 便捷函数
def generate_entity_json(namespace: str, entity_id: str, **kwargs) -> Dict[str, str]:
    """生成完整的实体 JSON 文件集"""
    # 分离行为包和资源包的参数
    behavior_kwargs = {}
    resource_kwargs = {}
    
    # 行为包参数
    behavior_keys = ['health', 'movement_speed', 'collision_width', 'collision_height', 
                     'family', 'is_spawnable', 'is_summonable', 'runtime_identifier', 'components']
    # 资源包参数
    resource_keys = ['spawn_egg_base_color', 'spawn_egg_overlay_color']
    
    for key, value in kwargs.items():
        if key in behavior_keys:
            behavior_kwargs[key] = value
        if key in resource_keys:
            resource_kwargs[key] = value
    
    return {
        "behavior": EntityJsonGenerator.generate_entity_behavior_json(namespace, entity_id, **behavior_kwargs),
        "resource": EntityJsonGenerator.generate_entity_resource_json(namespace, entity_id, **resource_kwargs)
    }


def generate_loot_table_json(pools: list) -> str:
    """生成战利品表 JSON"""
    return LootTableGenerator.generate_loot_table_json(pools)


def generate_simple_loot_table(items: list) -> str:
    """生成简单战利品表"""
    return LootTableGenerator.generate_simple_loot_table(items)


def generate_spawn_rules_json(namespace: str, entity_id: str, **kwargs) -> str:
    """生成生成规则 JSON"""
    return EntityJsonGenerator.generate_spawn_rules_json(namespace, entity_id, **kwargs)


# ============================================================================
# 国际版专用组件生成器 (Bedrock 1.16.100+)
# ============================================================================

class BedrockComponentsGenerator:
    """
    国际版 Bedrock 组件生成器
    
    生成符合国际版标准的物品、方块、实体组件
    支持 format_version 1.16.100+ 的新组件格式
    """
    
    # ========== 物品组件生成 ==========
    
    @staticmethod
    def generate_durability_component(
        max_durability: int = 100,
        damage_chance_min: int = 0,
        damage_chance_max: int = 0
    ) -> Dict[str, Any]:
        """
        生成耐久组件 (minecraft:durability)
        
        Args:
            max_durability: 最大耐久值
            damage_chance_min: 每次使用损失耐久的最小概率 (0-100)
            damage_chance_max: 每次使用损失耐久的最大概率 (0-100)
        """
        component = {
            "max_durability": max_durability
        }
        if damage_chance_min > 0 or damage_chance_max > 0:
            component["damage_chance"] = {
                "min": damage_chance_min,
                "max": damage_chance_max
            }
        return {"minecraft:durability": component}
    
    @staticmethod
    def generate_food_component(
        nutrition: int = 4,
        saturation_modifier: str = "normal",
        can_always_eat: bool = False,
        using_converts_to: str = None,
        effects: list = None
    ) -> Dict[str, Any]:
        """
        生成食物组件 (minecraft:food)
        
        Args:
            nutrition: 恢复的饥饿值 (半个鸡腿 = 1)
            saturation_modifier: 饱和度修饰符 (poor/low/normal/good/max/supernatural)
            can_always_eat: 是否在饱食状态下也能吃
            using_converts_to: 吃完后转换为的物品 (如 minecraft:bowl)
            effects: 效果列表 [{"name": "regeneration", "duration": 5, "amplifier": 1, "chance": 1.0}]
        """
        component = {
            "nutrition": nutrition,
            "saturation_modifier": saturation_modifier
        }
        if can_always_eat:
            component["can_always_eat"] = True
        if using_converts_to:
            component["using_converts_to"] = using_converts_to
        if effects:
            component["effects"] = effects
        return {"minecraft:food": component}
    
    @staticmethod
    def generate_weapon_component(
        on_hurt_entity: str = None,
        on_hit_block: str = None,
        on_not_hurt_entity: str = None
    ) -> Dict[str, Any]:
        """
        生成武器组件 (minecraft:weapon)
        
        Args:
            on_hurt_entity: 击中实体时触发的事件
            on_hit_block: 击中方块时触发的事件
            on_not_hurt_entity: 未击中实体时触发的事件
        """
        component = {}
        if on_hurt_entity:
            component["on_hurt_entity"] = {"event": on_hurt_entity}
        if on_hit_block:
            component["on_hit_block"] = {"event": on_hit_block}
        if on_not_hurt_entity:
            component["on_not_hurt_entity"] = {"event": on_not_hurt_entity}
        return {"minecraft:weapon": component}
    
    @staticmethod
    def generate_armor_component(
        protection: int = 2,
        texture_type: str = None
    ) -> Dict[str, Any]:
        """
        生成盔甲组件 (minecraft:armor)
        
        Args:
            protection: 护甲值
            texture_type: 盔甲纹理类型
        """
        component = {"protection": protection}
        if texture_type:
            component["texture_type"] = texture_type
        return {"minecraft:armor": component}
    
    @staticmethod
    def generate_wearable_component(
        slot: str = "slot.armor.chest",
        protection: int = 0,
        dispensable: bool = True
    ) -> Dict[str, Any]:
        """
        生成可穿戴组件 (minecraft:wearable)
        
        Args:
            slot: 穿戴槽位 (slot.armor.head/chest/legs/feet/offhand)
            protection: 护甲值
            dispensable: 是否可从发射器发射装备
        """
        return {
            "minecraft:wearable": {
                "slot": slot,
                "protection": protection,
                "dispensable": dispensable
            }
        }
    
    @staticmethod
    def generate_cooldown_component(
        category: str = "attack",
        duration: float = 1.0
    ) -> Dict[str, Any]:
        """
        生成冷却组件 (minecraft:cooldown)
        
        Args:
            category: 冷却类别（同类别物品共享冷却）
            duration: 冷却时间（秒）
        """
        return {
            "minecraft:cooldown": {
                "category": category,
                "duration": duration
            }
        }
    
    @staticmethod
    def generate_throwable_component(
        do_swing_animation: bool = True,
        launch_power_scale: float = 1.0,
        max_draw_duration: float = 0.0,
        max_launch_power: float = 1.0,
        min_draw_duration: float = 0.0,
        scale_power_by_draw_duration: bool = False
    ) -> Dict[str, Any]:
        """
        生成可投掷组件 (minecraft:throwable)
        
        Args:
            do_swing_animation: 投掷时是否播放挥动动画
            launch_power_scale: 发射力度倍率
            max_draw_duration: 最大蓄力时间
            max_launch_power: 最大发射力度
            min_draw_duration: 最小蓄力时间
            scale_power_by_draw_duration: 力度是否随蓄力时间缩放
        """
        return {
            "minecraft:throwable": {
                "do_swing_animation": do_swing_animation,
                "launch_power_scale": launch_power_scale,
                "max_draw_duration": max_draw_duration,
                "max_launch_power": max_launch_power,
                "min_draw_duration": min_draw_duration,
                "scale_power_by_draw_duration": scale_power_by_draw_duration
            }
        }
    
    @staticmethod
    def generate_projectile_component(
        projectile_entity: str = "minecraft:arrow",
        minimum_critical_power: float = 1.0
    ) -> Dict[str, Any]:
        """
        生成弹射物组件 (minecraft:projectile)
        
        Args:
            projectile_entity: 发射的实体类型
            minimum_critical_power: 触发暴击的最小力度
        """
        return {
            "minecraft:projectile": {
                "projectile_entity": projectile_entity,
                "minimum_critical_power": minimum_critical_power
            }
        }
    
    @staticmethod
    def generate_shooter_component(
        ammunition: list = None,
        charge_on_draw: bool = True,
        max_draw_duration: float = 1.0,
        scale_power_by_draw_duration: bool = True
    ) -> Dict[str, Any]:
        """
        生成发射器组件 (minecraft:shooter)
        
        Args:
            ammunition: 弹药列表 [{"item": "minecraft:arrow", "use_offhand": True, "search_inventory": True}]
            charge_on_draw: 是否在拉弓时充能
            max_draw_duration: 最大蓄力时间
            scale_power_by_draw_duration: 力度是否随蓄力时间缩放
        """
        if ammunition is None:
            ammunition = [{"item": "minecraft:arrow", "use_offhand": True, "search_inventory": True}]
        return {
            "minecraft:shooter": {
                "ammunition": ammunition,
                "charge_on_draw": charge_on_draw,
                "max_draw_duration": max_draw_duration,
                "scale_power_by_draw_duration": scale_power_by_draw_duration
            }
        }
    
    @staticmethod
    def generate_digger_component(
        destroy_speeds: list = None,
        use_efficiency: bool = True
    ) -> Dict[str, Any]:
        """
        生成挖掘器组件 (minecraft:digger)
        
        Args:
            destroy_speeds: 挖掘速度列表 [{"block": "minecraft:dirt", "speed": 4}]
            use_efficiency: 是否使用效率附魔
        """
        if destroy_speeds is None:
            destroy_speeds = []
        return {
            "minecraft:digger": {
                "destroy_speeds": destroy_speeds,
                "use_efficiency": use_efficiency
            }
        }
    
    @staticmethod
    def generate_block_placer_component(
        block: str,
        use_on: list = None
    ) -> Dict[str, Any]:
        """
        生成方块放置器组件 (minecraft:block_placer)
        
        Args:
            block: 要放置的方块
            use_on: 可以放置的方块列表
        """
        component = {"block": block}
        if use_on:
            component["use_on"] = use_on
        return {"minecraft:block_placer": component}
    
    @staticmethod
    def generate_entity_placer_component(
        entity: str,
        use_on: list = None,
        dispense_on: list = None
    ) -> Dict[str, Any]:
        """
        生成实体放置器组件 (minecraft:entity_placer)
        
        Args:
            entity: 要放置的实体
            use_on: 可以放置的方块列表
            dispense_on: 可以从发射器发射到的方块列表
        """
        component = {"entity": entity}
        if use_on:
            component["use_on"] = use_on
        if dispense_on:
            component["dispense_on"] = dispense_on
        return {"minecraft:entity_placer": component}
    
    @staticmethod
    def generate_repairable_component(
        repair_items: list = None
    ) -> Dict[str, Any]:
        """
        生成可修复组件 (minecraft:repairable)
        
        Args:
            repair_items: 修复材料列表 [{"items": ["minecraft:iron_ingot"], "repair_amount": 25}]
        """
        if repair_items is None:
            repair_items = []
        return {
            "minecraft:repairable": {
                "repair_items": repair_items
            }
        }
    
    @staticmethod
    def generate_enchantable_component(
        slot: str = "sword",
        value: int = 10
    ) -> Dict[str, Any]:
        """
        生成可附魔组件 (minecraft:enchantable)
        
        Args:
            slot: 附魔槽位类型 (armor_feet/armor_torso/armor_head/armor_legs/axe/bow/
                  cosmetic/crossbow/elytra/fishing_rod/flintsteel/hoe/pickaxe/
                  shears/shield/shovel/sword/all)
            value: 附魔等级
        """
        return {
            "minecraft:enchantable": {
                "slot": slot,
                "value": value
            }
        }
    
    @staticmethod
    def generate_chargeable_component(
        movement_modifier: float = 0.35
    ) -> Dict[str, Any]:
        """
        生成可蓄力组件 (minecraft:chargeable)
        
        Args:
            movement_modifier: 蓄力时的移动速度倍率
        """
        return {
            "minecraft:chargeable": {
                "movement_modifier": movement_modifier
            }
        }
    
    @staticmethod
    def generate_render_offsets_component(
        main_hand: Dict = None,
        off_hand: Dict = None
    ) -> Dict[str, Any]:
        """
        生成渲染偏移组件 (minecraft:render_offsets)
        
        Args:
            main_hand: 主手偏移 {"first_person": {...}, "third_person": {...}}
            off_hand: 副手偏移
        """
        component = {}
        if main_hand:
            component["main_hand"] = main_hand
        if off_hand:
            component["off_hand"] = off_hand
        return {"minecraft:render_offsets": component}
    
    @staticmethod
    def generate_fuel_component(
        duration: float = 200.0
    ) -> Dict[str, Any]:
        """
        生成燃料组件 (minecraft:fuel)
        
        Args:
            duration: 燃烧时间（tick），200 = 10秒
        """
        return {
            "minecraft:fuel": {
                "duration": duration
            }
        }
    
    @staticmethod
    def generate_record_component(
        sound_event: str,
        duration: float = 0.0,
        comparator_signal: int = 1
    ) -> Dict[str, Any]:
        """
        生成唱片组件 (minecraft:record)
        
        Args:
            sound_event: 音效事件名称
            duration: 播放时长
            comparator_signal: 比较器信号强度 (1-15)
        """
        return {
            "minecraft:record": {
                "sound_event": sound_event,
                "duration": duration,
                "comparator_signal": comparator_signal
            }
        }


# ============================================================================
# 网易特有组件生成器 (NetEase ModSDK)
# ============================================================================

class NeteaseComponentsGenerator:
    """
    网易特有组件生成器
    
    生成 NetEase ModSDK 特有的组件
    """
    
    @staticmethod
    def generate_customtips_component(
        value: str
    ) -> Dict[str, Any]:
        """
        生成自定义提示组件 (netease:customtips)
        
        Args:
            value: 提示文本（支持颜色代码）
        """
        return {
            "netease:customtips": {
                "value": value
            }
        }
    
    @staticmethod
    def generate_frame_animation_component(
        frame_count: int = 1,
        frame_time: float = 1.0
    ) -> Dict[str, Any]:
        """
        生成帧动画组件 (netease:frame_animation)
        
        Args:
            frame_count: 帧数
            frame_time: 每帧时间（秒）
        """
        return {
            "netease:frame_animation": {
                "frame_count": frame_count,
                "frame_time": frame_time
            }
        }
    
    @staticmethod
    def generate_show_in_hand_component(
        value: bool = True
    ) -> Dict[str, Any]:
        """
        生成手持显示组件 (netease:show_in_hand)
        
        Args:
            value: 是否在手中显示
        """
        return {
            "netease:show_in_hand": {
                "value": value
            }
        }
    
    # ========== 方块组件 ==========
    
    @staticmethod
    def generate_pathable_component(
        value: bool = True
    ) -> Dict[str, Any]:
        """
        生成可通行组件 (netease:pathable)
        
        Args:
            value: 是否可被AI寻路通过
        """
        return {
            "netease:pathable": {
                "value": value
            }
        }
    
    @staticmethod
    def generate_tier_component(
        destroy_level: int = 0,
        tool_type: str = "pickaxe"
    ) -> Dict[str, Any]:
        """
        生成挖掘等级组件 (netease:tier)
        
        Args:
            destroy_level: 挖掘等级 (0=手, 1=木, 2=石, 3=铁, 4=钻石, 5=下界合金)
            tool_type: 工具类型 (pickaxe/axe/shovel/hoe/shears)
        """
        return {
            "netease:tier": {
                "destroy_level": destroy_level,
                "tool_type": tool_type
            }
        }
    
    @staticmethod
    def generate_block_entity_component(
        tick: bool = False,
        movable: bool = True
    ) -> Dict[str, Any]:
        """
        生成方块实体组件 (netease:block_entity)
        
        Args:
            tick: 是否每tick触发事件
            movable: 是否可被活塞移动
        """
        return {
            "netease:block_entity": {
                "tick": tick,
                "movable": movable
            }
        }
    
    @staticmethod
    def generate_random_tick_component(
        enable: bool = True
    ) -> Dict[str, Any]:
        """
        生成随机刻组件 (netease:random_tick)
        
        Args:
            enable: 是否启用随机刻
        """
        return {
            "netease:random_tick": {
                "enable": enable
            }
        }
    
    @staticmethod
    def generate_listen_block_remove_component(
        enable: bool = True
    ) -> Dict[str, Any]:
        """
        生成监听方块移除组件 (netease:listen_block_remove)
        
        Args:
            enable: 是否监听方块移除事件
        """
        return {
            "netease:listen_block_remove": {
                "enable": enable
            }
        }
    
    @staticmethod
    def generate_aabb_component(
        collision: list = None,
        clip: list = None
    ) -> Dict[str, Any]:
        """
        生成碰撞箱组件 (netease:aabb)
        
        Args:
            collision: 碰撞箱 [minX, minY, minZ, maxX, maxY, maxZ]
            clip: 射线检测碰撞箱
        """
        component = {}
        if collision:
            component["collision"] = collision
        if clip:
            component["clip"] = clip
        return {"netease:aabb": component}
    
    @staticmethod
    def generate_redstone_component(
        can_be_powered: bool = True,
        emit_redstone: int = 0
    ) -> Dict[str, Any]:
        """
        生成红石组件 (netease:redstone)
        
        Args:
            can_be_powered: 是否可被红石充能
            emit_redstone: 发出的红石信号强度 (0-15)
        """
        return {
            "netease:redstone": {
                "can_be_powered": can_be_powered,
                "emit_redstone": emit_redstone
            }
        }
    
    @staticmethod
    def generate_block_container_component(
        container_size: int = 27,
        container_type: str = "chest"
    ) -> Dict[str, Any]:
        """
        生成方块容器组件 (netease:block_container)
        
        Args:
            container_size: 容器大小
            container_type: 容器类型 (chest/hopper/dispenser/dropper)
        """
        return {
            "netease:block_container": {
                "container_size": container_size,
                "container_type": container_type
            }
        }


# ============================================================================
# 高级物品生成函数
# ============================================================================

def generate_sword_item_json(
    namespace: str,
    item_id: str,
    damage: int = 5,
    durability: int = 131,
    enchantability: int = 15,
    repair_material: str = None
) -> Dict[str, str]:
    """
    生成剑类物品 JSON
    
    Args:
        namespace: 命名空间
        item_id: 物品ID
        damage: 攻击伤害
        durability: 耐久值
        enchantability: 附魔等级
        repair_material: 修复材料 (如 minecraft:iron_ingot)
    """
    components = {
        "minecraft:damage": damage,
        "minecraft:hand_equipped": True,
        "minecraft:stacked_by_data": True,
        "minecraft:max_stack_size": 1
    }
    components.update(BedrockComponentsGenerator.generate_durability_component(durability))
    components.update(BedrockComponentsGenerator.generate_weapon_component())
    components.update(BedrockComponentsGenerator.generate_enchantable_component("sword", enchantability))
    
    if repair_material:
        components.update(BedrockComponentsGenerator.generate_repairable_component([
            {"items": [repair_material], "repair_amount": "context.other->query.remaining_durability + 0.05 * context.other->query.max_durability"}
        ]))
    
    return generate_item_json(namespace, item_id, components=components)


# ============================================================================
# 国际版方块组件生成器
# ============================================================================

class BedrockBlockComponentsGenerator:
    """国际版基岩版方块组件生成器"""
    
    @staticmethod
    def generate_destroy_time_component(value: float = 1.0) -> Dict[str, Any]:
        """
        生成方块破坏时间组件 (minecraft:destroy_time)
        
        Args:
            value: 破坏时间（秒）
        """
        return {"minecraft:destroy_time": value}
    
    @staticmethod
    def generate_explosion_resistance_component(value: float = 1.0) -> Dict[str, Any]:
        """
        生成爆炸抗性组件 (minecraft:explosion_resistance)
        
        Args:
            value: 抗性值（TNT=4, 黑曜石=1200）
        """
        return {"minecraft:explosion_resistance": value}
    
    @staticmethod
    def generate_friction_component(value: float = 0.6) -> Dict[str, Any]:
        """
        生成摩擦力组件 (minecraft:friction)
        
        Args:
            value: 摩擦系数（0.0-1.0，冰=0.98，灵魂沙=0.5）
        """
        return {"minecraft:friction": value}
    
    @staticmethod
    def generate_flammable_component(
        catch_chance: int = 5,
        destroy_chance: int = 20
    ) -> Dict[str, Any]:
        """
        生成可燃性组件 (minecraft:flammable)
        
        Args:
            catch_chance: 着火概率
            destroy_chance: 被火焰摧毁概率
        """
        return {
            "minecraft:flammable": {
                "catch_chance_modifier": catch_chance,
                "destroy_chance_modifier": destroy_chance
            }
        }
    
    @staticmethod
    def generate_map_color_component(color: str = "#808080") -> Dict[str, Any]:
        """
        生成地图颜色组件 (minecraft:map_color)
        
        Args:
            color: 十六进制颜色代码
        """
        return {"minecraft:map_color": color}
    
    @staticmethod
    def generate_block_light_emission_component(value: float = 0.0) -> Dict[str, Any]:
        """
        生成光照发射组件 (minecraft:block_light_emission)
        
        Args:
            value: 光照等级（0.0-1.0，对应0-15光照）
        """
        return {"minecraft:block_light_emission": value}
    
    @staticmethod
    def generate_block_light_filter_component(value: int = 15) -> Dict[str, Any]:
        """
        生成光照过滤组件 (minecraft:block_light_filter)
        
        Args:
            value: 光照过滤等级（0-15，0=透明，15=不透光）
        """
        return {"minecraft:block_light_filter": value}
    
    @staticmethod
    def generate_crafting_table_component(
        table_name: str = "custom_crafting",
        crafting_tags: list = None
    ) -> Dict[str, Any]:
        """
        生成工作台组件 (minecraft:crafting_table)
        
        Args:
            table_name: 工作台名称
            crafting_tags: 支持的配方标签
        """
        if crafting_tags is None:
            crafting_tags = ["crafting_table"]
        return {
            "minecraft:crafting_table": {
                "table_name": table_name,
                "crafting_tags": crafting_tags
            }
        }
    
    @staticmethod
    def generate_on_interact_component(
        event: str,
        condition: str = None,
        target: str = "self"
    ) -> Dict[str, Any]:
        """
        生成交互事件组件 (minecraft:on_interact)
        
        Args:
            event: 触发的事件名称
            condition: Molang 条件表达式
            target: 事件目标 (self/other)
        """
        comp = {
            "minecraft:on_interact": {
                "event": event,
                "target": target
            }
        }
        if condition:
            comp["minecraft:on_interact"]["condition"] = condition
        return comp
    
    @staticmethod
    def generate_on_step_on_component(
        event: str,
        condition: str = None,
        target: str = "self"
    ) -> Dict[str, Any]:
        """
        生成踩踏事件组件 (minecraft:on_step_on)
        
        Args:
            event: 触发的事件名称
            condition: Molang 条件表达式
            target: 事件目标
        """
        comp = {
            "minecraft:on_step_on": {
                "event": event,
                "target": target
            }
        }
        if condition:
            comp["minecraft:on_step_on"]["condition"] = condition
        return comp
    
    @staticmethod
    def generate_on_step_off_component(
        event: str,
        condition: str = None,
        target: str = "self"
    ) -> Dict[str, Any]:
        """
        生成离开事件组件 (minecraft:on_step_off)
        """
        comp = {
            "minecraft:on_step_off": {
                "event": event,
                "target": target
            }
        }
        if condition:
            comp["minecraft:on_step_off"]["condition"] = condition
        return comp
    
    @staticmethod
    def generate_on_fall_on_component(
        event: str,
        min_fall_distance: float = 1.0,
        target: str = "self"
    ) -> Dict[str, Any]:
        """
        生成掉落到方块事件组件 (minecraft:on_fall_on)
        
        Args:
            event: 触发的事件名称
            min_fall_distance: 最小掉落高度
            target: 事件目标
        """
        return {
            "minecraft:on_fall_on": {
                "event": event,
                "min_fall_distance": min_fall_distance,
                "target": target
            }
        }
    
    @staticmethod
    def generate_on_placed_component(
        event: str,
        target: str = "self"
    ) -> Dict[str, Any]:
        """
        生成放置事件组件 (minecraft:on_placed)
        
        Args:
            event: 触发的事件名称
            target: 事件目标
        """
        return {
            "minecraft:on_placed": {
                "event": event,
                "target": target
            }
        }
    
    @staticmethod
    def generate_on_player_destroyed_component(
        event: str,
        target: str = "self"
    ) -> Dict[str, Any]:
        """
        生成玩家破坏事件组件 (minecraft:on_player_destroyed)
        """
        return {
            "minecraft:on_player_destroyed": {
                "event": event,
                "target": target
            }
        }
    
    @staticmethod
    def generate_random_ticking_component(
        event: str,
        target: str = "self"
    ) -> Dict[str, Any]:
        """
        生成随机刻组件 (minecraft:random_ticking)
        
        Args:
            event: 随机刻触发的事件
            target: 事件目标
        """
        return {
            "minecraft:random_ticking": {
                "on_tick": {
                    "event": event,
                    "target": target
                }
            }
        }
    
    @staticmethod
    def generate_queued_ticking_component(
        event: str,
        interval_range: list = None,
        looping: bool = True
    ) -> Dict[str, Any]:
        """
        生成计划刻组件 (minecraft:queued_ticking)
        
        Args:
            event: 触发的事件
            interval_range: 刻间隔范围 [min, max]
            looping: 是否循环
        """
        if interval_range is None:
            interval_range = [20, 20]
        return {
            "minecraft:queued_ticking": {
                "on_tick": {
                    "event": event,
                    "target": "self"
                },
                "interval_range": interval_range,
                "looping": looping
            }
        }
    
    @staticmethod
    def generate_unit_cube_component() -> Dict[str, Any]:
        """
        生成单位立方体组件 (minecraft:unit_cube)
        用于简单方块渲染
        """
        return {"minecraft:unit_cube": {}}
    
    @staticmethod
    def generate_geometry_component(
        identifier: str,
        bone_visibility: Dict[str, bool] = None
    ) -> Dict[str, Any]:
        """
        生成几何体组件 (minecraft:geometry)
        
        Args:
            identifier: 几何体标识符（如 geometry.custom_block）
            bone_visibility: 骨骼可见性设置
        """
        comp = {"minecraft:geometry": identifier}
        if bone_visibility:
            comp = {
                "minecraft:geometry": {
                    "identifier": identifier,
                    "bone_visibility": bone_visibility
                }
            }
        return comp
    
    @staticmethod
    def generate_material_instances_component(
        instances: Dict[str, Dict] = None
    ) -> Dict[str, Any]:
        """
        生成材质实例组件 (minecraft:material_instances)
        
        Args:
            instances: 材质实例定义
                {
                    "*": {"texture": "my_texture", "render_method": "opaque"},
                    "up": {"texture": "my_texture_top"}
                }
        """
        if instances is None:
            instances = {
                "*": {
                    "texture": "custom_texture",
                    "render_method": "opaque"
                }
            }
        return {"minecraft:material_instances": instances}
    
    @staticmethod
    def generate_collision_box_component(
        origin: list = None,
        size: list = None,
        enabled: bool = True
    ) -> Dict[str, Any]:
        """
        生成碰撞箱组件 (minecraft:collision_box)
        
        Args:
            origin: 原点 [-8, 0, -8]
            size: 尺寸 [16, 16, 16]
            enabled: 是否启用
        """
        if origin is None:
            origin = [-8, 0, -8]
        if size is None:
            size = [16, 16, 16]
        return {
            "minecraft:collision_box": {
                "origin": origin,
                "size": size
            }
        }
    
    @staticmethod
    def generate_selection_box_component(
        origin: list = None,
        size: list = None
    ) -> Dict[str, Any]:
        """
        生成选择箱组件 (minecraft:selection_box)
        
        Args:
            origin: 原点 [-8, 0, -8]
            size: 尺寸 [16, 16, 16]
        """
        if origin is None:
            origin = [-8, 0, -8]
        if size is None:
            size = [16, 16, 16]
        return {
            "minecraft:selection_box": {
                "origin": origin,
                "size": size
            }
        }
    
    @staticmethod
    def generate_placement_filter_component(
        conditions: list = None
    ) -> Dict[str, Any]:
        """
        生成放置过滤组件 (minecraft:placement_filter)
        
        Args:
            conditions: 放置条件列表
                [{"allowed_faces": ["up"], "block_filter": ["minecraft:grass"]}]
        """
        if conditions is None:
            conditions = [{"allowed_faces": ["up", "down", "north", "south", "east", "west"]}]
        return {
            "minecraft:placement_filter": {
                "conditions": conditions
            }
        }
    
    @staticmethod
    def generate_loot_component(loot_table: str) -> Dict[str, Any]:
        """
        生成战利品表组件 (minecraft:loot)
        
        Args:
            loot_table: 战利品表路径（如 loot_tables/blocks/my_block.json）
        """
        return {"minecraft:loot": loot_table}
    
    @staticmethod
    def generate_destructible_by_mining_component(
        seconds_to_destroy: float = 1.0
    ) -> Dict[str, Any]:
        """
        生成可挖掘破坏组件 (minecraft:destructible_by_mining)
        
        Args:
            seconds_to_destroy: 破坏时间（秒）
        """
        return {
            "minecraft:destructible_by_mining": {
                "seconds_to_destroy": seconds_to_destroy
            }
        }
    
    @staticmethod
    def generate_destructible_by_explosion_component(
        explosion_resistance: float = 1.0
    ) -> Dict[str, Any]:
        """
        生成可爆炸破坏组件 (minecraft:destructible_by_explosion)
        
        Args:
            explosion_resistance: 爆炸抗性值
        """
        return {
            "minecraft:destructible_by_explosion": {
                "explosion_resistance": explosion_resistance
            }
        }
    
    @staticmethod
    def generate_display_name_component(value: str) -> Dict[str, Any]:
        """
        生成显示名称组件 (minecraft:display_name)
        
        Args:
            value: 显示名称（支持本地化键）
        """
        return {"minecraft:display_name": value}
    
    @staticmethod
    def generate_breathability_component(value: str = "solid") -> Dict[str, Any]:
        """
        生成呼吸性组件 (minecraft:breathability)
        
        Args:
            value: 呼吸类型（solid/air）
        """
        return {"minecraft:breathability": value}


def generate_pickaxe_item_json(
    namespace: str,
    item_id: str,
    durability: int = 131,
    mining_speed: int = 4,
    enchantability: int = 15,
    destroy_speeds: list = None,
    repair_material: str = None
) -> Dict[str, str]:
    """
    生成镐类物品 JSON
    
    Args:
        namespace: 命名空间
        item_id: 物品ID
        durability: 耐久值
        mining_speed: 挖掘速度
        enchantability: 附魔等级
        destroy_speeds: 挖掘速度列表
        repair_material: 修复材料
    """
    if destroy_speeds is None:
        destroy_speeds = [
            {"block": {"tags": "q.any_tag('stone', 'metal')"},"speed": mining_speed}
        ]
    
    components = {
        "minecraft:hand_equipped": True,
        "minecraft:stacked_by_data": True,
        "minecraft:max_stack_size": 1
    }
    components.update(BedrockComponentsGenerator.generate_durability_component(durability))
    components.update(BedrockComponentsGenerator.generate_digger_component(destroy_speeds))
    components.update(BedrockComponentsGenerator.generate_enchantable_component("pickaxe", enchantability))
    
    if repair_material:
        components.update(BedrockComponentsGenerator.generate_repairable_component([
            {"items": [repair_material], "repair_amount": durability // 4}
        ]))
    
    return generate_item_json(namespace, item_id, components=components)


def generate_food_item_json(
    namespace: str,
    item_id: str,
    nutrition: int = 4,
    saturation: str = "normal",
    can_always_eat: bool = False,
    effects: list = None
) -> Dict[str, str]:
    """
    生成食物物品 JSON
    
    Args:
        namespace: 命名空间
        item_id: 物品ID
        nutrition: 饥饿值
        saturation: 饱和度
        can_always_eat: 是否可随时食用
        effects: 效果列表
    """
    components = {
        "minecraft:use_animation": "eat",
        "minecraft:use_duration": 1.6
    }
    components.update(BedrockComponentsGenerator.generate_food_component(
        nutrition, saturation, can_always_eat, effects=effects
    ))
    
    return generate_item_json(namespace, item_id, components=components)


def generate_armor_item_json(
    namespace: str,
    item_id: str,
    slot: str = "slot.armor.chest",
    protection: int = 5,
    durability: int = 165,
    enchantability: int = 9,
    repair_material: str = None
) -> Dict[str, str]:
    """
    生成盔甲物品 JSON
    
    Args:
        namespace: 命名空间
        item_id: 物品ID
        slot: 穿戴槽位
        protection: 护甲值
        durability: 耐久值
        enchantability: 附魔等级
        repair_material: 修复材料
    """
    # 根据槽位确定附魔类型
    slot_to_enchant = {
        "slot.armor.head": "armor_head",
        "slot.armor.chest": "armor_torso",
        "slot.armor.legs": "armor_legs",
        "slot.armor.feet": "armor_feet"
    }
    enchant_slot = slot_to_enchant.get(slot, "armor_torso")
    
    components = {
        "minecraft:max_stack_size": 1,
        "minecraft:stacked_by_data": True
    }
    components.update(BedrockComponentsGenerator.generate_wearable_component(slot, protection))
    components.update(BedrockComponentsGenerator.generate_armor_component(protection))
    components.update(BedrockComponentsGenerator.generate_durability_component(durability))
    components.update(BedrockComponentsGenerator.generate_enchantable_component(enchant_slot, enchantability))
    
    if repair_material:
        components.update(BedrockComponentsGenerator.generate_repairable_component([
            {"items": [repair_material], "repair_amount": durability // 4}
        ]))
    
    return generate_item_json(namespace, item_id, components=components)


def generate_throwable_item_json(
    namespace: str,
    item_id: str,
    projectile_entity: str,
    max_draw_duration: float = 0.0,
    launch_power: float = 1.0
) -> Dict[str, str]:
    """
    生成可投掷物品 JSON
    
    Args:
        namespace: 命名空间
        item_id: 物品ID
        projectile_entity: 投掷出的实体
        max_draw_duration: 最大蓄力时间
        launch_power: 发射力度
    """
    components = {}
    components.update(BedrockComponentsGenerator.generate_throwable_component(
        max_draw_duration=max_draw_duration,
        max_launch_power=launch_power
    ))
    components.update(BedrockComponentsGenerator.generate_projectile_component(projectile_entity))
    
    return generate_item_json(namespace, item_id, components=components)


def generate_bow_item_json(
    namespace: str,
    item_id: str,
    durability: int = 384,
    max_draw_duration: float = 1.0,
    enchantability: int = 1
) -> Dict[str, str]:
    """
    生成弓类物品 JSON
    
    Args:
        namespace: 命名空间
        item_id: 物品ID
        durability: 耐久值
        max_draw_duration: 最大蓄力时间
        enchantability: 附魔等级
    """
    components = {
        "minecraft:max_stack_size": 1,
        "minecraft:use_animation": "bow"
    }
    components.update(BedrockComponentsGenerator.generate_durability_component(durability))
    components.update(BedrockComponentsGenerator.generate_shooter_component(
        max_draw_duration=max_draw_duration
    ))
    components.update(BedrockComponentsGenerator.generate_chargeable_component())
    components.update(BedrockComponentsGenerator.generate_enchantable_component("bow", enchantability))
    
    return generate_item_json(namespace, item_id, components=components)


def generate_axe_item_json(
    namespace: str,
    item_id: str,
    damage: int = 4,
    durability: int = 131,
    mining_speed: int = 4,
    enchantability: int = 15,
    repair_material: str = None
) -> Dict[str, str]:
    """
    生成斧类物品 JSON
    """
    destroy_speeds = [
        {"block": {"tags": "q.any_tag('wood', 'log')"},"speed": mining_speed}
    ]
    components = {
        "minecraft:damage": damage,
        "minecraft:hand_equipped": True,
        "minecraft:stacked_by_data": True,
        "minecraft:max_stack_size": 1
    }
    components.update(BedrockComponentsGenerator.generate_durability_component(durability))
    components.update(BedrockComponentsGenerator.generate_digger_component(destroy_speeds))
    components.update(BedrockComponentsGenerator.generate_weapon_component())
    components.update(BedrockComponentsGenerator.generate_enchantable_component("axe", enchantability))
    
    if repair_material:
        components.update(BedrockComponentsGenerator.generate_repairable_component([
            {"items": [repair_material], "repair_amount": durability // 4}
        ]))
    
    return generate_item_json(namespace, item_id, components=components)


def generate_shovel_item_json(
    namespace: str,
    item_id: str,
    durability: int = 131,
    mining_speed: int = 4,
    enchantability: int = 15,
    repair_material: str = None
) -> Dict[str, str]:
    """
    生成锹类物品 JSON
    """
    destroy_speeds = [
        {"block": {"tags": "q.any_tag('dirt', 'sand', 'gravel', 'snow')"},"speed": mining_speed}
    ]
    components = {
        "minecraft:hand_equipped": True,
        "minecraft:stacked_by_data": True,
        "minecraft:max_stack_size": 1
    }
    components.update(BedrockComponentsGenerator.generate_durability_component(durability))
    components.update(BedrockComponentsGenerator.generate_digger_component(destroy_speeds))
    components.update(BedrockComponentsGenerator.generate_enchantable_component("shovel", enchantability))
    
    if repair_material:
        components.update(BedrockComponentsGenerator.generate_repairable_component([
            {"items": [repair_material], "repair_amount": durability // 4}
        ]))
    
    return generate_item_json(namespace, item_id, components=components)


def generate_hoe_item_json(
    namespace: str,
    item_id: str,
    durability: int = 131,
    enchantability: int = 15,
    repair_material: str = None
) -> Dict[str, str]:
    """
    生成锄类物品 JSON
    """
    components = {
        "minecraft:hand_equipped": True,
        "minecraft:stacked_by_data": True,
        "minecraft:max_stack_size": 1
    }
    components.update(BedrockComponentsGenerator.generate_durability_component(durability))
    components.update(BedrockComponentsGenerator.generate_enchantable_component("hoe", enchantability))
    
    if repair_material:
        components.update(BedrockComponentsGenerator.generate_repairable_component([
            {"items": [repair_material], "repair_amount": durability // 4}
        ]))
    
    return generate_item_json(namespace, item_id, components=components)
