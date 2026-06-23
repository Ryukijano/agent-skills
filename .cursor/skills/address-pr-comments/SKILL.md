---
name: address-pr-comments
description: Systematic process and conventions for triaging and addressing GitHub PR review comments in ML research projects. Use with the /address-pr-comments command.
---

## Addressing PR Comments

### Workflow
1. Checkout PR branch.
2. Pull comments via gh api + jq.
3. Prioritize: correctness/leak/security > perf/testing > style.
4. One change + narrow verification (pytest or 2-step smoke) per comment.
5. Commit with message referencing the comment/PR.
6. Push and reply on GitHub.

### Hygiene
- Keep branch rebased on latest main.
- Never leave uncommitted work at end of session (continual-learning habit).
- Run full `/code-review` before requesting re-review.

Related: `git-branch-workflow`, `code-review`, `code-quality`.
