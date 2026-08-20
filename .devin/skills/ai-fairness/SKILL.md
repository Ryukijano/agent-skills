# Fairness in Machine Learning

## Description

Detect, measure, and mitigate bias across demographic groups in classification, ranking, and regression.

## When to use

You are concerned that model predictions may be unfair to individuals or groups defined by protected attributes.

## Key concepts

- **Fairness criteria**: demographic parity, equalized odds, calibration.
- **Disparate impact**: statistical evidence of differential treatment.
- **Bias mitigation**: pre-processing, in-processing, post-processing.
- **Intersectionality**: fairness across combinations of protected attributes.

## Code pattern

```python
from aif360.sklearn.metrics import disparate_impact_ratio
from aif360.sklearn.inprocessing import AdversarialDebiasing

ratio = disparate_impact_ratio(y_true, y_pred, prot_attr='gender')
print(ratio)
```

## Tuning notes

- Choose a fairness criterion grounded in the deployment context.
- Fairness often conflicts with accuracy; document trade-offs.
- Test across subgroups and intersectional groups.

## Verification

1. Compute demographic parity and equalized odds on a dataset.
2. Apply a debiasing method and re-measure fairness metrics.
3. Evaluate whether accuracy drops disproportionately for any group.

## References

- https://arxiv.org/abs/2406.06330
- https://aif360.res.ibm.com/
- https://fairlearn.org/
- https://arxiv.org/abs/2402.08662
