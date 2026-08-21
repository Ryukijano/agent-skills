# AI for Palliative Care

## Description

Use machine learning for prognostication, symptom management, hospice suitability, and advance care planning in end-of-life care.

## When to use

You need to identify patients who may benefit from palliative or hospice care, forecast prognosis, or personalize symptom management.

## Usage

- Estimate 6- or 12-month mortality from EHR for referral triggers.
- Classify optimal care models (home, inpatient, shared) from health assessments.
- Extract pain, dyspnea, fatigue, and psychosocial distress from clinical notes.
- Alert clinicians to goals-of-care conversations and documentation needs.

## Steps

1. Define the palliative outcome (mortality, symptom, care setting) and assemble EHR.
2. Use time-stamped EHR splits and avoid labels that depend on the referral decision itself.
3. Train prognostic or NLP symptom models and calibrate probabilities.
4. Validate against palliative screening rules and chart review.
5. Integrate as decision support, keeping clinicians and patients at the center.
6. Monitor for bias in access to hospice and palliative services across groups.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Palliative-care referral trigger from structured EHR
X = df[["age", "comorbidity_count", "performance_status", "hospitalizations_90d", "symptom_burden"]]
y = df["palliative_referral_needed"]

clf = GradientBoostingClassifier(random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Keep clinicians and patients at the center; models should support, not replace, compassionate judgment.
- Use time-stamped EHR splits and avoid labels that depend on the referral decision itself.
- Calibrate predicted probabilities so clinicians can trust risk thresholds.
- Monitor for bias in access to hospice and palliative services across groups.

## Verification

1. Train a 6-month mortality model and compare to a palliative-screening rule.
2. Build an NLP symptom extractor and evaluate against manual chart review.
3. Pilot a referral decision-support tool and measure time-to-palliative consult.

## References

- https://pubmed.ncbi.nlm.nih.gov/40849027/
- https://link.springer.com/article/10.1186/s12911-025-03289-w
- https://www.nature.com/articles/s41746-026-02429-4
- https://sage.cnpereading.com/doi/10.1177/10499091251358379
- https://pubmed.ncbi.nlm.nih.gov/36842541/
