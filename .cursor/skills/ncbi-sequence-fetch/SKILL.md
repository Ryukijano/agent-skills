# Ncbi Sequence Fetch

Source: `science_skills/ncbi_sequence_fetch/`

## Overview
-   **NCBI E-utilities docs**: https://www.ncbi.nlm.nih.gov/books/NBK25499/
-   **Entrez search syntax**: https://www.ncbi.nlm.nih.gov/books/NBK49540/
-   **Database list**: protein, nuccore, gene, pubmed, pmc, biosample, etc.
-   **Common accession formats**:
    -   `XP_` / `NP_` — NCBI RefSeq protein
    -   `AAA` to `AZZ` + digits — GenPept (translated GenBank)
    -   `MK`, `MN`, `HQ`, etc. + digits — GenBank nucleotide
    -   `ENSG`, `ENST`, `ENSP` — Ensembl (use `ensembl-database` skill instead)
    -   `Q`, `P`, `O` + digits — UniProt (use `uniprot-database` skill instead)

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/ncbi_sequence_fetch/scripts/`:
- `ncbi_fetch.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
