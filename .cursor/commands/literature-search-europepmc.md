# Literature Search Europepmc

Search Europe PMC for scientific literature and download open-access full texts and PDFs. Retrieve full-text XML/plain text by PMCID, get citation lists and bibliography.

Source: `science_skills/literature_search_europepmc/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/literature_search_europepmc/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/europepmc_api.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Open Access Only**: This skill exclusively searches open-access content.
