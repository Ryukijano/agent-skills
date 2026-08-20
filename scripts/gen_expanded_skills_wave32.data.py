SKILLS = [
    {
        "name": "ai-for-management-consulting",
        "title": "AI for Management Consulting",
        "description": "Accelerate diagnostic research, market sizing, client synthesis, and GenAI-assisted advisory workflows while managing epistemic risk.",
        "devin_body": r'''
## When to use

You are building AI-augmented consulting workflows for market analysis, synthesis of client data, hypothesis generation, or executive-ready deliverables.

## Key concepts

- **Task-GenAI fit**: decide where to automate, augment, or avoid GenAI based on ambiguity and stakes.
- **Knowledge synthesis**: summarize interviews, documents, and benchmarks into defensible insights.
- **Market sizing and scenario modeling**: combine structured data with LLM-driven assumptions.
- **Epistemic risk and source grounding**: validate AI output against client facts and cited sources.

## Code pattern

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Cluster similar client documents or interview transcripts
vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
X = vec.fit_transform(documents)
sim = cosine_similarity(X)
```

## Tuning notes

- Keep human consultants in the loop for ambiguous, high-stakes judgments.
- Trace every AI-generated claim to a source document or dataset.
- Calibrate outputs to client style, confidentiality, and ethical standards.
- Monitor for hallucinations and over-reliance on generic benchmarks.

## Verification

1. Build a document-synthesis pipeline and compare output to a manually written summary.
2. Run a market-sizing model and verify inputs against published data.
3. Audit a sample of GenAI outputs for factual accuracy and source attribution.
''',
        "references": [
            "https://doi.org/10.1007/s12599-026-00992-4",
            "https://www.wi.uni-muenster.de/research/publications/193019598",
            "https://doi.org/10.1016/j.infoandorg.2025.100559",
            "https://arxiv.org/abs/2409.06643",
        ],
    },
    {
        "name": "ai-for-strategy",
        "title": "AI for Strategy",
        "description": "Data-driven strategy formulation, competitive scenario modeling, market sensing, and AI-augmented strategic decision-making.",
        "devin_body": r'''
## When to use

You are formulating corporate strategy, evaluating strategic options, sensing market shifts, or building decision support for leadership choices.

## Key concepts

- **Strategic decision-making with AI**: augment search, representation, and aggregation of strategic options.
- **Scenario and war-gaming models**: simulate competitive dynamics and uncertainty.
- **Outside view and base rates**: calibrate strategic plans with reference-class forecasting.
- **Strategy analytics**: apply causal and predictive models to resource allocation.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict strategic initiative value from market and firm features
X = df[["market_growth", "competitive_intensity", "investment", "capability"]]
y = df["value_created"]
model = GradientBoostingRegressor(n_estimators=300, random_state=42).fit(X, y)
```

## Tuning notes

- Avoid overfitting to a single scenario; test across multiple futures.
- Combine internal data with external market and macro signals.
- Maintain executive judgment as the final arbiter of strategic choices.
- Document assumptions and confidence intervals for each recommendation.

## Verification

1. Build a strategic initiative valuation model and backtest on historical outcomes.
2. Run a scenario simulation and compare results to a static strategic plan.
3. Evaluate whether AI insights change resource-allocation priorities in a blind test.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2408.08811",
            "https://arxiv.org/pdf/2210.12373",
            "https://arxiv.org/abs/2404.01230",
            "https://arxiv.org/abs/2412.13013",
        ],
    },
    {
        "name": "ai-for-innovation-management",
        "title": "AI for Innovation Management",
        "description": "Idea generation, R&D portfolio prioritization, trend forecasting, and AI-enabled new product development.",
        "devin_body": r'''
## When to use

You are managing an innovation pipeline, prioritizing R&D projects, forecasting technology trends, or accelerating concept-to-launch cycles.

## Key concepts

- **Idea mining and generation**: extract and evaluate ideas from patents, papers, and customer signals.
- **Portfolio prioritization**: rank projects by strategic fit, risk, and expected value.
- **Trend and weak-signal detection**: forecast emerging technologies and customer needs.
- **Stage-gate acceleration**: use AI to screen concepts and reduce uncertainty early.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Score project ideas by likelihood of stage-gate success
features = ["novelty", "strategic_fit", "technical_risk", "market_size"]
clf = RandomForestClassifier(class_weight="balanced", random_state=42).fit(X[features], y_pass)
```

## Tuning notes

- Balance exploration and exploitation in the portfolio.
- Validate trend models against expert forecasts and external data.
- Use embeddings to link ideas to prior art and customer pain points.
- Avoid hype cycles; measure incremental value and learning per project.

## Verification

1. Score a set of project ideas and compare to expert rankings.
2. Build a trend-forecasting model and evaluate directional accuracy.
3. Track stage-gate outcomes for AI-screened vs manually screened concepts.
''',
        "references": [
            "https://doi.org/10.1016/j.techfore.2020.120392",
            "https://doi.org/10.1016/j.technovation.2024.103081",
            "https://doi.org/10.1016/j.jbusres.2024.114542",
            "https://doi.org/10.1016/j.techfore.2022.121598",
        ],
    },
    {
        "name": "ai-for-knowledge-management",
        "title": "AI for Knowledge Management",
        "description": "Semantic knowledge search, enterprise RAG, expertise mining, and AI-assisted capture of institutional tacit knowledge.",
        "devin_body": r'''
## When to use

You need to make organizational knowledge searchable, capture tacit expertise, build enterprise RAG, or recommend relevant experts and documents.

## Key concepts

- **Enterprise RAG**: ground LLM answers in internal documents and wikis.
- **Knowledge graphs**: connect people, projects, and concepts across the organization.
- **Expertise mining**: identify who knows what from publications, projects, and communications.
- **Tacit knowledge capture**: turn meetings, tickets, and chats into reusable assets.

## Code pattern

```python
from sentence_transformers import SentenceTransformer

# Embed documents for semantic search and RAG retrieval
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(documents)
```

## Tuning notes

- Chunk documents to balance context length and retrieval precision.
- Refresh embeddings as documents and expertise evolve.
- Enforce access controls and confidentiality in search and RAG.
- Combine vector search with keyword and graph-based reranking.

## Verification

1. Build an enterprise search and measure nDCG against a labeled test set.
2. Run a RAG pipeline and verify answers cite the correct source passages.
3. Mine expert profiles and validate recommendations with peer feedback.
''',
        "references": [
            "https://doi.org/10.3389/frai.2025.1595930",
            "https://arxiv.org/abs/2607.02609",
            "https://link.springer.com/article/10.1007/s44163-026-01780-5",
            "https://doi.org/10.2478/czoto-2024-0027",
        ],
    },
    {
        "name": "ai-for-project-management",
        "title": "AI for Project Management",
        "description": "Schedule and cost forecasting, risk triage, resource optimization, and AI-driven project health monitoring.",
        "devin_body": r'''
## When to use

You are planning or executing projects and need to forecast duration, cost, risk, or resource bottlenecks across the project lifecycle.

## Key concepts

- **Predictive project analytics**: forecast cost, schedule, and risk from historical data.
- **Resource and schedule optimization**: allocate people and tasks under constraints.
- **Project health scoring**: aggregate scope, schedule, cost, and stakeholder signals.
- **Natural-language project data**: extract risks and issues from status reports and emails.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingRegressor

# Forecast project cost overrun from scope, team, and risk features
X = df[["team_size", "duration_weeks", "requirements_change_rate", "risk_score"]]
y = df["cost_overrun_pct"]
model = GradientBoostingRegressor(n_estimators=300, random_state=42).fit(X, y)
```

## Tuning notes

- Use chronological splits to avoid leakage from future status updates.
- Weight recent projects more heavily because processes and tools evolve.
- Integrate with PMBOK/Agile processes; do not replace governance.
- Explain predictions to project managers for actionable mitigation.

## Verification

1. Build a cost-overrun forecast and backtest on completed projects.
2. Predict schedule slippage and compare to a critical-path baseline.
3. Triage at-risk projects and validate against manager assessments.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2601.16392",
            "https://arxiv.org/pdf/2604.21958",
            "https://arxiv.org/pdf/2506.02214",
            "https://arxiv.org/abs/2604.13814v1",
        ],
    },
    {
        "name": "ai-for-change-management",
        "title": "AI for Change Management",
        "description": "Stakeholder sentiment monitoring, adoption analytics, training personalization, and AI-assisted transformation communications.",
        "devin_body": r'''
## When to use

You are leading organizational change, tracking adoption, personalizing enablement, or tailoring communications to stakeholder segments.

## Key concepts

- **Stakeholder sensing**: classify sentiment, concerns, and readiness from surveys and messages.
- **ADKAR and behavioral stages**: map AI interventions to awareness, desire, knowledge, ability, reinforcement.
- **Personalized learning paths**: recommend training and nudges by role and gap.
- **Change communication optimization**: generate targeted messaging and FAQs.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Predict employee readiness for a change initiative
X = df[["tenure", "prior_change_exposure", "sentiment_score", "manager_support"]]
y = df["ready"]
clf = RandomForestClassifier(class_weight="balanced", random_state=42).fit(X, y)
```

## Tuning notes

- Anchor AI output in change-management frameworks like ADKAR or Kotter.
- Protect employee privacy and avoid surveillance perceptions.
- Validate sentiment models with qualitative feedback and focus groups.
- Pair AI-generated content with human oversight for tone and trust.

## Verification

1. Classify stakeholder sentiment and compare to survey results.
2. Build a readiness model and validate against actual adoption outcomes.
3. Test personalized communication and measure engagement lift.
''',
        "references": [
            "https://arxiv.org/abs/2510.19997",
            "https://arxiv.org/abs/2411.08693",
            "https://aaltodoc.aalto.fi/items/f95a2878-deed-4814-bf3c-e326a4a1dc8d",
            "https://www.inderscience.com/info/inarticle.php?artid=132074",
        ],
    },
    {
        "name": "ai-for-operations-management",
        "title": "AI for Operations Management",
        "description": "Process mining, service-level optimization, quality control, and AI-driven operational decision support.",
        "devin_body": r'''
## When to use

You are optimizing business processes, improving service levels, monitoring quality, or augmenting operational decisions with data and AI.

## Key concepts

- **Process mining and discovery**: reconstruct workflows from event logs.
- **Service-level optimization**: balance demand, capacity, and waiting times.
- **Quality and anomaly detection**: monitor SPC, defect patterns, and drift.
- **Human-AI teaming**: design trust, incentives, and escalation in operations.

## Code pattern

```python
import pandas as pd
from scipy.optimize import linprog

# Simple staff-allocation LP to minimize cost while meeting service levels
c = hourly_cost
A_ub = -demand_by_hour
b_ub = -service_level_requirements
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(0, max_staff))
```

## Tuning notes

- Combine prediction with optimization for decision-centric value.
- Model variability and queue dynamics, not just average demand.
- Use process-mining outputs to validate assumptions before building models.
- Keep humans accountable for high-consequence operational calls.

## Verification

1. Mine a process from event logs and compare to an as-designed map.
2. Optimize staffing or inventory and measure service-level improvement.
3. Deploy an anomaly detector and validate against known quality issues.
''',
        "references": [
            "https://arxiv.org/abs/2507.17927",
            "https://arxiv.org/abs/2505.13580",
            "https://arxiv.org/abs/2510.03310",
            "https://arxiv.org/pdf/2601.06061",
        ],
    },
    {
        "name": "ai-for-risk-management",
        "title": "AI for Risk Management",
        "description": "Credit, market, operational, and emerging risk modeling with ML and scenario analysis.",
        "devin_body": r'''
## When to use

You are quantifying credit, market, operational, or emerging risks; building early-warning systems; or stress-testing portfolios and operations.

## Key concepts

- **Risk modeling**: probability of default, loss distribution, and value-at-risk estimation.
- **Anomaly and tail-risk detection**: spot rare events and emerging vulnerabilities.
- **Scenario and stress testing**: evaluate sensitivity to shocks and regime changes.
- **Model risk management**: validate, monitor, and govern AI risk models.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingClassifier

# Credit-risk probability of default from borrower features
X = df[["income", "debt_to_income", "credit_history", "collateral"]]
y = df["defaulted"]
model = GradientBoostingClassifier(n_estimators=300, random_state=42).fit(X, y)
```

## Tuning notes

- Calibrate predicted probabilities so they reflect true likelihoods.
- Use time-based splits and out-of-time validation to avoid leakage.
- Separate model development from model-risk governance roles.
- Monitor for distribution shift and adversarial behavior in production.

## Verification

1. Build a default model and report AUC-ROC and calibration curves.
2. Run a stress scenario and quantify tail losses vs a baseline.
3. Deploy a drift monitor and simulate a regime shift.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2502.06656",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12032382/",
            "https://www.msci.com/downloads/web/msci-com/research-and-insights/paper/ai-portfolio-insights-and-the-future-of-risk-management/AI-Portfolio-Insights-and-the-Future-of-Risk-Management.pdf",
            "https://arxiv.org/abs/2310.17721",
        ],
    },
    {
        "name": "ai-for-compliance",
        "title": "AI for Compliance",
        "description": "Regulatory mapping, policy gap analysis, automated control testing, and AI-assisted compliance monitoring.",
        "devin_body": r'''
## When to use

You need to map regulations to controls, identify policy gaps, test compliance automatically, or answer regulatory questions at scale.

## Key concepts

- **Regulatory intelligence**: parse and compare rules across jurisdictions.
- **Policy gap analysis**: align internal policies against external requirements.
- **Control testing automation**: sample and test controls with ML.
- **Model-card and AI governance**: document and evaluate AI systems for regulatory fit.

## Code pattern

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Classify regulatory text excerpts by requirement category
vec = TfidfVectorizer(ngram_range=(1, 2))
X = vec.fit_transform(regulatory_texts)
clf = MultinomialNB().fit(X, requirement_labels)
```

## Tuning notes

- Cite exact regulatory provisions for every automated finding.
- Keep humans in the loop for interpretation and enforcement decisions.
- Track regulatory changes and re-evaluate compliance continuously.
- Build audit trails that explain how conclusions were reached.

## Verification

1. Map a regulation to internal policies and report coverage gaps.
2. Classify regulatory requirements and measure accuracy vs legal review.
3. Automate a control test and compare results to manual sampling.
''',
        "references": [
            "https://doi.org/10.1007/s44163-026-01196-1",
            "https://doi.org/10.48550/arxiv.2601.04474",
            "https://link.springer.com/article/10.1007/s43681-025-00708-6",
            "https://arxiv.org/abs/2406.14758v2",
        ],
    },
    {
        "name": "ai-for-legal-operations",
        "title": "AI for Legal Operations",
        "description": "Contract review, clause extraction, matter intake, and AI-assisted legal workflow automation.",
        "devin_body": r'''
## When to use

You are automating contract review, triaging legal requests, extracting clauses, or streamlining matter management and e-billing.

## Key concepts

- **Contract review and clause extraction**: identify risks, obligations, and deviations.
- **Legal intake and routing**: classify matters and route to the right team.
- **E-billing and spend analytics**: detect anomalies and benchmark legal spend.
- **RAG and source grounding**: ground legal answers in contracts, policies, and precedent.

## Code pattern

```python
from transformers import pipeline

# Extract named entities and clauses from contracts
ner = pipeline("token-classification", model="dslim/bert-base-NER", aggregation_strategy="simple")
entities = ner(contract_text)
```

## Tuning notes

- Use retrieval-augmented generation with approved playbooks and clauses.
- Never let AI produce final legal advice; require attorney review.
- Preserve privilege and client confidentiality in all pipelines.
- Audit for hallucinated citations and subtle clause misinterpretations.

## Verification

1. Extract clauses from a contract set and compare to manual annotations.
2. Build a matter-intake classifier and measure routing accuracy.
3. Test a contract-review pipeline against a discrepancy benchmark.
''',
        "references": [
            "https://aclanthology.org/2026.findings-eacl.305/",
            "https://arxiv.org/abs/2508.03080",
            "https://arxiv.org/abs/2401.16212",
            "https://www.cambridge.org/core/journals/international-journal-of-legal-information/article/evaluating-ai-in-legal-operations-a-comparative-analysis-of-accuracy-completeness-and-hallucinations-in-chatgpt4-copilot-deepseek-lexis-ai-and-llama-3/64E4DA3715DFCAA99DF3A1AC4680CAC8",
        ],
    },
    {
        "name": "ai-for-insurance",
        "title": "AI for Insurance",
        "description": "Underwriting triage, claims automation, fraud detection, and AI-assisted pricing and reserving.",
        "devin_body": r'''
## When to use

You are building predictive models for underwriting, claims, fraud, pricing, or customer churn in insurance operations.

## Key concepts

- **Underwriting risk scoring**: predict loss cost and quote appropriate premiums.
- **Claims automation**: triage, document understanding, and fast-track routing.
- **Fraud and leakage detection**: identify suspicious patterns and provider behavior.
- **Pricing and reserving**: combine ML with actuarial methods for ratemaking.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Claims fraud detection from claim features and history
X = df[["claim_amount", "time_since_policy", "prior_claims", "provider_flags"]]
y = df["fraud"]
clf = RandomForestClassifier(class_weight="balanced_subsample", random_state=42).fit(X, y)
```

## Tuning notes

- Respect anti-discrimination and fair-lending regulations in features.
- Calibrate probability estimates for pricing and reserve decisions.
- Use temporal validation because claim patterns change over time.
- Explain model decisions to underwriters, adjusters, and regulators.

## Verification

1. Build a fraud model and report precision-recall at the top decile.
2. Predict claim severity and compare to actuarial baseline.
3. Test an underwriting triage workflow and measure straight-through processing.
''',
        "references": [
            "https://arxiv.org/abs/2605.18784v2",
            "https://arxiv.org/abs/2606.05449v1",
            "https://doi.org/10.48550/arxiv.2506.18942",
            "https://arxiv.org/abs/2306.01149",
        ],
    },
    {
        "name": "ai-for-real-estate",
        "title": "AI for Real Estate",
        "description": "Automated valuation, market analysis, lead matching, and AI-assisted property due diligence.",
        "devin_body": r'''
## When to use

You are valuing properties, analyzing market trends, matching buyers to listings, or screening properties for investment or lending.

## Key concepts

- **Automated valuation models (AVMs)**: predict price from property and market features.
- **Hedonic and multi-modal models**: combine structured, text, and image data.
- **Market and submarket analysis**: forecast rent, vacancy, and cap rates.
- **Lead matching and due diligence**: score opportunities and surface risks.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingRegressor

# Property valuation from structured features
X = df[["sqft", "bedrooms", "age", "location_score", "school_score"]]
y = df["price"]
model = GradientBoostingRegressor(n_estimators=300, random_state=42).fit(X, y)
```

## Tuning notes

- Geographically validate models; markets can differ sharply by subregion.
- Avoid data leakage from future sale prices and macro conditions.
- Incorporate image, text, and location embeddings where available.
- Explain valuations to clients, appraisers, and underwriters.

## Verification

1. Build an AVM and evaluate MAPE on a heldout geography and time window.
2. Forecast rent or cap-rate trends and compare to market benchmarks.
3. Score property leads and measure conversion lift over a rule-based baseline.
''',
        "references": [
            "https://arxiv.org/abs/2603.12986v1",
            "https://doi.org/10.48550/arxiv.2503.12344",
            "https://arxiv.org/pdf/2107.05180",
            "https://arxiv.org/abs/2506.11812",
        ],
    },
]
