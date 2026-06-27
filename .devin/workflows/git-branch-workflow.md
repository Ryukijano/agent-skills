---
description: Standardized git branching, commit conventions, and pull request creation
---

## Git Branch Workflow

1. Create branch from main:
   ```bash
   git checkout main && git pull origin main
   git checkout -b <type>/<short-description>
   ```
   Types: `feat/`, `fix/`, `experiment/`, `docs/`, `refactor/`, `test/`

2. Make changes and commit with conventional message:
   ```bash
   git add -A
   git commit -m "feat: <description in imperative mood>"
   ```

3. Push and create PR:
   ```bash
   git push -u origin <type>/<description>
   gh pr create --title "feat: <description>" --body "## Summary" --base main
   ```

4. Use PR description template with Summary, Changes, Testing, Checklist sections.

5. For experiment branches, squash merge to keep history clean.

6. Summarize: branch name, PR URL, changes made.
