---
name: thesis-writing
description: >-
  Write and structure PhD thesis chapters with LaTeX. Use when writing thesis chapters, managing citations, creating the thesis outline, or preparing for viva defense.
---

# PhD Thesis Writing

## Overview
Structured approach to writing a PhD thesis in computer science / medical AI, with LaTeX templates and chapter organization.

## Thesis Structure (University of Leeds Format)
1. **Abstract** (1-2 pages)
2. **Introduction** (10-15 pages): Motivation, problem statement, contributions, outline
3. **Background & Related Work** (20-30 pages): Literature review, technical background
4. **Methodology** (30-40 pages): Technical contributions (may span multiple chapters)
5. **Experiments & Results** (20-30 pages): Evaluation, ablations, qualitative results
6. **Discussion** (5-10 pages): Limitations, future work, broader impact
7. **Conclusion** (3-5 pages): Summary of contributions
8. **References**
9. **Appendices**: Additional experiments, hyperparameter tables

## LaTeX Setup
```latex
\documentclass[12pt,a4paper]{report}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage[round]{natbib}  % or biblatex
\usepackage{algorithm}
\usepackage{algorithmic}
```

## Writing Workflow
1. **Outline first**: Write chapter outlines before content
2. **Daily writing**: Aim for 500-1000 words/day
3. **Cite as you write**: Don't leave citations for later
4. **Figures early**: Create placeholder figures, refine later
5. **Iterate**: Write rough → revise → polish → proofread

## Citation Management
- Use BibTeX with `natbib` or `biblatex`
- Track citations with `research-workflow` MCP server
- Search for papers: `python3 mcp_servers/research_workflow/server.py --cli search_arxiv --query "surgical MOT"`
- Add to BibTeX: `python3 mcp_servers/research_workflow/server.py --cli add_to_bibtex --arxiv_id 2401.12345`

## Paper-to-Chapter Mapping
- Each published paper → one thesis chapter (expanded with more detail)
- Add unpublished experiments and negative results
- Include more related work context than paper allows

## Viva Preparation
- Know your contributions cold
- Anticipate questions on methodology choices
- Prepare to discuss limitations honestly
- Practice with mock vivas

## Reference Files
- Skill: `ml-paper-writing` (for individual papers)
- Skill: `academic-plotting` (for figures)
- MCP: `mcp_servers/research_workflow/server.py` (for literature search)
- University of Leeds thesis template: check university guidelines

