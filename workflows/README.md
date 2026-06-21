# Agent skills workflows

Canonical index for [Ryukijano/agent-skills](https://github.com/Ryukijano/agent-skills). Copy into consumer projects — do not edit only in the project copy.

## MOT workflows (Gyanateet_tracking)

| Workflow | Devin playbook | Cursor command | Skill |
|----------|----------------|----------------|-------|
| Browser research + SOTA | `devin/mot-browser-research.devin.md` | `/mot-browser-research` | `mot-browser-research` |
| Stage train / resume | `devin/mot-train-eval.devin.md` | `/mot-train-eval` | `mot-training-workflow` |
| HOTA + smoke eval | `devin/mot-hota-eval.devin.md` | `/mot-hota-eval` | `surgical-mot-eval` |
| Repo orientation | — | — | `mot-repo-orientation` |

## Cross-project workflows

| Workflow | Windsurf | Cursor command | Skill |
|----------|----------|----------------|-------|
| AIRE GPU job | `.windsurf/workflows/submit-gpu-job.md` | `/submit-gpu-job` | `aire-slurm-submit` |
| TDV pretrain + eval | `pretrain-and-evaluate.md` | `/pretrain-and-evaluate` | `tdv-pretrain` |
| Debug training | `debug-training.md` | `/debug-training` | `debug-pytorch-gpu` |
| Code review | `code-review.md` | `/code-review` | — |
| PR comments | `address-pr-comments.md` | `/address-pr-comments` | `git-branch-workflow` |
| Checkpoint deploy | `checkpoint-to-deployment.md` | `/checkpoint-to-deployment` | — |
| New ML project | `setup-ml-project.md` | `/setup-ml-project` | — |

## Install into a project

```bash
git clone https://github.com/Ryukijano/agent-skills.git
cp -r agent-skills/.cursor/skills/* your-project/.cursor/skills/
cp -r agent-skills/.cursor/commands/* your-project/.cursor/commands/
cp -r agent-skills/.windsurf your-project/   # optional Windsurf mirror
```

See `workflows/CURSOR_AGENT_INDEX.md` for the full skill list.
