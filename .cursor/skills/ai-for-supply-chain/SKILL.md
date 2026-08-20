# AI for Supply Chain

## Description

Demand forecasting, inventory optimization, risk and resilience, supplier analytics, and end-to-end supply chain visibility.

## When to use

You need to forecast demand, plan inventory, detect disruptions, or optimize sourcing and distribution across a multi-echelon supply chain.

## Key concepts

- **Demand forecasting**: statistical, ML, and deep-learning models for SKU-, store-, and channel-level demand.
- **Inventory optimization**: safety stock, reorder points, and multi-echelon optimization under uncertainty.
- **Resilience and risk**: disruption prediction, supplier risk scoring, and scenario planning.
- **Hierarchical forecasting**: reconcile forecasts across product, location, and time hierarchies.
- **Real-time visibility**: IoT, ERP, and EDI data integration for end-to-end tracking.

## Code pattern

```python
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA
import pandas as pd

df = pd.read_csv("demand_history.csv")  # columns: unique_id, ds, y
sf = StatsForecast(models=[AutoARIMA(season_length=52)], freq="W")
sf.fit(df)
fcst = sf.predict(h=8, level=[90])
```

## Tuning notes

- Include promotion, calendar, and external shock features (holidays, weather, macro indicators).
- Use hierarchical reconciliation to keep forecasts consistent across levels.
- Balance service level, holding cost, and obsolescence in inventory decisions.

## Verification

1. Backtest demand forecasts with rolling origin and report MAE, RMSE, and bias.
2. Simulate an inventory policy under stochastic demand and compare service level and cost.
3. Identify and rank suppliers by risk using a multi-criteria scoring model.

## References

- https://www.mdpi.com/2571-5577/7/5/93
- https://hbr.org/2024/03/how-machine-learning-will-transform-supply-chain-management
- https://www.mdpi.com/2305-6290/8/4/111
- https://doi.org/10.1109/access.2024.3507161
