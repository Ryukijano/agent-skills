# agent-skills

Reusable agent skills and slash-command workflows for **Cursor**, **Windsurf/Cascade**, and **Devin** — cross-project ML research (AIRE HPC, PyTorch, surgical MOT).

Canonical repo: https://github.com/Ryukijano/agent-skills

## Structure

```
.cursor/
├── skills/              # Cursor agent skills (SKILL.md + YAML frontmatter)
└── commands/            # Cursor slash commands (type / in chat)

.windsurf/
├── skills/              # Windsurf/Cascade skills (same SKILL.md files)
└── workflows/           # Full workflow playbooks (detailed steps)

workflows/
├── README.md            # Index of all workflows
├── CURSOR_AGENT_INDEX.md
└── devin/               # Devin playbook macros (!name)
```

## Skills (11)

| Skill | Description |
|-------|-------------|
| `aire-slurm-submit` | Submit and monitor Slurm jobs on Leeds AIRE (L40S) |
| `conda-env-setup` | Conda environments with CUDA on AIRE |
| `debug-pytorch-gpu` | OOM, DDP, NCCL, NaN diagnostics |
| `git-branch-workflow` | Branch naming, commits, PR templates |
| `lora-finetune` | LoRA for DINOv2 / ViT |
| `surgical-mot-eval` | CholecTrack20 MOT evaluation |
| `tdv-pretrain` | Temporal Difference in Vision pretraining |
| `wandb-experiment` | Weights & Biases on HPC |
| `mot-browser-research` | @Browser SOTA research for GOT-JEPA MOT |
| `mot-training-workflow` | Four-stage MOT train/resume/eval |
| `mot-repo-orientation` | Gyanateet_tracking repo map |

MOT skills target [Gyanateet_tracking](https://github.com/Ryukijano/Gyanateet_tracking) but copy into any surgical MOT project.

## Workflows / slash commands

### Cross-project

| Command | Description |
|---------|-------------|
| `/submit-gpu-job` | Submit GPU job to AIRE Slurm |
| `/pretrain-and-evaluate` | TDV pretrain → detection → eval |
| `/debug-training` | Debug loss=NaN, OOM, DDP hangs |
| `/code-review` | ML code review checklist |
| `/address-pr-comments` | Systematic PR comment triage |
| `/checkpoint-to-deployment` | Strip checkpoint for inference |
| `/setup-ml-project` | Scaffold new ML project |

### Surgical MOT (Gyanateet_tracking)

| Command | Devin macro | Description |
|---------|-------------|-------------|
| `/mot-browser-research` | `!mot-browser-research` | Online research + strategic verdict |
| `/mot-train-eval` | `!mot-train-eval` | Stages 1–4 training |
| `/mot-hota-eval` | `!mot-hota-eval` | HOTA + smoke-stratified eval |

## Usage

### Cursor

```bash
git clone https://github.com/Ryukijano/agent-skills.git
cp -r agent-skills/.cursor/skills/* your-project/.cursor/skills/
cp -r agent-skills/.cursor/commands/* your-project/.cursor/commands/
```

Or symlink: `ln -s ../agent-skills/.cursor/skills ./.cursor/skills-shared`

Skills auto-discover from `.cursor/skills/`. Invoke workflows with `/command-name` in chat.

### Windsurf / Cascade

```bash
cp -r agent-skills/.windsurf your-project/
```

Skills auto-invoke; workflows via `/workflow-name` (see `.windsurf/workflows/`).

### Devin

Upload playbooks from `workflows/devin/*.devin.md` or attach as macros (`!mot-browser-research`, etc.).

## Syncing into a project

From Gyanateet_tracking (example consumer):

```bash
cd Gyanateet_tracking
git pull   # project may vendor a snapshot; prefer pulling from agent-skills for updates
cp -r ../agent-skills/.cursor/skills/{aire-slurm-submit,conda-env-setup,...} .cursor/skills/
```

Keep **agent-skills** as the source of truth; copy into project repos — not the reverse.

## License

MIT
