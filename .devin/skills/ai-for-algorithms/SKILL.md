# AI for Algorithms

## Description

Learning-augmented algorithms, learned data structures, and ML-guided design for search, routing, scheduling, and data-intensive pipelines.

## When to use

You want to improve classic algorithms with machine-learned predictions, design learned indexes or data structures, or tune algorithmic decisions on a distribution of instances.

## Key concepts

- **Learning-augmented algorithms**: algorithms that take ML predictions as advice and retain worst-case guarantees when predictions are poor.
- **Learned indexes and data structures**: replace or augment B-trees, Bloom filters, and sketches with neural models.
- **Algorithm configuration and selection**: choose or configure solvers based on instance features.
- **Competitive and approximation ratios**: prove bounds that degrade gracefully with prediction error.

## Code pattern

```python
import numpy as np
from sklearn.linear_model import Ridge

# Predicted next request in a caching/paging problem
X = np.array([[1, 0, 1], [0, 1, 0], ...])  # recent access patterns
y = np.array([2, 0, ...])                   # next accessed item

predictor = Ridge().fit(X, y)

def learned_paging_predict(cache, request):
    scores = predictor.predict([request])
    return int(np.argmax(scores))
```

## Tuning notes

- Start with strong classical baselines and measure incremental lift.
- Use held-out instance distributions that differ from training.
- Validate worst-case behavior on adversarial or pathological inputs.

## Verification

1. Implement a learned Bloom filter and compare false-positive rate to a standard Bloom filter.
2. Train a learned index on integer keys and measure query latency vs. space.
3. Benchmark a learning-augmented algorithm against the prediction-free worst-case baseline.

## References

- https://ar5iv.labs.arxiv.org/html/2006.09123
- https://cacm.acm.org/opinion/algorithms-with-predictions/
- https://arpi.unipi.it/bitstream/11568/1038818/1/BookChapter__Learned_data_structures.pdf
- http://theory.stanford.edu/~sergei/slides/HALG-slides.pdf
- https://proceedings.neurips.cc/paper_files/paper/2024/file/2db08b94565c0d582cc53de6cee5fd47-Paper-Conference.pdf
