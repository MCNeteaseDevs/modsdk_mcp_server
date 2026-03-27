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
    
    # 实体预设组件（按玩法场景自动添加相关行为组件）
    ENTITY_PRESETS = {
        "mount": {
            "minecraft:rideable": {
                "seat_count": 1,
                "family_types": ["player"],
                "interact_text": "action.interact.ride"
            },
            "minecraft:tameable": {
                "probability": 0.33
            },
            "minecraft:behavior.follow_owner": {
                "priority": 4,
                "speed_multiplier": 1.0,
                "start_distance": 10,
                "stop_distance": 2
            },
            "minecraft:input_ground_controlled": {}
        },
        "pet": {
            "minecraft:behavior.follow_owner": {
                "priority": 4,
                "speed_multiplier": 1.0,
                "start_distance": 10,
                "stop_distance": 2
            },
            "minecraft:behavior.owner_hurt_by_target": {
                "priority": 1
            },
            "minecraft:behavior.owner_hurt_target": {
                "priority": 2
            },
            "minecraft:tameable": {
                "probability": 1.0
            },
            "minecraft:is_tamed": {}
        },
        "npc": {
            "minecraft:damage_sensor": {
                "triggers": [{"deals_damage": False}]
            },
            "minecraft:pushable": {
                "is_pushable": False,
                "is_pushable_by_piston": False
            }
        },
        "hostile": {
            "minecraft:behavior.melee_attack": {
                "priority": 3,
                "speed_multiplier": 1.2,
                "track_target": True
            },
            "minecraft:behavior.nearest_attackable_target": {
                "priority": 2,
                "within_radius": 25.0,
                "entity_types": [{"filters": {"test": "is_family", "subject": "other", "value": "player"}}]
            },
            "minecraft:behavior.hurt_by_target": {
                "priority": 1
            }
        }
    }

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
        components: Optional[Dict[str, Any]] = None,
        preset: str = None
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
            preset: 实体预设(mount/pet/npc/hostile)，自动添加相关行为组件
        """
        import json

        # 合并预设组件和用户指定组件
        merged_components = {}
        if preset and preset in EntityJsonGenerator.ENTITY_PRESETS:
            merged_components.update(EntityJsonGenerator.ENTITY_PRESETS[preset])
            # NPC预设：移动速度设为0
            if preset == "npc":
                movement_speed = 0
        if components:
            merged_components.update(components)  # 用户指定的优先级更高

        if family is None:
            family = [entity_id]
        family_str = ", ".join(['"{}"'.format(f) for f in family])
        
        # 默认 runtime_identifier 使用 minecraft:{entity_id}
        if runtime_identifier is None:
            runtime_identifier = "minecraft:{}".format(entity_id.lower())
        
        additional = ""
        if merged_components:
            for key, value in merged_components.items():
                if isinstance(value, bool):
                    additional += ',\n            "{}": {}'.format(key, str(value).lower())
                elif isinstance(value, (dict, list)):
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
                     'family', 'is_spawnable', 'is_summonable', 'runtime_identifier', 'components', 'preset']
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


# ============================================================================
# 高级物品生成 - 统一配置与工厂函数
# ============================================================================

# 物品类型配置表：每种类型的默认参数和组件构建规则
ITEM_TYPE_CONFIGS = {
    "sword": {
        "defaults": {"damage": 5, "durability": 131, "enchantability": 15},
        "enchant_slot": "sword",
        "base_components": {
            "minecraft:damage": "damage",
            "minecraft:hand_equipped": True,
            "minecraft:stacked_by_data": True,
            "minecraft:max_stack_size": 1,
        },
        "features": ["durability", "weapon", "enchantable"],
        "repair_amount": "formula",  # 使用公式而非整数
    },
    "pickaxe": {
        "defaults": {"durability": 131, "mining_speed": 4, "enchantability": 15},
        "enchant_slot": "pickaxe",
        "base_components": {
            "minecraft:hand_equipped": True,
            "minecraft:stacked_by_data": True,
            "minecraft:max_stack_size": 1,
        },
        "dig_tags": "q.any_tag('stone', 'metal')",
        "features": ["durability", "digger", "enchantable"],
        "repair_amount": "quarter",
    },
    "axe": {
        "defaults": {"damage": 4, "durability": 131, "mining_speed": 4, "enchantability": 15},
        "enchant_slot": "axe",
        "base_components": {
            "minecraft:damage": "damage",
            "minecraft:hand_equipped": True,
            "minecraft:stacked_by_data": True,
            "minecraft:max_stack_size": 1,
        },
        "dig_tags": "q.any_tag('wood', 'log')",
        "features": ["durability", "digger", "weapon", "enchantable"],
        "repair_amount": "quarter",
    },
    "shovel": {
        "defaults": {"durability": 131, "mining_speed": 4, "enchantability": 15},
        "enchant_slot": "shovel",
        "base_components": {
            "minecraft:hand_equipped": True,
            "minecraft:stacked_by_data": True,
            "minecraft:max_stack_size": 1,
        },
        "dig_tags": "q.any_tag('dirt', 'sand', 'gravel', 'snow')",
        "features": ["durability", "digger", "enchantable"],
        "repair_amount": "quarter",
    },
    "hoe": {
        "defaults": {"durability": 131, "enchantability": 15},
        "enchant_slot": "hoe",
        "base_components": {
            "minecraft:hand_equipped": True,
            "minecraft:stacked_by_data": True,
            "minecraft:max_stack_size": 1,
        },
        "features": ["durability", "enchantable"],
        "repair_amount": "quarter",
    },
    "food": {
        "defaults": {"nutrition": 4, "saturation": "normal", "can_always_eat": False},
        "base_components": {
            "minecraft:use_animation": "eat",
            "minecraft:use_duration": 1.6,
        },
        "features": ["food"],
    },
    "armor": {
        "defaults": {"slot": "slot.armor.chest", "protection": 5, "durability": 165, "enchantability": 9},
        "base_components": {
            "minecraft:max_stack_size": 1,
            "minecraft:stacked_by_data": True,
        },
        "features": ["wearable", "armor", "durability", "enchantable"],
        "repair_amount": "quarter",
        "slot_to_enchant": {
            "slot.armor.head": "armor_head",
            "slot.armor.chest": "armor_torso",
            "slot.armor.legs": "armor_legs",
            "slot.armor.feet": "armor_feet",
        },
    },
    "bow": {
        "defaults": {"durability": 384, "max_draw_duration": 1.0, "enchantability": 1},
        "enchant_slot": "bow",
        "base_components": {
            "minecraft:max_stack_size": 1,
            "minecraft:use_animation": "bow",
        },
        "features": ["durability", "shooter", "chargeable", "enchantable"],
    },
    "throwable": {
        "defaults": {"max_draw_duration": 0.0, "launch_power": 1.0},
        "features": ["throwable", "projectile"],
    },
}


def generate_typed_item_json(item_type: str, namespace: str, item_id: str, **kwargs) -> Dict[str, str]:
    """
    统一的物品 JSON 生成函数，根据 item_type 从 ITEM_TYPE_CONFIGS 构建组件。

    Args:
        item_type: 物品类型 (sword/pickaxe/axe/shovel/hoe/food/armor/bow/throwable)
        namespace: 命名空间
        item_id: 物品ID
        **kwargs: 覆盖默认参数（如 damage, durability, enchantability 等）
    """
    config = ITEM_TYPE_CONFIGS[item_type]
    defaults = config["defaults"]

    # 合并默认值与用户参数
    params = {k: kwargs.get(k, v) for k, v in defaults.items()}

    # 构建基础组件
    components = {}
    for key, value in config.get("base_components", {}).items():
        if isinstance(value, str) and value in params:
            components[key] = params[value]
        else:
            components[key] = value

    # 按 features 列表添加组件
    features = config.get("features", [])
    gen = BedrockComponentsGenerator

    if "durability" in features:
        components.update(gen.generate_durability_component(params["durability"]))

    if "weapon" in features:
        components.update(gen.generate_weapon_component())

    if "digger" in features:
        destroy_speeds = kwargs.get("destroy_speeds")
        if destroy_speeds is None:
            destroy_speeds = [{"block": {"tags": config["dig_tags"]}, "speed": params["mining_speed"]}]
        components.update(gen.generate_digger_component(destroy_speeds))

    if "food" in features:
        components.update(gen.generate_food_component(
            params["nutrition"], params["saturation"], params["can_always_eat"],
            effects=kwargs.get("effects")
        ))

    if "wearable" in features:
        components.update(gen.generate_wearable_component(params["slot"], params["protection"]))

    if "armor" in features:
        components.update(gen.generate_armor_component(params["protection"]))

    if "shooter" in features:
        components.update(gen.generate_shooter_component(max_draw_duration=params["max_draw_duration"]))

    if "chargeable" in features:
        components.update(gen.generate_chargeable_component())

    if "throwable" in features:
        components.update(gen.generate_throwable_component(
            max_draw_duration=params["max_draw_duration"],
            max_launch_power=params["launch_power"]
        ))

    if "projectile" in features:
        components.update(gen.generate_projectile_component(kwargs.get("projectile_entity", "minecraft:arrow")))

    if "enchantable" in features:
        enchant_slot = config.get("enchant_slot")
        if enchant_slot is None and "slot_to_enchant" in config:
            enchant_slot = config["slot_to_enchant"].get(params["slot"], "armor_torso")
        components.update(gen.generate_enchantable_component(enchant_slot, params["enchantability"]))

    # 修复材料
    repair_material = kwargs.get("repair_material")
    if repair_material and config.get("repair_amount"):
        if config["repair_amount"] == "formula":
            amount = "context.other->query.remaining_durability + 0.05 * context.other->query.max_durability"
        else:  # "quarter"
            amount = params["durability"] // 4
        components.update(gen.generate_repairable_component([
            {"items": [repair_material], "repair_amount": amount}
        ]))

    return generate_item_json(namespace, item_id, components=components)


# ============================================================================
# 向后兼容的薄包装函数
# ============================================================================

def generate_sword_item_json(namespace: str, item_id: str, **kwargs) -> Dict[str, str]:
    """生成剑类物品 JSON（向后兼容包装）"""
    return generate_typed_item_json("sword", namespace, item_id, **kwargs)


def generate_pickaxe_item_json(namespace: str, item_id: str, **kwargs) -> Dict[str, str]:
    """生成镐类物品 JSON（向后兼容包装）"""
    return generate_typed_item_json("pickaxe", namespace, item_id, **kwargs)


def generate_axe_item_json(namespace: str, item_id: str, **kwargs) -> Dict[str, str]:
    """生成斧类物品 JSON（向后兼容包装）"""
    return generate_typed_item_json("axe", namespace, item_id, **kwargs)


def generate_shovel_item_json(namespace: str, item_id: str, **kwargs) -> Dict[str, str]:
    """生成锹类物品 JSON（向后兼容包装）"""
    return generate_typed_item_json("shovel", namespace, item_id, **kwargs)


def generate_hoe_item_json(namespace: str, item_id: str, **kwargs) -> Dict[str, str]:
    """生成锄类物品 JSON（向后兼容包装）"""
    return generate_typed_item_json("hoe", namespace, item_id, **kwargs)


def generate_food_item_json(namespace: str, item_id: str, **kwargs) -> Dict[str, str]:
    """生成食物物品 JSON（向后兼容包装）"""
    return generate_typed_item_json("food", namespace, item_id, **kwargs)


def generate_armor_item_json(namespace: str, item_id: str, **kwargs) -> Dict[str, str]:
    """生成盔甲物品 JSON（向后兼容包装）"""
    return generate_typed_item_json("armor", namespace, item_id, **kwargs)


def generate_bow_item_json(namespace: str, item_id: str, **kwargs) -> Dict[str, str]:
    """生成弓类物品 JSON（向后兼容包装）"""
    return generate_typed_item_json("bow", namespace, item_id, **kwargs)


def generate_throwable_item_json(namespace: str, item_id: str, **kwargs) -> Dict[str, str]:
    """生成可投掷物品 JSON（向后兼容包装）"""
    return generate_typed_item_json("throwable", namespace, item_id, **kwargs)
