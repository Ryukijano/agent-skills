# LLM Inference on DGX Spark (GB10)

## Description

vLLM and TensorRT-LLM inference on GB10: FP8 KV, Marlin, MTP, MoE backend selection, and driver 580.x.

## When to use

You are serving LLMs on a DGX Spark and need to choose quantization, attention backend, and MoE backend.

## Key concepts

- **FP8 KV cache**: safe and recommended; saves 50% KV memory.
- **NVFP4 not recommended on GB10**: native kernels are immature; Marlin/MXFP4 is more stable.
- **CUTLASS FP4 is broken on sm_121**: produces silent garbage (row-identical wrong values).
- **Marlin works**: set `VLLM_MARLIN_USE_ATOMIC_ADD=1` and `--moe-backend=marlin`.
- **MTP speculative decoding**: Qwen3.6/Gemma 4/Nemotron 3.5 Lightning; pair with FP8 KV.
- **Driver 580.x**: 590.x has CUDAGraph deadlock and UMA memory leak; pin it.

## Code pattern

```python
from vllm import LLM

llm = LLM(
    model="Qwen/Qwen3-35B-A3B",
    quantization="fp8",
    kv_cache_dtype="fp8",
    gpu_memory_utilization=0.85,
    attention_backend="TRITON_ATTN",
    moe_backend="marlin",
    enable_prefix_caching=True,
    enforce_eager=False,
)
```

## Tuning notes

- `max-cudagraph-capture-size=2048` is required for full throughput.
- `--attention-backend=TRITON_ATTN` is safer than FlashInfer on sm_121 for some FP8 paths.
- Use `mxfp4` only with gpt-oss pre-quantized checkpoints.

## Verification

1. Run a known-answer benchmark (e.g., OpenLLM leaderboard subset) and compare to BF16.
2. Check output for row-identical garbage (sign of CUTLASS FP4).
3. Monitor `nvidia-smi dmon` for thermal and power under sustained load.

## References

- https://conselara.dev/notes/vllm-dgx-spark-sm121-gotchas/
- https://conselara.dev/notes/dgx-spark-gb10-hardware-reference/
- https://forums.developer.nvidia.com/t/guide-deepseek-v4-flash-on-2x-dgx-spark-gb10/374742
- https://github.com/vllm-project/vllm/pull/40923
