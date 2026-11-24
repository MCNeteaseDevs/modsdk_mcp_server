"""
我的世界中国版 ModSDK MCP Server
提供 API 文档查询、代码生成、事件系统查询等功能
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    GetPromptResult,
    PromptMessage,
    Prompt,
    PromptArgument,
    Resource,
)
from .docs_reader import get_docs_reader, reload_docs
from .knowledge_base import (
    ITEM_COMPONENTS,
    BLOCK_COMPONENTS,
    ENTITY_COMPONENTS,
    NETEASE_ITEM_COMPONENTS,
    NETEASE_BLOCK_COMPONENTS,
    search_component,
    get_component_info,
    get_best_practices,
    get_architecture_pattern,
    get_architecture_pattern_artifacts,
)
from .templates import (
    ARMOR_SLOT_SPECS,
    generate_block_json,
    generate_client_system,
    generate_custom_block,
    generate_custom_command,
    generate_custom_item,
    generate_entity_json,
    generate_event_listener,
    generate_item_json,
    generate_loot_table_json,
    generate_manifest_json,
    generate_mod_project,
    generate_recipe_json,
    generate_server_system,
    generate_spawn_rules_json,
    generate_typed_item_json,
    generate_ui_json,
    get_project_folder_name,
    render_bundle_markdown,
)
from .validation import CURRENT_TARGET_VERSION, Artifact, ValidationReport, get_registered_detectors, validate_artifacts
from .standards import get_version_profile


_TARGET_PROFILE = get_version_profile()
MODSDK_LABEL = "ModSDK {} / BE {}".format(_TARGET_PROFILE["version"], _TARGET_PROFILE["bedrock_version"])


# 创建 MCP Server 实例
server = Server(
    "minecraft-modsdk",
    instructions=f"""你是网易《我的世界》{MODSDK_LABEL} 开发助手，当前官方版本状态为 {_TARGET_PROFILE["status"]}。

固定工作流：
1. 先调用 get_development_guidance 获取与目标、端侧和产物匹配的规则。
2. 涉及 API 或事件时，用 search_api/get_api_detail 查证名称、端侧、参数和备注；需要正文时再用 search_docs/get_document_section。
3. 生成产物后读取随附校验报告；critical 必须修复后再输出，warning 说明证据边界和人工验证项。

运行时只使用仓库内快照。{_TARGET_PROFILE["source_boundary"]}。不得猜测 API 签名或把工程经验表述为官方硬规则。历史版本指导不切换当前 API 快照；版本迁移差异见 get_version_changes。"""
)

# Bedrock Wiki 路径（相对于项目根目录）
_PROJECT_ROOT = Path(__file__).parent.parent
BEDROCK_WIKI_PATH = Path(os.environ.get("MODSDK_BEDROCK_WIKI_PATH", str(_PROJECT_ROOT / "bedrock-wiki-wiki")))
# Bedrock Wiki 最大支持版本（网易版兼容上限）
BEDROCK_WIKI_MAX_VERSION = _TARGET_PROFILE["bedrock_version"]


# ============================================================================
# Bedrock Wiki 读取器
# ============================================================================

class BedrockWikiReader:
    """读取 bedrock-wiki-wiki/docs/ 下的 Markdown 文档，过滤版本 > MAX_VERSION 的内容"""
    
    def __init__(self, wiki_path, max_version=None):
        self.wiki_path = Path(wiki_path) / "docs"
        self.max_version = max_version or BEDROCK_WIKI_MAX_VERSION
        self._topics = {}  # topic_key -> {name, files: [{path, content}]}
        self._load_topics()
    
    def _parse_version(self, version_str):
        """解析版本号字符串为可比较的元组，如 '1.21.120' -> (1, 21, 120)"""
        try:
            return tuple(int(x) for x in version_str.strip().split('.'))
        except (ValueError, AttributeError):
            return (0,)
    
    def _version_exceeds_max(self, version_str):
        """检查版本是否超出最大支持版本"""
        return self._parse_version(version_str) > self._parse_version(self.max_version)
    
    def _filter_content(self, content):
        """过滤掉引用了超出版本的内容段落，并在开头添加版本警告"""
        import re
        # 检测 format_version / min_engine_version 等版本声明
        version_pattern = re.compile(
            r'["\']?(?:format_version|min_engine_version)["\']?\s*[:=]\s*["\']?([\d.]+)["\']?',
            re.IGNORECASE
        )
        
        found_versions = version_pattern.findall(content)
        has_exceeding = any(self._version_exceeds_max(v) for v in found_versions)
        
        warning = ""
        if has_exceeding:
            warning = (
                f"> ⚠️ 版本警告：本文档中包含高于 {self.max_version} 版本的内容，"
                f"这些特性在网易《我的世界》中国版中可能不可用。请以 docs/ 下的网易官方文档为准。\n\n"
            )
        
        return warning + content
    
    def _load_topics(self):
        """按一级子目录加载为 topic"""
        if not self.wiki_path.exists():
            return
        
        for subdir in sorted(self.wiki_path.iterdir()):
            if subdir.is_dir() and not subdir.name.startswith('.'):
                topic_key = subdir.name  # e.g. "entities", "blocks", "items"
                md_files = sorted(subdir.rglob("*.md"))
                if md_files:
                    self._topics[topic_key] = {
                        "name": topic_key,
                        "file_count": len(md_files),
                        "files": md_files,  # Path objects, lazy load content
                    }
        
        # 也加载根目录下的独立 md 文件
        root_mds = sorted(self.wiki_path.glob("*.md"))
        if root_mds:
            self._topics["_root"] = {
                "name": "概述",
                "file_count": len(root_mds),
                "files": root_mds,
            }
    
    def list_topics(self):
        """列出所有可用的 Wiki 主题"""
        return [
            {"key": k, "name": v["name"], "file_count": v["file_count"]}
            for k, v in self._topics.items()
            if k != "_root"
        ]
    
    def get_topic_content(self, topic_key, max_files=20):
        """获取指定主题的合并内容（带版本过滤）"""
        topic = self._topics.get(topic_key)
        if not topic:
            return None
        
        parts = []
        for md_file in topic["files"][:max_files]:
            try:
                raw = md_file.read_text(encoding="utf-8").strip()
                if raw:
                    filtered = self._filter_content(raw)
                    rel_name = str(md_file.relative_to(self.wiki_path))
                    parts.append(f"---\n## {rel_name}\n---\n\n{filtered}")
            except Exception:
                continue
        
        if not parts:
            return f"主题 '{topic_key}' 下没有可用内容"
        
        header = (
            f"# Bedrock Wiki: {topic_key}\n"
            f"> 来源: bedrock-wiki-wiki | 版本上限: {self.max_version}\n"
            f"> 共 {len(parts)} 个文档\n\n"
        )
        return header + "\n\n".join(parts)


# 全局 Bedrock Wiki 读取器实例
_bedrock_wiki_reader = None  # type: Optional[BedrockWikiReader]


def get_bedrock_wiki_reader():
    """获取 Bedrock Wiki 读取器实例"""
    global _bedrock_wiki_reader
    if _bedrock_wiki_reader is None:
        if BEDROCK_WIKI_PATH.exists():
            _bedrock_wiki_reader = BedrockWikiReader(
                BEDROCK_WIKI_PATH,
                max_version=BEDROCK_WIKI_MAX_VERSION
            )
        else:
            _bedrock_wiki_reader = BedrockWikiReader(
                BEDROCK_WIKI_PATH,  # will just have empty topics
                max_version=BEDROCK_WIKI_MAX_VERSION
            )
    return _bedrock_wiki_reader


# ============================================================================
# MCP Resources（用于提供 Skills 文件）
# ============================================================================

@server.list_resources()
async def list_resources() -> List[Resource]:
    """列出所有可用的 Resources"""
    resources = []

    from .standards import get_registry

    registry = get_registry()
    resources.extend([
        Resource(
            uri="modsdk-guidance://versions",
            name="ModSDK 规范版本",
            description="当前支持的 ModSDK/BE 版本、别名与运行时证据状态",
            mimeType="application/json",
        ),
        Resource(
            uri="modsdk-guidance://index",
            name="ModSDK 开发规则索引",
            description="经校验的版本化规则摘要，不暴露旧 standard/Skills 全文",
            mimeType="application/json",
        ),
        Resource(
            uri="modsdk-guidance://sources",
            name="ModSDK 规范来源",
            description="规则来源、authority 与快照元数据",
            mimeType="application/json",
        ),
        Resource(
            uri="modsdk-guidance://changes",
            name="ModSDK 官方版本完整差异",
            description="官方 3.9 与 3.10 的完整接口、事件、文档差异及更新日志分类",
            mimeType="application/json",
        ),
    ])
    for rule in registry.rules:
        resources.append(Resource(
            uri="modsdk-guidance://rules/{}".format(rule["id"]),
            name="ModSDK 规则: {}".format(rule["id"]),
            description=rule["title"],
            mimeType="application/json",
        ))
    
    # Bedrock Wiki 资源
    wiki_reader = get_bedrock_wiki_reader()
    for topic in wiki_reader.list_topics():
        resources.append(
            Resource(
                uri=f"bedrock-wiki://{topic['key']}",
                name=f"Bedrock Wiki: {topic['name']} ({topic['file_count']}篇)",
                description=f"Bedrock 版社区 Wiki: {topic['name']} 专题（{topic['file_count']}篇，版本上限 {BEDROCK_WIKI_MAX_VERSION}）",
                mimeType="text/markdown"
            )
        )

    docs_reader = get_docs_reader()
    categories = docs_reader.get_api_categories()
    api_total = docs_reader.get_api_entry_count()

    # API/事件紧凑索引 Resource — 让 LLM 直接看到所有 API，用自身语义能力匹配
    resources.append(
        Resource(
            uri="api-index://full",
            name="ModSDK API/事件完整索引",
            description=f"{api_total}个API/事件的紧凑索引（按分类组织）。LLM可直接阅读此索引找到正确的API名称，然后用get_api_detail获取完整签名。比search_api更精准。",
            mimeType="text/plain"
        )
    )

    # 按顶级分类拆分的子索引
    for top_cat in sorted(categories.keys()):
        total = sum(categories[top_cat].values())
        if total > 0:
            resources.append(
                Resource(
                    uri=f"api-index://{top_cat}",
                    name=f"ModSDK索引: {top_cat} ({total}条)",
                    description=f"{top_cat}分类下的API/事件索引，含{total}个条目",
                    mimeType="text/plain"
                )
            )

    # 网易官方教程 Resource — 高频使用的教程文档可直接加载
    GUIDE_RESOURCES = [
        ("guide://json-ui", "JSON UI 完整说明文档",
         "网易官方JSON UI教程（2741行），含控件类型、属性、数据绑定、动画、_ui_defs等完整参考",
         "21-界面与交互/30-UI说明文档.md"),
        ("guide://custom-dimension", "自定义维度教程合集",
         "网易官方自定义维度教程（7篇），含维度配置、群系地貌、生物生成、自定义特征、传送门等",
         "15-自定义游戏内容/4-自定义维度"),
        ("guide://custom-block", "自定义方块教程合集",
         "网易官方自定义方块教程，含JSON组件（675行）、方块功能、特殊方块等",
         "15-自定义游戏内容/2-自定义方块"),
        ("guide://custom-entity", "自定义实体教程合集",
         "网易官方自定义实体教程，含实体组件、AI行为、动画、渲染等",
         "15-自定义游戏内容/3-自定义生物"),
        ("guide://custom-item", "自定义物品教程合集",
         "网易官方自定义物品教程，含物品组件、物品事件等",
         "15-自定义游戏内容/1-自定义物品"),
        ("guide://particle-effect", "方块粒子特效与实体外观教程",
         "网易官方自定义方块实体外观教程，含网易版粒子特效、序列帧特效、原版粒子特效及控制接口",
         "15-自定义游戏内容/2-自定义方块/4.1-自定义方块实体外观.md"),
    ]

    for uri_str, name, desc, _ in GUIDE_RESOURCES:
        resources.append(
            Resource(uri=uri_str, name=name, description=desc, mimeType="text/markdown")
        )

    return resources


# 教程 Resource 路径映射（用于 read_resource）
_GUIDE_RESOURCE_PATHS = {
    "json-ui": "21-界面与交互/30-UI说明文档.md",
    "custom-dimension": "15-自定义游戏内容/4-自定义维度",
    "custom-block": "15-自定义游戏内容/2-自定义方块",
    "custom-entity": "15-自定义游戏内容/3-自定义生物",
    "custom-item": "15-自定义游戏内容/1-自定义物品",
    "particle-effect": "15-自定义游戏内容/2-自定义方块/4.1-自定义方块实体外观.md",
}


@server.read_resource()
async def read_resource(uri) -> str:
    """读取指定的 Resource 内容"""
    uri = str(uri)  # AnyUrl -> str

    # 解析 URI
    if uri.startswith("modsdk-guidance://"):
        from .standards import get_registry

        registry = get_registry()
        key = uri[len("modsdk-guidance://"):]
        if key == "versions":
            payload = {
                "schema_version": registry.manifest["schema_version"],
                "default_version": registry.manifest["default_version"],
                "versions": list(registry.versions),
            }
        elif key == "index":
            payload = {
                "schema_version": registry.manifest["schema_version"],
                "rules": [
                    {
                        field: rule[field]
                        for field in ("id", "title", "domain", "sides", "artifact_types", "versions", "severity", "enforcement", "authority")
                    }
                    for rule in registry.rules
                ],
            }
        elif key == "sources":
            payload = {
                "schema_version": registry.manifest["schema_version"],
                "sources": list(registry.sources),
            }
        elif key == "changes":
            payload = registry.get_version_changes()
        elif key.startswith("rules/"):
            rule_id = key[len("rules/"):]
            try:
                payload = registry.get_rule(rule_id)
            except KeyError:
                return json.dumps({"error": "未知规则 ID", "rule_id": rule_id}, ensure_ascii=False, sort_keys=True)
        else:
            return json.dumps({"error": "未知 guidance Resource", "uri": uri}, ensure_ascii=False, sort_keys=True)
        return json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2)

    if uri.startswith("bedrock-wiki://"):
        topic_key = uri[15:]  # 移除 "bedrock-wiki://" 前缀
        wiki_reader = get_bedrock_wiki_reader()
        content = wiki_reader.get_topic_content(topic_key)
        if content:
            return content
        else:
            topics = wiki_reader.list_topics()
            available = ', '.join(t['key'] for t in topics)
            return f"Wiki 主题 '{topic_key}' 不存在。可用主题: {available}"
    
    elif uri.startswith("api-index://"):
        from urllib.parse import unquote
        key = unquote(uri[12:])  # 移除前缀 + URL解码中文
        docs_reader = get_docs_reader()

        if key == "full":
            # 全量紧凑索引
            return docs_reader.generate_compact_index(include_params=False)
        else:
            # 按分类过滤的子索引
            index = docs_reader.generate_compact_index(include_params=False)
            # 从全量索引中提取指定分类的段落
            lines = index.splitlines()
            result_lines = []
            in_target = False
            target_header = f"## {key} "

            for line in lines:
                if line.startswith("## 常见操作速查"):
                    # 始终包含速查表
                    in_target = True
                elif line.startswith("## ") and not line.startswith("###"):
                    in_target = line.startswith(target_header)

                if in_target:
                    result_lines.append(line)

            if result_lines:
                return "\n".join(result_lines)
            else:
                return f"分类 '{key}' 不存在。可用分类请查看 api-index://full"

    elif uri.startswith("guide://"):
        from urllib.parse import unquote
        key = unquote(uri[8:])
        docs_reader = get_docs_reader()

        if key not in _GUIDE_RESOURCE_PATHS:
            return f"教程 '{key}' 不存在。可用教程: {', '.join(_GUIDE_RESOURCE_PATHS.keys())}"

        rel_path = _GUIDE_RESOURCE_PATHS[key]

        if not docs_reader.guide_root:
            return "未找到网易官方教程文档目录。请设置 MODSDK_WIKI_PATH 环境变量。"

        target = Path(docs_reader.guide_root) / rel_path

        if target.is_file():
            # 单文件教程（如 JSON UI 说明文档）
            with open(target, "r", encoding="utf-8") as f:
                return f.read()
        elif target.is_dir():
            # 目录教程（合并多个 md 文件）
            parts = []
            for md_file in sorted(target.rglob("*.md")):
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                if content:
                    # 添加文件名作为分隔
                    rel_name = str(md_file.relative_to(target))
                    parts.append(f"---\n## 📄 {rel_name}\n---\n\n{content}")
            return "\n\n".join(parts) if parts else f"目录 '{rel_path}' 下没有 md 文件"
        else:
            return f"路径不存在: {rel_path}"

    else:
        return f"未知的资源 URI: {uri}"


def _try_inline_enum(docs_reader, text: str) -> Optional[str]:
    """检测文本中的枚举引用，返回内联字符串。
    支持格式: [AttrType枚举](...), 枚举值文档的[AttrType](...), AttrType枚举
    """
    if not text:
        return None
    # 匹配 [XXX枚举] 或 [XXX] 后面跟枚举相关链接
    import re
    patterns = [
        r'\[([A-Za-z]\w+?)枚举\]',      # [AttrType枚举](...)
        r'枚举值文档的\[([A-Za-z]\w+?)\]',  # 枚举值文档的[AttrType](...)
        r'\[([A-Za-z]\w+?)\]\([^)]*枚举值',  # [AttrType](../枚举值/...)
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            enum_name = match.group(1)
            inline = docs_reader.get_enum_inline(enum_name)
            if inline:
                return f"  - {enum_name}: {inline}"
    return None


# ============================================================================
# 工具定义
# ============================================================================

@server.list_tools()
async def list_tools() -> List[Tool]:
    """列出所有可用的工具"""
    return [
        # 文档查询工具
        Tool(
            name="search_docs",
            description="""搜索 ModSDK API 参考文档的详细说明、备注、代码示例和枚举值。

