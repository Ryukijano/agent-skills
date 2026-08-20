# AI for Demand Forecasting

## Description

Time-series forecasting, hierarchical and intermittent demand, probabilistic forecasts, and promotion/event effects.

## When to use

You need to predict future demand for products, services, or resources to drive inventory, staffing, production, or pricing decisions.

## Key concepts

- **Statistical baselines**: ARIMA, ETS, Prophet, and Theta for structured seasonality.
- **ML/DL forecasting**: gradient boosting, LSTM, CNN, transformers, and N-BEATS for complex patterns.
- **Hierarchical and intermittent demand**: reconcile forecasts across levels and handle sparse/zero-inflated series.
- **Probabilistic forecasting**: prediction intervals and quantile forecasts for decision-making under uncertainty.

## Code pattern

```python
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA, Naive

sf = StatsForecast(
    df=df,
    models=[AutoARIMA(season_length=12), Naive()],
    freq="M",
    n_jobs=-1,
)
forecasts = sf.forecast(h=12)
```

## Tuning notes

- Match model choice to data frequency, seasonality, and horizon; benchmark against strong baselines.
- For promotions and events, include causal features and avoid future leakage.
- Evaluate with scale-independent metrics (MAPE, RMSSE, M5-style metrics).

## Verification

1. Build a demand forecast and backtest with rolling cross-validation.
2. Compare a tree-based, deep-learning, and statistical model on the same series.
3. Generate prediction intervals and check coverage on a holdout period.

## References

- https://www.mdpi.com/2571-5577/7/5/93
- https://nixtlaverse.nixtla.io/statsforecast/docs/getting-started/getting_started_complete.html
- https://doi.org/10.1016/j.aei.2026.104625
- https://www.sciencedirect.com/science/article/pii/S2212827122004036
