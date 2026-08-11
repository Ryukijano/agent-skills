---
name: dgx-monitor
description: >-
  Monitor DGX Spark GPU, memory, Docker, conda, and CUDA. Use when checking GPU status, system memory, Docker containers, conda environments, or compiling CUDA kernels on the GB10.
---

# DGX Spark Monitor MCP Server

## Overview
This skill provides 12 tools for dgx spark monitor via the MCP server at `mcp_servers/dgx_monitor/server.py`.

Dual CLI + MCP interface: use directly from terminal or via MCP-compatible agents.

## Available Tools

| Tool | Description |
|------|-------------|
| `gpu_status` | See server.py for details |
| `gpu_processes` | See server.py for details |
| `kill_gpu_process` | See server.py for details |
| `system_memory` | See server.py for details |
| `disk_usage` | See server.py for details |
| `docker_ps` | See server.py for details |
| `docker_logs` | See server.py for details |
| `docker_gpu_stats` | See server.py for details |
| `conda_envs` | See server.py for details |
| `conda_packages` | See server.py for details |
| `cuda_info` | See server.py for details |
| `compile_cuda` | See server.py for details |

## Quick Start

### CLI Mode
```bash
python3 mcp_servers/dgx_monitor/server.py --cli gpu_status
```

### MCP Mode
After running `mcp_servers/install_all.sh`, the server is available to all MCP-compatible agents.

## Reference Files
- Server code: `mcp_servers/dgx_monitor/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
