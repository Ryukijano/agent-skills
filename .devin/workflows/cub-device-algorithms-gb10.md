---
description: CUB device-wide algorithms on GB10 workflow
---

# CUB Device-Wide Algorithms on GB10 Workflow

Skill: `.devin/skills/cub-device-algorithms-gb10/SKILL.md`

## Steps
1. Read the skill at `.devin/skills/cub-device-algorithms-gb10/SKILL.md`
2. Install `nvidia-cuda-cccl` if the system CUDA headers do not include CUB
3. Write the two-call CUB pattern (query temp size, allocate, run)
4. Verify reduce/scan/sort results against CPU (`std::accumulate`, `std::sort`, etc.)
5. Report timing and bandwidth
