---
description: Ensure ML research reproducibility through seeds, config logging, and environment capture
---

## Reproducibility Setup

1. Add seed function to training script:
   ```python
   def set_all_seeds(seed=42):
       import random, numpy as np, torch
       random.seed(seed); np.random.seed(seed)
       torch.manual_seed(seed); torch.cuda.manual_seed_all(seed)
   ```

2. Add config + environment logging to experiment outputs:
   ```python
   # Save config.yaml and env_info.json (git commit, torch/cuda versions)
   ```

3. Run the reproducibility audit checklist (see `/reproducibility-checklist`).

4. Fix any gaps found.

5. Verify single-command reproduction works.

6. Summarize: what was set up, what gaps were fixed.
