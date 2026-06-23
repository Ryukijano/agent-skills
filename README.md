# agent-skills

Reusable Windsurf skills and workflows for cross-project AI-assisted development.
Designed for research scientists and software engineers working on ML projects.

## Overview

- **30 skills** (auto-invoked by Cascade based on task relevance)
- **26 workflows** (manually invoked via `/workflow-name` slash commands)
- Every skill has a corresponding workflow and vice versa

Skills use **progressive disclosure**: only `name` and `description` are loaded
until Cascade decides to invoke them, keeping context lean.

## Skills (30)

### Research Scientist (12)

| Skill | Description |
|-------|-------------|
| `reproducibility` | Seeds, config logging, environment capture, deterministic training |
| `reproducibility-checklist` | Audit project for reproducibility gaps before submission |
| `experiment-tracking` | Structured logging, hyperparameter management, result comparison |
| `data-management` | Dataset versioning, hashing, leak-free partitioning |
| `paper-code-release` | Prepare code for public release alongside paper |
| `paper-submission-prep` | Finalize repo for conference submission deadline |
| `ablation-study` | Design systematic ablation studies comparing model variants |
| `tdv-pretrain` | TDV (Temporal Difference in Vision) pretraining on surgical video |
| `surgical-mot-eval` | Evaluate surgical MOT models on CholecTrack20 |
| `lora-finetune` | LoRA fine-tuning for vision transformers (DINOv2, ViT) |
| `pretrain-and-evaluate` | Full Stage 0 pretrain → Stage 1 detect → eval pipeline |
| `continual-learning` | Cross-session context persistence with progress files |

### Software Engineering (10)

| Skill | Description |
|-------|-------------|
| `code-quality` | Formatting, linting, type checking with ruff + basedpyright |
| `code-review` | ML-focused code review checklist (correctness, perf, safety) |
| `testing-strategy` | Unit, integration, smoke, and property-based tests for ML code |
| `dependency-management` | Lock files, pyproject.toml, version conflicts, uv migration |
| `ci-cd-setup` | GitHub Actions workflows for automated testing and linting |
| `pre-commit-setup` | Pre-commit hooks with ruff and common checks |
| `release-checklist` | Versioned releases, changelogs, PyPI publishing |
| `refactor-extract-module` | Safely extract code into separate modules |
| `git-branch-workflow` | Branch naming, commit conventions, PR templates |
| `address-pr-comments` | Systematically address PR review comments via GitHub CLI |

### Infrastructure & Debugging (8)

| Skill | Description |
|-------|-------------|
| `aire-slurm-submit` | Submit and monitor Slurm jobs on AIRE HPC cluster |
| `submit-gpu-job` | Submit GPU training job with smoke test + monitoring |
| `conda-env-setup` | Create conda environments with CUDA PyTorch on AIRE |
| `debug-pytorch-gpu` | Diagnose OOM, DDP hangs, NCCL errors, gradient instability |
| `debug-training` | Debug NaN loss, OOM, DDP hangs, poor convergence by symptom |
| `checkpoint-to-deployment` | Convert training checkpoint to deployment-ready format |
| `setup-ml-project` | Scaffold new ML research project with standard structure |
| `wandb-experiment` | Weights & Biases experiment tracking setup and debugging |

## Workflows (26)

### Research Workflows (13)

| Workflow | Description |
|----------|-------------|
| `/reproducibility` | Set up seeds, config logging, environment capture |
| `/reproducibility-checklist` | Audit project for reproducibility gaps |
| `/experiment-tracking` | Set up structured experiment tracking |
| `/data-management` | Set up dataset versioning and leak-free splits |
| `/paper-code-release` | Prepare code for public release |
| `/paper-submission-prep` | Finalize repo for paper submission |
| `/ablation-study` | Design and run systematic ablation study |
| `/tdv-pretrain` | Run TDV pretraining on surgical video |
| `/surgical-mot-eval` | Evaluate MOT models on CholecTrack20 |
| `/lora-finetune` | Configure and run LoRA fine-tuning |
| `/pretrain-and-evaluate` | Full pretrain → detect → eval pipeline |
| `/continual-learning` | Session start/end handoff protocol |
| `/wandb-experiment` | Set up WandB tracking |

