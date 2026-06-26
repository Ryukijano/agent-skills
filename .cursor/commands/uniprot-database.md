# Uniprot Database

Access protein metadata, function, taxonomy, and sequences across UniProtKB, UniParc, and UniRef. Use when searching for proteins, mapping identifiers, or retrieving functional annotations and publica

Source: `science_skills/uniprot_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/uniprot_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/uniprot_tools.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: Always use the provided Python scripts (e.g.,
