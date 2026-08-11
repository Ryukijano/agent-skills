---
name: tpu-jax
description: >-
  JAX device discovery, TPU topology, gcloud TPU VM management, and JAX profiling. Use when working with Google Cloud TPUs, JAX distributed training, or profiling XLA compilation.
---

# TPU & JAX MCP Server

## Overview
This skill provides 10 tools for tpu & jax via the MCP server at `mcp_servers/tpu_jax/server.py`.

Dual CLI + MCP interface: use directly from terminal or via MCP-compatible agents.

## Available Tools

| Tool | Description |
|------|-------------|
| `jax_devices` | See server.py for details |
| `jax_tpu_info` | See server.py for details |
| `jax_distributed_setup` | See server.py for details |
| `gcloud_tpu_list` | See server.py for details |
| `gcloud_tpu_create` | See server.py for details |
| `gcloud_tpu_delete` | See server.py for details |
| `gcloud_tpu_ssh` | See server.py for details |
| `jax_profile` | See server.py for details |
| `jax_memory_info` | See server.py for details |
| `jax_compilation_check` | See server.py for details |

## Quick Start

### CLI Mode
```bash
python3 mcp_servers/tpu_jax/server.py --cli jax_devices
```

### MCP Mode
After running `mcp_servers/install_all.sh`, the server is available to all MCP-compatible agents.

## Reference Files
- Server code: `mcp_servers/tpu_jax/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
