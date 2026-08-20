SKILLS = [
    {
        "name": "ai-for-data-governance",
        "title": "AI for Data Governance",
        "description": "Automated policy enforcement, metadata management, data lineage, stewardship, and AI-driven regulatory compliance for enterprise data governance.",
        "devin_body": r'''## When to use

You need to define, enforce, and monitor policies, ownership, and lifecycle rules for data assets across an organization.

## Usage

- **Policy automation**: classify, tag, and enforce retention, access, and quality policies at scale.
- **Metadata and cataloging**: auto-extract business, technical, and operational metadata.
- **Lineage and stewardship**: map data ownership and provenance to support accountability.
- **Compliance and risk**: align with GDPR, CCPA, AI Act, and sector regulations.
- **Glossary and standards**: maintain consistent definitions, taxonomies, and master data.

## Steps

1. Inventory data assets, owners, and critical systems.
2. Define governance policies, data domains, and quality rules.
3. Implement automated policy checks and metadata capture.
4. Build a searchable data catalog with lineage views.
5. Monitor compliance and audit policy exceptions.

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
        "references": [
            "https://doi.org/10.1109/access.2024.3476373",
            "https://doi.org/10.3390/bdcc10010008",
            "https://doi.org/10.38035/rrj.v8i4.2110",
            "https://doi.org/10.3390/data10120201",
        ],
    },
    {
        "name": "ai-for-data-quality",
        "title": "AI for Data Quality",
        "description": "Automated profiling, anomaly detection, data cleaning, imputation, validation, and continuous data quality monitoring for ML and analytics.",
        "devin_body": r'''## When to use

You need to detect, measure, and improve the accuracy, completeness, consistency, and timeliness of datasets used for analytics or ML.

## Usage

- **Profiling and scoring**: compute quality dimensions across schema, values, and distributions.
- **Anomaly detection**: use statistical or ML models to flag outliers and drift.
- **Data cleaning**: auto-correct, impute, or standardize values.
- **Validation rules**: encode constraints and monitor rule violations.
- **Drift monitoring**: track data distribution and schema changes over time.

## Steps

1. Profile the dataset and define quality dimensions and thresholds.
2. Build or integrate an anomaly detector and validation rule engine.
3. Clean and impute data while preserving lineage.
4. Monitor quality metrics in dashboards and alerts.
5. Retrain models when quality issues or drift are detected.

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
        "references": [
            "https://doi.org/10.1145/3592616",
            "https://doi.org/10.1016/j.infsof.2023.107268",
            "https://doi.org/10.1145/3722214",
            "https://doi.org/10.1109/aitest62860.2024.00023",
        ],
    },
    {
        "name": "ai-for-data-observability",
        "title": "AI for Data Observability",
        "description": "ML-driven monitoring of data freshness, schema drift, volume anomalies, lineage breaks, and pipeline health to ensure reliable data operations.",
        "devin_body": r'''## When to use

You need end-to-end visibility into data pipelines and want to detect, diagnose, and remediate data incidents automatically.

## Usage

- **Freshness and volume monitoring**: detect late or missing data.
- **Schema and distribution drift**: identify unexpected changes in data shape or distributions.
- **Lineage-aware anomaly detection**: localize pipeline failures using dependency graphs.
- **Automated root cause analysis**: rank likely causes and suggest fixes.
- **SLO dashboards**: track data reliability, completeness, and freshness KPIs.

## Steps

1. Instrument pipelines with run, dataset, and model metadata.
2. Define observability signals: freshness, row count, schema, distributions.
3. Train anomaly detectors on historical pipeline behavior.
4. Correlate anomalies with lineage and code or infrastructure changes.
5. Alert and auto-remediate common failure modes.

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
        "references": [
            "https://www.vldb.org/pvldb/vol15/p4015-shankar.pdf",
            "https://doi.org/10.60087/jaigs.v6i1.412",
            "https://doi.org/10.5281/zenodo.20801568",
            "https://doi.org/10.5281/zenodo.19487347",
        ],
    },
    {
        "name": "ai-for-data-curation",
        "title": "AI for Data Curation",
        "description": "Automated selection, cleaning, labeling, augmentation, and documentation of datasets to produce high-quality, FAIR, and reusable ML data assets.",
        "devin_body": r'''## When to use

You are building or maintaining reusable datasets and need to select, clean, label, augment, and document them systematically.

## Usage

- **Dataset selection and deduplication**: identify representative, non-redundant samples.
- **Data cleaning and imputation**: detect and repair errors, missing values, and inconsistencies.
- **Active and programmatic labeling**: prioritize and scale data annotation.
- **Data augmentation and balancing**: synthesize or reweight samples for better coverage.
- **Documentation and metadata**: produce datasheets, data cards, and provenance records.

## Steps

1. Define the target population and collection criteria.
2. Profile the raw data and identify quality and coverage gaps.
3. Clean, deduplicate, and (re)label the dataset.
4. Augment or resample to improve representation and balance.
5. Publish with metadata, data cards, and usage licenses.

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
        "references": [
            "https://doi.org/10.1145/3711118",
            "https://doi.org/10.1016/j.dsm.2023.06.001",
            "https://doi.org/10.1145/3630106.3658955",
            "https://doi.org/10.48550/arxiv.2112.06409",
        ],
    },
    {
        "name": "ai-for-data-discovery",
        "title": "AI for Data Discovery",
        "description": "Intelligent dataset search, metadata enrichment, schema inference, and conversational data catalog exploration to find the right data quickly.",
        "devin_body": r'''## When to use

Users cannot find the right data in a lake, catalog, or open repository, and keyword search is insufficient.

## Usage

- **Dataset search and recommendation**: match needs by metadata, content, or examples.
- **Schema and semantic inference**: auto-extract columns, types, and relationships.
- **Data profiling and summarization**: surface distributions, coverage, and quality.
- **Conversational exploration**: use LLMs to answer natural-language data requests.
- **Similarity and join discovery**: identify related datasets and linkable keys.

## Steps

1. Collect and index datasets with metadata, schema, and samples.
2. Build embeddings and similarity indexes over metadata and content.
3. Deploy search and recommendation APIs or chat interfaces.
4. Let users explore lineage, quality, and usage statistics.
5. Refine ranking from user feedback and query logs.

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
        "references": [
            "https://doi.org/10.1145/3626521",
            "https://doi.org/10.1007/s00778-019-00564-x",
            "https://doi.org/10.48550/arxiv.2509.00728",
            "https://doi.org/10.1002/pra2.1242",
        ],
    },
    {
        "name": "ai-for-data-marketplaces",
        "title": "AI for Data Marketplaces",
        "description": "AI for data and model discovery, pricing, valuation, matching, trust, and governance in data-sharing marketplaces and AI model markets.",
        "devin_body": r'''## When to use

You are designing, operating, or participating in a marketplace that trades data, datasets, or AI models and need discovery, pricing, or trust mechanisms.

## Usage

- **Asset discovery and recommendation**: match buyers to relevant datasets or models.
- **Data and model valuation**: estimate worth using Shapley, information, or auction methods.
- **Pricing and bundling**: set prices that are arbitrage-free and incentive-aligned.
- **Trust and reputation**: score sellers, buyers, and data quality.
- **License and access control**: enforce usage terms and track consumption.

## Steps

1. Define marketplace assets, participants, and business rules.
2. Build search, profiling, and recommendation systems for assets.
3. Implement valuation and pricing models.
4. Add trust, rating, and dispute mechanisms.
5. Monitor transactions, enforce licenses, and adjust pricing.

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
        "references": [
            "https://www.vldb.org/pvldb/vol16/p3872-pei.pdf",
            "https://doi.org/10.3390/jtaer16070180",
            "https://doi.org/10.48550/arxiv.2411.07267",
            "https://doi.org/10.3390/fi17010035",
        ],
    },
    {
        "name": "ai-for-data-provenance",
        "title": "AI for Data Provenance",
        "description": "Lineage tracking, W3C PROV, reproducible ML pipelines, experiment tracking, and provenance for explainable and trustworthy AI.",
        "devin_body": r'''## When to use

You need to trace data origins, transformations, and decisions to ensure reproducibility, compliance, and explainability.

## Usage

- **Lineage and traceability**: record transformations from source to model.
- **W3C PROV and standards**: represent provenance with interoperable models.
- **ML experiment tracking**: version datasets, code, models, and metrics.
- **Reproducibility and audit**: replay pipelines and verify outputs.
- **Explainable AI**: link model predictions to training data and features.

## Steps

1. Identify sources, transformations, and outputs in the data pipeline.
2. Capture provenance metadata at each step using PROV or lineage APIs.
3. Version data, code, and model artifacts.
4. Index provenance for query, replay, and impact analysis.
5. Audit provenance for compliance and debugging.

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
        "references": [
            "https://doi.org/10.1162/dint_a_00119",
            "https://doi.org/10.3390/bdcc5020020",
            "https://doi.org/10.5220/0014732400004015",
            "https://doi.org/10.1145/3788853.3801877",
        ],
    },
    {
        "name": "ai-for-data-privacy",
        "title": "AI for Data Privacy",
        "description": "Differential privacy, federated learning, homomorphic encryption, PETs, and privacy-preserving ML for sensitive data.",
        "devin_body": r'''## When to use

You train or serve ML models on personal, sensitive, or regulated data and need to protect privacy across the lifecycle.

## Usage

- **Differential privacy**: add calibrated noise to queries, gradients, or outputs.
- **Federated and split learning**: keep raw data at the edge while training shared models.
- **Homomorphic encryption and secure multiparty computation**: compute on encrypted data.
- **Anonymization and pseudonymization**: de-identify datasets and evaluate re-identification risk.
- **Privacy auditing**: run membership inference and model inversion tests.

## Steps

1. Classify data sensitivity and identify privacy requirements.
2. Choose PETs (DP, FL, SMPC, HE) appropriate to the threat model.
3. Implement privacy mechanisms and tune privacy budgets or noise.
4. Audit models with attack simulations and privacy metrics.
5. Document privacy controls and compliance evidence.

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
        "references": [
            "https://doi.org/10.1145/3440754",
            "https://doi.org/10.1145/3624010",
            "https://doi.org/10.1016/j.cose.2023.103605",
            "https://doi.org/10.3390/app16010277",
        ],
    },
    {
        "name": "ai-for-data-security",
        "title": "AI for Data Security",
        "description": "Adversarial robustness, data poisoning detection, access control, threat detection, and AI-driven security for ML training and inference data.",
        "devin_body": r'''## When to use

You need to protect data and models from adversarial manipulation, unauthorized access, and data-centric attacks.

## Usage

- **Adversarial and poisoning defenses**: detect or mitigate malicious data and perturbations.
- **Access control and zero trust**: enforce least-privilege access to data and model artifacts.
- **Anomaly and intrusion detection**: identify exfiltration, unauthorized queries, or breaches.
- **Data sanitization and provenance**: verify data sources and remove poisoned samples.
- **Secure pipelines**: encrypt data at rest and in transit, harden CI/CD.

## Steps

1. Inventory data and model assets and threat surfaces.
2. Apply encryption, access control, and network segmentation.
3. Monitor for anomalies in data access, ingestion, and model usage.
4. Test robustness with adversarial and poisoning simulations.
5. Respond to incidents and update defenses and data provenance.

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
        "references": [
            "https://doi.org/10.48550/arxiv.2310.04513",
            "https://link.springer.com/article/10.1186/s13635-024-00158-3",
            "https://doi.org/10.1007/s11432-025-4388-5",
            "https://doi.org/10.1145/3670007",
        ],
    },
    {
        "name": "ai-for-data-ethics",
        "title": "AI for Data Ethics",
        "description": "Fairness, accountability, transparency, data dignity, consent, and responsible data use in ML pipelines and AI systems.",
        "devin_body": r'''## When to use

You need to identify and mitigate ethical risks in data collection, processing, and model deployment, including bias, consent, and transparency.

## Usage

- **Bias and fairness**: measure demographic parity, equalized odds, and calibration.
- **Transparency and explainability**: produce interpretable models and data cards.
- **Consent and data dignity**: respect user preferences and withdrawal rights.
- **Accountability**: assign responsibilities and audit decisions.
- **Environmental and societal impact**: assess energy, labor, and downstream harms.

## Steps

1. Identify stakeholders, harms, and ethical principles for the use case.
2. Audit data and models for bias, representativeness, and consent.
3. Implement fairness constraints, explainability, and redress mechanisms.
4. Document decisions, data cards, and model cards.
5. Monitor deployed systems for emerging ethical risks.

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
        "references": [
            "https://doi.org/10.3390/informatics13040051",
            "https://doi.org/10.1007/s41060-024-00541-w",
            "https://doi.org/10.1007/s00778-021-00671-8",
            "https://doi.org/10.30574/msarr.2023.7.2.0043",
        ],
    },
    {
        "name": "ai-for-data-sharing",
        "title": "AI for Data Sharing",
        "description": "Federated learning, data sharing incentives, interoperability, trust, and privacy-preserving collaboration for shared data ecosystems.",
        "devin_body": r'''## When to use

Organizations need to share data across silos, partners, or jurisdictions while preserving privacy and trust.

## Usage

- **Federated and collaborative learning**: train models on distributed data without centralizing it.
- **Incentive and reward design**: fairly compensate data contributors.
- **Interoperability and standards**: use common schemas, ontologies, and APIs.
- **Trust and reputation**: score participants and data quality.
- **Privacy-preserving sharing**: apply DP, SMPC, or synthetic data releases.

## Steps

1. Define sharing objectives, participants, and data sensitivity.
2. Choose a collaboration architecture (federated, pool, or synthetic release).
3. Implement access, consent, and privacy controls.
4. Build trust, reputation, and contribution-scoring mechanisms.
5. Monitor usage, enforce agreements, and audit compliance.

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
        "references": [
            "https://doi.org/10.1007/s44248-024-00006-2",
            "https://doi.org/10.3390/data10110182",
            "https://doi.org/10.1007/s10115-022-01664-x",
            "https://doi.org/10.48550/arxiv.2307.10655",
        ],
    },
    {
        "name": "ai-for-data-monetization",
        "title": "AI for Data Monetization",
        "description": "Data valuation, pricing, data products, marketplaces, and revenue allocation for turning data assets into measurable business value.",
        "devin_body": r'''## When to use

You want to turn raw data, derived features, models, or insights into revenue or measurable economic value.

## Usage

- **Data valuation**: estimate worth with Shapley, information, or influence-based methods.
- **Pricing models**: arbitrage-free pricing, auctions, and subscription tiers.
- **Data products**: package datasets, features, embeddings, or APIs for sale.
- **Revenue allocation**: reward contributors based on marginal value.
- **Marketplace dynamics**: match buyers and sellers and optimize liquidity.

## Steps

1. Identify data products and potential buyers.
2. Profile and value data assets using ML-driven valuation.
3. Set pricing, bundling, and licensing terms.
4. Operate a marketplace or direct sales channel.
5. Track revenue, usage, and contribution-based payouts.

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
        "references": [
            "https://doi.org/10.1007/s11301-022-00309-1",
            "https://doi.org/10.1109/tbdata.2023.3254152",
            "https://doi.org/10.24963/ijcai.2022/782",
            "https://doi.org/10.48550/arxiv.2108.07915",
        ],
    },
]
