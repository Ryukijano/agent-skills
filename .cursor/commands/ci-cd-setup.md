# Add / Update CI

1. Create `.github/workflows/ci.yml` with lint + smoke jobs (CPU).
2. Add separate job for type check if desired.
3. Ensure it runs on push and PR.
4. Add a badge to README.
5. Verify the workflow passes on next push.
6. (Later) Add a release workflow that builds + (optionally) uploads to PyPI or HF when a tag is pushed.
7. Document in README how CI is wired.

Apply `ci-cd-setup`, `code-quality`, `testing-strategy`.
