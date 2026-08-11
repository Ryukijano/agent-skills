---
description: DGX Spark Monitor workflow
---

# DGX Spark Monitor Workflow

Skill: `.devin/skills/dgx-monitor/SKILL.md`

## Steps
1. Read the skill at `.devin/skills/dgx-monitor/SKILL.md`
2. Identify which of the 12 tools is needed
3. Run the tool in CLI mode or invoke via MCP
4. Verify output

## CLI Quick Test
```bash
python3 mcp_servers/dgx_monitor/server.py --cli gpu_status
```
