FROM python:3.11-slim

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码和文档
COPY modsdk_mcp/ ./modsdk_mcp/
COPY docs/ ./docs/
COPY skills/ ./skills/
COPY standard/ ./standard/

# 环境变量
ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=8000
ENV MODSDK_DOCS_PATH=/app/docs

# 暴露端口
EXPOSE 8000

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# 启动 SSE 模式
CMD ["python", "-m", "modsdk_mcp.server", "--sse"]
