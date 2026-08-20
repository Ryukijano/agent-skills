# AI for Health Informatics

## Description

Electronic health records, clinical data standards, interoperability, and AI-enabled analytics for healthcare delivery and research.

## When to use

You need to structure, integrate, and analyze healthcare data across systems using standards such as HL7 FHIR, OMOP, and LOINC.

## Key concepts

- **Health data standards and interoperability**: HL7 FHIR, OMOP CDM, DICOM, and terminologies such as SNOMED-CT, ICD, RxNorm, and LOINC.
- **EHR phenotyping and clinical data warehouses**: extracting computable cohorts and longitudinal patient features.
- **Natural language processing for clinical text**: named-entity recognition, entity normalization, de-identification, and information extraction.
- **Clinical decision support and alert systems**: rules-based and ML-driven recommendations embedded in workflows.
- **Privacy, security, and governance**: HIPAA, GDPR, de-identification, and role-based access control.

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
