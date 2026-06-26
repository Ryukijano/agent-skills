# Embl Ebi Ols

Query and search the EMBL-EBI Ontology Lookup Service (OLS) for biomedical ontology terms, definitions, and hierarchies across 250+ ontologies (e.g., GO, DOID, HP). Use when the user asks to search fo

Source: `science_skills/embl_ebi_ols/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/embl_ebi_ols/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/get_individual.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   [!IMPORTANT] **Use the Utility Scripts**: You MUST ALWAYS use the provided
