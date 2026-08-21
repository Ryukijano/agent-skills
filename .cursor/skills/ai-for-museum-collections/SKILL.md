# AI for Museum Collections

## Description

Enrich collection records by auto-tagging objects, linking entities to knowledge graphs, and generating searchable descriptions.

## When to use

You need to catalog, tag, search, or interpret large museum, archive, or special-collections datasets combining images, text, and structured metadata.

## Usage

- Transcribe, classify, and link catalog cards and accession records.
- Detect forgeries, damage, and conservation needs.
- Recommend storage, handling, and display conditions.
- Enrich provenance and rights metadata.

## Steps

1. Transcribe, classify, and link catalog cards and accession records.
2. Detect forgeries, damage, and conservation needs.
3. Recommend storage, handling, and display conditions.
4. Enrich provenance and rights metadata.
5. Validate against museum standards and curators.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
from transformers import CLIPProcessor, CLIPModel
from PIL import Image

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

image = Image.open("artwork.jpg")
inputs = processor(text=["portrait", "landscape", "still life"], images=image, return_tensors="pt", padding=True)
outputs = model(**inputs)
probs = outputs.logits_per_image.softmax(dim=1)
```

## Tuning notes

- Museum collections are highly heterogeneous; fine-tune or few-shot adapt models to domain vocabularies.
- Combine AI-generated tags with curator review to avoid hallucinations and misattributions.
- Evaluate retrieval with human-relevant metrics such as nDCG and expert relevance judgments.

## Verification

1. Generate tags for a collection subset and measure curator agreement.
2. Build a semantic image search and compare recall to a keyword baseline.
3. Extract named entities from catalog text and validate against authority files.

## References

- https://ai.harvardartmuseums.org/
- https://dl.acm.org/doi/10.1145/3446621
- https://www.nature.com/articles/s41599-026-08367-6
- https://research.edgehill.ac.uk/en/publications/ai-in-the-curators-loop-designing-transparent-and-trustworthy-met/
- https://enc.hal.science/hal-05217762
