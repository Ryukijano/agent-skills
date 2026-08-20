# AI for Photonic Hardware

## Description

Photonic AI accelerators, optical neural networks, optoelectronic co-design, and programming of photonic tensor cores.

## When to use

You are building or programming photonic AI accelerators, optical neural networks, or photonic tensor cores for matrix/vector and tensor operations.

## Key concepts

- **Photonic matrix-vector multiplication (MVM)**: Mach-Zehnder meshes, microring resonators, and coherent crossbars for analog linear transforms.
- **Optical nonlinearities and hybrid compute**: combining photonic linear layers with electronic nonlinearities and memory.
- **Photonic accelerator co-design**: algorithm, photonic device, and control/electronics co-optimization.
- **Calibration and error mitigation**: phase drift, crosstalk, and loss-aware training.

## Code pattern

```python
import numpy as np

# Coherent MVM using a unitary mesh (simplified)
theta = np.random.rand(n, n)
U = construct_unitary_mesh(theta)
y = np.abs(U @ x) ** 2
```

## Tuning notes

- Calibrate phase shifters and photodiode gains with on-chip feedback loops.
- Account for optical losses, crosstalk, and ADC/DAC precision in the training graph.
- Use digital pre-emphasis and error correction for high-precision AI workloads.

## Verification

1. Implement a photonic MVM accelerator in simulation and compare matrix-vector output to a digital baseline.
2. Run a small neural network (e.g., MNIST) on a photonic tensor core and report accuracy.
3. Characterize and compensate phase drift over time in a programmable photonic chip.

## References

- https://www.nature.com/articles/s41586-025-08854-x
- https://www.nature.com/articles/s41566-025-01799-7
- https://www.nature.com/articles/s41467-026-71599-2
- https://lightmatter.co/products/envise/
