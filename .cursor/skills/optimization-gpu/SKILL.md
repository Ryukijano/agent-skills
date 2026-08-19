# Optimization for Scientific ML on GPU

## Description

First- and second-order optimization, Optax/JAXopt, L-BFGS, trust-region, constrained, and Newton-Krylov methods on GPU.

## When to use

You are training or solving an optimization problem on GPU and need to go beyond Adam/SGD.

## Key concepts

- **First-order**: SGD, AdamW, schedule-free (AdamW with no learning-rate schedule), Lion, Muon.
- **Second-order**: L-BFGS, Newton-CG, trust-region, Hessian-free methods.
- **JAX**: `optax` for stochastic, `jaxopt` for deterministic/constrained, `optimistix` for root finding.
- **PyTorch**: `pytorch-minimize`, `PyTorch-LBFGS`, `torch.optim.LBFGS`.
- **Newton-Krylov**: `scipy.optimize.newton_krylov` or Hessian-vector products in JAX/PyTorch.

## Code pattern

```python
import jax
import jax.numpy as jnp
import optax

optimizer = optax.adamw(1e-3)
params = model.init(...)
opt_state = optimizer.init(params)

@jax.jit
def train_step(params, opt_state, x, y):
    loss, grads = jax.value_and_grad(loss_fn)(params, x, y)
    updates, opt_state = optimizer.update(grads, opt_state, params)
    params = optax.apply_updates(params, updates)
    return params, opt_state, loss
```

## Tuning notes

- Second-order methods can converge in fewer steps but are expensive per step; use for small/medium deterministic problems.
- Use `jaxopt.ScipyBoundedMinimize` for constrained problems.
- For large neural nets, keep first-order; second-order is rarely worth it.

## Verification

1. Solve a small nonlinear least-squares with L-BFGS and compare to `scipy.optimize.minimize`.
2. Verify `jaxopt.GradientDescent` converges on a quadratic.
3. Check that GPU is used (e.g., `nvidia-smi` shows compute activity).

## References

- https://optax.readthedocs.io/en/stable/
- https://jaxopt.github.io/stable/
- https://github.com/patrick-kidger/optimistix
- https://github.com/rfeinman/pytorch-minimize
