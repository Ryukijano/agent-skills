# Human Protein Atlas Database

Use when you want to retrieve semi-quantitative protein expression and spatial localisation data from the Human Protein Atlas (HPA).

Source: `science_skills/human_protein_atlas_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/human_protein_atlas_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/hpa_cli.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the
