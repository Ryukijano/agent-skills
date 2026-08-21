# AI for Learning Analytics

## Description

Mine LMS logs and assessment traces to predict at-risk students and trigger timely advising interventions.

## When to use

You want to turn LMS logs, assessment records, and behavioral traces into actionable insight about student progress, risk, and course effectiveness.

## Usage

- Ingest LMS logs, assessment records, and behavioral traces.
- Engineer time-on-task, resource access, forum, and submission features.
- Model mastery trajectories with DKT and BKT.
- Train at-risk predictors and build an early-warning dashboard.

## Steps

1. Ingest LMS logs, assessment records, and behavioral traces.
2. Engineer time-on-task, resource access, forum, and submission features.
3. Model mastery trajectories with DKT and BKT.
4. Train at-risk predictors and build an early-warning dashboard.
5. Trigger advisor interventions and audit for subgroup fairness.
6. Integrate with LMS and virtual-teaching-assistant telemetry, then A/B test AI scaffolds and engagement interventions (JELAI-style).

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Build simple at-risk predictor from LMS engagement features
X = df[["logins_per_week", "assignments_completed", "forum_posts", "quiz_avg"]]
y = df["at_risk"]
model = GradientBoostingClassifier(random_state=42).fit(X, y)
df["risk_score"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Use time-based train/test splits to avoid look-ahead leakage.
- Prefer interpretable features so instructors can trust and act on alerts.
- Integrate predictions with advising workflows rather than using them in isolation.

## Verification

1. Build an engagement dashboard from an LMS export.
2. Train a dropout predictor and evaluate AUC on a held-out term.
3. Compare a DKT model to a baseline logistic model on a public knowledge-tracing dataset.

## References

- https://doi.org/10.1145/3636555.3636856
- https://doi.org/10.18608/jla.2024.8367
- https://arxiv.org/abs/2504.11481
- https://doi.org/10.1007/s40593-024-00429-7
