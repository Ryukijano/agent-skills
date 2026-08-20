# Self-Supervised Learning (SSL)

## Description

Pretext tasks, contrastive and non-contrastive SSL, masked prediction, and unsupervised representation learning for vision, language, and graphs.

## When to use

You have large amounts of unlabeled data and limited labels, or you want a pretrained representation that transfers well to downstream tasks.

## Key concepts

- **Pretext tasks**: predict rotation, solve jigsaw puzzles, inpaint, or forecast masked inputs to generate supervision.
- **Contrastive SSL**: SimCLR, MoCo, BYOL, DINO learn by pulling positive views together and pushing negatives apart.
- **Non-contrastive SSL**: VICReg, Barlow Twins, Bootstrap Your Own Latent (BYOL) avoid explicit negative pairs.
- **Masked modeling**: BERT-style token masking, MAE for vision, or data2vec for multimodal data.
- **Transfer learning**: pretrain on unlabeled data, then add a small head and finetune.

## Code pattern

```python
import torch, torchvision
from lightly.loss import NTXentLoss
from lightly.models.modules import SimCLRProjectionHead
from lightly.transforms.simclr_transform import SimCLRTransform

backbone = torchvision.models.resnet18(weights=None)
backbone.fc = torch.nn.Identity()
projector = SimCLRProjectionHead(512, 512, 128)
transform = SimCLRTransform(input_size=32)
criterion = NTXentLoss()
```

## Tuning notes

- Data augmentations (crop, color jitter, blur, grayscale) are the main inductive bias.
- Larger batch sizes help contrastive methods; non-contrastive methods can use smaller batches.
- Use a projection head during pretraining and a prediction head for non-contrastive methods.
- Monitor representation collapse via kNN accuracy, not just training loss.

## Verification

1. Train an SSL model on an unlabeled image set and run a linear probe.
2. Compare linear-probe accuracy to a supervised baseline and a random-initialized baseline.
3. Inspect embeddings with t-SNE/UMAP and nearest-neighbor retrieval.

## References

- https://doi.org/10.48550/arxiv.2301.05712
- https://docs.lightly.ai/self-supervised-learning/
- https://arxiv.org/abs/2006.08218
- https://github.com/lightly-ai/lightly
