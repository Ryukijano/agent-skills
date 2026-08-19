# Cuda Dynamic Parallelism Quicksort Gb10 on GB10

Use CUDA Dynamic Parallelism (CDP) to implement recursive quicksort on GB10. Covers parent/child kernel launch, -rdc=true, and sync depth limits.

Skill: `.cursor/skills/cuda-dynamic-parallelism-quicksort-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cuda-dynamic-parallelism-quicksort-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Benchmark and report throughput/latency
