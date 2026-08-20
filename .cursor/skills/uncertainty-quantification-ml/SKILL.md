# Uncertainty Quantification in ML

## Description

Predictive uncertainty, calibration, conformal prediction, and Bayesian methods for reliable ML.

## When to use

You need to estimate and communicate the uncertainty of model predictions.

## Key concepts

- **Aleatoric vs epistemic uncertainty**: data noise vs model uncertainty.
- **Calibration**: match predicted confidence with observed accuracy.
- **Conformal prediction**: distribution-free prediction sets with coverage guarantees.
- **Bayesian methods**: MC dropout, variational inference, deep ensembles.

## Code pattern

```python
import numpy as np

# Conformal prediction: construct a prediction set
n = len(y_cal)
scores = 1 - proba_cal[y_cal]
q = np.quantile(scores, np.ceil((n+1)*(1-alpha))/n, method='higher')
```

## Tuning notes

- Ensembles often provide the best uncertainty estimates.
- Temperature scaling can fix overconfidence.
- Conformal prediction requires an exchangeable calibration set.

## Verification

1. Train an ensemble and measure prediction uncertainty on a held-out set.
2. Apply temperature scaling and check expected calibration error (ECE).
3. Build conformal prediction sets and verify coverage on test data.

## References

- https://arxiv.org/abs/2404.02678
- https://github.com/uncertainty-toolbox/uncertainty-toolbox
- https://arxiv.org/abs/2005.14137
- https://arxiv.org/abs/2107.07511