⚠️ 查找具体 API/事件请优先用 search_api（更精准、更省上下文）。
本工具适合搜索：API 的详细用法说明、参数备注、代码示例、枚举值定义。

支持：模糊匹配、驼峰分词、中文搜索。""",
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
            name="search_api",
            description="""精确搜索 ModSDK 的 API 接口或事件（利用结构化数据索引）。

⚠️ 推荐优先使用 api-index://full Resource 直接浏览API索引，LLM语义理解比关键词搜索更精准。
找到API名后用 get_api_detail 获取完整签名。本工具适合探索性搜索（不确定API名称时）。

搜索示例：
- "GetPlayerPos" - 查找获取玩家位置的 API
- "玩家死亡" - 查找玩家死亡相关事件
- "按钮" / "button" - 查找 UI 按钮相关 API
- "SetBlock" - 查找方块放置相关的 API""",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索关键词（API 名、事件名、或中文描述）"
                    },
                    "entry_type": {
                        "type": "string",
                        "description": "搜索类型: api（仅接口）、event（仅事件）、all（全部）",
                        "enum": ["all", "api", "event"],
                        "default": "all"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "返回结果数量限制，默认 5",
                        "default": 5
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_api_detail",
            description="""按精确名称获取 API/事件的完整详情（参数签名、返回值、描述）。

