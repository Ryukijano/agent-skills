# Contrastive Learning

## Description

Instance discrimination, InfoNCE, SimCLR, MoCo, CLIP, and deep metric learning for vision, language, and retrieval.

## When to use

You want an embedding space where semantically similar samples are close and dissimilar samples are far apart, often with limited labels.

## Key concepts

- **Positive and negative pairs**: views of the same sample vs. other samples.
- **InfoNCE / NT-Xent**: noise-contrastive loss that scores positive pairs against negatives.
- **Momentum encoders and memory banks**: maintain a large and consistent set of negative examples.
- **Multimodal contrastive learning**: CLIP aligns images and text in a shared embedding space.
- **Hard negative mining**: focus on difficult negatives to improve sample efficiency.

## Code pattern

```python
from pytorch_metric_learning import losses, miners

miner = miners.MultiSimilarityMiner()
loss_func = losses.TripletMarginLoss()

for data, labels in dataloader:
    optimizer.zero_grad()
    embeddings = model(data)
    hard_pairs = miner(embeddings, labels)
    loss = loss_func(embeddings, labels, hard_pairs)
    loss.backward()
    optimizer.step()
```

## Tuning notes

- Batch size, temperature, and the number of negatives strongly affect InfoNCE.
- Choose a distance function (cosine, Euclidean) and mining strategy suited to the task.
- For CLIP-style multimodal training, balance image and text encoders and cap sequence length.
- Watch for mode collapse where embeddings collapse to a constant.

## Verification

1. Train a retrieval model and report Recall@K or mAP on a held-out query set.
2. Run a kNN classifier on learned embeddings and compare to a supervised baseline.
3. Visualize embedding space and confirm clusters align with classes.

## References

- https://arxiv.org/abs/2002.05709
- https://arxiv.org/abs/1911.05722
- https://arxiv.org/abs/2103.00027
- https://kevinmusgrave.github.io/pytorch-metric-learning/
