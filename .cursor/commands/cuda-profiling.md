# CUDA Profiling

Profile CUDA kernels with nsys, ncu, compute-sanitizer, and SASS/PTX dump. Use when profiling GPU code, checking memory errors, detecting data races, or inspecting compiled instructions.

Skill: `.cursor/skills/cuda-profiling/SKILL.md`

## Workflow
1. Read `.cursor/skills/cuda-profiling/SKILL.md`
2. Identify which tool you need from the 10 available
3. Run the tool in CLI mode or invoke via MCP
4. Verify and report results

## CLI Quick Test
```bash
python3 mcp_servers/cuda_profiling/server.py --cli memcheck --command ./my_kernel
```

## MCP Installation
```bash
bash mcp_servers/install_all.sh
```
