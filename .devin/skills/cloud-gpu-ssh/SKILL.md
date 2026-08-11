---
name: cloud-gpu-ssh
description: >-
  Manage remote GPU machines (Lambda Labs, RunPod, Vast.ai, SSH). Use when registering remote machines, running remote commands, monitoring remote GPUs, or syncing files to cloud instances.
---

# Cloud GPU & SSH MCP Server

## Overview
This skill provides 11 tools for cloud gpu & ssh via the MCP server at `mcp_servers/cloud_gpu_ssh/server.py`.

Dual CLI + MCP interface: use directly from terminal or via MCP-compatible agents.

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

### CLI Mode
```bash
python3 mcp_servers/cloud_gpu_ssh/server.py --cli list_machines
```

### MCP Mode
After running `mcp_servers/install_all.sh`, the server is available to all MCP-compatible agents.

## Reference Files
- Server code: `mcp_servers/cloud_gpu_ssh/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
