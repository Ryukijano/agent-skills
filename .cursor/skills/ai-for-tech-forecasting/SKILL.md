# AI for Tech Forecasting

## Description

Patent and publication analysis, trend extrapolation, expert elicitation, and ML models for predicting technological progress and emerging AI capabilities.

## When to use

You want to predict the pace, direction, or feasibility of technological progress to guide R&D investment, policy, or safety planning.

## Key concepts

- **Data sources for tech forecasting**: patents, publications, funding, product releases, and expert surveys.
- **Trend and time-series models**: S-curves, ARIMA, autoencoders, and transformer-based predictors.
- **Technological convergence and opportunity discovery**: link prediction and topic modeling on patent/paper graphs.
- **Expert judgement and Delphi methods**: structured elicitation, aggregation, and calibration.
- **Forecast evaluation**: calibration, Brier score, and accuracy over multiple time horizons.

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
