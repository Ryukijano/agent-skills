# Cooperative Groups on GB10

Use Cooperative Groups on GB10 (sm_121): thread_block_tile, grid_group, this_grid(), and cudaLaunchCooperativeKernel for single-pass multi-block reductions and other cross-block cooperative algorithms.

Skill: `.cursor/skills/cooperative-groups-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cooperative-groups-gb10/SKILL.md`
2. Confirm `prop.cooperativeLaunch` is true
3. Write a kernel using `cg::this_thread_block()` / `cg::this_grid()` or `cg::tiled_partition<N>`
4. Launch with `cudaLaunchCooperativeKernel` and occupancy-calculate the grid
5. Verify against a CPU reference and check memory bandwidth
