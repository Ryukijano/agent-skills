# AI for Insurance

## Description

Underwriting triage, claims automation, fraud detection, and AI-assisted pricing and reserving.

## When to use

You are building predictive models for underwriting, claims, fraud, pricing, or customer churn in insurance operations.

## Key concepts

- **Underwriting risk scoring**: predict loss cost and quote appropriate premiums.
- **Claims automation**: triage, document understanding, and fast-track routing.
- **Fraud and leakage detection**: identify suspicious patterns and provider behavior.
- **Pricing and reserving**: combine ML with actuarial methods for ratemaking.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Claims fraud detection from claim features and history
X = df[["claim_amount", "time_since_policy", "prior_claims", "provider_flags"]]
y = df["fraud"]
clf = RandomForestClassifier(class_weight="balanced_subsample", random_state=42).fit(X, y)
```

## Tuning notes

- Respect anti-discrimination and fair-lending regulations in features.
- Calibrate probability estimates for pricing and reserve decisions.
- Use temporal validation because claim patterns change over time.
- Explain model decisions to underwriters, adjusters, and regulators.

## Verification

1. Build a fraud model and report precision-recall at the top decile.
2. Predict claim severity and compare to actuarial baseline.
3. Test an underwriting triage workflow and measure straight-through processing.

## References

- https://arxiv.org/abs/2605.18784v2
- https://arxiv.org/html/2606.05449v1
- https://doi.org/10.48550/arxiv.2506.18942
- https://arxiv.org/abs/2306.01149
