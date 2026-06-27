---
name: release-checklist
description: Create a release checklist for publishing a library or research code package. Use when preparing a versioned release, updating changelogs, building packages, or publishing to PyPI.
---

## Release Checklist

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md` with Added/Fixed/Changed sections
3. Run full test suite: `pytest tests/ -v`
4. Run linters: `ruff check . && ruff format --check .`
5. Verify clean git state
6. Create git tag: `git tag -a v<version> -m "Release v<version>"`
7. Create GitHub release: `gh release create v<version> --notes-file CHANGELOG.md`
8. Build package: `python -m build`
9. Upload to PyPI (if public): `twine upload dist/*`
