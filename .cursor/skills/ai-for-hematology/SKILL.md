# AI for Hematology

## Description

Use machine learning to classify blood cells, predict leukemia and lymphoma outcomes, and optimize transfusion and transplant care.

## When to use

You are analyzing peripheral blood smears, bone marrow samples, coagulation data, or transplant registries to improve hematologic diagnosis, risk stratification, and treatment planning.

## Usage

- Automate blood smear differential and classify anemia from CBC and iron studies.
- Integrate morphology, immunophenotyping, cytogenetics, and molecular data (MICM).
- Predict thrombosis, bleeding, and transfusion need from labs and EHR.
- Model risk in AML/MDS, lymphoma subtyping, and measurable residual disease.
- Predict engraftment, GVHD, and relapse in stem-cell transplants.

## Steps

1. Assemble CBC, smear images, flow cytometry, genetic, and EHR data.
2. Define prediction or classification targets (anemia type, blast detection, VTE, relapse).
3. Train models with class imbalance handling and stain normalization.
4. Validate against manual differential counts, flow cytometry, or expert review.
5. Integrate results into hematology lab and transplant workflows.
6. Monitor rare-class recall and multicenter drift.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Classify anemia type from CBC and iron/B12/folate labs
X = df[["hemoglobin", "mcv", "ferritin", "b12", "folate", "rdw"]]
y = df["anemia_type"]

model = GradientBoostingClassifier(random_state=42)
model.fit(X, y)
print("Feature importances:", model.feature_importances_)
```

## Tuning notes

- Hematologic conditions are often rare; use stratified sampling and class-weighted loss.
- Stain and scanner differences in smear images require domain adaptation or stain normalization.
- Distinguish transfusion effect from disease-related changes in sequential CBCs.
- Validate against manual differential counts and flow cytometry.

## Verification

1. Classify anemia type from CBC and iron studies and compare to hematologist review.
2. Predict VTE risk in hospitalized patients and report precision-recall at high-risk thresholds.
3. Segment and classify blast cells in peripheral smear images with pathologist-annotated ground truth.

## References

- https://doi.org/10.1182/blood.2025029876
- https://link.springer.com/article/10.1007/s00277-025-06706-2
- https://doi.org/10.1016/j.cll.2025.07.011
- https://doi.org/10.4103/kkujhs.kkujhs_42_25
