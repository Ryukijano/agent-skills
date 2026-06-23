---
description: Submit and monitor Slurm jobs on the AIRE HPC cluster
---

## AIRE Slurm Job Submission

1. Verify the training script runs for 1-2 steps without errors:
   ```bash
   python scripts/<script>.py --config <config>.yaml --max-steps 2
   ```

2. Verify the SLURM job script in `jobs/<name>.slurm` has correct settings:
   - `#SBATCH --partition=gpu`
   - `#SBATCH --gres=gpu:l40s:<N>` (max 3 per node)
   - `module load cuda/12.6`
   - Conda activation and `LD_LIBRARY_PATH` set

3. Create logs directory if needed:
   ```bash
   mkdir -p logs
   ```

4. Submit the job:
   ```bash
   sbatch jobs/<name>.slurm
   ```

5. Note the job ID and monitor:
   ```bash
   squeue -j <JOBID>
   tail -f logs/<name>_<JOBID>.out
   ```

6. After completion, check efficiency:
   ```bash
   seff <JOBID>
   ```

7. If failed, check error log:
   ```bash
   tail -50 logs/<name>_<JOBID>.err
   ```

8. Summarize: job ID, GPU allocation, metrics, issues.
