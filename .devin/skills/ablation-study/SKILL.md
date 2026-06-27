---
name: ablation-study
description: Design and run systematic ablation studies comparing model variants by removing components one at a time. Use when planning ablation experiments, creating config variants, or analyzing component contributions.
---

## Ablation Study Design

### Process

1. Identify components to ablate (loss functions, model parts, training strategies)
2. Define baseline = full model with all components
3. Create config variant per ablation (change one thing at a time)
4. Run all variants with SAME seed, SAME data split, SAME training budget
5. Collect results into comparison table
6. Analyze: which component has largest impact? Any interactions?
7. Create bar chart + table for paper

### Common ablation targets

- Loss functions (remove DINO loss, remove L2-SP, remove motion loss)
- Model components (remove motion encoder, remove ReID head)
- Training strategies (no progressive unfreezing, no LoRA, no augmentation)
- Backbone size (ViT-S vs ViT-B)
- Data (different splits, different frame counts)
