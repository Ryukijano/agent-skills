# AI for Edge Computing

## Description

Model compression, inference offloading, task placement, federated learning, and MLOps at the network edge.

## When to use

You need to deploy, orchestrate, or optimize ML inference and training at the edge for low latency, privacy, and bandwidth savings.

## Key concepts

- **Edge inference and model serving**: TensorFlow Lite, ONNX Runtime, NVIDIA Triton.
- **Offloading decisions**: when to run on device, edge, or cloud.
- **Model compression**: quantization, pruning, knowledge distillation.
- **Federated and split learning**: train and infer across distributed edge nodes.
- **Edge MLOps**: continuous deployment, drift detection, and A/B testing at the edge.

## Code pattern

```python
import numpy as np
from scipy.optimize import linear_sum_assignment

# Cost matrix: tasks x edge nodes (latency estimate)
cost = np.array([[10, 25, 60], [15, 8, 50], [30, 20, 12]])
row_ind, col_ind = linear_sum_assignment(cost)
print("Assignments:", list(zip(row_ind, col_ind)))
```

## Tuning notes

- Profile end-to-end latency, energy, and memory, not just model accuracy.
- Use quantization-aware training for integer accelerators.
- Cache popular models and data near users; monitor drift on edge telemetry.
- Validate offloading policies under bandwidth and battery constraints.

## Verification

1. Quantize a model and measure accuracy and latency on an edge device.
2. Optimize task offloading across a set of edge nodes and compare to a greedy baseline.
3. Run a small federated-learning round and evaluate convergence vs. centralized.

## References

- https://doi.org/10.3390/fi17090417
- https://ieeexplore.ieee.org/document/9933792
- https://www.mdpi.com/2227-7080/12/6/81
- https://www.mdpi.com/2673-8732/5/2/16
