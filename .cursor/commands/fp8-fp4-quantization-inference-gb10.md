# Fp8 Fp4 Quantization Inference Gb10 on GB10

Quantize models and activations to FP8/FP4 for fast Blackwell inference on GB10. Covers NVIDIA TensorRT Model Optimizer, cuBLASLt narrow-precision GEMM, and NVFP4 KV cache.

Skill: `.cursor/skills/fp8-fp4-quantization-inference-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/fp8-fp4-quantization-inference-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Benchmark and report throughput/latency
