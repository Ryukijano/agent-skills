# Materials Discovery with Generative ML on GPU

## Description

MatterGen, GNoME, DiffCSP, CDVAE, and crystal structure generation on GPU.

## When to use

You are generating or screening novel inorganic materials and crystal structures.

## Key concepts

- **MatterGen**: diffusion model for inorganic materials; 2× stable/novel rate over prior methods.
- **GNoME**: graph network for materials exploration; discovered 380k+ stable structures.
- **DiffCSP**: periodic E(3)-equivariant diffusion in fractional coordinates.
- **CDVAE**: SE(3)-invariant VAE for periodic structures.
- **Materials Project / CSD**: training data sources.

## Code pattern

```python
from mattergen import MatterGen
model = MatterGen.load_from_checkpoint("checkpoint/")
structures = model.generate(num_samples=100)
```

## Tuning notes

- Training requires large batches and stable E(3) equivariance; use `bfloat16` with care.
- GNoME models can be fine-tuned on local datasets.
- Validate generated structures with DFT (VASP, Quantum ESPRESSO) or a surrogate model.

## Verification

1. Generate 100 structures and compute validity / uniqueness / novelty.
2. Relax with a universal MLP (CHGNet, MACE) and check convex-hull distance.
3. Compare to known stable materials from Materials Project.

## References

- https://github.com/microsoft/mattergen
- https://github.com/google-deepmind/materials_discovery
- https://github.com/jiaor17/DiffCSP
- https://github.com/txie-93/cdvae
