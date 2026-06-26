# String Database

Query the STRING database for protein-protein interactions (PPIs), functional enrichment, and homology. Use when the user asks about interactions between specific proteins, interaction evidence, confi

Source: `science_skills/string_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/string_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/string_cli.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs
