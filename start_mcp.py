"""
MCP Server 启动脚本
用于 CodeMaker 等不支持 cwd 参数的 MCP 客户端
"""
import sys
import os

# 将项目根目录加入 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modsdk_mcp.server import run

if __name__ == "__main__":
    run()
