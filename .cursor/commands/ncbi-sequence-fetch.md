# Ncbi Sequence Fetch

Retrieve protein and nucleotide sequences from NCBI databases using E-utilities. Supports direct accession lookup, CDS translation, gene+organism search, locus lookup, PubMed-linked sequences, patent 

Source: `science_skills/ncbi_sequence_fetch/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/ncbi_sequence_fetch/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/ncbi_fetch.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the
