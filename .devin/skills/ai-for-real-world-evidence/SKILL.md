# AI for Real-World Evidence

## Description

Generate regulatory and HTA evidence from EHR, claims, and registry data.

## When to use

You need to generate or evaluate clinical evidence from routinely collected data to support regulatory, reimbursement, or treatment decisions.

## Usage

- Link RWD sources across EHR, claims, and disease registries.
- Apply fit-for-purpose assessments per FDA/EMA guidance.
- Run target trial emulation and causal inference.
- Build external control arms for single-arm studies.
- Create interactive evidence dashboards for HTA bodies.

## Steps

1. Define the research question and regulatory use case.
2. Assess RWD source fitness and data quality.
3. Curate exposure, outcome, and confounder variables.
4. Apply causal or predictive methods and sensitivity checks.
5. Document evidence in a regulatory/HTA submission package.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit

# RWE treatment-decision model with time-aware validation
X = rwd_df[["age", "comorbidity_count", "prior_hospitalizations"]]
y = rwd_df["treatment_response"]

tscv = TimeSeriesSplit(n_splits=3)
for train_idx, test_idx in tscv.split(X):
    model = RandomForestClassifier(random_state=42).fit(X.iloc[train_idx], y.iloc[train_idx])
    preds = model.predict(X.iloc[test_idx])
```

## Tuning notes

- Avoid immortal-time and prevalent-user biases in treatment comparisons.
- Validate on external data or against RCT estimates when possible.
- Use transparent, auditable pipelines for regulatory submissions.
- Track data provenance and versioning for all RWE analyses.

## Verification

1. Emulate a target trial in claims or EHR data and compare estimates to an RCT.
2. Evaluate model performance on a different RWD source or calendar period.
3. Produce a fit-for-purpose assessment using FDA or EMA guidance criteria.

## References

- https://www.fda.gov/drugs/development-resources/advancing-real-world-evidence-program-frequently-asked-questions
- https://www.law.cornell.edu/uscode/text/21/355g
- https://bmcmedinformdecismak.biomedcentral.com/counter/pdf/10.1186/s12911-021-01403-2.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9189725/
- https://www.nature.com/articles/s43588-025-00901-x
