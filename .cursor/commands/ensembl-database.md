# Ensembl Database

Query the Ensembl database to resolve gene, transcript, and protein IDs, fetch genomic or protein sequences, retrieve gene structures (exons), and get variant consequence and effect predictions (VEP).

Source: `science_skills/ensembl_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/ensembl_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/ensembl_api.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the
