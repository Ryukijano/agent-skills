---
name: openfda-database
description: >-
  Query, search, and download data from the openFDA API for drugs, devices,
  foods, tobacco, cosmetics, animal and veterinary products, substances, and
  transparency data. Use for FDA adverse events, recalls, labeling, approvals,
  shortages, 510(k) clearances, NDC lookups, and any FDA safety or regulatory
  data query across all 28 API endpoints.
---

# Openfda Database

Source: `science_skills/openfda_database/`

## Overview
1.  Search for records using `search` with `--output`. Read the output file.
2.  Use `count` with `--summary 10 --output` to summarize field distributions.
3.  Use `download` (with `--all_results` for exhaustive pulls) to fetch larger
    datasets.
4.  Read and analyze the output file using standard tools.
5.  For MedDRA term hierarchy questions, use a biomedical ontology service skill
    (e.g. EMBL-EBI OLS skill with the HP or NCIT ontology) to look up the term.

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/openfda_database/scripts/`:
- `openfda_query.py`

## References
- `science_skills/openfda_database/references/api_endpoints.md`
- `science_skills/openfda_database/references/recipes.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
