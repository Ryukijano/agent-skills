---
description: Blackwell Fp4 Fp8 Block Scaling Ptx Gb10 workflow
---

# Blackwell Fp4 Fp8 Block Scaling Ptx Gb10 on GB10

Skill: `.devin/skills/blackwell-fp4-fp8-block-scaling-ptx-gb10/SKILL.md`

## Steps
1. Read the skill at `.devin/skills/blackwell-fp4-fp8-block-scaling-ptx-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Profile with Nsight Compute and report Tensor Core / memory throughput
6. Tune tile sizes, launch bounds, and SMEM layout for GB10's 273 GB/s bandwidth and 99 KB SMEM cap
