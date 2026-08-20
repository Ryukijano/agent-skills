# AI for Approximation Algorithms

## Description

Learning-augmented approximation, learned heuristics for NP-hard maximization and CSPs, and data-driven rounding.

## When to use

You want polynomial-time approximate solutions for NP-hard problems and are willing to use ML predictions to improve approximation factors or runtime.

## Key concepts

- **Approximation ratios and hardness**: worst-case guarantees and PTAS/FPTAS.
- **Learning-augmented approximation**: use predictions to beat classical lower bounds.
- **CSP and Max-Cut rounding**: learned rounding policies and semidefinite programming relaxations.
- **Data-driven heuristics**: train fast heuristics that approximate optimal solutions on a distribution.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

# Predict an approximate cut weight or rounding probability for Max-Cut
features = np.array([[0.5, 0.2, 0.8], [0.1, 0.9, 0.3], ...])
# Oracle labels from small exact solves
labels = np.array([1.2, 0.9, ...])

approx = GradientBoostingRegressor(random_state=42).fit(features, labels)
print("Predicted value:", approx.predict([[0.4, 0.3, 0.7]]))
```

## Tuning notes

- Verify that learned approximations retain valid worst-case or average-case guarantees.
- Use convex relaxations (LP/SDP) as a scaffold for learned rounding.
- Evaluate on out-of-distribution instance families, not just the training domain.

## Verification

1. Solve small Max-Cut instances exactly and compare a learned rounding policy to random rounding.
2. Prove or empirically verify an approximation ratio on a family of instances.
3. Benchmark a learned approximation heuristic against a classical constant-factor algorithm.

## References

- https://proceedings.neurips.cc/paper_files/paper/2024/file/2db08b94565c0d582cc53de6cee5fd47-Paper-Conference.pdf
- https://doi.org/10.1016/j.ejor.2020.07.063
- https://doi.org/10.1109/access.2020.3004964
- https://doi.org/10.48550/arxiv.2601.10583
- https://arxiv.org/abs/2006.09123
