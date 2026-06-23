---
name: refactor-extract-module
description: Safe patterns for extracting code into new modules or packages without breaking imports or behavior. Includes tests, circular import checks, and incremental commits.
---

## Refactoring / Extraction

### Process
1. Identify cohesive functionality to extract.
2. Create the new file/module with the extracted code (copy first).
3. Update imports in the new location and the old caller (use relative or absolute consistently).
4. Add or update a minimal test that exercises the extracted surface.
5. Run linter + smoke test on both old and new paths.
6. Check for circular imports: `python -c "import old; import new"`.
7. Commit with clear message: "refactor: extract <name> into core_app/<module>".
8. Update any docs or AGENTS.md that referenced the old location.

### Guardrails
- Small steps; verify after each.
- Keep public API stable or explicitly deprecate.
- For large extractions, keep a thin forwarding shim temporarily.

Related: `code-quality`, `testing-strategy`, `safe-refactor` (if available via skills-cursor).
