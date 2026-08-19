# Blackwell Sm121 Targeting Gb10 on GB10

Correctly target the GB10 (SM121) architecture: sm_121 vs sm_121f vs sm_121a, PTX version requirements, Triton ptxas setup, and common compile/runtime errors on DGX Spark.

Skill: `.cursor/skills/blackwell-sm121-targeting-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/blackwell-sm121-targeting-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Profile with Nsight Compute and report Tensor Core / memory throughput
6. Tune for GB10's 273 GB/s bandwidth and 99 KB SMEM cap
