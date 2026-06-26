# Protein Sequence Msa

Performs multiple sequence alignment of proteins with EBI Clustal Omega. Use when you need to align multiple sequences to assess similarity, domain conservation, or key residue conservation. Supports 

Source: `science_skills/protein_sequence_msa/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/protein_sequence_msa/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/msa_align.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the alignment using
