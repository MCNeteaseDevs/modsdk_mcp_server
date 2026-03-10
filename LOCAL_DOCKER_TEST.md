# 本地 Docker 测试 MCP Server 步骤

本文档指导你在本地搭建 Docker 容器运行 MCP Server，并在 Claude Desktop 中配置连接。

---

## 前置要求

- ✅ 已安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- ✅ 已安装 Claude Desktop
- ✅ 项目文件准备完毕

---

## 第一步：准备项目文件

确保你的项目目录结构如下：

```
D:/ModSDK MCP Server/
├── modsdk_mcp/
│   ├── __init__.py
│   ├── server.py
│   ├── docs_reader.py
│   └── templates.py
├── docs/                    # ModSDK 文档
├── skills/                  # Skills 文件
├── standard/                # 规范文档
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 第二步：创建 Dockerfile

在项目根目录创建 `Dockerfile`（如果还没有）：

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 复制依赖文件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY modsdk_mcp/ ./modsdk_mcp/
COPY docs/ ./docs/
COPY skills/ ./skills/
COPY standard/ ./standard/

# 环境变量
ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=8000
ENV MODSDK_DOCS_PATH=/app/docs
ENV MODSDK_SKILLS_PATH=/app/skills
ENV MODSDK_STANDARD_PATH=/app/standard

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["python", "-m", "modsdk_mcp.server", "--sse"]
```

---

## 第三步：创建 docker-compose.yml

在项目根目录创建 `docker-compose.yml`（如果还没有）：

```yaml
version: '3.8'

services:
  modsdk-mcp:
    build: .
    container_name: modsdk-mcp-server
    ports:
      - "8000:8000"
    volumes:
      # 挂载文档目录，便于实时更新
      - ./docs:/app/docs:ro
      - ./skills:/app/skills:ro
      - ./standard:/app/standard:ro
    environment:
      - MCP_HOST=0.0.0.0
      - MCP_PORT=8000
    restart: unless-stopped
```

---

## 第四步：构建并启动 Docker 容器

打开 PowerShell，进入项目目录：

```powershell
# 进入项目目录
cd "D:/ModSDK MCP Server"

# 构建 Docker 镜像
docker-compose build

# 启动容器
docker-compose up -d
```

**查看启动日志**：

```powershell
docker-compose logs -f
```

你应该看到类似输出：

```
modsdk-mcp-server  | 🚀 MCP Server (SSE) 启动在 http://0.0.0.0:8000
modsdk-mcp-server  |    - SSE 端点: http://0.0.0.0:8000/sse
modsdk-mcp-server  |    - 消息端点: http://0.0.0.0:8000/messages
modsdk-mcp-server  |    - 健康检查: http://0.0.0.0:8000/health
```

---

## 第五步：验证服务运行

**健康检查**：

```powershell
curl http://localhost:8000/health
```

预期输出：

```json
{"status":"ok","server":"netease-modsdk-mcp"}
```

**或在浏览器中访问**：

打开 http://localhost:8000/health 应该看到相同的 JSON 响应。

---

## 第六步：配置 Claude Desktop

### 6.1 找到配置文件

Claude Desktop 配置文件位置：

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **完整路径**: `C:\Users\<你的用户名>\AppData\Roaming\Claude\claude_desktop_config.json`

### 6.2 打开配置文件

```powershell
# 用记事本打开配置文件
notepad "$env:APPDATA\Claude\claude_desktop_config.json"
```

如果文件不存在，先创建一个空文件。

### 6.3 添加 MCP Server 配置

将配置文件内容修改为：

```json
{
  "mcpServers": {
    "netease-modsdk": {
      "transport": "sse",
      "url": "http://localhost:8000/sse"
    }
  }
}
```

**如果已有其他配置**，只需添加 `netease-modsdk` 部分：

```json
{
  "mcpServers": {
    "其他服务器": {
      "...": "..."
    },
    "netease-modsdk": {
      "transport": "sse",
      "url": "http://localhost:8000/sse"
    }
  }
}
```

