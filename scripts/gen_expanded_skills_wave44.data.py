SKILLS = [
    {
        "name": "ai-for-data-governance",
        "title": "AI for Data Governance",
        "description": "Build policy, catalog, and lineage-driven governance for trusted data and AI assets.",
        "devin_body": r'''## When to use

You need to define, enforce, and monitor policies, ownership, and lifecycle rules for data assets across an organization.

## Usage

- Map business terms and data assets in Collibra or Informatica.
- Automate data classification and sensitivity tagging.
- Define and enforce data and AI policies across clouds.
- Track lineage from source to AI model in an active catalog.
- Score data and AI system trust with governance dashboards.

## Steps

1. Inventory data, models, and policies across the estate.
2. Build a business glossary and assign data owners.
3. Automate classification, lineage, and policy workflows.
4. Integrate with data quality, privacy, and model-risk tools.
5. Monitor compliance and update policies as assets evolve.

## Code pattern

```python
import json

# Encode a governance policy as structured metadata
policy = {
    "table": "customers",
    "tags": ["pii", "gdpr"],
    "retention_days": 2555,
    "owner": "data-governance@example.com",
}
print(json.dumps(policy, indent=2))
```

## Tuning notes

- Align governance with business domains and clear data ownership.
- Balance strict policies with self-service access.
- Use lineage to trace the impact of policy and schema changes.

## Verification

1. Show a policy rule blocks unauthorized access or mis-tagging.
2. Generate a data lineage graph from source to dashboard.
3. Audit a sample of cataloged assets for metadata completeness.

''',
        "references": ["https://doi.org/10.1109/access.2024.3476373", "https://doi.org/10.3390/bdcc10010008", "https://doi.org/10.38035/rrj.v8i4.2110", "https://doi.org/10.3390/data10120201"],
    },
    {
        "name": "ai-for-data-quality",
        "title": "AI for Data Quality",
        "description": "Detect and repair data quality issues across pipelines, warehouses, and AI inputs.",
        "devin_body": r'''## When to use

You need to detect, measure, and improve the accuracy, completeness, consistency, and timeliness of datasets used for analytics or ML.

## Usage

- Profile tables and auto-generate data quality rules (Great Expectations, Soda).
- Detect null spikes, distribution drift, and schema changes.
- Build expectation suites and data contracts in CI.
- Prioritize remediation with impact/lineage scoring.
- Track data health SLAs and coverage.

## Steps

1. Profile source and warehouse tables.
2. Define business rules and data contracts.
3. Train or configure anomaly detection on historical patterns.
4. Alert, quarantine, and repair bad records.
5. Report data health and retrain baselines.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import IsolationForest

X = df.select_dtypes(include="number").fillna(0)
clf = IsolationForest(contamination=0.05, random_state=42)
df["anomaly_score"] = clf.decision_function(X)
```

## Tuning notes

- Tune contamination based on empirical false-positive rates.
- Distinguish between data bugs and legitimate distribution shift.
- Validate cleaning steps with business stakeholders.

## Verification

1. Compute quality scores before and after cleaning on a known-dirty dataset.
2. Detect and report the top anomalous records and their features.
3. Compare a model trained on cleaned data to one trained on raw data.

''',
        "references": ["https://doi.org/10.1145/3592616", "https://doi.org/10.1016/j.infsof.2023.107268", "https://doi.org/10.1145/3722214", "https://doi.org/10.1109/aitest62860.2024.00023"],
    },
    {
        "name": "ai-for-data-observability",
        "title": "AI for Data Observability",
        "description": "Monitor data freshness, volume, and lineage to detect pipeline failures.",
        "devin_body": r'''## When to use

You need end-to-end visibility into data pipelines and want to detect, diagnose, and remediate data incidents automatically.

## Usage

- Auto-generate freshness, volume, and schema monitors (Monte Carlo, dataobservability.ai).
- Detect anomalies in row counts and distribution (Soda, Prizm).
- Map column-level lineage and downstream impact.
- Correlate data incidents with cost and performance metrics.
- Build runbooks and root-cause analysis with AIOps.

## Steps

1. Connect warehouses, lakes, and pipeline orchestrators.
2. Baseline historical metrics for freshness, volume, and schema.
3. Deploy ML-based or rule-based anomaly detection.
4. Alert teams and route incidents by lineage.
5. Track MTTR and refine thresholds.

## Code pattern

```python
from scipy import stats

# Schema-free distribution check on a numeric column
latest = df["revenue"].dropna()
expected_mean = historical_mean
z_stat = (latest.mean() - expected_mean) / (latest.std() / len(latest) ** 0.5)
```

For production, integrate with tools such as Great Expectations, Soda, or Monte Carlo.

## Tuning notes

- Establish baseline windows that account for seasonality and known changes.
- Avoid alert fatigue by grouping correlated anomalies.
- Preserve lineage to reduce mean time to detection.

## Verification

1. Inject a schema change and show the observability alert fires.
2. Detect a row-count drop in a pipeline and localize the failed task.
3. Compare anomaly detection precision to threshold-only monitoring.

''',
        "references": ["https://www.vldb.org/pvldb/vol15/p4015-shankar.pdf", "https://doi.org/10.60087/jaigs.v6i1.412", "https://doi.org/10.5281/zenodo.20801568", "https://doi.org/10.5281/zenodo.19487347"],
    },
    {
        "name": "ai-for-data-curation",
        "title": "AI for Data Curation",
        "description": "Label, augment, and document training data for reliable machine learning.",
        "devin_body": r'''## When to use

You are building or maintaining reusable datasets and need to select, clean, label, augment, and document them systematically.

## Usage

- Run weak supervision and programmatic labeling (Snorkel, Alfred).
- Synthesize training examples with GANs or LLM augmenters.
- Create data cards and datasheets for datasets.
- Validate label quality with consensus and error analysis.
- Version datasets with DVC or Pachyderm.

## Steps

1. Define labeling schemas and data-card templates.
2. Collect raw data and apply rules, model, or LLM heuristics.
3. Aggregate and denoise labels with weak supervision.
4. Generate data sheets and quality reports.
5. Version and distribute curated datasets.

## Code pattern

```python
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

# Identify likely duplicates or outliers in a tabular dataset
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.01)
df["outlier"] = lof.fit_predict(df.select_dtypes(include="number").fillna(0))
```

## Tuning notes

- Document every curation decision for reproducibility.
- Balance augmentation with preservation of true distributions.
- Use active learning to focus labeling budget on uncertain examples.

## Verification

1. Compare model performance before and after curation on a holdout set.
2. Generate a data card and verify required metadata fields.
3. Measure label quality (inter-annotator agreement or consistency).

''',
        "references": ["https://doi.org/10.1145/3711118", "https://doi.org/10.1016/j.dsm.2023.06.001", "https://doi.org/10.1145/3630106.3658955", "https://doi.org/10.48550/arxiv.2112.06409"],
    },
    {
        "name": "ai-for-data-discovery",
        "title": "AI for Data Discovery",
        "description": "Help users find, understand, and trust the right data and AI assets.",
        "devin_body": r'''## When to use

Users cannot find the right data in a lake, catalog, or open repository, and keyword search is insufficient.

## Usage

- Search catalogs with natural language (Alation, Atlan, DataHub).
- Auto-generate descriptions, tags, and glossary links.
- Recommend similar or related datasets.
- Show data quality, popularity, and owner context.
- Embed search into BI and notebooks for self-service.

## Steps

1. Crawl data sources and extract metadata.
2. Build knowledge graph of datasets, terms, and users.
3. Train ranking and recommendation models.
4. Expose natural-language search and recommendations.
5. Track adoption and improve relevance.

## Code pattern

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")
query_emb = model.encode("monthly sales by region")
dataset_embs = model.encode(dataset_descriptions)
scores = cosine_similarity([query_emb], dataset_embs)[0]
```

## Tuning notes

- Combine lexical and semantic search for recall and precision.
- Keep provenance and access controls with every discovered asset.
- Update indexes as new datasets and schemas are added.

## Verification

1. Search for a dataset and verify the top result matches intent.
2. Discover joinable columns across two datasets.
3. Compare a semantic search to a keyword baseline on real queries.

''',
        "references": ["https://doi.org/10.1145/3626521", "https://doi.org/10.1007/s00778-019-00564-x", "https://doi.org/10.48550/arxiv.2509.00728", "https://doi.org/10.1002/pra2.1242"],
    },
    {
        "name": "ai-for-data-marketplaces",
        "title": "AI for Data Marketplaces",
        "description": "Match buyers and sellers, price data products, and manage data exchange.",
        "devin_body": r'''## When to use

You are designing, operating, or participating in a marketplace that trades data, datasets, or AI models and need discovery, pricing, or trust mechanisms.

## Usage

- Build searchable data-product catalogs with quality scores.
- Estimate data value with Shapley, SHAP, or auction models.
- Set usage-based, subscription, or outcome pricing.
- Automate contracts, licensing, and access controls.
- Track product performance and seller reputation.

## Steps

1. Curate and profile data products for the marketplace.
2. Train data valuation and price-prediction models.
3. Build pricing, negotiation, and contract workflows.
4. Enforce access, privacy, and audit terms.
5. Monitor transactions and refine pricing.

## Code pattern

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Simple hedonic pricing from metadata features
X = metadata[["n_rows", "n_features", "freshness_days", "domain_score"]]
y = prices
model = LinearRegression().fit(X, y)
estimates = model.predict(X)
```

## Tuning notes

- Balance privacy and utility when exposing samples or statistics.
- Prevent arbitrage and collusion in pricing and reward schemes.
- Build reputation systems that resist manipulation and sybil attacks.

## Verification

1. Recommend the top-k datasets for a buyer persona and evaluate relevance.
2. Estimate Shapley-based data valuation and compare to baseline pricing.
3. Simulate a transaction and verify license enforcement.

''',
        "references": ["https://www.vldb.org/pvldb/vol16/p3872-pei.pdf", "https://doi.org/10.3390/jtaer16070180", "https://doi.org/10.48550/arxiv.2411.07267", "https://doi.org/10.3390/fi17010035"],
    },
    {
        "name": "ai-for-data-provenance",
        "title": "AI for Data Provenance",
        "description": "Track the origin, transformation, and flow of data and AI artifacts.",
        "devin_body": r'''## When to use

You need to trace data origins, transformations, and decisions to ensure reproducibility, compliance, and explainability.

## Usage

- Capture lineage with W3C PROV, MLflow, or yProv4ML.
- Trace model training data, code, and parameters.
- Version data, code, and models with DVC and Git.
- Query provenance graphs in graph databases.
- Reproduce experiments and audit AI systems.

## Steps

1. Instrument pipelines to log activities and artifacts.
2. Map entities, activities, and agents to a provenance graph.
3. Store provenance in PROV-JSON, RDF, or graph DB.
4. Build queries and visualizations for lineage.
5. Audit and verify reproducibility.

## Code pattern

```python
import mlflow

mlflow.start_run()
mlflow.log_param("source", "raw_customers.csv")
mlflow.log_artifact("preprocess.py")
mlflow.log_metric("f1_score", 0.92)
mlflow.end_run()
```

## Tuning notes

- Capture fine-grained provenance without overwhelming storage.
- Link provenance to business terms and governance policies.
- Ensure provenance records are tamper-evident where needed.

## Verification

1. Reproduce an output from a tracked pipeline using stored artifacts.
2. Query lineage from a dashboard metric back to source tables.
3. Show provenance supports an audit or explainability request.

''',
        "references": ["https://doi.org/10.1162/dint_a_00119", "https://doi.org/10.3390/bdcc5020020", "https://doi.org/10.5220/0014732400004015", "https://doi.org/10.1145/3788853.3801877"],
    },
    {
        "name": "ai-for-data-privacy",
        "title": "AI for Data Privacy",
        "description": "Protect sensitive data using differential privacy, anonymization, and federated learning.",
        "devin_body": r'''## When to use

You train or serve ML models on personal, sensitive, or regulated data and need to protect privacy across the lifecycle.

## Usage

- Train models with differential privacy (Opacus, TensorFlow Privacy).
- Apply k-anonymity, l-diversity, and synthetic data generation.
- Run federated learning across institutions (NVIDIA FLARE, Flower).
- Audit re-identification risk and privacy budgets.
- De-identify free text with named-entity recognition.

## Steps

1. Classify sensitive attributes and privacy requirements.
2. Choose privacy mechanism (DP, federated, anonymization).
3. Implement training, aggregation, or synthesis.
4. Evaluate privacy-utility trade-off and budget.
5. Document privacy guarantees and audits.

## Code pattern

```python
import tensorflow_privacy as tfp
from tensorflow.keras import optimizers

# DP-SGD optimizer wrapper
optimizer = tfp.DPKerasSGDOptimizer(
    l2_norm_clip=1.0,
    noise_multiplier=0.5,
    num_microbatches=1,
    learning_rate=0.1,
)
```

## Tuning notes

- Trade off privacy budget against model utility on validation data.
- Account for composition across many queries or training steps.
- Validate that federated aggregation preserves privacy guarantees.

## Verification

1. Train a model with DP-SGD and report (epsilon, delta) privacy budget.
2. Run a membership inference attack and compare with and without DP.
3. Audit a synthetic or anonymized dataset for re-identification risk.

''',
        "references": ["https://doi.org/10.1145/3440754", "https://doi.org/10.1145/3624010", "https://doi.org/10.1016/j.cose.2023.103605", "https://doi.org/10.3390/app16010277"],
    },
    {
        "name": "ai-for-data-security",
        "title": "AI for Data Security",
        "description": "Defend AI systems against adversarial attacks, data poisoning, and model extraction.",
        "devin_body": r'''## When to use

You need to protect data and models from adversarial manipulation, unauthorized access, and data-centric attacks.

## Usage

- Evaluate adversarial robustness with ART (Adversarial Robustness Toolbox).
- Detect and remove poisoned samples (PoisonSpot, training provenance).
- Protect model APIs from extraction and inversion attacks.
- Scan for vulnerabilities in model artifacts and supply chain.
- Monitor production drift and anomalous queries.

## Steps

1. Threat-model the AI system and data pipeline.
2. Run adversarial and poisoning attacks in a sandbox.
3. Train or harden models with robust defenses.
4. Deploy monitoring and anomaly detection in production.
5. Red-team and update defenses regularly.

## Code pattern

```python
from sklearn.ensemble import IsolationForest

# Detect potentially poisoned training samples
X = features
clf = IsolationForest(contamination=0.02, random_state=42)
poison_labels = clf.fit_predict(X)
```

## Tuning notes

- Use a defense-in-depth strategy across storage, network, and application layers.
- Keep models and data access logs for forensic analysis.
- Validate sanitization does not remove important minority examples.

## Verification

1. Detect backdoor or poisoning samples in a contaminated dataset.
2. Run an adversarial example attack and evaluate defense effectiveness.
3. Audit access logs for anomalous data exfiltration patterns.

''',
        "references": ["https://doi.org/10.48550/arxiv.2310.04513", "https://link.springer.com/article/10.1186/s13635-024-00158-3", "https://doi.org/10.1007/s11432-025-4388-5", "https://doi.org/10.1145/3670007"],
    },
    {
        "name": "ai-for-data-ethics",
        "title": "AI for Data Ethics",
        "description": "Assess and mitigate fairness, bias, and societal impacts of data and AI.",
        "devin_body": r'''## When to use

You need to identify and mitigate ethical risks in data collection, processing, and model deployment, including bias, consent, and transparency.

## Usage

- Audit model fairness with Fairlearn and Aequitas.
- Measure group and intersectional disparities.
- Test for biases in data collection and labeling.
- Review model cards and explainability reports.
- Engage stakeholders and document mitigation.

## Steps

1. Define protected attributes and fairness metrics.
2. Audit data, features, and model outputs for disparities.
3. Train bias-mitigation models or apply post-processing.
4. Generate model cards and fairness reports.
5. Iterate with stakeholders and re-audit.

## Code pattern

```python
from fairlearn.metrics import demographic_parity_difference

# Assess demographic parity on a classification outcome
y_pred = model.predict(X_test)
dp = demographic_parity_difference(
    y_test, y_pred, sensitive_features=A_test
)
print("Demographic parity difference:", dp)
```

## Tuning notes

- Choose fairness metrics aligned to the specific harm and legal context.
- Involve domain experts and affected communities.
- Balance fairness with other business and accuracy objectives transparently.

## Verification

1. Compute fairness metrics before and after mitigation on a real dataset.
2. Generate a model card and verify it covers intended use and limitations.
3. Conduct a stakeholder review of consent and redress workflows.

''',
        "references": ["https://doi.org/10.3390/informatics13040051", "https://doi.org/10.1007/s41060-024-00541-w", "https://doi.org/10.1007/s00778-021-00671-8", "https://doi.org/10.30574/msarr.2023.7.2.0043"],
    },
    {
        "name": "ai-for-data-sharing",
        "title": "AI for Data Sharing",
        "description": "Enable privacy-preserving collaboration and data exchange across organizations.",
        "devin_body": r'''## When to use

Organizations need to share data across silos, partners, or jurisdictions while preserving privacy and trust.

## Usage

- Train federated models with Flower or NVIDIA FLARE.
- Share synthetic data generated from real datasets.
- Establish data trusts and consortium contracts.
- Exchange data via APIs with differential privacy.
- Track usage and compliance with smart contracts.

## Steps

1. Identify data partners, use case, and governance.
2. Set up a federated or synthetic-data platform.
3. Align schemas, privacy budgets, and access rules.
4. Train or generate shared data products.
5. Audit contributions and outputs.

## Code pattern

```python
import tensorflow_federated as tff

# Federated averaging on a simple Keras model
iterative_process = tff.learning.algorithms.build_weighted_fed_avg(model_fn)
state = iterative_process.initialize()
```

## Tuning notes

- Align incentives with long-term data quality and participation.
- Use secure aggregation and differential privacy for strong guarantees.
- Document data-use agreements and withdrawal rights.

## Verification

1. Train a model with federated learning and compare to a centralized baseline.
2. Simulate free-riding or low-quality participants and test reputation scoring.
3. Audit that no raw data leaves participant boundaries.

''',
        "references": ["https://doi.org/10.1007/s44248-024-00006-2", "https://doi.org/10.3390/data10110182", "https://doi.org/10.1007/s10115-022-01664-x", "https://doi.org/10.48550/arxiv.2307.10655"],
    },
    {
        "name": "ai-for-data-monetization",
        "title": "AI for Data Monetization",
        "description": "Value, price, and package data assets for market exchange and revenue.",
        "devin_body": r'''## When to use

You want to turn raw data, derived features, models, or insights into revenue or measurable economic value.

## Usage

- Estimate data Shapley value for contribution-based pricing.
- Build price-prediction models (DataPrice, SHAP explanations).
- Bundle data products for target buyers and use cases.
- Set dynamic pricing based on freshness and exclusivity.
- Track revenue, usage, and customer value.

## Steps

1. Catalog data assets and assess quality, uniqueness, and demand.
2. Train data valuation and price-prediction models.
3. Design pricing and packaging strategies.
4. Launch marketplace listings with access controls.
5. Measure revenue and iterate.

## Code pattern

```python
import numpy as np
from sklearn.linear_model import Ridge

# Hedonic pricing with metadata and quality features
X = catalog[["n_rows", "n_features", "quality_score", "freshness_days"]]
y = catalog["price"]
model = Ridge(alpha=1.0).fit(X, y)
```

## Tuning notes

- Separate the value of data from the value of the derived model or insight.
- Avoid privacy leakage through pricing metadata or samples.
- Use game-theoretic fairness in revenue allocation.

## Verification

1. Estimate Shapley values for a dataset and compare to leave-one-out retraining.
2. Simulate pricing under different demand and supply scenarios.
3. Allocate revenue to multiple contributors and verify fairness axioms.

''',
        "references": ["https://doi.org/10.1007/s11301-022-00309-1", "https://doi.org/10.1109/tbdata.2023.3254152", "https://doi.org/10.24963/ijcai.2022/782", "https://doi.org/10.48550/arxiv.2108.07915"],
    },
]