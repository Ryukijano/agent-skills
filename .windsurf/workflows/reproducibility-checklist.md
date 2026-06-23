---
description: Audit a project for reproducibility and fix any gaps before paper submission or code release
---

## Reproducibility Audit

1. Check for a LICENSE file:
   ```bash
   ls LICENSE* 2>/dev/null || echo "MISSING: No license file"
   ```

2. Check for a README with installation and usage instructions:
   ```bash
   head -20 README.md
   ```
   Verify it has: project description, install steps, quick start, citation.

3. Check for dependency specification:
   ```bash
   ls requirements.txt environment.yml pyproject.toml 2>/dev/null
   ```
   If none exist, create one. Prefer `pyproject.toml` with `[project]` dependencies.

4. Check that all seeds are set in training scripts:
   ```bash
   grep -rn "seed\|random_state\|manual_seed" --include="*.py" scripts/ core_app/
   ```
   If missing, add `set_all_seeds(config['seed'])` at the start of training.

5. Check for hardcoded paths:
   ```bash
   grep -rn "/scratch/\|/home/\|C:\\" --include="*.py" | grep -v "config\|args\|parser\|#"
   ```
   Replace any found with config parameters or environment variables.

6. Check that configs are saved with experiment outputs:
   ```bash
   ls outputs/*/config.yaml 2>/dev/null || echo "MISSING: No saved configs in outputs/"
   ```

7. Check that git commit hashes are logged:
   ```bash
   grep -rn "rev-parse\|git_commit" --include="*.py" scripts/ | head -5
   ```

8. Verify single-command reproduction:
   ```bash
   # This should work without errors (dry run):
   python scripts/train.py --config configs/default.yaml --max-steps 1
   ```

9. Check for `.gitignore` covering data, outputs, and caches:
   ```bash
   grep -E "data/|outputs/|wandb/|__pycache__" .gitignore
   ```

10. Generate a reproducibility report:
    - List all gaps found
    - Fix each gap or document why it can't be fixed
    - Create a `REPRODUCIBILITY.md` summarizing the audit results
