---
name: ucsc-conservation-and-tfbs
description: >-
  Fetch Evolutionary Conservation scores (phyloP, phastCons) and Transcription
  Factor Binding Sites (TFBS) from the UCSC Genome Browser. Use when analyzing
  whether genomic variants or regions are evolutionarily conserved, functionally
  important, or bounded by TF regulators across major projects (ENCODE, JASPAR,
  ReMap).
---

# Ucsc Conservation And Tfbs

Source: `science_skills/ucsc_conservation_and_tfbs/`

## Overview
*   **DON'T** query mammalian (`--collection mammal`) constraint if you are
    explicitly looking for deep evolutionary roots across all vertebrates. Use
    the default `vertebrate` collection.
*   **DON'T** use this skill for determining the ancestral state reconstruction
    of a nucleotide (this skill provides measures of *how much* sites have
    changed, not *what* the ancestral nucleotide was).
*   **DON'T** assume low conservation strictly means neutral/useless sequence;
    it could also reflect a high local mutation rate which conservation scores
    alone cannot distinguish.
*   **DON'T** print output on standard out, or run cat on output to files. The
    output is too large. Use jq or write your own code to parse the output
    files.
*   **DON'T** use hg19 unless the user has explicitly asked for it. The default
    should be to always use hg38.

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/ucsc_conservation_and_tfbs/scripts/`:
- `get_conservation.py`
- `get_tfbs.py`
- `list_tracks.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
