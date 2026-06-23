---
name: pretrain-and-evaluate
description: Reference for the full pretrain (TDV/JEPA) → MOT stages → leak-free stratified evaluation pipeline on CholecTrack20. Use when planning or auditing end-to-end experiments.
---

## End-to-End Pretrain → MOT Eval

### Pipeline stages
1. TDV (or GOT-JEPA) pretrain on Cholec80-like video → frame encoder weights.
2. Stage 1 supervised teacher (detector_only) on CT20 train using the encoder.
3. Stage 2 SSL / temporal adaptation (frozen or light student).
4. Stage 3 joint MOT (det + track + reid).
5. Stage 4 lean (OccuSolver + geometry stubs) — recommended final.
6. Eval: smoke-stratified mAP/MOTA + HOTA; never on pretrain-overlap videos.

### Success criteria (typical targets)
- mAP@50 lift ≥ 3–5 pts vs vanilla DINOv2 baseline.
- MOTA lift ≥ 5 pts.
- Stable per-tool AP (no tool <0.10 after tuning).
- HOTA after reasonable tracker gate search.

### Leak-free rule (critical)
CT20 Test overlap with pretrain: VID01,06,07,12,25,39,92,111. Val: VID30,110. Exclude from SSL and all training for reported numbers.

### Artifacts to capture
- Encoder weights + full checkpoint.
- Exact config + git sha + data manifest.
- WandB run + group for ablations.
- Eval json + per-tool table.

Related skills: `tdv-pretrain`, `surgical-mot-eval`, `mot-training-workflow`, `data-management`, `ablation-study`, `reproducibility`.
