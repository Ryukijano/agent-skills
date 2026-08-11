---
name: cuda-profiling
description: >-
  Profile CUDA kernels with nsys, ncu, compute-sanitizer, and SASS/PTX dump. Use when profiling GPU code, checking memory errors, detecting data races, or inspecting compiled instructions.
---

# CUDA Profiling MCP Server

## Overview
This skill provides 10 tools for cuda profiling via the MCP (Model Context Protocol) server at `mcp_servers/cuda_profiling/server.py`.

The server has a **dual CLI + MCP interface** — you can use it directly from the terminal or via any MCP-compatible AI agent (Cursor, Devin, Claude, Windsurf, Gemini).

## Available Tools

| Tool | Description |
|------|-------------|
| `profile_nsys` | See server.py for details |
| `parse_nsys_stats` | See server.py for details |
| `profile_ncu` | See server.py for details |
| `parse_ncu_report` | See server.py for details |
| `memcheck` | See server.py for details |
| `racecheck` | See server.py for details |
| `initcheck` | See server.py for details |
| `dump_sass` | See server.py for details |
| `dump_ptx` | See server.py for details |
| `benchmark_kernel` | See server.py for details |

## Quick Start

### CLI Mode (direct terminal)
```bash
python3 mcp_servers/cuda_profiling/server.py --cli memcheck --command ./my_kernel
```

### MCP Mode (via AI agent)
The server is automatically available to MCP-compatible agents after running `mcp_servers/install_all.sh`.

### MCP Inspector (web UI)
```bash
npx @modelcontextprotocol/inspector python3 mcp_servers/cuda_profiling/server.py
```

## Installation
```bash
bash mcp_servers/install_all.sh
```

## Reference Files
- Server code: `mcp_servers/cuda_profiling/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
