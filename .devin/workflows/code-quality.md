---
description: Enforce code quality with formatting, linting, type checking, and pre-commit hooks
---

## Code Quality Setup

1. Install tools:
   ```bash
   pip install ruff basedpyright pre-commit
   ```

2. Create `pyproject.toml` with ruff config:
   ```toml
   [tool.ruff]
   line-length = 100
   target-version = "py310"
   [tool.ruff.lint]
   select = ["E", "F", "W", "I", "UP", "B", "C4", "SIM"]
   ```

3. Run ruff on all files to fix existing issues:
   ```bash
   ruff check . --fix
   ruff format .
   ```

4. Set up pre-commit (call `/pre-commit-setup` workflow).

5. Check for common ML code issues:
   ```bash
   grep -rn "print(" --include="*.py" | grep -v "logger\|tqdm\|wandb"
   grep -rn "import \*" --include="*.py"
   grep -rn "def .*=\[\]" --include="*.py"  # mutable defaults
   ```

6. Fix all issues found.

7. Commit: `git commit -m "chore: code quality cleanup"`

8. Summarize: issues found, issues fixed, remaining warnings.
