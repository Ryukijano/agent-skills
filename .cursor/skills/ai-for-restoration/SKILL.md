# AI for Restoration

## Description

Use AI to virtually repair damaged paintings, murals, manuscripts, or photographs while preserving artistic style and historical authenticity.

## When to use

You want to virtually repair damaged paintings, murals, manuscripts, or photographs while preserving artistic style and historical authenticity.

## Usage

- Document current and historical state with imaging.
- Segment damage and missing regions.
- Inpaint or propose fills consistent with style.
- Simulate treatment effects.

## Steps

1. Document current and historical state with imaging.
2. Segment damage and missing regions.
3. Inpaint or propose fills consistent with style.
4. Simulate treatment effects.
5. Get expert approval before physical intervention.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
from diffusers import StableDiffusionInpaintPipeline
from PIL import Image

# Virtual inpainting of a damaged artwork region (mask provided)
pipe = StableDiffusionInpaintPipeline.from_pretrained("runwayml/stable-diffusion-inpainting")
pipe = pipe.to("cpu")
result = pipe(prompt="traditional Chinese landscape painting", image=image, mask_image=mask).images[0]
```

## Tuning notes

- Restoration datasets are small and domain-specific; fine-tune on heritage-specific corpora.
- Evaluate with both pixel metrics (PSNR/SSIM/LPIPS) and expert visual assessment.
- Avoid over-restoration; preserve damage history and uncertainty where appropriate.

## Verification

1. Inpaint simulated damage on a heritage image and compare to the ground-truth region.
2. Evaluate style consistency of restored areas using perceptual metrics and expert review.
3. Test a diffusion restoration model on authentic damage and document artifacts.

## References

- https://www.nature.com/articles/s40494-026-02371-4
- https://www.nature.com/articles/s40494-026-02843-7
- https://www.nature.com/articles/s40494-024-01391-2
- https://doi.org/10.1038/s40494-026-02327-8
- https://www.mdpi.com/1424-8220/21/6/2091
