# agent-skills

Reusable Windsurf rules, skills, and workflows for cross-project AI-assisted development.

## Structure

```
.windsurf/
├── skills/          # SKILL.md files with YAML frontmatter (auto-invoked by Cascade)
│   ├── aire-slurm-submit/
│   ├── conda-env-setup/
│   ├── debug-pytorch-gpu/
│   ├── git-branch-workflow/
│   ├── lora-finetune/
│   ├── surgical-mot-eval/
│   ├── tdv-pretrain/
│   └── wandb-experiment/
└── workflows/       # Slash-command workflows (manually invoked via /name)
    ├── address-pr-comments.md
    ├── checkpoint-to-deployment.md
    ├── code-review.md
    ├── debug-training.md
    ├── pretrain-and-evaluate.md
    ├── setup-ml-project.md
    └── submit-gpu-job.md
```

## Skills

Skills use progressive disclosure — only `name` and `description` are loaded
until Cascade decides to invoke them. Place supporting files alongside
`SKILL.md` in the skill folder.

| Skill | Description |
|-------|-------------|
| `aire-slurm-submit` | Submit and monitor Slurm jobs on the University of Leeds AIRE HPC cluster |
| `conda-env-setup` | Create and manage conda environments on AIRE with CUDA support |
| `debug-pytorch-gpu` | Diagnose PyTorch GPU issues (OOM, DDP, NCCL, CUDA mismatches) |
| `git-branch-workflow` | Standardized git branching, commit conventions, and PR creation |
| `lora-finetune` | LoRA fine-tuning for vision transformers (DINOv2, ViT) |
| `surgical-mot-eval` | Evaluate surgical multi-object tracking models on CholecTrack20 |
| `tdv-pretrain` | Run TDV (Temporal Difference in Vision) pretraining on surgical video |
| `wandb-experiment` | Set up Weights & Biases experiment tracking for ML projects |

## Workflows

Workflows are manually invoked via `/workflow-name` in Cascade.

| Workflow | Description |
|----------|-------------|
| `/submit-gpu-job` | Submit a GPU training job to AIRE Slurm |
| `/pretrain-and-evaluate` | Full pretrain + downstream evaluation pipeline |
| `/address-pr-comments` | Address pull request review comments |
| `/code-review` | Systematic code review checklist |
| `/setup-ml-project` | Scaffold a new ML research project |
| `/debug-training` | Debug training failures (loss=NaN, OOM, DDP hangs) |
| `/checkpoint-to-deployment` | Convert a training checkpoint to deployment |

## Usage

### In Windsurf
1. Copy the `.windsurf/` directory into your project root (or symlink it).
2. Skills are automatically discovered and invoked by Cascade.
3. Workflows are invoked via `/workflow-name` slash commands.

### In Cursor
The `SKILL.md` files are compatible with Cursor's agent rules system.
Copy individual skill folders into `.cursor/rules/` or your project's rules directory.

## License

MIT