推荐工作流：先通过 api-index Resource 浏览索引找到API名 → 再用本工具获取完整签名。
也可配合 search_api 使用：search_api 找到大致目标 → get_api_detail 获取精确参数。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "API或事件的精确名称，如 'SpawnItemToPlayerInv'、'MobDieEvent'"
                    }
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="get_document",
            description="获取指定文档内容。大文档（>8000字符）会自动返回目录结构，建议优先使用 get_document_section 获取具体章节。",
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

        Tool(
            name="get_version_changes",
            description="查询官方 3.9→3.10 完整差异。区分更新日志明确新增、索引新增、契约调整、分类迁移及旧库清理；默认返回摘要，可筛选名称并分页。",
            inputSchema={
                "type": "object",
                "properties": {
                    "section": {"type": "string", "enum": ["overview", "api", "event", "enum", "documents", "release_notes", "repository_reconciliation"], "default": "overview"},
                    "operation": {"type": "string", "enum": ["all", "added", "removed", "changed"], "default": "all"},
                    "query": {"type": "string", "default": ""},
                    "offset": {"type": "integer", "minimum": 0, "default": 0},
                    "limit": {"type": "integer", "minimum": 1, "maximum": 50, "default": 20},
                    "include_details": {"type": "boolean", "default": False},
                },
            },
        ),
        Tool(
            name="get_development_guidance",
            description="按目标、领域、端侧和 ModSDK 版本返回最相关的版本化开发规则与证据边界。",
            inputSchema={
                "type": "object",
                "properties": {
                    "goal": {
                        "type": "string",
                        "minLength": 1,
                        "description": "当前开发目标，不能为空"
                    },
                    "domain": {
                        "type": "string",
                        "enum": ["auto", "python", "architecture", "api_event", "json_content", "json_ui", "performance", "multiplayer"],
                        "default": "auto"
                    },
                    "side": {
                        "type": "string",
                        "enum": ["auto", "client", "server", "common", "cross_side"],
                        "default": "auto"
                    },
                    "target_version": {
                        "type": "string",
                        "default": "current"
                    },
                    "max_rules": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 12,
                        "default": 8
                    }
                },
                "required": ["goal"]
            }
        ),
        
        # 代码生成与组件包构建工具
        Tool(
            name="generate_mod_project",
            description="""生成完整可运行的双包 AddOn 项目骨架（behavior_pack + resource_pack）。

【生成的完整项目结构】
1. `behavior_pack/manifest.json` — 最新标准清单（`format_version: 2`，含唯一 UUID 并绑定资源包依赖）
2. `behavior_pack/entities/.gitkeep` — 保留中国版强制要求的 `entities/` 目录（平台审核错误码 24 检查项）
3. `behavior_pack/{mod_id}_Script/` — 直接位于行为包根目录下的扁平 Python 脚本包（`__init__.py`、`modConfig.py`、`modMain.py`、`serverSystem.py`、`clientSystem.py`），内置双端闭环事件通信
4. `resource_pack/manifest.json` — 最新标准资源包清单（`format_version: 2`）
5. `resource_pack/textures/{item_texture.json,terrain_texture.json}` — 满足中国版必选 `textures/` 目录并初始化贴图注册表
6. `resource_pack/texts/{languages.json,zh_CN.lang}` — 本地化语言注册与条目

默认使用无后缀 `behavior_pack` / `resource_pack`；若接入已有带后缀工程（如 MCStudio 目录），可通过 `behavior_pack_dir` / `resource_pack_dir` 指定。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "mod_name": {
                        "type": "string",
                        "description": "Mod 显示名称，如 '我的第一个Mod'"
                    },
                    "mod_id": {
                        "type": "string",
                        "description": "Mod 标识符与命名空间（小写字母开头，仅含小写字母/数字/下划线，如 'my_first_mod'）"
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
                        "description": "三段式版本号，如 '1.0.0'",
                        "default": "1.0.0"
                    },
                    "min_engine_version": {
                        "type": "array",
                        "items": {"type": "integer"},
                        "description": "最低引擎版本三元组，默认 [1, 18, 0]",
                        "default": [1, 18, 0]
                    },
                    "behavior_pack_dir": {
                        "type": "string",
                        "description": "行为包目录名，默认 'behavior_pack'",
                        "default": "behavior_pack"
                    },
                    "resource_pack_dir": {
                        "type": "string",
                        "description": "资源包目录名，默认 'resource_pack'",
                        "default": "resource_pack"
                    }
                },
                "required": ["mod_name", "mod_id"]
            }
        ),
        Tool(
            name="generate_manifest_json",
            description="""生成符合网易最新规范的 `manifest.json` 包清单（严格使用 `manifest.json` 文件名与 `format_version: 2`）。

支持单独生成行为包、资源包清单，或一键生成双包互绑依赖清单（`pack_type="both"`）。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "pack_name": {
                        "type": "string",
                        "description": "组件包名称"
                    },
                    "description": {
                        "type": "string",
                        "description": "组件包描述",
                        "default": ""
                    },
                    "pack_type": {
                        "type": "string",
                        "enum": ["both", "behavior", "resource"],
                        "default": "both",
                        "description": "生成类型：both（双包并自动绑定依赖）、behavior（仅行为包）、resource（仅资源包）"
                    },
                    "version": {
                        "type": "string",
                        "description": "三段式版本号，如 '1.0.0'",
                        "default": "1.0.0"
                    },
                    "min_engine_version": {
                        "type": "array",
                        "items": {"type": "integer"},
                        "description": "最低引擎版本三元组，默认 [1, 18, 0]",
                        "default": [1, 18, 0]
                    },
                    "resource_pack_uuid": {
                        "type": "string",
                        "description": "可选：单独生成 behavior 清单时指定要依赖的资源包 header UUID"
                    },
                    "behavior_pack_dir": {
                        "type": "string",
                        "description": "行为包目录名，默认 'behavior_pack'",
                        "default": "behavior_pack"
                    },
                    "resource_pack_dir": {
                        "type": "string",
                        "description": "资源包目录名，默认 'resource_pack'",
                        "default": "resource_pack"
                    }
                },
                "required": ["pack_name"]
            }
        ),
        Tool(
            name="generate_ui_json",
            description="""生成自定义 JSON UI 配套文件集（`resource_pack/ui/<ui_namespace>.json`、`resource_pack/ui/_ui_defs.json` 及可选 `ScreenNode` 客户端控制器）。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "ui_namespace": {
                        "type": "string",
                        "description": "UI 命名空间与文件名（小写字母开头，如 'main_hud' 或 'shop_panel'）"
                    },
                    "title": {
                        "type": "string",
                        "description": "界面标题文本",
                        "default": "自定义界面"
                    },
                    "is_hud": {
                        "type": "boolean",
                        "description": "是否为常驻 HUD（True 生成不拦截输入的 HUD 面板；False 生成带关闭按钮的弹窗 Screen）",
                        "default": False
                    },
                    "include_python": {
                        "type": "boolean",
                        "description": "是否同时生成配套 ScreenNode Python 客户端脚本",
                        "default": True
                    },
                    "mod_id": {
                        "type": "string",
                        "description": "所属 Mod ID（用于生成脚本包路径），默认 'mymod'",
                        "default": "mymod"
                    },
                    "behavior_pack_dir": {
                        "type": "string",
                        "description": "行为包目录名，默认 'behavior_pack'",
                        "default": "behavior_pack"
                    },
                    "resource_pack_dir": {
                        "type": "string",
                        "description": "资源包目录名，默认 'resource_pack'",
                        "default": "resource_pack"
                    }
                },
                "required": ["ui_namespace"]
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
            description="生成已查证的官方事件或显式声明的自定义事件监听器代码。官方同名多端事件必须选择端侧。",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_name": {
                        "type": "string",
                        "description": "事件名称，如 'AddServerPlayerEvent'"
                    },
                    "event_description": {
                        "type": "string",
                        "description": "事件描述",
                        "default": "事件处理"
                    },
                    "side": {
                        "type": "string",
                        "enum": ["auto", "client", "server"],
                        "default": "auto",
                        "description": "事件端侧；官方事件同名多端时必须显式选择"
                    },
                    "event_kind": {
                        "type": "string",
                        "enum": ["official", "custom"],
                        "default": "official"
                    },
                    "params": {
                        "type": "object",
                        "description": "自定义事件的参数名到说明映射；官方事件参数由文档取得"
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
            description="生成自定义物品完整配套文件（服务端交互脚本 + 行为包/资源包 1.10 JSON + item_texture.json + 语言文件）。",
            inputSchema={
                "type": "object",
                "properties": {
                    "item_id": {
                        "type": "string",
                        "description": "物品ID，如 'magic_wand'"
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
                        "description": "最大堆叠数量 (1-64)",
                        "default": 64
                    },
                    "hand_equipped": {
                        "type": "boolean",
                        "description": "是否按手持武器方式渲染",
                        "default": False
                    },
                    "behavior_pack_dir": {
                        "type": "string",
                        "description": "行为包目录名，默认 'behavior_pack'",
                        "default": "behavior_pack"
                    },
                    "resource_pack_dir": {
                        "type": "string",
                        "description": "资源包目录名，默认 'resource_pack'",
                        "default": "resource_pack"
                    }
                },
                "required": ["item_id"]
            }
        ),
        Tool(
            name="generate_custom_block",
            description="生成自定义方块完整配套文件（服务端交互脚本 + 现代 1.19.20 方块行为 JSON + blocks.json + terrain_texture.json + 语言文件）。",
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
                    },
                    "display_name": {
                        "type": "string",
                        "description": "显示名称",
                        "default": "自定义方块"
                    },
                    "behavior_pack_dir": {
                        "type": "string",
                        "description": "行为包目录名，默认 'behavior_pack'",
                        "default": "behavior_pack"
                    },
                    "resource_pack_dir": {
                        "type": "string",
                        "description": "资源包目录名，默认 'resource_pack'",
                        "default": "resource_pack"
                    }
                },
                "required": ["block_id"]
            }
        ),

        # ============================================================
        # 数据驱动 JSON 生成工具
        # ============================================================
        Tool(
            name="generate_item_json",
            description="""生成网易 `1.10` 自定义基础物品完整配套文件集：
- `behavior_pack/netease_items_beh/<namespace>_<item_id>.json`
- `resource_pack/netease_items_res/<namespace>_<item_id>.json`
- `resource_pack/textures/item_texture.json`
- `resource_pack/texts/languages.json` 与 `zh_CN.lang`

【重要】网易物品必须使用 `format_version: "1.10"` 及官方支持的 1.10/netease 组件（如 `minecraft:max_damage`、`netease:weapon`、`netease:armor`、`netease:customtips`），禁止混入国际版 1.16.100+ 组件（如 `minecraft:durability`、`minecraft:digger`）。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {
                        "type": "string",
                        "description": "命名空间（全小写字母开头，如 'mymod'）"
                    },
                    "item_id": {
                        "type": "string",
                        "description": "物品ID（全小写+下划线，如 'magic_gem'）"
                    },
                    "category": {
                        "type": "string",
                        "description": "创造栏分类 (items/equipment/construction/nature/commands/none)",
                        "default": "items"
                    },
                    "max_stack_size": {
                        "type": "integer",
                        "description": "最大堆叠数量 (1-64)",
                        "default": 64
                    },
                    "display_name": {
                        "type": "string",
                        "description": "中文显示名称",
                        "default": "自定义物品"
                    },
                    "components": {
                        "type": "object",
                        "description": "额外行为包物品组件（仅限网易 1.10 支持组件，如 minecraft:max_damage, minecraft:food, netease:customtips）"
                    },
                    "behavior_pack_dir": {
                        "type": "string",
                        "description": "行为包目录名，默认 'behavior_pack'",
                        "default": "behavior_pack"
                    },
                    "resource_pack_dir": {
                        "type": "string",
                        "description": "资源包目录名，默认 'resource_pack'",
                        "default": "resource_pack"
                    }
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_block_json",
            description="""生成自定义方块完整配套文件集：
- `behavior_pack/netease_blocks/<namespace>_<block_id>.json`
- `resource_pack/blocks.json`
- `resource_pack/textures/terrain_texture.json`
- `resource_pack/texts/languages.json` 与 `zh_CN.lang`

默认采用现代推荐档 `modern_1_19_20`（`format_version: "1.19.20"`，`minecraft:destructible_by_mining`、`minecraft:light_emission` 0-15 整数）；若显式指定旧档 `legacy_1_10` 或 `scalar_1_16`，`light_emission` 会自动归一化至引擎要求的 `[0.0, 1.0]` 浮点区间。""",
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
                        "type": "number",
                        "description": "发光等级 [0-15]",
                        "default": 0
                    },
                    "light_dampening": {
                        "type": "integer",
                        "description": "遮光等级 [0-15]",
                        "default": 15
                    },
                    "map_color": {
                        "type": "string",
                        "description": "地图颜色（十六进制，如 '#FF5500'）",
                        "default": "#FFFFFF"
                    },
                    "category": {
                        "type": "string",
                        "description": "创造栏分类 (Construction/Nature/Equipment/Items)",
                        "default": "Nature"
                    },
                    "register_to_menu": {
                        "type": "boolean",
                        "description": "是否注册到创造模式物品栏",
                        "default": True
                    },
                    "sound": {
                        "type": "string",
                        "description": "方块音效名（写入 blocks.json，如 'stone'、'wood'、'metal'）",
                        "default": "stone"
                    },
                    "display_name": {
                        "type": "string",
                        "description": "中文显示名称",
                        "default": "自定义方块"
                    },
                    "components": {
                        "type": "object",
                        "description": "额外方块组件"
                    },
                    "format_profile": {
                        "type": "string",
                        "enum": ["legacy_1_10", "scalar_1_16", "modern_1_19_20"],
                        "default": "modern_1_19_20",
                        "description": "方块 format_version 与组件形状档（默认推荐 modern_1_19_20）"
                    },
                    "behavior_pack_dir": {
                        "type": "string",
                        "description": "行为包目录名，默认 'behavior_pack'",
                        "default": "behavior_pack"
                    },
                    "resource_pack_dir": {
                        "type": "string",
                        "description": "资源包目录名，默认 'resource_pack'",
                        "default": "resource_pack"
                    }
                },
                "required": ["namespace", "block_id"]
            }
        ),
        Tool(
            name="generate_recipe_json",
            description="""生成合成配方 JSON 文件（位于 `behavior_pack/netease_recipes/<namespace>_<recipe_id>.json`）。

支持 `shaped`（有序合成）、`shapeless`（无序合成）、`furnace`（熔炉烧炼）。""",
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
                    },
                    "behavior_pack_dir": {
                        "type": "string",
                        "description": "行为包目录名，默认 'behavior_pack'",
                        "default": "behavior_pack"
                    }
                },
                "required": ["recipe_type", "namespace", "recipe_id"]
            }
        ),
        Tool(
            name="generate_entity_json",
            description=f"""生成自定义实体完整配套文件集（遵循 NetEase {MODSDK_LABEL} 规范）：
- `behavior_pack/entities/<namespace>_<entity_id>.json`
- `resource_pack/entity/<namespace>_<entity_id>.entity.json`
- `resource_pack/models/entity/<namespace>_<entity_id>.geo.json`（配套 1.12.0 几何体模型，避免缺少模型报错）
- `resource_pack/texts/languages.json` 与 `zh_CN.lang`""",
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
                    "family": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "实体家族标签列表"
                    },
                    "runtime_identifier": {
                        "type": "string",
                        "description": "基于哪个原版实体构建（如 'minecraft:pig'、'minecraft:zombie'）；不传时按 preset 自动选择合法原版实体"
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
                    },
                    "preset": {
                        "type": "string",
                        "description": "实体预设: mount(坐骑), pet(宠物), npc(NPC), hostile(敌对)",
                        "enum": ["mount", "pet", "npc", "hostile"]
                    },
                    "components": {
                        "type": "object",
                        "description": "额外实体行为组件"
                    },
                    "display_name": {
                        "type": "string",
                        "description": "中文显示名称",
                        "default": "自定义生物"
                    },
                    "behavior_pack_dir": {
                        "type": "string",
                        "description": "行为包目录名，默认 'behavior_pack'",
                        "default": "behavior_pack"
                    },
                    "resource_pack_dir": {
                        "type": "string",
                        "description": "资源包目录名，默认 'resource_pack'",
                        "default": "resource_pack"
                    }
                },
                "required": ["namespace", "entity_id"]
            }
        ),
        Tool(
            name="generate_loot_table_json",
            description="""生成战利品表 JSON 文件（位于 `behavior_pack/loot_tables/<table_name>.json`）。""",
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
                    },
                    "table_name": {
                        "type": "string",
                        "description": "战利品表文件名（不含 .json）",
                        "default": "custom_loot"
                    },
                    "behavior_pack_dir": {
                        "type": "string",
                        "description": "行为包目录名，默认 'behavior_pack'",
                        "default": "behavior_pack"
                    }
                },
                "required": ["pools"]
            }
        ),
        Tool(
            name="generate_spawn_rules_json",
            description="""生成实体自然生成规则 JSON 文件（位于 `behavior_pack/spawn_rules/<namespace>_<entity_id>.json`）。""",
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
                    },
                    "behavior_pack_dir": {
                        "type": "string",
                        "description": "行为包目录名，默认 'behavior_pack'",
                        "default": "behavior_pack"
                    }
                },
                "required": ["namespace", "entity_id"]
            }
        ),

        # ============================================================
        # 高级物品生成工具（严格遵循网易 1.10 官方组件规范）
        # ============================================================
        Tool(
            name="generate_sword_json",
            description="""【一键生成】网易 1.10 自定义剑类武器配套文件集（`custom_item_type: "weapon"` + `netease:weapon` + `minecraft:max_damage` + `item_texture.json` + 语言文件）。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "damage": {"type": "integer", "description": "攻击伤害", "default": 5},
                    "durability": {"type": "integer", "description": "最大耐久值", "default": 250},
                    "enchantability": {"type": "integer", "description": "附魔能力值", "default": 14},
                    "level": {"type": "integer", "description": "武器等级与铁砧修复档位 (0=木/金, 1=石, 2=铁, 3=钻石)", "default": 2},
                    "repair_material": {"type": "string", "description": "可选：按修复材料推断 level（如 minecraft:diamond -> 3）"},
                    "display_name": {"type": "string", "description": "显示名称", "default": "自定义剑"},
                    "behavior_pack_dir": {"type": "string", "default": "behavior_pack"},
                    "resource_pack_dir": {"type": "string", "default": "resource_pack"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_pickaxe_json",
            description="""【一键生成】网易 1.10 自定义镐类工具配套文件集（`custom_item_type: "weapon"` + `netease:weapon.type="pickaxe"` + 挖掘等级与速度 + 贴图注册）。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "durability": {"type": "integer", "description": "最大耐久值", "default": 250},
                    "mining_speed": {"type": "integer", "description": "基础挖掘速度", "default": 6},
                    "damage": {"type": "integer", "description": "近战伤害", "default": 2},
                    "enchantability": {"type": "integer", "description": "附魔能力值", "default": 14},
                    "level": {"type": "integer", "description": "挖掘等级 (0=木/金, 1=石, 2=铁, 3=钻石)", "default": 2},
                    "repair_material": {"type": "string", "description": "可选：修复材料映射"},
                    "display_name": {"type": "string", "description": "显示名称", "default": "自定义镐"},
                    "behavior_pack_dir": {"type": "string", "default": "behavior_pack"},
                    "resource_pack_dir": {"type": "string", "default": "resource_pack"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_axe_json",
            description="""【一键生成】网易 1.10 自定义斧类工具配套文件集（使用官方 `netease:weapon.type="hatchet"` + 攻击伤害 + 挖掘速度 + 贴图注册）。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "damage": {"type": "integer", "description": "攻击伤害", "default": 4},
                    "durability": {"type": "integer", "description": "最大耐久值", "default": 250},
                    "mining_speed": {"type": "integer", "description": "基础挖掘速度", "default": 6},
                    "enchantability": {"type": "integer", "description": "附魔能力值", "default": 14},
                    "level": {"type": "integer", "description": "工具等级 (0=木/金, 1=石, 2=铁, 3=钻石)", "default": 2},
                    "repair_material": {"type": "string", "description": "可选：修复材料映射"},
                    "display_name": {"type": "string", "description": "显示名称", "default": "自定义斧"},
                    "behavior_pack_dir": {"type": "string", "default": "behavior_pack"},
                    "resource_pack_dir": {"type": "string", "default": "resource_pack"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_shovel_json",
            description="""【一键生成】网易 1.10 自定义锹类工具配套文件集（`netease:weapon.type="shovel"` + 挖掘速度 + 贴图注册）。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "durability": {"type": "integer", "description": "最大耐久值", "default": 250},
                    "mining_speed": {"type": "integer", "description": "基础挖掘速度", "default": 6},
                    "damage": {"type": "integer", "description": "近战伤害", "default": 1},
                    "enchantability": {"type": "integer", "description": "附魔能力值", "default": 14},
                    "level": {"type": "integer", "description": "工具等级", "default": 2},
                    "repair_material": {"type": "string", "description": "可选：修复材料映射"},
                    "display_name": {"type": "string", "description": "显示名称", "default": "自定义锹"},
                    "behavior_pack_dir": {"type": "string", "default": "behavior_pack"},
                    "resource_pack_dir": {"type": "string", "default": "resource_pack"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_hoe_json",
            description="""【一键生成】网易 1.10 自定义锄类工具配套文件集（`netease:weapon.type="hoe"` + 耕地功能 + 贴图注册）。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "durability": {"type": "integer", "description": "最大耐久值", "default": 250},
                    "enchantability": {"type": "integer", "description": "附魔能力值", "default": 14},
                    "level": {"type": "integer", "description": "工具等级", "default": 2},
                    "repair_material": {"type": "string", "description": "可选：修复材料映射"},
                    "display_name": {"type": "string", "description": "显示名称", "default": "自定义锄"},
                    "behavior_pack_dir": {"type": "string", "default": "behavior_pack"},
                    "resource_pack_dir": {"type": "string", "default": "resource_pack"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_food_json",
            description="""【一键生成】网易 1.10 自定义食物配套文件集（行为包 `minecraft:food` + 整数刻 `minecraft:use_duration` + 资源包 `minecraft:use_animation`）。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "nutrition": {"type": "integer", "description": "恢复饥饿值", "default": 4},
                    "saturation": {"type": "string", "description": "饱和度等级 (poor/low/normal/good/max/supernatural)", "default": "normal"},
                    "can_always_eat": {"type": "boolean", "description": "是否满饥饿也可食用", "default": False},
                    "use_duration": {"type": "integer", "description": "食用耗时（游戏刻 tick，默认 32）", "default": 32},
                    "effects": {
                        "type": "array",
                        "description": "药水效果列表 [{name, duration, amplifier, chance}]",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string", "description": "效果名称"},
                                "duration": {"type": "integer", "description": "持续时间(秒)"},
                                "amplifier": {"type": "integer", "description": "效果等级"},
                                "chance": {"type": "number", "description": "触发概率(0-1)"}
                            }
                        }
                    },
                    "display_name": {"type": "string", "description": "显示名称", "default": "自定义食物"},
                    "behavior_pack_dir": {"type": "string", "default": "behavior_pack"},
                    "resource_pack_dir": {"type": "string", "default": "resource_pack"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_armor_json",
            description="""【一键生成】网易 1.10 自定义盔甲完整配套文件集（`custom_item_type: "armor"` + `netease:armor` + `resource_pack/attachables/` 穿戴渲染模型绑定 + 贴图注册）。""",
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
                    "protection": {"type": "integer", "description": "护甲防御值 (defense)", "default": 5},
                    "durability": {"type": "integer", "description": "最大耐久值", "default": 165},
                    "enchantability": {"type": "integer", "description": "附魔能力值", "default": 9},
                    "toughness": {"type": "integer", "description": "可选：盔甲韧性 (0-20)"},
                    "knockback_resistance": {"type": "number", "description": "可选：击退抗性 (0.0-1.0)"},
                    "display_name": {"type": "string", "description": "显示名称"},
                    "behavior_pack_dir": {"type": "string", "default": "behavior_pack"},
                    "resource_pack_dir": {"type": "string", "default": "resource_pack"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_bow_json",
            description="""【一键生成】网易 1.10 自定义远程蓄力武器配套文件集（`custom_item_type: "ranged_weapon"` + `minecraft:use_duration` + 资源包 `netease:frame_animation` 3 帧蓄力贴图注册）。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID（若需第三人称拉弓抬手动画，官方要求填 'bow'）"},
                    "durability": {"type": "integer", "description": "最大耐久值", "default": 384},
                    "use_duration": {"type": "integer", "description": "最大蓄力时长（tick，默认 72000）", "default": 72000},
                    "projectile_entity": {"type": "string", "description": "松手发射的抛射物实体标识", "default": "minecraft:arrow"},
                    "display_name": {"type": "string", "description": "显示名称", "default": "自定义弓"},
                    "behavior_pack_dir": {"type": "string", "default": "behavior_pack"},
                    "resource_pack_dir": {"type": "string", "default": "resource_pack"}
                },
                "required": ["namespace", "item_id"]
            }
        ),
        Tool(
            name="generate_throwable_json",
            description="""【一键生成】网易 1.10 自定义投掷物配套文件集（`custom_item_type: "projectile_item"` + `netease:projectile` + 贴图注册）。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {"type": "string", "description": "命名空间"},
                    "item_id": {"type": "string", "description": "物品ID"},
                    "projectile_entity": {"type": "string", "description": "右键发射的抛射物实体 identifier（如 'minecraft:snowball'）"},
                    "max_stack_size": {"type": "integer", "description": "最大堆叠数量 (1-64)", "default": 16},
                    "cooldown_ticks": {"type": "integer", "description": "可选冷却时间", "default": 0},
                    "display_name": {"type": "string", "description": "显示名称", "default": "自定义投掷物"},
                    "behavior_pack_dir": {"type": "string", "default": "behavior_pack"},
                    "resource_pack_dir": {"type": "string", "default": "resource_pack"}
                },
                "required": ["namespace", "item_id", "projectile_entity"]
            }
        ),

        # 代码审查工具
        Tool(
            name="review_code",
            description="""审查显式传入的 Python/JSON 文本，检测确定性兼容问题、架构违规和带证据边界的工程风险。

确定性阻断包括：UTF-8 声明、Python 2.7 语法、真实 u/U/ur/ru 前缀、精确导入白名单、跨端导入、动态导入、已证实事件字段，以及 JSON 解析、重复键、manifest.json 规范、必需标识、网易 1.10 物品组件合法性和方块版本—组件形状冲突。""",
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
                    },
                    "artifact_type": {
                        "type": "string",
                        "enum": ["auto", "python", "json", "json_ui", "item", "block", "manifest_json"],
                        "default": "auto"
                    },
                    "side": {
                        "type": "string",
                        "enum": ["auto", "client", "server", "common", "cross_side"],
                        "default": "auto"
                    },
                    "target_version": {
                        "type": "string",
                        "default": "current"
                    },
                    "project_modules": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "显式声明的项目内顶级模块或完整模块名"
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
            description="""搜索组件定义（网易支持的原版物品组件 / 方块组件 / 实体组件 / 网易特有组件）。

【支持的组件类型】
- item: 网易 1.10 支持的原版物品组件（minecraft:food, minecraft:max_damage 等）
- block: 方块组件（minecraft:destructible_by_mining, minecraft:light_emission 等）
- entity: 实体组件（minecraft:health, minecraft:movement 等）
- netease: 网易特有组件（netease:weapon, netease:armor, netease:tier 等）
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
- netease_item: 网易物品组件（4个）
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
            }
        ),
        Tool(
            name="get_best_practices",
            description="""获取 ModSDK 最佳实践规则。

