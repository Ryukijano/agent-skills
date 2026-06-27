---
description: Design and run a systematic ablation study comparing model variants
---

## Ablation Study

1. Identify the component(s) to ablate. Common ablation targets:
   - Model components (remove motion encoder, remove ReID head)
   - Loss functions (remove DINO loss, remove L2-SP)
   - Training strategies (no progressive unfreezing, no LoRA)
   - Data augmentation (no DINO aug, no color jitter)
   - Backbone size (vits14 vs vitb14)

2. Define the baseline configuration:
   ```bash
   cat configs/default.yaml | grep -E "model|loss|optimizer|training"
   ```
   This is the "full model" — all components enabled.

3. For each ablation, create a config variant:
   ```bash
   # Example: ablate DINO loss
   cp configs/default.yaml configs/ablation_no_dino_loss.yaml
   # Edit: set use_dino_loss: false, dino_loss_weight: 0.0
   ```

4. List all ablation configs to run:
   ```
   configs/ablation_no_dino_loss.yaml
   configs/ablation_no_motion_encoder.yaml
   configs/ablation_no_lora.yaml
   configs/ablation_no_progressive_unfreeze.yaml
   configs/ablation_vits14.yaml
   ```

5. Run each ablation with the SAME seed, SAME data split, SAME training budget:
   ```bash
   for config in configs/ablation_*.yaml; do
       name=$(basename $config .yaml)
       sbatch --job-name=$name jobs/train.slurm
   done
   ```

6. Collect results into a comparison table:
   ```markdown
   | Variant | Val mAP@50 | MOTA | Params | Notes |
   |---------|------------|------|-------|-------|
   | Full model | 0.35 | 61 | 86M | All components |
   | - DINO loss | 0.22 | 45 | 86M | Representation collapse |
   | - Motion encoder | 0.30 | 55 | 84M | No temporal modeling |
   | - LoRA | 0.18 | 38 | 86M | Full frozen backbone |
   | - Progressive unfreeze | 0.28 | 52 | 86M | All frozen throughout |
   | - ViT-S (vs ViT-B) | 0.25 | 48 | 22M | Smaller backbone |
   ```

7. Analyze results:
   - Which component has the largest impact when removed?
   - Are there interactions (removing A + B is worse than either alone)?
   - Is the full model using all components optimally?

8. Create ablation figures:
   - Bar chart: mAP for each variant
   - Table: formatted for paper inclusion

9. Summarize findings as bullet points for paper discussion section.
