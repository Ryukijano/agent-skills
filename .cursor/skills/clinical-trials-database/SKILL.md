---
name: clinical-trials-database
description: >-
  Query ClinicalTrials.gov via APIv2. Use when you want to search for trials by
  condition, drug, location, status, or phase; retrieve trial details by NCT ID;
  check eligibility/inclusion criteria; count trials across conditions or time
  periods; identify a sponsor's trial portfolio; find recruiting trials for
  patient matching.
---

# Clinical Trials Database

Source: `science_skills/clinical_trials_database/`

## Overview
-   **API parameters, enum values, and Essie syntax:**
    `references/clinical_trials_api.md`
-   **JSON field paths and `--fields` recipes:** `references/studies_schema.md`

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/clinical_trials_database/scripts/`:
- `clinical_trials_api.py`

## References
- `science_skills/clinical_trials_database/references/clinical_trials_api.md`
- `science_skills/clinical_trials_database/references/studies_schema.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
