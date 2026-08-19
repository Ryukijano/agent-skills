# Equivariant Neural Networks for Science

## Description

E(3)/SE(3)-equivariant networks (E3NN, Equiformer, MACE, NequIP, steerable CNNs) for atomic and molecular systems.

## When to use

You are building models for molecules, materials, point clouds, or 3D data where physical symmetries should be preserved.

## Key concepts

- **E(3) equivariance**: rotations, translations, reflections. Models built with irreducible representations (irreps).
- **E3NN**: PyTorch library for equivariant neural networks.
- **Equiformer/EquiformerV2**: transformer with equivariant attention.
- **NequIP/MACE/Allegro**: equivariant GNNs for interatomic potentials.
- **Steerable CNNs**: SO(2)/SO(3) steerable convolutions.

## Code pattern

```python
import e3nn
from e3nn import o3, nn

irreps = o3.Irreps("1x0e + 1x1o")
model = nn.Gate(...)
```

For MACE/NequIP, use the respective packages directly.

## Tuning notes

- Equivariant models are data-efficient but can be slower to train.
- Use `cuEquivariance` for fast tensor products on GPU.
- Match the symmetry group to the problem (E(3) for molecules, SE(2) for images).

## Verification

1. Train a small E3NN model and verify it is equivariant: `f(Rx) ≈ Rf(x)`.
2. Run a MACE training and compare forces/energies to a reference.
3. Check `cuEquivariance` is installed and active for 3×+ speedup.

## References

- https://e3nn.org/
- https://github.com/atomicarchitects/equiformer_v3
- https://github.com/ACEsuit/mace
- https://developer.nvidia.com/cuequivariance
