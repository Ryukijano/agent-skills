# FP8 Training with Transformer Engine on Hopper

## Description

FP8 recipes (E4M3/E5M2, current, delayed, and blockwise scaling) with Transformer Engine for LLM training.

## When to use

You are training large transformers on H100/H200/Blackwell and want to use FP8 to reduce memory and increase throughput.

## Key concepts

- **E4M3** for forward activations and weights; **E5M2** for backward gradients.
- **Per-tensor scaling**: one scale per tensor. Fast but can lose precision for high dynamic range.
- **Delayed scaling**: uses the previous iteration's max-abs to set the current scale.
- **Current scaling**: computes scale from the current tensor.
- **Blockwise scaling**: scale per block (e.g., 128 elements) for fine-grained dynamic range. Newer, better for accuracy.

## Code pattern

```python
import transformer_engine.pytorch as te

# FP8 linear with current scaling recipe
model = te.Linear(4096, 4096)
# Use TransformerEngine recipe with blockwise scales for matmuls
```

## Tuning notes

- Keep first and last layers in BF16 for numerical stability.
- Use FP8 only for matrix multiplications; LayerNorm and embeddings stay in BF16.
- When accuracy regresses, switch to blockwise scaling or retain master weights in FP32.

## Verification

1. Run a small Transformer layer with and without FP8 and compare loss curves.
2. Check `te.fp8_autocast()` context produces the expected `amax` history.
3. Profile memory: FP8 should reduce activation and weight footprint by ~40-50%.

## References

- https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/examples/fp8_primer.html
- https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/fp8_current_scaling/fp8_current_scaling.html
- https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/fp8_blockwise_scaling/fp8_blockwise_scaling.html
- https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/fp8_delayed_scaling/fp8_delayed_scaling.html
