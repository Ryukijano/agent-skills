# agent-skills

Reusable agent skills and slash-command workflows for **Cursor**, **Windsurf/Cascade**, and **Devin** — cross-project ML research (AIRE HPC, PyTorch, surgical MOT, Cosmos3/ESD).

Canonical repo: https://github.com/Ryukijano/agent-skills

## Structure

```
.cursor/
├── skills/              # 11 Cursor agent skills (SKILL.md)
└── commands/            # 24 Cursor slash commands (full playbooks)

.windsurf/
├── skills/              # Same 11 skills (Windsurf/Cascade)
└── workflows/           # 10 detailed workflow playbooks

workflows/
├── README.md
├── CURSOR_AGENT_INDEX.md
├── CURSOR_COMMANDS.md   # Full command catalog
└── devin/               # Devin macros (MOT + cosmos/)
```

## Cursor commands (24)

See **[workflows/CURSOR_COMMANDS.md](workflows/CURSOR_COMMANDS.md)** for the full list.

| Group | Examples |
|-------|----------|
| ML / HPC | `/submit-gpu-job`, `/debug-training`, `/pretrain-and-evaluate` |
| Surgical MOT | `/mot-browser-research`, `/mot-train-eval`, `/mot-hota-eval` |
| Cosmos / ESD | `/cosmos-verify`, `/esd-t2v`, `/esd-forward-dynamics` |
| Ship & review | `/ship-pr`, `/review-bugbot`, `/fix-ci`, `/iterative-test-loop` |

Commands in `.cursor/commands/` are **self-contained** (full steps inlined, not pointers to other files).

## Skills (11)

| Skill | Description |
|-------|-------------|
| `aire-slurm-submit` | AIRE Slurm (L40S) |
| `conda-env-setup` | Conda + CUDA on AIRE |
| `debug-pytorch-gpu` | GPU OOM, DDP, NCCL |
| `git-branch-workflow` | Branches, commits, PRs |
| `lora-finetune` | DINOv2 / ViT LoRA |
| `surgical-mot-eval` | CholecTrack20 eval |
| `tdv-pretrain` | TDV pretraining |
| `wandb-experiment` | W&B on HPC |
| `mot-browser-research` | @Browser MOT research |
| `mot-training-workflow` | Four-stage MOT pipeline |
| `mot-repo-orientation` | Gyanateet_tracking map |

## Usage

### Cursor

```bash
git clone https://github.com/Ryukijano/agent-skills.git
cp -r agent-skills/.cursor/skills/* your-project/.cursor/skills/
cp -r agent-skills/.cursor/commands/* your-project/.cursor/commands/
```

Type `/` in chat — e.g. `/mot-hota-eval`, `/ship-pr`, `/esd-t2v`.

### Windsurf

```bash
cp -r agent-skills/.windsurf your-project/
```

### Devin

Upload `workflows/devin/*.devin.md` and `workflows/devin/cosmos/*.devin.md`.

## Source of truth

Edit **agent-skills** first, then copy into consumer repos ([Gyanateet_tracking](https://github.com/Ryukijano/Gyanateet_tracking), [AIMSgeneral](https://github.com/Ryukijano/AIMSgeneral)).

## License

MIT
