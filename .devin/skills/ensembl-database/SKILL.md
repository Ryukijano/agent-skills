---
name: ensembl-database
description: >-
  Query the Ensembl database to resolve gene, transcript, and protein IDs, fetch
  genomic or protein sequences, retrieve gene structures (exons), and get
  variant consequence and effect predictions (VEP). Use this skill as a primary
  ID translator, genomic sequence database and variant effect prediction tool.
---

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
