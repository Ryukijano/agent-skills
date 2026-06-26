---
name: literature-search-europepmc
description: >-
  Search Europe PMC for scientific literature and download open-access full
  texts and PDFs. Retrieve full-text XML/plain text by PMCID, get citation lists
  and bibliography.
---

# Literature Search Europepmc

Source: `science_skills/literature_search_europepmc/`

## Overview
```bash
# First page
uv run scripts/europepmc_api.py search "CRISPR" --max_results 100 --output page1.json
# Extract cursor for next page
CURSOR=$(jq -r '.nextCursorMark // empty' page1.json)
# Next page
uv run scripts/europepmc_api.py search "CRISPR" --max_results 100 --cursor "$CURSOR" --output page2.json
```

## Core Rules
-   **Open Access Only**: This skill exclusively searches open-access content.

## Scripts
Located in `science_skills/literature_search_europepmc/scripts/`:
- `europepmc_api.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
