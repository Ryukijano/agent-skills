# AI for Patient-Reported Outcomes

## Description

Machine learning for predicting, personalizing, and reducing the burden of patient-reported outcome measures and PRO-based treatment decisions.

## When to use

You are collecting, analyzing, or predicting patient-reported outcomes, quality of life, symptom trajectories, or treatment satisfaction data.

## Usage

- **PRO prediction**: forecast post-treatment PRO scores from baseline and clinical data.
- **Computer adaptive testing**: select the most informative PRO items per patient.
- **Personalized interventions**: target patients whose PROs indicate high risk or unmet need.
- **Burden reduction**: minimize questionnaire length while preserving measurement precision.

## Steps

1. Map the PRO instrument, response scale, and recall period to the analysis goal.
2. Engineer baseline and longitudinal features (scores, trends, change from baseline).
3. Train models for prediction, classification, or item response theory.
4. Validate predictive accuracy and measurement properties in a held-out sample.
5. Assess clinical utility and patient acceptability before deployment.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

X = pro_df[["baseline_pain", "function_score", "age", "comorbidities"]]
y = pro_df["follow_up_quality_of_life"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
pro_df["predicted_pro"] = model.predict(X)
```

## Tuning notes

- Respect floor and ceiling effects in PRO scales.
- Handle item-level missingness with appropriate imputation or latent models.
- Calibrate predictions for decision thresholds used in clinical workflows.
- Engage patients and clinicians in validating model outputs.

## Verification

1. Predict a PRO score at a future visit and compare to observed values on a test set.
2. Implement a short adaptive PRO form and compare measurement precision to the full form.
3. Evaluate whether PRO-based predictions improve shared decision-making outcomes.

## References

- https://link.springer.com/article/10.1186/s12955-025-02365-z
- https://link.springer.com/article/10.1186/s12911-025-03083-8
- https://link.springer.com/article/10.1186/s41687-026-00992-8
- https://link.springer.com/article/10.1186/s41687-024-00808-7
