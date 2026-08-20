# AI for Allergy and Immunology

## Description

Machine learning for asthma phenotyping and exacerbation prediction, allergic rhinitis and food/drug allergy risk, anaphylaxis, and primary immunodeficiency screening.

## When to use

You are modeling asthma, allergic rhinitis, atopic dermatitis, food or drug allergy, anaphylaxis risk, or primary immunodeficiency from clinical, wearable, laboratory, or genomic data.

## Key concepts

- **Asthma phenotyping**: clustering by inflammation, spirometry, FeNO, and exacerbation patterns.
- **Exacerbation prediction**: environmental, medication, and physiological triggers.
- **Allergy diagnostics**: skin-prick tests, specific IgE, component-resolved diagnostics, and oral food challenges.
- **Drug and food allergy risk**: medication exposure, reaction history, and biologics.
- **Immunodeficiency screening**: infection frequency, immune cell counts, and genomic variants.

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
