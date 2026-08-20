# Wafer-Scale AI

## Description

Cerebras Wafer Scale Engine, wafer-scale training and inference, and massive on-chip compute fabric.

## When to use

You need to train or serve massive AI models with massive on-chip memory and near-linear scaling by avoiding multi-GPU communication overhead.

## Key concepts

- **Wafer Scale Engine (WSE)**: a chip the size of an entire wafer (e.g., Cerebras WSE-3).
- **Giant on-chip memory and compute fabric**: hundreds of thousands of cores on one die.
- **Weight streaming / appliance mode**: scale out with external MemoryX and SwarmX nodes.
- **CSoft / Cerebras SDK**: PyTorch/XLA interface and C-like kernel language (CSL).
- **Fail-in-place architecture**: redundant cores and routing tolerate manufacturing defects.

## Code pattern

```python
import torch
import cerebras.pytorch as cbtorch

# Run a standard PyTorch model on a CS-3 with Cerebras XLA backend
model = MyModel()
# compile and run through cbtorch; exact API is hardware-dependent
```

## Tuning notes

- Wafer-scale systems excel at large-model training/inference on a single device.
- Use the Cerebras Weight Streaming cluster for multi-system scaling.
- Optimize data loading and compilation time for your model shapes.

## Verification

1. Profile a model on a wafer-scale system and compare throughput to a GPU baseline.
2. Measure scaling efficiency from one to multiple CS nodes.
3. Verify weight streaming and gradient accumulation produce identical convergence.

## References

- https://www.cerebras.ai/chip
- https://www.cerebras.ai/inference
- https://www.cerebras.ai/product-software
- https://www.cerebras.ai/blog/the-complete-guide-to-scale-out-on-cerebras-wafer-scale-clusters