【规则分类】
- python27_compatibility: Python 2.7 兼容性规则
- client_server_separation: 客户端/服务端分离规则
- performance: 性能优化规则
- ui_development: JSON UI 开发规则
- modsdk_38_migration: ModSDK 3.8 迁移规则
- modsdk_39_migration: ModSDK 3.9 / BE 1.21.120 历史迁移规则
- modsdk_310_migration: ModSDK 3.10 / BE 1.21.130 迁移规则
- all: 所有规则（默认）""",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "规则分类",
                        "enum": ["all", "python27_compatibility", "client_server_separation", "performance", "ui_development", "modsdk_38_migration", "modsdk_39_migration", "modsdk_310_migration"],
                        "default": "all"
                    }
                },
            }
        ),
        Tool(
            name="get_architecture_pattern",
            description="""获取 ModSDK 核心架构模式的完整代码示例。

当你不确定如何组合多个API实现一个完整功能时，先查架构模式。

可用模式：跨端通信、组件使用、UI开发流程、实体创建与管理、定时任务、物品掉落与生成
不传参数返回所有可用模式列表。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "pattern_name": {
                        "type": "string",
                        "description": "模式名称，如'跨端通信'、'UI开发流程'、'物品掉落'。支持模糊匹配。"
                    }
                },
            }
        ),
        Tool(
            name="browse_api_category",
            description="""按分类浏览API/事件列表。当 search_api 搜索不到时，用此工具按分类逐步缩小范围。

可用一级分类：实体、玩家、方块、世界、物品、特效、控制、模型、自定义UI、后处理、音效等。
支持二级分类路径，如"实体/属性"、"世界/天气"、"玩家/背包"。
不传 category 参数时返回完整分类目录树。""",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "分类路径，如'实体/属性'、'世界/天气'、'后处理'。支持模糊匹配。不传则返回全部分类目录。"
                    },
                    "entry_type": {
                        "type": "string",
                        "description": "筛选类型",
                        "enum": ["all", "api", "event"],
                        "default": "all"
                    },
                },
            }
        )
    ]


