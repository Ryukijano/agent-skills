# Setup ML Project

Scaffold a new ML research project following AIMSgeneral conventions (surgical video, agentic, 3D, or general).

## 1. Create skeleton
```bash
mkdir -p <project>/{core_app,configs,scripts,jobs,tests,data,outputs,inputs,docs}
cd <project>
git init
```

## 2. Standard files
- `AGENTS.md` — user preferences + workspace facts (copy from sibling project and adapt)
- `README.md` — one-command setup + smoke + typical usage
- `pyproject.toml` or `requirements.txt` (with versions)
- `.gitignore` (data/, outputs/, wandb/, *.pth, __pycache__, etc.)
- `.cursor/skills/` and `.cursor/commands/` (copy portable ones; add project-specific)

## 3. Cursor assets (copy from Gyanateet_tracking or AIMSgeneral as base)
At minimum:
- `reproducibility`, `code-quality`, `testing-strategy`, `git-branch-workflow`, `experiment-tracking`
- Commands: `code-review`, `debug-training`, `submit-gpu-job`, `setup-ml-project` (self)

## 4. Core Python layout (adapt to domain)
```
core_app/
  models/
  data/
  train.py
  eval.py
configs/
  default.yaml
scripts/
  train.sh
  eval.sh
jobs/
  train.slurm
tests/
  test_smoke.py
```

## 5. First commit
```bash
git add -A
git commit -m "chore: scaffold project structure + cursor skills/commands"
```

## 6. Next steps for user
- Fill `AGENTS.md` with domain facts.
- Add first smoke test that imports the model and runs a 2-step forward.
- Wire verification gate rule.
- Add first skill for the core technique.

Apply `reproducibility` and `code-quality` skills from the start.
