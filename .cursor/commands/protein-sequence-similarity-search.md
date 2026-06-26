# Protein Sequence Similarity Search

Searches for homologous protein sequences using MMseqs2 (fast, default) or BLAST (comprehensive, fallback). Trigger this whenever the user provides a protein sequence or FASTA file and asks to find ho

Source: `science_skills/protein_sequence_similarity_search/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/protein_sequence_similarity_search/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/mmseqs2_search.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Strict Validation**: For BLAST, only use database codes listed in the
