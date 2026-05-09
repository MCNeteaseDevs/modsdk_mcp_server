"""
模块入口点
支持 python -m modsdk_mcp 运行
"""

import sys

from .server import run, run_sse

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--sse":
        run_sse()
    else:
        run()
