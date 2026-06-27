---
name: clinvar-database
description: >-
  Use when needing clinical significance, pathogenicity classifications (e.g.,
  Pathogenic, Benign, VUS), clinical evidence rationales, or finding "hard
  positive" benchmark controls for human genomic variants.
---

# Clinvar Database

Source: `science_skills/clinvar_database/`

## Overview
-   **Attempting to parse the E-utilities XML yourself** — Always use the
    provided `clinvar_api.py` client which handles the unpredictable XML schemas
    robustly.
-   **Getting HTTP 429 Too Many Requests** — The client throws an exception
    telling you to pause. Follow the prerequisite instructions to help the user
    add `NCBI_API_KEY` to the `.env` file, then retry.
-   **Sending raw DNA sequences to the API** — The API expects HGVS
    nomenclature, RS IDs, or proper Entrez coordinate syntax (`11[chr] AND
    1234[chrpos]`), not raw ATCG strings.
-   **For synonymous or non-coding variants** — HGVS nomenclature (e.g., CAPN3
    AND "c.551C>T") is more reliable than coordinate searches ([chrpos]), as
    many ClinVar records for these types lack precise genomic mappings.
-   **Case sensitivity in molecular consequences** — ClinVar returns mixed-case
    strings. Always use case-insensitive matching (`.lower()`) when filtering.
-   **Parsing `search` output as a bare list** — `search` returns a JSON object
    with `total_count`, `fetched_count`, and `variant_ids` — not a bare list.

## Core Rules
-   **Retmax Constraint**: The search command defaults to `--retmax 200`. For

## Scripts
Located in `science_skills/clinvar_database/scripts/`:
- `clinvar_api.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
