---
name: address-pr-comments
description: Address pull request review comments systematically using GitHub CLI. Use when responding to PR feedback, iterating on code based on reviewer suggestions, or managing PR review workflows.
---

## Address PR Comments

### Steps

1. `gh pr checkout <PR_ID>`
2. Get comments: `gh api repos/<owner>/<repo>/pulls/<PR_ID>/comments`
3. For each comment: read file, analyze, make change or ask for clarification
4. Run tests after each change: `pytest tests/ -x -q`
5. Commit: `git commit -m "fix: address PR review comments"`
6. Push: `git push origin <branch>`
7. Summarize what was addressed and what needs user attention
