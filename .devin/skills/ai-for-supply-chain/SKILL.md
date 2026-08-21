# AI for Supply Chain

## Description

Use ML to forecast demand, optimize inventory, score supplier risk, and improve visibility and resilience across multi-echelon supply chains.

## When to use

You need to forecast demand, plan inventory, detect disruptions, or optimize sourcing and distribution across a multi-echelon supply chain.

## Usage

- Forecast SKU-, store-, and channel-level demand with statistical, ML, or deep-learning models.
- Optimize safety stock, reorder points, and multi-echelon inventory under uncertainty.
- Predict disruptions and score supplier risk with multi-criteria and scenario models.
- Reconcile forecasts hierarchically and integrate IoT, ERP, and EDI data for real-time visibility.

## Steps

1. Ingest historical demand, promotions, external signals, inventory, supplier, and logistics data.
2. Train demand-forecasting models at the right granularity and reconcile them across product, location, and time.
3. Build inventory-optimization models that balance service level, holding cost, and obsolescence under demand uncertainty.
4. Score supplier risk and predict disruptions from financial, geopolitical, weather, and quality signals.
5. Integrate real-time IoT/ERP/EDI feeds and build exception alerts for stockouts, delays, and bottlenecks.
6. Backtest forecasts and inventory policies with rolling origin and measure total landed cost and service level.

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
