# Optimization Under Uncertainty

## Description

Robust optimization, stochastic programming, distributionally robust optimization, and Wasserstein DRO.

## When to use

You need to make decisions that are robust to uncertainty, distribution shift, or rare events.

## Key concepts

- **Robust optimization**: optimize worst case over an uncertainty set.
- **Stochastic programming**: optimize expected value over known distribution.
- **DRO**: optimize over an ambiguity set of distributions.
- **Wasserstein DRO**: ambiguity set defined by Wasserstein ball.

## Code pattern

```python
import cvxpy as cp

# Robust linear program
x = cp.Variable(n)
objective = cp.Minimize(c @ x)
constraints = [A @ x <= b + delta]  # uncertainty in b
prob = cp.Problem(objective, constraints)
prob.solve()
```

## Tuning notes

- Robustness comes at cost (conservatism).
- DRO often reduces to regularization with small ambiguity sets.
- Use convex duality for tractable reformulations.

## Verification

1. Solve a robust LP and compare to nominal solution.
2. Implement Wasserstein DRO on a small regression problem.
3. Test robustness on perturbed test data.

## References

- https://www.cvxpy.org/
- https://optimization-online.org/2021/04/8360/
- https://dl.acm.org/doi/10.1287/moor.2022.1275
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5B4E65E3A5A2AEF24E218A6B34E6EAA2
