---
name: embl-ebi-ols
description: >-
  Query and search the EMBL-EBI Ontology Lookup Service (OLS) for biomedical
  ontology terms, definitions, and hierarchies across 250+ ontologies (e.g., GO,
  DOID, HP). Use when the user asks to search for terms, retrieve details,
  navigate hierarchies (parents, children, ancestors), look up properties and
  individuals, get autocomplete suggestions, or access ontology metadata and
  statistics.
---

# Embl Ebi Ols

Source: `science_skills/embl_ebi_ols/`

## Overview
1.  Use `suggest_ols.py` for autocomplete when you have a partial term name.
2.  Search for terms using `search_ols.py`. Use `--defining` to prioritize
    authoritative definitions. Use `--exact` for entity resolution.
3.  If full details are needed, use `get_term.py` with the OBO ID or IRI. Use
    `--summary` for a concise view.
4.  To explore a term's hierarchy, use `get_term.py --relations
    parents,children` for is-a only, or `--relations
    hierarchicalParents,hierarchicalChildren` for "part of" etc.
5.  To explore from the top down, use `get_term.py --ontology go --roots`.
6.  For properties or individuals, use `get_property.py` or `get_individual.py`.
7.  To discover available ontologies, use `get_ontology.py`.
8.  To check OLS index status, use `get_stats.py`.

## Core Rules
-   [!IMPORTANT] **Use the Utility Scripts**: You MUST ALWAYS use the provided

## Scripts
Located in `science_skills/embl_ebi_ols/scripts/`:
- `get_individual.py`
- `get_ontology.py`
- `get_property.py`
- `get_stats.py`
- `get_term.py`
- `ols_utils.py`
- `search_ols.py`
- `suggest_ols.py`

## References
- `science_skills/embl_ebi_ols/references/api_reference.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
