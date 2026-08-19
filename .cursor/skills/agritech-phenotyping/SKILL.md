# Agritech and Plant Phenotyping

## Description

UAV/drone imaging, vision-language models, yield estimation, disease detection, and crop monitoring on GPU.

## When to use

You are applying ML to agriculture: crop yield, disease, pest, or phenotype analysis.

## Key concepts

- **UAV/drone imaging**: RGB, multispectral, hyperspectral, thermal.
- **Phenotyping**: plant height, biomass, head count, disease score.
- **Vision-language models**: PaliGemma, Syngenta Gemma for field reports.
- **Datasets**: PlantVillage, UAV crop datasets, Global Wheat Head Detection.

## Code pattern

```python
from transformers import PaliGemmaForConditionalImageGeneration, PaliGemmaProcessor

model = PaliGemmaForConditionalImageGeneration.from_pretrained("...")
inputs = processor(images=img, text="count wheat heads").to('cuda')
```

## Tuning notes

- Use NDVI and other vegetation indices from multispectral sensors.
- Class imbalance is common; use focal loss or oversampling.
- Georeference outputs for precision agriculture maps.

## Verification

1. Train a wheat head detector and compare F1 to published baselines.
2. Estimate yield for a genotype and compare to harvest measurements.
3. Run inference on drone imagery and visualize disease maps.

## References

- https://link.springer.com/article/10.1007/s11119-026-10371-4
- https://deepmind.google/models/gemma/gemmaverse/syngenta/
- https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1554193/full
