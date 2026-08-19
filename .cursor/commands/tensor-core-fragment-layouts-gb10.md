# Tensor Core Fragment Layouts Gb10 on GB10

Understand PTX mma.sync fragment layouts for NVIDIA Tensor Cores on GB10 (SM121). Covers m16n8k16/32/64 shapes, A/B/C/D register mapping, lane-to-element mapping, and how to stage swizzled shared memory for fragment loads.

Skill: `.cursor/skills/tensor-core-fragment-layouts-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/tensor-core-fragment-layouts-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Profile with Nsight Compute and report Tensor Core / memory throughput
6. Tune for GB10's 273 GB/s bandwidth and 99 KB SMEM cap
