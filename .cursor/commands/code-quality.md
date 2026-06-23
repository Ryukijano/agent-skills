# Code Quality Pass

1. Install dev tools if missing: `pip install ruff basedpyright pre-commit pytest`.
2. Run `ruff check . --fix`.
3. Run `ruff format .`.
4. Run type check on core: `basedpyright core_app` (or pyright).
5. Run pre-commit on all if configured: `pre-commit run --all-files`.
6. Fix any remaining issues; re-run.
7. Commit with `chore: code quality cleanup (ruff + types)`.
8. If adding new public API, ensure it has types + docstring.

Apply `code-quality`, `testing-strategy`.
