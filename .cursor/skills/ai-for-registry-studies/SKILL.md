# AI for Registry Studies

## Description

Analyze disease and product registries to monitor safety, effectiveness, and utilization.

## When to use

You are using a disease, product, or population registry to generate real-world evidence, monitor outcomes, or support regulatory and health-technology decisions.

## Usage

- Identify fit-for-purpose registries with AI-powered RWD catalogues.
- Define phenotypes using CQL, SNOMED, and FHIR (PhEMA).
- Track drug utilization and adverse events across registries.
- Benchmark outcomes against external controls.
- Generate real-world evidence for regulatory and HTA submissions.

## Steps

1. Identify relevant registries and assess data quality.
2. Define the study population and phenotype algorithms.
3. Extract exposure, outcome, and covariate records.
4. Apply epidemiological and ML methods for safety/effectiveness.
5. Prepare regulatory-grade reports and evidence packages.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Registry records with patient, event, and exposure flags
X = registry_df[["age", "sex", "disease_stage", "prior_treatment"]]
y = registry_df["outcome_event"]

clf = GradientBoostingClassifier(random_state=42).fit(X, y)
registry_df["risk_score"] = clf.predict_proba(X)[:, 1]
```

## Tuning notes

- Account for site and country effects if the registry spans multiple centers.
- Be explicit about data-quality flags and missingness mechanisms.
- Use time-dependent splits to avoid leakage from later enrollment periods.
- Align analyses with regulatory guidance and HTA evidentiary standards.

## Verification

1. Build a predictive model on a disease registry and validate on a temporally held-out sample.
2. Compare registry-derived estimates to published RCT estimates for the same treatment.
3. Report data-quality and completeness metrics alongside model performance.

## References

- https://link.springer.com/article/10.1007/s44250-026-00373-4
- https://doi.org/10.2196/71873
- https://www.real4reg.eu/
- https://cordis.europa.eu/project/id/101095479
