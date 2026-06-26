# Interpro Database

Identify domains, families, and sites in proteins; find all proteins in a family or sharing a domain; explore species distribution for a domain; annotate genomes with protein families and GO terms. In

Source: `science_skills/interpro_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/interpro_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/interpro_client.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the `scripts/interpro_client.py` helper
