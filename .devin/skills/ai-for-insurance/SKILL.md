# AI for Insurance

## Description

Score claims for fraud and triage underwriting by combining image metadata, network linkages, and historical loss patterns.

## When to use

You are building predictive models for underwriting, claims, fraud, pricing, or customer churn in insurance operations.

## Usage

- Ingest underwriting, claims, and policy data.
- Build risk, fraud, and severity models.
- Calibrate probabilities and pricing.
- Automate triage and fast-track routing.

## Steps

1. Ingest underwriting, claims, and policy data.
2. Build risk, fraud, and severity models.
3. Calibrate probabilities and pricing.
4. Automate triage and fast-track routing.
5. Audit for anti-discrimination and distribution shift.
6. Deploy in client engagements, capture requirements from discovery calls, and measure time-to-insight and decision quality (Task-GenAI Fit-style).

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
- https://arxiv.org/abs/2606.05449v1
- https://doi.org/10.48550/arxiv.2506.18942
- https://arxiv.org/abs/2306.01149
