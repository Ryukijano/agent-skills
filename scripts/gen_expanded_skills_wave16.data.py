SKILLS = [
    {
        "name": "ai-for-climate-policy",
        "title": "AI for Climate Policy",
        "description": "Natural-language analysis of climate laws, NDCs, and policies; target extraction, alignment scoring, and climate-finance tracking.",
        "devin_body": r'''
## When to use

You need to analyze, compare, or monitor national climate laws, Nationally Determined Contributions (NDCs), or corporate climate disclosures at scale.

## Key concepts

- **NDC and VNR alignment**: compare Nationally Determined Contributions with Voluntary National Reviews using NLP and classifiers.
- **Target extraction**: identify quantified climate targets (net-zero, reduction, renewable) in long documents.
- **Climate policy NLP**: domain-adapted language models (ClimateBERT) for climate-finance and policy text.
- **Policy impact monitoring**: track implementation progress, theme shifts, and equity implications over time.

## Code pattern

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("climatebert/distilroberta-base-climate-s")
model = AutoModelForSequenceClassification.from_pretrained("climatebert/distilroberta-base-climate-s")

text = "We commit to reduce greenhouse gas emissions by 55% by 2030."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
probs = outputs.logits.softmax(dim=-1)
```

## Tuning notes

- Use domain-adapted models (ClimateBERT, climate-nlp) rather than generic BERT for policy/finance text.
- Climate documents are often long and multilingual; chunking and translation may be needed.
- Be transparent about data provenance, temporal validity, and jurisdictional scope.

## Verification

1. Fine-tune a classifier on a labeled climate-policy dataset and evaluate F1.
2. Extract quantified targets from a set of NDCs and compare to human annotations.
3. Run a cross-country alignment analysis between NDCs and SDG reporting.
''',
        "references": [
            "https://huggingface.co/climatebert",
            "https://huggingface.co/ClimatePolicyRadar/national-climate-targets",
            "https://www.climatepolicyradar.org/latest/using-machine-learning-to-classify-climate-targets",
            "https://www.nature.com/articles/s41467-024-53956-1",
            "https://unfccc.int/ttclear/misc_/StaticFiles/gnwoerk_static/tn_meetings/43ef8d5f37e6484ca634479e3b74a3a8/3ee3862a08c84afe971c29f2687a45f1.pdf",
        ],
    },
    {
        "name": "ai-for-energy-grid",
        "title": "AI for Energy Grid",
        "description": "Power-flow surrogates, renewable and load forecasting, grid stability, optimal power flow, and AI-assisted grid operations.",
        "devin_body": r'''
## When to use

You are building, operating, or studying power systems with high renewable penetration and need fast, scalable, and physically consistent predictions or optimizations.

## Key concepts

- **AC/DC power flow**: compute bus voltages, branch flows, and generator dispatch subject to physical and operational constraints.
- **Optimal Power Flow (OPF)**: cost-minimizing dispatch while satisfying voltage, thermal, and generator limits.
- **Renewable and load forecasting**: probabilistic time-series models for solar, wind, and demand.
- **Grid foundation models**: neural surrogates such as GridSFM and OpenGridFM that solve OPF in milliseconds.
- **Stability and contingency**: N-1 security, fault detection, and dynamic stability analysis.

## Code pattern

```python
import pandapower as pp
import pandapower.networks as pn

net = pn.case_ieee30()
pp.runpp(net)
print(net.res_bus.vm_pu.min(), net.res_bus.vm_pu.max())
```

## Tuning notes

- Respect physical constraints (voltage limits, thermal limits, generator ramp rates).
- Use probabilistic forecasts and reserve scheduling for renewables and demand uncertainty.
- Neural surrogates should be validated against conventional solvers and checked for feasibility.

## Verification

1. Run a power flow on an IEEE benchmark and inspect bus voltages and branch loadings.
2. Train a PV/wind or load forecaster and backtest with rolling cross-validation.
3. Compare a neural OPF surrogate to a conventional solver on a held-out grid.
''',
        "references": [
            "https://www.pandapower.org/start/",
            "https://github.com/microsoft/gridsfm",
            "https://research.ibm.com/blog/gridfm-neural-solver-power-grid",
            "https://doi.org/10.1016/j.egyai.2026.100842",
        ],
    },
    {
        "name": "ai-for-smart-cities",
        "title": "AI for Smart Cities",
        "description": "Urban computing, IoT analytics, spatio-temporal forecasting, mobility, public safety, and citizen-centric services.",
        "devin_body": r'''
## When to use

You are analyzing urban sensor, mobility, or demographic data to support city planning, operations, or citizen services.

## Key concepts

- **Urban computing**: integration of sensing, data, and computing to understand and manage cities.
- **Spatio-temporal graph learning**: STGNNs for traffic, air quality, and crowd flow prediction.
- **Digital twins and IoT platforms**: real-time city models fed by heterogeneous sensors.
- **Citizen engagement and governance**: NLP and recommendation for participatory urban planning.
- **Sustainability and equity**: energy, emissions, accessibility, and resource distribution.

## Code pattern

```python
from torch_geometric_temporal.dataset import METRLADatasetLoader
from torch_geometric_temporal.signal import temporal_signal_split

loader = METRLADatasetLoader()
dataset = loader.get_dataset(num_timesteps_in=12, num_timesteps_out=12)
train, test = temporal_signal_split(dataset, train_ratio=0.8)
```

## Tuning notes

- Handle data sparsity, missing sensors, and distribution shifts across city zones.
- Respect privacy and consent when using mobility, camera, or social data.
- Evaluate models on multiple spatial and temporal horizons, not just aggregate accuracy.

## Verification

1. Train an STGNN for traffic or air-quality forecasting and compare to a temporal baseline.
2. Build a small digital-twin pipeline that ingests simulated IoT streams.
3. Audit model predictions for fairness across neighborhoods and demographics.
''',
        "references": [
            "https://www.mdpi.com/2071-1050/15/5/3916",
            "https://doi.org/10.1145/3768163",
            "https://www.mdpi.com/2624-6511/7/3/57",
            "https://dl.acm.org/doi/10.1109/TKDE.2023.3333824",
        ],
    },
    {
        "name": "ai-for-transportation",
        "title": "AI for Transportation",
        "description": "Traffic prediction, route optimization, public transit planning, autonomous driving, and multi-modal mobility.",
        "devin_body": r'''
## When to use

You need to predict, optimize, or simulate traffic, routes, transit, or autonomous-vehicle behavior in urban or highway networks.

## Key concepts

- **Spatio-temporal traffic forecasting**: predict flow, speed, or congestion on road graphs using GNNs and transformers.
- **Autonomous driving prediction**: multi-agent motion forecasting and planning under uncertainty.
- **Route and network optimization**: shortest paths, traffic-equilibrium, and multi-modal itinerary planning.
- **Public transit analytics**: ridership prediction, schedule optimization, and disruption recovery.
- **Sim-to-real and safety**: robustness to rare events, adversarial weather, and sensor failures.

## Code pattern

```python
import osmnx as ox
import networkx as nx

G = ox.graph_from_place("Berlin, Germany", network_type="drive")
orig = ox.distance.nearest_nodes(G, 13.4, 52.5)
dest = ox.distance.nearest_nodes(G, 13.5, 52.5)
route = nx.shortest_path(G, orig, dest, weight="length")
```

## Tuning notes

- Traffic patterns are highly non-stationary; use periodic and holiday features, and retrain frequently.
- Combine map priors with real-time data for robust routing.
- Pay attention to safety metrics, not just travel-time, for autonomous systems.

## Verification

1. Predict traffic speed on a real road network and evaluate MAE/RMSE.
2. Run a shortest-path or VRP solver on an OSMnx graph and sanity-check distances.
3. Test a motion-prediction model on a public benchmark such as Argoverse or nuScenes.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2109.11094",
            "https://ascelibrary.org/doi/10.1061/JTEPBS.TEENG-9105",
            "https://www.nature.com/articles/s41598-023-41902-y",
            "https://dl.acm.org/doi/10.1145/3637528.3671507",
        ],
    },
    {
        "name": "ai-for-logistics",
        "title": "AI for Logistics",
        "description": "Vehicle routing, last-mile delivery, warehouse automation, fleet scheduling, and dynamic logistics optimization.",
        "devin_body": r'''
## When to use

You are optimizing delivery routes, fleet dispatch, warehouse operations, or inventory flows under capacity, time, and cost constraints.

## Key concepts

- **Vehicle Routing Problem (VRP) and variants**: CVRP, VRPTW, multi-depot, dynamic, and stochastic VRP.
- **Last-mile optimization**: demand forecasting, route sequencing, and delivery-time windows.
- **Warehouse automation**: pick-path optimization, robot scheduling, and inventory placement.
- **Learning-based heuristics**: GNNs, reinforcement learning, and attention models for routing.
- **Sustainability**: fuel, emissions, and multi-modal trade-offs in logistics planning.

## Code pattern

```python
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

manager = pywrapcp.RoutingIndexManager(10, 2, 0)  # 10 nodes, 2 vehicles, depot 0
routing = pywrapcp.RoutingModel(manager)
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
solution = routing.SolveWithParameters(search_parameters)
```

## Tuning notes

- Combine exact solvers for small instances with learned heuristics for large, dynamic problems.
- Model real-world constraints: time windows, capacity, driver breaks, and customer priorities.
- Re-optimize in real time when new orders or disruptions arrive.

## Verification

1. Solve a CVRP or VRPTW instance and compare route cost to a baseline heuristic.
2. Run a delivery-time prediction model on historical GPS and order data.
3. Simulate dynamic disruptions and measure re-planning latency and cost.
''',
        "references": [
            "https://doi.org/10.3390/s25030955",
            "https://link.springer.com/article/10.1007/s44176-025-00053-2",
            "https://www.mdpi.com/2076-3417/15/14/8001",
            "https://arxiv.org/pdf/2402.04463",
        ],
    },
    {
        "name": "ai-for-manufacturing",
        "title": "AI for Manufacturing",
        "description": "Predictive maintenance, quality control, process optimization, digital twins, and human-interpretable factory AI.",
        "devin_body": r'''
## When to use

You are improving uptime, product quality, or process efficiency in a factory or industrial setting using sensor, image, or log data.

## Key concepts

- **Predictive maintenance (PdM)**: forecast equipment failures from vibration, temperature, acoustic, or current signatures.
- **Quality and defect detection**: vision and sensor-based inspection of products and processes.
- **Digital twins and process modeling**: simulation and optimization of production lines.
- **Explainable AI for operations**: SHAP, Grad-CAM, and attention for operator trust and regulatory compliance.
- **Edge deployment**: real-time inference on factory-floor devices and PLCs.

## Code pattern

```python
from sklearn.ensemble import IsolationForest
import numpy as np

X = np.load("sensor_features.npy")
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X)
anomalies = model.predict(X)
```

## Tuning notes

- Class imbalance and rare failures are common; use anomaly detection, survival models, or cost-sensitive learning.
- Watch for sensor drift and domain shift when models are deployed across machines or factories.
- Involve operators in validation and make explanations actionable.

## Verification

1. Train an anomaly detector on normal machine data and flag induced faults.
2. Build a defect classifier on manufacturing images and compare to human inspection.
3. Validate a predictive-maintenance model's lead time and false-alarm rate on a hold-out period.
''',
        "references": [
            "https://www.mdpi.com/1424-8220/26/3/911",
            "https://dl.acm.org/doi/10.1145/3732287",
            "https://www.mdpi.com/2227-9717/13/4/962",
            "https://arxiv.org/pdf/2603.11666",
        ],
    },
    {
        "name": "ai-for-supply-chain",
        "title": "AI for Supply Chain",
        "description": "Demand forecasting, inventory optimization, risk and resilience, supplier analytics, and end-to-end supply chain visibility.",
        "devin_body": r'''
## When to use

You need to forecast demand, plan inventory, detect disruptions, or optimize sourcing and distribution across a multi-echelon supply chain.

## Key concepts

- **Demand forecasting**: statistical, ML, and deep-learning models for SKU-, store-, and channel-level demand.
- **Inventory optimization**: safety stock, reorder points, and multi-echelon optimization under uncertainty.
- **Resilience and risk**: disruption prediction, supplier risk scoring, and scenario planning.
- **Hierarchical forecasting**: reconcile forecasts across product, location, and time hierarchies.
- **Real-time visibility**: IoT, ERP, and EDI data integration for end-to-end tracking.

## Code pattern

```python
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA
import pandas as pd

df = pd.read_csv("demand_history.csv")  # columns: unique_id, ds, y
sf = StatsForecast(models=[AutoARIMA(season_length=52)], freq="W")
sf.fit(df)
fcst = sf.predict(h=8, level=[90])
```

## Tuning notes

- Include promotion, calendar, and external shock features (holidays, weather, macro indicators).
- Use hierarchical reconciliation to keep forecasts consistent across levels.
- Balance service level, holding cost, and obsolescence in inventory decisions.

## Verification

1. Backtest demand forecasts with rolling origin and report MAE, RMSE, and bias.
2. Simulate an inventory policy under stochastic demand and compare service level and cost.
3. Identify and rank suppliers by risk using a multi-criteria scoring model.
''',
        "references": [
            "https://www.mdpi.com/2571-5577/7/5/93",
            "https://hbr.org/2024/03/how-machine-learning-will-transform-supply-chain-management",
            "https://www.mdpi.com/2305-6290/8/4/111",
            "https://doi.org/10.1109/access.2024.3507161",
        ],
    },
    {
        "name": "ai-for-public-health",
        "title": "AI for Public Health",
        "description": "Disease surveillance, outbreak prediction, resource allocation, geospatial health modeling, and health-equity analytics.",
        "devin_body": r'''
## When to use

You are working to predict disease burden, allocate resources, or understand health inequities at the population or health-system level.

## Key concepts

- **Syndromic and digital surveillance**: combine traditional epidemiology with search, social, mobile, and environmental signals.
- **Outbreak forecasting**: nowcasting and short-term forecasting of infectious diseases.
- **Geospatial and Earth-AI modeling**: link environmental, climate, and mobility data to health outcomes.
- **Resource allocation**: optimize clinic, vaccine, or workforce distribution under constraints.
- **Health equity and bias**: audit models for demographic and geographic disparities.

## Code pattern

```python
import lightgbm as lgb
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = lgb.LGBMClassifier(n_estimators=200, learning_rate=0.05)
model.fit(X_train, y_train, eval_set=[(X_test, y_test)])
```

## Tuning notes

- Public-health labels are often delayed, sparse, or noisy; use nowcasting and imputation carefully.
- Protect privacy when using individual-level data; aggregate and anonymize.
- Evaluate fairness across race, age, gender, geography, and socioeconomic groups.

## Verification

1. Build an outbreak-forecasting model and evaluate probabilistic calibration on a held-out season.
2. Predict clinic utilization or vaccination coverage using geospatial features.
3. Audit model predictions for subgroup disparities and report equity metrics.
''',
        "references": [
            "https://health.google/public-health/",
            "https://blog.google/innovation-and-ai/technology/health/google-earth-ai-global-public-health/",
            "https://www.nature.com/articles/s41467-026-72655-7",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC9619602/",
        ],
    },
    {
        "name": "ai-for-disaster-response",
        "title": "AI for Disaster Response",
        "description": "Situational awareness, damage assessment, evacuation planning, supply pre-positioning, and multi-modal disaster imagery analysis.",
        "devin_body": r'''
## When to use

You are supporting first responders, emergency managers, or humanitarian agencies before, during, or after a natural or human-made disaster.

## Key concepts

- **Multi-modal disaster imagery**: satellite, aerial, drone (sUAS), and social-media imagery for rapid assessment.
- **Damage and change detection**: segmentation and classification of building, road, and infrastructure damage.
- **Situational awareness and common operating picture**: fuse imagery, sensor, and crowd data into GIS-ready outputs.
- **Evacuation and logistics**: optimize routes, shelter assignment, and resource pre-positioning.
- **Operational constraints**: disconnected environments, real-time deadlines, and heterogeneous data quality.

## Code pattern

```python
import rasterio
from rasterio.plot import show

with rasterio.open("post_disaster.tif") as src:
    rgb = src.read([1, 2, 3])
    transform = src.transform
show(rgb)
```

## Tuning notes

- Models must generalize across resolutions, sensors, and disaster types; domain adaptation is often needed.
- Balance speed and accuracy: lightweight models for field deployment, heavier ones for cloud post-processing.
- Human-in-the-loop validation is critical for high-stakes decisions.

## Verification

1. Train a building-damage classifier on xBD or a sUAS damage dataset and report per-class F1.
2. Run a change-detection pipeline on pre- and post-event satellite imagery.
3. Validate a route-planning tool against real road closures and shelter demand scenarios.
''',
        "references": [
            "https://www.pnnl.gov/projects/rapid-analytics-disaster-response",
            "https://www.jhuapl.edu/sites/default/files/2022-12/AIEnabledSAinDisasterResponse.pdf",
            "https://www.cmu.edu/ai-sdm/research/research-highlights/bda-rda-models.html",
            "https://ojs.aaai.org/index.php/AAAI/article/view/41474",
        ],
    },
    {
        "name": "ai-for-space-exploration",
        "title": "AI for Space Exploration",
        "description": "Onboard autonomy, science target selection, anomaly detection, mission planning, and analysis of space and Earth-observation data.",
        "devin_body": r'''
## When to use

You are designing, simulating, or operating spacecraft, rovers, or satellites that must make decisions with limited communication, power, or compute.

## Key concepts

- **Onboard autonomy and science agents**: detect events, prioritize observations, and retarget instruments without ground-in-the-loop.
- **Dynamic targeting and opportunistic science**: AI-driven selection of targets during orbital overflights.
- **Anomaly detection and health monitoring**: detect faults in telemetry, instruments, and subsystems.
- **Mission planning and scheduling**: optimize observation campaigns under constraints.
- **Earth-observation and planetary data**: analyze multispectral, hyperspectral, and mass-spectrometer data.

## Code pattern

```python
from astropy.io import fits
import numpy as np

with fits.open("observation.fits") as hdul:
    image = hdul[0].data
    header = hdul[0].header

# Simple onboard anomaly score
score = np.abs(image - np.median(image)) / np.std(image)
anomaly_mask = score > 5
```

## Tuning notes

- Resource constraints (power, compute, radiation-hardened hardware) dominate design choices.
- Communication delays and blackouts require robust onboard decision-making.
- Validate autonomy with high-fidelity simulators and representative analog datasets.

## Verification

1. Implement a simple anomaly detector on spacecraft telemetry and flag synthetic faults.
2. Build a target-prioritization model and test it in a mission simulator.
3. Process a FITS image cube and validate derived science products against ground truth.
''',
        "references": [
            "https://science.jpl.nasa.gov/projects/autonomous-sciencecraft-experiment-ase/",
            "https://www.nasa.gov/science-research/earth-science/how-nasa-is-testing-ai-to-make-earth-observing-satellites-smarter/",
            "https://ntrs.nasa.gov/citations/20240005003",
            "https://science.nasa.gov/science-research/science-enabling-technology/technology-highlights/towards-autonomous-surface-missions-on-ocean-worlds/",
        ],
    },
    {
        "name": "ai-for-governance",
        "title": "AI for Governance",
        "description": "Public-service delivery, regulatory compliance, algorithmic accountability, participatory policy tools, and fair decision-support systems.",
        "devin_body": r'''
## When to use

You are building or auditing AI systems used by governments, public agencies, or regulated industries where accountability, fairness, and transparency are essential.

## Key concepts

- **Algorithmic accountability and transparency**: model cards, documentation, explainability, and audit trails.
- **Fairness and bias auditing**: group fairness, equalized odds, demographic parity, and calibration by subgroup.
- **Public-service automation**: eligibility, benefits, permitting, and case routing with human oversight.
- **Regulatory compliance**: EU AI Act, U.S. AI accountability frameworks, OECD AI Principles.
- **Participatory and deliberative AI**: citizen input, redress mechanisms, and public comment analysis.

## Code pattern

```python
from fairlearn.metrics import demographic_parity_difference
from fairlearn.reductions import ExponentiatedGradient, DemographicParity
from sklearn.linear_model import LogisticRegression

estimator = LogisticRegression()
mitigated = ExponentiatedGradient(estimator, DemographicParity())
mitigated.fit(X_train, y_train, sensitive_features=A_train)
```

## Tuning notes

- Quantitative fairness metrics cannot capture all normative concerns; embed human review and due process.
- Document data sources, assumptions, limitations, and intended use for every public-facing model.
- Plan for redress, appeal, and continuous monitoring after deployment.

## Verification

1. Audit a public-service model for demographic disparities with Fairlearn or Aequitas.
2. Generate SHAP or LIME explanations for representative decisions and review with stakeholders.
3. Map model risks and mitigations to an applicable AI governance framework (EU AI Act, NIST AI RMF, OECD).
''',
        "references": [
            "https://www.ntia.gov/issues/artificial-intelligence/ai-accountability-policy-report",
            "https://www.europarl.europa.eu/RegData/etudes/STUD/2019/624262/EPRS_STU(2019)624262_EN.pdf",
            "https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng",
            "https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/10/the-state-of-implementation-of-the-oecd-ai-principles-four-years-on_b9f13b5c/835641c9-en.pdf",
        ],
    },
    {
        "name": "ai-for-social-good",
        "title": "AI for Social Good",
        "description": "Education, poverty alleviation, agriculture, humanitarian response, accessibility, and community-driven AI for underserved populations.",
        "devin_body": r'''
## When to use

You are deploying AI to improve outcomes in education, health, agriculture, humanitarian aid, or economic inclusion, especially in low-resource or marginalized communities.

## Key concepts

- **Education and personalized tutoring**: adaptive learning, chat-based tutoring, and low-bandwidth delivery.
- **Poverty and development economics**: rigorous impact evaluation, cost-effectiveness, and scalable social programs.
- **Agriculture and food security**: crop-health monitoring, yield prediction, and extension services for smallholder farmers.
- **Humanitarian and crisis response**: information triage, needs assessment, and resource matching.
- **Participatory design and ethics**: co-design with communities, local language support, and harm prevention.

## Code pattern

```python
from transformers import pipeline

qa = pipeline(
    "question-answering",
    model="distilbert-base-uncased-distilled-squad"
)
answer = qa(question="What is crop rotation?", context=extension_text)
```

## Tuning notes

- Prioritize low-cost, low-bandwidth, and offline-capable deployments for last-mile users.
- Conduct randomized evaluations or quasi-experimental impact analysis when possible.
- Guard against paternalism and unintended consequences; center affected communities in design.

## Verification

1. Run a small RCT or A/B test of an AI tutoring or information tool and measure learning or adoption outcomes.
2. Build a farmer-facing crop-advisory prototype and validate recommendations with local experts.
3. Assess cost-effectiveness and equity impacts relative to non-AI alternatives.
''',
        "references": [
            "https://www.povertyactionlab.org/sites/default/files/review-paper/J-PAL_AI_Evidence_Playbook_02.16.2026.pdf",
            "https://arxiv.org/pdf/2402.09809",
            "https://solve.mit.edu/solutions/21651",
            "https://documents1.worldbank.org/curated/en/099548105192529324/pdf/IDU-c09f40d8-9ff8-42dc-b315-591157499be7.pdf",
            "https://news.mit.edu/2026/new-j-pal-research-policy-initiative-to-test-scale-ai-innovations-fight-poverty-0212",
        ],
    },
]
