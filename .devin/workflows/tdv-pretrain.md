---
description: Run TDV (Temporal Difference in Vision) pretraining on surgical video
---

## TDV Pretraining

1. Verify config exists and paths are correct:
   ```bash
   cat configs/train_mot/dinov2/tdv-pretrain.yaml | grep -E "frames_root|encoder_checkpoint|output_dir"
   ```

2. Run a 2-step smoke test:
   ```bash
   python scripts/pretrain_tdv.py --config configs/train_mot/dinov2/tdv-pretrain.yaml
   ```
   (Temporarily set `max_steps: 2` in config)

3. If smoke test passes, submit full training:
   ```bash
   sbatch jobs/tdv-pretrain.slurm
   ```

4. Monitor training:
   ```bash
   squeue -u $USER
   tail -f logs/tdv-pretrain_<JOBID>.out
   ```

5. Watch for collapse warnings in logs:
   - `feat_var < 1e-4` → representation collapse
   - `dino_entropy < 0.1` → teacher collapse
   - If collapse detected, increase DINO loss weight, check augmentations

6. After training completes, verify encoder checkpoint:
   ```bash
   ls -la outputs/tdv_pretrain/tdv_frame_encoder.pth
   ```

7. Run linear probe evaluation:
   ```bash
   python scripts/eval_tdv_linearprobe.py --checkpoint outputs/tdv_pretrain/final.pth.tar
   ```

8. Summarize: training steps, final loss, linear probe accuracy, collapse status.
