# Fast Gemm Inference Gb10 on GB10

Optimize GEMM for low-latency inference on GB10. Covers cuBLASLt heuristics, batched GEMM, epilogue fusion, and FP8/FP16 precision selection.

Skill: `.cursor/skills/fast-gemm-inference-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/fast-gemm-inference-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Benchmark and report throughput/latency
