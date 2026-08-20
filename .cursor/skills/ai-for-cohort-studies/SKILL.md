# AI for Cohort Studies

## Description

Machine learning for risk prediction, confounding control, survival analysis, and biomarker discovery in prospective and retrospective cohort studies.

## When to use

You are building risk or prognostic models, identifying risk factors, or estimating exposure-outcome associations in a defined cohort followed over time.

## Usage

- **Cohort risk prediction**: forecast disease onset, progression, or mortality.
- **Feature discovery**: find non-linear risk factors and interactions in large biobanks.
- **Survival modeling**: handle censored outcomes and time-to-event data.
- **Confounder adjustment**: control for selection bias and measured confounders.

## Steps

1. Define the cohort, eligibility window, and follow-up period.
2. Create a tabular feature set at baseline or as time-varying covariates.
3. Split by calendar time or admission date to mimic prospective use.
4. Train risk models with appropriate survival or classification objectives.
5. Validate calibration, discrimination, and generalizability to new cohorts.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = cohort_df[["age", "sex", "smoking", "systolic_bp", "biomarker"]]
y = cohort_df["event_within_5yr"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=42
)
model = RandomForestClassifier(class_weight="balanced", random_state=42).fit(X_train, y_train)
```

## Tuning notes

- Balance class weights or use resampling for rare outcomes.
- Avoid leakage by excluding post-baseline variables that are not available at prediction time.
- Report confidence intervals for performance metrics using bootstrapping.
- External validation on a temporally or geographically separate cohort is essential.

## Verification

1. Replicate a published cohort risk model and compare discrimination and calibration.
2. Test the model on a held-out time period or external cohort.
3. Audit key features for clinical plausibility and fairness across subgroups.

## References

- https://link.springer.com/article/10.1007/s10654-024-01173-x
- https://pubmed.ncbi.nlm.nih.gov/40701371/
- https://link.springer.com/article/10.1186/s12874-023-01837-4
- https://www.nature.com/articles/s41598-021-02476-9

## References

- https://link.springer.com/article/10.1007/s10654-024-01173-x
- https://pubmed.ncbi.nlm.nih.gov/40701371/
- https://link.springer.com/article/10.1186/s12874-023-01837-4
- https://www.nature.com/articles/s41598-021-02476-9
