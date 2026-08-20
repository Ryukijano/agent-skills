# AI for Human Resources

## Description

Talent analytics, recruitment matching, attrition prediction, workforce planning, and compensation and equity analysis.

## When to use

You are optimizing hiring, predicting turnover, matching candidates to roles, or analyzing workforce composition and pay equity.

## Key concepts

- **Talent analytics**: data-driven insights for recruitment, retention, and development.
- **Attrition prediction**: classification models to identify flight-risk employees.
- **Resume-job matching**: semantic similarity using embeddings and dense retrieval.
- **Pay and promotion equity**: statistical tests and models to detect disparities across groups.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = df[["age", "job_satisfaction", "overtime", "tenure", "salary_level"]]
y = df["attrition"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
model = RandomForestClassifier(random_state=42).fit(X_train, y_train)
```

## Tuning notes

- HR models are high-stakes; ensure fairness, explainability, and legal compliance.
- Attrition labels are often imbalanced; use resampling or cost-sensitive learning.
- Audit hiring models for adverse impact on protected groups.

## Verification

1. Train an attrition model and evaluate recall for at-risk employees.
2. Build a resume-to-job matching pipeline and measure top-k accuracy.
3. Run an equity analysis on compensation or promotion outcomes.

## References

- https://arxiv.org/abs/2307.03195
- https://link.springer.com/article/10.1186/s43093-025-00704-6
- https://doi.org/10.1016/j.fraope.2026.100673
- https://oracle.com/human-capital-management/analytics/
