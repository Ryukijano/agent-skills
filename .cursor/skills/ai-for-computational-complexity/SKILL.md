# AI for Computational Complexity

## Description

Using machine learning to predict, characterize, and understand the complexity of computational problems, reductions, and hardness proxies.

## When to use

You want to estimate the difficulty of an algorithmic or combinatorial problem, predict solver runtime, or learn hardness proxies for reductions and complexity classes.

## Key concepts

- **Complexity classes and reductions**: P, NP, NP-completeness, fine-grained reductions, and parameterized complexity.
- **Hardness proxies**: statistical-query lower bounds, low-degree likelihood ratios, and the Franz–Parisi criterion for planted problems.
- **ML for runtime prediction**: train regressors on instance features to predict SAT/MIP solver behavior.
- **Learned complexity boundaries**: data-driven conjectures on phase transitions and average-case hardness.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# instance features: n_vars, n_clauses, clause/variable ratio, graph metrics
X = np.array([[100, 420, 4.2, 0.35], [500, 2100, 4.2, 0.32], ...])
y = np.array([0.12, 1.4, ...])  # solver runtime in seconds

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = GradientBoostingRegressor(random_state=42).fit(X_train, y_train)
print("MAE:", np.mean(np.abs(model.predict(X_test) - y_test)))
```

## Tuning notes

- Use instance features that capture structure, not just size.
- Compare predicted runtimes against classical worst-case bounds.
- Watch for distribution shift when generalizing across problem families.

## Verification

1. Train a runtime predictor on a set of SAT/MIP instances and evaluate with time-based splits.
2. Plot predicted vs. actual runtimes and identify systematic underestimation on hard instances.
3. Compare the learned ranking of instances to a theoretical hardness proxy.

## References

- https://doi.org/10.1088/1742-5468/ad3a5b
- https://plato.stanford.edu/entries/computational-complexity/
- https://doi.org/10.48550/arxiv.2103.05127
- https://cacm.acm.org/research/fifty-years-of-p-vs-np-and-the-possibility-of-the-impossible/
- https://link.springer.com/article/10.1007/s10208-023-09607-w
