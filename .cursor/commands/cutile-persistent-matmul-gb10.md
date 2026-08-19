# Cutile Persistent Matmul Gb10 on GB10

Use cuTile Python persistent (static) kernels for high-throughput FP16/FP32 GEMM on GB10. Covers 2-wave block launch, tile swizzling, FP32 accumulation, and Tensor Core throughput tuning.

Skill: `.cursor/skills/cutile-persistent-matmul-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cutile-persistent-matmul-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Benchmark and report throughput/latency
