# AI for Clinical NLP

## Description

Natural language processing for electronic health records, clinical entity extraction, term normalization, de-identification, and question answering.

## When to use

You are extracting information from clinical notes, building EHR question-answering, normalizing medical terms, or de-identifying protected health information.

## Key concepts

- **Clinical named entity recognition (NER)**: symptoms, medications, diagnoses, procedures, and adverse events.
- **Domain-specific language models**: ClinicalBERT, BioBERT, GatorTron, and clinical LLMs.
- **Entity normalization**: mapping mentions to UMLS, SNOMED-CT, RxNorm, and ICD.
- **De-identification**: removing or surrogates of protected health information (PHI).
- **Clinical corpora and tasks**: MIMIC-III/IV, n2c2, MACCROBAT, and MedNLI.

## Code pattern

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

# Load a clinical NER model
tokenizer = AutoTokenizer.from_pretrained("samrawal/bert-base-uncased_clinical-ner")
model = AutoModelForTokenClassification.from_pretrained("samrawal/bert-base-uncased_clinical-ner")

text = "Patient was prescribed metformin 500 mg for type 2 diabetes."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
```

## Tuning notes

- Use domain-specific tokenizers and vocabularies for clinical abbreviations.
- Handle long documents with sliding windows or hierarchical encoders.
- De-identify notes before model training and external sharing.
- Evaluate with entity-level F1 and normalization accuracy.

## Verification

1. Fine-tune a clinical NER model on the n2c2 or MACCROBAT dataset.
2. Map extracted entities to UMLS/SNOMED-CT and measure F1.
3. Build a pipeline to extract diagnosis-procedure relations from discharge summaries.

## References

- https://doi.org/10.48550/arxiv.1904.05342
- https://mimic.mit.edu/docs/III/
- https://www.nature.com/articles/sdata201635
- https://aclanthology.org/W19-1909/
- https://par.nsf.gov/servlets/purl/10580364
