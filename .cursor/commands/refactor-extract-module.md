# Refactor: Extract Module

1. Identify the code to extract and write a one-sentence justification.
2. Create the target file (e.g. `core_app/utils/video.py`).
3. Move the functions/classes; keep a thin re-export in the old location if many call sites.
4. Update all internal imports.
5. Add a minimal test for the new module.
6. Run `ruff check .`, type check, and `pytest tests/test_smoke.py -q` (or broader impacted).
7. Check no circular imports.
8. Commit: `git commit -m "refactor: extract <name> into <module>"`.
9. If public API changed, update docs / README / AGENTS.
10. Open or update PR with clear "no behavior change" note.

Apply `refactor-extract-module`, `code-quality`, `testing-strategy`.
