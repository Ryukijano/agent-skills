# Reproducibility Checklist (Run)

1. Read the current `REPRODUCIBILITY.md` or create one.
2. For each main result/figure:
   - Locate the exact commit + config + command.
   - Re-run smoke (2–5 steps) + full small-scale if feasible.
   - Verify numbers are within tolerance or document drift.
3. Check data splits for leakage against pretrain corpus.
4. Verify environment export or lock file exists for the run.
5. Ensure README or docs have single-command repro instructions.
6. Add any missing items to the checklist file.
7. Generate a short `repro-audit-<date>.md` summarizing gaps and fixes.
8. Commit the audit + fixes.

Apply `reproducibility`, `data-management`, `paper-submission-prep`.