# ============================================================================
# 高级物品工具 - 统一查找表与格式化
# ============================================================================

ADVANCED_ITEM_TOOLS = {
    "generate_sword_json":     ("sword",     "自定义剑类武器"),
    "generate_pickaxe_json":   ("pickaxe",   "自定义镐类工具"),
    "generate_axe_json":       ("axe",       "自定义斧类工具"),
    "generate_shovel_json":    ("shovel",    "自定义锹类工具"),
    "generate_hoe_json":       ("hoe",       "自定义锄类工具"),
    "generate_food_json":      ("food",      "自定义食物"),
    "generate_armor_json":     ("armor",     "自定义盔甲"),
    "generate_bow_json":       ("bow",       "自定义远程弓"),
    "generate_throwable_json": ("throwable", "自定义投掷物"),
}

_SHARED_MERGE_NOTE = (
    "共享注册与语言文件（如 `item_texture.json`、`terrain_texture.json`、`blocks.json`、"
    "`_ui_defs.json`、`languages.json`、`zh_CN.lang`）：若项目中已存在同名文件，请将新增键值/词条合并进现有文件，勿直接覆盖已有条目。"
)


def _artifacts_from_files(
    files: Dict[str, str],
    project_modules: tuple = (),
    block_format_profile: Optional[str] = None,
) -> List[Artifact]:
    """将生成包中的路径到内容映射转换为结构化待校验 Artifact 列表。"""
    artifacts: List[Artifact] = []
    for filepath, content in files.items():
        norm = filepath.replace("\\", "/")
        lower = norm.lower()
        basename = norm.rsplit("/", 1)[-1].lower()
        if basename == ".gitkeep" or lower.endswith(".lang"):
            continue
        if lower.endswith(".py"):
            if basename == "modmain.py":
                side = "cross_side"
            elif (
                basename in {"serversystem.py", "server.py", "custom_command.py"}
                or basename.startswith(("item_", "block_"))
            ):
                side = "server"
            elif basename in {"clientsystem.py", "client.py"} or ("/ui/" in lower and basename != "__init__.py"):
                side = "client"
            else:
                side = "common"
            artifacts.append(
                Artifact(
                    content=content,
                    filename=norm,
                    artifact_type="python",
                    side=side,
                    target_version=CURRENT_TARGET_VERSION,
                    project_modules=project_modules,
                )
            )
        elif lower.endswith(".json"):
            if basename in {"manifest.json", "pack_manifest.json"}:
                artifact_type = "manifest_json"
                side = "common"
                fmt_profile = None
            elif "/netease_items_beh/" in lower:
                artifact_type = "item"
                side = "server"
                fmt_profile = None
            elif "/netease_items_res/" in lower:
                artifact_type = "item"
                side = "client"
                fmt_profile = None
            elif "/netease_blocks/" in lower:
                artifact_type = "block"
                side = "common"
                fmt_profile = block_format_profile
            elif "/ui/" in lower and basename != "_ui_defs.json":
                artifact_type = "json_ui"
                side = "client"
                fmt_profile = None
            else:
                artifact_type = "json"
                is_client = any(
                    marker in lower
                    for marker in ("/textures/", "/entity/", "/models/", "/attachables/", "/texts/", "/ui/", "/blocks.json")
                )
                side = "client" if is_client else "common"
                fmt_profile = None
            artifacts.append(
                Artifact(
                    content=content,
                    filename=norm,
                    artifact_type=artifact_type,
                    side=side,
                    target_version=CURRENT_TARGET_VERSION,
                    format_profile=fmt_profile,
                )
            )
    return artifacts


def _render_validation_report(report: ValidationReport) -> str:
    """生成稳定、紧凑且不包含违规产物正文的校验报告。"""
    payload = {
        "schema_version": "1.0",
        "status": "blocked" if report.blocked else ("warning" if report.has_warnings else "ok"),
    }
    payload.update(report.to_dict())
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _validated_generated_response(output: str, artifacts: List[Artifact]) -> List[TextContent]:
    """保持旧产物为第一段；warning 追加报告，critical 只返回报告。"""
    from .standards import get_python_module_whitelist

    report = validate_artifacts(artifacts, whitelist=get_python_module_whitelist())
    report_content = TextContent(type="text", text=_render_validation_report(report))
    if report.blocked:
        return [report_content]

    contents = [TextContent(type="text", text=output)]
    if report.has_warnings:
        contents.append(report_content)
    return contents


def _blocked_report(code: str, message: str, details: Optional[Dict[str, Any]] = None) -> List[TextContent]:
    """返回不携带候选产物的稳定阻断报告。"""
    issue = {
        "code": code,
        "severity": "critical",
        "message": message,
        "filename": "request",
        "line": 1,
        "column": 1,
        "detector": "request.contract",
    }
    if details:
        issue["details"] = details
    payload = {
        "schema_version": "1.0",
        "status": "blocked",
        "blocked": True,
        "has_warnings": False,
        "artifact_count": 0,
        "issue_count": 1,
        "artifacts": [],
        "issues": [issue],
    }
    return [TextContent(type="text", text=json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))]


