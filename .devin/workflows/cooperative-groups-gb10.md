---
description: Cooperative Groups on GB10 workflow
---

# Cooperative Groups on GB10 Workflow

Skill: `.devin/skills/cooperative-groups-gb10/SKILL.md`

## Steps
1. Read the skill at `.devin/skills/cooperative-groups-gb10/SKILL.md`
2. Confirm `prop.cooperativeLaunch` is true on the target device
3. Write a kernel using `cg::this_thread_block()` / `cg::this_grid()` or `cg::tiled_partition<N>`
4. Launch with `cudaLaunchCooperativeKernel` and occupancy-calculate the grid
5. Verify against a CPU reference and check memory bandwidth
