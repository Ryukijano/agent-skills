---
description: Literature Search Europepmc workflow
---

# Literature Search Europepmc Workflow

Source: `science_skills/literature_search_europepmc/`

## Prerequisites
1. Ensure `uv` is installed
2. Add API keys to `~/.env` if needed
3. Read `science_skills/literature_search_europepmc/SKILL.md`

## Steps

### 1. Identify inputs
Determine what identifiers or queries the user needs.

### 2. Run script
```bash
cd science_skills/literature_search_europepmc
uv run scripts/europepmc_api.py <output.json> <function> <args>
```
### 3. Process output
- Use `jq` to filter JSON
- Extract relevant fields only

### Final. Report results
- Include source URLs
- Mention skill used
- Note any warnings
