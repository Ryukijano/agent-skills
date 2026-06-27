---
description: Set up CI/CD pipelines for ML research projects using GitHub Actions
---

## CI/CD Setup

1. Create `.github/workflows/` directory:
   ```bash
   mkdir -p .github/workflows
   ```

2. Create lint workflow (`.github/workflows/lint.yml`):
   - Checkout, setup Python, install ruff, run `ruff check . && ruff format --check .`

3. Create test workflow (`.github/workflows/test.yml`):
   - Checkout, setup Python, install deps, run `pytest tests/ -v`

4. Create pre-commit workflow (`.github/workflows/pre-commit.yml`):
   - Run `pre-commit run --all-files`

5. Add status badge to README:
   ```markdown
   ![CI](https://github.com/<user>/<repo>/actions/workflows/test.yml/badge.svg)
   ```

6. Commit and push:
   ```bash
   git add .github/
   git commit -m "ci: add GitHub Actions workflows"
   git push
   ```

7. Verify workflows run on next push/PR.

8. Summarize: workflows created, badge URL, CI status.
