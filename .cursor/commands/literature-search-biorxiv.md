# Literature Search Biorxiv

Browse, filter, and download life sciences, biology, and medical preprints from bioRxiv and medRxiv. Supports fetching paper metadata by DOI, and browsing by date range with category and keyword filte

Source: `science_skills/literature_search_biorxiv/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/literature_search_biorxiv/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/search_by_dates.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the
