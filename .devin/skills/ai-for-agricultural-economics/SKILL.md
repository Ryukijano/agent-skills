# AI for Agricultural Economics

## Description

Machine learning and econometric ML for farm decision support, risk, policy, market analysis, adoption, and the economics of digital agriculture.

## When to use

You are evaluating the economic outcomes of farm technologies, forecasting prices or yields, modelling adoption and risk, or building decision support for farmers and policymakers.

## Usage

- **Yield and price forecasting**: predict crop yields, commodity prices, and revenue at regional or farm scale.
- **Risk and insurance analytics**: estimate weather, yield, and price risk for crop insurance or hedging.
- **Adoption and impact evaluation**: model technology adoption, treatment effects, and farm-level impact.
- **Decision support systems**: build cost-benefit and farm-planning tools that integrate agronomic and economic models.
- **Policy and market analysis**: assess subsidies, trade, and supply-chain effects.

## Steps

1. Collect farm accounts, market, policy, weather, and agronomic data.
2. Define the economic outcome (profit, cost, revenue, adoption, risk).
3. Build predictive, causal, or optimisation models suited to the question.
4. Validate on held-out farms, regions, or time periods.
5. Translate results into actionable recommendations and policy briefs.

## Code pattern

```python
import pandas as pd
import statsmodels.api as sm

X = sm.add_constant(df[["input_cost", "weather_index", "output_price"]])
y = df["farm_profit"]

model = sm.OLS(y, X).fit()
print(model.summary())
```

## Tuning notes

- Address endogeneity, omitted variables, and selection bias when estimating causal effects.
- Reflect heterogeneity across farm sizes, regions, and production systems.
- Incorporate farmer behaviour, risk aversion, and adoption constraints.
- Validate with out-of-sample predictions and robustness checks.

## Verification

1. Forecast farm revenue and compare to actual end-of-season values.
2. Estimate price or input-cost elasticity and interpret economic significance.
3. Compare a DSS recommendation to historical farmer practice in a pilot region.

## References

- https://www.annualreviews.org/content/journals/10.1146/annurev-resource-101623-092515
- https://doi.org/10.1007/s44279-026-00510-w
- https://doi.org/10.62486/latia2025326
- https://baylislab.ace.illinois.edu/wp-content/uploads/2019/09/Storm-et-al-ML-Review.pdf

## References

- https://www.annualreviews.org/content/journals/10.1146/annurev-resource-101623-092515
- https://doi.org/10.1007/s44279-026-00510-w
- https://doi.org/10.62486/latia2025326
- https://baylislab.ace.illinois.edu/wp-content/uploads/2019/09/Storm-et-al-ML-Review.pdf
