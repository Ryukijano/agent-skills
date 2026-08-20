# Pubmed Database

Source: `science_skills/pubmed_database/`

## Overview
-   `verify_medical_spelling`: Spell-check biomedical terms before searching.
-   `match_raw_citations`: Resolve incomplete bibliographic citations to PMIDs.

## Core Rules
-   **API Use**: Always use the provided wrapper `scripts/pubmed_api.py` which

## Scripts
Located in `science_skills/pubmed_database/scripts/`:
- `pubmed_api.py`

## References
- `science_skills/pubmed_database/references/advanced-linking.md`
- `science_skills/pubmed_database/references/advanced-search.md`
- `science_skills/pubmed_database/references/bulk-workflows.md`
- `science_skills/pubmed_database/references/citation-matching.md`
- `science_skills/pubmed_database/references/cross-database-linking.md`
- `science_skills/pubmed_database/references/fetch-and-resolve.md`
- `science_skills/pubmed_database/references/search-and-discovery.md`
- `science_skills/pubmed_database/references/utilities.md`

## Examples
```bash
uv run scripts/pubmed_api.py ./search_results.json search_pubmed "BRCA1" --max_results 5
cat ./search_results.json | jq '.[]' -r
uv run scripts/pubmed_api.py ./abstracts.json fetch_article_abstracts "35113657"
cat ./abstracts.json | jq '.[0].title' -r
```

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
