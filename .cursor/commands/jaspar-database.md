# Jaspar Database

Query the JASPAR database for Transcription Factor (TF) binding profiles. Use when retrieving Position Frequency Matrices (PFMs) or Position Weight Matrices (PWMs) for specific TFs, resolving gene sym

Source: `science_skills/jaspar_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/jaspar_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/jaspar_api.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs
