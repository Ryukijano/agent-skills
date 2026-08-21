# AI for Public Transport

## Description

Optimizes transit operations with ridership forecasts, dynamic scheduling, and real-time disruption recovery.

## When to use

You are optimizing bus/rail operations, forecasting ridership, planning schedules, or recovering from transit disruptions.

## Usage

- **Ridership forecasting**: predict passenger flows by route, stop, and time using GTFS, AFC, and weather data.
- **Dynamic headways and scheduling**: adjust frequencies, fleet rosters, and vehicle assignments to match demand and reduce crowding.
- **Disruption recovery**: re-route vehicles and push passenger alerts during incidents and special events.
- **Demand-responsive transit**: match on-demand shuttles with riders and integrate trains, buses, bikeshare, and ride-hail feeds.

## Steps

1. Ingest GTFS, AVL, AFC, and passenger count data.
2. Build short- to medium-term forecasting models with seasonality, weather, and event features.
3. Simulate headway, fleet, and route scenarios against cost and service targets.
4. Deploy real-time decision support for dispatchers and operations centers.
5. Backtest forecasts and measure on-time performance, crowding, and equity.

## Code pattern

```python
import pandas as pd
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA

# Forecast daily ridership by route
sf = StatsForecast(df=df, models=[AutoARIMA(season_length=7)], freq="D", n_jobs=-1)
fcst = sf.forecast(h=14)
print(fcst.head())
```

## Tuning notes

- Account for special events, weather, and disruptions.
- Use hierarchical reconciliation across routes and stops.
- Balance efficiency, accessibility, and coverage.

## Verification

1. Backtest ridership forecasts against actuals.
2. Compare optimized schedules to current headways using a simulator.
3. Measure on-time performance and rider satisfaction.

## References

- https://www.mdpi.com/2624-6511/8/3/87
- https://doi.org/10.1109/tits.2025.3603963
- https://dl.acm.org/doi/10.1109/TITS.2020.3041234
- https://www.mdpi.com/2079-9292/14/12/2359
