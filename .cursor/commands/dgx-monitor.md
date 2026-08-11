# DGX Spark Monitor

Monitor DGX Spark GPU, memory, Docker, conda, and CUDA. Use when checking GPU status, system memory, Docker containers, conda environments, or compiling CUDA kernels on the GB10.

Skill: `.cursor/skills/dgx-monitor/SKILL.md`

## Workflow
1. Read `.cursor/skills/dgx-monitor/SKILL.md`
2. Identify which tool you need from the 12 available
3. Run the tool in CLI mode or invoke via MCP
4. Verify and report results

## CLI Quick Test
```bash
python3 mcp_servers/dgx_monitor/server.py --cli gpu_status
```

## MCP Installation
```bash
bash mcp_servers/install_all.sh
```
