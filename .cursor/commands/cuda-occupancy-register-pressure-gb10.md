# Cuda Occupancy Register Pressure Gb10 on GB10

Tune CUDA kernel occupancy and register pressure on GB10. Covers launch bounds, the occupancy API, shared-memory vs register tradeoffs, and when high occupancy helps or hurts performance.

Skill: `.cursor/skills/cuda-occupancy-register-pressure-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cuda-occupancy-register-pressure-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Profile with Nsight Compute and report Tensor Core / memory throughput
6. Tune for GB10's 273 GB/s bandwidth and 99 KB SMEM cap
