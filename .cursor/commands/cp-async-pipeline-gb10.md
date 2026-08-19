# Cp Async Pipeline Gb10 on GB10

Build multi-stage async copy pipelines with `cp.async` on GB10. Covers commit/wait groups, mbarriers, double/triple buffering, and why SM121 uses `cp.async` instead of TMA for GMEM->SMEM staging.

Skill: `.cursor/skills/cp-async-pipeline-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cp-async-pipeline-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Profile with Nsight Compute and report Tensor Core / memory throughput
6. Tune for GB10's 273 GB/s bandwidth and 99 KB SMEM cap
