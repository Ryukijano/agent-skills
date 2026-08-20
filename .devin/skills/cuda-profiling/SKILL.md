# CUDA Profiling MCP Server

## Overview
This skill provides 10 tools for cuda profiling via the MCP server at `mcp_servers/cuda_profiling/server.py`.

Dual CLI + MCP interface: use directly from terminal or via MCP-compatible agents.

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

### CLI Mode
```bash
python3 mcp_servers/cuda_profiling/server.py --cli memcheck --command ./my_kernel
```

### MCP Mode
After running `mcp_servers/install_all.sh`, the server is available to all MCP-compatible agents.

## Reference Files
- Server code: `mcp_servers/cuda_profiling/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
