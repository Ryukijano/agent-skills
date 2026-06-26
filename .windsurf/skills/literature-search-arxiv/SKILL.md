---
name: literature-search-arxiv
description: >-
  Search for scientific papers, preprints, and publications on arXiv. Extract
  metadata, abstracts, and download full-text PDFs or HTML versions of papers.
  Use when the user asks to find research papers, literature, or specific arXiv
  IDs.
---

# Literature Search Arxiv

Source: `science_skills/literature_search_arxiv/`

## Overview
1.  Search for papers using `search_arxiv.py`. Review the JSON summaries.
2.  If full text is needed, use `download_paper.py` to fetch the PDF or HTML.
3.  If downloading a PDF, verify the PDF is not empty or corrupted.
4.  Read the downloaded file using standard file reading tools.

## Core Rules
-   **Terms of Use**: You MUST respect arXiv's Terms of Use.

## Scripts
Located in `science_skills/literature_search_arxiv/scripts/`:
- `download_paper.py`
- `download_paper_source.py`
- `search_arxiv.py`

## References
- `science_skills/literature_search_arxiv/references/query_syntax.md`

## Prerequisites
- Requires `uv` on PATH
- Use wrapper scripts for rate limits
