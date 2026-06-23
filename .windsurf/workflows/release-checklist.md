---
description: Create a release checklist for publishing a library or research code package
---

## Release Checklist

1. Update version number:
   ```bash
   # In pyproject.toml
   version = "0.2.0"
   # Or use bumpversion
   pip install bump-my-version
   bump-my-version bump patch  # 0.1.0 → 0.1.1
   bump-my-version bump minor  # 0.1.0 → 0.2.0
   ```

2. Update CHANGELOG.md:
   ```markdown
   ## [0.2.0] - 2026-06-23

   ### Added
   - TDV pretraining pipeline
   - Progressive unfreezing support

   ### Fixed
   - Deformable DETR spatial shape bug
   - NCCL P2P segfault on L40S

   ### Changed
   - LoRA default rank 16 → 8
   ```

3. Run full test suite:
   ```bash
   pytest tests/ -v
   ```

4. Run linters:
   ```bash
   ruff check .
   ruff format --check .
   ```

5. Check that all dependencies are pinned in lock file:
   ```bash
   ls requirements-lock.txt uv.lock 2>/dev/null
   ```

6. Verify clean git state:
   ```bash
   git status  # should be clean
   ```

7. Create git tag:
   ```bash
   git tag -a v0.2.0 -m "Release v0.2.0"
   git push origin v0.2.0
   ```

8. Create GitHub release:
   ```bash
   gh release create v0.2.0 --title "v0.2.0" --notes-file CHANGELOG.md
   ```

9. Build package (if installable):
   ```bash
   pip install build
   python -m build
   # Upload to PyPI (if public library)
   twine upload dist/*
   ```

10. Summarize the release: version, key changes, download link.
