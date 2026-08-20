# AI for Registry Studies

## Description

Machine learning for patient registries, disease surveillance, regulatory-grade real-world evidence, and longitudinal outcome tracking.

## When to use

You are using a disease, product, or population registry to generate real-world evidence, monitor outcomes, or support regulatory and health-technology decisions.

## Usage

- **Registry-based outcome prediction**: forecast events and treatment responses.
- **Quality and completeness assessment**: identify missing data and reporting gaps.
- **Comparative effectiveness**: emulate target trials within registry populations.
- **Surveillance and safety monitoring**: detect signals of adverse events or product issues.

## Steps

1. Understand registry design, inclusion criteria, and variable definitions.
2. Clean and link registry records, handling duplicates and missingness.
3. Define the target population and time-at-risk for the analysis.
4. Train and validate models appropriate to the registry structure and outcomes.
5. Produce transparent reports with clear limitations about generalizability.

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

## References

- https://link.springer.com/article/10.1007/s44250-026-00373-4
- https://doi.org/10.2196/71873
- https://www.real4reg.eu/
- https://cordis.europa.eu/project/id/101095479
