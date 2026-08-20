SKILLS = [
    {
        "name": "ai-for-linguistics",
        "title": "AI for Linguistics",
        "description": "Computational linguistics, corpus analysis, morphosyntactic annotation, syntactic parsing, language modeling, and NLP tools for linguistic research.",
        "devin_body": r'''
## When to use

You are studying language structure, change, or use and need to annotate, parse, model, or compare linguistic data at scale.

## Key concepts

- **Corpus linguistics**: analyze frequency, collocation, and distribution in large text collections.
- **Morphosyntactic annotation**: POS tagging, lemmatization, dependency parsing, and universal dependencies.
- **Language modeling**: n-gram, neural, and transformer-based models of syntax and semantics.
- **Historical and comparative linguistics**: phylogenetic language trees, cognate detection, and diachronic corpus analysis.
- **Speech and phonetics**: ASR, forced alignment, and phoneme recognition for spoken language.

## Code pattern

```python
import spacy

# Load a small multilingual or domain-specific pipeline
nlp = spacy.load("en_core_web_sm")
doc = nlp("The quick brown foxes jumped over the lazy dogs.")

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.dep_)
```

## Tuning notes

- Use treebank-specific or Universal Dependencies guidelines consistently.
- For low-resource or historical languages, consider adapters and cross-lingual transfer.
- Evaluate against gold annotations rather than generic accuracy alone.
- Watch for tokenization mismatches between modern and historical orthography.

## Verification

1. Parse a small annotated treebank and compute UAS/LAS against gold dependencies.
2. Compare a fine-tuned tagger to the pretrained pipeline on your target corpus.
3. Train a small language model and measure perplexity on a held-out test set.
''',
        "references": [
            "https://plato.stanford.edu/entries/computational-linguistics/",
            "https://dl.acm.org/doi/10.1145/3605943",
            "https://www.annualreviews.org/content/journals/10.1146/annurev-linguistics-030521-044439",
            "https://onlinelibrary.wiley.com/doi/book/10.1002/9781444324044",
        ],
    },
    {
        "name": "ai-for-history",
        "title": "AI for History",
        "description": "HTR and OCR for historical documents, event extraction, temporal reasoning, geospatial and network analysis, and distant reading for historical research.",
        "devin_body": r'''
## When to use

You are working with digitized archives, newspapers, manuscripts, or historical corpora and want to extract, structure, and analyze events, actors, places, and trends over time.

## Key concepts

- **Handwritten text recognition (HTR) and OCR**: convert scanned manuscripts and prints into searchable text.
- **Distant reading**: summarize large corpora through topic models, embeddings, and clustering.
- **Event extraction and entity linking**: identify people, places, organizations, and events in historical narratives.
- **Temporal knowledge graphs**: represent historical facts with time-aware relations and provenance.
- **Geospatial and network analysis**: map trade, migration, correspondence, and conflict networks.

## Code pattern

```python
import pandas as pd
from transformers import pipeline

# Example: historical NER and date extraction with a small fine-tuned model
ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
text = "In March 1848, revolutionaries gathered in Berlin."
for ent in ner(text):
    print(ent["word"], ent["entity_group"])
```

## Tuning notes

- Account for historical spelling variation, abbreviations, and dated language.
- Combine HTR confidence scores with human review for critical sources.
- Link extracted entities to authority files (VIAF, GeoNames, Wikidata).
- Be transparent about digitization and selection biases in archival collections.

## Verification

1. Run HTR/OCR on a small manuscript set and compare word error rate to a gold transcript.
2. Extract a timeline of events from a corpus and cross-check against a reference chronology.
3. Build a historical network and verify that key nodes match known actors.
''',
        "references": [
            "https://doi.org/10.3366/ijhac.2026.0361",
            "https://aclanthology.org/2023.cl-3.5/",
            "https://www.mdpi.com/2409-9252/2/2/13",
            "https://doi.org/10.47176/etg.2026.1009",
        ],
    },
    {
        "name": "ai-for-philosophy",
        "title": "AI for Philosophy",
        "description": "Computational philosophy, argument mining, automated reasoning, text analysis of philosophical corpora, and LLM-assisted conceptual analysis.",
        "devin_body": r'''
## When to use

You are analyzing philosophical arguments, formalizing reasoning, mining large corpora of philosophical texts, or exploring conceptual spaces with computational tools.

## Key concepts

- **Argument mining**: identify premises, conclusions, and argumentation schemes in text.
- **Automated theorem proving and formal logic**: encode arguments in SAT/SMT or proof assistants.
- **Corpus-based conceptual analysis**: track concepts across canonical texts using embeddings and topic models.
- **Philosophy of AI and mind**: use AI systems as objects of study for agency, consciousness, and reasoning.
- **Computational ethics and normative reasoning**: model dilemmas, value alignment, and preference aggregation.

## Code pattern

```python
from z3 import Solver, Bool, Implies, And, sat

# Encode a simple logical argument and test satisfiability
p = Bool("p")
q = Bool("q")
r = Bool("r")

s = Solver()
s.add(And(Implies(p, q), Implies(q, r), p))
print(s.check())
if s.check() == sat:
    print(s.model())
```

## Tuning notes

- Natural-language arguments are often enthymematic; supply missing premises carefully.
- Distinguish formal validity from interpretive plausibility.
- Use domain-specific embeddings or fine-tuned models for philosophical corpora.
- Engage with human philosophers to validate mined argument structures.

## Verification

1. Mine arguments from a short philosophical text and compare to a human annotation.
2. Prove a simple syllogism in a theorem prover and verify the conclusion.
3. Track a concept (e.g., free will) across texts and inspect nearest-neighbor terms.
''',
        "references": [
            "https://plato.stanford.edu/entries/computational-philosophy/",
            "https://philarchive.org/rec/MLLPOA",
            "https://www.cambridge.org/core/books/cambridge-handbook-of-artificial-intelligence/philosophical-foundations/5C3626F0F8F3A9E4D5148A8DAAB908B1",
            "https://link.springer.com/book/10.1007/978-3-032-10073-3",
        ],
    },
    {
        "name": "ai-for-sociology",
        "title": "AI for Sociology",
        "description": "Computational social science for sociology: text and image classification, survey augmentation, social network analysis, and modeling social inequalities.",
        "devin_body": r'''
## When to use

You are studying social behavior, institutions, or inequalities and want to use large-scale digital data, text, images, and networks to test sociological theories.

## Key concepts

- **Text-as-data**: classify, scale, and topic-model documents to measure social constructs.
- **Social network analysis**: identify communities, influencers, and diffusion patterns.
- **Survey augmentation and imputation**: use ML to handle item nonresponse and improve estimation.
- **Heterogeneity and segmentation**: discover subpopulations with causal forests or clustering.
- **Computational approaches to inequality**: audit algorithms, analyze mobility, and detect disparities.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Example: classify open-ended survey responses by theme
X_train, X_test, y_train, y_test = train_test_split(df["response"], df["theme"], stratify=df["theme"])
vec = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
clf = LogisticRegression(max_iter=1000)
clf.fit(vec.fit_transform(X_train), y_train)
print(clf.score(vec.transform(X_test), y_test))
```

## Tuning notes

- Validate text-based measures against representative surveys when possible.
- Address sampling bias from digital platforms and administrative records.
- Ensure constructs like class, race, and gender are measured with care and theory.
- Use causal inference rather than purely predictive models to support sociological claims.

## Verification

1. Replicate a published text-as-data finding on a new sample.
2. Compare a network-derived community partition to a demographic baseline.
3. Validate a survey-imputation model against a gold-standard subsample.
''',
        "references": [
            "https://www.annualreviews.org/content/journals/10.1146/annurev-soc-073117-041106",
            "https://doi.org/10.1146/annurev-soc-121919-054621",
            "https://journals.sagepub.com/doi/full/10.1177/23780231241259651",
            "https://link.springer.com/article/10.1007/s13278-025-01428-9",
        ],
    },
    {
        "name": "ai-for-anthropology",
        "title": "AI for Anthropology",
        "description": "Computational ethnography, NLP for field notes and interviews, multimodal cultural analysis, and AI-assisted thick description and reflexivity.",
        "devin_body": r'''
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
''',
        "references": [
            "https://doi.org/10.1177/20539517231153803",
            "https://doi.org/10.1177/20539517211069891",
            "https://www.annualreviews.org/content/journals/10.1146/annurev-anthro-071323-113942",
            "https://github.com/MattArtzAnthro/ai-anthropology-toolkit",
        ],
    },
    {
        "name": "ai-for-political-science",
        "title": "AI for Political Science",
        "description": "Text-as-data for politics: manifesto scaling, sentiment and stance detection, legislative and voting analysis, and causal inference for political institutions.",
        "devin_body": r'''
## When to use

You are analyzing political texts, campaigns, legislatures, or public opinion and need to measure ideology, sentiment, stance, or institutional behavior from unstructured data.

## Key concepts

- **Text-as-data in politics**: scale party manifestos, speeches, and social media posts.
- **Stance and sentiment detection**: classify support or opposition toward candidates, issues, and policies.
- **Legislative roll-call and voting**: predict votes, measure polarization, and detect coalitions.
- **Causal inference for institutions**: estimate effects of reforms, campaigns, and policies.
- **Surveys and synthetic populations**: augment or benchmark measures with LLMs and polls.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Supervised stance detection on political text
clf = make_pipeline(CountVectorizer(ngram_range=(1, 2)), MultinomialNB())
clf.fit(train["text"], train["stance"])
predictions = clf.predict(test["text"])
```

## Tuning notes

- Validate classifiers against expert or crowd-coded labels, not just accuracy.
- Account for temporal and partisan drift when deploying models on new election cycles.
- Be cautious about using LLM outputs as data without transparency and validation.
- Use out-of-time and cross-country tests to assess generalizability.

## Verification

1. Replicate a published manifesto scaling result and compare rankings.
2. Build a stance detector and evaluate F1 against expert annotations.
3. Predict roll-call votes and compare to a majority-class baseline.
''',
        "references": [
            "https://doi.org/10.1017/psrm.2024.64",
            "https://www.cambridge.org/core/journals/political-science-research-and-methods/article/toward-a-framework-for-creating-trustworthy-measures-with-supervised-machine-learning-for-text/4DECB1072FB983F991BA84ADB01EAFC4",
            "https://www.cambridge.org/core/journals/political-science-research-and-methods/article/stance-detection-a-practical-guide-to-classifying-political-beliefs-in-text/E227E746BD7D9751526DA0EC2C378787",
            "https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/applications-of-gpt-in-political-science-research-extracting-information-from-unstructured-text/7614D066F380A3751D298C2FF3C74F65",
        ],
    },
    {
        "name": "ai-for-international-relations",
        "title": "AI for International Relations",
        "description": "Conflict forecasting, event data analysis, crisis early warning, treaty and negotiation text mining, and geopolitical risk modeling.",
        "devin_body": r'''
## When to use

You are studying conflict, diplomacy, trade, sanctions, or global governance and want to forecast events, extract information from open-source reports, or model geopolitical networks.

## Key concepts

- **Event data and CAMEO/Phoenix**: code actor-action-target triples from news and reports.
- **Conflict forecasting**: predict civil unrest, armed conflict, and fatalities at country or grid level.
- **Crisis early warning**: combine event counts, economic indicators, and social media for alerts.
- **Treaty and negotiation text mining**: analyze agreements, UN speeches, and diplomatic cables.
- **Geopolitical network and spatial models**: capture alliances, trade dependencies, and neighborhood effects.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit

# Country-month conflict risk classifier from event and structural features
X = df[["past_fatalities", "event_count", "neighbor_conflict", "gdp_growth"]]
y = df["conflict_onset"]

cv = TimeSeriesSplit(n_splits=5)
for train_idx, test_idx in cv.split(X):
    model = RandomForestClassifier(class_weight="balanced", random_state=42)
    model.fit(X.iloc[train_idx], y.iloc[train_idx])
    print(model.score(X.iloc[test_idx], y.iloc[test_idx]))
```

## Tuning notes

- Conflict is rare; use class weights, cost-sensitive learning, and proper rare-event metrics.
- Respect temporal ordering with time-series cross-validation.
- Spatial autocorrelation and diffusion must be modeled explicitly, not ignored.
- Geopolitical models raise ethical and policy stakes; prioritize interpretability and caution.

## Verification

1. Backtest a conflict-forecasting model on out-of-sample country-months.
2. Compare your model to a strong baseline such as a random or lag-only model.
3. Evaluate with proper rare-event metrics (precision-recall, Brier score, CRPS).
''',
        "references": [
            "https://doi.org/10.1093/jeea/jvac025",
            "https://www.cambridge.org/core/journals/data-and-policy/article/promise-of-machine-learning-in-violent-conflict-forecasting/40D559ADA18FF7308915B08956B4E8F3",
            "https://doi.org/10.3389/frai.2022.893875",
            "https://par.nsf.gov/servlets/purl/10376284",
        ],
    },
    {
        "name": "ai-for-public-policy",
        "title": "AI for Public Policy",
        "description": "Causal and predictive policy evaluation, program impact assessment, regulatory text analysis, and equitable resource allocation for government and public administration.",
        "devin_body": r'''
## When to use

You are designing, implementing, or evaluating public programs and need evidence on what works, for whom, and under what conditions.

## Key concepts

- **Causal machine learning for policy**: heterogeneous treatment effects, causal forests, and double/debiased ML.
- **Counterfactual policy evaluation**: synthetic controls, difference-in-differences, and interrupted time series.
- **Predictive analytics for public services**: risk modeling, demand forecasting, and resource allocation.
- **Regulatory and legislative text analysis**: parse rulemaking comments, statutes, and contracts.
- **Equity and accountability**: audit for disparate impact and ensure explainability.

## Code pattern

```python
from econml.dml import LinearDML
from sklearn.ensemble import GradientBoostingRegressor

# Estimate the effect of a job-training program on earnings
est = LinearDML(
    model_y=GradientBoostingRegressor(random_state=42),
    model_t=GradientBoostingRegressor(random_state=42),
)
est.fit(Y, T, X=covariates)
print("ATE:", est.ate_)
print("CATE:", est.cate(X=covariates[:5]))
```

## Tuning notes

- Use cross-fitting and out-of-fold nuisance predictions to avoid overfitting.
- Validate causal claims with placebo tests, pre-trend checks, and sensitivity analysis.
- Consider external validity and transportability across jurisdictions.
- Balance predictive accuracy with fairness and transparency for high-stakes decisions.

## Verification

1. Replicate a published policy evaluation with a causal ML estimator.
2. Run a placebo test and confirm no effect before the treatment date.
3. Compare model recommendations to a status-quo allocation on held-out cases.
''',
        "references": [
            "https://www.oecd.org/en/publications/governing-with-artificial-intelligence_795de142-en/full-report/ai-in-policy-evaluation_c88cc2fd.html",
            "https://www.cambridge.org/core/journals/data-and-policy/article/transparency-challenges-in-policy-evaluation-with-causal-machine-learning-improving-usability-and-accountability/DA780C002E4D4309655CB0DEEC88BC79",
            "https://www.cambridge.org/core/journals/data-and-policy/article/explainable-machine-learning-for-public-policy-use-cases-gaps-and-research-directions/B5B66B3C3B16196482984E878D795161",
            "https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1502599/full",
        ],
    },
    {
        "name": "ai-for-journalism",
        "title": "AI for Journalism",
        "description": "Algorithmic journalism, automated reporting, fact-checking, news recommendation, and AI-assisted investigative data reporting.",
        "devin_body": r'''
## When to use

You are producing, verifying, or distributing news and want to automate routine reporting, find leads in data, or assist reporters with research and drafting.

## Key concepts

- **Robot and automated journalism**: generate data-driven stories from structured feeds.
- **Computational news discovery**: detect anomalies, trends, and leads in public datasets.
- **Fact-checking and verification**: identify claims, source evidence, and detect misinformation.
- **News summarization and personalization**: adapt stories for platforms and audiences.
- **Editorial oversight and provenance**: log decisions, keep humans in the loop, and cite sources.

## Code pattern

```python
import pandas as pd
from jinja2 import Template

# Generate a simple data-driven news brief from a structured dataset
template = Template("{{ n }} incidents were reported in {{ city }} in {{ month }}, up {{ pct }}% from last year.")
row = {"n": 42, "city": "Springfield", "month": "March", "pct": 12}
print(template.render(**row))
```

## Tuning notes

- Human editorial judgment remains responsible for publication decisions and framing.
- Avoid hallucination by grounding generated text in verified source data.
- Monitor for bias in story selection, source diversity, and recommendation algorithms.
- Ensure transparent disclosure when content is automated or AI-assisted.

## Verification

1. Generate a batch of briefs from a public dataset and have a reporter review them.
2. Build a claim-detection pipeline and evaluate precision on a fact-check corpus.
3. Compare an AI-written summary to the original article for factual consistency.
''',
        "references": [
            "https://arxiv.org/html/2409.03462v1",
            "https://arxiv.org/html/2603.13232",
            "https://aclanthology.org/2026.findings-acl.1816/",
            "https://workflow.ap.org/ai/",
        ],
    },
    {
        "name": "ai-for-media-literacy",
        "title": "AI for Media Literacy",
        "description": "AI for detecting disinformation, prebunking, source credibility, and teaching critical thinking and digital literacy.",
        "devin_body": r'''
## When to use

You want to help users identify misinformation, understand manipulation tactics, evaluate sources, and develop resilience against online deception.

## Key concepts

- **Misinformation and disinformation detection**: classify false or misleading claims across text, images, and video.
- **Prebunking and inoculation**: expose users to weakened manipulation tactics before they encounter them.
- **Source and claim credibility**: assess website reliability, author expertise, and evidence quality.
- **Explainable AI for literacy**: make detection models transparent so users learn from them.
- **Generative AI awareness**: teach users how synthetic media is created and how to spot it.

## Code pattern

```python
from transformers import pipeline

# Zero-shot classification for manipulative tactics in a headline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
text = "Shocking secret they do not want you to see!"
labels = ["emotional manipulation", "conspiracy", "sensationalism", "legitimate news"]
result = classifier(text, labels)
for label, score in zip(result["labels"], result["scores"]):
    print(f"{label}: {score:.3f}")
```

## Tuning notes

- Frame tools as learning aids, not oracles; avoid undermining trust in genuine news.
- Include media-literacy explanations and interactive exercises, not just flags.
- Tailor interventions to age, language, and cultural context.
- Evaluate impact with pre/post tests and real-world believability measures.

## Verification

1. Test a misinformation detector on a labeled fact-check dataset and report AUC-PR.
2. Run a prebunking micro-intervention and compare pre/post quiz scores.
3. Have users rate the helpfulness and fairness of AI-generated explanations.
''',
        "references": [
            "https://aclanthology.org/2026.acl-demo.48/",
            "https://cordis.europa.eu/article/id/464673-when-ai-also-becomes-a-disinformation-ally",
            "https://www.titanthinking.eu/",
            "https://www.fzi.de/en/project/discoboard/",
        ],
    },
    {
        "name": "ai-for-communication",
        "title": "AI for Communication",
        "description": "Computational communication science: content analysis, information diffusion, agenda setting, and audience effects across digital platforms.",
        "devin_body": r'''
## When to use

You are studying how information, opinions, and narratives spread across media and platforms and want to analyze content, networks, and audience effects at scale.

## Key concepts

- **Automated content analysis**: classify frames, topics, emotions, and persuasion strategies.
- **Information diffusion and virality**: model retweet cascades, rumor spread, and influence.
- **Agenda setting and framing**: track salience and framing over time and across actors.
- **Audience analytics and segmentation**: understand engagement, polarization, and selective exposure.
- **Ethical platform research**: respect terms of service, privacy, and representative sampling.

## Code pattern

```python
import networkx as nx

# Build and analyze a retweet diffusion network
G = nx.from_pandas_edgelist(df, source="from_user", target="to_user", edge_attr="weight")
print("Density:", nx.density(G))
print("Top influencers:", sorted(dict(G.in_degree()).items(), key=lambda x: x[1], reverse=True)[:5])
```

## Tuning notes

- Link computational measures to communication theory and prior literature.
- Address platform-specific biases and changes in APIs and algorithms.
- Combine text, network, and temporal features rather than relying on one signal.
- Validate automated content codes with human coders and inter-rater reliability.

## Verification

1. Replicate a known finding on information diffusion in a new dataset.
2. Compare automated topic labels to human-coded topics and compute agreement.
3. Test whether a framing measure predicts agenda salience in a time-series model.
''',
        "references": [
            "https://iopscience.iop.org/article/10.1209/0295-5075/ade337",
            "https://doi.org/10.1177/08944393261457540",
            "https://doi.org/10.1080/19312458.2023.2285766",
            "https://link.springer.com/chapter/10.1007/978-981-97-8865-1_40",
        ],
    },
    {
        "name": "ai-for-criminology",
        "title": "AI for Criminology",
        "description": "Predictive policing, recidivism risk assessment, crime forecasting, criminal network analysis, and fairness-aware public safety research.",
        "devin_body": r'''
## When to use

You are analyzing crime patterns, assessing risk, or designing public-safety interventions and want to use data and models responsibly.

## Key concepts

- **Crime forecasting**: spatiotemporal models for hot spots and future incident counts.
- **Recidivism risk assessment**: predict reoffending to inform sentencing or rehabilitation.
- **Criminal network analysis**: detect co-offending, money-laundering, and gang structures.
- **Victimization and fear-of-crime mapping**: combine survey, sensor, and report data.
- **Fairness and accountability**: audit for racial and neighborhood bias in predictions and deployment.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Example: risk classification for a public-safety outcome (use with extreme care)
X = df[["age", "prior_offenses", "employment_status", "substance_use"]]
y = df["recidivated"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
clf = RandomForestClassifier(class_weight="balanced", random_state=42)
clf.fit(X_train, y_train)
```

## Tuning notes

- Predictive models can amplify historical biases; require fairness audits before deployment.
- Avoid feedback loops where predictions influence policing patterns and then future data.
- Use transparent, interpretable models in high-stakes criminal justice settings.
- Engage affected communities and legal stakeholders in model design and review.

## Verification

1. Evaluate a crime-forecasting model on held-out spatial and temporal data.
2. Audit a risk model for equalized odds across demographic groups.
3. Compare a model to a simple baseline and document any deployment trade-offs.
''',
        "references": [
            "https://link.springer.com/article/10.1007/s10940-025-09629-3",
            "https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.587943/full",
            "https://doi.org/10.3390/computers15050325",
            "https://doi.org/10.3390/ijgi11070400",
        ],
    },
]
