# AI for Pathology

## Description

Computational pathology, whole-slide image analysis, cancer subtyping, biomarker discovery, and vision-language models for histopathology.

## When to use

You are analyzing whole-slide images (WSIs), grading tumors, predicting molecular biomarkers, or building AI-assisted pathology workflows.

## Key concepts

- **WSI tiling and patch sampling**: gigapixel images are processed as small patches because full slides do not fit in GPU memory.
- **Multiple instance learning (MIL)**: train on slide-level labels when pixel annotations are scarce.
- **Foundation and vision-language models**: pathology FMs (UNI, CONCH, PathChat) enable few-shot and multimodal analysis.
- **Cancer subtyping and biomarkers**: predict tumor origin, grade, prognosis, and therapy response from H&E slides.
- **Domain shift and stain normalization**: scanners, staining, and labs introduce significant batch effects.

## Code pattern

```python
import openslide
import torch
from torch.utils.data import DataLoader

# Open a WSI and extract a patch
slide = openslide.OpenSlide("tissue.svs")
patch = slide.read_region((10000, 10000), 0, (256, 256)).convert("RGB")

# Typical pipeline: tiles -> feature encoder -> aggregator (MIL/Transformer)
tensor = torch.from_numpy(np.array(patch)).permute(2, 0, 1).unsqueeze(0).float() / 255.0
```

## Tuning notes

- Normalize for staining and scanner differences (Macenko, Vahadane, or learned stain transfer).
- Use weak or noisy labels and bag-level losses for MIL.
- Evaluate with pathologist concordance and external test sets.
- Balance across tissue types and cancer grades.

## Verification

1. Train a MIL classifier on WSI patches and compare to pathologist grading.
2. Apply stain normalization and measure domain-shift robustness.
3. Extract attention heatmaps and validate against pathologist annotations.

## References

- https://doi.org/10.1016/j.csbj.2024.12.033
- https://arxiv.org/abs/2401.06148
- https://arxiv.org/abs/2408.14496v1
- https://www.sciencedirect.com/science/article/pii/S0895611124000144
- https://link.springer.com/article/10.1007/s00424-024-03002-2
