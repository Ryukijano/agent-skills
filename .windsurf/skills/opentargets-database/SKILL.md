---
name: opentargets-database
description: >-
  Query Open Targets Platform for target-disease associations, drug target
  discovery, tractability/safety data, genetics/omics evidence, known drugs, for
  therapeutic target identification.
---

# Opentargets Database

Source: `science_skills/opentargets_database/`

## Overview
-   **ID Formats**:
    -   Disease IDs must be in EFO format (e.g. `EFO_0000685`).
    -   Target IDs must be Ensembl IDs (e.g. `ENSG00000169083`), not HGNC
        symbols. If you only have a gene symbol, you may need to map it first
        using a custom GraphQL `search` query.
    -   Variant IDs are formatted as `chromosome_position_ref_alt` (e.g.,
        `1_154426264_C_T`). A `chr` prefix (e.g. `chr1_154426264_C_T`) is
        automatically stripped by the tool.
    -   Study IDs can be GWAS Catalog IDs (e.g. `GCST90204201`) or
        project-specific IDs (e.g. `FINNGEN_R12_RX_CROHN_2NDLINE`).
-   **Truncation**: The tool truncates arrays longer than `--limit` to protect
    the context window. If you see `"_truncated"`, you can run the query again
    with a higher limit if you specifically need more data, but be cautious with
    large limit values. Always use the `--output` flag to save the result to a
    file and avoid terminal output truncation.
-   **Pagination and incomplete results**: The `--page-size` option (default:
    200) controls how many items are fetched from the API. **Always check the
    `count` field in the response and compare it to the number of `rows`
    actually returned.** If `count` > number of rows, you have incomplete data —
    either increase `--page-size` to fetch more, or inform the user that only a
    partial result set was returned. This is especially important for `get-l2g`
    without `--study-id`, which can return hundreds of credible sets.

## Core Rules
-   **Use the Wrapper**: ALWAYS execute the provided helper scripts to query the

## Scripts
Located in `science_skills/opentargets_database/scripts/`:
- `query_opentargets.py`

## References
- `science_skills/opentargets_database/references/OpenTargets_GraphQL_Guide.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
