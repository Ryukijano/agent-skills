# AI for Pricing

## Description

Use AI for Pricing to estimate elasticity, set dynamic prices, manage revenue and optimize promotions.

## When to use

You need to set or adjust prices to maximize revenue, margin, or market share while accounting for demand response and competitive effects.


## Usage


- **Price elasticity**: Estimate how quantity demanded changes with price, often via log-log regression or causal ML.
- **Dynamic pricing**: Adjust prices in real time based on demand, inventory, and competitor signals.
- **Revenue management**: Capacity control, overbooking, and fare-class optimization.
- **Causal pricing**: Off-policy learning and DML to forecast demand under new price regimes.

## Steps

1. Collect and prepare transaction, price, competitor and inventory data.
2. Set or adjust prices to maximize revenue.
3. Margin.
4. Market share while accounting for demand response and competitive effects.
5. Validate by estimating a price elasticity and validate on an experimental price change.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

## Code pattern

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Log-log model for price elasticity
df["log_q"] = np.log(df["quantity"])
df["log_p"] = np.log(df["price"])
X = sm.add_constant(df[["log_p", "log_income", "promo"]])

model = sm.OLS(df["log_q"], X).fit()
print("Elasticity:", model.params["log_p"])
```


## Tuning notes

- Address price endogeneity with instrumental variables, randomized experiments, or DML.
- Consider business rules: price fences, fairness, and customer perception.
- Test new pricing policies with controlled experiments or counterfactual evaluation before rollout.


## Verification

1. Estimate a price elasticity and validate on an experimental price change.
2. Build a dynamic pricing simulator and optimize for revenue under demand uncertainty.
3. Compare a causal pricing model to a pure forecast model in an off-policy test.

## References

- https://doi.org/10.48550/arxiv.2312.15282
- https://doi.org/10.1057/s41272-024-00478-6
- https://proceedings.mlr.press/v202/simchi-levi23a/simchi-levi23a.pdf
- https://www.sciencedirect.com/science/article/abs/pii/S0278431921000578
