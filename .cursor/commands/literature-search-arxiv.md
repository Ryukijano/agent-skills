# Literature Search Arxiv

Search for scientific papers, preprints, and publications on arXiv. Extract metadata, abstracts, and download full-text PDFs or HTML versions of papers. Use when the user asks to find research papers,

Source: `science_skills/literature_search_arxiv/`

## Prerequisites
- `uv` on PATH
- API keys in `~/.env` if needed

## Workflow
1. Read `science_skills/literature_search_arxiv/SKILL.md`
2. Identify required inputs
3. Run: `uv run scripts/download_paper.py <out.json> <fn> <args>`
4. Filter with `jq`
5. Report results with URLs

## Core Rules
-   **Terms of Use**: You MUST respect arXiv's Terms of Use.
