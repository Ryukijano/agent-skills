---
description: CUDA Profiling workflow
---

# CUDA Profiling Workflow

Skill: `.devin/skills/cuda-profiling/SKILL.md`

## Steps
1. Read the skill at `.devin/skills/cuda-profiling/SKILL.md`
2. Identify which of the 10 tools is needed
3. Run the tool in CLI mode or invoke via MCP
4. Verify output

## CLI Quick Test
```bash
python3 mcp_servers/cuda_profiling/server.py --cli memcheck --command ./my_kernel
```
