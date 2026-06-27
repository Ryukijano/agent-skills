---
description: Prepare code, data, and documentation for paper submission deadline
---

## Paper Submission Prep

1. Freeze the codebase: create a submission branch and tag:
   ```bash
   git checkout -b paper-submission-v1
   git tag v1.0-paper
   ```

2. Run the reproducibility audit workflow (`/reproducibility-checklist`).
   Fix all critical gaps before submission.

3. Generate final results tables:
   ```bash
   python scripts/generate_results_table.py --outputs outputs/ --format latex
   ```
   Ensure tables match the paper exactly.

4. Create a `configs/paper/` directory with exact configs used:
   ```bash
   mkdir -p configs/paper
   cp configs/default.yaml configs/paper/main_experiment.yaml
   # Add any ablation configs
   ```

5. Write a `REPRODUCE.md` with step-by-step instructions:
   ```markdown
   ## Reproducing Main Results

   1. Environment setup:
      conda env create -f environment.yml

   2. Download data:
      [instructions]

   3. Train:
      python train.py --config configs/paper/main_experiment.yaml

   4. Evaluate:
      python eval.py --config configs/paper/main_experiment.yaml --checkpoint outputs/main/best.pth

   Expected: mAP@50 = 0.35 ± 0.02 (3 seeds)
   ```

6. Upload pretrained models:
   - Upload to HuggingFace, Zenodo, or Google Drive
   - Add download links to README.md

7. Clean the repository:
   ```bash
   # Remove debug code
   grep -rn "breakpoint()\|import pdb\|print('DEBUG" --include="*.py"
   # Remove large files from git history (if needed)
   # Ensure .gitignore is correct
   ```

8. Create a release on GitHub:
   ```bash
   gh release create v1.0-paper --title "Paper v1.0" --notes "Code for <paper title>"
   ```

9. Prepare citation file:
   ```bibtex
   @inproceedings{author2026,
     title={...},
     author={...},
     booktitle={...},
     year={2026}
   }
   ```
   Add to README.md and create `CITATION.bib`.

10. Final checklist:
    - [ ] Code runs with single command
    - [ ] Environment fully specified
    - [ ] Pretrained weights downloadable
    - [ ] Results reproducible with documented seeds
    - [ ] README has citation
    - [ ] LICENSE file present
    - [ ] No hardcoded paths or secrets
    - [ ] Repo is public (or will be upon acceptance)
