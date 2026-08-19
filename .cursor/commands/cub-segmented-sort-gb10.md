# Cub Segmented Sort Gb10 on GB10

Use CUB cub::DeviceSegmentedSort on GB10 to sort many independent segments in one call. Useful for top-k and batched attention score sorting.

Skill: `.cursor/skills/cub-segmented-sort-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cub-segmented-sort-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Benchmark and report throughput/latency
