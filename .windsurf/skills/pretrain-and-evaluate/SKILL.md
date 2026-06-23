---
name: pretrain-and-evaluate
description: Run the full Stage 0 pretrain to Stage 1 detection to evaluation pipeline. Use when executing end-to-end ML training pipelines, chaining pretraining with downstream task evaluation.
---

## Pretrain + Evaluate Pipeline

### Stage 0: Pretraining

1. Verify config: `cat configs/.../tdv-pretrain.yaml`
2. Smoke test: `python scripts/pretrain_tdv.py --config <config> --max-steps 2`
3. Submit: `sbatch jobs/tdv-pretrain.slurm`
4. Verify checkpoint: `ls outputs/tdv_pretrain/tdv_frame_encoder.pth`

### Stage 1: Detection

5. Update detection config: `encoder_checkpoint: outputs/tdv_pretrain/tdv_frame_encoder.pth`
6. Smoke test detection training
7. Submit detection job to Slurm

### Evaluation

8. Run: `python scripts/eval_mot.py --config <config> --checkpoint <path> --split val`
9. Compare: TDV-pretrained vs baseline (vanilla DINOv2)
10. Target: mAP@50 improvement ≥ 3 points, MOTA ≥ 5 points
