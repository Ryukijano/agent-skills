---
name: academic-poster
description: >-
  Create academic conference posters. Use when designing posters for conference presentations, research showcases, or poster sessions.
---

# Academic Poster Design

## Overview
Create effective conference posters that communicate research clearly and attract visitors.

## Poster Structure
1. **Title + Authors + Affiliations** (top, large font)
2. **Abstract/Motivation** (brief, 2-3 sentences)
3. **Method** (diagrams > text)
4. **Results** (charts, tables, key numbers)
5. **Conclusions** (3-4 bullet points)
6. **References** (small font, bottom)
7. **Contact + QR code** (bottom right)

## Design Principles
- **Less text, more visuals**: Aim for 40% text, 60% visuals
- **Readable from 2m**: Title 85pt+, body text 24pt+
- **Color scheme**: 2-3 colors max, consistent with university branding
- **White space**: Don't cram — leave breathing room
- **Flow**: Guide the eye top-to-bottom, left-to-right

## Tools
- **LaTeX (beamerposter)**: Best for academic posters with math
- **PowerPoint/Keynote**: Quick and easy
- **Figma**: Collaborative design
- **Python (matplotlib)**: Generate charts, export as PDF

## LaTeX Template
```latex
\documentclass[final]{beamer}
\usepackage[size=custom,width=120,height=90,scale=1.0]{beamerposter}
\usetheme{confposter}
\setbeamercolor{block title}{fg=blue,bg=white}
\setbeamercolor{block body}{fg=black,bg=white}
```

## Chart Generation
Use the `academic-plotting` skill for publication-quality figures that work in both papers and posters.

## Reference Files
- Skill: `academic-plotting`, `data-visualization`
- MCP: `mcp_servers/research_workflow/server.py`

