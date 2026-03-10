"""
我的世界中国版 ModSDK MCP Server
提供 API 文档查询、代码生成、事件系统查询等功能
"""

import json
import asyncio
import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
    GetPromptResult,
    PromptMessage,
    Prompt,
    PromptArgument,
    Resource,
    ResourceTemplate,
)
from .docs_reader import get_docs_reader, reload_docs, DocsReader
from .knowledge_base import (
    ITEM_COMPONENTS,
    BLOCK_COMPONENTS,
    ENTITY_COMPONENTS,
    NETEASE_ITEM_COMPONENTS,
    NETEASE_BLOCK_COMPONENTS,
    MODSDK_SERVER_API,
    MODSDK_EVENTS,
    BEST_PRACTICES,
    search_component,
    get_component_info,
    get_best_practices,
)
from .templates import (
    TemplateGenerator,
    generate_mod_project,
    generate_server_system,
    generate_client_system,
    generate_event_listener,
    generate_custom_command,
    generate_custom_item,
    generate_custom_block,
    # Bedrock JSON 生成器
    BedrockJsonGenerator,
    EntityJsonGenerator,
    LootTableGenerator,
    generate_item_json,
    generate_block_json,
    generate_recipe_json,
    generate_entity_json,
    generate_loot_table_json,
    generate_simple_loot_table,
    generate_spawn_rules_json,
    # 组件生成器
    BedrockComponentsGenerator,
    NeteaseComponentsGenerator,
    BedrockBlockComponentsGenerator,
    # 高级物品生成函数
    generate_sword_item_json,
    generate_pickaxe_item_json,
    generate_axe_item_json,
    generate_shovel_item_json,
    generate_hoe_item_json,
    generate_food_item_json,
    generate_armor_item_json,
    generate_throwable_item_json,
    generate_bow_item_json,
)


# 创建 MCP Server 实例
server = Server(
    "minecraft-modsdk",
    instructions="""你是 NetEase ModSDK（我的世界中国版）开发助手。

【重要】ModSDK 使用 Python 2.7 运行时，生成代码时必须确保兼容性！

【最高优先级：文档优先原则】

⚠️ 在编写任何代码之前，必须先查阅文档！这是强制性要求。

1. **事件参数必须查文档**
   - 使用任何事件前，必须先调用 search_docs 或 search_event 查询该事件的参数定义
   - 不同事件的参数名不一致！例如：
     * ServerPlayerTryDestroyBlockEvent 使用 "playerId" 和 "cancel"
     * ServerItemUseOnEvent 使用 "entityId" 和 "ret"
   - 禁止假设参数名，必须查证后再使用

2. **API 接口必须查文档**
   - 使用任何 API 前，必须先调用 search_api 查询接口定义
   - 确认参数类型、返回值、是否存在该接口
   - 禁止凭记忆或假设编写 API 调用

3. **组件和 JSON 格式必须查文档**
   - 使用 search_component 查询组件的正确格式
   - 网易版和国际版的 format_version 和组件名称不同
   - 网易版物品使用 "1.10"，方块使用 "1.10.0"

4. **参考示例项目**
   - input/ 目录下有示例项目，可参考实际用法
   - 使用 search_docs 时会同时搜索文档和示例代码

【强制遵循的代码规范】

在生成任何 ModSDK Python 代码时，你必须遵循以下规则：

0. **Python 2.7 兼容性（最重要）**
   - 禁止使用 f-string（f"..."），使用 "{}".format() 或 % 格式化
   - 禁止使用 print() 函数，使用 print 语句
   - 禁止使用 type hints（类型注解）
   - 禁止使用 async/await 语法
   - 文件顶部添加: # -*- coding: utf-8 -*-
   - 字典使用 .iteritems() 而非 .items()（大数据时）
   - 使用 xrange 代替 range（大范围时）

1. **客户端/服务端严格分离**
   - ServerSystem 禁止 import clientApi
   - ClientSystem 禁止 import serverApi
   - 跨端通信只能使用事件系统

2. **GetEngineCompFactory 必须缓存**
   在文件顶部缓存：
   CF = serverApi.GetEngineCompFactory()
   levelId = serverApi.GetLevelId()
   禁止在函数内重复调用 GetEngineCompFactory()

3. **import 必须在文件顶部**
   禁止在函数/方法内部 import

4. **Tick 逻辑必须降帧**
   使用质数间隔：if self.tick % 7 == 0:
   避免每帧执行耗时操作

5. **ServerBlockEntityTickEvent 必须加盐**
   使用坐标计算 salt 错开执行时机：
   salt = (x * 31 + y * 17 + z * 13) % 20

6. **点对点通信优先**
   优先使用 NotifyToClient(playerId, ...)
   谨慎使用 BroadcastToAllClient(...)

【UI 界面开发规范】

1. **_ui_defs.json 文件规范**
   - 必须放在 resource_pack/ui/ 目录下
   - 必须使用对象格式: {"ui_defs": ["ui/xxx.json"]}
   - 不能是纯数组格式

2. **UI 注册时机**
   - RegisterUI 必须在 UiInitFinished 事件回调中调用
   - 不能在 __init__ 或系统初始化时直接调用

3. **控件类型转换**
   - GetBaseUIControl() 返回 BaseUIControl
   - 按钮操作需要: asButton() 转换后调用 AddTouchEventParams/SetButtonTouchUpCallback
   - 文本操作需要: asLabel() 转换后调用 SetText()

4. **从 UI 发送事件到服务端**
   - 不能用 clientApi.BroadcastEvent()
   - 应该用: clientApi.GetSystem().NotifyToServer()

5. **关闭 UI 界面**
   - 使用 self.SetRemove()，不要用 clientApi.PopScreen()
   - PopScreen 可能影响原版 UI

6. **防止点击穿透**
   - 使用 input_panel + modal:true
   - 不要设置 is_swallow:true，否则子控件按钮无法点击

请在生成代码时自动应用这些规范，无需用户额外提醒。

【代码审查能力】

当用户请求代码审查时，检查以下问题：
- 🔴 严重：客户端/服务端混用、GetEngineCompFactory 未缓存、函数内 import、Tick 无降帧、事件参数名错误
- 🟠 警告：BroadcastToAllClient 滥用、ServerBlockEntityTickEvent 无加盐、组件重复创建、未查文档使用 API
- 🟡 建议：魔法数字、缺少错误处理、命名不规范

输出格式：问题严重程度 + 位置 + 问题代码 + 修复建议"""
)

# Skills 目录路径
SKILLS_PATH = Path(os.environ.get("MODSDK_SKILLS_PATH", "./skills"))
STANDARD_PATH = Path(os.environ.get("MODSDK_STANDARD_PATH", "./standard"))


# ============================================================================
# Skills 读取器
# ============================================================================

class SkillsReader:
    """读取 Skills 和 Standard 文档"""
    
    def __init__(self):
        self.skills = {}
        self.standards = {}
        self._load_all()
    
    def _load_all(self):
        """加载所有 Skills 和 Standard 文件"""
        # 加载 Skills
        if SKILLS_PATH.exists():
            for filepath in SKILLS_PATH.glob("*.md"):
                name = filepath.stem
                try:
                    content = filepath.read_text(encoding="utf-8")
                    self.skills[name] = {
                        "name": name,
                        "filepath": str(filepath),
                        "content": content,
                        "description": self._extract_description(content)
                    }
                except Exception as e:
                    print(f"加载 Skill 失败: {filepath}, 错误: {e}")
        
        # 加载 Standard
        if STANDARD_PATH.exists():
            for filepath in STANDARD_PATH.glob("*.md"):
                name = filepath.stem
                try:
                    content = filepath.read_text(encoding="utf-8")
                    self.standards[name] = {
                        "name": name,
                        "filepath": str(filepath),
                        "content": content,
                        "description": self._extract_description(content)
                    }
                except Exception as e:
                    print(f"加载 Standard 失败: {filepath}, 错误: {e}")
    
    def _extract_description(self, content: str) -> str:
        """从内容中提取描述（第一个标题后的第一段）"""
        lines = content.split('\n')
        found_title = False
        description_lines = []
        
        for line in lines:
            if line.startswith('# '):
                found_title = True
                continue
            if found_title:
                if line.strip() == '':
                    if description_lines:
                        break
                    continue
                if line.startswith('#'):
                    break
                description_lines.append(line.strip())
                if len(description_lines) >= 2:
                    break
        
        return ' '.join(description_lines)[:200] if description_lines else "无描述"
    
    def list_skills(self) -> List[Dict]:
        """列出所有 Skills"""
        return list(self.skills.values())
    
    def list_standards(self) -> List[Dict]:
        """列出所有 Standards"""
        return list(self.standards.values())
    
    def get_skill(self, name: str) -> Optional[Dict]:
        """获取指定 Skill"""
        return self.skills.get(name)
    
    def get_standard(self, name: str) -> Optional[Dict]:
        """获取指定 Standard"""
        return self.standards.get(name)
    
    def reload(self):
        """重新加载"""
        self.skills = {}
        self.standards = {}
        self._load_all()


# 全局 Skills 读取器实例
_skills_reader = None  # type: Optional[SkillsReader]


def get_skills_reader() -> SkillsReader:
    """获取 Skills 读取器实例"""
    global _skills_reader
    if _skills_reader is None:
        _skills_reader = SkillsReader()
    return _skills_reader


# ============================================================================
# MCP Resources（用于提供 Skills 文件）
# ============================================================================

@server.list_resources()
async def list_resources() -> List[Resource]:
    """列出所有可用的 Resources（Skills 和 Standards）"""
    skills_reader = get_skills_reader()
    resources = []
    
    # 添加 Skills 资源
    for skill in skills_reader.list_skills():
        resources.append(
            Resource(
                uri=f"skill://{skill['name']}",
                name=f"Skill: {skill['name']}",
                description=skill['description'],
                mimeType="text/markdown"
            )
        )
    
    # 添加 Standard 资源
    for standard in skills_reader.list_standards():
        resources.append(
            Resource(
                uri=f"standard://{standard['name']}",
                name=f"Standard: {standard['name']}",
                description=standard['description'],
                mimeType="text/markdown"
            )
        )
    
    # 添加合并的代码规范资源
    resources.append(
        Resource(
            uri="skill://code-generation-rules",
            name="NetEase ModSDK 代码生成规范（完整版）",
            description="生成 ModSDK 代码时必须遵循的所有规则，包括性能优化、架构规范等",
            mimeType="text/markdown"
        )
    )
    
    return resources


