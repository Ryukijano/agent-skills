---
name: protein-sequence-msa
description: >-
  Performs multiple sequence alignment of proteins with EBI Clustal Omega. Use
  when you need to align multiple sequences to assess similarity, domain
  conservation, or key residue conservation. Supports up to 4000 sequences and a
  maximum file size of 4 MB. Do not use to search for homologous proteins in a
  database (use MMseqs2, BLAST), align non-protein sequences (DNA, RNA), perform
  structural alignment (use Foldseek, PyMOL), or if you only have a single
  sequence.
---

# Protein Sequence Msa

Source: `science_skills/protein_sequence_msa/`

## Overview
Performs multiple sequence alignment of proteins with EBI Clustal Omega. Use when you need to align multiple sequences to assess similarity, domain conservation, or key residue conservation. Supports up to 4000 sequences and a maximum file size of 4 MB. Do not use to search for homologous proteins in a database (use MMseqs2, BLAST), align non-protein sequences (DNA, RNA), perform structural alignment (use Foldseek, PyMOL), or if you only have a single sequence.

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the alignment using

## Scripts
Located in `science_skills/protein_sequence_msa/scripts/`:
- `msa_align.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
