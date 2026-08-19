# Fused Attention Inference Gb10 on GB10

Build fused attention kernels for fast LLM inference on GB10. Covers online softmax, FlashAttention tiling, KV-cache slicing, and causal/left-padding masks.

Skill: `.cursor/skills/fused-attention-inference-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/fused-attention-inference-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Benchmark and report throughput/latency
