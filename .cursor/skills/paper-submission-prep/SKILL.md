---
name: paper-submission-prep
description: Final checklist and tasks to get a research repo submission-ready for a conference or journal (code + data + repro + presentation artifacts).
---

## Paper Submission Prep

### Code & repo
- All main results reproducible from committed configs + committed splits.
- No secrets or absolute paths.
- LICENSE and citation present.
- README has "Quick start", "Reproduce main result", hardware notes.
- Large weights are downloadable (not in git).

### Data & splits
- Leak-free policy documented and enforced for reported numbers.
- Splits committed or clearly referenced with hashes.

### Reproducibility bundle (recommended)
- Code at the exact commit.
- Configs + seeds.
- Env lock or export.
- Data manifest.
- Weights (or instructions).
- `REPRODUCIBILITY.md`.

### Non-code artifacts
- Slides / poster / appendix figures generated from committed code or clearly versioned notebooks.
- Any human-labeled analysis tables sourced.

Related: `reproducibility`, `paper-code-release`, `ablation-study`.
