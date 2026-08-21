# AI for Human Resources

## Description

Use AI for Human Resources to match candidates, predict attrition, plan workforce and audit pay and promotion equity.

## When to use

You are optimizing hiring, predicting turnover, matching candidates to roles, or analyzing workforce composition and pay equity.


## Usage


- **Talent analytics**: Data-driven insights for recruitment, retention, and development.
- **Attrition prediction**: Classification models to identify flight-risk employees.
- **Resume-job matching**: Semantic similarity using embeddings and dense retrieval.
- **Pay and promotion equity**: Statistical tests and models to detect disparities across groups.

## Steps

1. Collect and prepare HRIS, ATS, performance and compensation data.
2. Optimize hiring.
3. Predict turnover.
4. Match candidates to roles.
5. Validate by training an attrition model and evaluate recall for at-risk employees.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

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
