# AI for Health Informatics

## Description

Harmonize EHR data through FHIR to predict 30-day readmissions and mortality across institutions without manual feature engineering.

## When to use

You need to structure, integrate, and analyze healthcare data across systems using standards such as HL7 FHIR, OMOP, and LOINC.

## Usage

- Normalize FHIR, OMOP, SNOMED, ICD, RxNorm, and LOINC data.
- Build EHR phenotyping and longitudinal feature pipelines.
- Extract and de-identify clinical text.
- Deploy clinical decision support alerts.

## Steps

1. Normalize FHIR, OMOP, SNOMED, ICD, RxNorm, and LOINC data.
2. Build EHR phenotyping and longitudinal feature pipelines.
3. Extract and de-identify clinical text.
4. Deploy clinical decision support alerts.
5. Validate with temporal and site-split cross-validation.
6. Validate on local devices, clinical measurements, and diverse populations before embedding into EHR or public-health workflows (ChatEHR-style).

## Code pattern

```python
import pandas as pd

# Flatten FHIR Observation resources from a Bundle
observations = [
    r['resource'] for r in bundle['entry']
    if r['resource']['resourceType'] == 'Observation'
]
df = pd.json_normalize(observations)
```

## Tuning notes

- Normalize terminologies before modeling and reconcile conflicting code systems.
- Handle missing, longitudinal, and irregularly sampled EHR data.
- Avoid label leakage from future encounters; use time-split validation.
- Audit for bias across sites, documentation practices, and patient populations.

## Verification

1. Extract a computable phenotype from EHR data and compare it to manual chart review.
2. Map free-text diagnoses to ICD/SNOMED-CT codes with an NLP pipeline.
3. Evaluate a predictive model with temporal cross-validation across hospitals.

## References

- https://doi.org/10.1093/jamia/ocae074
- https://doi.org/10.1093/jamia/ocac095
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11700560/
- https://doi.org/10.1093/jamia/ocaf131
