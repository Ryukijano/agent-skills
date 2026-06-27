---
name: dbsnp-database
description: >-
  Use when you want to look up, map, and search for short genetic variants
  (SNPs, indels) in NCBI's dbSNP database. Resolves between rsIDs, genomic
  coordinates in VCF format, and HGVS strings. For an rsID, returns variant
  type, gene associations, clinical significance, allele frequencies, and
  genomic coordinates (GRCh38).
---

# Dbsnp Database

Source: `science_skills/dbsnp_database/`

## Overview
-   **Mistake:** Passing `X` or `Y` as the chromosome value **Fix:** Use the
    numeric equivalents: `23` for chromosome X and `24` for chromosome Y. The
    CLI treats chromosomes numerically by default.

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided wrapper script

## Scripts
Located in `science_skills/dbsnp_database/scripts/`:
- `dbsnp_cli.py`

## References
- `science_skills/dbsnp_database/references/api-notes.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
