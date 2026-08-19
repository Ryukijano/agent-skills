# Bayesian Inference and Gaussian Processes on GPU

## Description

MCMC, NUTS, variational inference, NumPyro, BlackJAX, and GPyTorch on NVIDIA GPUs.

## When to use

You need uncertainty estimates, posterior sampling, or Bayesian model calibration on GPU.

## Key concepts

- **MCMC**: HMC, NUTS, MALA, Langevin. Use `numpyro` or `blackjax` for JIT-compiled samplers.
- **VI**: ADVI, mean-field, pathfinder. Faster but approximate.
- **Gaussian Processes**: MVM-based inference (BBMM) in `gpytorch`; avoids Cholesky O(N³).
- **GPU**: JAX/PyTorch back ends compile log-prob and kernels to CUDA.

## Code pattern

```python
import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS

def model(x, y):
    alpha = numpyro.sample("alpha", dist.Normal(0, 10))
    beta = numpyro.sample("beta", dist.Normal(0, 1))
    numpyro.sample("obs", dist.Normal(alpha + beta * x, 0.1), obs=y)

mcmc = MCMC(NUTS(model), num_warmup=500, num_samples=1000)
mcmc.run(jax.random.PRNGKey(0), x, y)
```

For GPyTorch:

```python
import gpytorch
model = ExactGPModel(train_x, train_y, likelihood)
model = model.cuda()
model.train(); likelihood.train()
```

## Tuning notes

- NUTS needs gradients; JAX is ideal.
- For large GPs, use variational sparse approximations or SKI/KISS-GP.
- Set `numpyro.set_host_device_count(n)` for CPU parallelism; on GPU, one chain per GPU is typical.

## Verification

1. Run NUTS on a simple Bayesian linear regression and compare posterior means to analytic solution.
2. Train a small GPyTorch GP and check predictive log-likelihood.
3. Verify `jax.devices()` shows the GPU and the kernel is running there.

## References

- https://pyro.ai/numpyro/
- https://blackjax-devs.github.io/blackjax/
- https://docs.gpytorch.ai/
- https://github.com/patrick-kidger/diffrax
