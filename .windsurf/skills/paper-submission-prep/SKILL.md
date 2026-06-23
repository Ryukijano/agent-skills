---
name: paper-submission-prep
description: Prepare code, data, and documentation for paper submission deadline. Use when finalizing a repo for conference submission, creating reproducibility instructions, or tagging a release.
---

## Paper Submission Prep

### Checklist

1. Freeze codebase: create `paper-submission-v1` branch, tag `v1.0-paper`
2. Run `/reproducibility-checklist` workflow
3. Generate final results tables matching paper exactly
4. Create `configs/paper/` with exact configs
5. Write `REPRODUCE.md` with step-by-step instructions
6. Upload pretrained models (HuggingFace/Zenodo/Google Drive)
7. Clean repo: remove debug code, hardcoded paths, secrets
8. Create GitHub release: `gh release create v1.0-paper`
9. Add citation (BibTeX) to README and `CITATION.bib`
10. Final: single-command repro, env specified, weights downloadable, LICENSE present
