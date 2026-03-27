# 🎮 NetEase ModSDK MCP Server

> **Model Context Protocol Server for 我的世界中国版（网易）ModSDK 开发**

为 AI 编程助手（Claude Desktop、Cursor、CodeMaker 等）提供 **文档检索、代码生成、代码审查** 能力，显著提升 NetEase ModSDK 开发效率。

---

## ✨ 核心能力

| 能力 | 说明 |
|------|------|
| 🔍 **智能文档检索** | 模糊搜索、驼峰分词、中文搜索，覆盖 API 接口 & 事件文档 |
| 📝 **代码生成** | 自动生成符合网易规范的 Mod 项目、Server/Client System、自定义物品/方块/实体 |
| 🔧 **工具 & 武器生成** | 一键生成剑、镐、斧、锹、锄、弓、盔甲、食物、可投掷物品 JSON |
| 📋 **配方 & 战利品表** | 生成有序/无序合成配方、熔炉配方、战利品表、生成规则 |
| 🔬 **代码审查** | 检测 Python 2.7 兼容性、客户端/服务端混用、性能反模式 |
| 📚 **组件百科** | 查询物品/方块/实体/网易特有组件的用法和配置 |
| ⚡ **最佳实践** | 内置官方性能优化规范，生成代码自动遵循 |

---

## 🚀 快速开始

### 前置要求

- **Python ≥ 3.10**
- **pip**（Python 包管理器）

### 1. 安装依赖

```bash
cd "D:/ModSDK MCP Server"
pip install -r requirements.txt
```

### 2. 选择你的 AI 客户端进行配置

<details>
<summary><b>🟢 Claude Desktop（推荐）</b></summary>

编辑配置文件：
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "ModSDK MCP Server": {
      "command": "python",
      "args": ["-m", "modsdk_mcp"],
      "cwd": "D:/ModSDK MCP Server"
    }
  }
}
```

保存后重启 Claude Desktop。
</details>

<details>
<summary><b>🔵 Cursor / VS Code</b></summary>

在项目根目录创建 `.cursor/mcp.json`（Cursor）或 `.vscode/mcp.json`（VS Code）：

```json
{
  "servers": {
    "ModSDK MCP Server": {
      "command": "python",
      "args": ["-m", "modsdk_mcp"],
      "cwd": "D:/ModSDK MCP Server"
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
<summary><b>🟡 CodeMaker</b></summary>

在项目根目录创建 `.mcp.json`：

```json
{
  "servers": {
    "ModSDK MCP Server": {
      "command": "python",
      "args": ["start_mcp.py"],
      "cwd": "D:/ModSDK MCP Server"
    }
  }
}
```

> **说明**: CodeMaker 不支持 `python -m` 的 `cwd` 传参方式，因此使用 `start_mcp.py` 包装入口。
</details>

<details>
<summary><b>🔴 SSE 模式（远程 / Docker）</b></summary>

启动 SSE 服务：

```bash
python -m modsdk_mcp.server --sse
# 默认监听 http://0.0.0.0:8000
```

在客户端中配置：

```json
{
  "mcpServers": {
    "ModSDK MCP Server": {
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
| `get_document` | 获取指定文档完整内容 |
| `get_document_section` | 获取文档指定章节 |
| `get_document_structure` | 获取文档目录结构 |
| `list_documents` | 列出所有可用文档 |
| `reload_documents` | 重新加载文档索引 |

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
| `review_code` | 审查代码（Python 2.7 兼容性、架构、性能） |
| `get_best_practices` | 获取最佳实践规则 |
| `search_components` | 搜索基岩版组件 |
| `get_component_details` | 获取组件详细信息 |
| `list_components` | 列出所有可用组件 |
| `list_modsdk_events` | 列出常用事件 |

---

## 📂 项目结构

```
ModSDK MCP Server/
├── modsdk_mcp/                     # MCP Server 核心模块
│   ├── __init__.py                 # 包标识
│   ├── __main__.py                 # python -m 入口
│   ├── server.py                   # MCP Server 主程序（工具注册、请求处理）
│   ├── docs_reader.py              # 文档读取与搜索引擎
│   ├── knowledge_base.py           # 组件知识库 & 最佳实践规则
│   └── templates.py                # 代码模板 & JSON 生成器
├── docs/                           # ModSDK 官方文档（Markdown）
│   ├── 接口/                       #   API 接口文档
│   ├── 事件/                       #   事件文档
│   ├── 枚举值/                     #   枚举值文档
│   └── 更新信息/                   #   版本更新日志
├── standard/                       # 官方开发规范文档
├── skills/                         # Claude Skills 文件
├── start_mcp.py                    # CodeMaker 专用启动入口
├── .mcp.json                       # CodeMaker MCP 配置
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
| `MODSDK_SKILLS_PATH` | Skills 文件目录路径 | `./skills` |
| `MODSDK_STANDARD_PATH` | Standard 文档目录路径 | `./standard` |
| `MCP_HOST` | SSE 模式监听地址 | `0.0.0.0` |
| `MCP_PORT` | SSE 模式监听端口 | `8000` |

---

## 🎯 内置代码规范

MCP Server 生成的所有代码 **自动遵循** 以下网易 ModSDK 强制规范：

| 规范 | 说明 |
|------|------|
| **客户端/服务端分离** | ServerSystem 禁止 import clientApi，反之亦然 |
| **CompFactory 缓存** | `CF = serverApi.GetEngineCompFactory()` 模块级缓存 |
| **import 顶部化** | 所有 import 必须在文件顶部，禁止函数内 import |
| **Tick 降帧** | Tick 事件使用质数取模降帧 |
| **BlockTick 加盐** | ServerBlockEntityTickEvent 使用坐标哈希加盐 |
| **点对点通信** | 优先 `NotifyToClient`，慎用 `BroadcastToAllClient` |
| **Python 2.7 兼容** | 禁止 f-string、type hints、print() 函数 |

> 📚 完整规范见 `standard/` 目录或通过 `get_best_practices` 工具查询。

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
