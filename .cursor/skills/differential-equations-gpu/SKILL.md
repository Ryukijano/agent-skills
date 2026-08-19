# Differential Equations on GPU

## Description

ODE/PDE/SDE solvers, spectral and finite element methods, Diffrax, FEniCSx, PETSc, and NekRS on GPU.

## When to use

You are solving ODEs, PDEs, or SDEs in scientific ML on GPU.

## Key concepts

- **ODE/SDE solvers**: Diffrax (JAX), `torchdiffeq`, `torchsde`.
- **Finite element**: FEniCSx with `cuDOLFINx` plugin for GPU assembly.
- **PETSc**: GPU back end (`AIJCUSPARSE`, `MATAIJKOKKOS`) for sparse solvers.
- **Spectral element**: NekRS, JAX-Fluids, PhiFlow.
- **Neural differential equations**: solve ODEs inside a neural network with `jax.experimental.ode` or Diffrax.

## Code pattern

```python
import jax
import jax.numpy as jnp
from diffrax import diffeqsolve, Dopri5, ODETerm, SaveAt

term = ODETerm(lambda t, y, args: -y)
sol = diffeqsolve(term, Dopri5(), t0=0, t1=1, dt0=0.1, y0=1.0, saveat=SaveAt(ts=jnp.linspace(0, 1, 10)))
```

## Tuning notes

- Use adaptive step-size controllers (PID) for stiff or multi-scale problems.
- FEniCSx/PETSc multi-GPU scaling requires MPI and matching CUDA-aware MPI.
- Spectral methods (NekRS) can scale to thousands of GPUs but need good meshes.

## Verification

1. Solve a linear ODE with known analytic solution; check RMSE.
2. Run FEniCSx Poisson on GPU and compare to CPU result.
3. Benchmark Diffrax `Tsit5` vs `scipy.integrate.solve_ivp`.

## References

- https://docs.kidger.site/diffrax/
- https://fenicsproject.org/
- https://petsc.org/release/overview/gpu_roadmap/
- https://github.com/tumaer/jaxfluids
