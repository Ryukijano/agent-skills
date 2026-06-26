# Encode Ccres Database

Query the ENCODE Registry of cis-Regulatory Elements (cCREs) via the SCREEN GraphQL API, or make custom queries to the ENCODE Portal REST API for experiments and files (ChIP-seq peaks, etc.). Use when

Source: `science_skills/encode_ccres_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/encode_ccres_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/encode_portal_api.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the
