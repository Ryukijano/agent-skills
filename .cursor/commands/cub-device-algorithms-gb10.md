# CUB Device-Wide Algorithms on GB10

Use the CUB library on GB10 for device-wide reduce, scan, and sort. Covers temporary-storage sizing, fetching CCCL headers when the system CUDA install does not include them, and verifying against CPU references.

Skill: `.cursor/skills/cub-device-algorithms-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cub-device-algorithms-gb10/SKILL.md`
2. Install `nvidia-cuda-cccl` if CUB headers are missing
3. Write the two-call CUB pattern (query temp size, allocate, run)
4. Verify reduce/scan/sort results against CPU
5. Report timing and bandwidth
