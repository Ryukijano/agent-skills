# AI for Patient-Reported Outcomes

## Description

Use AI to administer, score, and interpret patient-reported outcome measures.

## When to use

You are collecting, analyzing, or predicting patient-reported outcomes, quality of life, symptom trajectories, or treatment satisfaction data.

## Usage

- Deploy computer adaptive testing with PROMIS-CAT and REDCap.
- Generate and validate LLM-PROMs from patient language.
- Detect response patterns and missing-not-at-random signals.
- Correlate PROs with wearables and clinical events.
- Adapt item banks to minimize patient burden.

## Steps

1. Select the PRO concept and validated instrument.
2. Integrate CAT or LLM-generated items into data capture.
3. Clean responses and detect careless or inconsistent patterns.
4. Train models linking PROs to outcomes or adverse events.
5. Validate psychometric properties and iterate.

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
