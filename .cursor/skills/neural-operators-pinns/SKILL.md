# Neural Operators and Physics-Informed ML on GPU

## Description

Fourier Neural Operator, DeepONet, PINNs, and JAX/Diffrax/Exponax for PDEs on GPU.

## When to use

You are solving parametric PDEs, surrogate modeling, or physics-constrained ML on GPU.

## Key concepts

- **FNO (Fourier Neural Operator)**: global convolutions in frequency space.
- **DeepONet**: branch-net + trunk-net for operator learning from function pairs.
- **PINNs**: add PDE residual to the loss; good for inverse problems.
- **PINO**: pre-train on coarse data, fine-tune with PDE constraints at higher resolution.
- **JAX tools**: Diffrax (ODE/SDE), Exponax (spectral PDEs), JAX-MD, JAX-FEM.

## Code pattern

```python
import jax
import jax.numpy as jnp
from diffrax import diffeqsolve, Tsit5

term = ...
sol = diffeqsolve(term, Tsit5(), t0=0, t1=1, dt0=0.01, y0=y0)
```

## Tuning notes

- PINNs can be hard to train; start with FNO if data is available.
- Use adaptive activations (tanh with learnable frequency) for multi-scale PDEs.
- JAX `jax.vmap` is powerful for batched parameter sweeps.

## Verification

1. Train FNO on Darcy flow and compare relative L2 to a spectral solver.
2. Solve a 1D Burgers equation with PINN and compare to finite-difference.
3. Run Diffrax ODE solve and compare to scipy.

## References

- https://arxiv.org/abs/2111.03794v4
- https://docs.kidger.site/diffrax/
- https://github.com/ceyron/exponax
- https://github.com/jax-md/jax-md
