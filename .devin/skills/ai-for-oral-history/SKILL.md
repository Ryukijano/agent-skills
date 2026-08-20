# AI for Oral History

## Description

Speech recognition, diarization, natural language processing, and generative AI for transcribing, indexing, and exploring oral history archives.

## When to use

You are transcribing, indexing, searching, or analyzing recorded oral history interviews and testimonies.

## Key concepts

- **Automatic speech recognition for oral history**: Whisper, wav2vec, and domain-adapted ASR for noisy, dialectal, and aging recordings.
- **Speaker diarization and punctuation**: segmenting speakers and restoring sentence boundaries for readability.
- **Question generation and semantic search**: generating navigable questions and retrieving testimony passages by topic.
- **Narrative and sentiment analysis**: topic modeling, keyword extraction, and emotion detection in survivor and witness narratives.

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