### SWE Workflows (8)

| Workflow | Description |
|----------|-------------|
| `/code-quality` | Set up formatting, linting, type checking |
| `/code-review` | Systematic ML code review |
| `/testing-strategy` | Design and implement test suite |
| `/dependency-management` | Manage Python dependencies and lock files |
| `/ci-cd-setup` | Set up GitHub Actions CI/CD |
| `/pre-commit-setup` | Install pre-commit hooks with ruff |
| `/release-checklist` | Create a versioned release |
| `/refactor-extract-module` | Extract code into separate module |

### Infrastructure Workflows (5)

| Workflow | Description |
|----------|-------------|
| `/aire-slurm-submit` | Submit and monitor Slurm jobs on AIRE |
| `/submit-gpu-job` | Submit GPU job with smoke test verification |
| `/conda-env-setup` | Create conda environment with CUDA |
| `/debug-pytorch-gpu` | Diagnose PyTorch GPU issues |
| `/debug-training` | Debug training failures by symptom |

## Usage

### In Windsurf
1. Copy the `.windsurf/` directory into your project root (or symlink it).
2. Skills are automatically discovered and invoked by Cascade based on task relevance.
3. Workflows are invoked via `/workflow-name` slash commands.

### In Cursor
The `SKILL.md` files are compatible with Cursor's agent rules system.
Copy individual skill folders into `.cursor/rules/` or your project's rules directory.

### Skill vs Workflow: When to use which

- **Skills** are auto-invoked by Cascade when it detects a relevant task. Use for
  knowledge that should be available on-demand (e.g., debugging guides, hyperparameter tables).
- **Workflows** are manually triggered via `/name` when you want to follow a specific
  step-by-step procedure (e.g., `/pretrain-and-evaluate`, `/code-review`).
- This repo provides both for every topic — use the skill for reference, the workflow for execution.

## Structure

```
.windsurf/
├── skills/                    # 30 SKILL.md files (auto-invoked)
│   ├── ablation-study/
│   ├── address-pr-comments/
│   ├── aire-slurm-submit/
│   ├── checkpoint-to-deployment/
│   ├── ci-cd-setup/
│   ├── code-quality/
│   ├── code-review/
│   ├── conda-env-setup/
│   ├── continual-learning/
│   ├── data-management/
│   ├── debug-pytorch-gpu/
│   ├── debug-training/
│   ├── dependency-management/
│   ├── experiment-tracking/
│   ├── git-branch-workflow/
│   ├── lora-finetune/
│   ├── paper-code-release/
│   ├── paper-submission-prep/
│   ├── pre-commit-setup/
│   ├── pretrain-and-evaluate/
│   ├── refactor-extract-module/
│   ├── release-checklist/
│   ├── reproducibility/
│   ├── reproducibility-checklist/
│   ├── setup-ml-project/
│   ├── submit-gpu-job/
│   ├── surgical-mot-eval/
│   ├── tdv-pretrain/
│   ├── testing-strategy/
│   └── wandb-experiment/
└── workflows/                 # 26 workflow .md files (slash commands)
    ├── ablation-study.md
    ├── address-pr-comments.md
    ├── aire-slurm-submit.md
    ├── checkpoint-to-deployment.md
    ├── ci-cd-setup.md
    ├── code-quality.md
    ├── code-review.md
    ├── conda-env-setup.md
    ├── continual-learning.md
    ├── data-management.md
    ├── debug-pytorch-gpu.md
    ├── debug-training.md
    ├── dependency-management.md
    ├── experiment-tracking.md
    ├── git-branch-workflow.md
    ├── lora-finetune.md
    ├── paper-code-release.md
    ├── paper-submission-prep.md
    ├── pre-commit-setup.md
    ├── pretrain-and-evaluate.md
    ├── refactor-extract-module.md
    ├── release-checklist.md
    ├── reproducibility-checklist.md
    ├── reproducibility.md
    ├── setup-ml-project.md
    ├── submit-gpu-job.md
    ├── surgical-mot-eval.md
    ├── tdv-pretrain.md
    ├── testing-strategy.md
    └── wandb-experiment.md
```

## License

MIT
