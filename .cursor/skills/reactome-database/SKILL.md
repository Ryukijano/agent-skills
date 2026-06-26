---
name: reactome-database
description: >-
  Query the Reactome database (Analysis and Content Services). Use when the user
  asks about pathway analysis, gene list enrichment, retrieving results by
  token, finding unmapped or not-found identifiers, mapping identifiers,
  reaction participants (inputs, outputs), pathway hierarchy (including top-
  level pathways), diagram export, cross-reference mapping, or searching the
  knowledgebase.
---

# Reactome Database

Source: `science_skills/reactome_database/`

## Overview
For detailed API endpoint documentation, see
[references/api_reference.md](references/api_reference.md).

## Scripts
Located in `science_skills/reactome_database/scripts/`:
- `reactome_analysis.py`

## References
- `science_skills/reactome_database/references/api_reference.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
