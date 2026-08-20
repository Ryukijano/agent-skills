# Stochastic Processes and Neural SDEs for ML

## Description

Itô calculus, score-based generative models, neural SDEs, rough paths, and continuous-time generative modeling.

## When to use

You are modeling continuous-time stochastic systems, time series, or score-based generative models.

## Key concepts

- **Itô calculus**: stochastic integrals with respect to Brownian motion.
- **Diffusion/SDE models**: forward noising and reverse-time SDE.
- **Neural SDEs**: learn drift/diffusion with neural networks.
- **Rough paths**: handle low-regularity stochastic processes.

## Code pattern

```python
import torchsde

sde = SDE(...)
y0 = torch.randn(batch, dim)
ys = torchsde.sdeint(sde, y0, ts)
```

## Tuning notes

- Use adaptive SDE solvers for stiff or multi-scale problems.
- Score matching can be replaced by flow matching for faster training.
- Neural CDEs/SDEs are good for irregular time series.

## Verification

1. Solve a simple SDE and compare moments to analytic solution.
2. Train a small diffusion/score model and sample.
3. Fit a neural SDE to a time series and compare to ODE baseline.

## References

- https://github.com/google-research/torchsde
- https://proceedings.neurips.cc/paper_files/paper/2023/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf
- https://arxiv.org/html/2106.10340
- https://proceedings.mlr.press/v139/kidger21b/kidger21b.pdf
