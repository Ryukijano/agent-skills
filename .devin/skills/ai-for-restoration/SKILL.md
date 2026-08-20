# AI for Restoration

## Description

Digital inpainting, virtual restoration, style-aware reconstruction, and diffusion models for repairing artworks, murals, and manuscripts.

## When to use

You want to virtually repair damaged paintings, murals, manuscripts, or photographs while preserving artistic style and historical authenticity.

## Key concepts

- **Digital inpainting**: GAN, diffusion, and transformer-based reconstruction of missing or damaged regions.
- **Style-aware restoration**: preserving brushwork, texture, and color palette of the original artwork.
- **Edge and structure guidance**: using sketch or edge priors to maintain structural coherence in murals and paintings.
- **Non-invasive virtual restoration**: generating hypotheses without altering the physical artifact.

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
