---
description: String Database workflow
---

# String Database Workflow

Source: `science_skills/string_database/`

## Prerequisites
1. Ensure `uv` is installed
2. Add API keys to `~/.env` if needed
3. Read `science_skills/string_database/SKILL.md`

## Steps

### 1. Identify inputs
Determine what identifiers or queries the user needs.

### 2. Run script
```bash
cd science_skills/string_database
uv run scripts/string_cli.py <output.json> <function> <args>
```
### 3. Process output
- Use `jq` to filter JSON
- Extract relevant fields only

### Final. Report results
- Include source URLs
- Mention skill used
- Note any warnings
