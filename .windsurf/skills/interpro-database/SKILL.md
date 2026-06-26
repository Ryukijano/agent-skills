---
name: interpro-database
description: >-
  Identify domains, families, and sites in proteins; find all proteins in a
  family or sharing a domain; explore species distribution for a domain;
  annotate genomes with protein families and GO terms. InterPro combines 14
  databases (e.g., Pfam, CDD) into one searchable resource. InterPro-N
  significantly expands annotation and sequence coverage with deep learning.
  Includes domain architecture (IDA) search.
---

# Interpro Database

Source: `science_skills/interpro_database/`

## Overview
```bash
# URL equivalent: /structure/pdb/entry/interpro/IPR011615
# Only fetch the first 5 structures
uv run ./scripts/interpro_client.py fetch structure
    --source_db pdb
    --linked_endpoint entry
    --linked_source_db interpro
    --linked_accession IPR011615
    --output ipr011615_structures.jsonl
```

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the `scripts/interpro_client.py` helper

## Scripts
Located in `science_skills/interpro_database/scripts/`:
- `interpro_client.py`

## References
- `science_skills/interpro_database/references/api_reference.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
