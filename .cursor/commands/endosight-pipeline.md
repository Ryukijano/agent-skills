# Endosight Pipeline

Monitor and manage the Endosight 3D reconstruction pipeline. Use when checking pipeline status, listing reconstructions, getting reconstruction stats, or triggering new reconstructions.

Skill: `.cursor/skills/endosight-pipeline/SKILL.md`

## Workflow
1. Read `.cursor/skills/endosight-pipeline/SKILL.md`
2. Identify which tool you need from the 8 available
3. Run the tool in CLI mode or invoke via MCP
4. Verify and report results

## CLI Quick Test
```bash
python3 mcp_servers/endosight_pipeline/server.py --cli pipeline_status
```

## MCP Installation
```bash
bash mcp_servers/install_all.sh
```
