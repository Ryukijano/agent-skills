# AI for Public Transport

## Description

Ridership prediction, service scheduling, bus and rail dispatch optimization, disruption recovery, and multi-modal transit analytics.

## When to use

You are optimizing bus/rail operations, forecasting ridership, planning schedules, or recovering from transit disruptions.

## Usage

- **Ridership forecasting**: predict passenger flows by route, stop, and time.
- **Schedule optimization**: set headways, fleet size, and crew rosters.
- **Disruption recovery**: re-route vehicles and inform passengers in real time.
- **Demand-responsive transit**: match on-demand shuttles with riders.
- **Multi-modal analytics**: integrate feeds from trains, buses, bikeshare, and ride-hail.

## Steps

1. Ingest GTFS, AFC, AVL, and passenger count data.
2. Build forecasting models for short- and medium-term demand.
3. Simulate service scenarios and cost-service trade-offs.
4. Deploy real-time decision support for dispatchers.
5. Evaluate equity across routes and population groups.

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
