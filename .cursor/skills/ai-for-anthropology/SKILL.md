# AI for Anthropology

## Description

Computational ethnography, NLP for field notes and interviews, multimodal cultural analysis, and AI-assisted thick description and reflexivity.

## When to use

You are conducting ethnographic or qualitative research and want to support transcription, coding, translation, and analysis of field notes, interviews, images, and artifacts.

## Key concepts

- **Computational ethnography**: combine fieldwork with computational text and media analysis.
- **Qualitative coding with AI**: assist open, axial, and thematic coding with embeddings and classifiers.
- **Speech-to-text for oral histories**: transcribe interviews in low-resource languages.
- **Multimodal cultural analysis**: analyze images, video, and material culture with vision models.
- **Reflexivity and positionality**: keep researcher interpretation central and audit AI-assisted claims.

## Code pattern

```python
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

# Embed and cluster field-note passages for thematic discovery
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(df["note"].tolist())
labels = KMeans(n_clusters=6, random_state=42, n_init="auto").fit_predict(embeddings)
df["theme"] = labels
print(df.groupby("theme")["note"].apply(lambda x: " ".join(x.head(3)))
```

## Tuning notes

- Obtain informed consent and protect participant privacy for all field data.
- Work with small, high-context data; generic models may miss local meaning.
- Co-design with communities and reflect on how AI reshapes ethnographic authority.
- Validate AI codes through participant checking and inter-rater agreement.

## Verification

1. Compare AI-generated codes to human-coded excerpts and compute Cohen's kappa.
2. Transcribe a short interview and verify key passages with a native speaker.
3. Cluster field notes and have domain experts interpret the resulting themes.

## References

- https://doi.org/10.1177/20539517231153803
- https://doi.org/10.1177/20539517211069891
- https://www.annualreviews.org/content/journals/10.1146/annurev-anthro-071323-113942
- https://github.com/MattArtzAnthro/ai-anthropology-toolkit
