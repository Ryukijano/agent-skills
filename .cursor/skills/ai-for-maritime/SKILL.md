# AI for Maritime

## Description

Use machine learning to route vessels autonomously, avoid collisions, predict traffic, and optimize port logistics and schedules.

## When to use

You are routing ships autonomously, predicting maritime traffic, avoiding collisions, or optimizing port operations and schedules.

## Usage

- Plan COLREGs-aware paths and predict collision risk from AIS and radar.
- Fuse AIS, camera, LiDAR, and GNSS for maritime situational awareness.
- Optimize weather routing, fuel use, and just-in-time arrival.
- Schedule berths, cargo, and supply-chain synchronization.

## Steps

1. Collect and clean AIS tracks, weather forecasts, and port schedules.
2. Train a route-prediction or collision-risk model with historical encounter data.
3. Validate against rule-based CPA and expert maritime assessments.
4. Implement a simulator test for COLREGs give-way behavior.
5. Deploy in a closed loop with human oversight on the bridge.

## Code pattern

```python
import pandas as pd
from sklearn.cluster import DBSCAN

# Cluster vessel AIS tracks to identify common routes
ais = pd.read_csv("ais_tracks.csv")
coords = ais[["lon", "lat", "cog", "sog"]].dropna()
routes = DBSCAN(eps=0.5, min_samples=10).fit_predict(coords)
```

## Tuning notes

- Maritime environments are harsh; ensure robustness to sensor occlusion and adverse weather.
- COLREGs and safety constraints must be encoded in the planning layer, not learned blindly.
- AIS data can be sparse or spoofed; cross-validate with radar/camera.

## Verification

1. Predict collision risk from AIS encounter data and compare to rule-based CPA.
2. Plan a COLREGs-aware trajectory in a simulator and verify give-way behavior.
3. Cluster real vessel tracks and validate route interpretability with maritime experts.

## References

- https://journal.hep.com.cn/jomsaa/EN/10.1007/s11804-023-00367-1
- https://doi.org/10.1017/s0373463326101428
- https://doi.org/10.1109/tits.2020.3023957
- https://doi.org/10.1016/j.oceaneng.2025.121988
