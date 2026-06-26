---
name: jaspar-database
description: >-
  Query the JASPAR database for Transcription Factor (TF) binding profiles. Use
  when retrieving Position Frequency Matrices (PFMs) or Position Weight Matrices
  (PWMs) for specific TFs, resolving gene symbols to JASPAR Matrix IDs, or
  getting TF metadata. Supports multiple output formats (MEME, TRANSFAC, PFM,
  JASPAR, YAML).
---

# Jaspar Database

Source: `science_skills/jaspar_database/`

## Overview
*   **DON'T** pass gene symbols (e.g., `JUN`) to `get_tf_motif`. You must pass
    the `MA...` Matrix ID.
*   **DON'T** forget the `--tax-id` when resolving a TF name.
*   **DON'T** use this skill for determining tissue-specific epigenetic
    availability (JASPAR shows *potential* binding, not *actual* tissue
    expression context).
*   **DON'T** use this skill to model how a specific protein mutation affects
    binding.

## Scripts
Located in `science_skills/jaspar_database/scripts/`:
- `jaspar_api.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
