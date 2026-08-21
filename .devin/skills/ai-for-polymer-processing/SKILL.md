# AI for Polymer Processing

## Description

Use machine learning on polymer processing data to predict part quality, detect instabilities, optimize cycle times and reduce scrap.

## When to use

You are running polymer processing equipment and need to set initial operating points, predict part quality, monitor melt quality, detect process instabilities, or optimize energy and material use in extrusion, injection, or blow molding.

## Usage

- **Predict quality**: forecast dimensional, cosmetic, and mechanical properties from process data.
- **Detect instabilities**: identify flow-front, pressure, and temperature excursions.
- **Optimize parameters**: tune injection velocity, pack/hold, cooling, and extruder settings.
- **Monitor extrusion**: predict diameter, thickness, and die swell from in-line sensors.
- **Reduce scrap**: classify and trace defects to root process conditions.

## Steps

1. Install sensors for temperature, pressure, flow, and machine setpoints and log per-shot data.
2. Label quality outcomes and defects from inspection or SPC data.
3. Train regression or classification models to predict part quality or stability.
4. Identify key process parameters with feature importance and DOE validation.
5. Optimize settings with surrogate models and validate on production trials.
6. Deploy a real-time dashboard and controller to flag out-of-control conditions.

## Code pattern

```python
import pandas as pd
from sklearn.neural_network import MLPRegressor

# Predict part weight and warpage from molding settings
X = df[["melt_temp_C", "mold_temp_C", "injection_speed_mm_s", "packing_pressure_MPa", "cooling_time_s"]]
y = df[["part_weight_g", "warpage_mm"]]
model = MLPRegressor(hidden_layer_sizes=(64, 64), random_state=42, max_iter=2000).fit(X, y)
```

## Tuning notes

- Recycled polymers have variable properties; include rheology or MFI features where possible.
- Batch effects and machine differences are common; use domain adaptation or per-machine models.
- Optimize with simulation data but validate on real parts with DOE.
- Time-series process signatures need windowing and trend removal.

## Verification

1. Predict part quality metrics from machine settings and compare to measured dimensions.
2. Recommend initial screw speed and back pressure for a target plasticizing time.
3. Detect a short-shot or flash condition from pressure traces and confirm with part inspection.

## References

- https://doi.org/10.3390/polym12061306
- https://www.mdpi.com/2073-4360/13/16/2652
- https://www.mdpi.com/2073-4360/16/16/2247
- https://doi.org/10.1039/d5fd00066a
- https://www.mdpi.com/2073-4360/17/7/940
