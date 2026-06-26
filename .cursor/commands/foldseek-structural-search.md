# Foldseek Structural Search

Performs 3D structural searches of proteins against various databases (PDB, AlphaFold, CATH, MGnify, etc.) using the Foldseek API. Use ONLY when the user provides a physical 3D coordinate file (.cif, 

Source: `science_skills/foldseek_structural_search/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/foldseek_structural_search/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/search.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **File Requirement**: This tool absolutely cannot search by sequence, name,
