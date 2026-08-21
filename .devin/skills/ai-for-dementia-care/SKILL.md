# AI for Dementia Care

## Description

Use machine learning to screen for cognitive decline, stratify dementia risk, and support caregivers.

## When to use

You need to detect cognitive decline early, triage memory-clinic referrals, or support people with dementia and their caregivers.

## Usage

- Screen for cognitive impairment from voice, language, and questionnaire responses.
- Build EHR-based dementia risk models with low-burden inputs.
- Combine neuropsychology, imaging, and biomarkers for differential diagnosis.
- Tier models from basic demographics to full neuropsych batteries.

## Steps

1. Collect voice, EHR, imaging, and neuropsych data with careful timestamping.
2. Define the screening or risk target and avoid leakage from future visits.
3. Train minimal-input screeners and more comprehensive diagnostic models.
4. Validate across health systems, countries, and cognitive assessment norms.
5. Balance sensitivity and specificity and provide explanations to clinicians.
6. Integrate into memory clinic triage and monitor referral outcomes.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Dementia risk stratification from structured EHR and cognitive scores
X = df[["age", "mmse", "cdr", "education_years", "functional_status", "comorbidity_count"]]
y = df["dementia"]

clf = RandomForestClassifier(class_weight="balanced", random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Avoid temporal leakage from future visits, tests, or diagnoses.
- External-validate across health systems, countries, and cognitive assessment norms.
- Balance sensitivity and specificity to avoid unnecessary anxiety and missed cases.
- Provide explanations to clinicians and caregivers; avoid opaque risk scores.

## Verification

1. Build a minimal-input dementia screener and compare AUC to a full neuropsych battery.
2. Analyze a voice-recording dataset for cognitive-impairment detection and report AUC.
3. Validate the model on an independent EHR cohort and check subgroup calibration.

## References

- https://link.springer.com/article/10.1186/s13195-026-02006-7
- https://www.nature.com/articles/s41467-026-76071-9
- https://www.nature.com/articles/s44400-025-00040-0
- https://www.nature.com/articles/s41591-024-03118-z
