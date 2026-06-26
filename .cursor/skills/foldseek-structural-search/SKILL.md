---
name: foldseek-structural-search
description: >-
  Performs 3D structural searches of proteins against various databases (PDB,
  AlphaFold, CATH, MGnify, etc.) using the Foldseek API. Use ONLY when the user
  provides a physical 3D coordinate file (.cif, .mmcif, or .pdb) and wants to
  find structurally similar proteins. Do NOT use if the user only provides a
  protein sequence, gene name, or UniProt ID.
---

# Foldseek Structural Search

Source: `science_skills/foldseek_structural_search/`

## Overview
Performs 3D structural searches of proteins against various databases (PDB, AlphaFold, CATH, MGnify, etc.) using the Foldseek API. Use ONLY when the user provides a physical 3D coordinate file (.cif, .mmcif, or .pdb) and wants to find structurally similar proteins. Do NOT use if the user only provides a protein sequence, gene name, or UniProt ID.

## Core Rules
-   **File Requirement**: This tool absolutely cannot search by sequence, name,

## Scripts
Located in `science_skills/foldseek_structural_search/scripts/`:
- `search.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
