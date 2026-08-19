# Shared Memory Swizzling Gb10 on GB10

Eliminate shared memory bank conflicts on GB10 with padding and XOR-based swizzling. Covers 32-bank layout, 128-byte swizzle patterns, CuTe `Swizzle<>`, and the SMEM occupancy tradeoff on SM121 (99 KB max per block).

Skill: `.cursor/skills/shared-memory-swizzling-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/shared-memory-swizzling-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Profile with Nsight Compute and report Tensor Core / memory throughput
6. Tune for GB10's 273 GB/s bandwidth and 99 KB SMEM cap
