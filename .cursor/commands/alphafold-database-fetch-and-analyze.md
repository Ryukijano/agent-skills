# Alphafold Database Fetch And Analyze

Retrieve and analyze AlphaFold predicted structures for a protein. Use when the user provides a specific UniProt Accession ID and wants structural confidence metrics (pLDDT), domain boundary analysis,

Source: `science_skills/alphafold_database_fetch_and_analyze/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/alphafold_database_fetch_and_analyze/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/analyze_pae.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the
