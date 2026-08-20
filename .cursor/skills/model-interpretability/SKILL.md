# Model Interpretability

## Description

Intrinsic and post-hoc methods for understanding model behavior, features, and decision boundaries.

## When to use

You need to understand which inputs, features, or concepts drive model decisions.

## Key concepts

- **Intrinsic interpretability**: decision trees, linear models, attention weights.
- **Post-hoc explanation**: SHAP, LIME, counterfactuals, prototypes.
- **Feature interactions**: H-statistics, partial dependence, ICE curves.
- **Concept-based methods**: TCAV, concept bottleneck models.

## Code pattern

```python
from sklearn.inspection import partial_dependence

result = partial_dependence(model, X, features=[0])
pd_values = result["average"]
```

## Tuning notes

- Simpler models are easier to interpret but may be less accurate.
- Post-hoc explanations can be unstable; test on multiple samples.
- Explainability needs differ by stakeholder.

## Verification

1. Train a decision tree and an MLP on the same tabular task; compare performance and interpretability.
2. Compute partial dependence for the top two features.
3. Generate counterfactual explanations for a few instances.

## References

- https://link.springer.com/article/10.1007/s10994-025-06852-8
- https://arxiv.org/abs/2506.06330
- https://christophm.github.io/interpretable-ml-book/
- https://github.com/tensorflow/tcav
