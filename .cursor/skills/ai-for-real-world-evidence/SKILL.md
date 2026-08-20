# AI for Real-World Evidence

## Description

Machine learning for extracting, validating, and synthesizing real-world evidence from EHRs, claims, registries, and wearables for regulatory and clinical decisions.

## When to use

You need to generate or evaluate clinical evidence from routinely collected data to support regulatory, reimbursement, or treatment decisions.

## Usage

- **RWE generation**: design and analyze non-interventional studies from RWD.
- **Data fit-for-purpose assessment**: evaluate reliability and relevance of RWD sources.
- **Target trial emulation**: mimic an RCT design using observational data.
- **Decision support**: translate RWE into individualized treatment recommendations.

## Steps

1. Define the research question and regulatory or decision context.
2. Map RWD sources (EHR, claims, registries, wearables) to study variables.
3. Apply causal inference and ML methods with appropriate validation.
4. Assess data quality, representativeness, and bias.
5. Document fit-for-purpose and produce reproducible evidence packages.

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
- https://uscode.house.gov/view.xhtml?req=%28title%3A21+section%3A355g+edition%3Aprelim%29
- https://bmcmedinformdecismak.biomedcentral.com/counter/pdf/10.1186/s12911-021-01403-2.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9189725/
- https://www.nature.com/articles/s43588-025-00901-x
