# Uncertainty Quantification in Scientific ML

## Description

Conformal prediction, evidential learning, Bayesian neural nets, ensembles, Fortuna, and UQ for PDE surrogates.

## When to use

You need calibrated uncertainty for safety-critical scientific predictions.

## Key concepts

- **Ensembles**: deep ensembles for epistemic uncertainty.
- **MC dropout**: cheap approximate Bayesian inference.
- **Conformal prediction**: coverage guarantees for prediction sets.
- **Evidential deep learning**: model uncertainty as evidence distributions.
- **Fortuna**: scalable UQ library built on Flax/JAX.

## Code pattern

```python
from fortuna import ProbRegressor
import jax

prob_model = ProbRegressor()
status = prob_model.train(train_data_loader, ...)
means = prob_model.predictive.mean(inputs)
```

Conformal:

```python
from nonconformist import IcpRegressor
icp = IcpRegressor(model)
icp.calibrate(calibration_x, calibration_y)
prediction_sets = icp.predict(test_x, significance=0.1)
```

## Tuning notes

- Conformal prediction requires exchangeable data; adapt for time-series/distribution shift.
- Evidential learning needs careful priors to avoid overconfident predictions.
- Ensembles scale linearly in compute but are easy to implement.

## Verification

1. Train an ensemble and measure calibration error (ECE).
2. Apply conformal prediction and verify marginal coverage on held-out data.
3. Test uncertainty on OOD inputs; uncertainty should increase.

## References

- https://fortuna.readthedocs.io/
- https://arxiv.org/pdf/1806.01768
- https://iopscience.iop.org/article/10.1088/2632-2153/ae2e7b
- https://proceedings.mlr.press/v267/gopakumar25a.html
