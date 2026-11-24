# -*- coding: utf-8 -*-
"""
NetEase ModSDK 项目骨架、Python 脚本与数据驱动 JSON 生成器。

设计原则：
1. 默认采用现代单组件仓库标准双包目录 `behavior_pack/` 与 `resource_pack/`，
   同时支持通过 `behavior_pack_dir` / `resource_pack_dir` 适配带后缀目录（如 MCStudio 项目）。
2. 所有 JSON 产物统一通过结构化字典与 `json.dumps` 序列化，杜绝字符串拼接导致的重复键或转义错误。
3. 所有自定义物品严格遵循网易官方 `format_version: "1.10"` 与 `netease:*` 组件契约；
   所有包清单严格采用最新 `manifest.json`（`format_version: 2`）规范。
"""

from __future__ import annotations

import json
import re
import uuid
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


DEFAULT_BEHAVIOR_PACK_DIR = "behavior_pack"
DEFAULT_RESOURCE_PACK_DIR = "resource_pack"
DEFAULT_MIN_ENGINE_VERSION: Tuple[int, int, int] = (1, 18, 0)

BLOCK_FORMAT_PROFILES: Dict[str, str] = {
    "legacy_1_10": "1.10.0",
    "scalar_1_16": "1.16.0",
    "modern_1_19_20": "1.19.20",
}

_LOWER_IDENTIFIER_RE = re.compile(r"^[a-z][a-z0-9_]*$")
_NAMESPACED_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_.-]*:[a-z0-9][a-z0-9_./-]*$")
_INVALID_DIR_CHARS = set('/\\:*?"<>|')


# ============================================================================
# 基础校验与目录规范化工具
# ============================================================================

def get_project_folder_name(mod_id: str) -> str:
    """返回行为包下的 Python 脚本根目录名（`{mod_id}_Script`）。"""
    return "{}_Script".format(mod_id)


def to_camel_case(identifier: str) -> str:
    """将下划线/连字符标识符转为大驼峰类名。"""
    return "".join(word.capitalize() for word in identifier.replace("-", "_").split("_") if word)


def validate_mod_id(mod_id: str, field_name: str = "mod_id") -> str:
    """校验 mod_id / namespace：必须同时满足合法小写命名空间与 Python 包名要求。"""
    value = str(mod_id or "").strip()
    if not _LOWER_IDENTIFIER_RE.fullmatch(value):
        raise ValueError(
            "{} 必须以小写字母开头且仅包含小写字母、数字和下划线（如 'my_mod'），当前为 {!r}".format(
                field_name, mod_id
            )
        )
    return value


def validate_content_id(content_id: str, field_name: str = "id") -> str:
    """校验物品/方块/实体/配方的短标识符（不含命名空间）。"""
    value = str(content_id or "").strip().lower()
    if not _LOWER_IDENTIFIER_RE.fullmatch(value):
        raise ValueError(
            "{} 必须以小写字母开头且仅包含小写字母、数字和下划线，当前为 {!r}".format(
                field_name, content_id
            )
        )
    return value


def normalize_pack_dir(pack_dir: Optional[str], default_dir: str, label: str = "pack_dir") -> str:
    """规范化行为包或资源包根目录名（单级相对目录名，不含路径穿越）。"""
    if pack_dir is None or not str(pack_dir).strip():
        return default_dir
    cleaned = str(pack_dir).strip().strip("/\\")
    if (
        not cleaned
        or cleaned in {".", ".."}
        or ".." in cleaned
        or any(ch in _INVALID_DIR_CHARS or ord(ch) < 32 for ch in cleaned)
    ):
        raise ValueError("{} 必须是合法的单层包目录名称，当前为 {!r}".format(label, pack_dir))
    return cleaned


def resolve_pack_dirs(
    behavior_pack_dir: Optional[str] = None,
    resource_pack_dir: Optional[str] = None,
) -> Tuple[str, str]:
    """统一解析行为包与资源包目录名。"""
    return (
        normalize_pack_dir(behavior_pack_dir, DEFAULT_BEHAVIOR_PACK_DIR, "behavior_pack_dir"),
        normalize_pack_dir(resource_pack_dir, DEFAULT_RESOURCE_PACK_DIR, "resource_pack_dir"),
    )


def parse_version_triplet(
    version: Any = "1.0.0",
    field_name: str = "version",
) -> List[int]:
    """将 '1.0.0' 或 [1, 0, 0] 解析为三元非负整数版本号列表。"""
    if isinstance(version, (list, tuple)):
        parts = list(version)
    elif isinstance(version, str):
        raw = [seg.strip() for seg in version.strip().split(".") if seg.strip()]
        if len(raw) != 3 or any(not seg.isdigit() for seg in raw):
            raise ValueError("{} 必须采用 '主.次.修订' 三段非负整数格式（如 '1.0.0'），当前为 {!r}".format(field_name, version))
        parts = [int(seg) for seg in raw]
    else:
        raise ValueError("{} 格式无效：{!r}".format(field_name, version))

    if len(parts) != 3 or any(type(x) is not int or x < 0 for x in parts):
        raise ValueError("{} 必须是包含 3 个非负整数的版本号，当前为 {!r}".format(field_name, version))
    return parts


def _dump_json(data: Any) -> str:
    """统一生成带 4 空格缩进的 UTF-8 JSON 文本。"""
    return json.dumps(data, ensure_ascii=False, indent=4)


def render_bundle_markdown(
    title: str,
    files: Mapping[str, str],
    notes: Optional[Sequence[str]] = None,
    extra_sections: Optional[Sequence[Tuple[str, str]]] = None,
) -> str:
    """将多文件生成包渲染为结构清晰的 Markdown 输出。"""
    lines: List[str] = ["## {}".format(title), ""]
    if notes:
        lines.append("### 结构与合并说明")
        lines.append("")
        for note in notes:
            lines.append("- {}".format(note))
        lines.append("")

    for filepath, content in files.items():
        lowered = filepath.lower()
        if lowered.endswith(".py"):
            fence = "python"
        elif lowered.endswith(".json"):
            fence = "json"
        else:
            fence = "text"
        lines.append("### `{}`".format(filepath))
        lines.append("")
        lines.append("```{}".format(fence))
        lines.append(content.rstrip("\n"))
        lines.append("```")
        lines.append("")

    if extra_sections:
        for heading, body in extra_sections:
            lines.append("### {}".format(heading))
            lines.append("")
            lines.append(body.rstrip("\n"))
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


# ============================================================================
# 清单与配套索引构造函数（最新 manifest.json format_version: 2）
# ============================================================================

def build_pack_manifest_dict(
    pack_name: str,
    description: str,
    module_type: str,
    header_uuid: Optional[str] = None,
    module_uuid: Optional[str] = None,
    version: Sequence[int] = (1, 0, 0),
    min_engine_version: Sequence[int] = DEFAULT_MIN_ENGINE_VERSION,
    dependencies: Optional[Sequence[Mapping[str, Any]]] = None,
) -> Dict[str, Any]:
    """构建符合网易最新规范（format_version: 2）的 manifest.json 字典。"""
    if module_type not in {"data", "resources"}:
        raise ValueError("manifest module_type 仅支持 'data' 或 'resources'，当前为 {!r}".format(module_type))
    ver_list = parse_version_triplet(version, "version")
    min_engine_list = parse_version_triplet(min_engine_version, "min_engine_version")
    clean_name = str(pack_name or "").strip() or ("behavior_pack" if module_type == "data" else "resource_pack")
    clean_desc = str(description or "").strip() or clean_name

    manifest: Dict[str, Any] = {
        "format_version": 2,
        "header": {
            "name": clean_name,
            "description": clean_desc,
            "uuid": str(header_uuid or uuid.uuid4()),
            "version": ver_list,
            "min_engine_version": min_engine_list,
        },
        "modules": [
            {
                "description": clean_desc,
                "type": module_type,
                "uuid": str(module_uuid or uuid.uuid4()),
                "version": ver_list,
            }
        ],
    }
    if dependencies:
        manifest["dependencies"] = [
            {
                "uuid": str(dep["uuid"]),
                "version": parse_version_triplet(dep.get("version", ver_list), "dependencies.version"),
            }
            for dep in dependencies
        ]
    return manifest


def generate_manifest_json(
    pack_name: str,
    description: str = "",
    pack_type: str = "both",
    version: Any = "1.0.0",
    min_engine_version: Any = DEFAULT_MIN_ENGINE_VERSION,
    behavior_pack_dir: Optional[str] = None,
    resource_pack_dir: Optional[str] = None,
    resource_pack_uuid: Optional[str] = None,
) -> Dict[str, str]:
    """生成最新标准 `manifest.json`（支持行为包、资源包或双包自动绑定依赖）。"""
    if pack_type not in {"both", "behavior", "resource"}:
        raise ValueError("pack_type 必须为 'both'、'behavior' 或 'resource'")
    bp_dir, rp_dir = resolve_pack_dirs(behavior_pack_dir, resource_pack_dir)
    ver_list = parse_version_triplet(version, "version")
    min_engine_list = parse_version_triplet(min_engine_version, "min_engine_version")
    clean_name = str(pack_name or "").strip()
    if not clean_name:
        raise ValueError("pack_name 不能为空")
    clean_desc = str(description or "").strip() or clean_name

    files: Dict[str, str] = {}
    rp_header_id = str(resource_pack_uuid or uuid.uuid4())

    if pack_type in {"both", "resource"}:
        rp_manifest = build_pack_manifest_dict(
            pack_name="{} Resources".format(clean_name) if pack_type == "both" else clean_name,
            description="{} 资源包".format(clean_desc) if pack_type == "both" else clean_desc,
            module_type="resources",
            header_uuid=rp_header_id,
            version=ver_list,
            min_engine_version=min_engine_list,
        )
        files["{}/manifest.json".format(rp_dir)] = _dump_json(rp_manifest)

    if pack_type in {"both", "behavior"}:
        deps = None
        if pack_type == "both" or resource_pack_uuid:
            deps = [{"uuid": rp_header_id, "version": ver_list}]
        bp_manifest = build_pack_manifest_dict(
            pack_name="{} Behaviors".format(clean_name) if pack_type == "both" else clean_name,
            description="{} 行为包".format(clean_desc) if pack_type == "both" else clean_desc,
            module_type="data",
            version=ver_list,
            min_engine_version=min_engine_list,
            dependencies=deps,
        )
        # 保证双包输出顺序：行为包在前、资源包在后
        ordered: Dict[str, str] = {"{}/manifest.json".format(bp_dir): _dump_json(bp_manifest)}
        ordered.update(files)
        files = ordered

    return files


