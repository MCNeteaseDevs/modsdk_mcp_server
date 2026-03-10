# NetEase ModSDK MCP Server — 部署指南

本文档详细介绍如何将 NetEase ModSDK MCP Server 部署到各种 AI 客户端中。

> 📖 如果你只想快速上手，请先阅读 [README.md](./README.md) 的「快速开始」章节。

---

## 目录

- [前置准备](#前置准备)
- [方法一：Claude Desktop（Stdio 模式）](#方法一claude-desktopstdio-模式)
- [方法二：Cursor / VS Code](#方法二cursor--vs-code)
- [方法三：CodeMaker](#方法三codemaker)
- [方法四：SSE 模式（本地 / 远程）](#方法四sse-模式本地--远程)
- [方法五：Docker 部署](#方法五docker-部署)
- [验证部署](#验证部署)
- [故障排除](#故障排除)
- [附录：环境变量](#附录环境变量)

---

## 前置准备

### 系统要求

| 项目 | 要求 |
|------|------|
| Python | ≥ 3.10 |
| 操作系统 | Windows / macOS / Linux |
| 磁盘空间 | ≥ 100 MB（含文档） |

### 安装依赖

```bash
cd "D:/ModSDK MCP Server"
pip install -r requirements.txt
```

`requirements.txt` 内容：

```
mcp>=1.0.0
httpx
starlette
uvicorn
```

### 项目文件结构

确保以下文件完整：

```
ModSDK MCP Server/
├── modsdk_mcp/              # ✅ 必需 — MCP Server 核心代码
│   ├── __init__.py
│   ├── __main__.py
│   ├── server.py
│   ├── docs_reader.py
│   ├── knowledge_base.py
│   └── templates.py
├── docs/                    # ✅ 必需 — ModSDK 文档
├── standard/                # 📌 推荐 — 开发规范文档
├── skills/                  # 📌 推荐 — Claude Skills
├── start_mcp.py             # 📌 CodeMaker 专用入口
├── requirements.txt         # ✅ 必需
├── Dockerfile               # 🔧 Docker 部署用
└── docker-compose.yml       # 🔧 Docker 部署用
```

---

## 方法一：Claude Desktop（Stdio 模式）

> **适合场景**：个人开发，最简单的部署方式。

### 步骤 1：找到配置文件

| 操作系统 | 配置文件路径 |
|----------|-------------|
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |

**Windows 快速打开**：

```powershell
notepad "$env:APPDATA\Claude\claude_desktop_config.json"
```

### 步骤 2：添加 MCP Server 配置

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

> ⚠️ **注意**：将 `cwd` 替换为你实际的项目路径。Windows 路径使用正斜杠 `/` 或双反斜杠 `\\`。

如果已有其他 MCP Server 配置，在 `mcpServers` 对象中追加即可：

```json
{
  "mcpServers": {
    "existing-server": { "...": "..." },
    "ModSDK MCP Server": {
      "command": "python",
      "args": ["-m", "modsdk_mcp"],
      "cwd": "D:/ModSDK MCP Server"
    }
  }
}
```

### 步骤 3：重启 Claude Desktop

1. 右键系统托盘中的 Claude 图标 → **退出**
2. 重新打开 Claude Desktop
3. 在对话界面底部应能看到 MCP 工具图标

---

## 方法二：Cursor / VS Code

> **适合场景**：在 IDE 内直接使用 MCP 能力。

### Cursor

在项目根目录创建 `.cursor/mcp.json`：

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

### VS Code（Copilot MCP 支持）

在项目根目录创建 `.vscode/mcp.json`：

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

### 可选：配合 `.cursorrules`

在项目根目录创建 `.cursorrules` 增强效果：

```markdown
## ModSDK 开发规范

本项目使用 NetEase ModSDK MCP Server，所有代码生成和审查已内置官方开发规范，请自动遵循。
```

---

## 方法三：CodeMaker

> **适合场景**：使用 CodeMaker AI 助手进行开发。

### 特殊说明

CodeMaker 对 `python -m` 方式的 `cwd` 支持存在限制，因此项目提供了 `start_mcp.py` 包装入口，它会自动设置正确的工作目录。

### 配置方法

在项目根目录创建 `.mcp.json`（项目中已预置）：

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

`start_mcp.py` 的作用：

```python
# 自动将项目目录加入 sys.path，然后启动 MCP Server
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modsdk_mcp.server import run
run()
```

---

## 方法四：SSE 模式（本地 / 远程）

> **适合场景**：团队共享 MCP Server、远程服务器部署、多客户端连接。

### 本地启动 SSE 服务

```bash
cd "D:/ModSDK MCP Server"
python -m modsdk_mcp --sse
```

默认监听 `http://0.0.0.0:8000`，可通过环境变量自定义：

```bash
# Windows PowerShell
$env:MCP_HOST = "0.0.0.0"
$env:MCP_PORT = "9000"
python -m modsdk_mcp --sse

# Linux / macOS
MCP_HOST=0.0.0.0 MCP_PORT=9000 python -m modsdk_mcp --sse
```

### 客户端连接配置

在任意支持 SSE 的 MCP 客户端中：

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

远程服务器替换为实际地址：

```json
{
  "mcpServers": {
    "ModSDK MCP Server": {
      "transport": "sse",
      "url": "https://your-server.com/sse"
    }
  }
}
```

### 健康检查

```bash
curl http://localhost:8000/health
# 返回: {"status": "ok", "server": "netease-modsdk-mcp"}
```

### 远程服务器部署（systemd）

创建 `/etc/systemd/system/modsdk-mcp.service`：

```ini
[Unit]
Description=NetEase ModSDK MCP Server
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/modsdk-mcp
Environment="MCP_HOST=0.0.0.0"
Environment="MCP_PORT=8000"
Environment="MODSDK_DOCS_PATH=/opt/modsdk-mcp/docs"
ExecStart=/usr/bin/python3 -m modsdk_mcp --sse
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable modsdk-mcp
sudo systemctl start modsdk-mcp
```

### Nginx 反向代理（可选）

```nginx
server {
    listen 443 ssl;
    server_name mcp.example.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_buffering off;
        proxy_cache off;
    }
}
```

---

## 方法五：Docker 部署

> **适合场景**：隔离环境、CI/CD 集成、一键部署。

### 构建 & 启动

```bash
cd "D:/ModSDK MCP Server"

# 构建并启动
docker-compose up -d --build

# 查看日志
docker-compose logs -f
```

预期输出：

```
modsdk-mcp-server  | 🚀 MCP Server (SSE) 启动在 http://0.0.0.0:8000
```

### 客户端配置

与 SSE 模式相同：

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

### Docker 常用命令

| 操作 | 命令 |
|------|------|
| 构建并启动 | `docker-compose up -d --build` |
| 查看日志 | `docker-compose logs -f` |
| 停止容器 | `docker-compose down` |
| 查看状态 | `docker-compose ps` |
| 健康检查 | `curl http://localhost:8000/health` |

### 自定义端口

修改 `docker-compose.yml` 中的端口映射：

```yaml
ports:
  - "9000:8000"   # 宿主机 9000 → 容器 8000
```

然后客户端 URL 改为 `http://localhost:9000/sse`。

---

## 验证部署

无论使用哪种部署方式，都可以通过以下步骤验证 MCP Server 是否正常工作。

### 测试 1：文档搜索

在 AI 助手中输入：

```
搜索 GetEngineCompFactory 的用法
```

✅ 预期：返回包含 `GetEngineCompFactory` 的 API 文档内容。

### 测试 2：代码生成

```
帮我写一个监听玩家加入游戏的 ServerSystem
```

✅ 预期：生成的代码应包含：
- 模块级缓存 `CF = serverApi.GetEngineCompFactory()`
- 所有 import 在文件顶部
- 只导入 `serverApi`，不会误导入 `clientApi`

### 测试 3：代码审查

```
帮我审查这段代码：

def OnTick(self):
    import mod.server.extraServerApi as serverApi
    comp = serverApi.GetEngineCompFactory().CreatePos(self.playerId)
    pos = comp.GetPos()
```

✅ 预期：指出以下问题：
- 🔴 函数内 import
- 🔴 GetEngineCompFactory 未缓存

### 测试 4：组件查询

```
查询 minecraft:food 组件的用法
```

✅ 预期：返回食物组件的属性、配置示例等详细信息。

---

## 故障排除

### 🔴 MCP Server 启动失败

**可能原因 & 解决方案**：

| 原因 | 解决 |
|------|------|
| Python 版本过低 | 运行 `python --version` 确认 ≥ 3.10 |
| 缺少依赖 | 运行 `pip install -r requirements.txt` |
| `docs/` 目录缺失 | 确保 `docs/` 目录存在且包含 `接口/` 和 `事件/` 子目录 |

### 🔴 AI 客户端未识别 MCP Server

**排查步骤**：

1. **检查配置文件 JSON 语法** — 使用在线 JSON 验证器确认格式正确
2. **检查路径** — `cwd` 指向的目录必须包含 `modsdk_mcp/` 文件夹
3. **Windows 路径** — 使用 `/` 或 `\\`，不要使用单个 `\`
4. **重启客户端** — 修改配置后必须完全重启（包括托盘进程）

```json
// ✅ 正确的 Windows 路径
"cwd": "D:/ModSDK MCP Server"
"cwd": "D:\\ModSDK MCP Server"

// ❌ 错误的 Windows 路径
"cwd": "D:\ModSDK MCP Server"
```

### 🔴 Docker 端口被占用

```powershell
# 查找占用端口的进程
netstat -ano | findstr :8000

# 或修改 docker-compose.yml 使用其他端口
ports:
  - "8001:8000"
```

### 🟡 SSE 连接不稳定

- 检查防火墙是否放行对应端口
- 如使用 Nginx，确保 `proxy_buffering off` 已设置
- 确认 SSE 端点路径为 `/sse`（不是 `/`）

---

## 附录：环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `MODSDK_DOCS_PATH` | ModSDK 文档目录路径 | `./docs` |
| `MODSDK_SKILLS_PATH` | Skills 文件目录路径 | `./skills` |
| `MODSDK_STANDARD_PATH` | Standard 文档目录路径 | `./standard` |
| `MCP_HOST` | SSE 模式监听地址 | `0.0.0.0` |
| `MCP_PORT` | SSE 模式监听端口 | `8000` |

---

## 部署方式对比

| 特性 | Stdio（本地） | SSE（远程） | Docker |
|------|:------------:|:----------:|:------:|
| 部署复杂度 | ⭐ 简单 | ⭐⭐ 中等 | ⭐⭐ 中等 |
| 适合场景 | 个人开发 | 团队共享 | 隔离环境 |
| 文档更新 | 本地即时生效 | 服务器统一更新 | 需重建容器 |
| 网络依赖 | 无 | 需要 | 可选 |
| 多客户端 | ❌ 每人一个 | ✅ 共享 | ✅ 共享 |
| 性能 | ⭐⭐⭐ 最佳 | ⭐⭐ 略有延迟 | ⭐⭐ 略有延迟 |

---

## 相关链接

- [MCP 官方文档](https://modelcontextprotocol.io/)
- [NetEase ModSDK 官方文档](https://mc.163.com/dev/mcmanual/mc-dev/)

---

## 支持

如有问题，请检查：
1. [MCP 官方文档](https://modelcontextprotocol.io/)
2. [NetEase ModSDK 官方文档](https://mc.163.com/dev/mcmanual/mc-dev/)
