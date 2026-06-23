---
name: ablation-study
description: Design, execution, and reporting of systematic ablations for MOT, TDV pretraining, and surgical video models. Emphasizes matched controls, metrics, and paper-ready tables.
---

## Ablation Studies

### Principles
- Change one thing at a time (or clearly factorized).
- Keep data, seeds, optimizer, schedule matched across the family.
- Use WandB groups for easy comparison.
- Report mean ± std over seeds when variance matters.

### Common surgical MOT ablations
- Backbone: DINOv2 ViT-S vs ViT-B vs (larger)
- Pretrain: none vs TDV vs GOT-JEPA vs ImageNet-only
- LoRA rank / start block
- Loss weights (motion, ReID, det)
- Tracker gates (birth, min_hits)
- Temporal context length T
- Geometry (depth/CoTracker) on/off in Stage 4

### Execution
1. Define the matrix in `experiments/<slug>/ablations.yaml`.
2. Launch matched runs (same commit, same data manifest).
3. After all finish: pull table via WandB API or UI.
4. Plot (bar or table) + statistical note.
5. Document "removed X → Y points" with confidence.

### Reporting
Include:
- Exact config diff (or full configs committed)
- Seeds
- Hardware
- "All else equal" statement

Related: `experiment-tracking`, `reproducibility`, `pretrain-and-evaluate`.
