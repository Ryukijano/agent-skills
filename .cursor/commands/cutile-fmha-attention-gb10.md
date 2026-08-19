# Cutile Fmha Attention Gb10 on GB10

Implement fused multi-head attention (FMHA) with cuTile Python on GB10. Covers online softmax, causal masking, grouped-query attention (GQA) tiles, and FlashAttention-style tiling for inference.

Skill: `.cursor/skills/cutile-fmha-attention-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cutile-fmha-attention-gb10/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Benchmark and report throughput/latency
