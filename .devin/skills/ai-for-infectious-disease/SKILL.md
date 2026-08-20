# AI for Infectious Disease

## Description

Machine learning for pathogen identification, antimicrobial resistance prediction, sepsis early warning, and infectious disease outbreak surveillance.

## When to use

You need to detect sepsis early, predict antimicrobial resistance, identify pathogens from clinical or genomic data, or forecast infectious disease spread and outbreak dynamics.

## Key concepts

- **Sepsis early warning**: EHR-based models using vitals, labs, and demographics for timely antibiotics.
- **AMR prediction**: genomic markers, culture data, and phenotypic resistance forecasting.
- **Pathogen identification**: MALDI-TOF, 16S/NGS, and metagenomic classification.
- **Antibiotic stewardship**: dosing optimization, de-escalation, and drug-target interaction prediction.
- **Epidemiological surveillance**: time-series and mobility models for outbreak detection.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Sepsis early-warning model from structured EHR
X = df[["heart_rate", "resp_rate", "temp", "wbc", "lactate", "creatinine"]]
y = df["sepsis_next_6h"]

model = GradientBoostingClassifier(random_state=42)
model.fit(X, y)
df["sepsis_risk"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Time-to-antibiotic is critical; validate alert lead time and false-positive burden.
- Avoid label leakage from cultures drawn after suspicion of sepsis.
- Genomic AMR models benefit from k-mer or gene-family feature representations.
- Monitor for concept drift as pathogens and resistance patterns evolve.

## Verification

1. Build a 6-hour sepsis prediction model with time-based cross-validation and report AUROC.
2. Predict phenotypic antibiotic resistance from assembled genome k-mers and compare to AST.
3. Forecast weekly influenza-like illness at the regional level and evaluate against surveillance data.

## References

- https://doi.org/10.1038/s44259-024-00068-x
- https://www.nature.com/articles/s44259-025-00085-4
- https://www.mdpi.com/2075-4418/15/15/1890
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12573687/
