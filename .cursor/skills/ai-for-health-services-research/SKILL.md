# AI for Health Services Research

## Description

AI for healthcare access, quality, utilization, policy, workforce, and health-system performance.

## When to use

You are studying healthcare delivery, access, quality, utilization, or policy using observational data and machine learning.

## Key concepts

- **Health services research methods and quasi-experimental designs**: difference-in-differences, regression discontinuity, and interrupted time series.
- **Healthcare utilization, access, and disparities**: inpatient, outpatient, emergency, and preventive service use.
- **Quality measurement and patient safety**: readmissions, adverse events, and process-of-care metrics.
- **Health policy and economic evaluation**: policy impact, HTA, and resource allocation.
- **Machine learning for evidence synthesis and health system optimization**: systematic review automation and operations research.

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
