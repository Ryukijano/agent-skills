# Masked Autoencoders (MAE)

## Description

BERT-style masked prediction for vision, BEVT, data2vec, and generative masked image and language modeling.

## When to use

You want to pretrain a transformer with high input masking ratios and reconstruct the masked content, especially for images or multimodal signals.

## Key concepts

- **Asymmetric encoder-decoder**: encoder processes only visible patches; decoder is lightweight.
- **High masking ratio**: vision MAE often masks 75% of input patches.
- **Pixel/ token reconstruction**: target is the original masked patch, often after per-patch normalization.
- **Masked language modeling**: BERT, RoBERTa, and DeBERTa use token masking for text.
- **data2vec and BEiT**: unified masked-prediction frameworks for multiple modalities.

## Code pattern

```python
import torch
from mae import models_mae

model = models_mae.mae_vit_base_patch16()
loss, pred, mask = model(images, mask_ratio=0.75)
loss.backward()
```

## Tuning notes

- Use a high masking ratio for images; lower ratios work better for dense signals or video.
- Keep the decoder small; most compute should be in the encoder.
- Normalize pixel targets by their mean and std within each patch.
- Minimal augmentation is usually sufficient for MAE pretraining.

## Verification

1. Reconstruct masked image patches and report PSNR/SSIM.
2. Run a linear probe or finetune on a downstream classification task.
3. Ablate masking ratio and decoder depth and measure downstream accuracy.

## References

- https://doi.org/10.48550/arxiv.2111.06377
- https://github.com/facebookresearch/mae
- https://ar5iv.labs.arxiv.org/html/2202.03670
- https://github.com/huggingface/pytorch-image-models
