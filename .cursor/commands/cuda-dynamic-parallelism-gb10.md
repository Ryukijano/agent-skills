# CUDA Dynamic Parallelism on GB10

Use CUDA Dynamic Parallelism (CDP) on GB10: parent kernels that launch child kernels with <<< >>> inside device code, compiling with -rdc=true and linking -lcudadevrt.

Skill: `.cursor/skills/cuda-dynamic-parallelism-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cuda-dynamic-parallelism-gb10/SKILL.md`
2. Design parent/child kernels with clear inputs/outputs
3. Compile with `-rdc=true` and link `-lcudadevrt`
4. Use `cudaDeviceSynchronize()` on the host
5. Verify with a synthetic trivially checkable input
