---
name: endosight-pipeline
description: >-
  Monitor and manage the Endosight 3D reconstruction pipeline. Use when checking pipeline status, listing reconstructions, getting reconstruction stats, or triggering new reconstructions.
---

# Endosight Pipeline MCP Server

## Overview
This skill provides 8 tools for endosight pipeline via the MCP (Model Context Protocol) server at `mcp_servers/endosight_pipeline/server.py`.

The server has a **dual CLI + MCP interface** — you can use it directly from the terminal or via any MCP-compatible AI agent (Cursor, Devin, Claude, Windsurf, Gemini).

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

### CLI Mode (direct terminal)
```bash
python3 mcp_servers/endosight_pipeline/server.py --cli pipeline_status
```

### MCP Mode (via AI agent)
The server is automatically available to MCP-compatible agents after running `mcp_servers/install_all.sh`.

### MCP Inspector (web UI)
```bash
npx @modelcontextprotocol/inspector python3 mcp_servers/endosight_pipeline/server.py
```

## Installation
```bash
bash mcp_servers/install_all.sh
```

## Reference Files
- Server code: `mcp_servers/endosight_pipeline/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
