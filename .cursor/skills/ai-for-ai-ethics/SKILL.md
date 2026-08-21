# AI for AI Ethics

## Description

Audit automated hiring and public-sector AI systems for disparate impact, transparency gaps, and compliance with bias-auditing laws like NYC Local Law 144.

## When to use

You need to identify, measure, and mitigate ethical risks such as bias, discrimination, privacy violations, lack of transparency, or harm in an AI system or dataset.

## Usage

- Audit models for demographic parity, equalized odds, and calibration across groups.
- Generate SHAP, LIME, and counterfactual explanations for high-stakes decisions.
- Maintain model cards, datasheets, and algorithmic audit logs.
- Apply differential privacy, consent, and data minimization practices.
- Engage stakeholders and use value-sensitive design.

## Steps

1. Define the protected groups and ethical risks for the use case.
2. Run a quantitative fairness audit and report subgroup performance.
3. Generate explanations and conduct stakeholder impact assessments.
4. Choose and apply an intervention (reweighting, threshold tuning, etc.).
5. Re-audit the system and document trade-offs in a model card.
6. Establish ongoing monitoring and governance for ethical risks.

## Code pattern

```python
from fairlearn.metrics import demographic_parity_difference, equalized_odds_difference

# Audit a classifier for fairness across a protected group
y_pred = model.predict(X_test)
dp = demographic_parity_difference(y_test, y_pred, sensitive_features=A_test)
eo = equalized_odds_difference(y_test, y_pred, sensitive_features=A_test)
print("DP:", dp, "EO:", eo)
```

## Tuning notes

- Choose a fairness criterion that matches the legal, social, and business context.
- Report subgroup performance and intersectional metrics, not just aggregate.
- Pair quantitative audits with qualitative stakeholder impact assessments.
- Document limitations and intended use in model cards and datasheets.

## Verification

1. Run a fairness audit on a credit or hiring model and report disparities by protected group.
2. Generate SHAP or counterfactual explanations for high-stakes decisions.
3. Compare an intervention (e.g., reweighting or threshold tuning) against a baseline across metrics.

## References

- https://arxiv.org/abs/2402.08323
- https://arxiv.org/abs/2311.17228
- https://arxiv.org/abs/2107.06641
- https://arxiv.org/abs/2411.09973
