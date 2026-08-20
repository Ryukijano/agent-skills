# AI for Ocean Conservation

## Description

Marine protected area monitoring, illegal fishing detection, species tracking, and ocean health assessment from satellite and vessel data.

## When to use

You are monitoring marine protected areas, detecting illegal fishing, tracking vessels, or assessing marine ecosystem health.

## Key concepts

- **Vessel monitoring**: AIS, VMS, and SAR-based dark-vessel detection.
- **Illegal fishing detection**: behavioral classification and anomaly detection.
- **Marine species and habitat mapping**: cetacean/sea-turtle detection, habitat suitability.
- **MPA performance**: compliance, spillover, and biodiversity indicators.

## Code pattern

```python
from sklearn.ensemble import IsolationForest

# Anomaly detection for fishing vessel behavior from AIS features
clf = IsolationForest(contamination=0.05, random_state=42)
clf.fit(X_ais)
```

## Tuning notes

- Fuse AIS, SAR, and optical imagery to detect vessels without AIS.
- Calibrate anomaly scores by region and gear type.
- Protect sensitive MPA data and respect maritime jurisdictions.
- Validate detections with patrol records and observer reports.

## Verification

1. Classify fishing vs non-fishing behavior and report AUC-ROC.
2. Detect anomalous vessel activity in an MPA and compare to patrol logs.
3. Map marine habitat and validate with survey or eDNA data.

## References

- https://arxiv.org/abs/2312.03207
- https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1798458/full
- https://doi.org/10.1016/j.procs.2026.06.143
- https://allenai.org/skylight
