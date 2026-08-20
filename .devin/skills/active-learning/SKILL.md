# Active Learning

## Description

Iteratively select the most informative unlabeled data points for efficient annotation and model improvement.

## When to use

You have a large pool of unlabeled data and limited labeling budget.

## Key concepts

- **Uncertainty sampling**: query points the model is least confident about.
- **Diversity sampling**: cover different regions of the data distribution.
- **Expected model change**: query points that would most change the model.
- **Pool-based vs stream-based**: select from a fixed pool or online.

## Code pattern

```python
import numpy as np

# Uncertainty sampling: pick points with lowest max probability
probs = model.predict_proba(X_pool)
uncertainty = 1 - np.max(probs, axis=1)
query_idx = np.argsort(uncertainty)[-k:]
```

## Tuning notes

- Combine uncertainty and diversity to avoid outliers.
- Re-train the model after each query batch.
- Track learning curves versus random sampling as a baseline.

## Verification

1. Implement uncertainty sampling on a text or image dataset.
2. Plot model accuracy versus number of labeled samples.
3. Compare uncertainty, diversity, and random acquisition strategies.

## References

- https://aclanthology.org/2025.acl-long.708/
- https://arxiv.org/abs/2405.00334
- https://modal-python.readthedocs.io/
- https://github.com/google-research/google-research/tree/master/active_learning
