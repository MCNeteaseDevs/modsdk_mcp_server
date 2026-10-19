# 🎮 NetEase ModSDK MCP Server

> **Model Context Protocol Server for 我的世界中国版（网易）ModSDK 开发**

为 AI 编程助手提供 ModSDK 3.10 Beta / BE 1.21.130 的**版本化开发指导、官方文档检索、产物生成与统一校验**。运行时完全离线，只读取仓库内快照。

截至 **2026-10-19**，官方 3.10 文档仍位于 Beta 频道；稳定版计划 2026-10-28 发布，全渠道更新计划 2026-10-30。3.9 历史规则继续保留，API/事件检索使用当前 3.10 完整快照。

[完整调查与迁移说明](docs/更新信息/3.10-迁移说明.md) · [全部机器可读差异](standard/registry/snapshots/modsdk-3.9-to-3.10.json) · [逐页来源与 SHA-256](standard/registry/snapshots/official-docs.json)

官方日志明确新增 **79 个接口条目、5 个事件**。两版公开快照另有索引补录与分类迁移，不能把全部索引新增当作首次引入；完整区别可用 `get_version_changes` 查询。

---

## ✨ 核心能力

| 能力 | 说明 |
|------|------|
| 🔍 **智能文档检索** | 模糊搜索、驼峰分词、中文搜索，覆盖 API 接口 & 事件文档 |
| 📝 **代码生成** | 自动生成符合网易规范的 Mod 项目、Server/Client System、自定义物品/方块/实体 |
| 🔧 **工具 & 武器生成** | 一键生成剑、镐、斧、锹、锄、弓、盔甲、食物、可投掷物品 JSON |
| 📋 **配方 & 战利品表** | 生成有序/无序合成配方、熔炉配方、战利品表、生成规则 |
| 🔬 **代码审查** | 检测 Python 2.7 兼容性、客户端/服务端混用、性能反模式 |
| 🧭 **版本化指导** | 按目标、领域和端侧选择规则，并返回来源等级与当前版本证据边界 |
| 📚 **组件百科** | 查询物品/方块/实体/网易特有组件的用法和配置 |
| ⚡ **最佳实践** | 从版本化注册表投影官方规则、MCP 策略与带边界的工程建议 |

---

## 🚀 快速开始

### 前置要求

- **Python ≥ 3.10**
- **pip**（Python 包管理器）

### 1. 安装依赖

```bash
cd "<PROJECT_ROOT>"
pip install -r requirements.txt
```

### 2. 选择你的 AI 客户端进行配置

> **通用说明**：所有客户端统一使用 `start_mcp.py` 绝对路径启动，无需 `cwd` 参数，兼容性最好。
> 请将下方示例中的 `<PROJECT_ROOT>` 替换为你本机的项目根目录。

<details>
<summary><b>🟢 Claude Desktop（推荐）</b></summary>

