# Pdb Database

Use when you want to search for or download experimentally-determined 3D structures for biomolecules (proteins, nucleic acids, bound ligands). Supports searching by sequence similarity, structure simi

Source: `science_skills/pdb_database/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/pdb_database/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/download_coordinate_files.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Always prefer to use the provided scripts**. Only as a last resort use
