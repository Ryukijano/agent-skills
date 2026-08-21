SKILLS = [
    {
        "name": "ai-for-e-government",
        "title": "AI for E-Government",
        "description": "Automates citizen-facing public services through conversational agents, document processing, and proactive eligibility screening.",
        "devin_body": r'''## When to use

You are modernizing digital government services, automating citizen inquiries, or designing proactive, citizen-centric public service delivery.

## Usage

- **Citizen chatbots and voice assistants**: answer FAQs, guide form completion, and route complex queries using services such as Portugal's ePortugal Virtual Assistant or India's Jan-Sahayak.
- **Document processing and pre-fill**: extract fields from submissions, classify requests, and auto-populate forms with NLP/LLM pipelines.
- **Proactive eligibility screening**: match residents to benefits, send renewal reminders, and flag missing documents.
- **Responsible AI governance**: monitor responses for bias, maintain audit trails, and provide human escalation paths.

## Steps

1. Map high-volume citizen journeys and identify service pain points.
2. Curate official policy documents, forms, and FAQs into a vetted knowledge base.
3. Build a retrieval-augmented generation or conversational pipeline grounded in authoritative sources.
4. Pilot with one service, measuring deflection, resolution, and satisfaction.
5. Audit outputs for accuracy, fairness, and accessibility before scaling.

## Code pattern

```python
from transformers import pipeline

# Answer citizen questions from a policy document
qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
context = "Citizens may renew a driver's license online if no address change is required."
result = qa(question="Can I renew my license online?", context=context)
print(result["answer"])
```

## Tuning notes

- Ground chatbots in official knowledge bases to reduce hallucination.
- Provide escalation paths to human staff and clear audit trails.
- Test for accessibility, multilingual support, and bias.

## Verification

1. Deploy a chatbot on a service page and measure deflection and resolution rates.
2. Run a document extraction pipeline and compare to a manual baseline.
3. Audit a sample of model responses for accuracy and fairness.

''',
        "references": [
            "https://www.mdpi.com/2227-9709/12/3/98",
            "https://doi.org/10.1016/j.heliyon.2024.e40591",
            "https://thedocs.worldbank.org/en/doc/a2d967023f2d5cba345a3a2b9d72f837-0050062026/original/How-Is-Government-Using-AI-final.pdf",
            "https://dl.acm.org/doi/10.1007/978-3-032-01589-1_25",
        ],
    },
    {
        "name": "ai-for-civic-tech",
        "title": "AI for Civic Tech",
        "description": "Supports participatory democracy by analyzing public comments, mapping priorities, and summarizing deliberation themes.",
        "devin_body": r'''## When to use

You are facilitating public participation, analyzing community input, or building tools for deliberative democracy and civic engagement.

## Usage

- **Public comment analysis**: classify, summarize, and cluster feedback from consultations using NLP and topic modeling.
- **Participatory budgeting**: visualize trade-offs, recommend allocations, and report community priorities.
- **Deliberation support**: identify consensus, surface concerns, and map argument themes from town halls or digital platforms.
- **Civic chatbots and issue mapping**: answer local questions and collect georeported community input.

## Steps

1. Define participation goals and target communities.
2. Collect comments, surveys, and petitions from platforms such as Commonplace or DIPAS, then redact PII.
3. Use open-source NLP or LLMs to summarize themes, sentiment, and geographic patterns.
4. Validate AI themes against manual coding and report findings back to participants.
5. Track demographic reach and the actionability of recommendations.

## Code pattern

```python
from transformers import pipeline

# Summarize and classify public comments
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
comments = [
    "We need more bike lanes on Main Street.",
    "The new park should include a playground and shade.",
]
summary = summarizer(" ".join(comments), max_length=60, min_length=20)
print(summary[0]["summary_text"])
```

## Tuning notes

- Protect privacy and anonymity in civic data.
- Avoid over-aggregating minority voices; disclose methods.
- Pair quantitative summaries with opportunities for deeper deliberation.

## Verification

1. Compare AI themes to a manual thematic analysis of a sample.
2. Measure participation reach across demographic groups.
3. Evaluate feedback reports for actionability and transparency.

''',
        "references": [
            "https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/07/artificial-intelligence-and-the-future-of-citizen-participation_0608e00e/a1ee2e0a-en.pdf",
            "https://journals.sagepub.com/doi/full/10.1177/23998083241296200",
            "https://www.europarl.europa.eu/RegData/etudes/STUD/2026/774753/EPRS_STU(2026)774753_EN.pdf",
            "https://www.cambridge.org/core/journals/data-and-policy/article/ai-and-citizen-participation-a-political-economy-lens/2A4CC7AAA4F24F5C10CFC9D606EE5E5B",
        ],
    },
    {
        "name": "ai-for-public-transport",
        "title": "AI for Public Transport",
        "description": "Optimizes transit operations with ridership forecasts, dynamic scheduling, and real-time disruption recovery.",
        "devin_body": r'''## When to use

You are optimizing bus/rail operations, forecasting ridership, planning schedules, or recovering from transit disruptions.

## Usage

- **Ridership forecasting**: predict passenger flows by route, stop, and time using GTFS, AFC, and weather data.
- **Dynamic headways and scheduling**: adjust frequencies, fleet rosters, and vehicle assignments to match demand and reduce crowding.
- **Disruption recovery**: re-route vehicles and push passenger alerts during incidents and special events.
- **Demand-responsive transit**: match on-demand shuttles with riders and integrate trains, buses, bikeshare, and ride-hail feeds.

## Steps

1. Ingest GTFS, AVL, AFC, and passenger count data.
2. Build short- to medium-term forecasting models with seasonality, weather, and event features.
3. Simulate headway, fleet, and route scenarios against cost and service targets.
4. Deploy real-time decision support for dispatchers and operations centers.
5. Backtest forecasts and measure on-time performance, crowding, and equity.

## Code pattern

```python
import pandas as pd
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA

# Forecast daily ridership by route
sf = StatsForecast(df=df, models=[AutoARIMA(season_length=7)], freq="D", n_jobs=-1)
fcst = sf.forecast(h=14)
print(fcst.head())
```

## Tuning notes

- Account for special events, weather, and disruptions.
- Use hierarchical reconciliation across routes and stops.
- Balance efficiency, accessibility, and coverage.

## Verification

1. Backtest ridership forecasts against actuals.
2. Compare optimized schedules to current headways using a simulator.
3. Measure on-time performance and rider satisfaction.

''',
        "references": [
            "https://www.mdpi.com/2624-6511/8/3/87",
            "https://doi.org/10.1109/tits.2025.3603963",
            "https://dl.acm.org/doi/10.1109/TITS.2020.3041234",
            "https://www.mdpi.com/2079-9292/14/12/2359",
        ],
    },
    {
        "name": "ai-for-public-utilities",
        "title": "AI for Public Utilities",
        "description": "Detect leaks and anomalies across water and energy smart-meter networks to cut non-revenue water and response times.",
        "devin_body": r'''## When to use

You are managing electricity, water, or gas distribution, forecasting demand, detecting faults, or optimizing infrastructure assets.

## Usage

- **Demand forecasting**: predict electricity, water, and gas consumption using AMI, SCADA, GIS, and weather feeds.
- **Leak and outage detection**: identify anomalies in pressure, flow, voltage, and meter data.
- **Asset health scoring**: rank transformers, pumps, pipes, and meters for risk-based maintenance.
- **Conservation and voltage optimization**: reduce peak demand, non-revenue water, and distribution losses.

## Steps

1. Integrate AMI, SCADA, GIS, weather, and customer data into a unified time-series platform.
2. Build forecasting and anomaly models for demand, leaks, and voltage deviations.
3. Prioritize maintenance and inspections by risk score and consequence.
4. Deploy real-time dashboards and alerts for control-room operators.
5. Validate with field crews and operational outcomes, retraining as DERs and demand patterns evolve.

## Code pattern

```python
from sklearn.ensemble import IsolationForest
import pandas as pd

# Anomaly detection on smart meter load profiles
X = df[["hour", "load_kw", "temp_c", "day_of_week"]]
clf = IsolationForest(contamination=0.01, random_state=42)
df["anomaly"] = clf.fit_predict(X)
```

## Tuning notes

- Combine physics-based and data-driven models.
- Respect privacy and cybersecurity in critical infrastructure.
- Update models frequently as demand patterns and DERs evolve.

## Verification

1. Forecast next-day demand and compare to a naive baseline.
2. Detect a synthetic leak or outage event.
3. Compare predictive maintenance schedules to historical failure records.

''',
        "references": [
            "https://www.publicpower.org/periodical/article/illinois-public-power-community-deploys-ai-advanced-grid-management",
            "https://aws.amazon.com/blogs/industries/building-autonomous-water-utility-operations-with-agentic-ai-on-aws/",
            "https://doi.org/10.1109/csitss67709.2025.11295772",
            "https://dewa.gov.ae/en/about-us/media-publications/latest-news/2026/1/dewa-deploys-intelligence-data-modelling-software-for-faster-operational-response",
        ],
    },
    {
        "name": "ai-for-taxation",
        "title": "AI for Taxation",
        "description": "Prioritizes tax audits and flags non-compliance by scoring returns, third-party data, and network relationships.",
        "devin_body": r'''## When to use

You are modernizing tax administration, detecting non-compliance, prioritizing audits, or assisting taxpayers with filings.

## Usage

- **Risk scoring and audit selection**: prioritize returns and transactions by compliance risk.
- **Fraud and evasion detection**: flag refund scams, under-reporting, and shell-company networks.
- **Taxpayer assistance**: answer filing questions and guide compliance through chatbots and portals.
- **Revenue forecasting and policy impact**: predict collections and simulate tax-policy changes.

## Steps

1. Integrate tax returns, payments, third-party data, and entity network relationships.
2. Build supervised and unsupervised risk models with explainable scores.
3. Implement human-in-the-loop review for high-stakes audit selection.
4. Deploy taxpayer-facing assistants and monitor resolution and accuracy rates.
5. Monitor fairness, revenue impact, and model drift against audit outcomes.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = df[["income", "deductions", "third_party", "history_flags"]]
y = df["audit_outcome"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
clf = RandomForestClassifier(random_state=42, class_weight="balanced").fit(X_train, y_train)
```

## Tuning notes

- Avoid bias against compliant taxpayers; use outcome-based fairness checks.
- Maintain confidentiality and legal safeguards for taxpayer data.
- Validate model predictions against independent audit samples.

## Verification

1. Compare audit yield of the model to random selection.
2. Audit a sample of low- and high-risk cases for fairness.
3. Test a taxpayer chatbot on real FAQs.

''',
        "references": [
            "https://www.imf.org/en/publications/tnm/issues/2024/11/21/understanding-artificial-intelligence-in-tax-and-customs-administration-555097",
            "https://www.imf.org/en/publications/tnm/issues/2025/08/09/generative-artificial-intelligence-for-compliance-risk-analysis-applications-in-tax-and-567429",
            "https://oecd.ai/en/gov/issues/tax-administration",
            "https://doi.org/10.1080/2573234x.2026.2644363",
        ],
    },
    {
        "name": "ai-for-budgeting",
        "title": "AI for Budgeting",
        "description": "Forecasts expenditures and simulates fiscal scenarios to optimize program allocations and spending controls.",
        "devin_body": r'''## When to use

You are preparing government budgets, forecasting expenditures, optimizing allocations, or analyzing fiscal scenarios.

## Usage

- **Expenditure and revenue forecasting**: predict spending by program and time horizon using historical execution and macro data.
- **Allocation optimization**: balance priorities under fiscal constraints and policy goals.
- **Scenario analysis**: simulate economic shocks, policy changes, and revenue shortfalls.
- **Spending anomaly detection**: flag unusual commitments, cost overruns, and reallocation patterns.

## Steps

1. Gather historical budgets, execution data, and macroeconomic indicators.
2. Build hierarchical forecasting models for revenue and expenditure lines.
3. Define objectives, constraints, and policy priorities.
4. Run optimization or simulation to compare budget scenarios.
5. Validate projections with finance officers and publish confidence intervals.

## Code pattern

```python
import xgboost as xgb
from sklearn.model_selection import TimeSeriesSplit

# Expenditure forecasting with gradient boosting
X = df[["quarter", "program", "prior_year", "gdp_growth"]]
y = df["expenditure"]
for train_idx, test_idx in TimeSeriesSplit(n_splits=3).split(X):
    model = xgb.XGBRegressor(random_state=42).fit(X.iloc[train_idx], y.iloc[train_idx])
```

## Tuning notes

- Use hierarchical reconciliation across agencies and functions.
- Document assumptions and confidence intervals for fiscal decisions.
- Avoid over-fitting to historical patterns with cross-validation.

## Verification

1. Forecast next-year expenditures and compare to official estimates.
2. Optimize a small allocation problem and check constraint satisfaction.
3. Stress-test a budget scenario against adverse macro shocks.

''',
        "references": [
            "https://doi.org/10.3390/electronics14204047",
            "https://oecd.ai/en/gov-issues-public-financial-management",
            "https://publicacoes.tesouro.gov.br/index.php/cadernos/article/download/284/362/1145",
            "https://www.cambridge.org/core/journals/data-and-policy/article/an-exploratory-hybrid-ai-workflow-for-brazilian-federal-budget-allocation/69F3EA6EAE0CAA37FE36E3E2B810FF72",
        ],
    },
    {
        "name": "ai-for-social-services",
        "title": "AI for Social Services",
        "description": "Matches clients to benefits and services by triaging eligibility, risk, and available community resources.",
        "devin_body": r'''## When to use

You are supporting social service delivery, eligibility determination, case prioritization, or benefit navigation.

## Usage

- **Eligibility pre-screening**: triage applicants for benefits and services.
- **Case prioritization**: rank cases by risk, urgency, and complexity.
- **Resource matching**: connect clients to housing, food, health, and employment programs.
- **Caseworker support**: summarize case notes, suggest next steps, and check policy.

## Steps

1. Map programs, eligibility rules, and referral pathways.
2. Collect client, program, and service data with consent and data minimization.
3. Build rule-based and ML triage models with explainable outputs.
4. Provide human review for high-stakes benefit and placement decisions.
5. Track outcomes, wait times, and access disparities across groups.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingClassifier

# Risk triage for case prioritization
X = df[["age", "household_size", "income", "prior_interactions"]]
y = df["high_need"]
model = GradientBoostingClassifier(random_state=42).fit(X, y)
df["risk_score"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Prioritize equity, consent, and data minimization.
- Keep humans in the loop for benefit and placement decisions.
- Monitor for disparate impact on protected groups.

## Verification

1. Compare triage model outcomes to expert social-worker rankings.
2. Build an eligibility screener and test against known cases.
3. Measure reduction in time-to-service and access gaps.

''',
        "references": [
            "https://sage.cnpereading.com/doi/10.1177/10497315251350933",
            "https://www.mathematica.org/publications/navigating-genai-in-child-welfare-quick-start-guide-for-agency-leaders",
            "https://digitalgovernmenthub.org/publications/ai-powered-rules-as-code-experiments-with-public-benefits-policy/",
            "https://doi.org/10.1145/3491102.3517439",
        ],
    },
    {
        "name": "ai-for-veterans-services",
        "title": "AI for Veterans Services",
        "description": "Accelerates veteran benefit claims and care coordination by triaging cases, summarizing evidence, and scheduling services.",
        "devin_body": r'''## When to use

You are improving access to benefits, healthcare, and memorial services for veterans, or streamlining VA claims and casework.

## Usage

- **Claims triage and routing**: prioritize and summarize disability claims evidence.
- **Benefits matching**: match veterans to eligible programs and track status.
- **Clinical decision support**: identify risk, predict readmissions, and suggest care.
- **Veteran-facing assistants**: provide plain-language answers and appointment scheduling.

## Steps

1. Integrate veteran health, benefits, service, and administrative records.
2. Build NLP and classification models for claims and eligibility.
3. Implement human-in-the-loop review and appeal processes.
4. Deploy veteran-facing tools with plain-language guidance.
5. Monitor accuracy, wait times, and trust.

## Code pattern

```python
from transformers import pipeline

# Summarize a claims evidence document
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
text = "The veteran served in... [medical evidence]..."
summary = summarizer(text, max_length=80, min_length=20)
print(summary[0]["summary_text"])
```

## Tuning notes

- Maintain veteran privacy and PII safeguards.
- Keep veterans and staff in control of final decisions.
- Evaluate for disability-group fairness and explainability.

## Verification

1. Compare AI-summarized claims to adjudicator summaries.
2. Test a veteran-facing chatbot on common benefit questions.
3. Track reduction in claims processing time and appeals.

''',
        "references": [
            "https://department.va.gov/ai/building-the-future-vas-strategy-for-adopting-high-impact-artificial-intelligence-to-improve-services-for-veterans/",
            "https://department.va.gov/ai/ai-use-case-inventory/",
            "https://www.gao.gov/assets/890/887587.pdf",
            "https://department.va.gov/privacy/wp-content/uploads/sites/5/2026/05/FY26ArtificialIntelligenceClaimsEvaluationSystemAICESPIA.pdf",
        ],
    },
    {
        "name": "ai-for-public-records",
        "title": "AI for Public Records",
        "description": "Classifies, appraises, and redacts born-digital government records to accelerate archival review and public access.",
        "devin_body": r'''## When to use

You are managing born-digital government records, reducing archival backlogs, or improving public access to official documents.

## Usage

- **Records classification and retention**: assign retention, security, and access labels.
- **Sensitivity review and redaction**: flag personal, classified, or confidential content.
- **Metadata extraction**: identify entities, dates, and topics for search and discovery.
- **Appraisal and selection**: surface historically significant material for transfer.

## Steps

1. Inventory records formats, systems, and retention schedules.
2. Pre-process text, images, audio, and structured data from repositories.
3. Train or apply classifiers for sensitivity, retention, and PII.
4. Route uncertain cases to records professionals for review.
5. Publish approved records with rich metadata and redactions.

## Code pattern

```python
import re

# Detect and redact potential PII in a document
text = "John Doe, SSN 123-45-6789, lives at 123 Main St."
redacted = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[REDACTED]", text)
print(redacted)
```

## Tuning notes

- Keep a human-in-the-loop for final retention and sensitivity decisions.
- Document provenance and model decisions for legal defensibility.
- Balance transparency against privacy and national security.

## Verification

1. Classify a sample of records and compare to archivist labels.
2. Process a backlog and measure throughput and accuracy.
3. Review redaction quality and public access outcomes.

''',
        "references": [
            "https://zenodo.org/records/18935870",
            "https://www.gov.uk/algorithmic-transparency-records/cabinet-office-automated-digital-document-review",
            "https://www.ukri.org/who-we-are/how-we-are-doing/research-outcomes-and-impact/ahrc/ai-for-accountability-unlocking-uk-digital-records/",
            "https://link.springer.com/article/10.1007/s00146-025-02221-0",
        ],
    },
    {
        "name": "ai-for-urban-planning",
        "title": "AI for Urban Planning",
        "description": "Generates land-use scenarios and simulates urban growth to balance density, accessibility, and sustainability.",
        "devin_body": r'''## When to use

You are developing land-use plans, simulating urban growth, designing neighborhoods, or engaging communities in planning.

## Usage

- **Land-use optimization**: allocate residential, commercial, and green spaces across scenarios.
- **Urban digital twins**: simulate mobility, energy, and environmental impacts at city scale.
- **Scenario simulation**: test zoning, density, and infrastructure options using agent-based and cellular models.
- **Participatory planning**: analyze public input and design trade-offs with stakeholder feedback.

## Steps

1. Define planning goals, constraints, and stakeholder objectives.
2. Collect geospatial, demographic, environmental, and mobility data.
3. Build or use spatial optimization and simulation models.
4. Co-design scenarios with planners and the public.
5. Evaluate alternatives on equity, sustainability, and feasibility.

## Code pattern

```python
import geopandas as gpd

# Compute zoning compliance area for a parcel
gdf = gpd.read_file("parcels.geojson")
gdf["allowed_units"] = (gdf["area_m2"] * gdf["floor_area_ratio"]) / gdf["unit_size"]
print(gdf[["parcel_id", "allowed_units"]].head())
```

## Tuning notes

- Combine AI suggestions with professional planner judgment.
- Validate model outputs with community priorities and legal constraints.
- Use high-quality, interoperable geospatial data.

## Verification

1. Generate a set of spatial plans and compare to expert designs.
2. Simulate a policy scenario and compare predicted outcomes.
3. Conduct a participatory review of AI-assisted alternatives.

''',
        "references": [
            "https://www.nature.com/articles/s43588-025-00846-1",
            "https://www.nature.com/articles/s43588-023-00503-5",
            "https://www.mdpi.com/2073-445X/12/7/1315",
            "https://www.sciencedirect.com/science/article/abs/pii/S0169204625000441",
        ],
    },
    {
        "name": "ai-for-zoning",
        "title": "AI for Zoning",
        "description": "Answers zoning questions and checks parcel compliance against local codes using retrieval-augmented code assistants.",
        "devin_body": r'''## When to use

You are interpreting zoning codes, checking compliance, answering applicant questions, or analyzing land-use regulations.

## Usage

- **Code Q&A**: answer natural-language questions about zoning rules and permitted uses.
- **Compliance checks**: determine whether a proposal meets code requirements and overlays.
- **Variance and exception analysis**: identify required approvals or waivers.
- **GIS-linked mapping**: reconcile zoning districts with environmental and historic layers.

## Steps

1. Digitize zoning code text, maps, and related regulations into a corpus.
2. Build a retrieval-augmented generation pipeline over the vetted code.
3. Validate answers against authoritative code sections and map overlays.
4. Integrate with GIS for parcel-based compliance checks.
5. Monitor Q&A logs for errors, bias, and outdated answers.

## Code pattern

```python
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Build a simple RAG index over a zoning code
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_texts(zoning_paragraphs, embeddings)
```

## Tuning notes

- Keep the code corpus up to date and cite sources in every answer.
- Disclose when a question requires professional planning review.
- Test for consistency across similar questions and parcel types.

## Verification

1. Test the Q&A system against a set of known zoning questions.
2. Compare AI compliance determinations to staff determinations.
3. Track applicant satisfaction and time saved.

''',
        "references": [
            "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5218771",
            "https://www.urban.org/urban-wire/how-can-local-governments-use-ai-answer-community-members-questions-about-zoning-and",
            "https://iopscience.iop.org/article/10.1088/1755-1315/1648/1/012010",
            "https://link.springer.com/chapter/10.1007/978-3-031-86039-3_9",
        ],
    },
    {
        "name": "ai-for-permitting",
        "title": "AI for Permitting",
        "description": "Pre-screens permit applications and checks plan compliance against building and zoning codes to shorten review cycles.",
        "devin_body": r'''## When to use

You are streamlining building or development permits, automating intake screening, or supporting plan review.

## Usage

- **Application pre-screening**: check completeness and required documents.
- **Plan review**: detect code issues and compare against building and zoning codes.
- **Code compliance**: flag violations and cite relevant sections.
- **Workflow routing**: assign applications to reviewers by type and complexity.
- **Status and Q&A**: keep applicants informed and answer common questions.

## Steps

1. Map permit types, checklists, and review workflows.
2. Ingest application forms, drawings, and supporting documents.
3. Build rules and ML models for completeness and compliance checks.
4. Route flagged items to human reviewers with explanations.
5. Track cycle times, first-pass approval rates, and rework.

## Code pattern

```python
import pytesseract
from PIL import Image

# Extract text from a scanned permit drawing
img = Image.open("site_plan.pdf")
text = pytesseract.image_to_string(img)
print(text[:500])
```

## Tuning notes

- Preserve human approval authority and auditability.
- Train models on local codes and amendments.
- Handle scanned drawings and PDFs with OCR and computer vision.

## Verification

1. Run a sample of applications through pre-screening and compare to staff review.
2. Measure change in first-pass approval rate and cycle time.
3. Audit a sample of AI-flagged code issues for accuracy.

''',
        "references": [
            "https://innovation-hub.seattle.gov/2026/06/17/ai-construction-permitting-seattle-civcheck-study/",
            "https://www.govtech.com/artificial-intelligence/honolulu-launches-ai-assisted-fast-track-permit-review",
            "https://www.archistar.ai/aiprecheck/ai-plan-review/",
            "https://iopscience.iop.org/article/10.1088/1755-1315/1648/1/012010",
        ],
    },
]