@server.read_resource()
async def read_resource(uri: str) -> str:
    """读取指定的 Resource 内容"""
    skills_reader = get_skills_reader()
    
    # 解析 URI
    if uri.startswith("skill://"):
        name = uri[8:]  # 移除 "skill://" 前缀
        
        # 特殊资源：合并的代码规范
        if name == "code-generation-rules":
            return _get_combined_rules()
        
        skill = skills_reader.get_skill(name)
        if skill:
            return skill['content']
        else:
            return f"Skill '{name}' 不存在。"
    
    elif uri.startswith("standard://"):
        name = uri[11:]  # 移除 "standard://" 前缀
        standard = skills_reader.get_standard(name)
        if standard:
            return standard['content']
        else:
            return f"Standard '{name}' 不存在。"
    
    else:
        return f"未知的资源 URI: {uri}"


def _get_combined_rules() -> str:
    """获取合并的代码生成规范"""
    skills_reader = get_skills_reader()
    
    # 尝试获取优化规范
    optimization_skill = skills_reader.get_skill("netease-optimization-expert")
    
    if optimization_skill:
        return optimization_skill['content']
    
    # 如果没有找到，返回内置的基本规则
    return """# NetEase ModSDK 代码生成规范

## 强制规则

### 1. 客户端/服务端分离
- 禁止在 ServerSystem 中 import clientApi
- 禁止在 ClientSystem 中 import serverApi
- 使用事件通信进行跨端交互

### 2. 缓存 GetEngineCompFactory
```python
CF = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()
```

### 3. import 放在文件顶部
不要在函数内 import

### 4. Tick 逻辑降帧
使用 `self.tick % N == 0` 降低执行频率

### 5. 点对点通信
使用 `NotifyToClient(playerId, ...)` 而非 `BroadcastToAllClient(...)`
"""


# ============================================================================
# 工具定义
# ============================================================================

# 代码生成强制规范（嵌入到工具描述中）
CODE_GENERATION_RULES = """
【NetEase ModSDK 代码生成强制规范】

生成代码时必须遵循以下规则：

1. **客户端/服务端严格分离**
   - ServerSystem 禁止 import clientApi
   - ClientSystem 禁止 import serverApi
   - 跨端通信只能使用事件系统

2. **GetEngineCompFactory 必须缓存**
   ```python
   # ✅ 正确：模块级缓存
   CF = serverApi.GetEngineCompFactory()
   levelId = serverApi.GetLevelId()
   
   # ❌ 错误：每次调用都创建
   def func():
       comp = serverApi.GetEngineCompFactory().CreateXxx()
   ```

3. **import 必须在文件顶部**
   - 禁止在函数/方法内部 import
   - 所有依赖必须在文件开头声明

4. **Tick 逻辑必须降帧**
   ```python
   # ✅ 正确：使用质数降帧
   def OnTickServer(self):
       self.tick += 1
       if self.tick % 7 == 0:  # 每7帧执行一次
           self.DoExpensiveWork()
   ```

5. **ServerBlockEntityTickEvent 必须加盐**
   ```python
   # ✅ 正确：使用坐标加盐错开执行
   def OnBlockTick(self, args):
       x, y, z = args['posX'], args['posY'], args['posZ']
       salt = (x * 31 + y * 17 + z * 13) % 20
       if self.tick % 20 == salt:
           self.DoBlockLogic(args)
   ```

6. **点对点通信优先**
   ```python
   # ✅ 优先使用
   self.NotifyToClient(playerId, "EventName", data)
   
   # ⚠️ 谨慎使用（仅全服广播时）
   self.BroadcastToAllClient("EventName", data)
   ```
""".strip()


