# Gyanateet_tracking Cursor Skills & Commands

Rich collection of skills (knowledge) and commands (workflows) for surgical MOT, TDV pretraining, research best practices, and SWE hygiene.

## Current inventory (as of this expansion)
See `find .cursor/skills -name SKILL.md | sort` and `find .cursor/commands -name '*.md' | sort`.

### Skills (reference)
Core research + SWE + MOT + domain-specific (30+).

### Commands (procedural)
Full step-by-step for training, eval, debugging, PRs, releases, Spark/Cosmos, 3D, agentic, etc. (25+).

## Cross-conversion policy
- Every significant skill has a command counterpart (step-by-step invocation).
- Every command has a skill counterpart (concise reference knowledge).
- This enables both auto-suggestion (skills) and explicit `/workflow` usage (commands).

## How to bootstrap a new project
1. Copy the `.cursor/` tree (or selected skills/commands).
2. Adapt AGENTS.md.
3. Add project-specific skills (e.g. `my-model-training`).
4. Wire verification gate and research-integrity rules.

## Key domain entry points
- MOT / TDV: `mot-training-workflow`, `surgical-mot-eval`, `tdv-pretrain`, `pretrain-and-evaluate`
- HPC: `aire-slurm-submit`, `submit-gpu-job`, `spark-hardware-optim`
- Data: `data-management`, `surgical-video-data-pipeline`
- Research process: `reproducibility`, `ablation-study`, `experiment-tracking`
- SWE: `code-quality`, `testing-strategy`, `git-branch-workflow`
- External: `dgx-spark-cosmos3`, `nemotron-agent-loop`, `endosight-3d-pipeline`, `3d-reconstruction-best-practices`

Follow the verification gate on all non-trivial edits.
