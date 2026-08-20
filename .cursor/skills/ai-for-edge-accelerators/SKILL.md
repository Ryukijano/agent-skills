# AI for Edge Accelerators

## Description

NPU/TPU/FPGA edge accelerator design, benchmarking, mapping, and optimization for low-latency, energy-efficient inference.

## When to use

You are selecting, programming, or designing an edge AI accelerator (NPU, TPU, GPU, FPGA) and need to optimize inference throughput and energy.

## Key concepts

- **Edge NPU/TPU architectures**: dataflow, systolic arrays, and in-memory computing for low-power inference.
- **Model mapping and tiling**: schedule operators to maximize MAC utilization and minimize off-chip traffic.
- **Benchmarking**: MLPerf Tiny and MLPerf Edge provide fair accuracy/latency/energy metrics.
- **Hybrid precision and sparsity**: exploit int4/int8, block sparsity, and structured pruning on accelerator hardware.

## Code pattern

```python
import onnxruntime as ort
import numpy as np

# Run a quantized model on an edge NPU with ONNX Runtime
session = ort.InferenceSession("model.onnx", providers=["NPUExecutionProvider"])
out = session.run(None, {"input": np.zeros((1, 3, 224, 224), dtype=np.float32)})
```

## Tuning notes

- Align model operators with the accelerator's supported op set and tensor formats.
- Quantize activations and weights to the supported bit width; fall back to CPU for unsupported ops.
- Measure end-to-end latency and energy on the target board, not just layer-wise roofline.

## Verification

1. Benchmark an image-classification model on an edge NPU and report top-1 accuracy vs. latency.
2. Profile operator placement and memory movement for a transformer on a Jetson/Coral board.
3. Compare an int8-quantized model to a floating-point baseline on energy-delay product.

## References

- https://doi.org/10.48550/arxiv.2106.07597
- https://mlcommons.org/working-groups/benchmarks/tiny/
- https://www.mdpi.com/1999-4893/15/11/419
- https://doi.org/10.3390/electronics14244877
