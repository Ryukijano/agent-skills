---
name: pdb-database
description: >-
  Use when you want to search for or download experimentally-determined 3D
  structures for biomolecules (proteins, nucleic acids, bound ligands). Supports
  searching by sequence similarity, structure similarity, chemical and other
  attributes. Also use to get metadata about biomolecular structure experiments.
---

# Pdb Database

Source: `science_skills/pdb_database/`

## Overview
```bash
# Fetch polymer entity external sequence database accessions
uv run scripts/fetch_pdb_metadata.py --query '{ entries(entry_ids:["7NHM", "5L2G"]){ polymer_entities { rcsb_id rcsb_polymer_entity_container_identifiers { reference_sequence_identifiers { database_accession database_name } } } } }' --output results.json
```

## Core Rules
-   **Always prefer to use the provided scripts**. Only as a last resort use

## Scripts
Located in `science_skills/pdb_database/scripts/`:
- `download_coordinate_files.py`
- `fetch_pdb_metadata.py`
- `fetch_schema.py`
- `search_pdb.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
