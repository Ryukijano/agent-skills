# AI for Disaster Response

## Description

Use multi-modal imagery and ML to assess damage, map situational awareness, plan evacuations, and pre-position supplies during disasters.

## When to use

You are supporting first responders, emergency managers, or humanitarian agencies before, during, or after a natural or human-made disaster.

## Usage

- Analyze satellite, aerial, drone, and social-media imagery for rapid disaster assessment.
- Detect and classify building, road, and infrastructure damage from multi-temporal imagery.
- Build a common operating picture by fusing imagery, sensors, and crowd data into GIS-ready outputs.
- Optimize evacuation routes, shelter assignment, and resource pre-positioning under real-time constraints.

## Steps

1. Collect pre- and post-event satellite, aerial, drone, and social-media imagery and align them to a common CRS.
2. Run a change-detection or damage-segmentation model and classify damage levels (e.g., xBD-style labels).
3. Extract roads, shelters, and critical infrastructure and estimate affected population and needs.
4. Optimize evacuation routes, shelter assignment, and resource pre-positioning with capacity and time constraints.
5. Build a live situational-awareness dashboard that fuses model outputs with field reports and sensor data.
6. Validate damage labels with ground truth and train a lightweight edge model for offline field deployment.

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
