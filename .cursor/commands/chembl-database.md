# Chembl Database

Query the ChEMBL database for bioactive molecules, drug targets, bioactivity data, approved drugs, and chemical structures. Use when the user asks about compounds, targets, IC50/Ki values, drug mechan

Source: `science_skills/chembl_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/chembl_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/chembl_api.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   [!IMPORTANT] **Use the Utility Scripts**: You MUST ALWAYS use the provided
