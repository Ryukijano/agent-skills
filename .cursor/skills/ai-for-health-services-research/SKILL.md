# AI for Health Services Research

## Description

Analyze real-world care delivery and access patterns to identify disparities and evaluate whether digital tools improve equity.

## When to use

You are studying healthcare delivery, access, quality, utilization, or policy using observational data and machine learning.

## Usage

- Apply quasi-experimental designs to policy evaluation.
- Analyze utilization, access, and disparities.
- Measure quality and patient safety outcomes.
- Model resource allocation and system optimization.

## Steps

1. Apply quasi-experimental designs to policy evaluation.
2. Analyze utilization, access, and disparities.
3. Measure quality and patient safety outcomes.
4. Model resource allocation and system optimization.
5. Translate findings into policy and implementation.
6. Validate on local devices, clinical measurements, and diverse populations before embedding into EHR or public-health workflows (ChatEHR-style).

## Code pattern

```python
import pandas as pd
import statsmodels.formula.api as smf

# Difference-in-differences evaluation of a policy on hospital utilization
model = smf.ols('utilization ~ treatment_post + treatment + post + controls', data=df).fit()
print(model.params['treatment_post'])
```

## Tuning notes

- Use appropriate causal designs for policy and implementation studies.
- Address confounding and selection bias in observational claims or EHR data.
- Measure outcomes that matter to patients and health systems.
- Interpret findings for policy action and implementation feasibility.

## Verification

1. Evaluate a healthcare policy change using a difference-in-differences design.
2. Predict hospital readmissions and identify modifiable utilization drivers.
3. Map AI implementation barriers from a mixed-methods health services study.

## References

- https://link.springer.com/article/10.1186/s12913-025-12664-2
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9582911/
- https://link.springer.com/article/10.1186/s12913-023-10462-2
- https://www.ncbi.nlm.nih.gov/books/NBK620201/
