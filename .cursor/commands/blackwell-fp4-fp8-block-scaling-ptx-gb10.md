# Blackwell Fp4 Fp8 Block Scaling Ptx Gb10 on GB10

Implement FP8 and block-scaled FP4 (NVFP4) Tensor Core MMA with inline PTX on GB10. Covers `kind::f8f6f4`, `kind::mxf4nvf4.block_scale`, scale-factor encoding, FP32 accumulation, and the sm_121f / sm_121a / PTX 9.1 requirements.

Skill: `.cursor/skills/blackwell-fp4-fp8-block-scaling-ptx-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/blackwell-fp4-fp8-block-scaling-ptx-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Profile with Nsight Compute and report Tensor Core / memory throughput
6. Tune for GB10's 273 GB/s bandwidth and 99 KB SMEM cap
