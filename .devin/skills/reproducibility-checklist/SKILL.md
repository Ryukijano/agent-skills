---
name: reproducibility-checklist
description: Audit a project for reproducibility gaps and fix them before paper submission or code release. Use when checking if experiments are reproducible, verifying seeds/configs/environments are logged, or preparing for submission.
---

## Reproducibility Audit

- [ ] LICENSE file present
- [ ] README with install + usage instructions
- [ ] Dependencies specified (requirements.txt / environment.yml / pyproject.toml)
- [ ] All seeds set (Python, NumPy, PyTorch, CUDA)
- [ ] Config saved as YAML in output dir per experiment
- [ ] Git commit hash logged per experiment
- [ ] No hardcoded paths
- [ ] Single-command reproduction: `python train.py --config <path>`
- [ ] Dataset version or hash recorded
- [ ] `.gitignore` covers data/, outputs/, wandb/
- [ ] Pre-trained weights downloadable
- [ ] `cudnn.deterministic=True` if bit-exact repro needed
