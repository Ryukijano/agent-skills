# AI for Disaster Response

## Description

Situational awareness, damage assessment, evacuation planning, supply pre-positioning, and multi-modal disaster imagery analysis.

## When to use

You are supporting first responders, emergency managers, or humanitarian agencies before, during, or after a natural or human-made disaster.

## Key concepts

- **Multi-modal disaster imagery**: satellite, aerial, drone (sUAS), and social-media imagery for rapid assessment.
- **Damage and change detection**: segmentation and classification of building, road, and infrastructure damage.
- **Situational awareness and common operating picture**: fuse imagery, sensor, and crowd data into GIS-ready outputs.
- **Evacuation and logistics**: optimize routes, shelter assignment, and resource pre-positioning.
- **Operational constraints**: disconnected environments, real-time deadlines, and heterogeneous data quality.

## Code pattern

```python
import rasterio
from rasterio.plot import show

with rasterio.open("post_disaster.tif") as src:
    rgb = src.read([1, 2, 3])
    transform = src.transform
show(rgb)
```

## Tuning notes

- Models must generalize across resolutions, sensors, and disaster types; domain adaptation is often needed.
- Balance speed and accuracy: lightweight models for field deployment, heavier ones for cloud post-processing.
- Human-in-the-loop validation is critical for high-stakes decisions.

## Verification

1. Train a building-damage classifier on xBD or a sUAS damage dataset and report per-class F1.
2. Run a change-detection pipeline on pre- and post-event satellite imagery.
3. Validate a route-planning tool against real road closures and shelter demand scenarios.

## References

- https://www.pnnl.gov/projects/rapid-analytics-disaster-response
- https://www.jhuapl.edu/sites/default/files/2022-12/AIEnabledSAinDisasterResponse.pdf
- https://www.cmu.edu/ai-sdm/research/research-highlights/bda-rda-models.html
- https://ojs.aaai.org/index.php/AAAI/article/view/41474
