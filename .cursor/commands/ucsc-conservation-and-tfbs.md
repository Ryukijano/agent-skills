# Ucsc Conservation And Tfbs

Fetch Evolutionary Conservation scores (phyloP, phastCons) and Transcription Factor Binding Sites (TFBS) from the UCSC Genome Browser. Use when analyzing whether genomic variants or regions are evolut

Source: `science_skills/ucsc_conservation_and_tfbs/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/ucsc_conservation_and_tfbs/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/get_conservation.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the
