---
name: distributed-training
description: >-
  Multi-GPU monitoring, NCCL diagnostics, DDP/FSDP setup, and training job management. Use when checking GPU topology, testing NCCL bandwidth, verifying distributed training setup, or managing training jobs.
---

# Distributed Training MCP Server

## Overview
This skill provides 11 tools for distributed training via the MCP server at `mcp_servers/distributed_training/server.py`.

Dual CLI + MCP interface: use directly from terminal or via MCP-compatible agents.

## Available Tools

| Tool | Description |
|------|-------------|
| `list_gpus` | See server.py for details |
| `gpu_interconnect` | See server.py for details |
| `cuda_visible_devices` | See server.py for details |
| `nccl_test_all_reduce` | See server.py for details |
| `check_nccl_env` | See server.py for details |
| `torch_distributed_info` | See server.py for details |
| `check_ddp_setup` | See server.py for details |
| `training_jobs` | See server.py for details |
| `kill_training_job` | See server.py for details |
| `list_checkpoints` | See server.py for details |
| `hostfile_info` | See server.py for details |

## Quick Start

### CLI Mode
```bash
python3 mcp_servers/distributed_training/server.py --cli list_gpus
```

### MCP Mode
After running `mcp_servers/install_all.sh`, the server is available to all MCP-compatible agents.

## Reference Files
- Server code: `mcp_servers/distributed_training/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
