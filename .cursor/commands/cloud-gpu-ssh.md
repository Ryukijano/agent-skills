# Cloud GPU & SSH

Manage remote GPU machines (Lambda Labs, RunPod, Vast.ai, SSH). Use when registering remote machines, running remote commands, monitoring remote GPUs, or syncing files to cloud instances.

Skill: `.cursor/skills/cloud-gpu-ssh/SKILL.md`

## Workflow
1. Read `.cursor/skills/cloud-gpu-ssh/SKILL.md`
2. Identify which tool you need from the 11 available
3. Run the tool in CLI mode or invoke via MCP
4. Verify and report results

## CLI Quick Test
```bash
python3 mcp_servers/cloud_gpu_ssh/server.py --cli list_machines
```

## MCP Installation
```bash
bash mcp_servers/install_all.sh
```
