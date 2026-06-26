---
name: uniprot-database
description: >-
  Access protein metadata, function, taxonomy, and sequences across UniProtKB,
  UniParc, and UniRef. Use when searching for proteins, mapping identifiers, or
  retrieving functional annotations and publications. Don't use for sequence
  alignment, protein folding, or sequence similarity search (use specialized
  skills for those tasks).
---

# Uniprot Database

Source: `science_skills/uniprot_database/`

## Overview
-   [SPARQL Examples](references/sparql_examples.md)
-   [Search Query Fields Documentation](references/search_query_fields.md)
-   [ID Mapping Documentation](references/id_mapping_documentation.md)
-   [UniProt Evidence Docs](https://www.uniprot.org/help/evidences)
-   **Underlying API Endpoints** (Used by `scripts/uniprot_tools.py`):
    -   `get`, `search`, `stream`, `count` -> `rest.uniprot.org/{dataset}/`
    -   `map` -> `rest.uniprot.org/idmapping/`
    -   `sparql` -> `sparql.uniprot.org/sparql`
    -   `get --dataset unisave` -> `rest.uniprot.org/unisave/`

## Core Rules
-   **Use the Wrapper**: Always use the provided Python scripts (e.g.,

## Scripts
Located in `science_skills/uniprot_database/scripts/`:
- `uniprot_tools.py`

## References
- `science_skills/uniprot_database/references/id_mapping_databases.md`
- `science_skills/uniprot_database/references/search_query_fields.md`
- `science_skills/uniprot_database/references/sparql_examples.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
