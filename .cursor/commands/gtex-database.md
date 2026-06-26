# Gtex Database

Use when you want to retrieve quantitative RNA expression data and variant eQTL information from the GTEx (Genotype-Tissue Expression) Project across 54 non-diseased tissue sites.

Source: `science_skills/gtex_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/gtex_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/gtex_cli.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs
