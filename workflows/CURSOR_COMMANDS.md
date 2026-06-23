# Cursor commands index

All slash commands live in `.cursor/commands/`. Type `/` in Cursor chat to invoke.

## ML / HPC

| Command | Description |
|---------|-------------|
| `/submit-gpu-job` | Submit GPU job to AIRE Slurm |
| `/pretrain-and-evaluate` | TDV pretrain → detection → eval |
| `/debug-training` | Debug loss=NaN, OOM, DDP hangs |
| `/setup-ml-project` | Scaffold new ML project |
| `/checkpoint-to-deployment` | Strip checkpoint for inference |

## Surgical MOT

| Command | Description |
|---------|-------------|
| `/mot-browser-research` | @Browser SOTA + strategic verdict |
| `/mot-train-eval` | GOT-JEPA stages 1–4 training |
| `/mot-hota-eval` | HOTA + smoke-stratified eval |

## Cosmos / ESD (AIMSgeneral)

| Command | Description |
|---------|-------------|
| `/cosmos-verify` | Verify Cosmos3 stack on DGX Spark |
| `/cosmos-spark-kernels` | Build NATTEN / flash-attn kernels |
| `/esd-t2v` | ESD synthetic video (Cosmos3 T2V) |
| `/esd-forward-dynamics` | ESD forward dynamics (needs NATTEN) |
| `/lap-t2v` | Laparoscopy T2V rich v2 |

## Code quality & shipping

| Command | Description |
|---------|-------------|
| `/code-review` | ML code review checklist |
| `/address-pr-comments` | Systematic PR comment triage |
| `/ship-pr` | Verify, commit, push, PR, watch CI |
| `/babysit-pr` | Keep PR merge-ready loop |
| `/split-to-prs` | Split work into small PRs |
| `/fix-ci` | Diagnose and fix failing checks |
| `/iterative-test-loop` | Change → test until green |
| `/impact-aware-testing` | Run tests for changed files |
| `/review-bugbot` | Bugbot subagent review |
| `/review-security` | Security subagent review |
| `/explore-sota` | arXiv / web SOTA triage |

## Install

```bash
cp -r agent-skills/.cursor/commands/* your-project/.cursor/commands/
```

Cross-project commands with full step-by-step bodies are self-contained (not stubs). Cursor workflow commands that wrap personal skills (`ship-pr`, `review-bugbot`, etc.) expect those skills in `~/.cursor/skills/` or your agent-skills install.
