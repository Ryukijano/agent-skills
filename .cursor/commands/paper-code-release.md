# Paper Code Release Steps

1. Audit with `reproducibility-checklist` and `paper-submission-prep`.
2. Clean repo: delete debug code, local paths, large unneeded checkpoints from git history if possible.
3. Add / update LICENSE, CITATION.bib, README repro section.
4. Create a `release/` or tag the commit used for the paper numbers.
5. Build any lock files or env exports.
6. Upload weights to stable location (HF, institutional storage) with SHA.
7. Test the "new user" flow on a fresh machine or container (one-command smoke + main result).
8. Create GitHub release with notes pointing to the paper + citation.
9. Add "If you use this code, please cite..." to README.
10. Announce internally; update any lab index.

Apply `paper-code-release`, `reproducibility`, `code-quality`.
