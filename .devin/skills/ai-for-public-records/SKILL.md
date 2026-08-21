# AI for Public Records

## Description

Classifies, appraises, and redacts born-digital government records to accelerate archival review and public access.

## When to use

You are managing born-digital government records, reducing archival backlogs, or improving public access to official documents.

## Usage

- **Records classification and retention**: assign retention, security, and access labels.
- **Sensitivity review and redaction**: flag personal, classified, or confidential content.
- **Metadata extraction**: identify entities, dates, and topics for search and discovery.
- **Appraisal and selection**: surface historically significant material for transfer.

## Steps

1. Inventory records formats, systems, and retention schedules.
2. Pre-process text, images, audio, and structured data from repositories.
3. Train or apply classifiers for sensitivity, retention, and PII.
4. Route uncertain cases to records professionals for review.
5. Publish approved records with rich metadata and redactions.

## Code pattern

```python
import re

# Detect and redact potential PII in a document
text = "John Doe, SSN 123-45-6789, lives at 123 Main St."
redacted = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[REDACTED]", text)
print(redacted)
```

## Tuning notes

- Keep a human-in-the-loop for final retention and sensitivity decisions.
- Document provenance and model decisions for legal defensibility.
- Balance transparency against privacy and national security.

## Verification

1. Classify a sample of records and compare to archivist labels.
2. Process a backlog and measure throughput and accuracy.
3. Review redaction quality and public access outcomes.

## References

- https://zenodo.org/records/18935870
- https://www.gov.uk/algorithmic-transparency-records/cabinet-office-automated-digital-document-review
- https://www.ukri.org/who-we-are/how-we-are-doing/research-outcomes-and-impact/ahrc/ai-for-accountability-unlocking-uk-digital-records/
- https://link.springer.com/article/10.1007/s00146-025-02221-0
