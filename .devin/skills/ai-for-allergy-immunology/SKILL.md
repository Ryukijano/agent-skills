# AI for Allergy and Immunology

## Description

Use machine learning to phenotype asthma, predict exacerbations, assess allergy risk, and screen immunodeficiency.

## When to use

You are modeling asthma, allergic rhinitis, atopic dermatitis, food or drug allergy, anaphylaxis risk, or primary immunodeficiency from clinical, wearable, laboratory, or genomic data.

## Usage

- Cluster asthma phenotypes by inflammation, spirometry, FeNO, and exacerbation patterns.
- Predict asthma exacerbations from environmental, medication, and physiological triggers.
- Interpret skin-prick, specific IgE, component-resolved diagnostics, and oral challenge data.
- Predict drug and food allergy risk and anaphylaxis severity.
- Screen primary immunodeficiency from infection history, cell counts, and genomics.

## Steps

1. Collect clinical, wearable, lab, genomic, and environmental data for the target allergy or immune condition.
2. Define outcomes (exacerbation, reaction severity, immunodeficiency flag) and windows.
3. Train models with seasonality, device standardization, and class imbalance in mind.
4. Validate against challenge-based labels and clinical expert review.
5. Integrate predictions into asthma action plans, allergy clinics, or screening tools.
6. Monitor pediatric and adult differences and update as immunological understanding evolves.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Predict asthma exacerbation in next 30 days
X = df[["fev1_fvc", "feNO", "exacerbations_12m", "ics_adherence", "smoking"]]
y = df["exacerbation_next_30d"]

model = GradientBoostingClassifier(random_state=42)
model.fit(X, y)
df["exacerbation_risk"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Seasonality and pollen/viral circulation affect asthma; include calendar features.
- Spirometry and FeNO devices vary; standardize by device and pediatric norms.
- Allergy outcomes are often self-reported; use challenge-based labels when possible.
- Pediatric and adult populations may need separate models.

## Verification

1. Predict 30-day asthma exacerbation and evaluate calibration across seasons.
2. Cluster asthma phenotypes and compare to Type-2 inflammation biomarkers.
3. Predict peanut allergy reaction severity from skin test, IgE, and component panels.

## References

- https://doi.org/10.1016/j.jaci.2025.08.022
- https://doi.org/10.1111/all.15849
- https://www.sciencedirect.com/science/article/abs/pii/S2213219825005094
- https://erj.ersjournals.com/content/56/3/2000521