def build_item_texture_json(namespace: str, texture_entries: Mapping[str, Any]) -> str:
    """构建 `resource_pack/textures/item_texture.json`。"""
    return _dump_json({
        "resource_pack_name": namespace,
        "texture_name": "atlas.items",
        "texture_data": dict(texture_entries),
    })


def build_terrain_texture_json(namespace: str, texture_entries: Mapping[str, Any]) -> str:
    """构建 `resource_pack/textures/terrain_texture.json`。"""
    return _dump_json({
        "resource_pack_name": namespace,
        "texture_name": "atlas.terrain",
        "padding": 8,
        "num_mip_levels": 4,
        "texture_data": dict(texture_entries),
    })


def build_blocks_json(entries: Mapping[str, Any]) -> str:
    """构建 `resource_pack/blocks.json`。"""
    payload: Dict[str, Any] = {"format_version": [1, 1, 0]}
    payload.update(entries)
    return _dump_json(payload)


def build_languages_json(languages: Sequence[str] = ("zh_CN",)) -> str:
    """构建 `resource_pack/texts/languages.json`。"""
    return _dump_json(list(languages))


# ============================================================================
# Python 代码模板（严格兼容 Python 2.7 与导入白名单）
# ============================================================================

MOD_CONFIG_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{mod_name} 共享配置常量（双端可安全导入，禁止在此导入单端 API）
"""

MOD_NAME = "{mod_id}"
MOD_VERSION = "{version}"
SCRIPT_DIR = "{project_folder}"

SERVER_SYSTEM_NAME = "{class_name}ServerSystem"
CLIENT_SYSTEM_NAME = "{class_name}ClientSystem"

SERVER_SYSTEM_PATH = "{project_folder}.serverSystem.{class_name}ServerSystem"
CLIENT_SYSTEM_PATH = "{project_folder}.clientSystem.{class_name}ClientSystem"

# 自定义跨端事件名
EVENT_PLAYER_WELCOME = "PlayerWelcome"
'''


MOD_MAIN_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{mod_name} - 我的世界中国版 Mod 入口
作者: {author}
描述: {description}
"""
from __future__ import print_function

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi
from {project_folder} import modConfig


@Mod.Binding(name=modConfig.SCRIPT_DIR, version=modConfig.MOD_VERSION)
class {class_name}Mod(object):
    def __init__(self):
        pass

    @Mod.InitServer()
    def initServer(self):
        """服务端系统注册"""
        serverApi.RegisterSystem(
            modConfig.MOD_NAME,
            modConfig.SERVER_SYSTEM_NAME,
            modConfig.SERVER_SYSTEM_PATH
        )

    @Mod.DestroyServer()
    def destroyServer(self):
        """服务端销毁"""
        pass

    @Mod.InitClient()
    def initClient(self):
        """客户端系统注册"""
        clientApi.RegisterSystem(
            modConfig.MOD_NAME,
            modConfig.CLIENT_SYSTEM_NAME,
            modConfig.CLIENT_SYSTEM_PATH
        )

    @Mod.DestroyClient()
    def destroyClient(self):
        """客户端销毁"""
        pass
'''


PROJECT_SERVER_SYSTEM_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{mod_name} 服务端系统
遵循 NetEase ModSDK 规范：仅导入 serverApi，严禁跨端导入 clientApi。
"""
from __future__ import print_function

import mod.server.extraServerApi as serverApi
from {project_folder} import modConfig

CF = serverApi.GetEngineCompFactory()
ServerSystem = serverApi.GetServerSystemCls()

TICK_INTERVAL = 20


class {class_name}ServerSystem(ServerSystem):
    """服务端系统"""

    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.tick = 0
        self._init_events()

    def _init_events(self):
        engine_ns = serverApi.GetEngineNamespace()
        engine_sys = serverApi.GetEngineSystemName()
        self.ListenForEvent(engine_ns, engine_sys, "AddServerPlayerEvent", self, self.on_player_join)
        self.ListenForEvent(engine_ns, engine_sys, "ClientLoadAddonsFinishServerEvent", self, self.on_client_addons_ready)
        self.ListenForEvent(engine_ns, engine_sys, "DelServerPlayerEvent", self, self.on_player_leave)

    def Destroy(self):
        self.UnListenAllEvents()

    def on_player_join(self, args):
        """玩家加入服务端（此时客户端 Mod 尚未加载完毕，请勿在此处 NotifyToClient）"""
        player_id = args.get("id")
        if not player_id:
            return
        name_comp = CF.CreateName(player_id)
        player_name = name_comp.GetName() if name_comp else player_id
        print("[{mod_name}] 玩家加入服务端: {{}} ({{}})".format(player_name, player_id))

    def on_client_addons_ready(self, args):
        """客户端 Mod 加载完成，可安全向客户端发送初始化同步事件"""
        player_id = args.get("playerId")
        if not player_id:
            return
        self.NotifyToClient(
            player_id,
            modConfig.EVENT_PLAYER_WELCOME,
            {{"message": "欢迎来到 {mod_name}！"}}
        )

    def on_player_leave(self, args):
        player_id = args.get("id")
        if not player_id:
            return
        print("[{mod_name}] 玩家离开: {{}}".format(player_id))

    def on_tick(self, args=None):
        self.tick += 1
        if self.tick % TICK_INTERVAL != 0:
            return
'''


PROJECT_CLIENT_SYSTEM_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{mod_name} 客户端系统
遵循 NetEase ModSDK 规范：仅导入 clientApi，严禁跨端导入 serverApi。
"""
from __future__ import print_function

import mod.client.extraClientApi as clientApi
from {project_folder} import modConfig

CF = clientApi.GetEngineCompFactory()
ClientSystem = clientApi.GetClientSystemCls()


class {class_name}ClientSystem(ClientSystem):
    """客户端系统"""

    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self._init_events()

    def _init_events(self):
        engine_ns = clientApi.GetEngineNamespace()
        engine_sys = clientApi.GetEngineSystemName()
        self.ListenForEvent(engine_ns, engine_sys, "UiInitFinished", self, self.on_ui_init_finished)
        self.ListenForEvent(
            modConfig.MOD_NAME,
            modConfig.SERVER_SYSTEM_NAME,
            modConfig.EVENT_PLAYER_WELCOME,
            self,
            self.on_player_welcome
        )

    def Destroy(self):
        self.UnListenAllEvents()

    def on_ui_init_finished(self, args):
        print("[{mod_name}] 客户端 UI 初始化完成")

    def on_player_welcome(self, args):
        message = args.get("message", "")
        if message:
            print("[{mod_name}] 收到服务端欢迎消息: {{}}".format(message))
'''


STANDALONE_SERVER_SYSTEM_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{mod_name} 服务端系统
仅导入 serverApi，禁止导入 clientApi；跨端通信请使用 NotifyToClient。
"""
from __future__ import print_function

import mod.server.extraServerApi as serverApi

CF = serverApi.GetEngineCompFactory()
ServerSystem = serverApi.GetServerSystemCls()

TICK_INTERVAL = 20


class {class_name}ServerSystem(ServerSystem):
    """服务端系统"""

    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.tick = 0
        self._init_events()

    def _init_events(self):
        engine_ns = serverApi.GetEngineNamespace()
        engine_sys = serverApi.GetEngineSystemName()
        self.ListenForEvent(engine_ns, engine_sys, "AddServerPlayerEvent", self, self.on_player_join)
        self.ListenForEvent(engine_ns, engine_sys, "ClientLoadAddonsFinishServerEvent", self, self.on_client_addons_ready)
        self.ListenForEvent(engine_ns, engine_sys, "DelServerPlayerEvent", self, self.on_player_leave)

    def Destroy(self):
        self.UnListenAllEvents()

    def on_player_join(self, args):
        player_id = args.get("id")
        if not player_id:
            return
        name_comp = CF.CreateName(player_id)
        player_name = name_comp.GetName() if name_comp else player_id
        print("[{mod_name}] 玩家加入服务端: {{}} ({{}})".format(player_name, player_id))

    def on_client_addons_ready(self, args):
        player_id = args.get("playerId")
        if not player_id:
            return
        self.NotifyToClient(player_id, "PlayerWelcome", {{"message": "欢迎加入服务器！"}})

    def on_player_leave(self, args):
        player_id = args.get("id")
        if not player_id:
            return
        print("[{mod_name}] 玩家离开: {{}}".format(player_id))

    def on_tick(self, args=None):
        self.tick += 1
        if self.tick % TICK_INTERVAL != 0:
            return
