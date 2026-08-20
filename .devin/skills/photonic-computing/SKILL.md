# Photonic Computing

## Description

Silicon photonics, optical processing units, and photonic interconnects for energy-efficient AI and HPC.

## When to use

You want to accelerate matrix-vector multiplications or interconnects using light, reducing energy and increasing bandwidth for AI/HPC.

## Key concepts

- **Silicon photonics**: integrate optical components on CMOS chips.
- **Optical Processing Unit (OPU)**: perform random projections in the analog optical domain.
- **Photonic interconnects**: replace electrical I/O with optical links for high bandwidth density.
- **Coherent and incoherent photonic accelerators**: MZIs, MRRs, and free-space optics.
- **Thermal/crosstalk calibration**: photonic devices are sensitive to temperature and phase drift.

## Code pattern

```python
# Example: LightOn OPU random projection via Python API
from lightonopu.opu import OPU
import numpy as np

opu = OPU()
X = np.random.randn(1000, 784).astype(np.float32)
Y = opu.transform(X)  # random feature map
```

## Tuning notes

- Photonic accelerators excel at large, high-dimensional linear transforms.
- Account for analog noise, drift, and finite precision when building models.
- Hybrid CPU/GPU/OPU pipelines are common; place OPU at the bottleneck layer.

## Verification

1. Run a random projection benchmark on an OPU and compare throughput to CPU/GPU.
2. Train a kernel/Ridge classifier on OPU features.
3. Measure energy per MAC and bit accuracy of optical outputs.

## References

- https://lightmatter.co/products/envise/
- https://arxiv.org/abs/2107.11814
- https://lightmatter.co/products/m1000/
- https://lightmatter.co/press-release/lightmatter-unveils-passage-m1000-photonic-superchip-worlds-fastest-ai-interconnect/