### 6.4 保存并重启 Claude Desktop

1. 保存配置文件
2. 完全关闭 Claude Desktop（确保托盘图标也关闭）
3. 重新启动 Claude Desktop

---

## 第七步：验证连接

在 Claude Desktop 中，你应该能看到 MCP 工具可用的标识。

### 测试 1：搜索文档

在 Claude 中输入：

```
搜索 GetEngineCompFactory 的用法
```

Claude 应该会调用 `search_docs` 工具并返回搜索结果。

### 测试 2：生成代码

在 Claude 中输入：

```
帮我写一个监听玩家加入游戏的 ServerSystem
```

Claude 应该会生成符合规范的代码（自动缓存 CF、import 在顶部等）。

### 测试 3：代码审查

在 Claude 中输入：

```
帮我审查这段代码：

def OnTick(self):
    import mod.server.extraServerApi as serverApi
    comp = serverApi.GetEngineCompFactory().CreatePos(self.playerId)
    pos = comp.GetPos()
```

Claude 应该会调用 `review_code` 工具并指出：
- 🔴 函数内 import
- 🔴 GetEngineCompFactory 未缓存

---

## 常用 Docker 命令

```powershell
# 查看容器状态
docker-compose ps

# 查看日志
docker-compose logs -f

# 停止容器
docker-compose down

# 重新构建并启动
docker-compose up -d --build

# 进入容器内部（调试用）
docker exec -it modsdk-mcp-server /bin/bash
```

---

## 故障排除

### 问题 1：Docker 构建失败

**错误**：`pip install` 失败

**解决**：检查 `requirements.txt` 内容是否正确：

```
mcp>=1.0.0
starlette>=0.27.0
uvicorn>=0.23.0
```

### 问题 2：端口被占用

**错误**：`Bind for 0.0.0.0:8000 failed: port is already allocated`

**解决**：
```powershell
# 找出占用端口的进程
netstat -ano | findstr :8000

# 或者修改端口（在 docker-compose.yml 中）
ports:
  - "8001:8000"  # 使用 8001 端口
```

然后修改 Claude 配置：
```json
"url": "http://localhost:8001/sse"
```

### 问题 3：Claude 无法连接

**检查步骤**：

1. **确认 Docker 容器运行中**：
   ```powershell
   docker-compose ps
   ```

2. **确认健康检查通过**：
   ```powershell
   curl http://localhost:8000/health
   ```

3. **确认配置文件格式正确**（JSON 语法）：
   - 检查是否有多余的逗号
   - 检查引号是否配对

4. **重启 Claude Desktop**：
   - 右键托盘图标 → 退出
   - 重新打开 Claude Desktop

### 问题 4：工具调用没有反应

**可能原因**：MCP 连接未建立

**解决**：
1. 检查 Claude Desktop 设置中 MCP 是否启用
2. 查看 Docker 日志是否有连接记录：
   ```powershell
   docker-compose logs -f
   ```

---

## 更新 MCP Server

当你修改了代码后，需要重新构建容器：

```powershell
# 停止并删除旧容器
docker-compose down

# 重新构建并启动
docker-compose up -d --build

# 查看日志确认启动成功
docker-compose logs -f
```

---

## 完整命令速查表

| 操作 | 命令 |
|------|------|
| 构建镜像 | `docker-compose build` |
| 启动容器 | `docker-compose up -d` |
| 停止容器 | `docker-compose down` |
| 查看日志 | `docker-compose logs -f` |
| 重建并启动 | `docker-compose up -d --build` |
| 健康检查 | `curl http://localhost:8000/health` |
| 打开配置 | `notepad "$env:APPDATA\Claude\claude_desktop_config.json"` |

---

## Claude Desktop 配置示例（完整版）

```json
{
  "mcpServers": {
    "netease-modsdk": {
      "transport": "sse",
      "url": "http://localhost:8000/sse"
    }
  }
}
```

配置完成后，享受 AI 辅助的 ModSDK 开发吧！🎮
