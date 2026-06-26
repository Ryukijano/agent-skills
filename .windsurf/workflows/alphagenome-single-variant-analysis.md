---
description: Alphagenome Single Variant Analysis workflow
---

# Alphagenome Single Variant Analysis Workflow

Source: `science_skills/alphagenome_single_variant_analysis/`

## Prerequisites
1. Ensure `uv` is installed
2. Add API keys to `~/.env` if needed
3. Read `science_skills/alphagenome_single_variant_analysis/SKILL.md`

## Steps

### 1. Identify inputs
Determine what identifiers or queries the user needs.

### 2. Run script
```bash
cd science_skills/alphagenome_single_variant_analysis
uv run scripts/analyze_ism.py <output.json> <function> <args>
```
### 3. Process output
- Use `jq` to filter JSON
- Extract relevant fields only

### Final. Report results
- Include source URLs
- Mention skill used
- Note any warnings
