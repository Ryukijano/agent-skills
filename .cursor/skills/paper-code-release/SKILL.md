---
name: paper-code-release
description: Preparing a research codebase for public release alongside a paper or tech report. Covers licensing, citation, repro instructions, artifact packaging, and hygiene.
---

## Paper Code Release

### Required artifacts
- Clean README with one-command setup + "reproduce main table" section + expected numbers.
- LICENSE (MIT or Apache-2 preferred for research).
- CITATION.bib + citation snippet in README.
- All configs and split manifests for main results.
- Environment lock or clear major-version pins + CUDA notes.
- Downloadable weights (or clear instructions + HF link) for the main model.
- `REPRODUCIBILITY.md` or equivalent audit.

### Hygiene before release
- Remove secrets, local paths, TODOs that reveal unfinished work.
- Strip large binary checkpoints from git (use release assets or HF).
- Run full `code-quality` + `testing-strategy` pass.
- Tag the release commit.

### Optional but recommended
- Docker / conda-pack for exact env.
- Minimal demo notebook or script that produces one key figure/table.
- Model card.

Related: `reproducibility`, `paper-submission-prep`, `code-quality`, `release-checklist`.
