# Edge AI and On-Device Machine Learning

## Description

Quantization, pruning, knowledge distillation, neural architecture search, and deployment of ML models on mobile, embedded, and edge accelerators.

## When to use

You need to run ML inference (or training) on constrained devices where latency, privacy, or connectivity limit cloud offloading.

## Key concepts

- **Model compression**: quantization, pruning, knowledge distillation, low-rank factorization.
- **Edge tiers**: mobile, embedded SoC, edge gateway, near-edge server.
- **Hardware accelerators**: NPU, GPU, DSP, TPU, and custom inference chips.
- **Deployment runtimes**: TensorRT, ONNX Runtime, OpenVINO, TensorFlow Lite, Core ML.
- **Accuracy-latency trade-off**: choose quantization bits and model size to meet SLOs.

## Code pattern

```python
import torch
import torch.quantization

# Dynamic post-training quantization of a PyTorch model
model = torch.load('model.pt', map_location='cpu')
model.eval()
quantized_model = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)

# Export to ONNX for an edge runtime
x = torch.randn(1, 3, 224, 224)
torch.onnx.export(quantized_model, x, 'model_quantized.onnx', opset_version=13)
```

## Tuning notes

- Quantize-aware training (QAT) usually preserves accuracy better than post-training quantization.
- Profile latency on the target device, not just the development workstation.
- Beware of operator support differences across runtimes (e.g., ONNX opset).
- Use batching, parallel execution, and memory planning to maximize throughput.

## Verification

1. Quantize a model and compare top-1 accuracy on a validation set before and after.
2. Benchmark end-to-end latency on the target edge device.
3. Run an operator coverage check for the chosen runtime.

## References

- https://arxiv.org/abs/2403.17154
- https://arxiv.org/abs/2411.00907
- https://arxiv.org/abs/1806.07846
- https://arxiv.org/abs/2605.26119
- https://arxiv.org/abs/2604.14661
