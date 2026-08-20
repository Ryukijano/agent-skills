# AI for Global Health

## Description

AI for disease burden, healthcare systems, and health equity in low- and middle-income countries and resource-limited settings.

## When to use

You are designing or evaluating AI for health challenges in global or resource-limited settings, with a focus on equity, access, and implementation.

## Key concepts

- **Global health equity and context-specific validation**: performance, acceptability, and fairness in diverse settings.
- **Low-resource deployment, mobile health, and task shifting**: point-of-care and community health tools.
- **Open data, data sovereignty, and local capacity building**: community-owned data and workforce development.
- **AI for tropical and neglected diseases, maternal/child health, and outbreak response**: priority conditions in LMICs.
- **Implementation and cost-effectiveness in LMICs**: real-world evidence and scalability.

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
- https://doi.org/10.1016/S2214-109X(25)00473-5
