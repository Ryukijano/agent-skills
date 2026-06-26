---
name: gtex-database
description: >-
  Use when you want to retrieve quantitative RNA expression data and variant
  eQTL information from the GTEx (Genotype-Tissue Expression) Project across 54
  non-diseased tissue sites.
---

# Gtex Database

Source: `science_skills/gtex_database/`

## Overview
# Step 2: Query for top tissues using the resolved ID
uv run scripts/gtex_cli.py get-top-expressed-tissues <gencode_id> --n 5 \
  --output /tmp/gata4_top.json
```

## Scripts
Located in `science_skills/gtex_database/scripts/`:
- `gtex_cli.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
