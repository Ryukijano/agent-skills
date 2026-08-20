SKILLS = [
    {
        "name": "ai-for-science-communication",
        "title": "AI for Science Communication",
        "description": "Plain-language summaries, research storytelling, audience adaptation, and ethical, evidence-based use of generative AI for public-facing science.",
        "devin_body": r'''## When to use

You need to translate technical scientific findings into accessible, engaging formats for the public, patients, educators, or policymakers while preserving accuracy.

## Key concepts

- **Plain-language summaries**: rewrite abstracts and papers for non-expert reading levels.
- **Audience adaptation**: tune tone, length, and examples for patients, teachers, journalists, or legislators.
- **Narrative and framing**: use story structure, metaphors, and relatable examples without overclaiming.
- **Multimodal science communication**: combine text, audio, slides, and visuals for broader reach.
- **Hallucination and fact-checking**: every generated claim must be traceable to the source paper.

## Code pattern

```python
import textstat

# Example: post-process a plain-language summary for target reading level
summary = "CRISPR edits DNA to treat disease."
print("Flesch-Kincaid grade:", textstat.flesch_kincaid_grade(summary))
```

## Tuning notes

- Target a specific reading level (e.g., Flesch-Kincaid 8-10 for general public).
- Preserve hedges and uncertainty (e.g., "suggests," "may," "in this sample").
- Always have a domain expert review AI-generated summaries before publication.
- Disclose AI assistance and maintain transparency about the source material.

## Verification

1. Generate a plain-language summary from a paper and compare its reading level to a human-written version.
2. Fact-check every generated claim against the original source.
3. Pilot the summary with a small non-expert audience and collect comprehension and trust metrics.
''',
        "references": [
            "https://doi.org/10.1177/10755470251411176",
            "https://doi.org/10.1093/pnasnexus/pgae387",
            "https://doi.org/10.48550/arxiv.2308.16377",
            "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0342852",
        ],
    },
    {
        "name": "ai-for-research-communication",
        "title": "AI for Research Communication",
        "description": "Drafting manuscripts, abstracts, cover letters, response-to-reviewers, and translating findings across disciplines with LLMs.",
        "devin_body": r'''## When to use

You are writing or refining academic manuscripts, abstracts, cover letters, response-to-reviewers, or interdisciplinary summaries of research findings.

## Key concepts

- **Structured scientific writing**: follow IMRaD, abstract structures, and journal-specific guidelines.
- **Academic tone and style**: use LLMs to adjust formality, clarity, and field-specific conventions.
- **Citation and reference management**: ground drafts in uploaded PDFs and verified bibliographies.
- **Integrity checks**: detect accidental plagiarism, AI-patterned text, and citation errors.
- **Cross-disciplinary translation**: reframe findings for readers in adjacent fields.

## Code pattern

```python
from transformers import pipeline

# Example: condense a long methods section into an abstract-sized summary
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
short = summarizer(long_methods, max_length=120, min_length=30, do_sample=False)
```

## Tuning notes

- Feed the model your own sources, outline, and reviewer comments to keep outputs grounded.
- Avoid asking the model to invent citations; verify every DOI and page number.
- Maintain author voice by editing generated drafts rather than publishing them raw.
- Use dedicated tools (e.g., Paperpal, Elicit, Semantic Scholar) for citation-aware writing.

## Verification

1. Draft an abstract from a full paper and compare it to the original for accuracy and style.
2. Run a reference check to confirm every generated citation exists and supports its claim.
3. Have a colleague compare an LLM-edited response-to-reviewers to a human-only version.
''',
        "references": [
            "https://peelback.ai/",
            "https://paperpal.com/",
            "https://sciencecast.org/",
            "https://github.com/microsoft/ResearchStudio",
            "https://aclanthology.org/2025.aisd-main.4.pdf",
        ],
    },
    {
        "name": "ai-for-public-engagement",
        "title": "AI for Public Engagement",
        "description": "Conversational agents, citizen science, public consultations, and participatory science supported by LLMs and interactive AI.",
        "devin_body": r'''## When to use

You are running public consultations, citizen-science projects, science-festival chatbots, or community outreach and want to make engagement more inclusive and scalable.

## Key concepts

- **Bidirectional science communication**: collect, analyze, and respond to public questions and concerns.
- **Conversational AI**: chatbots and voice agents that answer science questions and guide participation.
- **Citizen science and data quality**: LLMs help onboard volunteers, validate submissions, and provide feedback.
- **Deliberative and participatory design**: AI can support but not replace community voice and agency.
- **Transparency and accessibility**: disclose AI involvement, support multiple languages, and protect privacy.

## Code pattern

```python
from collections import Counter

# Example: simple theme extraction from public consultation comments
def extract_theme(comment):
    # In practice, use an NER or topic model
    return comment.split(":")[0]

themes = [extract_theme(c) for c in comments]
print(Counter(themes).most_common(10))
```

## Tuning notes

- Co-design prompts with community stakeholders, not just technical staff.
- Use retrieval-augmented generation to ground chatbot answers in vetted FAQs and sources.
- Monitor for bias, misinformation, and over-reliance on AI in sensitive discussions.
- Ensure data ownership and consent, especially for youth and marginalized groups.

## Verification

1. Deploy a chatbot at a public event and log question types, answer accuracy, and escalation rates.
2. Analyze a corpus of consultation comments and compare AI-extracted themes to human coding.
3. Measure changes in volunteer retention and data quality when adding an LLM onboarding assistant.
''',
        "references": [
            "https://doi.org/10.1057/s41599-026-06594-5",
            "https://publichealth.jmir.org/2025/1/e65699",
            "https://doi.org/10.1038/s41893-024-01489-2",
            "https://doi.org/10.5334/cstp.812",
        ],
    },
    {
        "name": "ai-for-policy-briefs",
        "title": "AI for Policy Briefs",
        "description": "Converting scientific evidence and legislative text into concise, actionable policy briefs and impact analyses.",
        "devin_body": r'''## When to use

You need to turn a scientific paper, a body of evidence, or a legislative document into a short, decision-ready policy brief for government, agencies, or advocacy groups.

## Key concepts

- **Policy brief structure**: problem, evidence, policy options, recommendations, and implications.
- **Science-to-policy translation**: reframe technical findings into actionable, audience-specific guidance.
- **Stakeholder and impact analysis**: map who is affected, how, and what trade-offs exist.
- **Evidence synthesis**: combine multiple studies while tracking source credibility and recency.
- **Hallucination control**: policy briefs must not invent statistics, legal clauses, or citations.

## Code pattern

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Example: identify key themes across a set of policy documents
vectorizer = TfidfVectorizer(max_features=20, stop_words="english")
X = vectorizer.fit_transform(policy_docs)
print(vectorizer.get_feature_names_out())
```

## Tuning notes

- Tailor length and tone to the specific decision-maker and meeting context.
- Use verified sources (peer-reviewed research, official legislation, government data).
- Lead with the recommendation; support it with concise evidence and trade-offs.
- Have a policy expert review the brief before it reaches decision-makers.

## Verification

1. Generate a one-page brief from a scientific paper and compare it to a human-written brief.
2. Verify that every statistic and citation in the brief exists and is accurately represented.
3. Ask a policy professional to rate clarity, relevance, and actionability.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2509.21493",
            "https://openreview.net/forum?id=S6gJESWNSX",
            "https://doi.org/10.1038/d41586-023-02999-3",
            "https://algorithms.dk/responsible-use-of-ai-in-scientific-advice/",
        ],
    },
    {
        "name": "ai-for-white-papers",
        "title": "AI for White Papers",
        "description": "Authoring long-form, evidence-based white papers and thought-leadership documents grounded in verified sources.",
        "devin_body": r'''## When to use

You are producing a B2B or technical white paper that defines a problem, surveys evidence, presents a solution, and establishes thought leadership.

## Key concepts

- **Problem-solution narrative**: state the problem, quantify the cost, and present an evidence-based approach.
- **Executive summary**: write it last, place it first, and make it self-contained.
- **Evidence and case studies**: support claims with benchmarks, peer-reviewed studies, and real customer outcomes.
- **ROI and implementation**: include practical guidance on cost, benefits, and adoption.
- **Brand voice and design**: maintain a consistent, professional tone and visual format.

## Code pattern

```python
from jinja2 import Template

# Example: fill a white-paper outline template from structured evidence
template = Template(open("whitepaper_template.md").read())
doc = template.render(
    title="Edge AI for Manufacturing",
    problem="High latency and cloud costs",
    evidence=evidence_list,
)
```

## Tuning notes

- Decouple evidence retrieval from drafting; never let the model invent sources.
- Define audience, length, and sections before generating text.
- Use a second model or human reviewer to challenge unsupported claims.
- Export to editable formats (DOCX, PDF) with consistent styles and branding.

## Verification

1. Produce an executive summary and confirm it accurately reflects the full paper.
2. Spot-check every statistic and citation against its original source.
3. Compare the AI-assisted white paper to a prior human-written one for tone and structure.
''',
        "references": [
            "https://journals.sagepub.com/doi/10.1177/00472816251332208",
            "https://doi.org/10.1007/978-981-95-4632-9_10",
            "https://specswriter.com/blog/ai_white_papers_how_to_write_one_people_actually_finish.php",
            "https://www.qwe.edu.pl/tutorial/how-to-use-ai-to-write-white-papers/",
        ],
    },
    {
        "name": "ai-for-technical-blogs",
        "title": "AI for Technical Blogs",
        "description": "Planning, drafting, SEO-optimizing, and reviewing technical blog posts and tutorials with LLMs.",
        "devin_body": r'''## When to use

You are creating tutorials, engineering deep-dives, API explainers, or product announcements for a technical audience.

## Key concepts

- **Technical narrative**: combine motivation, concept, code, and outcome in a coherent arc.
- **Code-first examples**: include runnable snippets, output, and common pitfalls.
- **SEO and discoverability**: structure headings, metadata, and keywords for search and social sharing.
- **Audience calibration**: adjust depth for beginners, practitioners, or experts.
- **Expert review**: subject-matter experts should validate accuracy before publishing.

## Code pattern

```python
import frontmatter

# Example: write a structured Markdown post with YAML frontmatter
post = frontmatter.Post(
    content=draft_md,
    title="Getting Started with LoRA Fine-Tuning",
    tags=["machine-learning", "fine-tuning"],
    author="Your Name",
)
with open("post.md", "w") as f:
    f.write(frontmatter.dumps(post))
```

## Tuning notes

- Start with a strong outline and code examples; let the model expand, not invent.
- Run every code snippet in the target environment and include actual output.
- Keep the author's voice by editing extensively rather than publishing raw output.
- Add diagrams and alt text to make the post accessible and shareable.

## Verification

1. Publish a draft and compare reader engagement to a manually written baseline.
2. Run all code examples in a clean environment and confirm they execute correctly.
3. Ask a peer to rate technical accuracy, clarity, and usefulness.
''',
        "references": [
            "https://aclanthology.org/2026.findings-acl.296.pdf",
            "https://dev.to/neeraj_ciju/building-vtob-turning-youtube-videos-into-technical-blog-posts-with-a-multi-stage-ai-pipeline-1mng",
            "https://techwriting.pro/",
            "https://www.silverthreadlabs.com/products/bloggen",
            "https://github.com/SurajBhar/deep-blog-agent",
        ],
    },
    {
        "name": "ai-for-open-science",
        "title": "AI for Open Science",
        "description": "Reproducible research agents, open-source workbenches, provenance tracking, and computational reproducibility with AI.",
        "devin_body": r'''## When to use

You want to make a research project open, reproducible, and auditable by automating literature review, code execution, provenance tracking, and FAIR data packaging.

## Key concepts

- **Open science principles**: open data, code, protocols, preprints, and transparent methods.
- **Reproducibility and replication packages**: containerized, documented, and versioned artifacts.
- **Provenance and RO-Crate**: record the origin and transformation of every dataset, figure, and model.
- **AI research workbenches**: agents that search literature, run experiments, and write reports with traceability.
- **FAIR and knowledge graphs**: make data Findable, Accessible, Interoperable, and Reusable.

## Code pattern

```python
import hashlib

# Example: create a content hash to track data provenance
with open("data.csv", "rb") as f:
    digest = hashlib.sha256(f.read()).hexdigest()
print("data.csv sha256:", digest)
```

## Tuning notes

- Prefer open-weight or local models when handling sensitive research data.
- Version data, code, and environment definitions together.
- Document every assumption, parameter, and random seed.
- Have an independent run attempt to reproduce the key results.

## Verification

1. Hand the project to a colleague and ask them to reproduce the main result from the README.
2. Compare AI-generated analysis outputs to the original data and code.
3. Check that every figure can be traced back to the script and dataset that produced it.
''',
        "references": [
            "https://arxiv.org/abs/2412.17859",
            "https://github.com/synthetic-sciences/openscience",
            "https://github.com/opencodon/opencodon",
            "https://reproai.org/",
            "https://arxiv.org/abs/2409.11363",
        ],
    },
    {
        "name": "ai-for-data-journalism",
        "title": "AI for Data Journalism",
        "description": "Using AI to find stories in datasets, fact-check claims, generate visualizations, and produce data-driven reporting.",
        "devin_body": r'''## When to use

You are investigating public datasets, leaked documents, FOIA releases, or real-time data streams and need to find and verify stories at speed.

## Key concepts

- **Computational journalism**: algorithmic story discovery, monitoring, and verification.
- **Structured data parsing**: read CSV, JSON, PDF tables, and APIs with reproducible scripts.
- **Entity and anomaly detection**: identify people, organizations, and outliers in large corpora.
- **Verifiable claims**: every number, quote, and chart must link to the underlying source.
- **Document intelligence**: full-text search, named-entity recognition, and cross-document linking.

## Code pattern

```python
import pandas as pd
import altair as alt

# Example: explore a dataset and export an interactive chart
df = pd.read_csv("public_spending.csv")
chart = alt.Chart(df).mark_bar().encode(
    x="department:N",
    y="amount:Q",
)
chart.save("spending_chart.html")
```

## Tuning notes

- Clean and document every data transformation; share the analysis notebook.
- Cross-check surprising findings with the source agency or a domain expert.
- Avoid ecological fallacy; report uncertainty and sample limits.
- Protect sources and personally identifiable information.

## Verification

1. Replicate a published data story from raw data and compare the headline numbers.
2. Generate a chart and manually verify a subset of values against the source table.
3. Fact-check a generated claim by locating the exact sentence or row it came from.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2606.11176",
            "https://github.com/icij/datashare/",
            "https://datashare.icij.org/",
            "https://www.mdpi.com/2227-7080/10/3/68",
            "https://arxiv.org/abs/2409.07286",
        ],
    },
    {
        "name": "ai-for-visual-communication",
        "title": "AI for Visual Communication",
        "description": "Generating and refining posters, slides, brand assets, and visual narratives with diffusion models and design tools.",
        "devin_body": r'''## When to use

You need to create presentations, pitch decks, posters, social media assets, or brand visuals that communicate complex ideas clearly and consistently.

## Key concepts

- **Prompt engineering for visuals**: guide diffusion and layout models with precise, style-aware prompts.
- **Layout and composition**: balance text, images, whitespace, and hierarchy for the target medium.
- **Brand and style consistency**: enforce colors, fonts, and templates across generated variants.
- **ControlNet and structured generation**: constrain generation to layouts, sketches, or existing assets.
- **Human-in-the-loop**: AI drafts; designers refine for accuracy, accessibility, and taste.

## Code pattern

```python
from PIL import Image, ImageDraw, ImageFont

# Example: build a simple poster canvas in Python
canvas = Image.new("RGB", (1200, 1600), "white")
draw = ImageDraw.Draw(canvas)
draw.text((60, 60), "Research Highlights", fill="black")
canvas.save("poster_draft.png")
```

## Tuning notes

- Generate several variants and select the one that best matches the message.
- Check for visual artifacts, unintended bias, and misrepresentation of data.
- Export editable formats (SVG, PPTX) so designers can refine the output.
- Ensure accessible color contrast and include alt text for generated images.

## Verification

1. Produce a poster or slide deck and compare it to existing brand guidelines.
2. Test the visual with the target audience and measure comprehension and recall.
3. Review generated images for artifacts, false labels, and copyright issues.
''',
        "references": [
            "https://www.nature.com/articles/s41598-026-55838-6",
            "https://www.mdpi.com/2313-433X/11/9/289",
            "https://arxiv.org/abs/2604.04192v1",
            "https://doi.org/10.1016/j.heliyon.2024.e40037",
        ],
    },
    {
        "name": "ai-for-infographics",
        "title": "AI for Infographics",
        "description": "Generating data-rich infographics and visual stories from documents, tables, and natural-language prompts.",
        "devin_body": r'''## When to use

You want to turn reports, data tables, or articles into shareable infographics, data stories, or social-media explainers.

## Key concepts

- **Text-to-infographic**: generate metadata, chart code, and layout from natural language or documents.
- **Chart composition**: combine multiple sub-charts (bar, line, pie, maps) into a coherent layout.
- **Data faithfulness**: ensure values, labels, and visual proportions match the source data.
- **Visual hierarchy and accessibility**: guide the eye, use alt text, and maintain color-blind safe palettes.
- **Evaluation benchmarks**: use benchmarks like IGENBENCH to assess reliability of generated infographics.

## Code pattern

```python
import matplotlib.pyplot as plt

# Example: generate a chart component for later infographic assembly
categories = ["A", "B", "C"]
values = [12, 19, 8]
fig, ax = plt.subplots(figsize=(4, 3))
ax.bar(categories, values)
plt.savefig("chart_component.png")
```

## Tuning notes

- Verify every number and label against the source data table.
- Keep brand colors, fonts, and layout grids consistent.
- Avoid chart junk; prioritize the story over decoration.
- Test generated infographics with both data experts and general readers.

## Verification

1. Generate an infographic from a small table and verify every value and label.
2. Evaluate the output on a reliability benchmark or with a rubric for data faithfulness.
3. Compare engagement and comprehension between the infographic and the original table.
''',
        "references": [
            "https://aclanthology.org/2025.acl-long.1003.pdf",
            "https://aclanthology.org/2026.acl-long.1713.pdf",
            "https://aclanthology.org/anthology-files/anthology-files/pdf/acl/2023.acl-demo.11.pdf",
            "https://arxiv.org/abs/2401.13245",
            "https://arxiv.org/abs/2505.18668v3",
        ],
    },
    {
        "name": "ai-for-document-design",
        "title": "AI for Document Design",
        "description": "Automating layout, typography, templates, and multi-format rendering of reports, certificates, and proposals.",
        "devin_body": r'''## When to use

You need to produce many reports, certificates, proposals, invoices, or policy briefs from structured data while keeping layouts consistent and on-brand.

## Key concepts

- **Document layout generation**: produce structured page layouts from content and design constraints.
- **Template-based design**: create reusable templates with dynamic fields for text, tables, and images.
- **Data binding**: map CSV, JSON, or database records into document fields.
- **Multi-format rendering**: output PDF, DOCX, PPTX, or HTML from a single source of truth.
- **Typography and accessibility**: choose readable fonts, spacing, color contrast, and tagged PDFs.

## Code pattern

```python
from jinja2 import Template
from docx import Document

# Example: render a Word report from a template and data
template = Template(open("report_template.md").read())
rendered = template.render(data=records[0])
doc = Document()
doc.add_heading("Report", level=1)
doc.add_paragraph(rendered)
doc.save("report.docx")
```

## Tuning notes

- Design the template once and validate it before batch generation.
- Use conditional logic for optional sections and repeating rows for tables.
- Test page breaks, headers, and footers across edge cases.
- Add PDF/UA or DOCX accessibility tags where required.

## Verification

1. Generate 100 documents from a CSV and visually inspect for formatting consistency.
2. Compare a generated document to a manually produced reference for layout fidelity.
3. Validate that dynamic fields are correctly bound and no placeholder text remains.
''',
        "references": [
            "https://arxiv.org/abs/2510.26213v2",
            "https://doi.org/10.48550/arxiv.2303.10787",
            "https://dl.acm.org/doi/10.1007/978-3-031-41676-7_21",
            "https://www.box.com/docgen",
            "https://imaginepdf.com/",
        ],
    },
    {
        "name": "ai-for-knowledge-design",
        "title": "AI for Knowledge Design",
        "description": "Designing knowledge architectures, taxonomies, ontologies, and agent-facing knowledge layers for organizations.",
        "devin_body": r'''## When to use

You are building a knowledge base, wiki, documentation site, knowledge graph, or agent-facing memory system for a team or organization.

## Key concepts

- **Knowledge architecture**: structure content so both humans and AI agents can navigate it.
- **Taxonomies and ontologies**: define concepts, relations, and inference rules for a domain.
- **Knowledge graphs**: connect entities and facts for search, reasoning, and recommendation.
- **RAG vs persistent knowledge layers**: choose between retrieval at query time and curated, versioned knowledge stores.
- **Knowledge-as-code**: version-control knowledge in Markdown, YAML, or structured schemas.

## Code pattern

```python
import networkx as nx

# Example: build a small knowledge graph from extracted relationships
G = nx.DiGraph()
G.add_node("LoRA", type="technique")
G.add_node("Fine-tuning", type="task")
G.add_edge("LoRA", "Fine-tuning", relation="used_for")
print(nx.shortest_path(G, source="LoRA", target="Fine-tuning"))
```

## Tuning notes

- Start with the questions users and agents need to answer, then design the schema.
- Keep source attribution and freshness metadata on every knowledge unit.
- Use human-in-the-loop curation to avoid compounding AI-generated errors.
- Plan for both human-readable pages and machine-readable APIs/MCP interfaces.

## Verification

1. Build a knowledge graph for a domain and answer a set of representative queries.
2. Check coverage and freshness against a human-curated reference set.
3. Test that an agent can correctly retrieve and cite knowledge in downstream tasks.
''',
        "references": [
            "https://doi.org/10.1080/09544828.2026.2680617",
            "https://link.springer.com/chapter/10.1007/978-3-031-95901-1_1",
            "https://github.com/cantara/knowledge-context-protocol",
            "https://towardsdatascience.com/designing-a-persistent-knowledge-layer-that-refuses-to-guess/",
            "https://knowledge-as-code.com/",
        ],
    },
]
