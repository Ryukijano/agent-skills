# AI for Art History

## Description

Computer vision, deep learning, and vision-language models for style classification, iconography, provenance, and quantitative art history.

## When to use

You are classifying art styles, attributing works, analyzing iconography, or studying large-scale visual trends in art history.

## Key concepts

- **Style and period classification**: CNN and VLM-based classification of artistic style, school, and period.
- **Visual similarity and embeddings**: learned representations for catalog navigation and provenance research.
- **Iconography and subject analysis**: object detection, scene graphs, and semantic tagging of artworks.
- **Quantitative art history**: statistical analysis of visual features over time and across cultures.

## Code pattern

```python
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image

# Generate a descriptive caption for an artwork using a vision-language model
processor = AutoProcessor.from_pretrained("microsoft/git-base-coco")
model = AutoModelForVision2Seq.from_pretrained("microsoft/git-base-coco")
image = Image.open("painting.jpg")
pixel_values = processor(images=image, return_tensors="pt").pixel_values
generated_ids = model.generate(pixel_values, max_length=50)
caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

## Tuning notes

- Fine-tune models on curated art datasets because natural-image pretraining often misses style-specific cues.
- Combine quantitative findings with art-historical context and archival evidence.
- Evaluate attribution and style models with cross-collection validation to avoid data leakage.

## Verification

1. Train a style classifier on a painting dataset and compare accuracy to art historians.
2. Compute visual-similarity embeddings and verify that nearest neighbors are stylistically related.
3. Generate iconographic tags for artworks and validate against catalog metadata.

## References

- https://arxiv.org/html/2603.11024
- https://aaai.org/papers/11894-the-shape-of-art-history-in-the-eyes-of-the-machine/
- https://doi.org/10.1145/3633454
- https://arxiv.org/html/2409.03521
- https://link.springer.com/article/10.1140/epjds/s13688-023-00397-3
