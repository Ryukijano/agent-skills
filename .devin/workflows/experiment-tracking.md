---
description: Set up structured ML experiment tracking with config logging and result comparison
---

## Experiment Tracking Setup

1. Create output directory structure:
   ```bash
   mkdir -p outputs/<experiment_name>
   ```

2. Add config snapshot to training script:
   ```python
   import yaml
   with open("outputs/<name>/config.yaml", "w") as f:
       yaml.dump(config, f)
   ```

3. Initialize WandB (if using):
   ```python
   wandb.init(project="<project>", name="<run>", config=config)
   ```

4. Log metrics at each step:
   ```python
   wandb.log({"loss": loss.item(), "lr": lr}, step=step)
   ```

5. Save env info (git commit, versions) to `outputs/<name>/env_info.json`.

6. After all experiments, generate comparison table.

7. Summarize: tracking setup, run names, key metrics.
