# Reproducibility Audit

Step-by-step checklist to make (or audit) an experiment for reproducibility.

1. Record current commit: `git rev-parse HEAD >> experiment.log`.
2. Capture full config (yaml + overrides) and log to WandB.
3. Set and log all seeds (Python/numpy/torch).
4. Export environment: `conda env export --no-builds > env-<date>.yml`.
5. Hash data manifests / splits used.
6. For any reported table number, ensure at least 3 seeds or note single-run.
7. Write `REPRO.md` or section in run notes listing the above.
8. Run smoke + targeted eval; attach outputs.
9. If gaps found, either fix or explicitly document why not fixable.
10. Update project `REPRODUCIBILITY.md` with status.

Apply skills: `reproducibility`, `data-management`, `experiment-tracking`.

Verification gate applies before claiming a result is reproducible.