def _entry_side(entry: Dict[str, Any]) -> str:
    """将结构化文档中的中英文端侧统一为工具契约值。"""
    value = str(entry.get("side", "")).strip().lower()
    if value in {"server", "服务端"}:
        return "server"
    if value in {"client", "客户端"}:
        return "client"
    return value


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
            return [TextContent(type="text", text=f"未找到与 '{query}' 相关的文档（{search_mode}模式）。\n\n提示：尝试更换关键词，或使用 search_api 工具精确搜索 API/事件。")]
        
        output = f"## 搜索结果: {query} ({len(results)} 个)\n\n"
        
        for i, result in enumerate(results, 1):
            output += f"{i}. **{result['title']}** `{result['filepath']}`\n"

            # 匹配项最多 2 个
            if fuzzy and result.get('matched_terms'):
                output += f"   匹配: {', '.join(result['matched_terms'][:2])}\n"

            # snippet 截短到 80 字符
            snippet = result.get('snippet', '')
            if len(snippet) > 80:
                snippet = snippet[:80] + "..."
            output += f"   {snippet}\n\n"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "get_api_detail":
        api_name = arguments.get("name", "")
        detail = docs_reader.get_api_detail(api_name)

        if not detail:
            output = f"未找到名为 `{api_name}` 的API或事件。请检查名称拼写。\n"
            output += "提示：可通过 api-index Resource 浏览完整索引，或用 search_api 模糊搜索。"
            return [TextContent(type="text", text=output)]

        # 支持同名多端API（如 GetPos 有服务端和客户端两个版本）
        entries = detail if isinstance(detail, list) else [detail]
        output = f"## `{api_name}` 详情\n\n"

        for entry in entries:
            side = entry.get("side", "")
            output += f"### {entry['name']} ({side})\n"
            output += f"- 类型: {entry['type']} | 分类: {entry.get('category', '无')}\n"
            output += "- 类路径: `{}` | 文档版本: {}\n".format(entry["class_path"], entry.get("sdk_version", CURRENT_TARGET_VERSION))
            output += f"- 描述: {entry['desc']}\n"

            if entry.get('params'):
                param_strs = []
                enum_notes = []
                for p in entry['params']:
                    pname = p.get('param_name', '')
                    ptype = p.get('param_type', '')
                    pcomment = p.get('param_comment', '')
                    param_strs.append(f"  - `{pname}`({ptype}){' — ' + pcomment if pcomment else ''}")
                    # 自动检测枚举引用并内联（覆盖全部 73 个枚举）
                    inline = _try_inline_enum(docs_reader, pcomment)
                    if inline:
                        enum_notes.append(inline)
                output += "- 参数:\n" + "\n".join(param_strs) + "\n"
                if enum_notes:
                    output += "- 枚举值:\n" + "\n".join(enum_notes) + "\n"

            ret = entry.get('return', {})
            if ret:
                rtype = ret.get('return_type', '')
                rcomment = ret.get('return_comment', '')
                if rtype:
                    output += f"- 返回: `{rtype}`{' — ' + rcomment if rcomment else ''}\n"

            remarks = entry.get("remarks") or []
            if remarks:
                output += "- 备注:\n" + "\n".join("  - {}".format(item) for item in remarks) + "\n"
            examples = entry.get("examples") or []
            if examples:
                output += "- 示例:\n" + "\n".join("```python\n{}\n```".format(item) for item in examples) + "\n"
            if entry.get("source_url"):
                output += "- 来源: {}\n".format(entry["source_url"])
            if entry.get("source_last_modified"):
                output += "- 来源更新时间: {}\n".format(entry["source_last_modified"])
            if entry.get("state"):
                output += "- 版本状态: {}\n".format(json.dumps(entry["state"], ensure_ascii=False, sort_keys=True))

            output += "\n"

        return [TextContent(type="text", text=output)]

    elif name == "search_api":
        query = arguments.get("query", "")
        entry_type = arguments.get("entry_type", "all")
        limit = arguments.get("limit", 5)
        results = docs_reader.search_api(query, limit=limit, entry_type=entry_type)
        
        type_label = {"api": "接口", "event": "事件", "all": "API/事件"}.get(entry_type, "API/事件")

        if not results:
            # 智能兜底：从查询提取token匹配相关分类，引导LLM用browse_api_category逐步发现
            tokens = docs_reader._tokenize(query)
            categories = docs_reader.get_api_categories()

            related_cats = []
            for cat_top, subs in categories.items():
                for token in tokens:
                    tl = token.lower()
                    if tl in cat_top.lower() or any(tl in s.lower() for s in subs if s):
                        total = sum(subs.values())
                        related_cats.append((cat_top, total, subs))
                        break
            related_cats.sort(key=lambda x: -x[1])

            output = f"## 未找到与 '{query}' 精确匹配的{type_label}\n\n"

            if related_cats:
                output += "### 相关分类（可用 `browse_api_category` 浏览）\n\n"
                for cat, count, subs in related_cats[:5]:
                    sub_list = ", ".join(s for s in sorted(subs.keys()) if s)[:50]
                    output += f"- **{cat}**（{count}个） — {sub_list}\n"
                output += "\n"

            output += "### 全部一级分类\n\n"
            sorted_cats = sorted(categories.items(), key=lambda x: -sum(x[1].values()))
            for cat, subs in sorted_cats[:12]:
                total = sum(subs.values())
                sub_list = ", ".join(s for s in sorted(subs.keys()) if s)[:40]
                output += f"- **{cat}**（{total}） — {sub_list}\n"

            output += "\n### 建议下一步\n\n"
            output += "1. 使用 `browse_api_category` 工具，传入上述分类名浏览详细列表\n"
            output += "2. 尝试用英文API名搜索（如 `SetPos`、`GetBlock`）\n"
            output += "3. 使用 `get_document_structure` 查看相关文档的章节目录\n"

            return [TextContent(type="text", text=output)]
        output = f"## {type_label}搜索结果: {query}\n\n"

        for i, r in enumerate(results, 1):
            # 紧凑参数格式 + 枚举自动内联（从 docs/枚举值/*.md 解析，非硬编码）
            params_parts = []
            inline_notes = []
            if r['params']:
                for p in r['params']:
                    pname = p['param_name']
                    ptype = p.get('param_type', '')
                    pdesc = p.get('param_comment', '')
                    params_parts.append(f"`{pname}`({ptype}) {pdesc}")
                    # 自动检测枚举引用并内联（覆盖全部 73 个枚举）
                    inline = _try_inline_enum(docs_reader, pdesc)
                    if inline:
                        inline_notes.append(inline)

            ret = r.get('return', {})
            ret_str = ret.get('return_type', '') if ret else ''

            output += f"### {i}. `{r['name']}` ({r['side']})\n"
            output += f"- 类型: {r['type']} | 分类: {r['category']}\n"
            output += f"- 描述: {r['desc']}\n"
            if params_parts:
                output += f"- 参数: {', '.join(params_parts)}\n"
                for note in inline_notes:
                    output += f"{note}\n"
            if ret_str:
                output += f"- 返回: {ret_str}\n"
            output += "\n"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "get_document":
        filepath = arguments.get("filepath", "")
        doc = docs_reader.get_document(filepath)

        if not doc:
            return [TextContent(type="text", text=f"文档 '{filepath}' 不存在。")]

        content = doc.content
        # 截断保护：超过 8000 字符时只返回目录 + 提示，避免灾难性上下文消耗
        if len(content) > 8000:
            structure = docs_reader.get_document_structure(filepath)
            if structure:
                toc = "\n".join(f"{'  ' * (s['level']-1)}- {s['title']}" for s in structure)
                return [TextContent(type="text", text=(
                    f"# {doc.title}\n\n"
                    f"⚠️ 文档较长（{len(content)}字符），已返回目录结构。"
                    f"请使用 get_document_section 获取具体章节内容。\n\n"
                    f"## 目录\n{toc}"
                ))]
        return [TextContent(type="text", text=f"# {doc.title}\n\n{content}")]
    
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

    elif name == "get_version_changes":
        from .standards import get_registry

        changes = get_registry().get_version_changes()
        section = arguments.get("section", "overview")
        if section == "overview":
            payload = {key: changes[key] for key in ("from_version", "to_version", "scope", "retrieved_at")}
            for kind in ("api", "event", "enum", "documents"):
                payload[kind] = {key: changes[kind][key] for key in ("before_count", "after_count")}
                payload[kind].update({op: len(changes[kind][op]) for op in ("added", "removed", "changed")})
            payload["release_notes"] = changes.get("release_notes", {}).get("summary", {})
            payload["caveats"] = changes.get("caveats", [])
        elif section == "repository_reconciliation":
            payload = changes.get(section, {})
        else:
            operation = arguments.get("operation", "all")
            offset, limit = arguments.get("offset", 0), arguments.get("limit", 20)
            if section not in {"api", "event", "enum", "documents", "release_notes"} or operation not in {"all", "added", "removed", "changed"}:
                return _blocked_report("VERSION_CHANGES_FILTER_INVALID", "未知差异分类或操作类型")
            if type(offset) is not int or type(limit) is not int or offset < 0 or not 1 <= limit <= 50:
                return _blocked_report("VERSION_CHANGES_PAGE_INVALID", "offset 必须非负，limit 必须为 1 到 50")
            if section == "release_notes":
                records = changes.get(section, {}).get("entries", [])
                if operation != "all":
                    accepted = {"added": {"新增"}, "removed": {"删除", "废弃"}, "changed": {"调整"}}[operation]
                    records = [entry for entry in records if entry["operation"] in accepted]
            else:
                records = [dict(entry, change=op) for op in ("added", "removed", "changed") if operation in {"all", op} for entry in changes[section][op]]
            query = str(arguments.get("query", "")).casefold()
            records = [record for record in records if not query or query in json.dumps(record, ensure_ascii=False).casefold()]
            selected = records[offset:offset + limit]
            if not arguments.get("include_details", False):
                fields = {"change", "name", "side", "path", "changed_fields", "source_url", "before_url", "after_url", "before_value", "after_value", "operation", "comment", "declared_operation", "historical_repository_entry"}
                selected = [{key: value for key, value in entry.items() if key in fields} for entry in selected]
            payload = {"section": section, "total": len(records), "offset": offset, "entries": selected, "next_offset": offset + limit if offset + limit < len(records) else None}
        return [TextContent(type="text", text=json.dumps(payload, ensure_ascii=False, indent=2))]

    elif name == "get_development_guidance":
        from .guidance import render_guidance_json

        goal = str(arguments.get("goal", "")).strip()
        if not goal:
            return _blocked_report("GUIDANCE_GOAL_REQUIRED", "goal 必填且不能为空")

        domain = arguments.get("domain", "auto")
        side = arguments.get("side", "auto")
        target_version = arguments.get("target_version", "current")
        max_rules = arguments.get("max_rules", 8)
        try:
            guidance = render_guidance_json(
                request=goal,
                version=target_version,
                domains=None if domain == "auto" else [domain],
                sides=None if side == "auto" else [side],
                limit=max_rules,
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GUIDANCE_REQUEST_INVALID", str(exc))
        return [TextContent(type="text", text=guidance)]
    
    # 代码与组件包生成工具
    elif name == "generate_mod_project":
        mod_id = arguments.get("mod_id")
        try:
            files = generate_mod_project(
                mod_name=arguments.get("mod_name"),
                mod_id=mod_id,
                author=arguments.get("author", "Author"),
                description=arguments.get("description", "A Minecraft mod"),
                version=arguments.get("version", "1.0.0"),
                min_engine_version=arguments.get("min_engine_version", [1, 18, 0]),
                behavior_pack_dir=arguments.get("behavior_pack_dir"),
                resource_pack_dir=arguments.get("resource_pack_dir"),
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        clean_mod_id = str(mod_id).strip()
        project_root = get_project_folder_name(clean_mod_id)
        notes = [
            "完整双包结构：同时包含行为包与资源包的最新 `manifest.json`（`format_version: 2`，行为包 `dependencies` 已绑定资源包 `header.uuid`）。",
            "中国版必选目录已就绪：`entities/.gitkeep` 保留空实体目录（避免上传错误码 24），`textures/` 已初始化贴图注册表。",
            "Python 脚本包 `{}` 直接位于行为包根目录下，通过 `modConfig.py` 统一管理双端系统名与跨端事件名。".format(project_root),
        ]
        output = render_bundle_markdown(
            "生成的 Mod 双包项目骨架 ({})".format(clean_mod_id),
            files,
            notes=notes,
        )
        artifacts = _artifacts_from_files(files, project_modules=(project_root, clean_mod_id))
        return _validated_generated_response(output, artifacts)

    elif name == "generate_manifest_json":
        try:
            files = generate_manifest_json(
                pack_name=arguments.get("pack_name", ""),
                description=arguments.get("description", ""),
                pack_type=arguments.get("pack_type", "both"),
                version=arguments.get("version", "1.0.0"),
                min_engine_version=arguments.get("min_engine_version", [1, 18, 0]),
                behavior_pack_dir=arguments.get("behavior_pack_dir"),
                resource_pack_dir=arguments.get("resource_pack_dir"),
                resource_pack_uuid=arguments.get("resource_pack_uuid"),
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        output = render_bundle_markdown(
            "生成的组件包清单 (manifest.json)",
            files,
            notes=[
                "严格使用最新标准 `manifest.json` 与 `format_version: 2`（避免 3.8+ 自定义生物蛋贴图异常）。",
                "所有 `header.uuid` 与 `modules[].uuid` 均已生成独立 UUID4，后续版本升级时请仅递增 `version` 而不要改动 UUID。",
            ],
        )
        return _validated_generated_response(output, _artifacts_from_files(files))

    elif name == "generate_ui_json":
        mod_id = arguments.get("mod_id", "mymod")
        try:
            bundle = generate_ui_json(
                ui_namespace=arguments.get("ui_namespace", ""),
                title=arguments.get("title", "自定义界面"),
                is_hud=bool(arguments.get("is_hud", False)),
                include_python=bool(arguments.get("include_python", True)),
                mod_id=mod_id,
                behavior_pack_dir=arguments.get("behavior_pack_dir"),
                resource_pack_dir=arguments.get("resource_pack_dir"),
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        clean_mod_id = str(mod_id).strip()
        project_root = get_project_folder_name(clean_mod_id)
        reg_snippet = (
            "```python\n"
            "# 在客户端系统的 UiInitFinished 事件回调中先完成注册：\n"
            "clientApi.RegisterUI('{mod_id}', '{ui_ns}', '{proj}.ui.{cls}.{cls}', '{ui_def}')\n"
            "# 注册成功后再按模式创建：\n"
            "clientApi.CreateUI('{mod_id}', '{ui_ns}', {{'isHud': {hud_flag}}})\n"
            "```"
        ).format(
            mod_id=clean_mod_id,
            ui_ns=arguments.get("ui_namespace", "").strip().lower(),
            proj=project_root,
            cls=bundle["screen_class"],
            ui_def=bundle["ui_screen_def"],
            hud_flag=1 if arguments.get("is_hud", False) else 0,
        )
        output = render_bundle_markdown(
            "自定义 JSON UI 配套文件: {}".format(bundle["ui_screen_def"]),
            bundle["files"],
            notes=[
                "遵循 `UI-LIFE-001` / `UI-HUD-001`：必须先 `RegisterUI` 再 `CreateUI`/`PushScreen`，HUD 层级需在 `CreateUI` 时通过 `isHud` 指定。",
                _SHARED_MERGE_NOTE,
            ],
            extra_sections=[("客户端系统注册调用示例", reg_snippet)],
        )
        artifacts = _artifacts_from_files(bundle["files"], project_modules=(project_root, clean_mod_id))
        return _validated_generated_response(output, artifacts)

    elif name == "generate_server_system":
        code = generate_server_system(
            mod_name=arguments.get("mod_name", "MyMod"),
            class_name=arguments.get("class_name", "MyMod"),
        )
        output = f"## 服务端系统代码\n\n```python\n{code}\n```"
        return _validated_generated_response(output, [Artifact(code, "serverSystem.py", "python", "server", CURRENT_TARGET_VERSION)])

    elif name == "generate_client_system":
        code = generate_client_system(
            mod_name=arguments.get("mod_name", "MyMod"),
            class_name=arguments.get("class_name", "MyMod"),
        )
        output = f"## 客户端系统代码\n\n```python\n{code}\n```"
        return _validated_generated_response(output, [Artifact(code, "clientSystem.py", "python", "client", CURRENT_TARGET_VERSION)])

    elif name == "generate_event_listener":
        event_name = arguments.get("event_name")
        event_kind = arguments.get("event_kind", "official")
        requested_side = arguments.get("side", "auto")
        event_description = arguments.get("event_description", "事件处理")

        if event_kind not in {"official", "custom"}:
            return _blocked_report("EVENT_KIND_INVALID", "event_kind 只能是 official 或 custom")
        if requested_side not in {"auto", "client", "server"}:
            return _blocked_report("EVENT_SIDE_INVALID", "side 只能是 auto、client 或 server")

        if event_kind == "custom":
            params = arguments.get("params")
            if not isinstance(params, dict) or not params or any(not str(value).strip() for value in params.values()):
                return _blocked_report(
                    "CUSTOM_EVENT_PARAMS_REQUIRED",
                    "自定义事件必须提供非空 params 参数说明",
                    {"event_name": event_name},
                )
            if requested_side == "auto":
                return _blocked_report("CUSTOM_EVENT_SIDE_REQUIRED", "自定义事件必须显式选择 client 或 server")
            selected_side = requested_side
        else:
            detail = docs_reader.get_api_detail(event_name)
            entries = detail if isinstance(detail, list) else ([detail] if detail else [])
            entries = [entry for entry in entries if entry.get("type") == "event"]
            if requested_side != "auto":
                entries = [entry for entry in entries if _entry_side(entry) == requested_side]
            if not entries:
                return _blocked_report(
                    "OFFICIAL_EVENT_NOT_FOUND",
                    "结构化官方文档中未找到匹配的事件与端侧，已拒绝猜测参数",
                    {"event_name": event_name, "side": requested_side},
                )
            sides = sorted({_entry_side(entry) for entry in entries})
            if requested_side == "auto" and len(sides) != 1:
                return _blocked_report(
                    "OFFICIAL_EVENT_SIDE_AMBIGUOUS",
                    "该官方事件存在多个端侧版本，必须显式选择 side",
                    {"event_name": event_name, "available_sides": sides},
                )
            entry = entries[0]
            selected_side = _entry_side(entry)
            if selected_side not in {"server", "client"}:
                return _blocked_report("OFFICIAL_EVENT_SIDE_UNSUPPORTED", "该事件属于独立服务器环境，请按官方环境接入", {"side": entry.get("side")})
            event_name = entry["name"]
            params = {
                param.get("param_name", ""): "{}{}".format(
                    param.get("param_type", ""),
                    " - " + param.get("param_comment", "") if param.get("param_comment") else "",
                )
                for param in entry.get("params", [])
                if param.get("param_name")
            }
            if event_description == "事件处理":
                event_description = entry.get("desc") or event_description

        code = generate_event_listener(
            event_name=event_name,
            event_description=event_description,
            params=params,
            side=selected_side,
        )
        output = f"## 事件监听器代码\n\n```python\n{code}\n```"
        return _validated_generated_response(output, [Artifact(code, "event_listener.py", "python", selected_side, CURRENT_TARGET_VERSION)])

    elif name == "generate_custom_command":
        try:
            code = generate_custom_command(
                command_name=arguments.get("command_name", "")
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))
        output = f"## 自定义命令代码\n\n```python\n{code}\n```"
        return _validated_generated_response(output, [Artifact(code, "custom_command.py", "python", "server", CURRENT_TARGET_VERSION)])

    elif name == "generate_custom_item":
        namespace = arguments.get("namespace", "mymod")
        item_id = arguments.get("item_id", "")
        try:
            bundle = generate_custom_item(
                item_id=item_id,
                namespace=namespace,
                display_name=arguments.get("display_name", "自定义物品"),
                max_stack=arguments.get("max_stack", 64),
                hand_equipped=bool(arguments.get("hand_equipped", False)),
                behavior_pack_dir=arguments.get("behavior_pack_dir"),
                resource_pack_dir=arguments.get("resource_pack_dir"),
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        clean_ns = str(namespace).strip()
        project_root = get_project_folder_name(clean_ns)
        output = render_bundle_markdown(
            "自定义物品完整开发包: {}:{}".format(clean_ns, str(item_id).strip().lower()),
            bundle["files"],
            notes=[
                "已同步生成服务端事件脚本、行为包 `netease_items_beh`、资源包 `netease_items_res`、`textures/item_texture.json` 及中文语言文件。",
                "请将贴图 PNG 放置于 `resource_pack/textures/items/{}.png`。".format(str(item_id).strip().lower()),
                _SHARED_MERGE_NOTE,
            ],
        )
        return _validated_generated_response(
            output,
            _artifacts_from_files(bundle["files"], project_modules=(project_root, clean_ns)),
        )

    elif name == "generate_custom_block":
        namespace = arguments.get("namespace", "mymod")
        block_id = arguments.get("block_id", "")
        try:
            bundle = generate_custom_block(
                block_id=block_id,
                namespace=namespace,
                destroy_time=arguments.get("destroy_time", 1.0),
                explosion_resistance=arguments.get("explosion_resistance", 1.0),
                display_name=arguments.get("display_name", "自定义方块"),
                behavior_pack_dir=arguments.get("behavior_pack_dir"),
                resource_pack_dir=arguments.get("resource_pack_dir"),
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        clean_ns = str(namespace).strip()
        project_root = get_project_folder_name(clean_ns)
        output = render_bundle_markdown(
            "自定义方块完整开发包: {}:{}".format(clean_ns, str(block_id).strip().lower()),
            bundle["files"],
            notes=[
                "采用现代推荐档 `modern_1_19_20`（`1.19.20`），并同步生成资源包 `blocks.json`、`textures/terrain_texture.json` 与语言文件。",
                "请将方块贴图 PNG 放置于 `resource_pack/textures/blocks/{}.png`。".format(str(block_id).strip().lower()),
                _SHARED_MERGE_NOTE,
            ],
        )
        return _validated_generated_response(
            output,
            _artifacts_from_files(
                bundle["files"],
                project_modules=(project_root, clean_ns),
                block_format_profile="modern_1_19_20",
            ),
        )

    # ============================================================
    # 数据驱动 JSON 生成工具处理
    # ============================================================

    elif name == "generate_item_json":
        namespace = arguments.get("namespace", "")
        item_id = arguments.get("item_id", "")
        try:
            bundle = generate_item_json(
                namespace=namespace,
                item_id=item_id,
                category=arguments.get("category", "items"),
                max_stack_size=arguments.get("max_stack_size", 64),
                components=arguments.get("components"),
                display_name=arguments.get("display_name", "自定义物品"),
                behavior_pack_dir=arguments.get("behavior_pack_dir"),
                resource_pack_dir=arguments.get("resource_pack_dir"),
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        output = render_bundle_markdown(
            "自定义物品 JSON 配套集: {}:{}".format(str(namespace).strip(), str(item_id).strip().lower()),
            bundle["files"],
            notes=[
                "请将物品图标贴图放置于 `resource_pack/textures/items/{}.png`。".format(str(item_id).strip().lower()),
                _SHARED_MERGE_NOTE,
            ],
        )
        return _validated_generated_response(output, _artifacts_from_files(bundle["files"]))

    elif name == "generate_block_json":
        namespace = arguments.get("namespace", "")
        block_id = arguments.get("block_id", "")
        format_profile = arguments.get("format_profile", "modern_1_19_20")
        try:
            bundle = generate_block_json(
                namespace=namespace,
                block_id=block_id,
                destroy_time=arguments.get("destroy_time", 1.5),
                explosion_resistance=arguments.get("explosion_resistance", 10.0),
                light_emission=arguments.get("light_emission", 0),
                light_dampening=arguments.get("light_dampening", 15),
                map_color=arguments.get("map_color", "#FFFFFF"),
                category=arguments.get("category", "Nature"),
                register_to_menu=arguments.get("register_to_menu", True),
                sound=arguments.get("sound", "stone"),
                display_name=arguments.get("display_name", "自定义方块"),
                components=arguments.get("components"),
                format_profile=format_profile,
                behavior_pack_dir=arguments.get("behavior_pack_dir"),
                resource_pack_dir=arguments.get("resource_pack_dir"),
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        output = render_bundle_markdown(
            "自定义方块 JSON 配套集: {}:{} ({})".format(
                str(namespace).strip(), str(block_id).strip().lower(), format_profile
            ),
            bundle["files"],
            notes=[
                "已同步生成资源包 `blocks.json` 与 `textures/terrain_texture.json`，请将贴图放置于 `resource_pack/textures/blocks/{}.png`。".format(
                    str(block_id).strip().lower()
                ),
                _SHARED_MERGE_NOTE,
            ],
        )
        return _validated_generated_response(
            output,
            _artifacts_from_files(bundle["files"], block_format_profile=format_profile),
        )

    elif name == "generate_recipe_json":
        recipe_type = arguments.get("recipe_type")
        namespace = arguments.get("namespace", "")
        recipe_id = arguments.get("recipe_id", "")
        if recipe_type not in {"shaped", "shapeless", "furnace"}:
            return _blocked_report("RECIPE_TYPE_INVALID", "未知的配方类型: {!r}".format(recipe_type))

        try:
            bundle = generate_recipe_json(
                recipe_type=recipe_type,
                namespace=namespace,
                recipe_id=recipe_id,
                behavior_pack_dir=arguments.get("behavior_pack_dir"),
                pattern=arguments.get("pattern", ["   ", "   ", "   "]),
                keys=arguments.get("keys", {}),
                ingredients=arguments.get("ingredients", []),
                input_item=arguments.get("input_item", "minecraft:air"),
                output_item=arguments.get("output_item", "minecraft:air"),
                result_item=arguments.get("result_item", "minecraft:air"),
                result_count=arguments.get("result_count", 1),
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        output = render_bundle_markdown(
            "{} 配方 JSON: {}:{}".format(
                recipe_type.capitalize(), str(namespace).strip(), str(recipe_id).strip().lower()
            ),
            bundle["files"],
            notes=["网易版合成配方目录固定为行为包下的 `netease_recipes/`（而非国际版的 `recipes/`）。"],
        )
        return _validated_generated_response(output, _artifacts_from_files(bundle["files"]))

    elif name == "generate_entity_json":
        namespace = arguments.get("namespace", "")
        entity_id = arguments.get("entity_id", "")
        try:
            bundle = generate_entity_json(
                namespace=namespace,
                entity_id=entity_id,
                health=arguments.get("health", 20),
                movement_speed=arguments.get("movement_speed", 0.25),
                collision_width=arguments.get("collision_width", 0.6),
                collision_height=arguments.get("collision_height", 1.8),
                family=arguments.get("family"),
                runtime_identifier=arguments.get("runtime_identifier"),
                components=arguments.get("components"),
                preset=arguments.get("preset"),
                spawn_egg_base_color=arguments.get("spawn_egg_base_color", "#FFFFFF"),
                spawn_egg_overlay_color=arguments.get("spawn_egg_overlay_color", "#000000"),
                display_name=arguments.get("display_name", "自定义生物"),
                behavior_pack_dir=arguments.get("behavior_pack_dir"),
                resource_pack_dir=arguments.get("resource_pack_dir"),
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        output = render_bundle_markdown(
            "自定义实体 JSON 配套集: {}:{}".format(str(namespace).strip(), str(entity_id).strip().lower()),
            bundle["files"],
            notes=[
                "已同步生成 `models/entity/{}_{}.geo.json` 基础几何体模型，避免客户端缺少几何体报错；请将实体贴图放置于 `resource_pack/textures/entity/{}.png`。".format(
                    str(namespace).strip(), str(entity_id).strip().lower(), str(entity_id).strip().lower()
                ),
                _SHARED_MERGE_NOTE,
            ],
        )
        return _validated_generated_response(output, _artifacts_from_files(bundle["files"]))

    elif name == "generate_loot_table_json":
        try:
            bundle = generate_loot_table_json(
                pools=arguments.get("pools", []),
                table_name=arguments.get("table_name", "custom_loot"),
                behavior_pack_dir=arguments.get("behavior_pack_dir"),
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        output = render_bundle_markdown("战利品表 JSON", bundle["files"])
        return _validated_generated_response(output, _artifacts_from_files(bundle["files"]))

    elif name == "generate_spawn_rules_json":
        namespace = arguments.get("namespace", "")
        entity_id = arguments.get("entity_id", "")
        try:
            bundle = generate_spawn_rules_json(
                namespace=namespace,
                entity_id=entity_id,
                population_control=arguments.get("population_control", "animal"),
                spawn_weight=arguments.get("spawn_weight", 8),
                min_size=arguments.get("min_size", 2),
                max_size=arguments.get("max_size", 4),
                behavior_pack_dir=arguments.get("behavior_pack_dir"),
            )
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        output = render_bundle_markdown(
            "实体生成规则 JSON: {}:{}".format(str(namespace).strip(), str(entity_id).strip().lower()),
            bundle["files"],
        )
        return _validated_generated_response(output, _artifacts_from_files(bundle["files"]))

    # ============================================================
    # 高级物品生成工具处理（统一处理 9 种网易 1.10 物品类型）
    # ============================================================

    elif name in ADVANCED_ITEM_TOOLS:
        item_type, display_label = ADVANCED_ITEM_TOOLS[name]
        namespace = arguments.get("namespace", "")
        item_id = arguments.get("item_id", "")
        kwargs = {k: v for k, v in arguments.items() if k not in ("namespace", "item_id")}
        try:
            bundle = generate_typed_item_json(item_type, namespace, item_id, **kwargs)
        except (TypeError, ValueError) as exc:
            return _blocked_report("GENERATOR_INPUT_INVALID", str(exc))

        if item_type == "armor":
            slot_spec = ARMOR_SLOT_SPECS.get(str(arguments.get("slot", "slot.armor.chest")), {})
            display_label = "自定义{}".format(slot_spec.get("label", "盔甲"))

        notes = list(bundle.get("notes") or [])
        notes.append(_SHARED_MERGE_NOTE)
        output = render_bundle_markdown(
            "{}: {}:{}".format(display_label, str(namespace).strip(), str(item_id).strip().lower()),
            bundle["files"],
            notes=notes,
        )
        return _validated_generated_response(output, _artifacts_from_files(bundle["files"]))

    # 代码审查工具
    elif name == "review_code":
        from .standards import get_python_module_whitelist, get_version_profile

        code = arguments.get("code", "")
        filename = arguments.get("filename", "unknown.py")
        artifact_type = arguments.get("artifact_type", "auto")
        side = arguments.get("side", "auto")
        target_version = arguments.get("target_version", "current")
        project_modules = arguments.get("project_modules", [])
        if artifact_type not in {"auto", "python", "json", "json_ui", "item", "block", "manifest_json"}:
            return _blocked_report("ARTIFACT_TYPE_INVALID", "artifact_type 不受支持：{}".format(artifact_type))
        if side not in {"auto", "client", "server", "common", "cross_side"}:
            return _blocked_report("SIDE_INVALID", "side 不受支持：{}".format(side))
        try:
            target_profile = get_version_profile(str(target_version))
        except KeyError:
            return _blocked_report(
                "TARGET_VERSION_UNSUPPORTED",
                "不支持的目标版本：{}".format(target_version),
            )
        if not isinstance(project_modules, list) or any(not isinstance(module, str) for module in project_modules):
            return _blocked_report("PROJECT_MODULES_INVALID", "project_modules 必须是字符串数组")

        artifact = Artifact(
            content=code,
            filename=filename,
            artifact_type=artifact_type,
            side=side,
            target_version=target_profile["version"],
            project_modules=tuple(project_modules),
        )
        report = validate_artifacts([artifact], whitelist=get_python_module_whitelist())
        return [TextContent(type="text", text=_render_validation_report(report))]
    
    # ============================================================
    # 分类浏览工具（搜索兜底）
    # ============================================================

    elif name == "browse_api_category":
        category = arguments.get("category", "")
        entry_type = arguments.get("entry_type", "all")

        if not category:
            # 无参数：返回完整分类目录树
            categories = docs_reader.get_api_categories()
            output = "## API/事件分类目录\n\n"
            for cat, subs in sorted(categories.items(), key=lambda x: -sum(x[1].values())):
                total = sum(subs.values())
                output += f"### {cat}（{total}）\n"
                for sub, count in sorted(subs.items(), key=lambda x: -x[1]):
                    if sub:
                        output += f"- {sub}（{count}）\n"
                output += "\n"
            return [TextContent(type="text", text=output)]

        items = docs_reader.browse_api_category(category, entry_type)

        if not items:
            return [TextContent(type="text", text=f"分类 '{category}' 下没有条目。\n\n使用 `browse_api_category` 不传 category 参数可查看所有分类目录。")]

        type_label = {"api": "接口", "event": "事件", "all": "API/事件"}.get(entry_type, "API/事件")
        output = f"## {category} 分类下的{type_label}（共{len(items)}个）\n\n"
        for item in items:
            output += f"- `{item['name']}` ({item['side']}) — {item['desc']}\n"

        if len(items) > 30:
            output += f"\n*共{len(items)}个，建议配合 search_api 用具体关键词进一步筛选*\n"

        return [TextContent(type="text", text=output)]

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
            if cat_data.get("projection") == "standard_registry":
                output += "- 规范来源：`standard/registry`（目标版本 {}）\n".format(
                    cat_data.get("target_version", CURRENT_TARGET_VERSION)
                )
            elif cat_data.get("projection") == "legacy_3.8_compatibility":
                output += "- 兼容边界：保留 3.8 历史迁移入口；当前默认目标为 {}。\n".format(CURRENT_TARGET_VERSION)
            if cat_data.get("source_boundary"):
                output += "- 证据边界：{}\n".format(cat_data["source_boundary"])
            for rule in cat_data.get('rules', []):
                output += f"- {rule}\n"
            output += "\n"
        
        return [TextContent(type="text", text=output)]
    
    elif name == "get_architecture_pattern":
        pattern_name = arguments.get("pattern_name", "")
        result = get_architecture_pattern(pattern_name)
        pattern_files = get_architecture_pattern_artifacts(pattern_name) if pattern_name else {}
        if not pattern_files:
            return [TextContent(type="text", text=result)]
        artifacts = [
            Artifact(code, filename, "python", "auto", CURRENT_TARGET_VERSION)
            for filename, code in pattern_files.items()
        ]
        return _validated_generated_response(result, artifacts)

    else:
        return [TextContent(type="text", text=f"未知的工具: {name}")]


def _perform_code_review(code: str, filename: str) -> str:
    """兼容旧内部调用，实际委托给统一结构感知校验器。"""
    from .standards import get_python_module_whitelist

    artifact_type = "json" if filename.lower().endswith(".json") else "python"
    report = validate_artifacts(
        [Artifact(code, filename, artifact_type, "auto", CURRENT_TARGET_VERSION)],
        whitelist=get_python_module_whitelist(),
    )
    return _render_validation_report(report)

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
                        text=f"""以 {MODSDK_LABEL} 为目标处理开发请求（当前状态：{_TARGET_PROFILE["status"]}）：
1. 调用 get_development_guidance 取得目标、端侧和产物规则。
2. 涉及 API/事件时用 search_api → get_api_detail 查证；需要正文再用 search_docs/get_document_section。
3. 生成代码或 JSON，并读取随附校验报告。
4. 修复 critical；对 warning 说明证据边界与人工验证项。不得猜测签名。"""
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

按固定流程完成：get_development_guidance → search_api/get_api_detail 查证事件与接口 → generate_mod_project 及所需生成器 → 阅读校验报告并修复 critical。最后给出本地验证步骤。"""
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

先调用 get_development_guidance；再用 search_api/get_api_detail 或 search_docs/get_document_section 查证相关行为；对显式代码调用 review_code；最后给出证据、修复和本地复现步骤。"""
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

按 get_development_guidance → API/事件详情查证 → review_code 的流程审查。critical 给出可验证的修复；warning 明确上下文与证据等级，不把工程建议描述为官方硬规则。"""
                    )
                )
            ]
        )
    
    else:
        raise ValueError(f"未知的提示词: {name}")


# ============================================================================
# 主函数
# ============================================================================

def _configure_diagnostics() -> None:
    """让重定向的诊断流稳定使用 UTF-8，不触碰 MCP 协议 stdout。"""
    reconfigure = getattr(sys.stderr, "reconfigure", None)
    if callable(reconfigure):
        reconfigure(encoding="utf-8", errors="backslashreplace")


def _initialize_runtime():
    """先校验核心注册表，再加载离线文档；任何损坏都会终止启动。"""
    from .standards import get_registry

    registry = get_registry()
    docs_reader = get_docs_reader()
    return registry, docs_reader


def _health_payload() -> Dict[str, Any]:
    """构造可验证版本、规则和快照状态的 SSE 健康信息。"""
    from .standards import get_python_module_whitelist_snapshot, get_registry

    registry = get_registry()
    profile = registry.get_version_profile(registry.manifest["default_version"])
    snapshot = get_python_module_whitelist_snapshot()
    return {
        "status": "ok",
        "server": "netease-modsdk-mcp",
        "modsdk_version": profile["version"],
        "bedrock_version": profile["bedrock_version"],
        "rule_count": len(registry.rules),
        "detector_count": len(get_registered_detectors()),
        "document_count": len(get_docs_reader().list_documents()),
        "snapshot_time": snapshot["retrieved_at"],
        "runtime_evidence_status": profile["runtime_evidence_status"],
    }


async def main_stdio():
    """使用 stdio 模式运行（本地部署）"""
    _configure_diagnostics()
    _initialize_runtime()
    
    # 启动 stdio 服务器
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


def create_sse_app():
    """创建 SSE 模式使用的 Starlette 应用。"""
    from mcp.server.sse import SseServerTransport
    from starlette.applications import Starlette
    from starlette.routing import Mount, Route
    from starlette.responses import JSONResponse, Response
    
    _configure_diagnostics()
    _initialize_runtime()
    
    # 创建 SSE transport
    sse = SseServerTransport("/messages/")
    
    async def handle_sse(request):
        async with sse.connect_sse(
            request.scope, request.receive, request._send
        ) as streams:
            await server.run(
                streams[0],
                streams[1],
                server.create_initialization_options()
            )
        return Response()
    
    async def health_check(request):
        return JSONResponse(_health_payload())
    
    return Starlette(
        debug=True,
        routes=[
            Route("/sse", endpoint=handle_sse, methods=["GET"]),
            Mount("/messages/", app=sse.handle_post_message),
            Route("/health", endpoint=health_check),
        ],
    )


async def main_sse(host: str = "0.0.0.0", port: int = 8000):
    """使用 SSE 模式运行（远程部署）"""
    import uvicorn

    app = create_sse_app()
    
    print(f"MCP Server (SSE) 启动在 http://{host}:{port}", file=sys.stderr)
    print(f"- SSE 端点: http://{host}:{port}/sse", file=sys.stderr)
    print(f"- 消息端点: http://{host}:{port}/messages/", file=sys.stderr)
    print(f"- 健康检查: http://{host}:{port}/health", file=sys.stderr)
    
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
        # SSE 模式：python -m modsdk_mcp --sse
        run_sse()
    else:
        # 默认 stdio 模式
        run()
