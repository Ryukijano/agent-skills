---
name: literature-search-biorxiv
description: >-
  Browse, filter, and download life sciences, biology, and medical preprints
  from bioRxiv and medRxiv. Supports fetching paper metadata by DOI, and
  browsing by date range with category and keyword filters. Keyword filtering is
  local, so date ranges MUST be narrow (1-4 weeks) with a category to prevent
  timeouts.
---

# Literature Search Biorxiv

Source: `science_skills/literature_search_biorxiv/`

## Overview
`addiction_medicine`, `allergy_and_immunology`, `anesthesia`,
`cardiovascular_medicine`, `dentistry_and_oral_medicine`, `dermatology`,
`emergency_medicine`, `endocrinology`, `epidemiology`, `forensic_medicine`,
`gastroenterology`, `genetic_and_genomic_medicine`, `health_informatics`,
`health_economics_and_outcomes_research`, `health_policy`,
`health_systems_and_quality_improvement`, `hematology`, `hiv_aids`,
`infectious_diseases`, `intensive_care_and_critical_care_medicine`,
`medical_education`, `medical_ethics`, `nephrology`, `neurology`, `nursing`,
`nutrition`, `obstetrics_and_gynecology`,
`occupational_and_environmental_health`, `oncology`, `ophthalmology`,
`orthopedics`, `otolaryngology`, `pain_medicine`, `palliative_care`,
`pathology`, `pediatrics`, `pharmacology_and_therapeutics`,
`primary_care_research`, `psychiatry_and_clinical_psychology`,
`public_and_global_health`, `radiology_and_imaging`,
`rehabilitation_medicine_and_physical_therapy`, `respiratory_medicine`,
`rheumatology`, `sexual_and_reproductive_health`, `sports_medicine`, `surgery`,
`toxicology`, `transplantation`, `urology`

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/literature_search_biorxiv/scripts/`:
- `search_by_dates.py`
- `search_by_doi.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
