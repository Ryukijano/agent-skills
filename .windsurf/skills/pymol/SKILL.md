---
name: pymol
description: >-
  Visualize, analyze, and render protein and molecular structures using PyMOL.
  Use when the user wants to create images of protein structures, perform
  structural alignments or superposition, measure distances or contacts,
  highlight binding sites or active site residues, color by B-factor/pLDDT, or
  analyze protein-ligand interactions. Do not use for docking, molecular
  dynamics, or sequence-only analysis.
---

# Pymol

Source: `science_skills/pymol/`

## Overview
-   The `output/` directory contains PNG images and a `.pse` session file.
-   Any measurements or metrics (distances, RMSD, atom counts) are printed to
    stdout by the PyMOL script. Report these values to the user.
-   Present PNG images to the user and describe the visualization.
-   Tell the user they can open the `.pse` file in their local PyMOL to further
    explore, rotate, or modify the visualization.
-   If the user wants modifications, load the saved `.pse` in a new script and
    re-run.
-   Large sessions with surfaces can exceed the `--max_output_mb` limit (default
    500 MB). Increase it with `--max_output_mb=1000` if needed.

## Core Rules
-   **Output paths must be absolute or relative to the user's project root.**

## References
- `science_skills/pymol/references/PYMOL_REFERENCE.md`
- `science_skills/pymol/references/RECIPES.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
