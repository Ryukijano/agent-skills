SKILLS = [
    {
        "name": 'ai-for-cultural-heritage',
        "title": 'AI for Cultural Heritage',
        "description": 'Transcribe and restore damaged manuscripts and inscriptions with OCR and lacuna filling to make fragile heritage accessible.',
        "devin_body": r'''## When to use

You are digitizing, analyzing, or preserving cultural heritage assets such as monuments, artifacts, manuscripts, oral traditions, or historic sites.

## Usage

- Digitize, annotate, and segment heritage assets.
- Extract and link entities, provenance, and temporal metadata.
- Reconstruct damaged or missing regions with inpainting.
- Build knowledge graphs and digital twins.

## Steps

1. Digitize, annotate, and segment heritage assets.
2. Extract and link entities, provenance, and temporal metadata.
3. Reconstruct damaged or missing regions with inpainting.
4. Build knowledge graphs and digital twins.
5. Validate with domain experts and authority files.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
import open3d as o3d
from sklearn.ensemble import IsolationForest

# Load a heritage 3D point cloud and detect anomalous structural regions
pcd = o3d.io.read_point_cloud("heritage_site.ply")
points = np.asarray(pcd.points)
outliers = IsolationForest(contamination=0.05, random_state=42).fit_predict(points)
pcd.colors = o3d.utility.Vector3dVector([
    [1, 0, 0] if x == -1 else [0.7, 0.7, 0.7] for x in outliers
])
```

## Tuning notes

- Heritage data is often scarce and imbalanced; combine domain priors with data augmentation.
- Validate 3D reconstructions against measured ground truth and expert connoisseurship.
- Address bias and provenance in training data, especially for indigenous or contested heritage.

## Verification

1. Digitize a small artifact and compare the 3D model to manual measurements.
2. Train an object classifier on a heritage image corpus and report per-class precision/recall.
3. Forecast microclimate risk for a heritage building and compare to observed degradation.''',
        "references": [
            'https://www.mdpi.com/2072-4292/18/4/628',
            'https://www.mdpi.com/2071-1050/17/20/9192',
            'https://www.nature.com/articles/s40494-026-02403-z',
            'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335943',
            'https://link.springer.com/article/10.1007/s10791-026-10049-5',
        ],
    },
    {
        "name": 'ai-for-museum-collections',
        "title": 'AI for Museum Collections',
        "description": 'Enrich collection records by auto-tagging objects, linking entities to knowledge graphs, and generating searchable descriptions.',
        "devin_body": r'''## When to use

You need to catalog, tag, search, or interpret large museum, archive, or special-collections datasets combining images, text, and structured metadata.

## Usage

- Transcribe, classify, and link catalog cards and accession records.
- Detect forgeries, damage, and conservation needs.
- Recommend storage, handling, and display conditions.
- Enrich provenance and rights metadata.

## Steps

1. Transcribe, classify, and link catalog cards and accession records.
2. Detect forgeries, damage, and conservation needs.
3. Recommend storage, handling, and display conditions.
4. Enrich provenance and rights metadata.
5. Validate against museum standards and curators.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
from transformers import CLIPProcessor, CLIPModel
from PIL import Image

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

image = Image.open("artwork.jpg")
inputs = processor(text=["portrait", "landscape", "still life"], images=image, return_tensors="pt", padding=True)
outputs = model(**inputs)
probs = outputs.logits_per_image.softmax(dim=1)
```

## Tuning notes

- Museum collections are highly heterogeneous; fine-tune or few-shot adapt models to domain vocabularies.
- Combine AI-generated tags with curator review to avoid hallucinations and misattributions.
- Evaluate retrieval with human-relevant metrics such as nDCG and expert relevance judgments.

## Verification

1. Generate tags for a collection subset and measure curator agreement.
2. Build a semantic image search and compare recall to a keyword baseline.
3. Extract named entities from catalog text and validate against authority files.''',
        "references": [
            'https://ai.harvardartmuseums.org/',
            'https://dl.acm.org/doi/10.1145/3446621',
            'https://www.nature.com/articles/s41599-026-08367-6',
            'https://research.edgehill.ac.uk/en/publications/ai-in-the-curators-loop-designing-transparent-and-trustworthy-met/',
            'https://enc.hal.science/hal-05217762',
        ],
    },
    {
        "name": 'ai-for-ethnomusicology',
        "title": 'AI for Ethnomusicology',
        "description": 'Use AI to analyze archival field recordings, microtonal traditions, regional vocal styles, or cross-cultural musical patterns in ethnomusicological research.',
        "devin_body": r'''## When to use

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
3. Analyze a microtonal vocal tradition and visualize its tuning system.''',
        "references": [
            'https://www.audiolabs-erlangen.de/content/05_fau/professor/00_mueller/03_publications/2023_RosenzweigSM_FuneralSongs_ACM-JOCCH_ePrint.pdf',
            'https://archives.ismir.net/ismir2023/paper/000052.pdf',
            'https://arxiv.org/abs/2503.11956v1',
            'https://doi.org/10.3390/app9030439',
            'https://real.mtak.hu/190618/1/juhasz-2024-revealing.pdf',
        ],
    },
    {
        "name": 'ai-for-folklore',
        "title": 'AI for Folklore',
        "description": 'Classify folk-tale motifs and tale types across multilingual corpora to compare narrative traditions and cultural diffusion.',
        "devin_body": r'''## When to use

You are studying folk tales, legends, proverbs, or other vernacular traditions and want to detect motifs, tale types, or narrative structures at scale.

## Usage

- Collect and transcribe oral narratives and texts.
- Classify tale types and motifs (ATU/Thompson).
- Map geographic and temporal diffusion.
- Generate variants and synthetic examples.

## Steps

1. Collect and transcribe oral narratives and texts.
2. Classify tale types and motifs (ATU/Thompson).
3. Map geographic and temporal diffusion.
4. Generate variants and synthetic examples.
5. Validate against archival sources and storytellers.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Cluster a corpus of folktale variants by motif content
vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
X = vectorizer.fit_transform(tale_texts)
clusters = KMeans(n_clusters=8, random_state=42, n_init="auto").fit_predict(X)
```

## Tuning notes

- Folklore variants are culturally specific; avoid flattening regional and historical nuance.
- Validate motif extraction against expert-annotated samples.
- Use multilingual models and cross-lingual alignment for comparative studies.

## Verification

1. Extract motifs from a set of Cinderella variants and compare to the ATU index.
2. Cluster tales by narrative similarity and interpret the resulting groups.
3. Evaluate an LLM's ability to classify tale types in a held-out test set.''',
        "references": [
            'https://doi.org/10.1093/9780197852712.003.0159',
            'https://doi.org/10.1080/0015587x.2023.2233839',
            'https://cacm.acm.org/research/computational-folkloristics/',
            'https://arxiv.org/pdf/2510.18561',
            'https://www.mdpi.com/2076-0787/14/12/230',
        ],
    },
    {
        "name": 'ai-for-mythology',
        "title": 'AI for Mythology',
        "description": 'Use AI to model mythological narratives, build knowledge graphs of mythic figures, or compare structural patterns across world mythologies.',
        "devin_body": r'''## When to use

You are modeling mythological narratives, building knowledge graphs of mythic figures, or comparing structural patterns across world mythologies.

## Usage

- Build structured myth databases (characters, events, motifs).
- Align myths across cultures and language families.
- Map narrative networks and archetypes.
- Generate comparative analyses.

## Steps

1. Build structured myth databases (characters, events, motifs).
2. Align myths across cultures and language families.
3. Map narrative networks and archetypes.
4. Generate comparative analyses.
5. Cite primary sources and mythographers.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
import networkx as nx

# Build and query a simple mythological knowledge graph
G = nx.DiGraph()
G.add_edge("Zeus", "Hera", relation="sibling_spouse")
G.add_edge("Zeus", "Athena", relation="parent_child")
print(list(nx.descendants(G, "Zeus")))
```

## Tuning notes

- Mythologies are interpretively rich; encode scholarly sources and uncertainty in the knowledge graph.
- Be cautious with LLM hallucinations when extracting rare or polysemous mythological entities.
- Validate structural models against domain experts and comparative mythology scholarship.

## Verification

1. Build a knowledge graph for a pantheon and query family and conflict relations.
2. Extract mythological allusions from a literary corpus and evaluate precision/recall.
3. Compare creation-myth schemas across cultures using a shared schema framework.''',
        "references": [
            'https://doi.org/10.5281/zenodo.20253116',
            'https://arxiv.org/abs/2601.15078v1',
            'https://doi.org/10.48550/arxiv.2412.18270',
            'https://kgeographer.org/glos_creation_schema.html',
            'https://doi.org/10.1177/20539517211037862',
        ],
    },
    {
        "name": 'ai-for-literary-studies',
        "title": 'AI for Literary Studies',
        "description": 'Attribute authorship and detect stylistic patterns across literary corpora to study genre, influence, and intertextuality.',
        "devin_body": r'''## When to use

You are analyzing style, genre, authorship, intertextuality, or thematic structures in literary texts and corpora.

## Usage

- OCR/segment texts, paratext, and marginalia.
- Identify style, authorship, intertextuality, and themes.
- Create annotated editions and linked data.
- Model narrative structures and character networks.

## Steps

1. OCR/segment texts, paratext, and marginalia.
2. Identify style, authorship, intertextuality, and themes.
3. Create annotated editions and linked data.
4. Model narrative structures and character networks.
5. Validate with literary scholars and primary sources.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Simple authorship attribution from most-frequent-word features
vectorizer = TfidfVectorizer(max_features=500, ngram_range=(1, 2))
X = vectorizer.fit_transform(corpus)
model = MultinomialNB().fit(X, authors)
```

## Tuning notes

- Use closed-vocabulary features for stylometry to reduce content leakage into style signals.
- Compare model predictions with close-reading interpretations and literary theory.
- Watch for anachronism in training corpora and chronological leakage in attribution tasks.

## Verification

1. Attribute authorship on a benchmark corpus and compare to Burrows' Delta.
2. Classify genre or period and inspect the most predictive features.
3. Probe an LLM for stylistic features and compare to human-annotated style dimensions.''',
        "references": [
            'https://txtlab.org/wp-content/uploads/2021/10/Herrmann_Piper_Jacobs_CompStylistics_2021.pdf',
            'https://www.cambridge.org/core/journals/computational-humanities-research/article/looking-for-the-inner-music/558CF901089D78168E83915B0AD9C34C',
            'https://doi.org/10.1057/s41599-025-05986-3',
            'https://aclanthology.org/2025.emnlp-main.1227.pdf',
            'https://www.routledge.com/Computational-Literary-Studies-Theory-and-Methods/Rebora/p/book/9781041059769',
        ],
    },
    {
        "name": 'ai-for-art-history',
        "title": 'AI for Art History',
        "description": 'Use AI to classify art styles, attributing works, analyze iconography, or study large-scale visual trends in art history.',
        "devin_body": r'''## When to use

You are classifying art styles, attributing works, analyzing iconography, or studying large-scale visual trends in art history.

## Usage

- Digitize, color-correct, and segment artworks.
- Classify style, artist, provenance, and iconography.
- Compare visual features across collections.
- Detect forgeries and condition issues.

## Steps

1. Digitize, color-correct, and segment artworks.
2. Classify style, artist, provenance, and iconography.
3. Compare visual features across collections.
4. Detect forgeries and condition issues.
5. Ground conclusions in curatorial and conservation records.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image

# Generate a descriptive caption for an artwork using a vision-language model
processor = AutoProcessor.from_pretrained("microsoft/git-base-coco")
model = AutoModelForVision2Seq.from_pretrained("microsoft/git-base-coco")
image = Image.open("painting.jpg")
pixel_values = processor(images=image, return_tensors="pt").pixel_values
generated_ids = model.generate(pixel_values, max_length=50)
caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

## Tuning notes

- Fine-tune models on curated art datasets because natural-image pretraining often misses style-specific cues.
- Combine quantitative findings with art-historical context and archival evidence.
- Evaluate attribution and style models with cross-collection validation to avoid data leakage.

## Verification

1. Train a style classifier on a painting dataset and compare accuracy to art historians.
2. Compute visual-similarity embeddings and verify that nearest neighbors are stylistically related.
3. Generate iconographic tags for artworks and validate against catalog metadata.''',
        "references": [
            'https://arxiv.org/abs/2603.11024',
            'https://aaai.org/papers/11894-the-shape-of-art-history-in-the-eyes-of-the-machine/',
            'https://doi.org/10.1145/3633454',
            'https://arxiv.org/abs/2409.03521',
            'https://link.springer.com/article/10.1140/epjds/s13688-023-00397-3',
        ],
    },
    {
        "name": 'ai-for-digital-humanities',
        "title": 'AI for Digital Humanities',
        "description": 'Use AI to work with digitized historical texts, multilingual archives, ancient languages, or multimodal humanities corpora that require scalable computational analysis.',
        "devin_body": r'''## When to use

You are working with digitized historical texts, multilingual archives, ancient languages, or multimodal humanities corpora that require scalable computational analysis.

## Usage

- Ingest text, image, audio, and structured data.
- Apply OCR, NER, topic modeling, and stylometry.
- Build searchable, linked digital editions.
- Visualize patterns and networks.

## Steps

1. Ingest text, image, audio, and structured data.
2. Apply OCR, NER, topic modeling, and stylometry.
3. Build searchable, linked digital editions.
4. Visualize patterns and networks.
5. Publish FAIR data with provenance and source citation.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
from transformers import pipeline

# Named-entity recognition on a historical text
ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
entities = ner("Dr. Livingstone explored the Zambezi river in 1855.")
```

## Tuning notes

- Historical language is non-standard; use domain-adapted models or fine-tune on period corpora.
- OCR errors propagate downstream; add post-correction and confidence filtering.
- Interpretability and transparency matter; document model choices and limitations for humanities scholars.

## Verification

1. Run OCR on a historical page and measure character/word error rate.
2. Build a semantic search index for a historical corpus and evaluate retrieval relevance.
3. Fine-tune a language model on a low-resource ancient language and compare to a general baseline.''',
        "references": [
            'https://arxiv.org/pdf/2307.16217',
            'https://doi.org/10.1007/978-3-030-36599-8_31',
            'https://aclanthology.org/2025.nlp4dh-1.35/',
            'https://aclanthology.org/2026.nlp4dh-1.20/',
            'https://aclanthology.org/anthology-files/pdf/cl/2023.cl-3.5.pdf',
        ],
    },
    {
        "name": 'ai-for-oral-history',
        "title": 'AI for Oral History',
        "description": 'Use AI to transcribe, index, search, or analyze recorded oral history interviews and testimonies.',
        "devin_body": r'''## When to use

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
3. Generate navigational questions for an interview and validate relevance and semantic continuity.''',
        "references": [
            'https://doi.org/10.18267/j.aip.268',
            'https://aclanthology.org/2024.htres-1.6.pdf',
            'https://www.emerald.com/insight/content/doi/10.1108/el-12-2023-0303/full/html',
            'https://www.isca-archive.org/interspeech_2023/svec23_interspeech.pdf',
            'https://www.isca-archive.org/interspeech_2023/lehecka23_interspeech.html',
        ],
    },
    {
        "name": 'ai-for-preservation',
        "title": 'AI for Preservation',
        "description": 'Use AI to monitor environmental conditions, predict degradation, prioritize conservation actions, or build digital twins for heritage preservation.',
        "devin_body": r'''## When to use

You need to monitor environmental conditions, predict degradation, prioritize conservation actions, or build digital twins for heritage preservation.

## Usage

- Assess environmental and material risk factors.
- Model degradation and pest/disease spread.
- Prioritize preservation actions and budgets.
- Monitor condition changes.

## Steps

1. Assess environmental and material risk factors.
2. Model degradation and pest/disease spread.
3. Prioritize preservation actions and budgets.
4. Monitor condition changes.
5. Calibrate with conservators and preventive-conservation data.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
from sklearn.ensemble import GradientBoostingRegressor

# Predict a preservation risk index from environmental time series
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_risk)
risk_forecast = model.predict(X_future)
```

## Tuning notes

- Heritage systems are slow-moving and data-sparse; use physics-informed features and strong baselines.
- Integrate expert conservation knowledge into model design and alert thresholds.
- Respect intervention constraints; preservation models should support, not replace, conservators.

## Verification

1. Forecast microclimate conditions for a site and compare to sensor readings.
2. Detect damage in building images and map risk zones against expert surveys.
3. Build a digital twin dashboard and validate that alerts align with observed conditions.''',
        "references": [
            'https://doi.org/10.3390/buildings14123979',
            'https://www.mdpi.com/2220-9964/15/1/1',
            'https://www.nature.com/articles/s40494-025-02038-6',
            'https://link.springer.com/article/10.1007/s12065-024-00959-y',
            'https://doi.org/10.1088/1742-6596/3217/1/012006',
        ],
    },
    {
        "name": 'ai-for-restoration',
        "title": 'AI for Restoration',
        "description": 'Use AI to virtually repair damaged paintings, murals, manuscripts, or photographs while preserving artistic style and historical authenticity.',
        "devin_body": r'''## When to use

You want to virtually repair damaged paintings, murals, manuscripts, or photographs while preserving artistic style and historical authenticity.

## Usage

- Document current and historical state with imaging.
- Segment damage and missing regions.
- Inpaint or propose fills consistent with style.
- Simulate treatment effects.

## Steps

1. Document current and historical state with imaging.
2. Segment damage and missing regions.
3. Inpaint or propose fills consistent with style.
4. Simulate treatment effects.
5. Get expert approval before physical intervention.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
from diffusers import StableDiffusionInpaintPipeline
from PIL import Image

# Virtual inpainting of a damaged artwork region (mask provided)
pipe = StableDiffusionInpaintPipeline.from_pretrained("runwayml/stable-diffusion-inpainting")
pipe = pipe.to("cpu")
result = pipe(prompt="traditional Chinese landscape painting", image=image, mask_image=mask).images[0]
```

## Tuning notes

- Restoration datasets are small and domain-specific; fine-tune on heritage-specific corpora.
- Evaluate with both pixel metrics (PSNR/SSIM/LPIPS) and expert visual assessment.
- Avoid over-restoration; preserve damage history and uncertainty where appropriate.

## Verification

1. Inpaint simulated damage on a heritage image and compare to the ground-truth region.
2. Evaluate style consistency of restored areas using perceptual metrics and expert review.
3. Test a diffusion restoration model on authentic damage and document artifacts.''',
        "references": [
            'https://www.nature.com/articles/s40494-026-02371-4',
            'https://www.nature.com/articles/s40494-026-02843-7',
            'https://www.nature.com/articles/s40494-024-01391-2',
            'https://doi.org/10.1038/s40494-026-02327-8',
            'https://www.mdpi.com/1424-8220/21/6/2091',
        ],
    },
    {
        "name": 'ai-for-heritage-tourism',
        "title": 'AI for Heritage Tourism',
        "description": 'Use AI to build personalized heritage itineraries, recommend cultural sites, forecast visitor flows, or balance tourism with heritage preservation.',
        "devin_body": r'''## When to use

You are building personalized heritage itineraries, recommending cultural sites, forecasting visitor flows, or balancing tourism with heritage preservation.

## Usage

- Build multimodal heritage site experiences.
- Personalize tours by interest, mobility, and language.
- Generate AR/VR reconstructions.
- Balance tourism access with conservation limits.

## Steps

1. Build multimodal heritage site experiences.
2. Personalize tours by interest, mobility, and language.
3. Generate AR/VR reconstructions.
4. Balance tourism access with conservation limits.
5. Evaluate visitor learning and satisfaction.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Content-based recommendation of heritage sites by user profile features
knn = NearestNeighbors(n_neighbors=5, metric="cosine")
knn.fit(site_features)
_, indices = knn.kneighbors([user_profile])
recommended_sites = sites.iloc[indices[0]]
```

## Tuning notes

- Tourist preferences are diverse and context-dependent; incorporate time, weather, and accessibility.
- Avoid filter bubbles by mixing popular and lesser-known heritage assets.
- Evaluate recommendations with both offline metrics and on-site visitor satisfaction.

## Verification

1. Build a heritage-site recommender and measure hit rate on a held-out test set.
2. Generate an optimized day itinerary and check feasibility against travel times.
3. Forecast visitor arrivals and compare to actual gate counts for a heritage site.''',
        "references": [
            'https://www.mdpi.com/2504-2289/4/2/12',
            'https://doi.org/10.4018/ijitsa.402196',
            'https://research.unipg.it/handle/11391/1616242',
            'https://doi.org/10.1038/s41598-025-22592-0',
            'http://scholar.uoa.gr/gealexandri/publications/personalized-and-content-adaptive-cultural-heritage-path-recommendation',
        ],
    },
]