'''


STANDALONE_CLIENT_SYSTEM_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{mod_name} 客户端系统
仅导入 clientApi，禁止导入 serverApi；跨端通信请使用 NotifyToServer。
"""
from __future__ import print_function

import mod.client.extraClientApi as clientApi

CF = clientApi.GetEngineCompFactory()
ClientSystem = clientApi.GetClientSystemCls()


class {class_name}ClientSystem(ClientSystem):
    """客户端系统"""

    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self._init_events()

    def _init_events(self):
        engine_ns = clientApi.GetEngineNamespace()
        engine_sys = clientApi.GetEngineSystemName()
        self.ListenForEvent(engine_ns, engine_sys, "UiInitFinished", self, self.on_ui_init_finished)

    def Destroy(self):
        self.UnListenAllEvents()

    def on_ui_init_finished(self, args):
        print("[{mod_name}] 客户端 UI 初始化完成")

    def on_player_welcome(self, args):
        message = args.get("message", "")
        if message:
            print("[{mod_name}] 收到服务端消息: {{}}".format(message))
'''


INIT_FILE_TEMPLATE = '''# -*- coding: utf-8 -*-
"""{mod_name} Python 包初始化文件"""
'''


EVENT_LISTENER_TEMPLATE = '''# -*- coding: utf-8 -*-
"""事件监听器示例"""
from __future__ import print_function

import {api_module} as {api_alias}


def register_event_listeners(system):
    """注册事件监听器

    Args:
        system: {system_kind} 实例
    """
    namespace = {api_alias}.GetEngineNamespace()
    system_name = {api_alias}.GetEngineSystemName()

    # {event_description}
    system.ListenForEvent(
        namespace,
        system_name,
        "{event_name}",
        system,
        system.on_{event_handler}
    )


class EventHandlers(object):
    """事件处理器集合"""

    def on_{event_handler}(self, args):
        """
        {event_description}

        Args:
            args: 事件参数
{event_params}
        """
        pass
'''


CUSTOM_COMMAND_TEMPLATE = '''# -*- coding: utf-8 -*-
"""自定义聊天前缀命令示例（或使用 CustomCommandTriggerServerEvent 注册原生命令）"""
from __future__ import print_function

import mod.server.extraServerApi as serverApi

CF = serverApi.GetEngineCompFactory()


class CommandManager(object):
    """命令管理器"""

    def __init__(self, level_id):
        self.level_id = level_id
        self.commands = {{}}

    def register_command(self, name, callback, permission=0):
        self.commands[name] = {{
            "callback": callback,
            "permission": permission
        }}

    def on_chat(self, args):
        """在 ServerChatEvent 中解析命令"""
        message = args.get("message", "")
        player_id = args.get("playerId")
        if message.startswith("/"):
            parts = message[1:].split(" ")
            cmd_name = parts[0]
            cmd_args = parts[1:]
            if cmd_name in self.commands:
                self.commands[cmd_name]["callback"](player_id, cmd_args)
                return True
        return False


def cmd_{command_name}(player_id, args):
    """/{command_name} 命令回调"""
    comp = CF.CreateMsg(player_id)
    comp.NotifyOneMessage(player_id, "命令执行成功", "§a")
'''


CUSTOM_ITEM_SCRIPT_TEMPLATE = '''# -*- coding: utf-8 -*-
"""自定义物品服务端交互脚本示例"""
from __future__ import print_function

import mod.server.extraServerApi as serverApi

CF = serverApi.GetEngineCompFactory()


def on_item_use_on(args):
    """在 ServerSystem 中监听 ServerItemUseOnEvent（注意玩家实体字段为 entityId）"""
    player_id = args.get("entityId")
    item_dict = args.get("itemDict")
    if item_dict and item_dict.get("itemName") == "{namespace}:{item_id}":
        print("[{namespace}] 玩家 {{}} 使用了物品 {namespace}:{item_id}".format(player_id))
        return True
    return False
'''


CUSTOM_BLOCK_SCRIPT_TEMPLATE = '''# -*- coding: utf-8 -*-
"""自定义方块服务端交互脚本示例"""
from __future__ import print_function

import mod.server.extraServerApi as serverApi

CF = serverApi.GetEngineCompFactory()


def on_block_use(args):
    """在 ServerSystem 中监听 ServerBlockUseEvent"""
    player_id = args.get("playerId")
    block_name = args.get("blockName")
    pos = (args.get("x"), args.get("y"), args.get("z"))
    if block_name == "{namespace}:{block_id}":
        print("[{namespace}] 玩家 {{}} 与方块 {namespace}:{block_id} 交互，位置: {{}}".format(player_id, pos))
        return True
    return False
'''


