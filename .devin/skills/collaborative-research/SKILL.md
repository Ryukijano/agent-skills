---
name: collaborative-research
description: >-
  Manage collaborative research projects with multiple contributors. Use when coordinating with supervisors, sharing code, managing issues, or preparing multi-author papers.
---

# Collaborative Research Management

## Overview
Best practices for managing collaborative ML research projects, from code sharing to multi-author papers.

## Code Collaboration
### Git Workflow
- Use feature branches: `git checkout -b feature/new-detector`
- Small, focused PRs (see `git-branch-workflow` skill)
- Review every PR (see `code-review` skill)
- Use GitHub Issues for bugs and feature requests

### GitHub MCP Server
The GitHub MCP Server is available for repo management:
- Create/update issues
- Manage PRs and reviews
- Monitor CI/CD
- Search code across repos

### Project Structure
```
project/
├── README.md           # Setup + usage instructions
├── CONTRIBUTING.md     # How to contribute
├── configs/            # All experiment configs
├── src/                # Source code
├── scripts/            # Run scripts (run_train.sh, run_eval.sh)
├── notebooks/          # Exploratory notebooks
├── data/               # Data links (not actual data)
├── results/            # Experiment outputs (gitignored)
└── docs/               # Documentation
```

## Multi-Author Papers
### Author Order
- First author: did the bulk of the work
- Last author: senior supervisor/PI
- Middle authors: by contribution amount

### Writing Collaboration
- Use Overleaf for LaTeX collaboration
- Use Google Docs for outline/brainstorming
- Track contributions: who wrote what section
- Regular writing meetings (weekly)

### Citation Management
- Shared BibTeX file in the repo
- Use `research-workflow` MCP to search and add citations
- Agree on citation style early

## Supervisor Communication
- Weekly progress meetings
- Share a progress doc before each meeting:
  - What I did last week
  - What I'm doing this week
  - Blockers / questions
  - Results to discuss

## Conference Deadlines
- Track deadlines: https://aideadlin.es/
- Submit 2 days early (not at the deadline)
- Get supervisor review 1 week before deadline
- Prepare rebuttal template in advance

## Reference Files
- Skills: `git-branch-workflow`, `code-review`, `ml-paper-writing`, `paper-submission-prep`
- MCP: `mcp_servers/research_workflow/server.py`

