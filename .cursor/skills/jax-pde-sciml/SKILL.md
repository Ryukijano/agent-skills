# JAX for PDEs and Differentiable Scientific Computing

## Description

JAX-based SciML: Diffrax, Exponax, JAX-MD, neural operators, and differentiable simulations.

## When to use

You are solving PDEs, ODEs, running differentiable MD, or implementing neural operators in JAX.

## Key concepts

- **Diffrax**: ODE/SDE/CDE solvers with JIT and AD support.
- **Exponax**: spectral PDE solvers for 46+ equations.
- **JAX-MD**: differentiable molecular dynamics.
- **JAX-FEM**: finite element analysis with AD.
- **Neural operators**: FNO, DeepONet, PINO.

## Code pattern

```python
import jax
import jax.numpy as jnp
from diffrax import Tsit5, ODETerm, diffeqsolve

def f(t, y, args):
    return -y

term = ODETerm(f)
sol = diffeqsolve(term, Tsit5(), t0=0, t1=1, dt0=0.1, y0=1.0)
```

## Tuning notes

- Use `jax.vmap` for batched trajectories.
- For long rollouts, use `jax.lax.scan` instead of Python loops.
- `jax.jit` can compile the whole solver; use `saveat` to avoid storing all intermediates.

## Verification

1. Solve a linear ODE and compare to analytic solution.
2. Train an FNO on 1D Burgers and compare to finite-difference.
3. Run JAX-MD energy minimization and compare to a reference MD package.

## References

- https://docs.kidger.site/diffrax/
- https://github.com/ceyron/exponax
- https://github.com/jax-md/jax-md
- https://github.com/deepmodeling/jax-fem