@server.list_tools()
async def list_tools() -> List[Tool]:
    """列出所有可用的工具"""
    return [
        # 文档查询工具
        Tool(
            name="search_docs",
            description="""搜索 ModSDK 文档（支持模糊搜索）。
            
功能特性：
- 模糊匹配：允许拼写错误，如 "getBlok" 可匹配 "getBlock"
- 驼峰分词：搜索 "comp factory" 可匹配 "GetEngineCompFactory"
- 中文搜索：支持中文关键词搜索
- 相关度排序：按匹配度自动排序结果

搜索示例：
- "玩家事件" - 查找玩家相关的事件
- "GetEngineCompFactory" - 查找组件工厂 API
- "背包 物品" - 查找背包和物品相关内容
- "tick 优化" - 查找 tick 相关的优化方法
""",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索关键词，支持模糊匹配、驼峰分词、中文搜索"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "返回结果数量限制，默认 10",
                        "default": 10
                    },
                    "fuzzy": {
                        "type": "boolean",
                        "description": "是否启用模糊搜索，默认 true。关闭后使用精确匹配。",
                        "default": True
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_document",
            description="获取指定文档的完整内容。需要提供文档的文件路径。",
            inputSchema={
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "文档文件路径，如 'api/block.md'"
                    }
                },
                "required": ["filepath"]
            }
        ),
        Tool(
            name="get_document_section",
            description="获取文档中指定章节的内容。",
            inputSchema={
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "文档文件路径"
                    },
                    "section_title": {
                        "type": "string",
                        "description": "章节标题"
                    }
                },
                "required": ["filepath", "section_title"]
            }
        ),
        Tool(
            name="list_documents",
            description="列出所有可用的文档。",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_document_structure",
            description="获取文档的结构（章节目录）。",
            inputSchema={
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "文档文件路径"
                    }
                },
                "required": ["filepath"]
            }
        ),
        Tool(
            name="reload_documents",
            description="重新加载所有文档。当文档更新后使用。",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        
        # 代码生成工具（描述中包含强制规范）
        Tool(
            name="generate_mod_project",
            description=f"""生成一个完整的 Mod 项目模板，包含入口文件、服务端系统、客户端系统。

【重要：脚本目录必须直接放在 behavior_pack 下面】
脚本文件夹直接放在行为包根目录下，这是网易 ModSDK 的强制要求！

【项目结构规范】
1. 脚本文件夹命名：{{mod_id}}_Script（如 myMod_Script）
2. 脚本文件夹必须位于：behavior_pack_{{mod_id}}/{{mod_id}}_Script/（直接在行为包根目录下）
3. 每个 Python 文件夹包含 __init__.py
4. modMain.py 的 @Mod.Binding(name=...) 与脚本文件夹名同步

【完整部署结构】
behavior_pack_{{mod_id}}/              # 行为包根目录
├── {{mod_id}}_Script/                 # 脚本根目录（直接在行为包下，使用 _Script 后缀）
│   ├── __init__.py                    # Python 包标识（根目录）
│   ├── modMain.py                     # Mod 入口文件
│   └── scripts/
│       ├── __init__.py                # Python 包标识
│       └── {{mod_id}}/                # 脚本子目录（不加 _Script）
│           ├── __init__.py            # Python 包标识
│           ├── server.py              # 服务端系统
│           └── client.py              # 客户端系统
├── netease_items_beh/                 # 自定义物品行为 JSON
├── netease_blocks/                    # 自定义方块 JSON
├── netease_recipes/                   # 合成配方 JSON
├── entities/                          # 自定义实体 JSON
└── loot_tables/                       # 战利品表 JSON

resource_pack_{{mod_id}}/              # 资源包根目录
├── netease_items_res/                 # 自定义物品资源 JSON
├── entity/                            # 自定义实体资源 JSON
└── texts/                             # 本地化文件
    └── zh_CN.lang

【RegisterSystem 路径规范】
路径必须从脚本根目录开始：
- 服务端: "{{mod_id}}_Script.scripts.{{mod_id}}.server.XxxServerSystem"
- 客户端: "{{mod_id}}_Script.scripts.{{mod_id}}.client.XxxClientSystem"

{CODE_GENERATION_RULES}""",
            inputSchema={
                "type": "object",
                "properties": {
                    "mod_name": {
                        "type": "string",
                        "description": "Mod 名称，如 '我的第一个Mod'"
                    },
                    "mod_id": {
                        "type": "string",
                        "description": "Mod ID，用于代码中的标识符，如 'my_first_mod'"
                    },
                    "author": {
                        "type": "string",
                        "description": "作者名称",
                        "default": "Author"
                    },
                    "description": {
                        "type": "string",
                        "description": "Mod 描述",
                        "default": "A Minecraft mod"
                    },
                    "version": {
                        "type": "string",
                        "description": "版本号",
                        "default": "1.0.0"
                    }
                },
                "required": ["mod_name", "mod_id"]
            }
        ),
        Tool(
            name="generate_server_system",
            description="生成服务端系统代码。",
            inputSchema={
                "type": "object",
                "properties": {
                    "mod_name": {
                        "type": "string",
                        "description": "Mod 名称"
                    },
                    "class_name": {
                        "type": "string",
                        "description": "类名前缀，如 'MyMod'"
                    }
                },
                "required": ["mod_name", "class_name"]
            }
        ),
        Tool(
            name="generate_client_system",
            description="生成客户端系统代码。",
            inputSchema={
                "type": "object",
                "properties": {
                    "mod_name": {
                        "type": "string",
                        "description": "Mod 名称"
                    },
                    "class_name": {
                        "type": "string",
                        "description": "类名前缀，如 'MyMod'"
                    }
                },
                "required": ["mod_name", "class_name"]
            }
        ),
        Tool(
            name="generate_event_listener",
            description="生成事件监听器代码。",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_name": {
                        "type": "string",
                        "description": "事件名称，如 'PlayerJoinEvent'"
                    },
                    "event_description": {
                        "type": "string",
                        "description": "事件描述",
                        "default": "事件处理"
                    }
                },
                "required": ["event_name"]
            }
        ),
        Tool(
            name="generate_custom_command",
            description="生成自定义命令代码。",
            inputSchema={
                "type": "object",
                "properties": {
                    "command_name": {
                        "type": "string",
                        "description": "命令名称，如 'teleport'"
                    }
                },
                "required": ["command_name"]
            }
        ),
        Tool(
            name="generate_custom_item",
            description="生成自定义物品代码和 JSON 配置。",
            inputSchema={
                "type": "object",
                "properties": {
                    "item_id": {
                        "type": "string",
                        "description": "物品ID，如 'magic_sword'"
                    },
                    "namespace": {
                        "type": "string",
                        "description": "命名空间，如 'mymod'",
                        "default": "mymod"
                    },
                    "display_name": {
                        "type": "string",
                        "description": "显示名称",
                        "default": "自定义物品"
                    },
                    "max_stack": {
                        "type": "integer",
                        "description": "最大堆叠数量",
                        "default": 64
                    }
                },
                "required": ["item_id"]
            }
        ),
        Tool(
            name="generate_custom_block",
            description="生成自定义方块代码和 JSON 配置。",
            inputSchema={
                "type": "object",
                "properties": {
                    "block_id": {
                        "type": "string",
                        "description": "方块ID，如 'magic_ore'"
                    },
                    "namespace": {
                        "type": "string",
                        "description": "命名空间，如 'mymod'",
                        "default": "mymod"
                    },
                    "destroy_time": {
                        "type": "number",
                        "description": "破坏时间（秒）",
                        "default": 1.0
                    },
                    "explosion_resistance": {
                        "type": "number",
                        "description": "爆炸抗性",
                        "default": 1.0
                    }
                },
                "required": ["block_id"]
            }
        ),
        
        # ============================================================
        # Bedrock JSON 生成工具
        # ============================================================
        Tool(
            name="generate_item_json",
            description="""生成自定义物品的 JSON 文件（行为包 + 资源包）。

【适用于 NetEase 我的世界数据驱动物品】

【重要】format_version 必须使用 "1.10"，这是网易版的强制要求！

生成内容：
- 行为包物品 JSON: behavior_pack_<namespace>/netease_items_beh/<namespace>_<item_id>.json
- 资源包物品 JSON: resource_pack_<namespace>/netease_items_res/<namespace>_<item_id>.json

物品组件支持（1.10 版本格式）：
- minecraft:max_stack_size - 最大堆叠数（直接数值）
- minecraft:hand_equipped - 是否手持装备（布尔值）
- minecraft:food - 食物组件
- minecraft:max_damage - 耐久度
- netease:customtips - 网易自定义提示
等更多 NetEase 特有组件

【注意】资源包的 minecraft:icon 使用字符串格式，不是对象格式""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {
                        "type": "string",
                        "description": "命名空间（建议使用 mod 简称，全小写，如 'mymod'）"
                    },
                    "item_id": {
                        "type": "string",
                        "description": "物品ID（全小写+下划线，如 'magic_sword'）"
                    },
                    "category": {
                        "type": "string",
                        "description": "创造栏分类 (items/equipment/construction/nature/none)",
                        "default": "items"
                    },
                    "max_stack_size": {
                        "type": "integer",
                        "description": "最大堆叠数量 (1-64)",
                        "default": 64
                    },
                    "components": {
                        "type": "object",
                        "description": "额外物品组件（如 minecraft:food, minecraft:durability 等）"
                    }
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_block_json",
            description="""生成自定义方块的 JSON 文件。

【适用于 NetEase 我的世界数据驱动方块】

【重要】format_version 必须使用 "1.10.0"，这是网易版的强制要求！

生成内容：
- 行为包方块 JSON: behavior_pack_<namespace>/netease_blocks/<namespace>_<block_id>.json

方块组件支持（1.10.0 版本格式，使用旧版组件名）：
- minecraft:destroy_time - 挖掘时间 {"value": 2.0}
- minecraft:explosion_resistance - 爆炸抗性 {"value": 10.0}
- minecraft:block_light_emission - 发光等级 {"emission": 15}
- minecraft:block_light_absorption - 遮光等级 {"value": 15}
- minecraft:friction - 摩擦力
- netease:solid - 是否为固体方块
- netease:tier - 挖掘等级和工具类型
等更多网易特有组件

【注意】不要使用 1.19.20+ 的新版组件名（如 destructible_by_mining）""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {
                        "type": "string",
                        "description": "命名空间"
                    },
                    "block_id": {
                        "type": "string",
                        "description": "方块ID（全小写+下划线）"
                    },
                    "destroy_time": {
                        "type": "number",
                        "description": "挖掘时间（秒）",
                        "default": 1.5
                    },
                    "explosion_resistance": {
                        "type": "number",
                        "description": "爆炸抗性",
                        "default": 10.0
                    },
                    "light_emission": {
                        "type": "integer",
                        "description": "发光等级 [0-15]",
                        "default": 0
                    },
                    "map_color": {
                        "type": "string",
                        "description": "地图颜色（十六进制，如 '#FF5500'）",
                        "default": "#FFFFFF"
                    },
                    "components": {
                        "type": "object",
                        "description": "额外方块组件"
                    }
                },
                "required": ["namespace", "block_id"]
            }
        ),
        Tool(
            name="generate_recipe_json",
            description="""生成合成配方 JSON 文件。

【配方类型】
- shaped: 有序合成（工作台）
- shapeless: 无序合成（工作台）
- furnace: 熔炉配方

【文件位置】
behavior_pack_<namespace>/netease_recipes/<recipe_id>.json""",
            inputSchema={
                "type": "object",
                "properties": {
                    "recipe_type": {
                        "type": "string",
                        "description": "配方类型: shaped/shapeless/furnace",
                        "enum": ["shaped", "shapeless", "furnace"]
                    },
                    "namespace": {
                        "type": "string",
                        "description": "命名空间"
                    },
                    "recipe_id": {
                        "type": "string",
                        "description": "配方ID"
                    },
                    "pattern": {
                        "type": "array",
                        "description": "合成图案（shaped 专用），如 ['DDD', ' S ', ' S ']",
                        "items": {"type": "string"}
                    },
                    "keys": {
                        "type": "object",
                        "description": "字符到物品的映射（shaped 专用），如 {'D': 'minecraft:diamond', 'S': 'minecraft:stick'}"
                    },
                    "ingredients": {
                        "type": "array",
                        "description": "材料列表（shapeless 专用），如 ['minecraft:diamond', 'minecraft:stick']",
                        "items": {"type": "string"}
                    },
                    "input_item": {
                        "type": "string",
                        "description": "输入物品（furnace 专用）"
                    },
                    "output_item": {
                        "type": "string",
                        "description": "输出物品（furnace 专用）"
                    },
                    "result_item": {
                        "type": "string",
                        "description": "结果物品（shaped/shapeless 专用）"
                    },
                    "result_count": {
                        "type": "integer",
                        "description": "结果数量",
                        "default": 1
                    }
                },
                "required": ["recipe_type", "namespace", "recipe_id"]
            }
        ),
        Tool(
            name="generate_entity_json",
            description="""生成自定义实体 JSON 文件（行为包 + 资源包）。

【适用于自定义生物/实体】
遵循 NetEase ModSDK 3.7 官方文档规范

生成内容：
- 行为包实体 JSON: behavior_pack_<namespace>/entities/<namespace>_<entity_id>.json
- 资源包实体 JSON: resource_pack_<namespace>/entity/<namespace>_<entity_id>.entity.json

实体组件支持：
- minecraft:health - 生命值
- minecraft:movement - 移动速度
- minecraft:collision_box - 碰撞箱
- minecraft:type_family - 实体家族
- minecraft:physics - 物理
- minecraft:navigation.walk - 寻路
- runtime_identifier - 基于哪个原版实体构建
等更多组件""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {
                        "type": "string",
                        "description": "命名空间"
                    },
                    "entity_id": {
                        "type": "string",
                        "description": "实体ID（全小写+下划线）"
                    },
                    "health": {
                        "type": "integer",
                        "description": "生命值",
                        "default": 20
                    },
                    "movement_speed": {
                        "type": "number",
                        "description": "移动速度",
                        "default": 0.25
                    },
                    "collision_width": {
                        "type": "number",
                        "description": "碰撞箱宽度",
                        "default": 0.6
                    },
                    "collision_height": {
                        "type": "number",
                        "description": "碰撞箱高度",
                        "default": 1.8
                    },
                    "runtime_identifier": {
                        "type": "string",
                        "description": "基于哪个原版实体构建（如 minecraft:pig, minecraft:zombie）。决定实体的基础行为特性。",
                        "default": "minecraft:{entity_id}"
                    },
                    "spawn_egg_base_color": {
                        "type": "string",
                        "description": "刷怪蛋底色（十六进制）",
                        "default": "#FFFFFF"
                    },
                    "spawn_egg_overlay_color": {
                        "type": "string",
                        "description": "刷怪蛋覆盖色（十六进制）",
                        "default": "#000000"
                    }
                },
                "required": ["namespace", "entity_id"]
            }
        ),
        Tool(
            name="generate_loot_table_json",
            description="""生成战利品表 JSON 文件。

【适用于】
- 实体死亡掉落
- 方块破坏掉落
- 宝箱战利品

【文件位置】
behavior_pack_<namespace>/loot_tables/<path>.json

【池（Pool）结构】
每个池包含多个条目，每次从池中随机抽取""",
            inputSchema={
                "type": "object",
                "properties": {
                    "pools": {
                        "type": "array",
                        "description": "战利品池列表",
                        "items": {
                            "type": "object",
                            "properties": {
                                "rolls": {"type": "integer", "description": "抽取次数"},
                                "entries": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "item": {"type": "string", "description": "物品ID"},
                                            "weight": {"type": "integer", "description": "权重"},
                                            "count": {"description": "数量或范围 [min, max]"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "required": ["pools"]
            }
        ),
        Tool(
            name="generate_spawn_rules_json",
            description="""生成实体生成规则 JSON 文件。

【适用于自然生成的生物】

【文件位置】
behavior_pack_<namespace>/spawn_rules/<namespace>_<entity_id>.json

【控制项】
- population_control: 种群控制类型 (animal/monster/water_animal/ambient)
- spawn_weight: 生成权重
- herd_size: 群组大小""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {
                        "type": "string",
                        "description": "命名空间"
                    },
                    "entity_id": {
                        "type": "string",
                        "description": "实体ID"
                    },
                    "population_control": {
                        "type": "string",
                        "description": "种群控制类型",
                        "enum": ["animal", "monster", "water_animal", "ambient"],
                        "default": "animal"
                    },
                    "spawn_weight": {
                        "type": "integer",
                        "description": "生成权重",
                        "default": 8
                    },
                    "min_size": {
                        "type": "integer",
                        "description": "最小群组大小",
                        "default": 2
                    },
                    "max_size": {
                        "type": "integer",
                        "description": "最大群组大小",
                        "default": 4
                    }
                },
                "required": ["namespace", "entity_id"]
            }
        ),
        
        # ============================================================
        # 高级物品生成工具（一键生成复杂物品）
        # ============================================================
        Tool(
            name="generate_sword_json",
            description="""【一键生成】自定义剑类武器 JSON
包含：耐久度、武器伤害、附魔、可修复等完整组件配置。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "damage": {"type": "integer", "description": "攻击伤害", "default": 5},
                    "durability": {"type": "integer", "description": "耐久值", "default": 131},
                    "enchantability": {"type": "integer", "description": "附魔等级", "default": 15},
                    "repair_material": {"type": "string", "description": "修复材料（如 minecraft:iron_ingot）"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_pickaxe_json",
            description="""【一键生成】自定义镐类工具 JSON
包含：耐久度、挖掘速度（石头/金属类方块）、附魔、可修复。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "durability": {"type": "integer", "description": "耐久值", "default": 131},
                    "mining_speed": {"type": "integer", "description": "挖掘速度", "default": 4},
                    "enchantability": {"type": "integer", "description": "附魔等级", "default": 15},
                    "repair_material": {"type": "string", "description": "修复材料"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_axe_json",
            description="""【一键生成】自定义斧类工具 JSON
包含：攻击伤害、耐久度、木头类方块挖掘加速、附魔、可修复。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "damage": {"type": "integer", "description": "攻击伤害", "default": 4},
                    "durability": {"type": "integer", "description": "耐久值", "default": 131},
                    "mining_speed": {"type": "integer", "description": "挖掘速度", "default": 4},
                    "enchantability": {"type": "integer", "description": "附魔等级", "default": 15},
                    "repair_material": {"type": "string", "description": "修复材料"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_shovel_json",
            description="""【一键生成】自定义锹类工具 JSON
包含：耐久度、泥土/沙子/沙砾类方块挖掘加速、附魔、可修复。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "durability": {"type": "integer", "description": "耐久值", "default": 131},
                    "mining_speed": {"type": "integer", "description": "挖掘速度", "default": 4},
                    "enchantability": {"type": "integer", "description": "附魔等级", "default": 15},
                    "repair_material": {"type": "string", "description": "修复材料"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_hoe_json",
            description="""【一键生成】自定义锄类工具 JSON
包含：耐久度、附魔、可修复。用于耕地。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "durability": {"type": "integer", "description": "耐久值", "default": 131},
                    "enchantability": {"type": "integer", "description": "附魔等级", "default": 15},
                    "repair_material": {"type": "string", "description": "修复材料"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_food_json",
            description="""【一键生成】自定义食物物品 JSON
包含：饥饿值、饱和度、可随时食用、药水效果等。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "nutrition": {"type": "integer", "description": "饥饿值", "default": 4},
                    "saturation": {"type": "string", "description": "饱和度(low/normal/good/max)", "default": "normal"},
                    "can_always_eat": {"type": "boolean", "description": "是否可随时食用", "default": False},
                    "effects": {
                        "type": "array",
                        "description": "药水效果列表 [{name, duration, amplifier, chance}]"
                    }
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_armor_json",
            description="""【一键生成】自定义盔甲物品 JSON
包含：护甲值、穿戴槽位、耐久度、附魔、可修复。

槽位选项：slot.armor.head / slot.armor.chest / slot.armor.legs / slot.armor.feet""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "slot": {
                        "type": "string",
                        "description": "穿戴槽位",
                        "enum": ["slot.armor.head", "slot.armor.chest", "slot.armor.legs", "slot.armor.feet"],
                        "default": "slot.armor.chest"
                    },
                    "protection": {"type": "integer", "description": "护甲值", "default": 5},
                    "durability": {"type": "integer", "description": "耐久值", "default": 165},
                    "enchantability": {"type": "integer", "description": "附魔等级", "default": 9},
                    "repair_material": {"type": "string", "description": "修复材料"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_bow_json",
            description="""【一键生成】自定义弓类武器 JSON
包含：耐久度、蓄力时间、弓箭发射、附魔。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "durability": {"type": "integer", "description": "耐久值", "default": 384},
                    "max_draw_duration": {"type": "number", "description": "最大蓄力时间", "default": 1.0},
                    "enchantability": {"type": "integer", "description": "附魔等级", "default": 1}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_throwable_json",
            description="""【一键生成】自定义可投掷物品 JSON（如雪球、末影珍珠）
包含：投掷组件、弹射物实体、发射力度。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "projectile_entity": {"type": "string", "description": "投掷出的实体ID"},
                    "max_draw_duration": {"type": "number", "description": "最大蓄力时间", "default": 0.0},
                    "launch_power": {"type": "number", "description": "发射力度", "default": 1.0}
                },
                "required": ["namespace", "item_id", "projectile_entity"]
            }
        ),
        
        # 代码审查工具
        Tool(
            name="review_code",
            description="""审查 NetEase ModSDK 代码，检测性能问题、架构违规和 Python 2.7 兼容性问题。

【重要】ModSDK 运行在 Python 2.7 环境！

【审查检查项】

🔴 严重问题（CRITICAL）- 必须修复：
1. Python 2.7 不兼容语法（f-string、type hints、print()函数、async/await）
2. 客户端/服务端混用（ServerSystem 导入 clientApi）
3. GetEngineCompFactory 未缓存（在函数内调用）
4. 函数内 import（每次调用都执行 import）
5. Tick 事件无降帧（每帧执行耗时操作）

🟠 警告问题（WARNING）- 建议修复：
6. BroadcastToAllClient 滥用
7. ServerBlockEntityTickEvent 无加盐
8. 组件重复创建（循环内创建组件）
9. 大量字符串拼接

🟡 优化建议（SUGGESTION）- 可选：
10. 魔法数字
11. 缺少错误处理
12. 事件命名不规范

【输出格式】
对每个问题输出：严重程度 + 位置 + 问题代码 + 修复建议

【审查报告】
最后提供统计和整体评价""",
            inputSchema={
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "要审查的代码内容"
                    },
                    "filename": {
                        "type": "string",
                        "description": "文件名（可选，用于定位问题）",
                        "default": "unknown.py"
                    }
                },
                "required": ["code"]
            }
        ),
        
        # ============================================================
        # 知识库查询工具
        # ============================================================
        Tool(
            name="search_components",
            description="""搜索基岩版组件（物品/方块/实体/网易特有）。

【支持的组件类型】
- item: 物品组件（minecraft:food, minecraft:durability 等）
- block: 方块组件（minecraft:friction, minecraft:geometry 等）
- entity: 实体组件（minecraft:health, minecraft:movement 等）
- netease: 网易特有组件（netease:customtips, netease:tier 等）
- all: 搜索所有类型（默认）

【使用场景】
- 查询组件用法和属性
- 确认组件是否存在
- 获取组件配置示例""",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索关键词（组件名或中文描述）"
                    },
                    "component_type": {
                        "type": "string",
                        "description": "组件类型",
                        "enum": ["all", "item", "block", "entity", "netease"],
                        "default": "all"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_component_details",
            description="""获取指定组件的详细信息。

需要提供完整的组件 ID，如：
- minecraft:food
- minecraft:durability
- netease:customtips
- minecraft:behavior.melee_attack""",
            inputSchema={
                "type": "object",
                "properties": {
                    "component_id": {
                        "type": "string",
                        "description": "组件 ID（如 minecraft:food）"
                    }
                },
                "required": ["component_id"]
            }
        ),
        Tool(
            name="list_components",
            description="""列出所有可用的组件。

【组件分类】
- item: 物品组件（22个）
- block: 方块组件（22个）
- entity: 实体组件（19个）
- netease_item: 网易物品组件（3个）
- netease_block: 网易方块组件（7个）""",
            inputSchema={
                "type": "object",
                "properties": {
                    "component_type": {
                        "type": "string",
                        "description": "组件类型",
                        "enum": ["item", "block", "entity", "netease_item", "netease_block", "all"],
                        "default": "all"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="get_best_practices",
            description="""获取 ModSDK 最佳实践规则。

【规则分类】
- python27_compatibility: Python 2.7 兼容性规则
- client_server_separation: 客户端/服务端分离规则
- performance: 性能优化规则
- all: 所有规则（默认）""",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "规则分类",
                        "enum": ["all", "python27_compatibility", "client_server_separation", "performance"],
                        "default": "all"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="list_modsdk_events",
            description="""列出 ModSDK 常用事件。

提供服务端和客户端事件列表，包含：
- 事件名称
- 触发时机
- 参数列表
- 是否可取消
- 重要提示""",
            inputSchema={
                "type": "object",
                "properties": {
                    "side": {
                        "type": "string",
                        "description": "事件所属端",
                        "enum": ["all", "server", "client"],
                        "default": "all"
                    }
                },
                "required": []
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """处理工具调用"""
    
    docs_reader = get_docs_reader()
    
    # 文档查询工具
    if name == "search_docs":
        query = arguments.get("query", "")
        limit = arguments.get("limit", 10)
        fuzzy = arguments.get("fuzzy", True)
        results = docs_reader.search(query, limit, fuzzy=fuzzy)
        
        if not results:
            search_mode = "模糊搜索" if fuzzy else "精确搜索"
            return [TextContent(type="text", text=f"未找到与 '{query}' 相关的文档（{search_mode}模式）。\n\n**提示**：\n- 尝试更换关键词\n- 使用英文 API 名称如 'getBlock'\n- 使用中文描述如 '玩家背包'")]
        
        search_mode = "🔍 模糊搜索" if fuzzy else "📌 精确搜索"
        output = f"## {search_mode}结果: {query}\n\n"
        output += f"找到 **{len(results)}** 个相关文档\n\n"
        
        for i, result in enumerate(results, 1):
            output += f"### {i}. {result['title']}\n"
            output += f"- 📄 文件: `{result['filepath']}`\n"
            output += f"- ⭐ 相关度: {result['score']}\n"
            
            # 显示匹配的术语（仅模糊搜索）
            if fuzzy and result.get('matched_terms'):
                matched = ', '.join(result['matched_terms'][:3])
                output += f"- 🎯 匹配: {matched}\n"
            
            output += f"- 📝 片段: {result['snippet']}\n\n"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "get_document":
        filepath = arguments.get("filepath", "")
        doc = docs_reader.get_document(filepath)
        
        if not doc:
            return [TextContent(type="text", text=f"文档 '{filepath}' 不存在。")]
        
        return [TextContent(type="text", text=f"# {doc.title}\n\n{doc.content}")]
    
    elif name == "get_document_section":
        filepath = arguments.get("filepath", "")
        section_title = arguments.get("section_title", "")
        content = docs_reader.get_section_content(filepath, section_title)
        
        if not content:
            return [TextContent(type="text", text=f"在文档 '{filepath}' 中未找到章节 '{section_title}'。")]
        
        return [TextContent(type="text", text=f"## {section_title}\n\n{content}")]
    
    elif name == "list_documents":
        docs = docs_reader.list_documents()
        
        if not docs:
            return [TextContent(type="text", text="当前没有加载任何文档。请确保 docs 目录存在且包含 Markdown 文件。")]
        
        output = "## 可用文档列表\n\n"
        for doc in docs:
            output += f"- **{doc['title']}** (`{doc['filepath']}`)\n"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "get_document_structure":
        filepath = arguments.get("filepath", "")
        structure = docs_reader.get_document_structure(filepath)
        
        if not structure:
            return [TextContent(type="text", text=f"文档 '{filepath}' 不存在。")]
        
        output = f"## 文档结构: {filepath}\n\n"
        for section in structure:
            indent = "  " * (section['level'] - 1)
            output += f"{indent}- {section['title']}\n"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "reload_documents":
        reload_docs()
        docs = docs_reader.list_documents()
        return [TextContent(type="text", text=f"文档已重新加载。当前共有 {len(docs)} 个文档。")]
    
    # 代码生成工具
    elif name == "generate_mod_project":
        files = generate_mod_project(
            mod_name=arguments.get("mod_name"),
            mod_id=arguments.get("mod_id"),
            author=arguments.get("author", "Author"),
            description=arguments.get("description", "A Minecraft mod"),
            version=arguments.get("version", "1.0.0")
        )
        
        output = "## 生成的 Mod 项目文件\n\n"
        for filename, content in files.items():
            output += f"### `{filename}`\n\n```python\n{content}\n```\n\n"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_server_system":
        code = generate_server_system(
            mod_name=arguments.get("mod_name"),
            class_name=arguments.get("class_name")
        )
        return [TextContent(type="text", text=f"## 服务端系统代码\n\n```python\n{code}\n```")]
    
    elif name == "generate_client_system":
        code = generate_client_system(
            mod_name=arguments.get("mod_name"),
            class_name=arguments.get("class_name")
        )
        return [TextContent(type="text", text=f"## 客户端系统代码\n\n```python\n{code}\n```")]
    
    elif name == "generate_event_listener":
        code = generate_event_listener(
            event_name=arguments.get("event_name"),
            event_description=arguments.get("event_description", "事件处理")
        )
        return [TextContent(type="text", text=f"## 事件监听器代码\n\n```python\n{code}\n```")]
    
    elif name == "generate_custom_command":
        code = generate_custom_command(
            command_name=arguments.get("command_name")
        )
        return [TextContent(type="text", text=f"## 自定义命令代码\n\n```python\n{code}\n```")]
    
    elif name == "generate_custom_item":
        code = generate_custom_item(
            item_id=arguments.get("item_id"),
            namespace=arguments.get("namespace", "mymod"),
            display_name=arguments.get("display_name", "自定义物品"),
            max_stack=arguments.get("max_stack", 64)
        )
        return [TextContent(type="text", text=f"## 自定义物品代码\n\n```python\n{code}\n```")]
    
    elif name == "generate_custom_block":
        code = generate_custom_block(
            block_id=arguments.get("block_id"),
            namespace=arguments.get("namespace", "mymod"),
            destroy_time=arguments.get("destroy_time", 1.0),
            explosion_resistance=arguments.get("explosion_resistance", 1.0)
        )
        return [TextContent(type="text", text=f"## 自定义方块代码\n\n```python\n{code}\n```")]
    
    # ============================================================
    # Bedrock JSON 生成工具处理
    # ============================================================
    
    elif name == "generate_item_json":
        namespace = arguments.get("namespace")
        item_id = arguments.get("item_id")
        category = arguments.get("category", "items")
        max_stack_size = arguments.get("max_stack_size", 64)
        components = arguments.get("components")
        
        result = generate_item_json(
            namespace=namespace,
            item_id=item_id,
            category=category,
            max_stack_size=max_stack_size,
            components=components
        )
        
        pack_id = namespace
        output = f"## 自定义物品 JSON: {namespace}:{item_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/netease_items_beh/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['behavior']}\n```\n\n"
        output += f"### 资源包文件: `resource_pack_{pack_id}/netease_items_res/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['resource']}\n```\n\n"
        output += f"### 本地化条目 (texts/zh_CN.lang)\n\n```\nitem.{namespace}:{item_id}.name=物品显示名称\n```"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_block_json":
        namespace = arguments.get("namespace")
        block_id = arguments.get("block_id")
        
        result = generate_block_json(
            namespace=namespace,
            block_id=block_id,
            destroy_time=arguments.get("destroy_time", 1.5),
            explosion_resistance=arguments.get("explosion_resistance", 10.0),
            light_emission=arguments.get("light_emission", 0),
            map_color=arguments.get("map_color", "#FFFFFF"),
            components=arguments.get("components")
        )
        
        pack_id = namespace
        output = f"## 自定义方块 JSON: {namespace}:{block_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/netease_blocks/{namespace}_{block_id}.json`\n\n"
        output += f"```json\n{result}\n```\n\n"
        output += f"### 本地化条目 (texts/zh_CN.lang)\n\n```\ntile.{namespace}:{block_id}.name=方块显示名称\n```"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_recipe_json":
        recipe_type = arguments.get("recipe_type")
        namespace = arguments.get("namespace")
        recipe_id = arguments.get("recipe_id")
        
        if recipe_type == "shaped":
            result = generate_recipe_json(
                recipe_type="shaped",
                namespace=namespace,
                recipe_id=recipe_id,
                pattern=arguments.get("pattern", ["   ", "   ", "   "]),
                keys=arguments.get("keys", {}),
                result_item=arguments.get("result_item", "minecraft:air"),
                result_count=arguments.get("result_count", 1)
            )
        elif recipe_type == "shapeless":
            result = generate_recipe_json(
                recipe_type="shapeless",
                namespace=namespace,
                recipe_id=recipe_id,
                ingredients=arguments.get("ingredients", []),
                result_item=arguments.get("result_item", "minecraft:air"),
                result_count=arguments.get("result_count", 1)
            )
        elif recipe_type == "furnace":
            result = generate_recipe_json(
                recipe_type="furnace",
                namespace=namespace,
                recipe_id=recipe_id,
                input_item=arguments.get("input_item", "minecraft:air"),
                output_item=arguments.get("output_item", "minecraft:air")
            )
        else:
            return [TextContent(type="text", text=f"未知的配方类型: {recipe_type}")]
        
        pack_id = namespace
        output = f"## {recipe_type.capitalize()} 配方 JSON: {namespace}:{recipe_id}\n\n"
        output += f"### 文件: `behavior_pack_{pack_id}/netease_recipes/{recipe_id}.json`\n\n"
        output += f"```json\n{result}\n```"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_entity_json":
        namespace = arguments.get("namespace")
        entity_id = arguments.get("entity_id")
        
        result = generate_entity_json(
            namespace=namespace,
            entity_id=entity_id,
            health=arguments.get("health", 20),
            movement_speed=arguments.get("movement_speed", 0.25),
            collision_width=arguments.get("collision_width", 0.6),
            collision_height=arguments.get("collision_height", 1.8),
            runtime_identifier=arguments.get("runtime_identifier"),
            spawn_egg_base_color=arguments.get("spawn_egg_base_color", "#FFFFFF"),
            spawn_egg_overlay_color=arguments.get("spawn_egg_overlay_color", "#000000")
        )
        
        pack_id = namespace
        output = f"## 自定义实体 JSON: {namespace}:{entity_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/entities/{namespace}_{entity_id}.json`\n\n"
        output += f"```json\n{result['behavior']}\n```\n\n"
        output += f"### 资源包文件: `resource_pack_{pack_id}/entity/{namespace}_{entity_id}.entity.json`\n\n"
        output += f"```json\n{result['resource']}\n```\n\n"
        output += f"### 本地化条目 (texts/zh_CN.lang)\n\n```\nentity.{namespace}:{entity_id}.name=实体显示名称\n```"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_loot_table_json":
        pools = arguments.get("pools", [])
        
        result = generate_loot_table_json(pools)
        
        output = "## 战利品表 JSON\n\n"
        output += "### 文件: `behavior_pack_<ID>/loot_tables/xxx.json`\n\n"
        output += f"```json\n{result}\n```"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_spawn_rules_json":
        namespace = arguments.get("namespace")
        entity_id = arguments.get("entity_id")
        
        result = generate_spawn_rules_json(
            namespace=namespace,
            entity_id=entity_id,
            population_control=arguments.get("population_control", "animal"),
            spawn_weight=arguments.get("spawn_weight", 8),
            min_size=arguments.get("min_size", 2),
            max_size=arguments.get("max_size", 4)
        )
        
        pack_id = namespace
        output = f"## 生成规则 JSON: {namespace}:{entity_id}\n\n"
        output += f"### 文件: `behavior_pack_{pack_id}/spawn_rules/{namespace}_{entity_id}.json`\n\n"
        output += f"```json\n{result}\n```"
        
        return [TextContent(type="text", text=output)]
    
    # ============================================================
    # 高级物品生成工具处理
    # ============================================================
    
    elif name == "generate_sword_json":
        namespace = arguments.get("namespace")
        item_id = arguments.get("item_id")
        result = generate_sword_item_json(
            namespace=namespace,
            item_id=item_id,
            damage=arguments.get("damage", 5),
            durability=arguments.get("durability", 131),
            enchantability=arguments.get("enchantability", 15),
            repair_material=arguments.get("repair_material")
        )
        pack_id = namespace
        output = f"## ⚔️ 自定义剑类武器: {namespace}:{item_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/netease_items_beh/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['behavior']}\n```\n\n"
        output += f"### 资源包文件: `resource_pack_{pack_id}/netease_items_res/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['resource']}\n```\n\n"
        output += f"### 📝 本地化条目 (texts/zh_CN.lang)\n\n```\nitem.{namespace}:{item_id}.name=自定义剑\n```"
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_pickaxe_json":
        namespace = arguments.get("namespace")
        item_id = arguments.get("item_id")
        result = generate_pickaxe_item_json(
            namespace=namespace,
            item_id=item_id,
            durability=arguments.get("durability", 131),
            mining_speed=arguments.get("mining_speed", 4),
            enchantability=arguments.get("enchantability", 15),
            repair_material=arguments.get("repair_material")
        )
        pack_id = namespace
        output = f"## ⛏️ 自定义镐类工具: {namespace}:{item_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/netease_items_beh/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['behavior']}\n```\n\n"
        output += f"### 资源包文件: `resource_pack_{pack_id}/netease_items_res/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['resource']}\n```\n\n"
        output += f"### 📝 本地化条目 (texts/zh_CN.lang)\n\n```\nitem.{namespace}:{item_id}.name=自定义镐\n```"
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_axe_json":
        namespace = arguments.get("namespace")
        item_id = arguments.get("item_id")
        result = generate_axe_item_json(
            namespace=namespace,
            item_id=item_id,
            damage=arguments.get("damage", 4),
            durability=arguments.get("durability", 131),
            mining_speed=arguments.get("mining_speed", 4),
            enchantability=arguments.get("enchantability", 15),
            repair_material=arguments.get("repair_material")
        )
        pack_id = namespace
        output = f"## 🪓 自定义斧类工具: {namespace}:{item_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/netease_items_beh/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['behavior']}\n```\n\n"
        output += f"### 资源包文件: `resource_pack_{pack_id}/netease_items_res/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['resource']}\n```\n\n"
        output += f"### 📝 本地化条目 (texts/zh_CN.lang)\n\n```\nitem.{namespace}:{item_id}.name=自定义斧\n```"
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_shovel_json":
        namespace = arguments.get("namespace")
        item_id = arguments.get("item_id")
        result = generate_shovel_item_json(
            namespace=namespace,
            item_id=item_id,
            durability=arguments.get("durability", 131),
            mining_speed=arguments.get("mining_speed", 4),
            enchantability=arguments.get("enchantability", 15),
            repair_material=arguments.get("repair_material")
        )
        pack_id = namespace
        output = f"## 🥄 自定义锹类工具: {namespace}:{item_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/netease_items_beh/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['behavior']}\n```\n\n"
        output += f"### 资源包文件: `resource_pack_{pack_id}/netease_items_res/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['resource']}\n```\n\n"
        output += f"### 📝 本地化条目 (texts/zh_CN.lang)\n\n```\nitem.{namespace}:{item_id}.name=自定义锹\n```"
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_hoe_json":
        namespace = arguments.get("namespace")
        item_id = arguments.get("item_id")
        result = generate_hoe_item_json(
            namespace=namespace,
            item_id=item_id,
            durability=arguments.get("durability", 131),
            enchantability=arguments.get("enchantability", 15),
            repair_material=arguments.get("repair_material")
        )
        pack_id = namespace
        output = f"## 🌾 自定义锄类工具: {namespace}:{item_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/netease_items_beh/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['behavior']}\n```\n\n"
        output += f"### 资源包文件: `resource_pack_{pack_id}/netease_items_res/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['resource']}\n```\n\n"
        output += f"### 📝 本地化条目 (texts/zh_CN.lang)\n\n```\nitem.{namespace}:{item_id}.name=自定义锄\n```"
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_food_json":
        namespace = arguments.get("namespace")
        item_id = arguments.get("item_id")
        result = generate_food_item_json(
            namespace=namespace,
            item_id=item_id,
            nutrition=arguments.get("nutrition", 4),
            saturation=arguments.get("saturation", "normal"),
            can_always_eat=arguments.get("can_always_eat", False),
            effects=arguments.get("effects")
        )
        pack_id = namespace
        output = f"## 🍎 自定义食物: {namespace}:{item_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/netease_items_beh/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['behavior']}\n```\n\n"
        output += f"### 资源包文件: `resource_pack_{pack_id}/netease_items_res/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['resource']}\n```\n\n"
        output += f"### 📝 本地化条目 (texts/zh_CN.lang)\n\n```\nitem.{namespace}:{item_id}.name=自定义食物\n```"
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_armor_json":
        namespace = arguments.get("namespace")
        item_id = arguments.get("item_id")
        result = generate_armor_item_json(
            namespace=namespace,
            item_id=item_id,
            slot=arguments.get("slot", "slot.armor.chest"),
            protection=arguments.get("protection", 5),
            durability=arguments.get("durability", 165),
            enchantability=arguments.get("enchantability", 9),
            repair_material=arguments.get("repair_material")
        )
        slot_name_map = {
            "slot.armor.head": "头盔",
            "slot.armor.chest": "胸甲",
            "slot.armor.legs": "护腿",
            "slot.armor.feet": "靴子"
        }
        slot_name = slot_name_map.get(arguments.get("slot", "slot.armor.chest"), "盔甲")
        pack_id = namespace
        output = f"## 🛡️ 自定义{slot_name}: {namespace}:{item_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/netease_items_beh/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['behavior']}\n```\n\n"
        output += f"### 资源包文件: `resource_pack_{pack_id}/netease_items_res/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['resource']}\n```\n\n"
        output += f"### 📝 本地化条目 (texts/zh_CN.lang)\n\n```\nitem.{namespace}:{item_id}.name=自定义{slot_name}\n```"
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_bow_json":
        namespace = arguments.get("namespace")
        item_id = arguments.get("item_id")
        result = generate_bow_item_json(
            namespace=namespace,
            item_id=item_id,
            durability=arguments.get("durability", 384),
            max_draw_duration=arguments.get("max_draw_duration", 1.0),
            enchantability=arguments.get("enchantability", 1)
        )
        pack_id = namespace
        output = f"## 🏹 自定义弓: {namespace}:{item_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/netease_items_beh/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['behavior']}\n```\n\n"
        output += f"### 资源包文件: `resource_pack_{pack_id}/netease_items_res/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['resource']}\n```\n\n"
        output += f"### 📝 本地化条目 (texts/zh_CN.lang)\n\n```\nitem.{namespace}:{item_id}.name=自定义弓\n```"
        return [TextContent(type="text", text=output)]
    
    elif name == "generate_throwable_json":
        namespace = arguments.get("namespace")
        item_id = arguments.get("item_id")
        projectile_entity = arguments.get("projectile_entity")
        result = generate_throwable_item_json(
            namespace=namespace,
            item_id=item_id,
            projectile_entity=projectile_entity,
            max_draw_duration=arguments.get("max_draw_duration", 0.0),
            launch_power=arguments.get("launch_power", 1.0)
        )
        pack_id = namespace
        output = f"## 🎯 自定义投掷物: {namespace}:{item_id}\n\n"
        output += f"### 行为包文件: `behavior_pack_{pack_id}/netease_items_beh/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['behavior']}\n```\n\n"
        output += f"### 资源包文件: `resource_pack_{pack_id}/netease_items_res/{namespace}_{item_id}.json`\n\n"
        output += f"```json\n{result['resource']}\n```\n\n"
        output += f"### 📝 本地化条目 (texts/zh_CN.lang)\n\n```\nitem.{namespace}:{item_id}.name=自定义投掷物\n```"
        return [TextContent(type="text", text=output)]
    
    # 代码审查工具
    elif name == "review_code":
        code = arguments.get("code", "")
        filename = arguments.get("filename", "unknown.py")
        review_result = _perform_code_review(code, filename)
        return [TextContent(type="text", text=review_result)]
    
    # ============================================================
    # 知识库查询工具处理
    # ============================================================
    
    elif name == "search_components":
        query = arguments.get("query", "")
        component_type = arguments.get("component_type", "all")
        results = search_component(query, component_type)
        
        if not results:
            return [TextContent(type="text", text=f"未找到与 '{query}' 相关的组件。\n\n**提示**：\n- 尝试使用英文名如 'food', 'durability'\n- 尝试使用中文描述如 '食物', '耐久'")]
        
        output = f"## 🔍 组件搜索结果: {query}\n\n"
        output += f"找到 **{len(results)}** 个相关组件\n\n"
        
        for result in results:
            output += f"### `{result['id']}`\n"
            output += f"- **名称**: {result.get('name', '未知')}\n"
            output += f"- **类型**: {result['type']}\n"
            output += f"- **描述**: {result.get('description', '无描述')}\n"
            if result.get('properties'):
                output += f"- **属性**: {result['properties']}\n"
            output += "\n"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "get_component_details":
        component_id = arguments.get("component_id", "")
        result = get_component_info(component_id)
        
        if not result:
            return [TextContent(type="text", text=f"未找到组件 '{component_id}'。\n\n**提示**：使用 search_components 工具搜索可用组件。")]
        
        output = f"## 📦 组件详情: `{result['id']}`\n\n"
        output += f"- **名称**: {result.get('name', '未知')}\n"
        output += f"- **类型**: {result.get('type', '未知')}\n"
        output += f"- **描述**: {result.get('description', '无描述')}\n"
        
        if result.get('properties'):
            output += f"\n### 属性\n"
            for prop, desc in result['properties'].items():
                output += f"- `{prop}`: {desc}\n"
        
        if result.get('values'):
            output += f"\n### 可选值\n"
            for value in result['values']:
                output += f"- `{value}`\n"
        
        if result.get('example'):
            output += f"\n### 示例\n"
            output += f"```json\n\"{result['id']}\": {result['example']}\n```\n"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "list_components":
        component_type = arguments.get("component_type", "all")
        output = "## 📋 组件列表\n\n"
        
        components_map = {
            "item": ("物品组件", ITEM_COMPONENTS),
            "block": ("方块组件", BLOCK_COMPONENTS),
            "entity": ("实体组件", ENTITY_COMPONENTS),
            "netease_item": ("网易物品组件", NETEASE_ITEM_COMPONENTS),
            "netease_block": ("网易方块组件", NETEASE_BLOCK_COMPONENTS),
        }
        
        if component_type == "all":
            types_to_show = list(components_map.keys())
        else:
            types_to_show = [component_type]
        
        for ctype in types_to_show:
            if ctype in components_map:
                name_cn, components = components_map[ctype]
                output += f"### {name_cn} ({len(components)} 个)\n\n"
                for comp_id, comp_data in components.items():
                    output += f"- `{comp_id}` - {comp_data.get('name', '未知')}\n"
                output += "\n"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "get_best_practices":
        category = arguments.get("category", "all")
        practices = get_best_practices(category)
        
        if not practices:
            return [TextContent(type="text", text=f"未找到分类 '{category}' 的最佳实践。")]
        
        output = "## 📚 ModSDK 最佳实践\n\n"
        
        if category != "all":
            practices = {category: practices}
        
        for cat_id, cat_data in practices.items():
            output += f"### {cat_data.get('name', cat_id)}\n\n"
            for rule in cat_data.get('rules', []):
                output += f"- {rule}\n"
            output += "\n"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "list_modsdk_events":
        side = arguments.get("side", "all")
        output = "## 📋 ModSDK 事件列表\n\n"
        
        for event_name, event_data in MODSDK_EVENTS.items():
            if side != "all" and event_data.get("side") != side:
                continue
            
            output += f"### `{event_name}`\n"
            output += f"- **端**: {event_data.get('side', 'unknown')}\n"
            output += f"- **描述**: {event_data.get('description', '无描述')}\n"
            
            if event_data.get('args'):
                output += f"- **参数**: {', '.join(event_data['args'])}\n"
            
            output += f"- **可取消**: {'是' if event_data.get('cancel') else '否'}\n"
            
            if event_data.get('important'):
                output += f"- **⚠️ 重要**: {event_data['important']}\n"
            
            output += "\n"
        
        return [TextContent(type="text", text=output)]
    
    else:
        return [TextContent(type="text", text=f"未知的工具: {name}")]


def _perform_code_review(code: str, filename: str) -> str:
    """执行代码审查，返回审查报告"""
    import re
    
    issues = {
        "critical": [],
        "warning": [],
        "suggestion": []
    }
    
    lines = code.split('\n')
    
    # 判断是否是 ServerSystem 文件（更精确的检测）
    # 只通过类继承或主要 import 来判断
    is_server_system = 'ServerSystem' in code or 'import mod.server.' in code
    is_client_system = 'ClientSystem' in code or 'import mod.client.' in code
    
    # 如果同时检测到两种系统，优先根据类定义判断
    if is_server_system and is_client_system:
        # 检查实际的类定义
        if 'class ' in code and 'ServerSystem' in code and 'ClientSystem' not in code:
            is_client_system = False
        elif 'class ' in code and 'ClientSystem' in code and 'ServerSystem' not in code:
            is_server_system = False
    
    # 检查是否有 from __future__ import print_function
    has_print_function_import = 'from __future__ import print_function' in code
    
    for i, line in enumerate(lines, 1):
        line_stripped = line.strip()
        
        # 跳过注释行
        if line_stripped.startswith('#'):
            continue
        
        # 🔴 严重问题检查
        
        # ========================================
        # Python 2.7 兼容性检查（最重要）
        # ========================================
        
        # 1. f-string 检测 (Python 3.6+)
        if re.search(r'\bf["\']', line):
            issues["critical"].append({
                "line": i,
                "issue": "使用 f-string（Python 3.6+ 语法，ModSDK 不支持）",
                "code": line_stripped,
                "fix": '使用 "{}".format() 或 % 格式化。例如: "Hello {}".format(name) 或 "Hello %s" % name'
            })
        
        # 2. print() 函数检测（应使用 print 语句）
        # 如果文件顶部有 from __future__ import print_function，则允许使用 print()
        # 检测 print(...) 但不是 print = 或 def print 或 .print(
        if not has_print_function_import:
            if re.search(r'(?<![.\w])print\s*\(', line) and 'from __future__' not in line:
                issues["critical"].append({
                    "line": i,
                    "issue": "使用 print() 函数（Python 3 语法）",
                    "code": line_stripped,
                    "fix": '使用 print 语句：print "message" 或在文件顶部添加 from __future__ import print_function'
                })
        
        # 3. Type hints 检测 (Python 3.5+)
        # 检测函数参数类型注解 def func(x: int)
        if re.search(r'def \w+\([^)]*:\s*\w+', line):
            issues["critical"].append({
                "line": i,
                "issue": "使用类型注解（Python 3.5+ 语法，ModSDK 不支持）",
                "code": line_stripped,
                "fix": "移除类型注解。例如: def func(x: int) -> str 改为 def func(x)"
            })
        
        # 检测变量类型注解 x: int = 1
        if re.search(r'^\s*\w+\s*:\s*\w+\s*=', line):
            issues["critical"].append({
                "line": i,
                "issue": "使用变量类型注解（Python 3.6+ 语法）",
                "code": line_stripped,
                "fix": "移除类型注解。例如: x: int = 1 改为 x = 1"
            })
        
        # 检测返回值类型注解 -> 
        if re.search(r'def \w+\([^)]*\)\s*->', line):
            issues["critical"].append({
                "line": i,
                "issue": "使用返回值类型注解（Python 3.5+ 语法）",
                "code": line_stripped,
                "fix": "移除返回值类型注解 -> Type"
            })
        
        # 4. async/await 检测 (Python 3.5+)
        if re.search(r'\basync\s+def\b', line):
            issues["critical"].append({
                "line": i,
                "issue": "使用 async def（Python 3.5+ 语法，ModSDK 不支持）",
                "code": line_stripped,
                "fix": "ModSDK 不支持异步编程，请使用同步代码"
            })
        
        if re.search(r'\bawait\s+', line):
            issues["critical"].append({
                "line": i,
                "issue": "使用 await（Python 3.5+ 语法，ModSDK 不支持）",
                "code": line_stripped,
                "fix": "ModSDK 不支持异步编程，请使用同步代码"
            })
        
        # 5. 字典/集合推导式中的 walrus 运算符 := (Python 3.8+)
        if ':=' in line:
            issues["critical"].append({
                "line": i,
                "issue": "使用海象运算符 :=（Python 3.8+ 语法）",
                "code": line_stripped,
                "fix": "将赋值和条件分开写"
            })
        
        # ========================================
        # 架构规范检查
        # ========================================
        
        # 6. 客户端/服务端混用
        # ServerSystem 中不能导入 clientApi
        if is_server_system and 'clientApi' in line and 'import' in line and not line_stripped.startswith('#'):
            issues["critical"].append({
                "line": i,
                "issue": "ServerSystem 中导入 clientApi",
                "code": line_stripped,
                "fix": "使用 NotifyToClient() 事件通信代替直接调用客户端 API"
            })
        
        # ClientSystem 中不能导入 serverApi
        if is_client_system and 'serverApi' in line and 'import' in line and not line_stripped.startswith('#'):
            issues["critical"].append({
                "line": i,
                "issue": "ClientSystem 中导入 serverApi",
                "code": line_stripped,
                "fix": "使用 NotifyToServer() 事件通信代替直接调用服务端 API"
            })
        
        # 2. GetEngineCompFactory 未缓存（在 def 内调用）
        # 排除注释行
        if 'GetEngineCompFactory()' in line and not line_stripped.startswith('#'):
            # 检查是否在函数内部（有缩进）
            indent = len(line) - len(line.lstrip())
            if indent >= 4:  # 缩进说明在函数内
                issues["critical"].append({
                    "line": i,
                    "issue": "GetEngineCompFactory 在函数内调用（未缓存）",
                    "code": line_stripped,
                    "fix": "在文件顶部添加 CF = serverApi.GetEngineCompFactory()，然后使用 CF.CreateXxx()"
                })
        
        # 3. 函数内 import
        if line_stripped.startswith('import ') or line_stripped.startswith('from '):
            indent = len(line) - len(line.lstrip())
            if indent >= 4:  # 缩进说明在函数内
                issues["critical"].append({
                    "line": i,
                    "issue": "函数内 import",
                    "code": line_stripped,
                    "fix": "将 import 语句移到文件顶部"
                })
        
        # 4. Tick 事件无降帧检查（需要上下文分析）
        if 'def OnTickServer' in line or 'def OnTickClient' in line:
            # 检查后续行是否有 tick % 
            has_frame_skip = False
            for j in range(i, min(i + 20, len(lines))):
                if 'tick %' in lines[j] or 'tick%' in lines[j]:
                    has_frame_skip = True
                    break
                if j > i and lines[j].strip().startswith('def '):
                    break
            
            if not has_frame_skip:
                issues["warning"].append({
                    "line": i,
                    "issue": "Tick 事件可能缺少降帧逻辑",
                    "code": line_stripped,
                    "fix": "添加 if self.tick % 7 == 0: 来降低执行频率"
                })
        
        # 🟠 警告问题检查
        
        # 5. BroadcastToAllClient 滥用
        if 'BroadcastToAllClient' in line:
            issues["warning"].append({
                "line": i,
                "issue": "使用 BroadcastToAllClient 广播",
                "code": line_stripped,
                "fix": "评估是否可以使用 NotifyToClient 进行点对点通信"
            })
        
        # 6. ServerBlockEntityTickEvent 无加盐（检查处理函数）
        if 'ServerBlockEntityTickEvent' in line or 'OnBlockEntityTick' in line.replace(' ', ''):
            # 检查后续是否有 salt 计算
            has_salt = False
            for j in range(i, min(i + 15, len(lines))):
                if 'salt' in lines[j].lower() or ('posX' in lines[j] and '%' in lines[j]):
                    has_salt = True
                    break
                if j > i and lines[j].strip().startswith('def '):
                    break
            
            if not has_salt:
                issues["warning"].append({
                    "line": i,
                    "issue": "ServerBlockEntityTickEvent 可能缺少加盐处理",
                    "code": line_stripped,
                    "fix": "使用 salt = (x * 31 + y * 17 + z * 13) % N 错开执行时机"
                })
        
        # 7. 循环内创建组件
        if re.search(r'for .+ in .+:', line_stripped):
            # 检查循环体内是否有 Create
            for j in range(i, min(i + 10, len(lines))):
                if j > i and 'Create' in lines[j] and 'CF.' in lines[j]:
                    issues["warning"].append({
                        "line": j + 1,
                        "issue": "循环内创建组件",
                        "code": lines[j].strip(),
                        "fix": "考虑缓存组件或在循环外创建"
                    })
                    break
                if j > i and not lines[j].startswith(' ' * 4):
                    break
        
        # 8. 字符串拼接
        if '+=' in line and ('str' in line.lower() or '"' in line or "'" in line):
            if 'for ' in '\n'.join(lines[max(0, i-5):i]):  # 检查是否在循环内
                issues["warning"].append({
                    "line": i,
                    "issue": "循环内字符串拼接",
                    "code": line_stripped,
                    "fix": "使用列表收集后 ''.join() 拼接"
                })
        
        # 🟡 建议优化检查
        
        # 9. 魔法数字
        magic_number_match = re.search(r'[=<>!]=?\s*(\d{2,})', line)
        if magic_number_match and not any(kw in line for kw in ['line', 'range', 'len', 'tick', '%']):
            number = magic_number_match.group(1)
            issues["suggestion"].append({
                "line": i,
                "issue": f"魔法数字 {number}",
                "code": line_stripped,
                "fix": "考虑定义为常量"
            })
        
        # 10. 缺少错误处理
        if '[' in line and ']' in line and '=' in line:
            if not any(kw in line for kw in ['.get(', 'if ', 'try', 'range']):
                if re.search(r'\[[\'"]\w+[\'"]\]', line) or re.search(r'\[\w+\]', line):
                    issues["suggestion"].append({
                        "line": i,
                        "issue": "直接字典/列表访问可能引发 KeyError",
                        "code": line_stripped,
                        "fix": "使用 .get() 方法或添加 try-except"
                    })
        
        # 11. 事件命名
        if 'NotifyToClient' in line or 'NotifyToServer' in line or 'BroadcastEvent' in line:
            event_match = re.search(r'["\']([a-z][a-z0-9]*)["\']', line, re.I)
            if event_match:
                event_name = event_match.group(1)
                if len(event_name) < 4 or event_name.lower() == event_name:
                    issues["suggestion"].append({
                        "line": i,
                        "issue": f"事件名 '{event_name}' 可能不够描述性",
                        "code": line_stripped,
                        "fix": "使用 PascalCase 描述性命名，如 'PlayerInventoryUpdated'"
                    })
    
    # 生成报告
    output = f"# 代码审查报告: {filename}\n\n"
    
    total_critical = len(issues["critical"])
    total_warning = len(issues["warning"])
    total_suggestion = len(issues["suggestion"])
    
    output += "## 📊 统计\n\n"
    output += f"- 🔴 严重问题：{total_critical} 个\n"
    output += f"- 🟠 警告问题：{total_warning} 个\n"
    output += f"- 🟡 优化建议：{total_suggestion} 个\n\n"
    
    if total_critical == 0 and total_warning == 0:
        output += "✅ **整体评价**：代码质量良好，未发现严重问题！\n\n"
    elif total_critical > 0:
        output += "⚠️ **整体评价**：发现严重问题，建议立即修复！\n\n"
    else:
        output += "📝 **整体评价**：代码基本合格，建议优化警告项。\n\n"
    
    # 输出详细问题
    if issues["critical"]:
        output += "---\n\n## 🔴 严重问题（必须修复）\n\n"
        for issue in issues["critical"]:
            output += f"### 行 {issue['line']}: {issue['issue']}\n\n"
            output += f"**问题代码**:\n```python\n{issue['code']}\n```\n\n"
            output += f"**修复建议**: {issue['fix']}\n\n"
    
    if issues["warning"]:
        output += "---\n\n## 🟠 警告问题（建议修复）\n\n"
        for issue in issues["warning"]:
            output += f"### 行 {issue['line']}: {issue['issue']}\n\n"
            output += f"**问题代码**:\n```python\n{issue['code']}\n```\n\n"
            output += f"**修复建议**: {issue['fix']}\n\n"
    
    if issues["suggestion"]:
        output += "---\n\n## 🟡 优化建议（可选）\n\n"
        for issue in issues["suggestion"]:
            output += f"### 行 {issue['line']}: {issue['issue']}\n\n"
            output += f"**代码**:\n```python\n{issue['code']}\n```\n\n"
            output += f"**建议**: {issue['fix']}\n\n"
    
    return output


# ============================================================================
# 提示词定义
# ============================================================================

@server.list_prompts()
async def list_prompts() -> List[Prompt]:
    """列出所有可用的提示词"""
    return [
        Prompt(
            name="modsdk_expert",
            description="我的世界中国版 ModSDK 开发专家模式。提供专业的 Mod 开发指导。",
            arguments=[]
        ),
        Prompt(
            name="create_mod",
            description="引导创建一个新的 Mod 项目。",
            arguments=[
                PromptArgument(
                    name="mod_name",
                    description="Mod 名称",
                    required=True
                ),
                PromptArgument(
                    name="mod_description",
                    description="Mod 功能描述",
                    required=True
                )
            ]
        ),
        Prompt(
            name="debug_help",
            description="帮助调试 Mod 代码问题。",
            arguments=[
                PromptArgument(
                    name="error_message",
                    description="错误信息",
                    required=True
                )
            ]
        ),
        Prompt(
            name="code_review",
            description="对 ModSDK 代码进行专业审查，检测性能问题和架构违规。",
            arguments=[
                PromptArgument(
                    name="code",
                    description="要审查的代码",
                    required=True
                )
            ]
        )
    ]


@server.get_prompt()
async def get_prompt(name: str, arguments: Optional[Dict[str, str]]) -> GetPromptResult:
    """获取提示词内容"""
    
    if name == "modsdk_expert":
        return GetPromptResult(
            messages=[
                PromptMessage(
                    role="user",
                    content=TextContent(
                        type="text",
                        text="""你现在是一位我的世界中国版（网易我的世界）ModSDK 开发专家。你精通：

1. **Python ModSDK API**
   - 服务端 API (mod.server.extraServerApi)
   - 客户端 API (mod.client.extraClientApi)
   - 组件系统 (GetEngineCompFactory)

2. **事件系统**
   - 服务端事件监听与处理
   - 客户端事件监听与处理
   - 自定义事件的创建与触发

3. **游戏机制**
   - 方块操作、实体操作、玩家系统
   - 背包管理、物品系统
   - 世界操作、命令系统

4. **最佳实践**
   - Mod 项目结构
   - 代码组织与模块化
   - 性能优化
   - 调试技巧

请根据用户的问题，提供专业、准确的技术指导。在回答时：
- 使用 search_docs 工具查找相关文档
- 使用代码生成工具提供示例代码
- 解释代码的工作原理
- 提供最佳实践建议"""
                    )
                )
            ]
        )
    
    elif name == "create_mod":
        mod_name = arguments.get("mod_name", "MyMod") if arguments else "MyMod"
        mod_description = arguments.get("mod_description", "一个新的 Mod") if arguments else "一个新的 Mod"
        
        return GetPromptResult(
            messages=[
                PromptMessage(
                    role="user",
                    content=TextContent(
                        type="text",
                        text=f"""请帮我创建一个新的我的世界中国版 Mod：

**Mod 名称**: {mod_name}
**功能描述**: {mod_description}

请：
1. 使用 generate_mod_project 工具生成项目结构
2. 根据功能需求，解释需要监听哪些事件
3. 提供实现功能的具体代码
4. 说明如何测试和部署这个 Mod"""
                    )
                )
            ]
        )
    
    elif name == "debug_help":
        error_message = arguments.get("error_message", "") if arguments else ""
        
        return GetPromptResult(
            messages=[
                PromptMessage(
                    role="user",
                    content=TextContent(
                        type="text",
                        text=f"""我的 Mod 遇到了问题，请帮我调试：

**错误信息**:
```
{error_message}
```

请：
1. 分析错误原因
2. 搜索相关文档了解正确用法
3. 提供修复方案
4. 解释如何避免类似问题"""
                    )
                )
            ]
        )
    
    elif name == "code_review":
        code = arguments.get("code", "") if arguments else ""
        
        return GetPromptResult(
            messages=[
                PromptMessage(
                    role="user",
                    content=TextContent(
                        type="text",
                        text=f"""请对以下 NetEase ModSDK 代码进行专业审查：

```python
{code}
```

请使用 review_code 工具进行自动检测，并提供：

1. **审查报告**
   - 🔴 严重问题（必须修复）
   - 🟠 警告问题（建议修复）
   - 🟡 优化建议（可选）

2. **详细说明**
   - 每个问题的具体位置和原因
   - 不修复会带来的影响
   - 具体的修复代码

3. **整体评价**
   - 代码质量评分
   - 改进方向建议"""
                    )
                )
            ]
        )
    
    else:
        raise ValueError(f"未知的提示词: {name}")


# ============================================================================
# 主函数
# ============================================================================

async def main_stdio():
    """使用 stdio 模式运行（本地部署）"""
    # 初始化文档读取器
    get_docs_reader()
    
    # 启动 stdio 服务器
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


async def main_sse(host: str = "0.0.0.0", port: int = 8000):
    """使用 SSE 模式运行（远程部署）"""
    from mcp.server.sse import SseServerTransport
    from starlette.applications import Starlette
    from starlette.routing import Route
    from starlette.responses import JSONResponse
    import uvicorn
    
    # 初始化文档读取器
    get_docs_reader()
    
    # 创建 SSE transport
    sse = SseServerTransport("/messages")
    
    async def handle_sse(request):
        async with sse.connect_sse(
            request.scope, request.receive, request._send
        ) as streams:
            await server.run(
                streams[0],
                streams[1],
                server.create_initialization_options()
            )
    
    async def handle_messages(request):
        await sse.handle_post_message(request.scope, request.receive, request._send)
    
    async def health_check(request):
        return JSONResponse({"status": "ok", "server": "netease-modsdk-mcp"})
    
    app = Starlette(
        debug=True,
        routes=[
            Route("/sse", endpoint=handle_sse),
            Route("/messages", endpoint=handle_messages, methods=["POST"]),
            Route("/health", endpoint=health_check),
        ],
    )
    
    print(f"🚀 MCP Server (SSE) 启动在 http://{host}:{port}")
    print(f"   - SSE 端点: http://{host}:{port}/sse")
    print(f"   - 消息端点: http://{host}:{port}/messages")
    print(f"   - 健康检查: http://{host}:{port}/health")
    
    config = uvicorn.Config(app, host=host, port=port, log_level="info")
    server_instance = uvicorn.Server(config)
    await server_instance.serve()


def run():
    """运行入口（默认 stdio 模式）"""
    asyncio.run(main_stdio())


def run_sse():
    """运行入口（SSE 模式）"""
    import os
    host = os.environ.get("MCP_HOST", "0.0.0.0")
    port = int(os.environ.get("MCP_PORT", "8000"))
    asyncio.run(main_sse(host, port))


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--sse":
        # SSE 模式：python -m modsdk_mcp.server --sse
        run_sse()
    else:
        # 默认 stdio 模式
        run()
