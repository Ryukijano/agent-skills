# Astrophysics and Cosmology ML on GPU

## Description

Gravitational lensing, galaxy classification, N-body simulations, dark matter mapping, and cosmological parameter inference.

## When to use

You are applying ML to astrophysics or cosmology problems, especially with survey data or N-body simulations.

## Key concepts

- **Gravitational lensing**: GIGA-Lens, TinyLensGPU, GLaD for lens modeling.
- **N-body simulations**: GADGET-4, Shenqi, BlueTides, ASTRID.
- **Galaxy classification**: CNNs, vision transformers on DESI/Euclid/LSST images.
- **Cosmological inference**: emulator-based, simulation-based inference (SBI), neural density estimators.
- **GPU**: JAX/TensorFlow for lens modeling; CUDA for tree-walk gravity.

## Code pattern

```python
import jax
import jax.numpy as jnp

# JAX-based lens model
# TinyLensGPU / GIGA-Lens use NumPyro/TensorFlow for posterior sampling
```

For N-body:

```bash
# Run GADGET-4 or Shenqi with MPI+CUDA
mpirun -np 8 ./Shenqi param.txt
```

## Tuning notes

- Survey images can be large; use data augmentations and TFRecord/WebDataset.
- N-body codes need excellent MPI-GPU load balancing.
- Use simulation-based inference for expensive forward models.

## Verification

1. Classify 1000 galaxy images and compare accuracy to published baselines.
2. Run a small N-body box and check halo mass function against a reference.
3. Recover a lens parameter with MCMC and compare to known truth.

## References

- https://iopscience.iop.org/article/10.3847/1538-4357/ac6de4
- https://github.com/caoxiaoyue/TinyLensGpu
- https://github.com/MP-Gadget/shenqi
- https://arxiv.org/html/2606.17145
