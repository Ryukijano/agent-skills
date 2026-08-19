# Cub Reduce By Key Gb10 on GB10

Use CUB cub::DeviceReduce::ReduceByKey on GB10 for grouping and reducing contiguous key runs in device memory. Useful for batched embedding aggregation.

Skill: `.cursor/skills/cub-reduce-by-key-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cub-reduce-by-key-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Benchmark and report throughput/latency
