# AI for Land Use

## Description

Maps urban functional zones and monitors land-cover change from remote sensing and multi-source geospatial data.

## When to use

You want to map, monitor, and plan land use; identify functional zones; or support zoning and environmental policy.

## Usage

- **Land-use/land-cover mapping**: use CNNs, vision transformers, and large vision-language models on remote sensing.
- **Functional zone identification**: fuse imagery, POI, building, mobility, and nightlight data.
- **Change detection**: monitor urban expansion, informal settlement, and land conversion.
- **Planning support**: combine neural predictions with planning rules and objectives.

## Steps

1. Define land-use classes and study area.
2. Gather Sentinel-2, SDGSAT-1, OSM, and socio-economic data.
3. Train and validate multi-modal deep learning models.
4. Produce land-use maps and uncertainty estimates.
5. Translate maps into planning dashboards and policy inputs.

## Code pattern

```python
import torch
import torchgeo.models

# Load a pretrained remote-sensing backbone and inspect
model = torchgeo.models.resnet18(weights='sentinel2_all')
print(model)
```

## Tuning notes

- Use multi-scale and multi-temporal inputs.
- Validate against field surveys and official zoning data.
- Address class imbalance and spectral confusion in urban scenes.

## Verification

1. Classify urban land use and compute accuracy and kappa.
2. Identify functional zones in a city and compare to census/POI data.
3. Detect land-use change over a multi-year period.

## References

- https://www.sciencedirect.com/science/article/abs/pii/S0924271626001760
- https://www.frontiersin.org/journals/sustainable-cities/articles/10.3389/frsc.2026.1736773/full
- https://www.mdpi.com/2072-4292/17/6/990
- https://link.springer.com/article/10.1007/s42452-026-08351-4
- https://isprs-archives.copernicus.org/articles/XLVIII-G-2025/1647/2025/isprs-archives-XLVIII-G-2025-1647-2025.pdf
