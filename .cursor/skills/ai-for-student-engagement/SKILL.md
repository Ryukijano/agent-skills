# AI for Student Engagement

## Description

Use AI to identify disengaged or at-risk learners and trigger timely, evidence-based supports before performance declines.

## When to use

You want to identify disengaged or at-risk learners and trigger timely, evidence-based supports before performance declines.

## Usage

- Collect LMS, academic, and self-report signals.
- Build engagement features and risk scores.
- Match at-risk students to supports.
- Send timely nudges to students and advisors.

## Steps

1. Collect LMS, academic, and self-report signals.
2. Build engagement features and risk scores.
3. Match at-risk students to supports.
4. Send timely nudges to students and advisors.
5. Measure re-engagement and equity of intervention reach.
6. Integrate with LMS and virtual-teaching-assistant telemetry, then A/B test AI scaffolds and engagement interventions (JELAI-style).

## Code pattern

```python
import pandas as pd
from xgboost import XGBClassifier

X = df[["login_count", "time_on_platform", "assignments_late", "discussion_posts", "prior_gpa"]]
y = df["disengaged"]

model = XGBClassifier(eval_metric="logloss", random_state=42)
model.fit(X, y)
df["engagement_risk"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Use chronological splits and avoid leakage from future events.
- Combine LMS data with academic and demographic context carefully.
- Address surveillance and equity concerns by involving students and advisors.

## Verification

1. Build an engagement dashboard from a course LMS export.
2. Predict at-risk status weekly and evaluate precision-recall over time.
3. Run a small intervention pilot and measure re-engagement rates.

## References

- https://www.sciencedirect.com/science/article/pii/S0160791X24000228
- https://doi.org/10.1145/3636555.3636906
- https://www.frontiersin.org/articles/10.3389/feduc.2024.1421479
- https://learning-analytics.info/index.php/JLA/article/view/7985
