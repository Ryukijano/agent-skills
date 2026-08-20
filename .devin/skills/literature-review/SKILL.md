# Systematic Literature Review

## Overview
Methodology for conducting thorough literature reviews, from initial search to synthesis.

## Search Strategy
1. **Keywords**: Define 3-5 core terms and synonyms
2. **Databases**: arXiv, Semantic Scholar, PubMed, Google Scholar, IEEE Xplore
3. **Snowballing**: Forward (citations of) + backward (cited by)
4. **Time range**: Last 3-5 years for fast-moving fields, 10+ for foundations

## Tools Available
```bash
# Search arXiv
python3 mcp_servers/research_workflow/server.py --cli search_arxiv --query "surgical instrument tracking" --max_results 20

# Search Semantic Scholar (includes citation counts)
python3 mcp_servers/research_workflow/server.py --cli search_semantic_scholar --query "3D endoscopy reconstruction" --max_results 20

# Get paper details and download PDF
python3 mcp_servers/research_workflow/server.py --cli get_arxiv_paper --arxiv_id 2401.12345 --download_pdf true

# Add to BibTeX
python3 mcp_servers/research_workflow/server.py --cli add_to_bibtex --arxiv_id 2401.12345

# Search your BibTeX database
python3 mcp_servers/research_workflow/server.py --cli search_bibtex --query "surgical"
```

## Screening Process
1. **Title/Abstract screen**: Include/exclude based on relevance
2. **Full-text screen**: Read paper, assess quality
3. **Data extraction**: Method, dataset, metrics, results
4. **Synthesis**: Group by approach, compare results

## Quality Assessment
- **Venue**: Top conferences (NeurIPS, ICML, CVPR, MICCAI) vs workshops
- **Citations**: High citation count = influential (but check recency)
- **Reproducibility**: Code available? Datasets public?
- **Statistical rigor**: Multiple seeds? Significance tests?

## Writing the Review
### Structure
1. **Introduction**: Define the problem and scope
2. **Taxonomy**: Categorize approaches (e.g., detection-based vs tracking-based)
3. **Chronological**: Show evolution over time
4. **Comparison table**: Methods × datasets/metrics
5. **Discussion**: Strengths, weaknesses, gaps
6. **Future directions**: Open problems

### Tips
- Don't just list papers — synthesize and compare
- Use comparison tables for clarity
- Identify gaps that your work addresses
- Cite seminal works, not just recent ones

## Reference Files
- MCP: `mcp_servers/research_workflow/server.py`
- Skills: `literature-search-arxiv`, `literature-search-openalex`, `deep-research`
- HF Skill: `huggingface-papers`

