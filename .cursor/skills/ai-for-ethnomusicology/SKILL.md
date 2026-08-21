# AI for Ethnomusicology

## Description

Use AI to analyze archival field recordings, microtonal traditions, regional vocal styles, or cross-cultural musical patterns in ethnomusicological research.

## When to use

You are analyzing archival field recordings, microtonal traditions, regional vocal styles, or cross-cultural musical patterns in ethnomusicological research.

## Usage

- Transcribe field recordings and encode scales and rhythms.
- Segment and classify instrument, vocal, and genre features.
- Map musical patterns across regions and communities.
- Annotate with performer, context, and consent metadata.

## Steps

1. Transcribe field recordings and encode scales and rhythms.
2. Segment and classify instrument, vocal, and genre features.
3. Map musical patterns across regions and communities.
4. Annotate with performer, context, and consent metadata.
5. Return outputs to source communities for review.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
import librosa
import numpy as np

# Extract pitch contour and compute a pitch-class histogram
y, sr = librosa.load("field_recording.wav")
f0, voiced_flag, _ = librosa.pyin(y, fmin=60, fmax=800, sr=sr)
f0 = f0[voiced_flag]
hist, _ = np.histogram(np.mod(1200 * np.log2(f0 / 440.0), 1200), bins=120, range=(0, 1200))
```

## Tuning notes

- Oral traditions are microtonal and ornamented; avoid assuming 12-tone equal temperament.
- Compensate for pitch drift and slides before building pitch inventories.
- Combine computational results with ethnomusicologist feedback and local expert knowledge.

## Verification

1. Reproduce a published pitch inventory from a field recording and compare to the original study.
2. Cluster recordings by region or style and validate against annotated metadata.
3. Analyze a microtonal vocal tradition and visualize its tuning system.

## References

- https://www.audiolabs-erlangen.de/content/05_fau/professor/00_mueller/03_publications/2023_RosenzweigSM_FuneralSongs_ACM-JOCCH_ePrint.pdf
- https://archives.ismir.net/ismir2023/paper/000052.pdf
- https://arxiv.org/abs/2503.11956v1
- https://doi.org/10.3390/app9030439
- https://real.mtak.hu/190618/1/juhasz-2024-revealing.pdf
