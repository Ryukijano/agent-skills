# AI for Global Health

## Description

Use AI to design or evaluate AI for health challenges in global or resource-limited settings, with a focus on equity, access, and implementation.

## When to use

You are designing or evaluating AI for health challenges in global or resource-limited settings, with a focus on equity, access, and implementation.

## Usage

- Co-design tools with local clinicians and communities.
- Train portable triage and diagnostic models.
- Validate on local devices and infrastructure.
- Evaluate cost-effectiveness and scalability.

## Steps

1. Co-design tools with local clinicians and communities.
2. Train portable triage and diagnostic models.
3. Validate on local devices and infrastructure.
4. Evaluate cost-effectiveness and scalability.
5. Ensure data sovereignty and equitable access.
6. Validate on local devices, clinical measurements, and diverse populations before embedding into EHR or public-health workflows (ChatEHR-style).

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Portable triage model for a low-resource clinic
features = ['fever', 'cough', 'respiratory_rate', 'oxygen_saturation', 'age']
X = df[features]
y = df['referral_needed']
model = RandomForestClassifier(class_weight='balanced').fit(X, y)
```

## Tuning notes

- Co-design with local clinicians and communities; respect data sovereignty.
- Validate on local devices, connectivity, and infrastructure constraints.
- Consider fairness across geography, language, and health-system tier.
- Evaluate cost-effectiveness and scalability relative to standard care.

## Verification

1. Validate a diagnostic or triage model on data from the target country or region.
2. Assess model performance across facility types and demographic groups.
3. Estimate cost-effectiveness and implementation feasibility in a local health system.

## References

- https://annalsofglobalhealth.org/articles/10.5334/aogh.5268
- https://doi.org/10.1016/s0140-6736(20)30226-9
- https://doi.org/10.1038/s41746-022-00700-y
- https://www.research.ed.ac.uk/en/publications/research-priorities-for-data-science-and-artificial-intelligence-/
