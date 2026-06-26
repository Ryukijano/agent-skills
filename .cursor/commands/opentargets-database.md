# Opentargets Database

Query Open Targets Platform for target-disease associations, drug target discovery, tractability/safety data, genetics/omics evidence, known drugs, for therapeutic target identification.

Source: `science_skills/opentargets_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/opentargets_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/query_opentargets.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the
