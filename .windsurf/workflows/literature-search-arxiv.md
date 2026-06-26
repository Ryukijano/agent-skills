---
description: Literature Search Arxiv workflow
---

# Literature Search Arxiv Workflow

Source: `science_skills/literature_search_arxiv/`

## Prerequisites
1. Ensure `uv` is installed
2. Add API keys to `~/.env` if needed
3. Read `science_skills/literature_search_arxiv/SKILL.md`

## Steps

### 1. Identify inputs
Determine what identifiers or queries the user needs.

### 2. Run script
```bash
cd science_skills/literature_search_arxiv
uv run scripts/download_paper.py <output.json> <function> <args>
```
### 3. Process output
- Use `jq` to filter JSON
- Extract relevant fields only

### Final. Report results
- Include source URLs
- Mention skill used
- Note any warnings
