# AI for Health Economics

## Description

Use AI to evaluate the economic value, cost-effectiveness, or budget impact of health technologies and interventions using ML.

## When to use

You are evaluating the economic value, cost-effectiveness, or budget impact of health technologies and interventions using ML.

## Usage

- Build cost, QALY, and budget-impact models.
- Estimate causal treatment effects from observational data.
- Run probabilistic sensitivity and bootstrapping.
- Report ICER and acceptability curves.

## Steps

1. Build cost, QALY, and budget-impact models.
2. Estimate causal treatment effects from observational data.
3. Run probabilistic sensitivity and bootstrapping.
4. Report ICER and acceptability curves.
5. Align with payer, societal, and health-system perspectives.
6. Validate on local devices, clinical measurements, and diverse populations before embedding into EHR or public-health workflows (ChatEHR-style).

## Code pattern

```python
import numpy as np

# Compute incremental cost-effectiveness ratio (ICER)
delta_cost = mean_cost_new - mean_cost_standard
delta_qaly = mean_qaly_new - mean_qaly_standard
icer = delta_cost / delta_qaly
print("ICER:", icer)
```

## Tuning notes

- Align cost and outcome perspectives (payer, societal, health system).
- Use bootstrapping or probabilistic sensitivity analysis for uncertainty.
- Account for treatment selection bias with propensity scores or instrumental variables.
- Report incremental net health benefit and cost-effectiveness acceptability curves.

## Verification

1. Replicate a cost-effectiveness analysis with bootstrapped confidence intervals.
2. Estimate a causal treatment effect from observational claims data.
3. Build an acceptability curve and compare it to a cost-effectiveness threshold.

## References

- https://doi.org/10.1016/j.jval.2026.01.014
- https://link.springer.com/article/10.1186/s13561-025-00645-4
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11786987/
- https://doi.org/10.1016/j.jval.2023.09.2123
