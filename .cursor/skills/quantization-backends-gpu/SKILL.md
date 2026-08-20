# LLM Quantization Backends on NVIDIA GPUs

## Description

AWQ, GPTQ, AutoRound, Marlin, FP8, NVFP4, MXFP4, and backend selection for A100/H100/L40S/RTX50/GB10.

## When to use

You are quantizing or serving LLMs with reduced precision and need to pick the right method and backend for the GPU.

## Key concepts

- **AWQ**: activation-aware, protects 1% salient weights, ~10 min for 8B.
- **GPTQ**: Hessian-based, slower, supports 2/3/4-bit.
- **AutoRound**: sign-gradient descent, minimal tuning, exports to GPTQ/AWQ/GGUF.
- **Marlin**: optimized FP16×INT4 kernel for Ampere+ (sm_80+).
- **FP8**: E4M3/E5M2, good for H100/Blackwell.
- **NVFP4**: NVIDIA native 4-bit with hierarchical scaling; best on B200/GB200.
- **MXFP4**: cross-platform microscaling 4-bit, works on AMD and NVIDIA.

## Code pattern

```python
# AutoRound
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b",
    quantization_config=AutoRoundConfig(bits=4, group_size=128)
)

# vLLM Marlin
vllm serve model --quantization gptq_marlin --moe-backend marlin
```

## Tuning notes

- A100/H100: FP8/Marlin for memory-bound; INT4 for larger models.
- L40S: good for 7B-30B INT4/Marlin.
- RTX 50/GB10: Marlin is most reliable; NVFP4/MXFP4 need specific checkpoints.
- Backend priority: AutoRound selects Marlin > ExLLaMAV2 > Triton.

## Verification

1. Quantize a 7B model with AWQ and GPTQ and compare perplexity.
2. Serve with vLLM and measure throughput at batch 1 and 16.
3. Verify no garbage output with Marlin and no CUTLASS FP4 path on sm_121.

## References

- https://huggingface.co/docs/transformers/en/quantization/selecting
- https://github.com/intel/auto-round
- https://github.com/IST-DASLab/marlin
- https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/
- https://arxiv.org/abs/2509.23202v3
