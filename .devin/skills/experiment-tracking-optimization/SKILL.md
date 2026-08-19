# Experiment Tracking and Hyperparameter Optimization

## Description

W&B, MLflow, Neptune, Aim, Optuna, Ray Tune, and reproducible hyperparameter search on HPC.

## When to use

You need to track experiments, compare runs, and search hyperparameters for scientific ML.

## Key concepts

- **Experiment tracking**: W&B, MLflow, Neptune, TensorBoard, Aim.
- **HPO**: Optuna, Ray Tune, Ax, W&B Sweeps, Hyperband/ASHA.
- **Reproducibility**: log hyperparameters, code commit, data version, random seeds, environment.
- **Distributed search**: Ray Tune across a SLURM cluster; Optuna with RDB storage.

## Code pattern

```python
import wandb
import optuna

def objective(trial):
    lr = trial.suggest_float("lr", 1e-5, 1e-1, log=True)
    # train and return validation metric
    return val_loss

study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=100)
```

W&B:

```python
wandb.init(project="science-ml", config={"lr": 1e-3})
wandb.log({"loss": loss})
```

## Tuning notes

- W&B has the best UI but is SaaS; MLflow/Aim are self-hosted.
- Optuna is lightweight; Ray Tune is best for large distributed sweeps.
- Use ASHA/Hyperband early stopping to cut compute.

## Verification

1. Log 10 training runs and compare them in the tracking UI.
2. Run an Optuna search and verify the best trial improves over random search.
3. Re-run the best config with a different seed and check variance.

## References

- https://docs.wandb.ai/
- https://mlflow.org/
- https://optuna.readthedocs.io/
- https://docs.ray.io/en/latest/tune/index.html
