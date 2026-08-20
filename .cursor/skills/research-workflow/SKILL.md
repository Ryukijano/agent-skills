# Research Workflow MCP Server

## Overview
This skill provides 8 tools for research workflow via the MCP (Model Context Protocol) server at `mcp_servers/research_workflow/server.py`.

The server has a **dual CLI + MCP interface** — you can use it directly from the terminal or via any MCP-compatible AI agent (Cursor, Devin, Claude, Windsurf, Gemini).

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

### CLI Mode (direct terminal)
```bash
python3 mcp_servers/research_workflow/server.py --cli search_arxiv --query 'CUDA Blackwell'
```

### MCP Mode (via AI agent)
The server is automatically available to MCP-compatible agents after running `mcp_servers/install_all.sh`.

### MCP Inspector (web UI)
```bash
npx @modelcontextprotocol/inspector python3 mcp_servers/research_workflow/server.py
```

## Installation
```bash
bash mcp_servers/install_all.sh
```

## Reference Files
- Server code: `mcp_servers/research_workflow/server.py`
- Install script: `mcp_servers/install_all.sh`
- Full documentation: `mcp_servers/README.md`
