# Submit GPU Job (AIRE)

1. Verify the training script runs locally for 1-2 steps without errors:
   ```
   python scripts/<script>.py --config <config>.yaml --max-steps 2
   ```

2. Create or verify the SLURM job script in `jobs/<name>.slurm`. Ensure it has:
   - `#SBATCH --partition=gpu`
   - `#SBATCH --gres=gpu:l40s:<N>` (max 3 per node)
   - `#SBATCH --mem=96G` (adjust per GPU count)
   - `#SBATCH --time=<HH:MM:SS>`
   - `module load cuda/12.6`
   - Conda activation with `source /scratch/kcwp264/conda/etc/profile.d/conda.sh`
   - `export LD_LIBRARY_PATH` for the conda env

3. Create the logs directory if it doesn't exist:
   ```bash
   mkdir -p logs
   ```

4. Submit the job:
   ```bash
   sbatch jobs/<name>.slurm
   ```

5. Note the job ID from the output (e.g., `Submitted batch job 4624948`).

6. Monitor job status:
   ```bash
   squeue -j <JOBID>
   ```

7. Once the job starts, tail the output log:
   ```bash
   tail -f logs/<name>_<JOBID>.out
   ```

8. After completion, check job efficiency:
   ```bash
   seff <JOBID>
   ```
   Look for: GPU utilization >70%, memory usage <80%, no OOM kills.

9. If the job failed, check the error log:
   ```bash
   cat logs/<name>_<JOBID>.err | tail -50
   ```

10. Summarize: report the job ID, GPU allocation, training metrics, and any issues encountered.
