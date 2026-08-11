---
name: research-workflow
description: >-
  ArXiv search, paper digestion, BibTeX management, experiment tracking, and Semantic Scholar. Use when searching for papers, managing citations, creating experiments, or tracking research.
---

# Research Workflow MCP Server

## Overview
This skill provides 8 tools for research workflow via the MCP server at `mcp_servers/research_workflow/server.py`.

Dual CLI + MCP interface: use directly from terminal or via MCP-compatible agents.

## Available Tools

| Tool | Description |
|------|-------------|
| `search_arxiv` | See server.py for details |
| `get_arxiv_paper` | See server.py for details |
| `add_to_bibtex` | See server.py for details |
| `search_bibtex` | See server.py for details |
| `list_experiments` | See server.py for details |
| `create_experiment` | See server.py for details |
| `log_experiment` | See server.py for details |
| `search_semantic_scholar` | See server.py for details |

## Quick Start

### CLI Mode
```bash
python3 mcp_servers/research_workflow/server.py --cli search_arxiv --query 'CUDA Blackwell'
```

### MCP Mode
After running `mcp_servers/install_all.sh`, the server is available to all MCP-compatible agents.

## Reference Files
- Server code: `mcp_servers/research_workflow/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
