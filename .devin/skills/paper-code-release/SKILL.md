---
name: paper-code-release
description: Prepare research code for public release alongside a paper submission. Use when cleaning up a codebase for open-sourcing, writing READMEs for papers, creating reproducibility instructions, or packaging code for conference submission.
---

## Paper Code Release Preparation

### Release checklist

- [ ] **LICENSE** file added (MIT or Apache-2.0 recommended)
- [ ] **README.md** with: project description, installation, quick start, results table, citation
- [ ] **requirements.txt** or **environment.yml** with pinned versions
- [ ] **pyproject.toml** or **setup.py** for installable package
- [ ] All hardcoded paths replaced with config arguments or environment variables
- [ ] No API keys, credentials, or personal data in code
- [ ] No large binary files in git (use Git LFS or download links)
- [ ] **.gitignore** covers data/, outputs/, wandb/, __pycache__/
- [ ] Seeds set explicitly in training scripts
- [ ] Single-command reproduction: `python train.py --config configs/paper.yaml`
- [ ] Pre-trained model weights downloadable (Google Drive, HuggingFace, Zenodo)
- [ ] **CITATION.bib** or citation block in README
- [ ] **AGENTS.md** for LLM-friendly context (design choices, not style)

### README template for paper code

```markdown
# <Paper Title> — <Short Name>

Official code for: **"<Paper Title>"** (<Conference> <Year>).

## Results

| Method | Dataset | Metric 1 | Metric 2 |
|--------|---------|----------|----------|
| Baseline | Cholec80 | 0.12 | 35 |
| Ours | Cholec80 | **0.35** | **61** |

## Installation

```bash
conda env create -f environment.yml
conda activate <env_name>
```

## Quick Start

### Training
```bash
python train.py --config configs/default.yaml
```

### Evaluation
```bash
python eval.py --config configs/default.yaml --checkpoint <path>
```

### Pretrained Models

Download pretrained weights:
- [Model Name](https://...) (trained on <dataset>)

## Citation

```bibtex
@inproceedings{...}
```

## License

MIT
```

### Cleaning code for release

```bash
# Remove debug prints
grep -rn "print(" --include="*.py" | grep -v "logger\|tqdm\|wandb"

# Remove hardcoded paths
grep -rn "/scratch/\|/home/\|C:\\" --include="*.py"

# Remove notebook outputs
jupyter nbconvert --clear-output --inplace notebooks/*.ipynb

# Check for secrets
grep -rn "api_key\|password\|secret\|token" --include="*.py" | grep -v "# "
```

### Reproducibility statement for paper

Include in README or supplementary:
```
## Reproducibility

All experiments use seed 42. Training was performed on NVIDIA L40S GPUs.
Environment details are in `environment.yml`. To reproduce main results:

1. `conda env create -f environment.yml && conda activate <env>`
2. `python train.py --config configs/paper_main.yaml`
3. `python eval.py --config configs/paper_main.yaml --checkpoint outputs/main/best.pth`

Expected: mAP@50 = 0.35 ± 0.02 (variance across 3 seeds)
```
