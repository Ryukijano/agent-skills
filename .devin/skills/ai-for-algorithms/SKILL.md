# AI for Algorithms

## Description

Use machine learning to augment classic algorithms with learned predictions, indexes, and data structures.

## When to use

You want to improve classic algorithms with machine-learned predictions, design learned indexes or data structures, or tune algorithmic decisions on a distribution of instances.

## Usage

- Build learning-augmented algorithms that take ML predictions as advice while retaining worst-case guarantees.
- Replace or augment B-trees, Bloom filters, and sketches with learned indexes and data structures.
- Select and configure solvers, sorters, or search algorithms based on instance features.
- Prove competitive or approximation ratios that degrade gracefully with prediction error.

## Steps

1. Identify the algorithmic decision (caching, indexing, search, or routing) to enhance and collect instance features.
2. Train a lightweight predictor on historical instances to provide advice for that decision.
3. Design the algorithm to incorporate predictions while bounding worst-case cost when predictions are poor.
4. Benchmark the learning-augmented method against the classical worst-case baseline on held-out distributions.
5. Validate on adversarial or pathological inputs and tune the reliance on predictions.
6. Deploy as a drop-in replacement or wrapper and monitor performance on production traffic.

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

- https://arxiv.org/abs/2006.09123
- https://cacm.acm.org/opinion/algorithms-with-predictions/
- https://arpi.unipi.it/bitstream/11568/1038818/1/BookChapter__Learned_data_structures.pdf
- http://theory.stanford.edu/~sergei/slides/HALG-slides.pdf
- https://proceedings.neurips.cc/paper_files/paper/2024/file/2db08b94565c0d582cc53de6cee5fd47-Paper-Conference.pdf
