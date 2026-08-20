# Cloud GPU & SSH MCP Server

## Overview
This skill provides 11 tools for cloud gpu & ssh via the MCP (Model Context Protocol) server at `mcp_servers/cloud_gpu_ssh/server.py`.

The server has a **dual CLI + MCP interface** — you can use it directly from the terminal or via any MCP-compatible AI agent (Cursor, Devin, Claude, Windsurf, Gemini).

## Available Tools

| Tool | Description |
|------|-------------|
| `register_machine` | See server.py for details |
| `list_machines` | See server.py for details |
| `unregister_machine` | See server.py for details |
| `remote_command` | See server.py for details |
| `remote_gpu_status` | See server.py for details |
| `remote_training_status` | See server.py for details |
| `remote_disk_usage` | See server.py for details |
| `remote_tail_log` | See server.py for details |
| `upload_file` | See server.py for details |
| `download_file` | See server.py for details |
| `lambda_gpu_pricing` | See server.py for details |

## Quick Start

### CLI Mode (direct terminal)
```bash
python3 mcp_servers/cloud_gpu_ssh/server.py --cli list_machines
```

### MCP Mode (via AI agent)
The server is automatically available to MCP-compatible agents after running `mcp_servers/install_all.sh`.

### MCP Inspector (web UI)
```bash
npx @modelcontextprotocol/inspector python3 mcp_servers/cloud_gpu_ssh/server.py
```

## Installation
```bash
bash mcp_servers/install_all.sh
```

## Reference Files
- Server code: `mcp_servers/cloud_gpu_ssh/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
