# AI for Sales

## Description

Predictive lead scoring, sales forecasting, opportunity win probability, next-best action, and pipeline analytics.

## When to use

You want to prioritize leads, forecast revenue, reduce churn, or guide sales reps toward the next best action.

## Key concepts

- **Predictive lead scoring**: estimate conversion probability from firmographic and engagement signals.
- **Pipeline forecasting**: time-series or classification models to predict bookings and close dates.
- **Opportunity win probability**: models updated with CRM stage, activity, and sentiment features.
- **Next-best action**: recommend the next call, email, content, or offer to advance a deal.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

X = df[["email_opens", "demo_attended", "company_size", "page_views"]]
y = df["converted"]

model = GradientBoostingClassifier(random_state=42).fit(X, y)
df["lead_score"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Use chronological splits to avoid leakage from future activities into lead scores.
- Calibrate probabilities so sales teams can trust score thresholds.
- Refresh models frequently because buyer behavior and market conditions shift.

## Verification

1. Train a lead-scoring model and compare conversion lift over a rule-based baseline.
2. Build a weekly sales forecast and measure MAPE against actuals.
3. Test a next-best-action recommendation in a field pilot.

## References

- https://doi.org/10.3390/forecast6030028
- https://learn.microsoft.com/en-us/dynamics365/sales/work-predictive-lead-scoring
- https://docs.oracle.com/en/cloud/saas/sales/fasqa/how-does-the-ai-lead-score-get-calculated.html
- https://www.malque.pub/ojs/index.php/mr/article/view/10728
