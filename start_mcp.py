"""
MCP Server 启动脚本（通用入口）
使用绝对路径调用本文件即可启动，无需 cwd 参数，兼容所有 MCP 客户端。

用法:
  python start_mcp.py          # stdio 模式（默认）
  python start_mcp.py --sse    # SSE 模式
"""
import sys
import os

# 将项目根目录加入 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modsdk_mcp.server import run, run_sse

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--sse":
        run_sse()
    else:
        run()
