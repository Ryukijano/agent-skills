# Pretrain and Evaluate

This workflow runs the complete Stage 0 (pretraining) → Stage 1 (detection) → evaluation pipeline.

### Stage 0: Pretraining

1. Verify the pretraining config exists and is correct:
   ```
   cat configs/train_mot/dinov2/tdv-pretrain.yaml
   ```
   Check: `frames_root` path, `batch_size`, `max_steps`, `output_dir`.

2. Run a 2-step smoke test locally:
   ```bash
   python scripts/pretrain_tdv.py --config configs/train_mot/dinov2/tdv-pretrain.yaml
   ```
   (Modify config temporarily: `max_steps: 2`, `log_interval: 1`)

3. If smoke test passes, submit the full pretraining job:
   ```bash
   sbatch jobs/tdv-pretrain.slurm
   ```

4. Wait for pretraining to complete. Monitor via:
   ```bash
   squeue -u $USER
   tail -f logs/tdv-pretrain_<JOBID>.out
   ```

5. Verify the encoder checkpoint was saved:
   ```bash
   ls -la outputs/tdv_pretrain/tdv_frame_encoder.pth
   ```

### Stage 1: Downstream Detection

6. Update the detection config to point to the pretrained encoder:
   ```yaml
   model:
     encoder_checkpoint: outputs/tdv_pretrain/tdv_frame_encoder.pth
   ```

7. Run a smoke test of the detection training:
   ```bash
   python scripts/train_mot.py --config configs/train_mot/dinov2/cholec20-mot-stage1-tdv-detect.yaml
   ```
   (Use `--max-steps 2` or equivalent for quick verification)

8. Submit the full detection training job to Slurm.

### Evaluation

9. After detection training completes, run evaluation on the validation split:
   ```bash
   python scripts/eval_mot.py \
       --config configs/train_mot/dinov2/cholec20-mot-stage1-tdv-detect.yaml \
       --checkpoint outputs/mot/<run_name>/best.pth \
       --split val
   ```

10. Compare metrics against the baseline (vanilla DINOv2 without TDV pretraining):
    - mAP@50: target improvement ≥ 3 points
    - MOTA: target improvement ≥ 5 points
    - Per-tool AP: check for consistent improvement across all 7 tools

11. Summarize results in a table comparing baseline vs TDV-pretrained.
