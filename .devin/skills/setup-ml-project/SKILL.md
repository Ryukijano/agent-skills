# ML Project Setup

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