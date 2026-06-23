# Paper Submission Prep Run

1. Run `/reproducibility-checklist` and fix gaps.
2. Run `/paper-code-release` hygiene steps (but don't publish yet).
3. Verify one-command repro of the main table/figure on a clean checkout + fresh env (smoke at minimum).
4. Check that all figures/tables in the paper have a corresponding committed config + result json or WandB link.
5. Ensure LICENSE + CITATION.bib + README citation are present.
6. Confirm no private data or patient-identifiable material is shipped.
7. Create a `submission/` folder with: code snapshot tarball (or git tag), weights SHA, repro instructions.
8. Add a `SUBMISSION.md` with "to reproduce, run: ..." and expected outputs.
9. Tag the repo `v1.0-<conf>-submission` or similar.
10. Final human review per research-integrity rule before upload.

Apply `paper-submission-prep`, `reproducibility`, `paper-code-release`.
