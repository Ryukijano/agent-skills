# Ensembl Database

Source: `science_skills/ensembl_database/`

## Overview
**CRITICAL:** When writing custom scripts or using alternatives to the provided
scripts, you **MUST** respect the Ensembl REST API rate limits (maximum 15
requests per second) and handle `429 Too Many Requests` errors gracefully (e.g.,
with exponential backoff).

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/ensembl_database/scripts/`:
- `ensembl_api.py`

## References
- `science_skills/ensembl_database/references/ensembl_rest_api_reference.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
