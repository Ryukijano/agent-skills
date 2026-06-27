# Agent skills index

Canonical source: this repo ([Ryukijano/agent-skills](https://github.com/Ryukijano/agent-skills)).

Copy `.cursor/` and `.devin/` into consumer projects (e.g. [Gyanateet_tracking](https://github.com/Ryukijano/Gyanateet_tracking)).

## All skills (`.cursor/skills/`)

| Skill | Trigger |
|-------|---------|
| `mot-browser-research` | @Browser, SOTA, strategic direction |
| `mot-training-workflow` | Train/resume MOT stages 1–4 |
| `mot-repo-orientation` | Repo map and pipeline |
| `aire-slurm-submit` | AIRE Slurm submit/monitor |
| `conda-env-setup` | Conda + CUDA on AIRE |
| `debug-pytorch-gpu` | GPU OOM, DDP, NCCL |
| `git-branch-workflow` | Branches, commits, PRs |
| `lora-finetune` | DINOv2/ViT LoRA |
| `surgical-mot-eval` | CholecTrack20 HOTA/mAP |
| `tdv-pretrain` | TDV surgical video SSL |
| `wandb-experiment` | W&B on HPC |

## Slash commands (`.cursor/commands/` — 24 total)

See `workflows/CURSOR_COMMANDS.md` for the full catalog.

**MOT:** `/mot-browser-research`, `/mot-train-eval`, `/mot-hota-eval`

**ML/HPC:** `/submit-gpu-job`, `/pretrain-and-evaluate`, `/debug-training`, `/setup-ml-project`, `/checkpoint-to-deployment`

**Cosmos/ESD:** `/cosmos-verify`, `/cosmos-spark-kernels`, `/esd-t2v`, `/esd-forward-dynamics`, `/lap-t2v`

**Ship/review:** `/ship-pr`, `/babysit-pr`, `/split-to-prs`, `/fix-ci`, `/code-review`, `/address-pr-comments`, `/iterative-test-loop`, `/impact-aware-testing`, `/review-bugbot`, `/review-security`, `/explore-sota`

## Devin playbooks (`workflows/devin/`)

- `mot-browser-research.devin.md` → `!mot-browser-research`
- `mot-train-eval.devin.md` → `!mot-train-eval`
- `mot-hota-eval.devin.md` → `!mot-hota-eval`

## Consumer project quick paths (Gyanateet_tracking)

- Train: `bash scripts/train_stage1_ddp_3gpu.sh` (Spark) or `sbatch jobs/*.slurm` (AIRE)
- Eval: `python scripts/eval_checkpoint.py --mot-eval --stratify-smoke`
- Tests: `pytest tests/test_mot_smoke.py -q`
