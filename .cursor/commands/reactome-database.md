# Reactome Database

Query the Reactome database (Analysis and Content Services). Use when the user asks about pathway analysis, gene list enrichment, retrieving results by token, finding unmapped or not-found identifiers

Source: `science_skills/reactome_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/reactome_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/reactome_analysis.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs
