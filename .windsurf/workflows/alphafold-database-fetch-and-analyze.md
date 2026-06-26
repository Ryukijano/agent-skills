---
description: Alphafold Database Fetch And Analyze workflow
---

# Alphafold Database Fetch And Analyze Workflow

Source: `science_skills/alphafold_database_fetch_and_analyze/`

## Prerequisites
1. Ensure `uv` is installed
2. Add API keys to `~/.env` if needed
3. Read `science_skills/alphafold_database_fetch_and_analyze/SKILL.md`

## Steps

### 1. Identify inputs
Determine what identifiers or queries the user needs.

### 2. Run script
```bash
cd science_skills/alphafold_database_fetch_and_analyze
uv run scripts/analyze_pae.py <output.json> <function> <args>
```
### 3. Process output
- Use `jq` to filter JSON
- Extract relevant fields only

### Final. Report results
- Include source URLs
- Mention skill used
- Note any warnings
