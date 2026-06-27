---
name: setup-ml-project
description: Scaffold a new ML research project with standard directory structure, configs, and tooling. Use when starting a new project, initializing repo structure, or standardizing an existing project layout.
---

## ML Project Setup

### Directory structure
```
<project>/
├── core_app/
│   ├── models/
│   ├── data/
│   └── eval/
├── configs/
├── scripts/
├── jobs/
├── logs/
├── outputs/
├── tests/
├── .devin/
├── requirements.txt
├── .gitignore
└── README.md
```

### Essential files
- `requirements.txt` with pinned deps
- `.gitignore` covering data/, outputs/, wandb/, __pycache__/
- `configs/default.yaml` template
- `jobs/train.slurm` AIRE template
- `tests/test_smoke.py` import test
- `README.md` with setup + usage
