# AI for Oral History

## Description

Use AI to transcribe, index, search, or analyze recorded oral history interviews and testimonies.

## When to use

You are transcribing, indexing, searching, or analyzing recorded oral history interviews and testimonies.

## Usage

- Transcribe, diarize, and timestamp interviews.
- Index themes, events, and named entities.
- Link testimonies to archival and geospatial context.
- Respect consent and community access protocols.

## Steps

1. Transcribe, diarize, and timestamp interviews.
2. Index themes, events, and named entities.
3. Link testimonies to archival and geospatial context.
4. Respect consent and community access protocols.
5. Return transcripts to narrators for correction.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
import whisper

# Transcribe an oral history interview
model = whisper.load_model("base")
result = model.transcribe("interview.wav", language="en")
print(result["text"])
```

## Tuning notes

- Oral history audio is often noisy, accented, or overlapping; fine-tune ASR when possible.
- Preserve authenticity; clearly distinguish transcript, AI-generated metadata, and human annotation.
- Use chronological, not random, splits to evaluate ASR on temporal data drift.

## Verification

1. Transcribe a sample of interviews and compute word error rate against a human transcript.
2. Build a topic search over testimonies and evaluate retrieval relevance with historians.
3. Generate navigational questions for an interview and validate relevance and semantic continuity.

## References

- https://doi.org/10.18267/j.aip.268
- https://aclanthology.org/2024.htres-1.6.pdf
- https://www.emerald.com/insight/content/doi/10.1108/el-12-2023-0303/full/html
- https://www.isca-archive.org/interspeech_2023/svec23_interspeech.pdf
- https://www.isca-archive.org/interspeech_2023/lehecka23_interspeech.html