UI_SCREEN_PYTHON_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{title} ScreenNode 客户端控制器
遵循 UI-LIFE-001 / UI-LIFE-002：先在 UiInitFinished 中 RegisterUI，再 CreateUI/PushScreen，
并在 ScreenNode.Create 生命周期内绑定控件事件。
"""
from __future__ import print_function

import mod.client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()


class {screen_class}(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.title_label_path = "/main_panel/title_label"
        self.close_btn_path = "/main_panel/close_btn"

    def Create(self):
        close_ctrl = self.GetBaseUIControl(self.close_btn_path)
        if close_ctrl:
            close_btn = close_ctrl.asButton()
            if close_btn:
                close_btn.AddTouchEventParams({{"isSwallow": True}})
                close_btn.SetButtonTouchUpCallback(self.on_close_click)

    def on_close_click(self, args):
        self.SetRemove()

    def set_title(self, text):
        label_ctrl = self.GetBaseUIControl(self.title_label_path)
        if label_ctrl:
            label = label_ctrl.asLabel()
            if label:
                label.SetText(text)
'''


# ============================================================================
# 项目骨架与 Python 生成函数
# ============================================================================

def generate_mod_project(
    mod_name: str,
    mod_id: str,
    author: str = "Author",
    description: str = "A Minecraft mod",
    version: str = "1.0.0",
    min_engine_version: Sequence[int] = DEFAULT_MIN_ENGINE_VERSION,
    behavior_pack_dir: Optional[str] = None,
    resource_pack_dir: Optional[str] = None,
) -> Dict[str, str]:
    """生成完整可运行的双包 AddOn 项目骨架（behavior_pack + resource_pack）。

    包含：
    - 双包最新 `manifest.json`（format_version: 2，唯一 UUID，行为包依赖绑定资源包）
    - 中国版必选目录：`behavior_pack/entities/` 与 `resource_pack/textures/`
    - 扁平清晰的 Python 脚本包：`behavior_pack/{mod_id}_Script/`（含双端闭环事件通信）
    - 资源包基础纹理注册表与中文语言文件（`texts/languages.json` + `texts/zh_CN.lang`）
    """
    clean_mod_id = validate_mod_id(mod_id, "mod_id")
    clean_mod_name = str(mod_name or "").strip() or clean_mod_id
    clean_desc = str(description or "").strip() or clean_mod_name
    clean_author = str(author or "").strip() or "Author"
    ver_list = parse_version_triplet(version, "version")
    ver_str = ".".join(str(x) for x in ver_list)
    bp_dir, rp_dir = resolve_pack_dirs(behavior_pack_dir, resource_pack_dir)

    class_name = to_camel_case(clean_mod_id)
    project_folder = get_project_folder_name(clean_mod_id)
    script_base = "{}/{}".format(bp_dir, project_folder)

    manifests = generate_manifest_json(
        pack_name=clean_mod_name,
        description=clean_desc,
        pack_type="both",
        version=ver_list,
        min_engine_version=min_engine_version,
        behavior_pack_dir=bp_dir,
        resource_pack_dir=rp_dir,
    )

    files: Dict[str, str] = {}
    files["{}/manifest.json".format(bp_dir)] = manifests["{}/manifest.json".format(bp_dir)]
    # 网易平台上传审核（错误码 24）要求行为包必须包含 entities 目录
    files["{}/entities/.gitkeep".format(bp_dir)] = ""
    files["{}/__init__.py".format(script_base)] = INIT_FILE_TEMPLATE.format(mod_name=clean_mod_name)
    files["{}/modConfig.py".format(script_base)] = MOD_CONFIG_TEMPLATE.format(
        mod_name=clean_mod_name,
        mod_id=clean_mod_id,
        version=ver_str,
        project_folder=project_folder,
        class_name=class_name,
    )
    files["{}/modMain.py".format(script_base)] = MOD_MAIN_TEMPLATE.format(
        mod_name=clean_mod_name,
        author=clean_author,
        description=clean_desc,
        project_folder=project_folder,
        class_name=class_name,
    )
    files["{}/serverSystem.py".format(script_base)] = PROJECT_SERVER_SYSTEM_TEMPLATE.format(
        mod_name=clean_mod_name,
        project_folder=project_folder,
        class_name=class_name,
    )
    files["{}/clientSystem.py".format(script_base)] = PROJECT_CLIENT_SYSTEM_TEMPLATE.format(
        mod_name=clean_mod_name,
        project_folder=project_folder,
        class_name=class_name,
    )

    files["{}/manifest.json".format(rp_dir)] = manifests["{}/manifest.json".format(rp_dir)]
    # 网易中国版要求资源包必须存在 textures 目录；初始化空纹理注册表一并满足后续物品/方块扩展
    files["{}/textures/item_texture.json".format(rp_dir)] = build_item_texture_json(clean_mod_id, {})
    files["{}/textures/terrain_texture.json".format(rp_dir)] = build_terrain_texture_json(clean_mod_id, {})
    files["{}/texts/languages.json".format(rp_dir)] = build_languages_json(("zh_CN",))
    files["{}/texts/zh_CN.lang".format(rp_dir)] = (
        "## {} 本地化文件\n"
        "pack.name={}\n"
        "pack.description={}\n"
    ).format(clean_mod_name, clean_mod_name, clean_desc)

    return files


def generate_server_system(mod_name: str, class_name: str) -> str:
    """生成独立服务端系统代码。"""
    clean_class = to_camel_case(class_name) if "_" in class_name or "-" in class_name else class_name
    return STANDALONE_SERVER_SYSTEM_TEMPLATE.format(
        mod_name=mod_name,
        class_name=clean_class,
    )


def generate_client_system(mod_name: str, class_name: str) -> str:
    """生成独立客户端系统代码。"""
    clean_class = to_camel_case(class_name) if "_" in class_name or "-" in class_name else class_name
    return STANDALONE_CLIENT_SYSTEM_TEMPLATE.format(
        mod_name=mod_name,
        class_name=clean_class,
    )


def generate_event_listener(
    event_name: str,
    event_description: str = "事件处理",
    params: Optional[Dict[str, str]] = None,
    side: str = "server",
) -> str:
    """生成事件监听器代码。"""
    if side not in ("server", "client"):
        raise ValueError("Event listener side must be 'server' or 'client'")

    event_handler = re.sub(r"[^a-z0-9_]", "_", event_name.lower()).replace("event", "").strip("_") or "event"
    params_doc = ""
    if params:
        for name, desc in params.items():
            params_doc += "                {}: {}\n".format(name, desc)

    return EVENT_LISTENER_TEMPLATE.format(
        event_name=event_name,
        event_description=event_description,
        event_handler=event_handler,
        event_params=params_doc.rstrip("\n"),
        api_module=("mod.server.extraServerApi" if side == "server" else "mod.client.extraClientApi"),
        api_alias=("serverApi" if side == "server" else "clientApi"),
        system_kind=("ServerSystem" if side == "server" else "ClientSystem"),
    )


def generate_custom_command(command_name: str) -> str:
    """生成自定义命令代码。"""
    clean_cmd = validate_content_id(command_name, "command_name")
    return CUSTOM_COMMAND_TEMPLATE.format(command_name=clean_cmd)


# ============================================================================
# 数据驱动 JSON 生成器（物品 / 武器工具 / 盔甲 / 食物 / 远程 / 方块 / 配方 / 实体 / UI）
# ============================================================================

def generate_item_json(
    namespace: str,
    item_id: str,
    category: str = "items",
    max_stack_size: int = 64,
    components: Optional[Dict[str, Any]] = None,
    resource_components: Optional[Dict[str, Any]] = None,
    custom_item_type: Optional[str] = None,
    display_name: str = "自定义物品",
    icon_name: Optional[str] = None,
    behavior_pack_dir: Optional[str] = None,
    resource_pack_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """生成完整的网易 `1.10` 自定义物品配套文件集（行为包 + 资源包 + 贴图注册 + 语言文件）。"""
    ns = validate_mod_id(namespace, "namespace")
    iid = validate_content_id(item_id, "item_id")
    bp_dir, rp_dir = resolve_pack_dirs(behavior_pack_dir, resource_pack_dir)

    if not isinstance(max_stack_size, int) or isinstance(max_stack_size, bool) or not 1 <= max_stack_size <= 64:
        raise ValueError("max_stack_size 必须是 1 到 64 之间的整数")

    beh_description: Dict[str, Any] = {
        "identifier": "{}:{}".format(ns, iid),
        "category": category,
    }
    if custom_item_type:
        beh_description["custom_item_type"] = custom_item_type

    beh_components: Dict[str, Any] = {
        "minecraft:max_stack_size": max_stack_size,
    }
    if components:
        # 字典合并天然消除重复键；若外部显式传入 max_stack_size 则安全覆盖默认值
        beh_components.update(components)

    behavior_payload = {
        "format_version": "1.10",
        "minecraft:item": {
            "description": beh_description,
            "components": beh_components,
        },
    }

    resolved_icon = icon_name or "{}:{}".format(ns, iid)
    res_components: Dict[str, Any] = {
        "minecraft:icon": resolved_icon,
    }
    if resource_components:
        res_components.update(resource_components)

    resource_payload = {
        "format_version": "1.10",
        "minecraft:item": {
            "description": {
                "identifier": "{}:{}".format(ns, iid),
                "category": category,
            },
            "components": res_components,
        },
    }

    behavior_text = _dump_json(behavior_payload)
    resource_text = _dump_json(resource_payload)
    texture_json = build_item_texture_json(
        ns,
        {
            resolved_icon: {
                "textures": "textures/items/{}".format(iid),
            }
        },
    )
    languages_json = build_languages_json(("zh_CN",))
    lang_text = "item.{}:{}.name={}\n".format(ns, iid, display_name)

    files: Dict[str, str] = {
        "{}/netease_items_beh/{}_{}.json".format(bp_dir, ns, iid): behavior_text,
        "{}/netease_items_res/{}_{}.json".format(rp_dir, ns, iid): resource_text,
        "{}/textures/item_texture.json".format(rp_dir): texture_json,
        "{}/texts/languages.json".format(rp_dir): languages_json,
        "{}/texts/zh_CN.lang".format(rp_dir): lang_text,
    }
    return {
        "behavior": behavior_text,
        "resource": resource_text,
        "item_texture": texture_json,
        "languages": languages_json,
        "lang": lang_text,
        "files": files,
    }


# 铁砧修复材料到 netease:weapon.level 的官方映射（参考《2-自定义武器及工具.md》）
_REPAIR_MATERIAL_TO_LEVEL: Dict[str, int] = {
    "minecraft:planks": 0,
    "minecraft:oak_planks": 0,
    "minecraft:gold_ingot": 0,
    "minecraft:cobblestone": 1,
    "minecraft:stone": 1,
    "minecraft:iron_ingot": 2,
    "minecraft:diamond": 3,
}

# 盔甲槽位映射（参考《3-自定义盔甲.md》与 ArmorSlotType 枚举：HEAD=0, BODY=1, LEG=2, FOOT=3）
ARMOR_SLOT_SPECS: Dict[str, Dict[str, Any]] = {
    "slot.armor.head": {
        "armor_slot": 0,
        "label": "头盔",
        "geometry": "geometry.humanoid.armor.helmet",
        "parent_setup": "variable.helmet_layer_visible = 0.0;",
        "default_texture": "textures/models/armor/diamond_1",
    },
    "slot.armor.chest": {
        "armor_slot": 1,
        "label": "胸甲",
        "geometry": "geometry.humanoid.armor.chestplate",
        "parent_setup": "variable.chest_layer_visible = 0.0;",
        "default_texture": "textures/models/armor/diamond_1",
    },
    "slot.armor.legs": {
        "armor_slot": 2,
        "label": "护腿",
        "geometry": "geometry.humanoid.armor.leggings",
        "parent_setup": "variable.leg_layer_visible = 0.0;",
        "default_texture": "textures/models/armor/diamond_2",
    },
    "slot.armor.feet": {
        "armor_slot": 3,
        "label": "靴子",
        "geometry": "geometry.humanoid.armor.boots",
        "parent_setup": "variable.boot_layer_visible = 0.0;",
        "default_texture": "textures/models/armor/diamond_1",
    },
}

_WEAPON_TOOL_DEFAULTS: Dict[str, Dict[str, Any]] = {
    "sword": {"weapon_type": "sword", "damage": 5, "durability": 250, "speed": 0, "enchantability": 14, "level": 2, "display_name": "自定义剑"},
    "pickaxe": {"weapon_type": "pickaxe", "damage": 2, "durability": 250, "speed": 6, "enchantability": 14, "level": 2, "display_name": "自定义镐"},
    "axe": {"weapon_type": "hatchet", "damage": 4, "durability": 250, "speed": 6, "enchantability": 14, "level": 2, "display_name": "自定义斧"},
    "shovel": {"weapon_type": "shovel", "damage": 1, "durability": 250, "speed": 6, "enchantability": 14, "level": 2, "display_name": "自定义锹"},
    "hoe": {"weapon_type": "hoe", "damage": 1, "durability": 250, "speed": 0, "enchantability": 14, "level": 2, "display_name": "自定义锄"},
}


def _infer_weapon_level(level: Optional[int], repair_material: Optional[str], default_level: int = 2) -> int:
    if level is not None:
        return int(level)
    if repair_material:
        normalized = str(repair_material).strip().lower()
        if ":" not in normalized:
            normalized = "minecraft:{}".format(normalized)
        if normalized in _REPAIR_MATERIAL_TO_LEVEL:
            return _REPAIR_MATERIAL_TO_LEVEL[normalized]
    return default_level


def generate_typed_item_json(
    item_type: str,
    namespace: str,
    item_id: str,
    **kwargs: Any
) -> Dict[str, Any]:
    """按网易官方 `1.10` 组件规范生成 9 类高级自定义物品及完整配套资源文件。

    支持类型：`sword`, `pickaxe`, `axe`, `shovel`, `hoe`, `food`, `armor`, `bow`, `throwable`。
    """
    ns = validate_mod_id(namespace, "namespace")
    iid = validate_content_id(item_id, "item_id")
    bp_dir, rp_dir = resolve_pack_dirs(
        kwargs.get("behavior_pack_dir"),
        kwargs.get("resource_pack_dir"),
    )
    notes: List[str] = []

    if item_type in _WEAPON_TOOL_DEFAULTS:
        spec = _WEAPON_TOOL_DEFAULTS[item_type]
        durability = int(kwargs.get("durability", spec["durability"]))
        damage = int(kwargs.get("damage", spec["damage"]))
        speed = int(kwargs.get("mining_speed", spec["speed"]))
        enchantability = int(kwargs.get("enchantability", spec["enchantability"]))
        level = _infer_weapon_level(kwargs.get("level"), kwargs.get("repair_material"), spec["level"])
        display_name = str(kwargs.get("display_name") or spec["display_name"])

        beh_components: Dict[str, Any] = {
            "minecraft:max_stack_size": 1,
            "minecraft:max_damage": durability,
            "minecraft:hand_equipped": True,
            "netease:weapon": {
                "type": spec["weapon_type"],
                "level": level,
                "speed": speed,
                "attack_damage": damage,
                "enchantment": enchantability,
            },
        }
        bundle = generate_item_json(
            namespace=ns,
            item_id=iid,
            category="equipment",
            max_stack_size=1,
            components=beh_components,
            custom_item_type="weapon",
            display_name=display_name,
            behavior_pack_dir=bp_dir,
            resource_pack_dir=rp_dir,
        )
        notes.append(
            "网易 1.10 武器/工具通过 `custom_item_type: \"weapon\"` + `netease:weapon` + `minecraft:max_damage` 驱动；"
            "注意斧头的官方 `netease:weapon.type` 为 `\"hatchet\"`，且有耐久物品严禁同时声明 `minecraft:stacked_by_data`。"
        )
        bundle["notes"] = notes
        return bundle

    if item_type == "armor":
        slot = str(kwargs.get("slot", "slot.armor.chest"))
        if slot not in ARMOR_SLOT_SPECS:
            raise ValueError("不支持的盔甲槽位：{!r}，可选值为 {}".format(slot, ", ".join(ARMOR_SLOT_SPECS)))
        slot_spec = ARMOR_SLOT_SPECS[slot]
        protection = int(kwargs.get("protection", 5))
        durability = int(kwargs.get("durability", 165))
        enchantability = int(kwargs.get("enchantability", 9))
        toughness = kwargs.get("toughness")
        knockback_resistance = kwargs.get("knockback_resistance")
        display_name = str(kwargs.get("display_name") or "自定义{}".format(slot_spec["label"]))

        armor_comp: Dict[str, Any] = {
            "defense": protection,
            "enchantment": enchantability,
            "armor_slot": slot_spec["armor_slot"],
        }
        if toughness is not None:
            armor_comp["toughness"] = int(toughness)
        if knockback_resistance is not None:
            armor_comp["knockback_resistance"] = float(knockback_resistance)

        beh_components = {
            "minecraft:max_stack_size": 1,
            "minecraft:max_damage": durability,
            "netease:armor": armor_comp,
        }
        bundle = generate_item_json(
            namespace=ns,
            item_id=iid,
            category="equipment",
            max_stack_size=1,
            components=beh_components,
            custom_item_type="armor",
            display_name=display_name,
            behavior_pack_dir=bp_dir,
            resource_pack_dir=rp_dir,
        )

        attachable_payload = {
            "format_version": "1.8.0",
            "minecraft:attachable": {
                "description": {
                    "identifier": "{}:{}".format(ns, iid),
                    "materials": {
                        "default": "armor",
                        "enchanted": "armor_enchanted",
                    },
                    "textures": {
                        "default": slot_spec["default_texture"],
                        "enchanted": "textures/misc/enchanted_item_glint",
                    },
                    "geometry": {
                        "default": slot_spec["geometry"],
                    },
                    "scripts": {
                        "parent_setup": slot_spec["parent_setup"],
                    },
                    "render_controllers": ["controller.render.armor"],
                }
            },
        }
        attachable_text = _dump_json(attachable_payload)
        bundle["attachable"] = attachable_text
        bundle["files"]["{}/attachables/{}_{}.json".format(rp_dir, ns, iid)] = attachable_text
        notes.append(
            "网易 1.10 盔甲必须使用 `custom_item_type: \"armor\"` + `netease:armor`（`armor_slot`: 0=头盔, 1=胸甲, 2=护腿, 3=靴子），"
            "并配套 `resource_pack/attachables/` 穿戴渲染定义。"
        )
        bundle["notes"] = notes
        return bundle

    if item_type == "food":
        nutrition = int(kwargs.get("nutrition", 4))
        saturation = str(kwargs.get("saturation", "normal"))
        can_always_eat = bool(kwargs.get("can_always_eat", False))
        use_duration = int(kwargs.get("use_duration", 32))
        effects = kwargs.get("effects")
        using_converts_to = kwargs.get("using_converts_to")
        display_name = str(kwargs.get("display_name") or "自定义食物")

        food_comp: Dict[str, Any] = {
            "nutrition": nutrition,
            "saturation_modifier": saturation,
        }
        if can_always_eat:
            food_comp["can_always_eat"] = True
        if using_converts_to:
            food_comp["using_converts_to"] = str(using_converts_to)
        if effects:
            food_comp["effects"] = list(effects)

        beh_components = {
            "minecraft:max_stack_size": 64,
            "minecraft:use_duration": use_duration,
            "minecraft:food": food_comp,
        }
        res_components = {
            "minecraft:use_animation": "eat",
        }
        bundle = generate_item_json(
            namespace=ns,
            item_id=iid,
            category="nature",
            max_stack_size=64,
            components=beh_components,
            resource_components=res_components,
            display_name=display_name,
            behavior_pack_dir=bp_dir,
            resource_pack_dir=rp_dir,
        )
        notes.append(
            "`minecraft:use_animation` 属于资源包组件（位于 `netease_items_res`），"
            "行为包中的 `minecraft:use_duration` 使用游戏刻整数（默认 32 tick = 1.6 秒）。"
        )
        bundle["notes"] = notes
        return bundle

    if item_type == "bow":
        durability = int(kwargs.get("durability", 384))
        use_duration = int(kwargs.get("use_duration", 72000))
        display_name = str(kwargs.get("display_name") or "自定义弓")
        projectile_entity = str(kwargs.get("projectile_entity", "minecraft:arrow"))

        beh_components = {
            "minecraft:max_stack_size": 1,
            "minecraft:max_damage": durability,
            "minecraft:hand_equipped": True,
            "minecraft:use_duration": use_duration,
            "netease:render_offsets": {
                "controller_position_adjust": [0.0, 0.1, 0.0],
                "controller_rotation_adjust": [0.0, -45.0, 0.0],
                "controller_scale": 1.0,
            },
        }
        frame_key = "{}:{}_pulling".format(ns, iid)
        res_components = {
            "minecraft:use_animation": "bow",
            "netease:frame_animation": {
                "frame_count": 3,
                "texture_name": frame_key,
                "animate_in_toolbar": True,
            },
        }
        bundle = generate_item_json(
            namespace=ns,
            item_id=iid,
            category="equipment",
            max_stack_size=1,
            components=beh_components,
            resource_components=res_components,
            custom_item_type="ranged_weapon",
            display_name=display_name,
            behavior_pack_dir=bp_dir,
            resource_pack_dir=rp_dir,
        )
        # 远程蓄力武器贴图注册需同时包含默认图标与 3 帧蓄力序列帧
        bow_texture_json = build_item_texture_json(
            ns,
            {
                "{}:{}".format(ns, iid): {
                    "textures": "textures/items/{}_0".format(iid),
                },
                frame_key: {
                    "textures": [
                        "textures/items/{}_0".format(iid),
                        "textures/items/{}_1".format(iid),
                        "textures/items/{}_2".format(iid),
                    ]
                },
            },
        )
        bundle["item_texture"] = bow_texture_json
        bundle["files"]["{}/textures/item_texture.json".format(rp_dir)] = bow_texture_json

        notes.append(
            "网易自定义蓄力远程武器通过 `custom_item_type: \"ranged_weapon\"` + `minecraft:use_duration` 驱动，"
            "松手发射需在服务端监听 `ItemReleaseUsingServerEvent` 并调用 `CreateProjectileEntity` 生成抛射物（如 `{}`）。".format(projectile_entity)
        )
        if iid != "bow":
            notes.append(
                "根据网易官方《自定义远程武器》规范：若需第三人称视角拉弓抬手动作生效，物品 `identifier` 必须以 `:bow` 结尾（即 `{}:bow`）。".format(ns)
            )
        bundle["notes"] = notes
        return bundle

    if item_type == "throwable":
        projectile_entity = str(kwargs.get("projectile_entity", "")).strip()
        if not _NAMESPACED_ID_RE.fullmatch(projectile_entity):
            raise ValueError(
                "projectile_entity 必须是合法的小写 namespace:id 实体标识符（如 'minecraft:snowball'），当前为 {!r}".format(
                    projectile_entity
                )
            )
        max_stack_size = int(kwargs.get("max_stack_size", 16))
        cooldown_ticks = int(kwargs.get("cooldown_ticks", 0))
        display_name = str(kwargs.get("display_name") or "自定义投掷物")

        beh_components = {
            "minecraft:max_stack_size": max_stack_size,
            "netease:projectile": projectile_entity,
        }
        if cooldown_ticks > 0:
            beh_components["netease:cooldown"] = {
                "category": iid,
                "duration": cooldown_ticks,
            }

        bundle = generate_item_json(
            namespace=ns,
            item_id=iid,
            category="equipment",
            max_stack_size=max_stack_size,
            components=beh_components,
            custom_item_type="projectile_item",
            display_name=display_name,
            behavior_pack_dir=bp_dir,
            resource_pack_dir=rp_dir,
        )
        notes.append(
            "网易 1.10 投掷物物品使用 `custom_item_type: \"projectile_item\"` + `\"netease:projectile\": \"{}\"`，右键即可直接发射对应抛射物实体。".format(
                projectile_entity
            )
        )
        bundle["notes"] = notes
        return bundle

    raise ValueError("未知物品类型：{!r}".format(item_type))


def _normalize_legacy_light_emission(light_emission: float) -> float:
    """将 [0, 15] 或 [0.0, 1.0] 的发光输入安全转换为旧版 `minecraft:block_light_emission` 要求的 [0.0, 1.0] 浮点。"""
    if isinstance(light_emission, bool) or not isinstance(light_emission, (int, float)):
        raise ValueError("light_emission 必须是数值")
    val = float(light_emission)
    if val < 0.0 or val > 15.0:
        raise ValueError("light_emission 必须在 0 到 15 范围内，当前为 {!r}".format(light_emission))
    if isinstance(light_emission, float) and val <= 1.0:
        return round(val, 4)
    if val <= 1.0 and light_emission in (0, 1):
        # 整数 0 -> 0.0；整数 1 按 1/15 亮度等级归一化（若需满亮度 1.0 在 0-15 量纲下应传 15）
        return 0.0 if light_emission == 0 else round(1.0 / 15.0, 4)
    return round(val / 15.0, 4)


def generate_block_json(
    namespace: str,
    block_id: str,
    destroy_time: float = 1.5,
    explosion_resistance: float = 10.0,
    light_emission: float = 0,
    light_dampening: int = 15,
    map_color: str = "#FFFFFF",
    category: str = "Nature",
    register_to_menu: bool = True,
    sound: str = "stone",
    display_name: str = "自定义方块",
    components: Optional[Dict[str, Any]] = None,
    format_profile: str = "modern_1_19_20",
    behavior_pack_dir: Optional[str] = None,
    resource_pack_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """按选定格式档（默认推荐 `modern_1_19_20`）生成方块行为包 JSON 及资源包 `blocks.json` / `terrain_texture.json`。"""
    ns = validate_mod_id(namespace, "namespace")
    bid = validate_content_id(block_id, "block_id")
    bp_dir, rp_dir = resolve_pack_dirs(behavior_pack_dir, resource_pack_dir)

    if format_profile not in BLOCK_FORMAT_PROFILES:
        raise ValueError("Unknown block format profile: {}".format(format_profile))
    if isinstance(light_emission, bool) or not isinstance(light_emission, (int, float)) or not (0 <= float(light_emission) <= 15):
        raise ValueError("light_emission 必须在 0 到 15 范围内，当前为 {!r}".format(light_emission))
    if isinstance(light_dampening, bool) or not isinstance(light_dampening, int) or not (0 <= light_dampening <= 15):
        raise ValueError("light_dampening 必须是 0 到 15 之间的整数")

    format_version = BLOCK_FORMAT_PROFILES[format_profile]
    if format_profile == "modern_1_19_20":
        description: Dict[str, Any] = {
            "identifier": "{}:{}".format(ns, bid),
            "menu_category": {
                "category": category.lower() if register_to_menu else "none",
            },
        }
        beh_components: Dict[str, Any] = {
            "minecraft:destructible_by_mining": {"seconds_to_destroy": float(destroy_time)},
            "minecraft:destructible_by_explosion": {"explosion_resistance": float(explosion_resistance)},
            "minecraft:light_emission": int(round(light_emission)),
            "minecraft:light_dampening": int(light_dampening),
            "minecraft:map_color": map_color,
        }
    elif format_profile == "scalar_1_16":
        description = {
            "identifier": "{}:{}".format(ns, bid),
            "register_to_create_menu": bool(register_to_menu),
            "category": category,
        }
        beh_components = {
            "minecraft:destroy_time": float(destroy_time),
            "minecraft:explosion_resistance": float(explosion_resistance),
            "minecraft:block_light_emission": _normalize_legacy_light_emission(light_emission),
            "minecraft:block_light_absorption": int(light_dampening),
            "minecraft:map_color": map_color,
        }
    else:  # legacy_1_10
        description = {
            "identifier": "{}:{}".format(ns, bid),
            "register_to_create_menu": bool(register_to_menu),
            "category": category,
        }
        beh_components = {
            "minecraft:destroy_time": {"value": float(destroy_time)},
            "minecraft:explosion_resistance": {"value": float(explosion_resistance)},
            "minecraft:block_light_emission": {"emission": _normalize_legacy_light_emission(light_emission)},
            "minecraft:block_light_absorption": {"value": int(light_dampening)},
        }

    if components:
        beh_components.update(components)

    behavior_payload = {
        "format_version": format_version,
        "minecraft:block": {
            "description": description,
            "components": beh_components,
        },
    }
    behavior_text = _dump_json(behavior_payload)

    texture_key = "{}_{}".format(ns, bid)
    blocks_json = build_blocks_json({
        "{}:{}".format(ns, bid): {
            "textures": texture_key,
            "sound": sound,
        }
    })
    terrain_texture_json = build_terrain_texture_json(
        ns,
        {
            texture_key: {
                "textures": "textures/blocks/{}".format(bid),
            }
        },
    )
    languages_json = build_languages_json(("zh_CN",))
    lang_text = "tile.{}:{}.name={}\n".format(ns, bid, display_name)

    files: Dict[str, str] = {
        "{}/netease_blocks/{}_{}.json".format(bp_dir, ns, bid): behavior_text,
        "{}/blocks.json".format(rp_dir): blocks_json,
        "{}/textures/terrain_texture.json".format(rp_dir): terrain_texture_json,
        "{}/texts/languages.json".format(rp_dir): languages_json,
        "{}/texts/zh_CN.lang".format(rp_dir): lang_text,
    }
    return {
        "behavior": behavior_text,
        "blocks_json": blocks_json,
        "terrain_texture": terrain_texture_json,
        "languages": languages_json,
        "lang": lang_text,
        "format_profile": format_profile,
        "files": files,
    }


def generate_custom_item(
    item_id: str,
    namespace: str = "mymod",
    display_name: str = "自定义物品",
    max_stack: int = 64,
    hand_equipped: bool = False,
    behavior_pack_dir: Optional[str] = None,
    resource_pack_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """生成自定义物品完整配套包（服务端事件脚本 + 行为包/资源包 JSON + 贴图注册 + 语言条目）。"""
    ns = validate_mod_id(namespace, "namespace")
    iid = validate_content_id(item_id, "item_id")
    bp_dir, rp_dir = resolve_pack_dirs(behavior_pack_dir, resource_pack_dir)

    item_bundle = generate_item_json(
        namespace=ns,
        item_id=iid,
        category="items",
        max_stack_size=max_stack,
        components={"minecraft:hand_equipped": bool(hand_equipped)},
        display_name=display_name,
        behavior_pack_dir=bp_dir,
        resource_pack_dir=rp_dir,
    )
    script_code = CUSTOM_ITEM_SCRIPT_TEMPLATE.format(namespace=ns, item_id=iid)
    script_path = "{}/{}_Script/item_{}.py".format(bp_dir, ns, iid)

    files: Dict[str, str] = {script_path: script_code}
    files.update(item_bundle["files"])
    return {
        "script": script_code,
        "script_path": script_path,
        "item": item_bundle,
        "files": files,
    }


def generate_custom_block(
    block_id: str,
    namespace: str = "mymod",
    destroy_time: float = 1.0,
    explosion_resistance: float = 1.0,
    display_name: str = "自定义方块",
    behavior_pack_dir: Optional[str] = None,
    resource_pack_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """生成自定义方块完整配套包（服务端交互脚本 + 现代 1.19.20 行为包 JSON + blocks.json + terrain_texture.json）。"""
    ns = validate_mod_id(namespace, "namespace")
    bid = validate_content_id(block_id, "block_id")
    bp_dir, rp_dir = resolve_pack_dirs(behavior_pack_dir, resource_pack_dir)

    block_bundle = generate_block_json(
        namespace=ns,
        block_id=bid,
        destroy_time=destroy_time,
        explosion_resistance=explosion_resistance,
        display_name=display_name,
        format_profile="modern_1_19_20",
        behavior_pack_dir=bp_dir,
        resource_pack_dir=rp_dir,
    )
    script_code = CUSTOM_BLOCK_SCRIPT_TEMPLATE.format(namespace=ns, block_id=bid)
    script_path = "{}/{}_Script/block_{}.py".format(bp_dir, ns, bid)

    files: Dict[str, str] = {script_path: script_code}
    files.update(block_bundle["files"])
    return {
        "script": script_code,
        "script_path": script_path,
        "block": block_bundle,
        "files": files,
    }


def _recipe_item_descriptor(item_str: str) -> Dict[str, Any]:
    """解析配方物品标识（支持 `namespace:item` 或带附加值 `namespace:item:aux`）。"""
    parts = str(item_str or "").strip().split(":")
    if len(parts) == 3 and parts[2].lstrip("-").isdigit():
        return {"item": "{}:{}".format(parts[0], parts[1]), "data": int(parts[2])}
    return {"item": str(item_str or "minecraft:air").strip()}


def generate_recipe_json(
    recipe_type: str,
    namespace: str,
    recipe_id: str,
    behavior_pack_dir: Optional[str] = None,
    **kwargs: Any
) -> Dict[str, Any]:
    """生成合成配方 JSON（位于 `{behavior_pack}/netease_recipes/{namespace}_{recipe_id}.json`）。"""
    ns = validate_mod_id(namespace, "namespace")
    rid = validate_content_id(recipe_id, "recipe_id")
    bp_dir = normalize_pack_dir(behavior_pack_dir, DEFAULT_BEHAVIOR_PACK_DIR, "behavior_pack_dir")
    recipe_tag = str(kwargs.get("recipe_tag") or ("furnace" if recipe_type == "furnace" else "crafting_table"))

    if recipe_type == "shaped":
        raw_pattern = list(kwargs.get("pattern") or ["   ", "   ", "   "])
        while len(raw_pattern) < 3:
            raw_pattern.append("   ")
        keys_input = kwargs.get("keys") or {}
        key_map = {str(char): _recipe_item_descriptor(item) for char, item in keys_input.items()}
        result_desc = _recipe_item_descriptor(kwargs.get("result_item", "minecraft:air"))
        result_desc["count"] = int(kwargs.get("result_count", 1))
        payload: Dict[str, Any] = {
            "format_version": "1.12",
            "minecraft:recipe_shaped": {
                "description": {"identifier": "{}:{}".format(ns, rid)},
                "tags": [recipe_tag],
                "pattern": raw_pattern[:3],
                "key": key_map,
                "result": result_desc,
            },
        }
    elif recipe_type == "shapeless":
        ingredients_input = kwargs.get("ingredients") or []
        ingredients = [_recipe_item_descriptor(item) for item in ingredients_input]
        result_desc = _recipe_item_descriptor(kwargs.get("result_item", "minecraft:air"))
        result_desc["count"] = int(kwargs.get("result_count", 1))
        payload = {
            "format_version": "1.12",
            "minecraft:recipe_shapeless": {
                "description": {"identifier": "{}:{}".format(ns, rid)},
                "tags": [recipe_tag],
                "ingredients": ingredients,
                "result": result_desc,
            },
        }
    elif recipe_type == "furnace":
        payload = {
            "format_version": "1.12",
            "minecraft:recipe_furnace": {
                "description": {"identifier": "{}:{}".format(ns, rid)},
                "tags": [recipe_tag],
                "input": str(kwargs.get("input_item", "minecraft:air")),
                "output": str(kwargs.get("output_item", "minecraft:air")),
            },
        }
    else:
        raise ValueError("Unknown recipe type: {}".format(recipe_type))

    recipe_text = _dump_json(payload)
    filepath = "{}/netease_recipes/{}_{}.json".format(bp_dir, ns, rid)
    return {
        "recipe": recipe_text,
        "filepath": filepath,
        "files": {filepath: recipe_text},
    }


_ENTITY_PRESETS: Dict[str, Dict[str, Any]] = {
    "mount": {
        "runtime_identifier": "minecraft:horse",
        "components": {
            "minecraft:rideable": {
                "seat_count": 1,
                "family_types": ["player"],
                "interact_text": "action.interact.ride",
            },
            "minecraft:tameable": {"probability": 0.33},
            "minecraft:behavior.follow_owner": {
                "priority": 4,
                "speed_multiplier": 1.0,
                "start_distance": 10,
                "stop_distance": 2,
            },
            "minecraft:input_ground_controlled": {},
        },
    },
    "pet": {
        "runtime_identifier": "minecraft:wolf",
        "components": {
            "minecraft:behavior.follow_owner": {
                "priority": 4,
                "speed_multiplier": 1.0,
                "start_distance": 10,
                "stop_distance": 2,
            },
            "minecraft:behavior.owner_hurt_by_target": {"priority": 1},
            "minecraft:behavior.owner_hurt_target": {"priority": 2},
            "minecraft:tameable": {"probability": 1.0},
            "minecraft:is_tamed": {},
        },
    },
    "npc": {
        "runtime_identifier": "minecraft:villager_v2",
        "components": {
            "minecraft:damage_sensor": {"triggers": [{"deals_damage": False}]},
            "minecraft:pushable": {"is_pushable": False, "is_pushable_by_piston": False},
        },
    },
    "hostile": {
        "runtime_identifier": "minecraft:zombie",
        "components": {
            "minecraft:attack": {"damage": 4},
            "minecraft:behavior.melee_attack": {
                "priority": 3,
                "speed_multiplier": 1.2,
                "track_target": True,
            },
            "minecraft:behavior.nearest_attackable_target": {
                "priority": 2,
                "within_radius": 25.0,
                "entity_types": [
                    {"filters": {"test": "is_family", "subject": "other", "value": "player"}}
                ],
            },
            "minecraft:behavior.hurt_by_target": {"priority": 1},
        },
    },
}


def generate_entity_json(
    namespace: str,
    entity_id: str,
    health: int = 20,
    movement_speed: float = 0.25,
    collision_width: float = 0.6,
    collision_height: float = 1.8,
    family: Optional[List[str]] = None,
    is_spawnable: bool = True,
    is_summonable: bool = True,
    runtime_identifier: Optional[str] = None,
    components: Optional[Dict[str, Any]] = None,
    preset: Optional[str] = None,
    spawn_egg_base_color: str = "#FFFFFF",
    spawn_egg_overlay_color: str = "#000000",
    display_name: str = "自定义生物",
    behavior_pack_dir: Optional[str] = None,
    resource_pack_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """生成完整的自定义实体配套文件集（行为包实体 + 资源包实体 + `.geo.json` 几何体 + 语言文件）。"""
    ns = validate_mod_id(namespace, "namespace")
    eid = validate_content_id(entity_id, "entity_id")
    bp_dir, rp_dir = resolve_pack_dirs(behavior_pack_dir, resource_pack_dir)

    preset_spec = _ENTITY_PRESETS.get(preset or "", {})
    if preset == "npc":
        movement_speed = 0.0

    resolved_runtime = runtime_identifier
    if not resolved_runtime or "{entity_id}" in str(resolved_runtime):
        resolved_runtime = preset_spec.get("runtime_identifier", "minecraft:pig")

    beh_components: Dict[str, Any] = {
        "minecraft:type_family": {"family": list(family) if family else [eid, "mob"]},
        "minecraft:collision_box": {"width": float(collision_width), "height": float(collision_height)},
        "minecraft:health": {"value": int(health), "max": int(health)},
        "minecraft:movement": {"value": float(movement_speed)},
        "minecraft:navigation.walk": {"can_walk": True, "avoid_water": True},
        "minecraft:movement.basic": {},
        "minecraft:jump.static": {},
        "minecraft:physics": {},
    }
    if preset_spec.get("components"):
        beh_components.update(preset_spec["components"])
    if components:
        beh_components.update(components)

    behavior_payload = {
        "format_version": "1.10.0",
        "minecraft:entity": {
            "description": {
                "identifier": "{}:{}".format(ns, eid),
                "is_spawnable": bool(is_spawnable),
                "is_summonable": bool(is_summonable),
                "runtime_identifier": resolved_runtime,
            },
            "component_groups": {
                "default": {},
            },
            "components": beh_components,
            "events": {
                "minecraft:entity_spawned": {"add": {"component_groups": ["default"]}},
            },
        },
    }

    geometry_id = "geometry.{}_{}".format(ns, eid)
    resource_payload = {
        "format_version": "1.10.0",
        "minecraft:client_entity": {
            "description": {
                "identifier": "{}:{}".format(ns, eid),
                "materials": {"default": "entity_alphatest"},
                "textures": {"default": "textures/entity/{}".format(eid)},
                "geometry": {"default": geometry_id},
                "render_controllers": ["controller.render.default"],
                "spawn_egg": {
                    "base_color": spawn_egg_base_color,
                    "overlay_color": spawn_egg_overlay_color,
                },
            }
        },
    }

    box_w = max(4, int(round(collision_width * 16.0)))
    box_h = max(8, int(round(collision_height * 16.0)))
    geometry_payload = {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": geometry_id,
                    "texture_width": 64,
                    "texture_height": 64,
                    "visible_bounds_width": max(2.0, float(collision_width) + 1.0),
                    "visible_bounds_height": max(2.0, float(collision_height) + 1.0),
                    "visible_bounds_offset": [0.0, round(float(collision_height) / 2.0, 2), 0.0],
                },
                "bones": [
                    {
                        "name": "root",
                        "pivot": [0.0, 0.0, 0.0],
                        "cubes": [
                            {
                                "origin": [-box_w / 2.0, 0.0, -box_w / 2.0],
                                "size": [box_w, box_h, box_w],
                                "uv": [0, 0],
                            }
                        ],
                    }
                ],
            }
        ],
    }

    behavior_text = _dump_json(behavior_payload)
    resource_text = _dump_json(resource_payload)
    geometry_text = _dump_json(geometry_payload)
    languages_json = build_languages_json(("zh_CN",))
    lang_text = (
        "entity.{ns}:{eid}.name={name}\n"
        "item.spawn_egg.entity.{ns}:{eid}.name=生成 {name}\n"
    ).format(ns=ns, eid=eid, name=display_name)

    files: Dict[str, str] = {
        "{}/entities/{}_{}.json".format(bp_dir, ns, eid): behavior_text,
        "{}/entity/{}_{}.entity.json".format(rp_dir, ns, eid): resource_text,
        "{}/models/entity/{}_{}.geo.json".format(rp_dir, ns, eid): geometry_text,
        "{}/texts/languages.json".format(rp_dir): languages_json,
        "{}/texts/zh_CN.lang".format(rp_dir): lang_text,
    }
    return {
        "behavior": behavior_text,
        "resource": resource_text,
        "geometry": geometry_text,
        "languages": languages_json,
        "lang": lang_text,
        "files": files,
    }


def generate_loot_table_json(
    pools: List[Dict[str, Any]],
    table_name: str = "custom_loot",
    behavior_pack_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """生成战利品表 JSON。"""
    bp_dir = normalize_pack_dir(behavior_pack_dir, DEFAULT_BEHAVIOR_PACK_DIR, "behavior_pack_dir")
    clean_table = validate_content_id(table_name, "table_name")

    normalized_pools: List[Dict[str, Any]] = []
    for pool in pools or []:
        rolls = int(pool.get("rolls", 1))
        entries_out: List[Dict[str, Any]] = []
        for entry in pool.get("entries", []):
            item_obj: Dict[str, Any] = {
                "type": "item",
                "name": str(entry.get("item", "minecraft:air")),
                "weight": int(entry.get("weight", 1)),
            }
            if "count" in entry and entry["count"] is not None:
                count_val = entry["count"]
                if isinstance(count_val, list) and len(count_val) == 2:
                    item_obj["functions"] = [
                        {"function": "set_count", "count": {"min": int(count_val[0]), "max": int(count_val[1])}}
                    ]
                else:
                    item_obj["functions"] = [
                        {"function": "set_count", "count": int(count_val)}
                    ]
            entries_out.append(item_obj)
        normalized_pools.append({"rolls": rolls, "entries": entries_out})

    loot_text = _dump_json({"pools": normalized_pools})
    filepath = "{}/loot_tables/{}.json".format(bp_dir, clean_table)
    return {
        "loot_table": loot_text,
        "filepath": filepath,
        "files": {filepath: loot_text},
    }


def generate_spawn_rules_json(
    namespace: str,
    entity_id: str,
    population_control: str = "animal",
    spawn_weight: int = 8,
    min_size: int = 2,
    max_size: int = 4,
    behavior_pack_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """生成生物自然生成规则 JSON。"""
    ns = validate_mod_id(namespace, "namespace")
    eid = validate_content_id(entity_id, "entity_id")
    bp_dir = normalize_pack_dir(behavior_pack_dir, DEFAULT_BEHAVIOR_PACK_DIR, "behavior_pack_dir")

    payload = {
        "format_version": "1.8.0",
        "minecraft:spawn_rules": {
            "description": {
                "identifier": "{}:{}".format(ns, eid),
                "population_control": population_control,
            },
            "conditions": [
                {
                    "minecraft:spawns_on_surface": {},
                    "minecraft:spawns_on_block_filter": "minecraft:grass",
                    "minecraft:brightness_filter": {"min": 7, "max": 15, "adjust_for_weather": False},
                    "minecraft:weight": {"default": int(spawn_weight)},
                    "minecraft:herd": {"min_size": int(min_size), "max_size": int(max_size)},
                }
            ],
        },
    }
    spawn_text = _dump_json(payload)
    filepath = "{}/spawn_rules/{}_{}.json".format(bp_dir, ns, eid)
    return {
        "spawn_rules": spawn_text,
        "filepath": filepath,
        "files": {filepath: spawn_text},
    }


def generate_ui_json(
    ui_namespace: str,
    title: str = "自定义界面",
    is_hud: bool = False,
    include_python: bool = True,
    mod_id: str = "mymod",
    behavior_pack_dir: Optional[str] = None,
    resource_pack_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """生成符合网易 JSON UI 规范的界面定义、`ui/_ui_defs.json` 及可选 `ScreenNode` 客户端脚本。"""
    clean_ui_ns = validate_content_id(ui_namespace, "ui_namespace")
    clean_mod_id = validate_mod_id(mod_id, "mod_id")
    bp_dir, rp_dir = resolve_pack_dirs(behavior_pack_dir, resource_pack_dir)

    controls: List[Dict[str, Any]] = [
        {
            "title_label": {
                "type": "label",
                "text": title,
                "color": [1.0, 1.0, 1.0],
                "anchor_from": "top_middle",
                "anchor_to": "top_middle",
                "offset": [0, 12],
                "layer": 10,
                "shadow": True,
            }
        }
    ]

    ui_payload: Dict[str, Any] = {
        "namespace": clean_ui_ns,
    }

    if not is_hud:
        ui_payload["btn_default"] = {
            "type": "image",
            "texture": "textures/netease/common/button/default",
            "layer": 2,
        }
        ui_payload["btn_hover"] = {
            "type": "image",
            "texture": "textures/netease/common/button/hover",
            "layer": 2,
        }
        ui_payload["btn_pressed"] = {
            "type": "image",
            "texture": "textures/netease/common/button/pressed",
            "layer": 2,
        }
        ui_payload["btn_label"] = {
            "type": "label",
            "text": "关闭",
            "color": [1.0, 1.0, 1.0],
            "layer": 5,
            "text_alignment": "center",
        }
        controls.insert(
            0,
            {
                "bg": {
                    "type": "image",
                    "texture": "textures/ui/dialog_background_opaque",
                    "size": ["100%", "100%"],
                    "nineslice_size": 4,
                    "layer": 1,
                }
            },
        )
        controls.append(
            {
                "close_btn@common.button": {
                    "$pressed_button_name": "button.close",
                    "size": [64, 24],
                    "anchor_from": "bottom_middle",
                    "anchor_to": "bottom_middle",
                    "offset": [0, -12],
                    "layer": 6,
                    "controls": [
                        {"default@{}.btn_default".format(clean_ui_ns): {}},
                        {"hover@{}.btn_hover".format(clean_ui_ns): {}},
                        {"pressed@{}.btn_pressed".format(clean_ui_ns): {}},
                        {"button_label@{}.btn_label".format(clean_ui_ns): {}},
                    ],
                }
            }
        )

    ui_payload["main_panel"] = {
        "type": "panel",
        "size": ["100%", "100%"] if is_hud else [220, 140],
        "anchor_from": "center",
        "anchor_to": "center",
        "controls": controls,
    }
    ui_payload["main"] = {
        "type": "panel" if is_hud else "screen",
        "absorbs_input": not is_hud,
        "is_showing_menu": not is_hud,
        "render_game_behind": True,
        "controls": [
            {"main_panel@{}.main_panel".format(clean_ui_ns): {}}
        ],
    }

    ui_rel_path = "ui/{}.json".format(clean_ui_ns)
    ui_json_text = _dump_json(ui_payload)
    ui_defs_text = _dump_json({"ui_defs": [ui_rel_path]})

    files: Dict[str, str] = {
        "{}/{}".format(rp_dir, ui_rel_path): ui_json_text,
        "{}/ui/_ui_defs.json".format(rp_dir): ui_defs_text,
    }

    screen_class = "{}Screen".format(to_camel_case(clean_ui_ns))
    python_code = ""
    python_path = ""
    if include_python:
        project_folder = get_project_folder_name(clean_mod_id)
        python_path = "{}/{}/ui/{}.py".format(bp_dir, project_folder, screen_class)
        files["{}/{}/ui/__init__.py".format(bp_dir, project_folder)] = INIT_FILE_TEMPLATE.format(mod_name=title)
        python_code = UI_SCREEN_PYTHON_TEMPLATE.format(
            title=title,
            screen_class=screen_class,
        )
        files[python_path] = python_code

    return {
        "ui_json": ui_json_text,
        "ui_defs": ui_defs_text,
        "python": python_code,
        "python_path": python_path,
        "screen_class": screen_class,
        "ui_screen_def": "{}.main".format(clean_ui_ns),
        "files": files,
    }


__all__ = [
    "ARMOR_SLOT_SPECS",
    "BLOCK_FORMAT_PROFILES",
    "DEFAULT_BEHAVIOR_PACK_DIR",
    "DEFAULT_MIN_ENGINE_VERSION",
    "DEFAULT_RESOURCE_PACK_DIR",
    "build_blocks_json",
    "build_item_texture_json",
    "build_languages_json",
    "build_pack_manifest_dict",
    "build_terrain_texture_json",
    "generate_block_json",
    "generate_client_system",
    "generate_custom_block",
    "generate_custom_command",
    "generate_custom_item",
    "generate_entity_json",
    "generate_event_listener",
    "generate_item_json",
    "generate_loot_table_json",
    "generate_manifest_json",
    "generate_mod_project",
    "generate_recipe_json",
    "generate_server_system",
    "generate_spawn_rules_json",
    "generate_typed_item_json",
    "generate_ui_json",
    "get_project_folder_name",
    "normalize_pack_dir",
    "parse_version_triplet",
    "render_bundle_markdown",
    "resolve_pack_dirs",
    "to_camel_case",
    "validate_content_id",
    "validate_mod_id",
]
