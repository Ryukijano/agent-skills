# AI for Threat Intelligence

## Description

Use machine learning and NLP to extract indicators, attribute threat actors, build knowledge graphs, and prioritize cyber-threat intelligence.

## When to use

You are turning large volumes of security reports, logs, and dark-web
sources into structured, actionable intelligence about threats.

## Usage

- Extract and normalize IoCs, TTPs, and MITRE ATT&CK mappings from reports.
- Attribute threat actors from behavioral and artifact similarity.
- Build knowledge graphs for multi-hop reasoning over CTI.
- Summarize and triage reports, and enrich alerts with risk scoring.

## Steps

1. Collect structured and unstructured threat reports and dark-web sources.
2. Train or run an NER and relationship-extraction model on a labeled corpus.
3. Normalize entities to a shared taxonomy and build a CTI knowledge graph.
4. Validate extraction against a labeled gold set and analyst summaries.
5. Integrate low-confidence triage with analyst-in-the-loop attribution.

## Code pattern

```python
import spacy

# Extract named entities from a threat report
nlp = spacy.load("en_core_web_sm")
doc = nlp(report_text)
entities = [(ent.text, ent.label_) for ent in doc.ents]
```

## Tuning notes

- Normalize entities to a shared taxonomy for correlation.
- Combine structured and unstructured sources; ground LLM answers in
  retrieved evidence.
- Track data provenance and confidence to avoid circular reporting.
- Automate low-confidence triage but keep analyst-in-the-loop for
  attribution.

## Verification

1. Extract IoCs from a report corpus and compare to a labeled gold set.
2. Build a CTI knowledge graph and answer multi-hop attribution queries.
3. Evaluate an LLM summarization pipeline against analyst summaries.

## References

- https://arxiv.org/abs/2604.11419v1
- https://link.springer.com/article/10.1007/s10462-025-11338-z
- https://arxiv.org/abs/2603.05068v1
- https://arxiv.org/abs/2511.01144v1
- https://attack.mitre.org/
