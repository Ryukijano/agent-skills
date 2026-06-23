---
description: Set up Weights & Biases experiment tracking for ML projects
---

## WandB Experiment Setup

1. Install and login:
   ```bash
   pip install wandb
   wandb login
   ```

2. Initialize in training script:
   ```python
   import wandb
   wandb.init(
       project="<project_name>",
       name="<run_name>",
       config=all_hyperparameters_dict,
   )
   ```

3. Log metrics every N steps:
   ```python
   wandb.log({"loss": loss.item(), "lr": lr}, step=global_step)
   ```

4. For DDP, only log on rank 0:
   ```python
   if int(os.environ.get("RANK", 0)) == 0:
       wandb.log(...)
   ```

5. For offline mode on compute nodes:
   ```bash
   export WANDB_MODE=offline
   # Sync later:
   wandb sync wandb/offline-run-*/
   ```

6. Set WandB directory to avoid HOME quota:
   ```bash
   export WANDB_DIR=/scratch/kcwp264/wandb
   ```

7. Finish run at end of training:
   ```python
   wandb.finish()
   ```

8. Summarize: project name, run URL, key metrics logged.
