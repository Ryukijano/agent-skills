# Dependency Audit & Pin

1. Audit current imports and usage; remove unused.
2. Decide policy (research vs release) and update `pyproject.toml` or requirements.
3. Generate lock or env export.
4. Test install in a fresh env or container (smoke import + 2-step train).
5. For cluster: ensure install path is under scratch quota-friendly location.
6. Commit lock + a note of resolved key versions.
7. Update CI to use the lock for reproducible builds.

Apply `dependency-management`, `reproducibility`.
