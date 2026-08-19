# Cooperative Groups Warp Tile Gb10 on GB10

Use Cooperative Groups `cg::tiled_partition` and `cg::thread_block_tile` for warp-level reduction, scan, and matrix/vector operations on GB10.

Skill: `.cursor/skills/cooperative-groups-warp-tile-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cooperative-groups-warp-tile-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Benchmark and report throughput/latency
