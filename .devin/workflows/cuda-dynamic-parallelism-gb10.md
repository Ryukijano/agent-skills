---
description: CUDA Dynamic Parallelism on GB10 workflow
---

# CUDA Dynamic Parallelism on GB10 Workflow

Skill: `.devin/skills/cuda-dynamic-parallelism-gb10/SKILL.md`

## Steps
1. Read the skill at `.devin/skills/cuda-dynamic-parallelism-gb10/SKILL.md`
2. Design a parent kernel and child kernel(s) with clearly defined inputs/outputs
3. Compile with `-rdc=true` and link `-lcudadevrt`
4. Use `cudaDeviceSynchronize()` on the host to wait for parent and child kernels
5. Verify with a synthetic input where expected outputs are trivially checkable
