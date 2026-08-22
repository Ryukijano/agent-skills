# Repro Bundle Run

1. Scope the bundle: which claims/results must reproduce.
2. Assemble: code at exact commit, configs+seeds, run scripts (00_setup → 01_download_data → 02_run_experiment).
3. Environment manifest: lockfile or pip/conda export + hardware notes.
4. Data manifest: sources, hashes, splits; no private data.
5. Verify runs in a CLEAN environment; compare outputs to expected/metrics.json within documented tolerance.
6. Log verification in repro/VERIFICATION.log; fix gaps and re-verify until green.

Apply `repro-bundle`, `reproducibility-checklist`.
