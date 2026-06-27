---
name: protein-sequence-similarity-search
description: >-
  Searches for homologous protein sequences using MMseqs2 (fast, default) or
  BLAST (comprehensive, fallback). Trigger this whenever the user provides a
  protein sequence or FASTA file and asks to find homologues, sequence matches,
  or wants to infer protein function based on sequence similarity, but not when
  the user wants to infer protein function based on structural similarity.
---

# Protein Sequence Similarity Search

Source: `science_skills/protein_sequence_similarity_search/`

## Overview
Searches for homologous protein sequences using MMseqs2 (fast, default) or BLAST (comprehensive, fallback). Trigger this whenever the user provides a protein sequence or FASTA file and asks to find homologues, sequence matches, or wants to infer protein function based on sequence similarity, but not when the user wants to infer protein function based on structural similarity.

## Core Rules
-   **Strict Validation**: For BLAST, only use database codes listed in the

## Scripts
Located in `science_skills/protein_sequence_similarity_search/scripts/`:
- `mmseqs2_search.py`
- `uniprot_blast.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
