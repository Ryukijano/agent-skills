---
name: dgx-monitor
description: >-
  Monitor DGX Spark GPU, memory, Docker, conda, and CUDA. Use when checking GPU status, system memory, Docker containers, conda environments, or compiling CUDA kernels on the GB10.
---

# DGX Spark Monitor MCP Server

## Overview
This skill provides 12 tools for dgx spark monitor via the MCP (Model Context Protocol) server at `mcp_servers/dgx_monitor/server.py`.

The server has a **dual CLI + MCP interface** — you can use it directly from the terminal or via any MCP-compatible AI agent (Cursor, Devin, Claude, Windsurf, Gemini).

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

### CLI Mode (direct terminal)
```bash
python3 mcp_servers/dgx_monitor/server.py --cli gpu_status
```

### MCP Mode (via AI agent)
The server is automatically available to MCP-compatible agents after running `mcp_servers/install_all.sh`.

### MCP Inspector (web UI)
```bash
npx @modelcontextprotocol/inspector python3 mcp_servers/dgx_monitor/server.py
```

## Installation
```bash
bash mcp_servers/install_all.sh
```

## Reference Files
- Server code: `mcp_servers/dgx_monitor/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
