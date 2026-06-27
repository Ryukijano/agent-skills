---
name: human-protein-atlas-database
description: >-
  Use when you want to retrieve semi-quantitative protein expression and spatial
  localisation data from the Human Protein Atlas (HPA).
---

# Human Protein Atlas Database

Source: `science_skills/human_protein_atlas_database/`

## Overview
-   If no results are returned, confirm the query is detailed enough starting
    with the api reference in references/search-api.md
-   If you cannot find the results, search the web for example HPA queries and
    use these to construct a better query.
-   The output is usually large. Use jq or write your own python data parsing
    library to process the search results. Never output to stdout, or cat the
    output file.

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/human_protein_atlas_database/scripts/`:
- `hpa_cli.py`

## References
- `science_skills/human_protein_atlas_database/references/search-api.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
