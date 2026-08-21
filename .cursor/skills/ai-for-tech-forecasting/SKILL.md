# AI for Tech Forecasting

## Description

Use patents, publications, funding, and expert judgment to forecast technological progress and emerging capabilities.

## When to use

You want to predict the pace, direction, or feasibility of technological progress to guide R&D investment, policy, or safety planning.

## Usage

- Collect patents, papers, funding, product releases, and expert surveys.
- Model S-curves, ARIMA, autoencoders, and transformer-based technology trends.
- Discover technological convergence and opportunities with topic and link models.
- Aggregate expert judgment with Delphi and structured elicitation.
- Evaluate forecasts with Brier scores and calibration over horizons.

## Steps

1. Define the technology, metric, and forecasting horizon.
2. Gather historical data (patents, papers, funding, product releases) and expert judgments.
3. Train or fit trend, topic, or link-prediction models.
4. Backtest on held-out time periods and avoid look-ahead bias.
5. Combine model and expert forecasts and report uncertainty scenarios.
6. Update regularly as new signals and events emerge.

## Code pattern

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Simple trend extrapolation of a technology metric
years = np.array([[2015], [2018], [2021], [2024]])
metric = np.array([0.2, 0.4, 0.65, 0.85])  # e.g., capability score

model = LinearRegression().fit(years, metric)
future_years = np.array([[2027], [2030]])
print("Forecasts:", model.predict(future_years))
```

## Tuning notes

- Combine quantitative signals with domain expertise; neither is sufficient alone.
- Distinguish capability trends from adoption and diffusion curves.
- Use holdout time periods and avoid look-ahead bias in feature construction.
- Report uncertainty and scenarios, not just point estimates.

## Verification

1. Build a model to forecast a technology metric and backtest on historical data.
2. Use patent topic modeling to identify emerging technology combinations.
3. Compare an ML forecast to expert elicitation on a set of concrete questions.

## References

- https://arxiv.org/abs/2605.22681
- https://arxiv.org/pdf/2008.01848
- https://arxiv.org/abs/2605.04875
- https://arxiv.org/abs/2211.15334
