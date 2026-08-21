# AI for Ocean Conservation

## Description

Use AI to monitor marine protected areas, detect illegal fishing, tracking vessels, or assess marine ecosystem health.

## When to use

You are monitoring marine protected areas, detecting illegal fishing, tracking vessels, or assessing marine ecosystem health.

## Usage

- Fuse AIS, SAR, and optical vessel data.
- Classify fishing vs. non-fishing behavior.
- Detect anomalous vessel activity in MPAs.
- Map marine habitats and species.

## Steps

1. Fuse AIS, SAR, and optical vessel data.
2. Classify fishing vs. non-fishing behavior.
3. Detect anomalous vessel activity in MPAs.
4. Map marine habitats and species.
5. Validate with patrol records and eDNA surveys.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
