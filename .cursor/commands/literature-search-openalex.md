# Literature Search Openalex

Query the OpenAlex scholarly database for research papers, authors, institutions, topics, sources, publishers, funders, geo-locations, and keywords. Use when searching academic papers, resolving DOIs,

Source: `science_skills/literature_search_openalex/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/literature_search_openalex/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/openalex_cli.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs
