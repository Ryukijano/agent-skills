---
name: setup-ml-project
description: Standard scaffolding conventions for new ML research projects in this lab (directory layout, Cursor assets, first smoke, reproducibility basics). Pairs with /setup-ml-project.
---

## ML Project Scaffolding

### Recommended tree
core_app/ configs/ scripts/ jobs/ tests/ outputs/ inputs/ docs/ .cursor/skills/ .cursor/commands/

### Must-haves on day 1
- AGENTS.md with workspace facts + preferences.
- README with one-command smoke.
- .gitignore covering data/ outputs/ wandb/ checkpoints.
- `tests/test_smoke.py` that imports model and runs 2-step forward.
- At least the core portable Cursor skills copied in.

### Cursor bootstrap
Copy: reproducibility, code-quality, testing-strategy, git-branch-workflow, debug-training, code-review, experiment-tracking, and their command counterparts.

Related: `reproducibility`, `code-quality`, `git-branch-workflow`.
