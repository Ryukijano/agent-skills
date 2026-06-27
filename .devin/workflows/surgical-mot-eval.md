---
description: Evaluate surgical multi-object tracking models on CholecTrack20
---

## Surgical MOT Evaluation

1. Verify checkpoint and config paths:
   ```bash
   ls outputs/mot/<run_name>/best.pth
   cat configs/train_mot/dinov2/<config>.yaml | grep -E "eval_split|infer_score"
   ```

2. Run evaluation on validation split:
   ```bash
   python scripts/eval_mot.py \
       --config configs/train_mot/dinov2/<config>.yaml \
       --checkpoint outputs/mot/<run_name>/best.pth \
       --split val
   ```

3. Check key metrics:
   - mAP@50 (target ≥ 0.35)
   - MOTA (target ≥ 60)
   - Per-tool AP (check for low-AP tools)

4. If mAP is near zero, check for:
   - Deformable DETR spatial shape bug
   - DN-DETR query overflow
   - Wrong checkpoint loaded
   - Data split leakage

5. Compare against baseline (vanilla DINOv2 without pretraining).

6. Generate per-tool AP table and confusion matrix.

7. Summarize: mAP, MOTA, per-tool breakdown, comparison to baseline.
