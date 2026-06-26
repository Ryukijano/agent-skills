# Alphagenome Single Variant Analysis

Analyzes genetic variant effects on gene expression (RNA-seq), chromatin accessibility (DNASE), histone marks (ChIP), and transcription factors using the AlphaGenome API. Use when the user asks about 

Source: `science_skills/alphagenome_single_variant_analysis/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/alphagenome_single_variant_analysis/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/analyze_ism.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **NEVER run `python3` or `python3 -c` directly.** The system Python does not
