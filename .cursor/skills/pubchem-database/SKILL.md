---
name: pubchem-database
description: >-
  Query PubChem, search by name/CID/SMILES, retrieve properties,
  similarity/substructure searches, bioactivity, for cheminformatics. Use when a
  user asks about a specific chemical, drug, or molecule.
---

# Pubchem Database

Source: `science_skills/pubchem_database/`

## Overview
*   **Custom/Complex Queries**: For more details, read
    [references/endpoints.md](references/endpoints.md) to construct raw PUG-REST
    URLs.
*   **Multi-Step Tasks**: For complex tasks like drug discovery pipelines,
    follow the checklists in [references/workflows.md](references/workflows.md).

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/pubchem_database/scripts/`:
- `pubchem_api.py`

## References
- `science_skills/pubchem_database/references/endpoints.md`
- `science_skills/pubchem_database/references/workflows.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
