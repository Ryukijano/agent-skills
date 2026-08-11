# Distributed Training

Multi-GPU monitoring, NCCL diagnostics, DDP/FSDP setup, and training job management. Use when checking GPU topology, testing NCCL bandwidth, verifying distributed training setup, or managing training jobs.

Skill: `.cursor/skills/distributed-training/SKILL.md`

## Workflow
1. Read `.cursor/skills/distributed-training/SKILL.md`
2. Identify which tool you need from the 11 available
3. Run the tool in CLI mode or invoke via MCP
4. Verify and report results

## CLI Quick Test
```bash
python3 mcp_servers/distributed_training/server.py --cli list_gpus
```

## MCP Installation
```bash
bash mcp_servers/install_all.sh
```
