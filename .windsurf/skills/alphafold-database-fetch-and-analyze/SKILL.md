---
name: alphafold-database-fetch-and-analyze
description: >-
  Retrieve and analyze AlphaFold predicted structures for a protein. Use when
  the user provides a specific UniProt Accession ID and wants structural
  confidence metrics (pLDDT), domain boundary analysis, or disorder assessment.
  Do not use if the user only has a protein name, gene name, or amino acid
  sequence — ask for a UniProt ID first.
---

# Alphafold Database Fetch And Analyze

Source: `science_skills/alphafold_database_fetch_and_analyze/`

## Overview
1.  **Isoform / Large Protein Warning (MANDATORY):** Check the script output for
    any `[!] WARNING` lines. If the script reports that no canonical entry was
    found and an isoform was used, or if the protein is very large (>2700 AAs),
    you **MUST** prominently relay this warning to the user. Do not omit this
    warning.
2.  **Synthesize the Structural Analysis**: Combine the "pLDDT Conclusion" and
    the "PAE Structural Conclusion" into a single, cohesive overall summary.
    Describe the protein's overall folding confidence, the presence of
    disordered regions, and its rigid domain layout.
3.  Highlight the supporting metrics:
    -   Overall Global pLDDT and the breakdown of fraction confidence
        (especially Very Low vs. Very High).
    -   Domain Boundary Analysis (number of distinct global domains and their
        specific residue ranges).
4.  **Explicit Disorder Warning:** If the analysis concludes that the protein is
    highly intrinsically disordered (e.g., high fraction of <50 pLDDT or lack of
    rigid domains), issue a separate, prominent warning. Advise the user against
    proceeding with whole-protein downstream structural analysis (like Foldseek
    or docking). If small ordered domains exist amidst the disorder, advise the
    user to restrict any future analysis strictly to those specific residue
    boundaries.
5.  Remind the user that per-residue pLDDT is embedded in the B-factor column of
    the downloaded mmCIF file.

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/alphafold_database_fetch_and_analyze/scripts/`:
- `analyze_pae.py`
- `analyze_plddt.py`
- `fetch_structure.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
