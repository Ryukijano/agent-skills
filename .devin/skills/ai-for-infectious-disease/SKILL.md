# AI for Infectious Disease

## Description

Use machine learning to identify pathogens, predict antimicrobial resistance, detect sepsis, and monitor disease outbreaks.

## When to use

You need to detect sepsis early, predict antimicrobial resistance, identify pathogens from clinical or genomic data, or forecast infectious disease spread and outbreak dynamics.

## Usage

- Build EHR-based early-warning models for sepsis and time-to-antibiotics.
- Predict antimicrobial resistance from genomic markers, culture data, and phenotypes.
- Identify pathogens from MALDI-TOF, 16S/NGS, and metagenomic data.
- Optimize antibiotic stewardship with dosing, de-escalation, and drug-target predictions.
- Forecast outbreak spread with time-series and mobility models.

## Steps

1. Collect EHR, genomic, microbiology, and surveillance data for the target infection.
2. Define labels carefully to avoid leakage from cultures drawn after suspicion.
3. Train classifiers or genomic AMR models with appropriate feature representations.
4. Validate alert lead time, false-positive burden, and calibration.
5. Integrate predictions into stewardship, triage, or public-health dashboards.
6. Monitor for pathogen and resistance drift and update the model.

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
