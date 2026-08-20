# AI for Threat Intelligence

## Description

Cyber threat intelligence extraction, attribution, knowledge graphs, and automated indicator analysis with ML and LLMs.

## When to use

You are turning large volumes of security reports, logs, and dark-web
sources into structured, actionable intelligence about threats.

## Key concepts

- **Indicator extraction and normalization**: IoCs, TTPs, and
  MITRE ATT&CK mapping.
- **Threat actor attribution**: behavioral and artifact similarity
  analysis.
- **Knowledge graphs**: entity-relationship models for multi-hop
  reasoning over CTI.
- **Natural language processing**: LLM summarization, question
  answering, and report triage.
- **Prioritization and situational awareness**: risk scoring and
  alert enrichment.

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
