---
name: quickgo-database
description: >-
  Query the QuickGO and Evidence & Conclusion Ontology (ECO) REST API. Use this
  when you need to map genes to biological processes, molecular functions, or
  cellular components, find genes associated with a specific pathway/GO term, or
  explore the Gene Ontology hierarchy. Do not use for querying drug targets (use
  OpenTargets) or mechanistic signaling pathway diagrams (use KEGG).
---

# Quickgo Database

Source: `science_skills/quickgo_database/`

## Overview
# Step 2: Create a slim summary from those specific GO IDs
uv run scripts/quickgo_tool.py go slim --slimsToIds "GO:0005575,GO:0008150,GO:0003674" --slimsFromIds "GO:0006915,GO:0008219" --output my_slim.json
```

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/quickgo_database/scripts/`:
- `quickgo_tool.py`

## References
- `science_skills/quickgo_database/references/annotations.md`
- `science_skills/quickgo_database/references/eco_terms.md`
- `science_skills/quickgo_database/references/gene_products.md`
- `science_skills/quickgo_database/references/go_terms.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
