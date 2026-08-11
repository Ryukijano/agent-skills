---
name: endosight-pipeline
description: >-
  Monitor and manage the Endosight 3D reconstruction pipeline. Use when checking pipeline status, listing reconstructions, getting reconstruction stats, or triggering new reconstructions.
---

# Endosight Pipeline MCP Server

## Overview
This skill provides 8 tools for endosight pipeline via the MCP server at `mcp_servers/endosight_pipeline/server.py`.

Dual CLI + MCP interface: use directly from terminal or via MCP-compatible agents.

## Available Tools

| Tool | Description |
|------|-------------|
| `list_clips` | See server.py for details |
| `list_reconstructions` | See server.py for details |
| `get_reconstruction_stats` | See server.py for details |
| `pipeline_status` | See server.py for details |
| `start_pipeline` | See server.py for details |
| `verify_pipeline` | See server.py for details |
| `sweep_clinical_clips` | See server.py for details |
| `run_reconstruction` | See server.py for details |

## Quick Start

### CLI Mode
```bash
python3 mcp_servers/endosight_pipeline/server.py --cli pipeline_status
```

### MCP Mode
After running `mcp_servers/install_all.sh`, the server is available to all MCP-compatible agents.

## Reference Files
- Server code: `mcp_servers/endosight_pipeline/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
