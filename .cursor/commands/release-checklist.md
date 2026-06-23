# Release Run

1. Ensure main is green (CI + manual smoke on clean checkout).
2. Update CHANGELOG.
3. Bump version.
4. Commit "chore: release vX.Y.Z".
5. Tag and push tag.
6. Build sdist + wheel.
7. Upload (PyPI or target).
8. Create GitHub release.
9. Test fresh install + one key command.
10. Communicate the release.

Apply `release-checklist`, `code-quality`.