编辑配置文件：
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "modsdk-mcp-server": {
      "command": "python",
      "args": ["<PROJECT_ROOT>/start_mcp.py"]
    }
  }
}
```

保存后重启 Claude Desktop。
</details>

<details>
<summary><b>🟣 Claude Code（CLI）</b></summary>

Claude Code 不支持 `cwd` 参数，使用 `start_mcp.py` 绝对路径即可：

```bash
claude mcp add "modsdk-mcp-server" -- python "<PROJECT_ROOT>/start_mcp.py"
```

或手动编辑 `~/.claude/settings.json`：

```json
{
  "mcpServers": {
    "modsdk-mcp-server": {
      "command": "python",
      "args": ["<PROJECT_ROOT>/start_mcp.py"]
    }
  }
}
```
</details>

<details>
<summary><b>🔵 Cursor / VS Code</b></summary>

在项目根目录创建 `.cursor/mcp.json`（Cursor）或 `.vscode/mcp.json`（VS Code）：

```json
{
  "servers": {
    "modsdk-mcp-server": {
      "command": "python",
      "args": ["<PROJECT_ROOT>/start_mcp.py"]
    }
  }
}
```
> ⚠️ **常见问题（VS Code / Cursor）**
>
> 如果在 VS Code 或 Cursor 中启动 MCP 时出现以下错误：
>
> ```
> Error: tool parameters array type must have items
> ```
>
> **原因：**
>
> MCP 工具的参数 schema 中，某些字段声明为 `"type": "array"`，但没有提供 `"items"` 字段。
>
> 根据 JSON Schema 规范，所有数组类型必须定义 `"items"`，否则在严格校验环境（如 VS Code / Cursor）中会报错。
>
> **解决方法：**
>
> 修改对应工具的参数定义，例如：
>
> ❌ 错误写法：
> ```json
> {
>   "type": "array"
> }
> ```
>
> ✅ 正确写法：
> ```json
> {
>   "type": "array",
>   "items": {
>     "type": "object"
>   }
> }
> ```

</details>


<details>
<summary><b>🔴 SSE 模式（远程 / Docker）</b></summary>

启动 SSE 服务：

```bash
python "<PROJECT_ROOT>/start_mcp.py" --sse
# 默认监听 http://0.0.0.0:8000
```

在客户端中配置：

```json
{
  "mcpServers": {
    "modsdk-mcp-server": {
      "transport": "sse",
      "url": "http://localhost:8000/sse"
    }
  }
}
```
</details>

### 3. 验证连接

在 AI 助手中输入以下测试指令：

```
搜索 GetEngineCompFactory 的用法
```

如果返回了 API 文档内容，说明 MCP Server 已成功连接。

---

## 📖 MCP 工具一览

### 文档查询

| 工具 | 描述 |
|------|------|
| `search_docs` | 搜索文档（支持模糊匹配、驼峰分词、中文） |
| `search_api` | 搜索结构化 API/事件索引 |
| `get_api_detail` | 读取同名多端 API/事件的签名、备注、示例和来源元数据 |
| `get_document` | 获取指定文档完整内容 |
| `get_document_section` | 获取文档指定章节 |
| `get_document_structure` | 获取文档目录结构 |
| `list_documents` | 列出所有可用文档 |
| `reload_documents` | 重新加载文档索引 |
| `get_version_changes` | 查询接口、事件、枚举、正文及发布日志差异，支持筛选和分页 |
| `get_development_guidance` | 按目标、领域、端侧和版本返回最相关规则与验证建议 |

### 代码生成

| 工具 | 描述 |
|------|------|
| `generate_mod_project` | 生成完整 Mod 项目模板（含入口、服务端、客户端） |
| `generate_server_system` | 生成服务端系统代码 |
| `generate_client_system` | 生成客户端系统代码 |
| `generate_event_listener` | 生成事件监听器代码 |
| `generate_custom_command` | 生成自定义命令代码 |
| `generate_custom_item` | 生成自定义物品代码和 JSON |
| `generate_custom_block` | 生成自定义方块代码和 JSON |

### JSON 生成

| 工具 | 描述 |
|------|------|
| `generate_item_json` | 生成物品 JSON（行为包 + 资源包） |
| `generate_block_json` | 生成方块 JSON |
| `generate_recipe_json` | 生成合成配方 JSON（有序/无序/熔炉） |
| `generate_entity_json` | 生成实体 JSON（行为包 + 资源包） |
| `generate_loot_table_json` | 生成战利品表 JSON |
| `generate_spawn_rules_json` | 生成生成规则 JSON |

### 一键生成工具 & 武器

| 工具 | 描述 |
|------|------|
| `generate_sword_json` | 自定义剑（伤害、耐久、附魔、修复） |
| `generate_pickaxe_json` | 自定义镐（挖掘速度、耐久） |
| `generate_axe_json` | 自定义斧（伤害、挖掘速度） |
| `generate_shovel_json` | 自定义锹 |
| `generate_hoe_json` | 自定义锄 |
| `generate_bow_json` | 自定义弓（蓄力时间、耐久） |
| `generate_food_json` | 自定义食物（饥饿值、饱和度、药水效果） |
| `generate_armor_json` | 自定义盔甲（护甲值、槽位） |
| `generate_throwable_json` | 自定义可投掷物品 |

### 代码审查 & 最佳实践

| 工具 | 描述 |
|------|------|
| `review_code` | 统一审查显式传入的 Python/JSON 产物 |
| `get_best_practices` | 获取注册表规则的旧接口兼容投影 |
| `search_components` | 搜索基岩版组件 |
| `get_component_details` | 获取组件详细信息 |
| `list_components` | 列出所有可用组件 |
| `get_architecture_pattern` | 获取并校验核心架构示例 |

---

## 📂 项目结构

```
ModSDK MCP Server/
├── modsdk_mcp/                     # MCP Server 核心模块
│   ├── __init__.py                 # 包标识
│   ├── __main__.py                 # python -m 入口
│   ├── server.py                   # MCP Server 主程序（工具注册、请求处理）
│   ├── docs_reader.py              # 文档读取与搜索引擎
│   ├── standards.py                # 严格加载版本化规范注册表
│   ├── guidance.py                 # 规则筛选与稳定 guidance JSON
│   ├── validation.py               # Python/JSON 统一产物校验
│   ├── knowledge_base.py           # 组件知识库 & 最佳实践兼容投影
│   └── templates.py                # 代码模板 & JSON 生成器
├── docs/                           # ModSDK 官方文档（Markdown）
│   ├── 接口/                       #   API 接口文档
│   ├── 事件/                       #   事件文档
│   ├── 枚举值/                     #   枚举值文档
│   └── 更新信息/                   #   版本更新日志
├── standard/registry/              # 唯一规范源、版本配置与白名单快照
├── skills/                         # 兼容说明；不作为运行时规范源
├── start_mcp.py                    # Agent专用启动入口
├── .mcp.json                       # MCP 配置
├── requirements.txt                # Python 依赖
├── Dockerfile                      # Docker 镜像配置
├── docker-compose.yml              # Docker Compose 配置
├── DEPLOYMENT.md                   # 详细部署指南
└── README.md                       # 本文件
```

---

## ⚙️ 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `MODSDK_DOCS_PATH` | ModSDK 文档目录路径 | `./docs` |
| `MCP_HOST` | SSE 模式监听地址 | `0.0.0.0` |
| `MCP_PORT` | SSE 模式监听端口 | `8000` |

---

## 🎯 内置代码规范

MCP Server 的生成器统一经过结构感知校验。只有可确定证明的严重违规以及项目明确禁止的字符串前缀会阻断；性能、JSON UI 和生命周期工程建议默认告警或人工确认。

| 规范 | 说明 |
|------|------|
| **客户端/服务端分离** | ServerSystem 禁止 import clientApi，反之亦然 |
| **Python 2.7 兼容** | 禁止真实 `u/U/ur/ru` 字符串前缀及 Python 3 专属语法，文件含 UTF-8 声明 |
| **精确 import 白名单** | 使用仓库内 456 项官方快照；项目模块须显式声明 |
| **上下文性能告警** | 仅在循环、Tick 或高频事件上下文充分时提示刷屏、重复创建或降频 |
| **点对点通信** | 优先 `NotifyToClient`，慎用 `BroadcastToAllClient` |
| **JSON 格式档** | 基础物品 1.10；方块支持 legacy_1_10、scalar_1_16、modern_1_19_20 |

> `standard/registry/` 是唯一规范源。优先使用 `get_development_guidance`；`get_best_practices` 仅保留兼容投影。

---

## 📝 使用示例

### 生成 Mod 项目

```
帮我创建一个名为"传送系统"的 Mod，ID 为 teleport_sys，功能是让玩家通过命令传送到指定位置
```

### 生成自定义钻石剑

```
帮我生成一把自定义钻石剑，命名空间 mymod，ID 为 diamond_blade，攻击力 10，耐久 500
```

### 代码审查

```
帮我审查这段代码：

