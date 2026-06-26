# Pubchem Database

Query PubChem, search by name/CID/SMILES, retrieve properties, similarity/substructure searches, bioactivity, for cheminformatics. Use when a user asks about a specific chemical, drug, or molecule.

Source: `science_skills/pubchem_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/pubchem_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/pubchem_api.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the
