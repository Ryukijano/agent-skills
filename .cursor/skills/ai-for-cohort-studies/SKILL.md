# AI for Cohort Studies

## Description

Analyze defined patient groups to estimate risk, survival, and treatment effects over time.

## When to use

You are building risk or prognostic models, identifying risk factors, or estimating exposure-outcome associations in a defined cohort followed over time.

## Usage

- Predict incident disease with AutoPrognosis or MILTON on UK Biobank.
- Run survival analysis with Cox, random survival forests, or deep survival.
- Build propensity-matched cohorts from EHR and claims.
- Identify biomarker trajectories linked to outcomes.
- Stratify cohorts by genotype, exposure, or frailty.

## Steps

1. Define cohort inclusion/exclusion and baseline characteristics.
2. Curate linked data (EHR, claims, omics, registries).
3. Engineer survival or longitudinal features.
4. Train risk or survival models with cross-validation.
5. Report hazard ratios, C-indices, and subgroup effects.

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