def OnTick(self):
    import mod.server.extraServerApi as serverApi
    comp = serverApi.GetEngineCompFactory().CreatePos(self.playerId)
    pos = comp.GetPos()
```

### 查询组件用法

```
搜索 minecraft:food 组件的详细用法
```

---

## 官方文档维护

默认 ModSDK、BE 版本、文档频道和发布状态由 `standard/registry/manifest.json` 与对应版本档统一指定。官方稳定版上线后，核实来源再调整版本档，不按计划日期自动宣称发布。

```bash
python tools/sync_official_docs.py
```

同步器全量抓取当前版本的公开接口、事件、枚举和关联教程，冻结 3.9 官方基线后自动生成差异与迁移报告。按“类路径 + 名称 + 端侧”保留同名方法，事务性更新正文、结构化索引和导航；旧仓库资料清单单独归档。

`--dry-run` 只抓取并核对数据；`--cache-dir <目录>` 保留本次调查原始响应，复用该目录时使用缓存；默认不使用响应缓存。仅当官网仍提供相应旧版频道时，才使用 `--refresh-baseline` 显式重抓旧版基线。

新增入口：`get_version_changes`、`modsdk-guidance://changes`、`get_best_practices(category="modsdk_310_migration")`。服务代码升级后需要重启 MCP 连接，单独 `reload_documents` 只重读文档。

制作核对只检查编译、JSON、引用、编码、身份去重和 SHA-256。本次不编写或运行离线单元测试，也没有进行游戏实机功能验收。
