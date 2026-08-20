# AI for Maritime

## Description

AI for maritime autonomous surface ships, route and weather routing optimization, collision avoidance, port logistics, and vessel situational awareness.

## When to use

You are routing ships autonomously, predicting maritime traffic, avoiding collisions, or optimizing port operations and schedules.

## Key concepts

- **Maritime Autonomous Surface Ships (MASS)**: COLREGs-compliant navigation, path planning, and decision-making.
- **Situational awareness**: sensor fusion across AIS, radar, LiDAR, cameras, and GNSS.
- **Route optimization**: weather routing, fuel minimization, and just-in-time arrival.
- **Port and logistics AI**: berth scheduling, cargo handling, and supply-chain synchronization.

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
