# AI for Synthetic Controls

## Description

Construct synthetic control arms from historical or real-world data to augment clinical evidence.

## When to use

You have one or a few treated units and many untreated donor units, and need a credible counterfactual trajectory from a weighted combination of donors.

## Usage

- Build donor pools from aggregate and patient-level data.
- Estimate synthetic controls with penalized regression (pensynth).
- Quantify uncertainty with scpi prediction intervals.
- Validate pre-treatment fit and placebo tests.
- Support regulatory submissions with external comparators.

## Steps

1. Define the treated unit(s) and pre-treatment period.
2. Assemble a donor pool of similar historical controls.
3. Estimate donor weights and counterfactual trajectories.
4. Evaluate fit, placebo robustness, and sensitivity.
5. Report treatment effects with confidence intervals.

## Code pattern

```python
import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Pre-treatment outcome matrix: rows = time, columns = control units
Y_pre = donor_df.loc[donor_df["pre"] == 1, control_units].values
y_treated = treated_df.loc[treated_df["pre"] == 1, "outcome"].values

def sc_loss(w):
    return np.mean((Y_pre @ w - y_treated) ** 2)

res = minimize(sc_loss, x0=np.ones(Y_pre.shape[1]) / Y_pre.shape[1],
               method="SLSQP", bounds=[(0, 1)] * Y_pre.shape[1],
               constraints={"type": "eq", "fun": lambda w: np.sum(w) - 1})
```

## Tuning notes

- Exclude donors that are poor matches or place high weight on a single unit.
- Use cross-validation on pre-treatment periods to choose regularization.
- Apply placebo tests and leave-one-out robustness checks.
- Be cautious when using synthetic controls as primary evidence in regulatory settings.

## Verification

1. Replicate the California tobacco-control synthetic control case study.
2. Compare classic SCM, penalized SCM, and a learned-representation baseline.
3. Run placebo inference and show that treatment effects exceed the null distribution.

## References

- https://www.bis.org/publ/work1181.pdf
- https://doi.org/10.22541/au.176072431.11742213/v1
- https://arxiv.org/abs/2602.04611
- https://microsoft.github.io/SparseSC/
- https://www.mit.edu/~jhainm/Paper/ccs.pdf
