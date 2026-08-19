# Reproducible Scientific Workflows on HPC

## Description

Workflow engines (Snakemake, Nextflow, CWL), containers, DVC, SLURM job arrays, checkpointing, and cloud HPC.

## When to use

You are running multi-step scientific pipelines on a cluster and need reproducibility, scaling, and fault tolerance.

## Key concepts

- **Workflow engines**: Snakemake (Pythonic, file-based), Nextflow (dataflow, portable), CWL/WDL (standardized).
- **Containers**: Docker for dev, Singularity/Apptainer for HPC (no root needed).
- **Reproducibility**: `conda-lock`, `pip-tools`, DVC for data/models.
- **HPC**: SLURM/PBS job arrays, `--dependency`, checkpointing, `$SCRATCH` vs permanent storage.
- **Cloud HPC**: AWS ParallelCluster, Azure Batch, GCP Slurm, cloud bursting.

## Code pattern

```python
# Snakemake rule
rule train:
    input:
        "data/train.csv"
    output:
        "models/model.pt"
    shell:
        "python train.py --input {input} --output {output}"
```

SLURM:

```bash
#SBATCH --array=1-10%1
#SBATCH --gpus=1
python train.py --seed $SLURM_ARRAY_TASK_ID
```

## Tuning notes

- Job arrays are ideal for embarrassingly parallel sweeps; limit concurrency with `%N`.
- Checkpoint model + optimizer + RNG state for long jobs.
- Store checkpoints in `$SCRATCH`, copy final artifacts to permanent storage.

## Verification

1. Run a Snakemake/Nextflow pipeline end-to-end with `--dry-run` first.
2. Verify a container reproduces results across two hosts.
3. Resume a job from a checkpoint and confirm identical loss curve.

## References

- https://snakemake.readthedocs.io/
- https://www.nextflow.io/
- https://dvc.org/doc
- https://docs.mila.quebec/examples/good_practices/checkpointing/
