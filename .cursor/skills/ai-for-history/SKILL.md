# AI for History

## Description

Use AI for History to transcribe documents, extract entities and events and analyze historical networks.

## When to use

You are working with digitized archives, newspapers, manuscripts, or historical corpora and want to extract, structure, and analyze events, actors, places, and trends over time.


## Usage


- **Handwritten text recognition (HTR) and OCR**: Convert scanned manuscripts and prints into searchable text.
- **Distant reading**: Summarize large corpora through topic models, embeddings, and clustering.
- **Event extraction and entity linking**: Identify people, places, organizations, and events in historical narratives.
- **Temporal knowledge graphs**: Represent historical facts with time-aware relations and provenance.
- **Geospatial and network analysis**: Map trade, migration, correspondence, and conflict networks.

## Steps

1. Collect and prepare scanned manuscripts, newspapers and archival text.
2. Worke with digitized archives.
3. Newspapers.
4. Manuscripts.
5. Validate by runing HTR/OCR on a small manuscript set and compare word error rate to a gold transcript.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

## Code pattern

```python
import pandas as pd
from transformers import pipeline

# Example: historical NER and date extraction with a small fine-tuned model
ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
text = "In March 1848, revolutionaries gathered in Berlin."
for ent in ner(text):
    print(ent["word"], ent["entity_group"])
```


## Tuning notes

- Account for historical spelling variation, abbreviations, and dated language.
- Combine HTR confidence scores with human review for critical sources.
- Link extracted entities to authority files (VIAF, GeoNames, Wikidata).
- Be transparent about digitization and selection biases in archival collections.


## Verification

1. Run HTR/OCR on a small manuscript set and compare word error rate to a gold transcript.
2. Extract a timeline of events from a corpus and cross-check against a reference chronology.
3. Build a historical network and verify that key nodes match known actors.

## References

- https://doi.org/10.3366/ijhac.2026.0361
- https://aclanthology.org/2023.cl-3.5/
- https://www.mdpi.com/2409-9252/2/2/13
- https://doi.org/10.47176/etg.2026.1009
