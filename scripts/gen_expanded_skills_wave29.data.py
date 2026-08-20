SKILLS = [
    {
        "name": "ai-for-creative-writing",
        "title": "AI for Creative Writing",
        "description": "Co-writing novels, screenplays, and long-form fiction with LLMs, prompt engineering for voice and style, and human-AI revision workflows.",
        "devin_body": r'''
## When to use

You are drafting fiction, scripts, or long-form prose and want an AI collaborator for ideation, continuation, style calibration, and revision.

## Key concepts

- **Human-AI co-writing**: treat the LLM as a brainstorming partner, outline generator, first-drafter, or revision assistant.
- **Voice and style control**: use few-shot examples, persona prompts, tone descriptors, and style guides to keep output on-brand.
- **Long-context planning**: maintain coherence across chapters or scenes with outlines, character sheets, and worldbuilding bibles.
- **Retrieval and memory**: use vector stores or note systems to ground the model in characters, settings, and prior events.
- **Bias and safety**: audit for stereotypes, toxicity, and hallucinations; respect copyright and cultural context.

## Code pattern

```python
from transformers import pipeline

# A simple continuation pipeline for a fiction scene
generator = pipeline("text-generation", model="gpt2")

prompt = """Continue the noir detective scene in first person, raining, 1920s Chicago:

The alley was a river of shadows..."""

output = generator(
    prompt,
    max_new_tokens=200,
    temperature=0.8,
    do_sample=True,
)
print(output[0]["generated_text"])
```

## Tuning notes

- Tune temperature for creativity (0.7-0.9) vs. coherence (lower).
- Constrain outputs with a style guide or constrained decoding to preserve voice.
- Chunk long manuscripts and feed context incrementally to avoid loss of continuity.
- Evaluate with human readers; use LLM-as-judge only as a secondary metric.

## Verification

1. Generate a 1,000-word scene from a provided outline and compare it to a style guide.
2. Maintain character consistency across three generated chapters using a shared character sheet.
3. Run a toxicity and bias audit on generated prose.
''',
        "references": [
            "https://arxiv.org/abs/2209.14958",
            "https://doi.org/10.1145/3544548.3581225",
            "https://doi.org/10.48550/arxiv.2310.08433",
            "https://link.springer.com/article/10.1007/s00146-024-02127-3",
        ],
    },
    {
        "name": "ai-for-poetry",
        "title": "AI for Poetry",
        "description": "Meter, rhyme, and stylistic constraints for AI-generated poetry, with evaluation and human-AI curation.",
        "devin_body": r'''
## When to use

You want to generate or co-write poems under formal constraints such as meter, rhyme, syllable counts, or a specific literary style.

## Key concepts

- **Formal constraints**: meter, rhyme scheme, syllable counts, stanza forms, and refrain patterns.
- **Poetic style prompting**: persona, era, mood, imagery, alliteration, and lexical register.
- **Controllable generation**: constrained decoding, iterative refinement, and rule-based post-processing for rhyme and meter.
- **Evaluation**: automatic metrics, LLM-as-judge, and human evaluation for novelty, emotion, and aesthetic quality.
- **Ethics and attribution**: respect public-domain or licensed training data and credit human curators.

## Code pattern

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = """Write a Shakespearean sonnet about autumn.
Use iambic pentameter and an ABAB CDCD EFEF GG rhyme scheme:

"""

inputs = tokenizer(prompt, return_tensors="pt")
output = model.generate(
    **inputs,
    max_new_tokens=200,
    temperature=0.9,
    do_sample=True,
)
poem = tokenizer.decode(output[0], skip_special_tokens=True)
print(poem)
```

## Tuning notes

- Use constrained decoding or post-hoc rhyme checking to satisfy form.
- Fine-tune on poetry corpora for stronger stylistic control.
- Balance novelty with readability; avoid cliches.
- Validate meter and rhyme with dedicated tools such as `pronouncingpy` or `pyphen`.

## Verification

1. Generate 10 sonnets and check rhyme and meter compliance automatically.
2. Compare human vs. AI poems in a small blinded preference test.
3. Evaluate diversity and novelty across a themed set of poems.
''',
        "references": [
            "https://doi.org/10.1613/jair.1.20584",
            "https://aclanthology.org/W17-3502/",
            "https://aclanthology.org/2024.emnlp-main.1097/",
            "https://computationalcreativity.net/iccc24/papers/ICCC24_paper_164.pdf",
        ],
    },
    {
        "name": "ai-for-storytelling",
        "title": "AI for Storytelling",
        "description": "Narrative generation, plot planning, character arcs, and worldbuilding with structured LLM workflows.",
        "devin_body": r'''
## When to use

You are building interactive fiction, game narratives, brand stories, or structured plots with multiple acts and characters.

## Key concepts

- **Narrative planning**: outlines, beat sheets, story graphs, and plot-point scaffolding.
- **Character and world consistency**: memory, character sheets, and knowledge graphs to preserve continuity.
- **Interactive storytelling**: branching choices, dynamic dialogue, and player or reader agency.
- **Long-form coherence**: recursive summarization and hierarchical generation.
- **Evaluation**: narrative coherence, engagement, originality, and human judgment.

## Code pattern

```python
from openai import OpenAI

client = OpenAI()

outline = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a narrative architect."},
        {"role": "user", "content": "Create a three-act outline for a sci-fi heist story."},
    ],
    temperature=0.7,
)
print(outline.choices[0].message.content)
```

## Tuning notes

- Decompose generation into premise, outline, scenes, and prose.
- Use structured output (JSON or YAML) to control acts and characters.
- Keep a persistent world and character store for multi-session stories.
- Test with readers for narrative engagement and coherence.

## Verification

1. Generate a complete story arc with premise, outline, and three scenes.
2. Track character consistency through a 2,000-word passage.
3. Run an A/B test comparing human vs. AI story continuations.
''',
        "references": [
            "https://aclanthology.org/2025.findings-emnlp.750/",
            "https://aclanthology.org/2023.inlg-main.23.pdf",
            "https://www.mdpi.com/2227-7390/13/23/3885",
            "https://aclanthology.org/2024.findings-emnlp.824/",
        ],
    },
    {
        "name": "ai-for-content-strategy",
        "title": "AI for Content Strategy",
        "description": "Planning, auditing, and orchestrating content portfolios with AI, including generative-engine optimization and cross-platform adaptation.",
        "devin_body": r'''
## When to use

You are planning editorial calendars, auditing content libraries, adapting assets across channels, or optimizing for AI search citations.

## Key concepts

- **Content audit and gap analysis**: inventory, performance data, topic clusters, and competitive whitespace.
- **Generative engine optimization (GEO)**: structuring content so LLMs cite your brand in their answers.
- **Cross-platform adaptation**: tone, length, and format for web, social, email, and video.
- **Personalization and audience personas**: AI-driven segmentation and messaging.
- **Governance and quality**: brand voice, fact-checking, and editorial guidelines.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Cluster existing content into topic pillars
df = pd.read_csv("content_inventory.csv")
vectors = TfidfVectorizer(stop_words="english").fit_transform(df["body"])
df["cluster"] = KMeans(n_clusters=6, random_state=42, n_init="auto").fit_predict(vectors)
print(df[["title", "cluster"]].head())
```

## Tuning notes

- Focus on answer-first, structured, citeable passages for GEO.
- Map content to buyer prompts, not just keywords.
- Maintain a single source of truth for brand voice and facts.
- Measure LLM citation share, not just search ranking.

## Verification

1. Audit a site and produce a gap analysis with 10 new topic recommendations.
2. Reformat one long-form article into social, email, and video scripts.
3. Track citation rate in a small LLM-retrieval benchmark.
''',
        "references": [
            "https://doi.org/10.1177/14413582251390582",
            "https://doi.org/10.1177/00472816211041951",
            "https://doi.org/10.1145/3648188.3675142",
            "https://doi.org/10.1108/ejim-03-2024-0317",
        ],
    },
    {
        "name": "ai-for-copywriting",
        "title": "AI for Copywriting",
        "description": "Marketing and advertising copy, email and landing-page text, conversion frameworks, and brand-voice calibration with LLMs.",
        "devin_body": r'''
## When to use

You are creating ads, emails, landing pages, product descriptions, or calls to action that must convert and match a brand voice.

## Key concepts

- **Copy frameworks**: AIDA, PAS, BAB, FAB, 4U, and Hook-Promise-Proof.
- **Brand voice calibration**: few-shot examples, tone descriptors, and style guides.
- **A/B testing and uplift**: generate variants, rank them, and test in the field.
- **CRO integration**: align copy with audience, channel, and funnel stage.
- **Hallucination and claim control**: verify claims and avoid fabricated specifics.

## Code pattern

```python
from openai import OpenAI

client = OpenAI()

prompt = (
    "Using the Problem-Agitate-Solution framework, write 3 email subject lines "
    "and opening lines for a sustainable running-shoe launch. "
    "Tone: bold but warm."
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.8,
)
print(response.choices[0].message.content)
```

## Tuning notes

- Provide 3-5 brand voice examples for consistent tone.
- Generate many variants, then rank with historic CTR data or a reward model.
- Keep within platform character limits.
- Always run a human QA pass for claims and brand safety.

## Verification

1. Generate 5 email subject lines and test open rate against a baseline.
2. Apply a brand-voice scorecard to 20 copy samples.
3. Run a small A/B test on a landing-page headline.
''',
        "references": [
            "https://arxiv.org/abs/2402.13667",
            "https://www.chicagobooth.edu/review/ai-is-coming-marketing-department",
            "https://doi.org/10.1016/j.jbusres.2024.114984",
            "https://www.deloittedigital.com/us/en/insights/research/genai-human-marketing-operations.html",
        ],
    },
    {
        "name": "ai-for-advertising",
        "title": "AI for Advertising",
        "description": "Ad creative generation, media buying optimization, dynamic creative optimization, and predictive performance modeling.",
        "devin_body": r'''
## When to use

You are building ad campaigns across search, social, display, and video; generating and selecting creatives; or optimizing budget allocation.

## Key concepts

- **Dynamic creative optimization (DCO)**: assemble and test copy, image, and video variants.
- **Predictive creative performance**: CTR/CVR models trained on historical A/B tests.
- **Audience and contextual targeting**: lookalikes, retargeting, and contextual signals.
- **Attribution and incrementality**: multi-touch, geo-experiments, and causal lift.
- **Brand safety and compliance**: ad policies, disclosures, and responsible AI.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# Predict ad CTR from creative and audience features
X = pd.get_dummies(df[["headline", "image_tag", "audience_segment"]], drop_first=True)
y = df["ctr"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = GradientBoostingRegressor(random_state=42).fit(X_train, y_train)
print("R2:", model.score(X_test, y_test))
```

## Tuning notes

- Use structured creative features so models generalize across variants.
- Run adaptive or Thompson-sampling experiments to discover top creatives.
- Protect against leakage and data snooping in campaign history.
- Balance short-term conversions with long-term brand effects.

## Verification

1. Train a CTR predictor and evaluate rank correlation on held-out creatives.
2. Run a DCO experiment and report lift over a static ad.
3. Measure incremental lift with a geo or randomized holdout.
''',
        "references": [
            "https://arxiv.org/abs/2607.23696v1",
            "https://dl.acm.org/doi/10.1145/3442381.3449909",
            "https://dl.acm.org/doi/10.1145/3340531.3412720",
            "https://www.iab.com/wp-content/uploads/2025/01/IAB_GenerativeAIPlaybook_January_26.pdf",
        ],
    },
    {
        "name": "ai-for-digital-marketing",
        "title": "AI for Digital Marketing",
        "description": "SEO, SEM, social media, email automation, marketing analytics, and AI-driven personalization across digital channels.",
        "devin_body": r'''
## When to use

You need to drive traffic, engagement, and conversions across digital channels with AI-assisted search, social, email, and analytics.

## Key concepts

- **SEO and GEO**: keyword intent, technical SEO, structured data, and answer-first content.
- **Paid search and social**: automated bidding, audience signals, and creative rotation.
- **Email and marketing automation**: segmentation, send-time optimization, and personalization.
- **Attribution and analytics**: multi-touch, cohorts, incrementality, and marketing mix modeling.
- **Privacy and first-party data**: consent, clean rooms, and server-side tracking.

## Code pattern

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Forecast weekly search impressions for budget planning
model = ExponentialSmoothing(
    impressions,
    seasonal_periods=52,
    trend="add",
    seasonal="add",
).fit()
forecast = model.forecast(steps=4)
print(forecast)
```

## Tuning notes

- Integrate AI on a unified first-party data foundation.
- Use causal methods and holdouts to separate AI-driven lift from seasonality.
- Keep human oversight on brand voice and channel strategy.
- Monitor platform policy and privacy compliance.

## Verification

1. Build a keyword-visibility forecast and compare it to actuals.
2. Test an AI-recommended audience segment against a rule-based one.
3. Run an email send-time optimization experiment and measure lift.
''',
        "references": [
            "https://business.google.com/us/think/ai-excellence/how-to-use-ai-for-marketing/",
            "https://www.bcg.com/publications/2024/blueprint-for-ai-powered-marketing",
            "https://doi.org/10.47392/irjaem.2025.0410",
            "https://ahrefs.com/blog/how-to-use-ai-in-marketing/",
        ],
    },
    {
        "name": "ai-for-branding",
        "title": "AI for Branding",
        "description": "Brand strategy, visual identity, brand voice, naming, and AI-assisted brand co-creation with human curation.",
        "devin_body": r'''
## When to use

You are developing or refreshing a brand: naming, logos, taglines, visual identity, brand architecture, or brand voice.

## Key concepts

- **Brand strategy and positioning**: audience, promise, differentiation, and values.
- **Visual identity and design systems**: logos, color, typography, and imagery.
- **Brand voice and messaging**: tone, personality, and cross-channel consistency.
- **AI co-creation**: concept generation, mood boards, and style exploration.
- **Governance and ethics**: trademark checks, cultural sensitivity, and authenticity.

## Code pattern

```python
from difflib import SequenceMatcher

names = ["Nexa", "Vello", "Aurora", "Kinetic", "Forma"]
existing = ["nexa.io", "vello.com", "aurora.co"]

def uniqueness(name):
    return max(SequenceMatcher(None, name, e).ratio() for e in existing)

candidates = [f"{n.lower()}.com" for n in names]
ranked = sorted(candidates, key=uniqueness)
print(ranked[:5])
```

## Tuning notes

- Treat AI as a concept generator; human designers own final identity.
- Run trademark and domain availability checks before launch.
- Build a brand style guide and asset library to enforce consistency.
- Evaluate brand perception with audience surveys, not just aesthetics.

## Verification

1. Generate 20 brand-name candidates and screen for trademark and domain conflicts.
2. Create a brand voice guide and score 10 AI-written messages for consistency.
3. Conduct a small perception survey on AI-assisted vs. human-led brand concepts.
''',
        "references": [
            "https://doi.org/10.2139/ssrn.5011625",
            "https://www.nature.com/articles/s41599-025-04488-6",
            "https://dl.designresearchsociety.org/cgi/viewcontent.cgi?article=1472&context=iasdr",
            "https://repository.tudelft.nl/record/uuid:d11fd183-b727-41a8-9c21-28eac6319d44",
        ],
    },
    {
        "name": "ai-for-ux-design",
        "title": "AI for UX Design",
        "description": "Interaction design, user research, prototyping, and AI UX patterns for human-centered AI products.",
        "devin_body": r'''
## When to use

You are designing AI-powered products, chatbots, agent interfaces, recommendation surfaces, or generative tools where user trust and control are critical.

## Key concepts

- **Human-centered AI UX**: user needs, mental models, and trust calibration.
- **AI UX patterns**: contextual assistance, progressive disclosure, explainability, and graceful failure.
- **Conversational and agent interfaces**: turn-taking, intent, escalation, and feedback.
- **UX research with AI**: synthesis of interviews, usability testing, and analytics.
- **Accessibility and ethics**: inclusive design, privacy, safety, and transparency.

## Code pattern

```python
import gradio as gr

# A simple chat UI with user feedback

def chat(message, history):
    response = model.respond(message, history)
    return response

demo = gr.ChatInterface(chat)
demo.launch()
```

## Tuning notes

- Set clear expectations for AI capabilities and confidence.
- Provide easy correction, undo, and escalation paths.
- Show why the AI made a recommendation when feasible.
- Test with diverse users under realistic failure conditions.

## Verification

1. Prototype an AI feature in a low-fidelity clickable mock.
2. Run a usability test with 5 users and measure task success.
3. Evaluate trust and comprehension with a post-task survey.
''',
        "references": [
            "https://www.aiuxdesign.guide/patterns",
            "https://ai-interaction.com/",
            "https://doi.org/10.1561/1100000106",
            "https://web.dev/learn/ai/ux-patterns",
        ],
    },
    {
        "name": "ai-for-product-design",
        "title": "AI for Product Design",
        "description": "Concept generation, design space exploration, prototyping, and engineering handoff with generative AI in product development.",
        "devin_body": r'''
## When to use

You are designing physical or digital products, from early ideation and concept exploration to prototyping, testing, and engineering handoff.

## Key concepts

- **Design space exploration**: generative concepts, parametric variants, and trade-off analysis.
- **Human-AI co-creation**: the designer sets constraints, the AI proposes candidates, and the human selects and refines.
- **Prototyping and simulation**: CAD, generative design, digital twins, and FEA/CFD integration.
- **User-centered validation**: rapid user testing, conjoint analysis, and desirability studies.
- **Sustainability and manufacturing**: material selection, design for manufacturing, and lifecycle considerations.

## Code pattern

```python
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

# Explore a generated design-space sample in 2D
X = np.random.rand(50, 10)  # 10 design parameters for 50 concepts
pca = PCA(n_components=2)
coords = pca.fit_transform(X)
pd.DataFrame(coords, columns=["dim1", "dim2"]).to_csv("design_space.csv")
```

## Tuning notes

- Keep constraints explicit and traceable from requirements to final concept.
- Use preference-based ranking to converge on top concepts.
- Validate generated concepts against engineering and cost constraints.
- Document human decisions and AI contributions for IP and accountability.

## Verification

1. Generate 50 concept variants for a brief and rank them by preference.
2. Run a small user study to validate the top concepts.
3. Hand off a selected concept to a CAD or engineering workflow.
''',
        "references": [
            "https://www.cambridge.org/core/journals/proceedings-of-the-design-society/article/mapping-ai-applications-in-design/16F2188A6CEC60F2AD7E6D32A16338D4",
            "https://doi.org/10.3390/sym18020352",
            "https://doi.org/10.1145/3613904.3642908",
            "https://codelabs.developers.google.com/codelabs/pair-guidebook",
        ],
    },
    {
        "name": "ai-for-podcasting",
        "title": "AI for Podcasting",
        "description": "AI-generated and AI-assisted podcast production, including scriptwriting, voice synthesis, editing, transcription, and show notes.",
        "devin_body": r'''
## When to use

You are producing podcasts: planning, scripting, recording, editing, and distributing, where AI can speed up production or enable synthetic hosts.

## Key concepts

- **Script and outline generation**: episode structures, interview questions, hooks, and summaries.
- **Voice synthesis and cloning**: TTS, multi-speaker conversation, and zero-shot voice.
- **Audio editing and enhancement**: noise removal, auto-leveling, and filler-word removal.
- **Transcription and show notes**: ASR, speaker diarization, and chapter markers.
- **Ethics and disclosure**: synthetic-voice labels, consent, and copyright.

## Code pattern

```python
from transformers import pipeline

# Transcribe audio and generate show notes
asr = pipeline("automatic-speech-recognition", model="openai/whisper-base")
transcript = asr("episode.mp3")["text"]

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarizer(transcript[:1024], max_length=130, min_length=30)[0]["summary_text"]
print(summary)
```

## Tuning notes

- Use high-quality source audio for transcription; edit AI summaries for accuracy.
- Label synthetic voices and obtain speaker consent.
- Balance automation with editorial judgment.
- Test across accents and audio conditions.

## Verification

1. Transcribe a 10-minute episode and measure WER against a reference.
2. Generate AI show notes and compare listener engagement to manual notes.
3. Produce a 2-minute segment with a synthetic voice and disclose its nature.
''',
        "references": [
            "https://www.microsoft.com/en-us/research/publication/vibevoice-expressive-podcast-generation/",
            "https://blog.google/innovation-and-ai/products/notebooklm-audio-overviews/",
            "https://arxiv.org/abs/2510.00485v1",
            "https://www.scientificamerican.com/podcast/episode/how-tools-like-notebooklm-create-ai-generated-podcasts/",
        ],
    },
    {
        "name": "ai-for-influencer-marketing",
        "title": "AI for Influencer Marketing",
        "description": "Creator discovery, campaign matching, content co-creation, performance prediction, and authenticity measurement for influencer marketing.",
        "devin_body": r'''
## When to use

You are finding and vetting creators, matching them to campaigns, predicting performance, measuring ROI, or managing brand-creator collaborations.

## Key concepts

- **Creator discovery and vetting**: audience demographics, engagement, brand safety, and fake-follower detection.
- **Campaign matching**: brief-to-creator fit, content style, and values alignment.
- **Content co-creation**: AI-assisted briefs, scripts, thumbnails, and captions.
- **Performance prediction and attribution**: reach, engagement, conversions, and lift.
- **Authenticity and disclosure**: sponsorship transparency, FTC guidelines, and trust.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Predict influencer campaign engagement from creator features
X = df[["followers", "avg_likes", "avg_comments", "video_count", "audience_quality"]]
y = df["engagement_rate"]
model = RandomForestRegressor(random_state=42).fit(X, y)
df["predicted_er"] = model.predict(X)
print(df[["creator", "predicted_er"]].head())
```

## Tuning notes

- Prioritize engagement quality and audience fit over raw follower counts.
- Use multi-objective optimization for reach, brand safety, and cost.
- Verify disclosure and compliance in sponsored content.
- Build feedback loops with actual campaign outcomes.

## Verification

1. Rank creators for a brief using a fit score and compare to human picks.
2. Predict engagement for 50 past campaigns and report MAE vs. actuals.
3. Audit a campaign for disclosure compliance and brand safety.
''',
        "references": [
            "https://doi.org/10.1007/s11747-026-01186-w",
            "https://doi.org/10.1186/s43093-026-00910-w",
            "https://doi.org/10.1007/s11747-026-01185-x",
            "https://www.mdpi.com/0718-1876/20/1/17",
        ],
    },
]
