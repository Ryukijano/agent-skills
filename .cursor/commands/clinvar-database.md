# Clinvar Database

Use when needing clinical significance, pathogenicity classifications (e.g., Pathogenic, Benign, VUS), clinical evidence rationales, or finding "hard positive" benchmark controls for human genomic var

Source: `science_skills/clinvar_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/clinvar_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/clinvar_api.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Retmax Constraint**: The search command defaults to `--retmax 200`. For
