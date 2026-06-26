# Pubmed Database

Search PubMed for scientific literature, including published clinical trials. Fetch abstracts and full text. Link published research to biological databases (gene, protein, nucleotide, PubChem) to dis

Source: `science_skills/pubmed_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/pubmed_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/pubmed_api.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **API Use**: Always use the provided wrapper `scripts/pubmed_api.py` which
