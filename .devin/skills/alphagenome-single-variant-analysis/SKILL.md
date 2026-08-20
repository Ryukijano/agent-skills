# Alphagenome Single Variant Analysis

Source: `science_skills/alphagenome_single_variant_analysis/`

## Overview
| Script                      | Purpose                                        |
| --------------------------- | ---------------------------------------------- |
| `lookup_gene_info`          | Comprehensive gene and transcript lookup using |
:                             : GTF data                                       :
| `resolve_ontology_terms`    | Biological terms → UBERON/CL/EFO IDs           |
| `visualize_variant_effects` | REF/ALT visualization (expression, regulatory, |
:                             : splicing)                                      :
| `analyze_ism`               | In-Silico Mutagenesis SeqLogo generation       |
| `interpret_splicing`        | Quantitative splicing analysis (delta scores,  |
:                             : junctions)                                     :
| `visualize_genome_tracks`   | Genomic track visualization for a region       |

## Core Rules
-   **NEVER run `python3` or `python3 -c` directly.** The system Python does not

## Scripts
Located in `science_skills/alphagenome_single_variant_analysis/scripts/`:
- `analyze_ism.py`
- `generate_ontology_mapping.py`
- `interpret_splicing.py`
- `lookup_gene_info.py`
- `resolve_ontology_terms.py`
- `visualize_genome_tracks.py`
- `visualize_variant_effects.py`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
