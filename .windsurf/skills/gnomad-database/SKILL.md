---
name: gnomad-database
description: >-
  Query the Genome Aggregation Database (gnomAD). Use when determining the
  rarity or allele frequency of specific genetic variants, retrieving gene
  constraint metrics (pLI, LOEUF) to assess loss-of-function intolerance,
  finding variants in a genomic region or gene, or querying structural variants.
  Don't use for analyzing individual patient genomes, tracking somatic mutations
  in cancer (use COSMIC), or requesting raw sequencing reads (use ENA).
---

# Gnomad Database

Source: `science_skills/gnomad_database/`

## Overview
Further documentation on the data: https://gnomad.broadinstitute.org/data#api
More general database documentation: https://gnomad.broadinstitute.org/help

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/gnomad_database/scripts/`:
- `get_gene_constraint.py`
- `get_variant_frequency.py`
- `search_variants.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
