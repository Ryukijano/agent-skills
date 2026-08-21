SKILLS = [
    {
        "name": "ai-for-creative-writing",
        "title": "AI for Creative Writing",
        "description": 'Use large language models to co-write fiction and long-form prose, brainstorm outlines, calibrate voice, and run human-AI revision workflows.',
        "devin_body": r'''
## When to use

You are drafting fiction, scripts, or long-form prose and want an AI collaborator for ideation, continuation, style calibration, and revision.

## Usage

- Brainstorm premises, outlines, and character sheets for novels and scripts.
- Generate first drafts and continuations in a controlled voice and style.
- Use few-shot examples and style guides to keep output on-brand.
- Audit generated prose for stereotypes, toxicity, and hallucinations.

## Steps

1. Define the genre, audience, and style guide for the project.
2. Create an outline, character sheet, and world bible to maintain long-context coherence.
3. Generate scenes with structured prompts and a calibrated temperature.
4. Review and rewrite with a human-in-the-loop, checking voice consistency.
5. Run a toxicity, bias, and fact-check audit before finalizing the draft.

## Code pattern

```python
from transformers import pipeline

# A simple continuation pipeline for a fiction scene
generator = pipeline("text-generation", model="openai-community/gpt2")

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
        "description": 'Co-write poems under meter, rhyme, and style constraints with interactive language models that suggest lines and refine form.',
        "devin_body": r'''
## When to use

You want to generate or co-write poems under formal constraints such as meter, rhyme, syllable counts, or a specific literary style.

## Usage

- Generate poems under meter, rhyme scheme, syllable count, and stanza constraints.
- Emulate a specific poet, era, mood, or lexical register.
- Post-process with rule-based rhyme and meter checking.
- Curate and evaluate poems for novelty, emotion, and aesthetic quality.

## Steps

1. Choose a form (sonnet, haiku, villanelle) and its formal constraints.
2. Prompt the model with persona, mood, imagery, and a target rhyme scheme.
3. Generate multiple drafts and score them for form compliance.
4. Validate meter and rhyme with tools such as pronouncingpy or pyphen.
5. Select and edit the best poems in a blinded human-curation pass.

## Code pattern

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "openai-community/gpt2"
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
        "description": 'Use structured LLM workflows to generate plots, build character arcs, manage worldbuilding, and create interactive or branching narratives.',
        "devin_body": r'''
## When to use

You are building interactive fiction, game narratives, brand stories, or structured plots with multiple acts and characters.

## Usage

- Generate three-act outlines, beat sheets, and plot-point scaffolding.
- Maintain character and world consistency with memory and knowledge graphs.
- Build branching dialogue and choices for interactive fiction and games.
- Use recursive summarization to preserve coherence in long-form stories.

## Steps

1. Write a one-page premise and target genre for the story.
2. Generate a structured outline with acts, beats, and character arcs.
3. Create a persistent character/world store and use it in every generation.
4. Draft scenes and branch points, then check continuity against the store.
5. Test with readers for engagement and coherence, then iterate.

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
        "description": 'Use AI to audit content libraries, identify topic gaps, optimize for generative-engine citation, and adapt assets across channels.',
        "devin_body": r'''
## When to use

You are planning editorial calendars, auditing content libraries, adapting assets across channels, or optimizing for AI search citations.

## Usage

- Inventory existing content and cluster it into topic pillars.
- Identify performance gaps and competitive whitespace.
- Structure content so LLMs cite the brand in their answers.
- Repurpose long-form content into social, email, and video scripts.

## Steps

1. Export the content inventory and performance data.
2. Cluster content into topic pillars using NLP or embeddings.
3. Map buyer prompts and answer-first passages to target for GEO.
4. Audit for gaps and generate a prioritized topic backlog.
5. Reformat a flagship piece into channel-specific variants and track LLM citation share.

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
        "description": 'Draft and A/B-test personalized marketing emails that match brand voice and lift conversion rates by double digits.',
        "devin_body": r'''
## When to use

You are creating ads, emails, landing pages, product descriptions, or calls to action that must convert and match a brand voice.

## Usage

- Draft ads, emails, landing pages, and product descriptions in brand voice.
- Apply copy frameworks such as AIDA, PAS, BAB, and Hook-Promise-Proof.
- Generate variants for A/B testing and rank them by predicted CTR.
- Verify claims, avoid fabricated specifics, and run brand-safety QA.

## Steps

1. Load the brand voice guide, audience profile, and copy framework.
2. Prompt for several variants with constraints on tone and length.
3. Score variants against brand voice and predicted performance.
4. Run a human QA pass for claims, safety, and platform limits.
5. Launch an A/B test and iterate based on CTR or conversion lift.

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
        "description": 'Use machine learning to generate ad creatives, optimize media buying, run dynamic creative optimization, and model campaign performance.',
        "devin_body": r'''
## When to use

You are building ad campaigns across search, social, display, and video; generating and selecting creatives; or optimizing budget allocation.

## Usage

- Assemble and test copy, image, and video variants with dynamic creative optimization.
- Predict CTR and CVR from creative and audience features.
- Target lookalikes, retargeting segments, and contextual signals.
- Measure incrementality with multi-touch, geo, and holdout experiments.

## Steps

1. Define campaign goals, audience, channels, and creative variables.
2. Structure historical creative and audience features for model training.
3. Train a CTR/CVR predictor and validate rank correlation on held-out creatives.
4. Run a DCO or Thompson-sampling experiment against a static baseline.
5. Measure incremental lift with a geo or randomized holdout and optimize spend.

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
        "description": 'Use AI to optimize search, social, email, and analytics across digital channels while respecting privacy and first-party data.',
        "devin_body": r'''
## When to use

You need to drive traffic, engagement, and conversions across digital channels with AI-assisted search, social, email, and analytics.

## Usage

- Optimize SEO and GEO for answer-first, citeable content.
- Automate bidding, audience signals, and creative rotation in paid channels.
- Personalize email and marketing automation with segmentation and send-time optimization.
- Attribute impact with multi-touch, cohort, and marketing-mix models.

## Steps

1. Unify first-party data and ensure consent and privacy compliance.
2. Audit technical SEO, structured data, and keyword visibility.
3. Build a keyword-visibility or send-time optimization experiment.
4. Test an AI-recommended audience segment against a rule-based baseline.
5. Measure lift with causal methods and holdouts, then refine the mix.

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
        "description": 'Use AI to co-create brand strategy, name and tagline options, visual identity concepts, and brand voice guides with human designers in the loop.',
        "devin_body": r'''
## When to use

You are developing or refreshing a brand: naming, logos, taglines, visual identity, brand architecture, or brand voice.

## Usage

- Generate naming and tagline candidates and screen for conflicts.
- Explore visual identity concepts, color palettes, and mood boards.
- Draft and score brand voice messages across channels.
- Run trademark and cultural-sensitivity checks before launch.

## Steps

1. Document audience, promise, values, and differentiation for the brand.
2. Generate a large set of name, tagline, and visual concepts.
3. Screen candidates for trademark, domain, and cultural conflicts.
4. Develop a brand voice guide and score AI-written messages for consistency.
5. Run a perception survey and refine with human designers before finalizing.

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
        "description": 'Use AI to design interaction patterns, prototype AI features, synthesize user research, and build human-centered AI experiences.',
        "devin_body": r'''
## When to use

You are designing AI-powered products, chatbots, agent interfaces, recommendation surfaces, or generative tools where user trust and control are critical.

## Usage

- Prototype chat, agent, and recommendation interfaces with user control.
- Synthesize user interviews, usability tests, and analytics.
- Apply AI UX patterns such as explainability, progressive disclosure, and graceful failure.
- Test trust, comprehension, and accessibility with diverse users.

## Steps

1. Define the user task, mental model, and trust expectations.
2. Create low-fidelity wireframes and a clickable prototype.
3. Design feedback, correction, and escalation paths into the UI.
4. Run a usability test with 5+ users and measure task success.
5. Iterate on trust, comprehension, and failure handling based on results.

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
        "description": 'Use AI to explore design spaces, generate concepts, prototype products, and hand off to engineering while tracking constraints and human decisions.',
        "devin_body": r'''
## When to use

You are designing physical or digital products, from early ideation and concept exploration to prototyping, testing, and engineering handoff.

## Usage

- Generate and rank concepts across a parametric design space.
- Co-create with designers by combining constraints, AI proposals, and human selection.
- Integrate CAD, generative design, simulation, and FEA/CFD workflows.
- Validate concepts with user studies and manufacturability checks.

## Steps

1. Capture requirements, constraints, and success metrics in a design brief.
2. Generate and sample a design space with AI-assisted concept tools.
3. Rank concepts by preference, engineering, and cost constraints.
4. Run a small user study and validate top concepts.
5. Hand off the selected concept to CAD, simulation, or manufacturing.

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
        "description": 'Automate transcripts, show notes and chapter markers to speed podcast production and improve accessibility.',
        "devin_body": r'''
## When to use

You are producing podcasts: planning, scripting, recording, editing, and distributing, where AI can speed up production or enable synthetic hosts.

## Usage

- Generate episode outlines, interview questions, and hooks.
- Synthesize or clone voices for hosts and guests with disclosure.
- Edit audio with noise removal, auto-leveling, and filler-word removal.
- Transcribe, diarize speakers, and generate show notes and chapter markers.

## Steps

1. Plan the episode theme, structure, and guest questions.
2. Record or synthesize audio and label any synthetic voices.
3. Transcribe and diarize the recording with an ASR pipeline.
4. Edit for noise, levels, and filler words, then generate show notes.
5. Verify transcription accuracy and listener engagement before publishing.

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
        "description": 'Use machine learning to discover and vet creators, match them to campaigns, predict performance, and measure ROI and authenticity.',
        "devin_body": r'''
## When to use

You are finding and vetting creators, matching them to campaigns, predicting performance, measuring ROI, or managing brand-creator collaborations.

## Usage

- Score creators by audience fit, engagement quality, and brand safety.
- Match briefs to creators based on content style and values alignment.
- Co-create briefs, scripts, thumbnails, and captions with AI assistance.
- Predict reach, engagement, and conversion lift for campaigns.

## Steps

1. Define campaign goals, audience, budget, and brand-safety criteria.
2. Build a creator database with demographics, engagement, and content analysis.
3. Rank creators with a fit score and compare to human picks.
4. Predict engagement for past campaigns and report MAE vs. actuals.
5. Audit delivered content for disclosure, brand safety, and FTC compliance.

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
