# AI for Climate Policy

## Description

Extract and classify quantified climate targets from national laws and NDCs to track policy alignment and accountability.

## When to use

You need to analyze, compare, or monitor national climate laws, Nationally Determined Contributions (NDCs), or corporate climate disclosures at scale.

## Usage

- Extract quantified climate targets (net-zero, reduction, renewable) from NDCs, laws, and corporate disclosures.
- Compare NDCs with Voluntary National Reviews (VNRs) and SDGs to score alignment.
- Apply domain-adapted language models such as ClimateBERT to climate-finance and policy text.
- Track policy implementation, theme shifts, and equity implications over time.

## Steps

1. Collect NDCs, national climate laws, VNRs, and corporate climate reports from official registries.
2. Chunk and normalize the documents; use a domain-adapted LM (e.g., ClimateBERT) to classify paragraphs and extract quantified targets.
3. Build an alignment-scoring pipeline that maps commitments to SDGs and NDC objectives.
4. Track climate-finance flows and implementation progress against stated targets across countries and years.
5. Validate extraction and alignment results against expert annotations and produce transparent, auditable tables.
6. Deploy the pipeline as a monitoring dashboard for policy analysts and climate-finance stakeholders.

## Code pattern

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("climatebert/distilroberta-base-climate-s")
model = AutoModelForSequenceClassification.from_pretrained("climatebert/distilroberta-base-climate-s")

text = "We commit to reduce greenhouse gas emissions by 55% by 2030."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
probs = outputs.logits.softmax(dim=-1)
```

## Tuning notes

- Use domain-adapted models (ClimateBERT, climate-nlp) rather than generic BERT for policy/finance text.
- Climate documents are often long and multilingual; chunking and translation may be needed.
- Be transparent about data provenance, temporal validity, and jurisdictional scope.

## Verification

1. Fine-tune a classifier on a labeled climate-policy dataset and evaluate F1.
2. Extract quantified targets from a set of NDCs and compare to human annotations.
3. Run a cross-country alignment analysis between NDCs and SDG reporting.

## References

- https://huggingface.co/climatebert
- https://huggingface.co/ClimatePolicyRadar/national-climate-targets
- https://www.climatepolicyradar.org/latest/using-machine-learning-to-classify-climate-targets
- https://www.nature.com/articles/s41467-024-53956-1
- https://unfccc.int/ttclear/misc_/StaticFiles/gnwoerk_static/tn_meetings/43ef8d5f37e6484ca634479e3b74a3a8/3ee3862a08c84afe971c29f2687a45f1.pdf
