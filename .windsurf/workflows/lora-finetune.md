---
description: Configure and run LoRA fine-tuning for vision transformers (DINOv2, ViT)
---

## LoRA Fine-Tuning Setup

1. Choose hyperparameters based on the recommended table:
   | Parameter | Conservative | Standard |
   |-----------|-------------|----------|
   | rank | 4 | 8 |
   | alpha | 8 | 16 |
   | dropout | 0.1 | 0.05 |
   | target_modules | qkv, proj | qkv, proj, fc1, fc2 |
   | start_block | 6 | 3 |
   | LoRA LR | 1e-4 | 1e-3 |

2. Inject LoRA into the encoder:
   ```python
   inject_lora_into_dinov2(encoder, r=8, alpha=16, dropout=0.05,
       target_modules=['qkv', 'proj', 'fc1', 'fc2'], start_block=3)
   ```

3. Create optimizer with separate LR groups:
   ```python
   lora_params = get_lora_params(encoder)
   optimizer = torch.optim.AdamW(lora_params, lr=1e-4)
   ```

4. Add gradient clipping:
   ```python
   torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
   ```

5. Run a smoke test (2 steps) to verify training works.

6. If loss is unstable, reduce LoRA LR by 10x.

7. If no adaptation, increase rank or add more target modules.

8. For progressive unfreezing, schedule block unfreezing across training steps.

9. Summarize: LoRA config, trainable params, training stability.
