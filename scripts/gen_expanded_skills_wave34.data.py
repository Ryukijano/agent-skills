SKILLS = [
    {
        "name": "ai-for-cultural-heritage",
        "title": "AI for Cultural Heritage",
        "description": "Machine learning and deep learning for the digitization, documentation, analysis, and sustainable management of tangible and intangible cultural heritage.",
        "devin_body": r'''
## When to use

You are digitizing, analyzing, or preserving cultural heritage assets such as monuments, artifacts, manuscripts, oral traditions, or historic sites.

## Key concepts

- **Heritage digitization**: photogrammetry, laser scanning, 3D reconstruction, and digital twins for tangible and intangible assets.
- **Recognition and classification**: object detection, iconography analysis, and style identification in heritage imagery.
- **Virtual reconstruction and restoration**: AI-driven inpainting, point-cloud completion, and historical scene generation.
- **Monitoring and risk prediction**: time-series forecasting, change detection, and environmental risk modeling for heritage sites.
- **Ethics and provenance**: indigenous data sovereignty, copyright, cultural sensitivity, and transparent AI decision-making.

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
3. Forecast microclimate risk for a heritage building and compare to observed degradation.
''',
        "references": [
            "https://www.mdpi.com/2072-4292/18/4/628",
            "https://www.mdpi.com/2071-1050/17/20/9192",
            "https://www.nature.com/articles/s40494-026-02403-z",
            "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335943",
            "https://link.springer.com/article/10.1007/s10791-026-10049-5",
        ],
    },
    {
        "name": "ai-for-museum-collections",
        "title": "AI for Museum Collections",
        "description": "Computer vision, natural language processing, and metadata enrichment for cataloging, searching, and interpreting museum and archive collections.",
        "devin_body": r'''
## When to use

You need to catalog, tag, search, or interpret large museum, archive, or special-collections datasets combining images, text, and structured metadata.

## Key concepts

- **Automated cataloging**: object detection, image classification, and VLM-generated descriptions for collection records.
- **Semantic enrichment**: entity linking, subject tagging, and knowledge-graph construction from collection metadata.
- **Visual search and retrieval**: similarity search, CLIP-style embeddings, and faceted browsing.
- **Provenance and rights**: copyright, licensing, donor restrictions, and ethical use of AI-generated metadata.

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
3. Extract named entities from catalog text and validate against authority files.
''',
        "references": [
            "https://ai.harvardartmuseums.org/",
            "https://dl.acm.org/doi/10.1145/3446621",
            "https://www.nature.com/articles/s41599-026-08367-6",
            "https://research.edgehill.ac.uk/en/projects/spot-semantic-processing-for-object-tagging-ai-enriched-metadata/",
            "https://enc.hal.science/hal-05217762",
        ],
    },
    {
        "name": "ai-for-ethnomusicology",
        "title": "AI for Ethnomusicology",
        "description": "Computational analysis of field recordings, oral musical traditions, tuning systems, and cross-cultural musical patterns using MIR and machine learning.",
        "devin_body": r'''
## When to use

You are analyzing archival field recordings, microtonal traditions, regional vocal styles, or cross-cultural musical patterns in ethnomusicological research.

## Key concepts

- **Field recording analysis**: pitch extraction, pitch drift compensation, and pitch inventory estimation from oral performances.
- **Tuning and intonation modeling**: pitch histograms, dynamic time warping, and optimization-based tuning-system inference.
- **Corpus comparison**: clustering, dimensionality reduction, and similarity networks across musical cultures.
- **Self-supervised and deep learning**: representation learning from raw audio for folk-music style and region classification.

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
''',
        "references": [
            "https://www.audiolabs-erlangen.de/content/05_fau/professor/00_mueller/03_publications/2023_RosenzweigSM_FuneralSongs_ACM-JOCCH_ePrint.pdf",
            "https://archives.ismir.net/ismir2023/paper/000052.pdf",
            "https://arxiv.org/html/2503.11956v1",
            "https://kadmos.iliauni.edu.ge/index.php/kadmos/article/view/506",
            "https://real.mtak.hu/190618/1/juhasz-2024-revealing.pdf",
        ],
    },
    {
        "name": "ai-for-folklore",
        "title": "AI for Folklore",
        "description": "Computational folkloristics, motif and tale-type detection, and large-scale narrative analysis of folk tales, legends, and oral traditions.",
        "devin_body": r'''
## When to use

You are studying folk tales, legends, proverbs, or other vernacular traditions and want to detect motifs, tale types, or narrative structures at scale.

## Key concepts

- **Tale-type and motif indexing**: ATU tale types, Thompson Motif Index, and automated motif extraction.
- **Computational folkloristics**: network analysis, clustering, and distant reading of folklore corpora.
- **LLM-assisted narrative analysis**: prompting, fine-tuning, and evaluating language models on folktale variants.
- **Digital folklore and algorithms**: folk theories of algorithms and the study of folklore on social media platforms.

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
3. Evaluate an LLM's ability to classify tale types in a held-out test set.
''',
        "references": [
            "https://doi.org/10.1093/9780197852712.003.0159",
            "https://doi.org/10.1080/0015587x.2023.2233839",
            "https://cacm.acm.org/research/computational-folkloristics/",
            "https://arxiv.org/pdf/2510.18561",
            "https://www.mdpi.com/2076-0787/14/12/230",
        ],
    },
    {
        "name": "ai-for-mythology",
        "title": "AI for Mythology",
        "description": "Computational mythography, knowledge graphs of mythological figures, structural analysis of myths, and cross-cultural narrative comparison.",
        "devin_body": r'''
## When to use

You are modeling mythological narratives, building knowledge graphs of mythic figures, or comparing structural patterns across world mythologies.

## Key concepts

- **Mythological knowledge graphs**: structured representations of characters, events, objects, and relationships in myths.
- **Structural analysis**: Levi-Straussian transformations, narrative oppositions, and formal models of mythic variation.
- **Entity and allusion detection**: LLM-based annotation of mythological references in literary and historical texts.
- **Cross-cultural comparison**: schema induction and network analysis to compare creation myths and pantheons.

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
3. Compare creation-myth schemas across cultures using a shared schema framework.
''',
        "references": [
            "https://doi.org/10.5281/zenodo.20253116",
            "https://arxiv.org/html/2601.15078v1",
            "https://doi.org/10.48550/arxiv.2412.18270",
            "https://kgeographer.org/glos_creation_schema.html",
            "https://doi.org/10.1177/20539517211037862",
        ],
    },
    {
        "name": "ai-for-literary-studies",
        "title": "AI for Literary Studies",
        "description": "Computational stylistics, authorship attribution, genre and style analysis, and interpretive NLP for literary texts and corpora.",
        "devin_body": r'''
## When to use

You are analyzing style, genre, authorship, intertextuality, or thematic structures in literary texts and corpora.

## Key concepts

- **Stylometry and computational stylistics**: frequency-based, vector-space, and neural methods for style and authorship.
- **Genre and period classification**: supervised and unsupervised models for literary categorization.
- **Authorship attribution and verification**: Burrows' Delta, embedding-based classifiers, and attribution benchmarks.
- **Interpretive NLP and LLMs**: probing language models for literary style, metaphor, and intertextual allusion.

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
3. Probe an LLM for stylistic features and compare to human-annotated style dimensions.
''',
        "references": [
            "https://txtlab.org/wp-content/uploads/2021/10/Herrmann_Piper_Jacobs_CompStylistics_2021.pdf",
            "https://www.cambridge.org/core/journals/computational-humanities-research/article/looking-for-the-inner-music/558CF901089D78168E83915B0AD9C34C",
            "https://doi.org/10.1057/s41599-025-05986-3",
            "https://aclanthology.org/2025.emnlp-main.1227.pdf",
            "https://www.routledge.com/Computational-Literary-Studies-Theory-and-Methods/Rebora/p/book/9781041059769",
        ],
    },
    {
        "name": "ai-for-art-history",
        "title": "AI for Art History",
        "description": "Computer vision, deep learning, and vision-language models for style classification, iconography, provenance, and quantitative art history.",
        "devin_body": r'''
## When to use

You are classifying art styles, attributing works, analyzing iconography, or studying large-scale visual trends in art history.

## Key concepts

- **Style and period classification**: CNN and VLM-based classification of artistic style, school, and period.
- **Visual similarity and embeddings**: learned representations for catalog navigation and provenance research.
- **Iconography and subject analysis**: object detection, scene graphs, and semantic tagging of artworks.
- **Quantitative art history**: statistical analysis of visual features over time and across cultures.

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
3. Generate iconographic tags for artworks and validate against catalog metadata.
''',
        "references": [
            "https://arxiv.org/html/2603.11024",
            "https://aaai.org/papers/11894-the-shape-of-art-history-in-the-eyes-of-the-machine/",
            "https://doi.org/10.1145/3633454",
            "https://arxiv.org/html/2409.03521",
            "https://link.springer.com/article/10.1140/epjds/s13688-023-00397-3",
        ],
    },
    {
        "name": "ai-for-digital-humanities",
        "title": "AI for Digital Humanities",
        "description": "Machine learning, NLP, and network analysis for historical texts, archives, languages, and multimodal humanities collections.",
        "devin_body": r'''
## When to use

You are working with digitized historical texts, multilingual archives, ancient languages, or multimodal humanities corpora that require scalable computational analysis.

## Key concepts

- **Text mining and NLP for DH**: OCR, spelling normalization, named entity recognition, and semantic search.
- **Historical and ancient languages**: transfer learning, low-resource adaptation, and digitization pipelines for classical and endangered texts.
- **Corpus curation and thematic modeling**: word embeddings, topic models, and expert-in-the-loop curation platforms.
- **Intertextuality and semantic search**: paraphrase detection, passage alignment, and reception studies.

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
3. Fine-tune a language model on a low-resource ancient language and compare to a general baseline.
''',
        "references": [
            "https://arxiv.org/pdf/2307.16217",
            "https://doi.org/10.1007/978-3-030-36599-8_31",
            "https://aclanthology.org/2025.nlp4dh-1.35/",
            "https://aclanthology.org/2026.nlp4dh-1.20/",
            "https://aclanthology.org/anthology-files/pdf/cl/2023.cl-3.5.pdf",
        ],
    },
    {
        "name": "ai-for-oral-history",
        "title": "AI for Oral History",
        "description": "Speech recognition, diarization, natural language processing, and generative AI for transcribing, indexing, and exploring oral history archives.",
        "devin_body": r'''
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
''',
        "references": [
            "https://doi.org/10.18267/j.aip.268",
            "https://aclanthology.org/2024.htres-1.6.pdf",
            "https://www.emerald.com/insight/content/doi/10.1108/el-12-2023-0303/full/html",
            "https://www.isca-archive.org/interspeech_2023/svec23_interspeech.pdf",
            "https://www.isca-archive.org/interspeech_2023/lehecka23_interspeech.html",
        ],
    },
    {
        "name": "ai-for-preservation",
        "title": "AI for Preservation",
        "description": "Predictive monitoring, environmental risk assessment, digital twins, and preventive conservation for built heritage and cultural collections.",
        "devin_body": r'''
## When to use

You need to monitor environmental conditions, predict degradation, prioritize conservation actions, or build digital twins for heritage preservation.

## Key concepts

- **Preventive conservation**: condition-based maintenance, microclimate control, and risk forecasting.
- **IoT and environmental monitoring**: temperature, humidity, vibration, and air-quality sensors for heritage sites.
- **Digital twins for heritage**: dynamic 3D models coupled with sensor data and predictive analytics.
- **Damage detection and risk assessment**: semantic segmentation, structural health monitoring, and spatiotemporal risk mapping.

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
3. Build a digital twin dashboard and validate that alerts align with observed conditions.
''',
        "references": [
            "https://doi.org/10.3390/buildings14123979",
            "https://www.mdpi.com/2220-9964/15/1/1",
            "https://www.nature.com/articles/s40494-025-02038-6",
            "https://link.springer.com/article/10.1007/s12065-024-00959-y",
            "https://doi.org/10.1088/1742-6596/3217/1/012006",
        ],
    },
    {
        "name": "ai-for-restoration",
        "title": "AI for Restoration",
        "description": "Digital inpainting, virtual restoration, style-aware reconstruction, and diffusion models for repairing artworks, murals, and manuscripts.",
        "devin_body": r'''
## When to use

You want to virtually repair damaged paintings, murals, manuscripts, or photographs while preserving artistic style and historical authenticity.

## Key concepts

- **Digital inpainting**: GAN, diffusion, and transformer-based reconstruction of missing or damaged regions.
- **Style-aware restoration**: preserving brushwork, texture, and color palette of the original artwork.
- **Edge and structure guidance**: using sketch or edge priors to maintain structural coherence in murals and paintings.
- **Non-invasive virtual restoration**: generating hypotheses without altering the physical artifact.

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
3. Test a diffusion restoration model on authentic damage and document artifacts.
''',
        "references": [
            "https://www.nature.com/articles/s40494-026-02371-4",
            "https://www.nature.com/articles/s40494-026-02843-7",
            "https://www.nature.com/articles/s40494-024-01391-2",
            "https://doi.org/10.1038/s40494-026-02327-8",
            "https://www.mdpi.com/1424-8220/21/6/2091",
        ],
    },
    {
        "name": "ai-for-heritage-tourism",
        "title": "AI for Heritage Tourism",
        "description": "Recommender systems, itinerary planning, visitor behavior modeling, and personalized cultural heritage experiences for sustainable tourism.",
        "devin_body": r'''
## When to use

You are building personalized heritage itineraries, recommending cultural sites, forecasting visitor flows, or balancing tourism with heritage preservation.

## Key concepts

- **Cultural recommender systems**: collaborative filtering, content-based, and hybrid recommendations for heritage sites.
- **Itinerary and path planning**: route optimization, time constraints, and content-adaptive path recommendation.
- **Visitor behavior modeling**: spatiotemporal forecasting, sequence modeling, and crowd-flow prediction.
- **Sustainable heritage tourism**: balancing visitor experience with site carrying capacity and conservation.

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
3. Forecast visitor arrivals and compare to actual gate counts for a heritage site.
''',
        "references": [
            "https://www.mdpi.com/2504-2289/4/2/12",
            "https://doi.org/10.4018/ijitsa.402196",
            "https://research.unipg.it/handle/11391/1616242",
            "https://doi.org/10.1038/s41598-025-22592-0",
            "http://scholar.uoa.gr/gealexandri/publications/personalized-and-content-adaptive-cultural-heritage-path-recommendation",
        ],
    },
]
