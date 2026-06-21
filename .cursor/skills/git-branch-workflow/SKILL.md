---
name: git-branch-workflow
description: Standardized git branching, commit message conventions, and pull request creation. Use when creating feature branches, writing commit messages, creating PRs, or managing version control across ML research projects.
---

## Git Branch Workflow for ML Research Projects

### Branch naming convention

```
<type>/<short-description>
```

Types:
- `feat/` — New feature or model implementation
- `fix/` — Bug fix
- `experiment/` — Experimental changes (may be squashed later)
- `docs/` — Documentation only
- `refactor/` — Code restructuring without behavior change
- `test/` — Adding or updating tests

Examples:
```
feat/tdv-pretraining
fix/deformable-detr-spatial-shape
experiment/lora-rank-sweep
docs/update-readme-with-results
```

### Commit message convention

```
<type>: <short description in imperative mood>

## Optional: Longer description
- Bullet points for key changes
- Reference issues: #123
```

Types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `experiment`

Examples:
```
feat: TDV pretraining integration + critical DETR/LoRA/DN fixes

fix: pass per-level spatial shapes to deformable cross-attention

experiment: try LoRA rank=4 with alpha=8 on blocks 6+

docs: add TDV pretraining instructions to README
```

### Standard workflow

```bash
# 1. Create branch from main (or feature branch)
git checkout main
git pull origin main
git checkout -b feat/<description>

# 2. Make changes, stage, and commit
git add -A
git commit -m "feat: <description>"

# 3. Push and create PR
git push -u origin feat/<description>
gh pr create --title "feat: <description>" --body "## Summary" --base main
```

### PR description template

```markdown
## Summary
<1-2 sentence summary>

## Changes
- <Key change 1>
- <Key change 2>

## Testing
- [ ] Smoke test passes
- [ ] Training runs for N steps without crash
- [ ] Eval metrics match expectations

## Checklist
- [ ] No debug prints left
- [ ] Configs updated
- [ ] Documentation updated
```

### Squash merging for experiment branches

```bash
# Squash N commits into one before merging
git rebase -i main
# Mark all but first as "squash" in the editor

# Or via GitHub: "Squash and merge" button
```
