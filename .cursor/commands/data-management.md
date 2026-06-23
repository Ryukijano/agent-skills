# Data Management Workflow

1. Inventory raw sources and note licenses/access.
2. Create or update `splits/*.yaml` (or equivalent) with explicit video IDs per split.
3. Compute and commit SHA of split files.
4. Write `data/README.md` with source, preprocessing, and leak policy.
5. For any new pretraining corpus, cross-check against CT20 test/val exclusion list.
6. When starting a run, log the manifest SHAs + git commit of the splits code.
7. After major data change: re-run a small eval to confirm no silent breakage.
8. For release: include split files + SHA + a one-paragraph data card.

Apply `data-management`, `reproducibility`, `surgical-mot-eval`.
