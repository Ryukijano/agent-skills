---
name: chembl-database
description: >-
  Query the ChEMBL database for bioactive molecules, drug targets, bioactivity
  data, approved drugs, and chemical structures. Use when the user asks about
  compounds, targets, IC50/Ki values, drug mechanisms, or structure searches.
---

# Chembl Database

Source: `science_skills/chembl_database/`

## Overview
1.  Use `status --output /tmp/status.json` to verify the API is available.
2.  Search for targets, molecules, or drugs using the relevant subcommand.
3.  Read the output JSON file to extract IDs and data.
4.  Use IDs from search results to fetch detailed records.
5.  Query `activity` with filters to get bioactivity data for targets/molecules.
    Use `--normalize` when comparing values across studies.
6.  Use `similarity` or `substructure` for server-side structure-based queries.
7.  Download compound images with `image` or structure files with `molecule
    --dl_format sdf`.
8.  Use `target --filter target_components__accession=<UniProt>` to cross-
    reference with UniProt.

## Core Rules
-   [!IMPORTANT] **Use the Utility Scripts**: You MUST ALWAYS use the provided

## Scripts
Located in `science_skills/chembl_database/scripts/`:
- `chembl_api.py`

## References
- `science_skills/chembl_database/references/api_endpoints.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
