---
name: encode-ccres-database
description: >-
  Query the ENCODE Registry of cis-Regulatory Elements (cCREs) via the SCREEN
  GraphQL API, or make custom queries to the ENCODE Portal REST API for
  experiments and files (ChIP-seq peaks, etc.). Use when you want to query
  regulatory annotations or raw experimental data across human cell types.
---

# Encode Ccres Database

Source: `science_skills/encode_ccres_database/`

## Overview
If you need to make a complex GraphQL query that the script does not support,
read `references/graphql_schema.md` for a reference of available queries,
arguments, and return fields in the SCREEN GraphQL API.

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/encode_ccres_database/scripts/`:
- `encode_portal_api.py`
- `screen_api.py`

## References
- `science_skills/encode_ccres_database/references/graphql_schema.md`
- `science_skills/encode_ccres_database/references/json_output_structure.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
