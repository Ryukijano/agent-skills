# Nsight Compute Tensor Cores Gb10 on GB10

Profile CUDA kernels on GB10 with Nsight Compute to find Tensor Core utilization, memory bottlenecks, and occupancy limiters. Covers the key NCU metrics and how to interpret them for SM121.

Skill: `.cursor/skills/nsight-compute-tensor-cores-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/nsight-compute-tensor-cores-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Profile with Nsight Compute and report Tensor Core / memory throughput
6. Tune for GB10's 273 GB/s bandwidth and 99 KB SMEM cap
