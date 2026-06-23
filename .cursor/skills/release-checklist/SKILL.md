---
name: release-checklist
description: >-
  Versioned release process for research tools/libraries: changelog, tagging,
  building, publishing, post-release verification.
---

## Release Checklist

### Steps
1. Update CHANGELOG.md with user-facing changes.
2. Bump version in pyproject / __init__.
3. `git tag -a vX.Y.Z -m "Release vX.Y.Z"`.
4. `git push origin vX.Y.Z`.
5. Build: `python -m build`.
6. (If public) `twine upload dist/*` (or equivalent for HF spaces / internal registry).
7. Create GitHub release with notes.
8. Verify install in a fresh env: `pip install <pkg>==X.Y.Z` and smoke.
9. Announce (internal Slack / lab list / paper).

Related: `paper-code-release`, `dependency-management`.
