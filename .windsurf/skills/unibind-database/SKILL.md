---
name: unibind-database
description: >-
  Queries the UniBind database for experimentally validated transcription factor
  (TF) binding sites. Use when retrieving direct TF-DNA interaction datasets,
  downloading binding site coordinates (BED/FASTA) for local analysis, or
  listing available datasets by species, cell line, or TF name. Don't use to
  query specific intervals, locations, genes, motif models or expression data.
---

# Unibind Database

Source: `science_skills/unibind_database/`

## Overview
-   **DON'T** attempt to use the UniBind API to query specific genomic
    intervals, locations, or genes.
-   **DON'T** guess or hallucinate genome coordinates. Always use
    `ensembl-database` as an external check if you're pulling local BED tracks
    for offline bedtools intersection.
-   **DON'T** use for motif models (PFMs). Use the **jaspar-database** skill
    instead.
-   **DON'T** use for gene expression data. UniBind only stores binding events.
-   **DON'T** assume tissue-specific expression from dataset lists alone.
-   **DON'T** use `cat` to read large JSON output files into context. The output
    is too large. Use `jq` or write your own code to parse the output files.

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/unibind_database/scripts/`:
- `unibind_api.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
