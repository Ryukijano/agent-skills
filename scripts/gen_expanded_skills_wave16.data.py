SKILLS = [
    {
        "name": "ai-for-climate-policy",
        "title": "AI for Climate Policy",
        "description": "Extract and classify quantified climate targets from national laws and NDCs to track policy alignment and accountability.",
        "devin_body": r'''
## When to use

You need to analyze, compare, or monitor national climate laws, Nationally Determined Contributions (NDCs), or corporate climate disclosures at scale.

## Usage

- Extract quantified climate targets (net-zero, reduction, renewable) from NDCs, laws, and corporate disclosures.
- Compare NDCs with Voluntary National Reviews (VNRs) and SDGs to score alignment.
- Apply domain-adapted language models such as ClimateBERT to climate-finance and policy text.
- Track policy implementation, theme shifts, and equity implications over time.

## Steps

1. Collect NDCs, national climate laws, VNRs, and corporate climate reports from official registries.
2. Chunk and normalize the documents; use a domain-adapted LM (e.g., ClimateBERT) to classify paragraphs and extract quantified targets.
3. Build an alignment-scoring pipeline that maps commitments to SDGs and NDC objectives.
4. Track climate-finance flows and implementation progress against stated targets across countries and years.
5. Validate extraction and alignment results against expert annotations and produce transparent, auditable tables.
6. Deploy the pipeline as a monitoring dashboard for policy analysts and climate-finance stakeholders.

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
        "description": "Solve AC optimal power flow with neural surrogates to schedule generation and integrate renewables within milliseconds.",
        "devin_body": r'''
## When to use

You are building, operating, or studying power systems with high renewable penetration and need fast, scalable, and physically consistent predictions or optimizations.

## Usage

- Solve or approximate AC/DC power flow and Optimal Power Flow (OPF) with neural surrogates.
- Forecast solar, wind, and demand with probabilistic time-series models.
- Monitor grid stability, fault detection, and N-1 contingency security in real time.
- Deploy grid foundation models (e.g., GridSFM, OpenGridFM, GridFM) for millisecond dispatch decisions.

## Steps

1. Build or load a grid model (e.g., pandapower IEEE case or a real network) and define constraints (voltage, thermal, generator limits).
2. Train a neural surrogate or foundation model to predict power-flow/OPF solutions from load and generation inputs.
3. Implement probabilistic solar, wind, and load forecasting with rolling cross-validation.
4. Run stability and N-1 contingency checks, flagging constraint violations and critical branches.
5. Compare the neural OPF surrogate to a conventional solver on held-out operating conditions and check feasibility.
6. Deploy the fastest-acceptable model in a control room or market-clearing loop with uncertainty-aware reserve scheduling.

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
        "description": "Optimize fixed-time traffic signals from connected-vehicle trajectories to cut urban delays and stops by up to 30 percent.",
        "devin_body": r'''
## When to use

You are analyzing urban sensor, mobility, or demographic data to support city planning, operations, or citizen services.

## Usage

- Forecast traffic, air quality, crowd flow, and energy demand with spatio-temporal graph and sequence models.
- Build digital twins and IoT platforms that mirror real-time city operations.
- Apply NLP and recommendation systems to participatory planning and citizen engagement.
- Optimize energy, emissions, accessibility, and resource distribution for sustainable and equitable cities.

## Steps

1. Ingest heterogeneous urban data: traffic loops, public transit, air-quality sensors, weather, mobility, and demographics.
2. Build a spatio-temporal graph or digital-twin model to represent city zones, roads, and sensor networks.
3. Train forecasting models for traffic, air quality, and energy demand and evaluate them on multiple horizons.
4. Deploy anomaly detection and decision-support modules for public safety, transit, and emergency response.
5. Audit model outputs for fairness across neighborhoods and incorporate citizen feedback.
6. Integrate validated predictions into city operations dashboards and policy planning tools.

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
        "description": "Retime city traffic signals from sparse vehicle trajectories and prioritize public transit to reduce congestion and emissions.",
        "devin_body": r'''
## When to use

You need to predict, optimize, or simulate traffic, routes, transit, or autonomous-vehicle behavior in urban or highway networks.

## Usage

- Forecast traffic flow, speed, and congestion on road graphs with GNNs and spatio-temporal models.
- Predict multi-agent motion and plan safe trajectories for autonomous vehicles.
- Optimize shortest paths, traffic equilibrium, and multi-modal itineraries.
- Predict transit ridership, optimize schedules, and recover from disruptions.

## Steps

1. Ingest road graph, real-time traffic, weather, transit, and incident data for the target network.
2. Train a spatio-temporal traffic-forecasting model and validate on rolling cross-validation against baselines.
3. Implement route or network-optimization algorithms (A*, traffic-equilibrium, multi-modal) and benchmark travel time.
4. Build a multi-agent motion-prediction or trajectory-planning model for autonomous driving and test on a public benchmark.
5. Add public-transit ridership and schedule-optimization modules and simulate disruption recovery.
6. Deploy the integrated forecasting, routing, and planning pipeline with safety and sim-to-real checks.

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
        "description": "Use optimization and learning-based methods to solve vehicle routing, last-mile delivery, warehouse automation, and fleet-scheduling problems.",
        "devin_body": r'''
## When to use

You are optimizing delivery routes, fleet dispatch, warehouse operations, or inventory flows under capacity, time, and cost constraints.

## Usage

- Model and solve VRP variants (CVRP, VRPTW, multi-depot, dynamic, stochastic) with exact or learned heuristics.
- Optimize last-mile demand forecasting, route sequencing, and time-window compliance.
- Automate warehouse pick-paths, robot scheduling, and inventory slotting.
- Reduce fuel, emissions, and cost by balancing multi-modal and real-time re-routing trade-offs.

## Steps

1. Gather order, depot, vehicle, traffic, weather, and customer time-window data for the logistics network.
2. Build a VRP or routing model with capacity and time-window constraints using OR-Tools, RL, or GNN heuristics.
3. Integrate demand forecasting to pre-position inventory and sequence last-mile routes.
4. Add warehouse pick-path and robot-scheduling optimization, measuring throughput and travel distance.
5. Implement real-time re-routing when disruptions occur and compare cost and SLA performance to baselines.
6. Track fuel, emissions, and cost KPIs, and deploy the integrated logistics decision-support system.

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
        "description": "Apply predictive maintenance, vision-based quality control, process modeling, and edge AI to improve uptime and efficiency in factories.",
        "devin_body": r'''
## When to use

You are improving uptime, product quality, or process efficiency in a factory or industrial setting using sensor, image, or log data.

## Usage

- Forecast equipment failures from vibration, temperature, acoustic, or current signatures.
- Detect product and process defects with vision and sensor-based inspection.
- Build digital twins and process models to simulate and optimize production lines.
- Deploy explainable AI on edge devices and PLCs for operator trust and regulatory compliance.

## Steps

1. Collect sensor, image, log, and maintenance records from production machines and lines.
2. Train anomaly-detection or survival models for predictive maintenance and measure warning lead time.
3. Build computer-vision classifiers or segmentation models for defect inspection and compare to human inspection.
4. Create a digital twin or process model and use it to simulate line bottlenecks and what-if optimizations.
5. Add explainability (SHAP, Grad-CAM, attention) and validate with operators and domain experts.
6. Deploy approved models on edge devices or PLCs and continuously monitor drift and false-alarm rates.

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
        "description": "Use ML to forecast demand, optimize inventory, score supplier risk, and improve visibility and resilience across multi-echelon supply chains.",
        "devin_body": r'''
## When to use

You need to forecast demand, plan inventory, detect disruptions, or optimize sourcing and distribution across a multi-echelon supply chain.

## Usage

- Forecast SKU-, store-, and channel-level demand with statistical, ML, or deep-learning models.
- Optimize safety stock, reorder points, and multi-echelon inventory under uncertainty.
- Predict disruptions and score supplier risk with multi-criteria and scenario models.
- Reconcile forecasts hierarchically and integrate IoT, ERP, and EDI data for real-time visibility.

## Steps

1. Ingest historical demand, promotions, external signals, inventory, supplier, and logistics data.
2. Train demand-forecasting models at the right granularity and reconcile them across product, location, and time.
3. Build inventory-optimization models that balance service level, holding cost, and obsolescence under demand uncertainty.
4. Score supplier risk and predict disruptions from financial, geopolitical, weather, and quality signals.
5. Integrate real-time IoT/ERP/EDI feeds and build exception alerts for stockouts, delays, and bottlenecks.
6. Backtest forecasts and inventory policies with rolling origin and measure total landed cost and service level.

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
        "description": "Use ML and geospatial models for disease surveillance, outbreak forecasting, resource allocation, and health-equity analytics.",
        "devin_body": r'''
## When to use

You are working to predict disease burden, allocate resources, or understand health inequities at the population or health-system level.

## Usage

- Combine traditional epidemiology with search, social, mobile, and environmental signals for syndromic surveillance.
- Nowcast and short-term forecast infectious disease burden and outbreaks.
- Link environmental, climate, and mobility data to health outcomes through geospatial ML.
- Optimize clinic, vaccine, and workforce distribution and audit for demographic and geographic equity.

## Steps

1. Aggregate case data, syndromic signals, search/social trends, mobility, weather, and environmental covariates.
2. Build a nowcasting or short-term forecasting model and validate probabilistic calibration on held-out seasons.
3. Train geospatial models that link climate, land use, and mobility to disease risk and health outcomes.
4. Optimize resource allocation (clinics, vaccines, workforce) under capacity and equity constraints.
5. Audit predictions for bias across age, gender, race, and geography and report equity metrics.
6. Deploy a decision-support dashboard for public-health agencies and update as new data streams arrive.

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
        "description": "Use multi-modal imagery and ML to assess damage, map situational awareness, plan evacuations, and pre-position supplies during disasters.",
        "devin_body": r'''
## When to use

You are supporting first responders, emergency managers, or humanitarian agencies before, during, or after a natural or human-made disaster.

## Usage

- Analyze satellite, aerial, drone, and social-media imagery for rapid disaster assessment.
- Detect and classify building, road, and infrastructure damage from multi-temporal imagery.
- Build a common operating picture by fusing imagery, sensors, and crowd data into GIS-ready outputs.
- Optimize evacuation routes, shelter assignment, and resource pre-positioning under real-time constraints.

## Steps

1. Collect pre- and post-event satellite, aerial, drone, and social-media imagery and align them to a common CRS.
2. Run a change-detection or damage-segmentation model and classify damage levels (e.g., xBD-style labels).
3. Extract roads, shelters, and critical infrastructure and estimate affected population and needs.
4. Optimize evacuation routes, shelter assignment, and resource pre-positioning with capacity and time constraints.
5. Build a live situational-awareness dashboard that fuses model outputs with field reports and sensor data.
6. Validate damage labels with ground truth and train a lightweight edge model for offline field deployment.

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
        "description": "Select science targets and detect anomalies onboard spacecraft and rovers to maximize discovery without round-trip latency.",
        "devin_body": r'''
## When to use

You are designing, simulating, or operating spacecraft, rovers, or satellites that must make decisions with limited communication, power, or compute.

## Usage

- Run onboard science agents that detect events, prioritize targets, and retarget instruments without ground-in-the-loop.
- Select targets dynamically during orbital overflights or rover traverses.
- Detect faults in telemetry, instruments, and subsystems with anomaly detection.
- Optimize observation and operations schedules under power, memory, and downlink constraints.

## Steps

1. Define science goals, instrument constraints, and onboard compute/downlink budgets for the mission.
2. Train event-detection and target-priority models on representative orbital or rover datasets.
3. Implement onboard anomaly detection on telemetry and instrument health data.
4. Build a scheduler that optimizes observation campaigns and downlink priorities under resource constraints.
5. Validate the autonomy stack in high-fidelity mission simulators and analog test datasets.
6. Deploy the qualified models on flight-like hardware and monitor performance during operations.

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
        "description": "Audit public-sector algorithms against governance, privacy, and fairness standards to ensure accountable and participatory AI deployment.",
        "devin_body": r'''
## When to use

You are building or auditing AI systems used by governments, public agencies, or regulated industries where accountability, fairness, and transparency are essential.

## Usage

- Document and audit AI systems with model cards, explainability, and algorithmic accountability frameworks.
- Audit for group fairness, equalized odds, demographic parity, and calibration across subgroups.
- Automate public-service decisions (eligibility, benefits, permitting) with human oversight and due process.
- Map systems to regulatory frameworks (EU AI Act, NIST AI RMF, OECD AI Principles).

## Steps

1. Inventory the AI system, its training data, intended use, stakeholders, and risk profile.
2. Document assumptions, limitations, and model cards, and establish audit trails for decisions.
3. Measure fairness and bias across subgroups using appropriate metrics and mitigations (e.g., Fairlearn, Aequitas).
4. Generate explainable outputs (SHAP, LIME, counterfactuals) and review representative decisions with stakeholders.
5. Map risks and mitigations to applicable governance and regulatory frameworks.
6. Set up continuous monitoring, redress mechanisms, and periodic re-audits.

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
        "description": "Optimize vaccination outreach and agricultural advice for low-resource communities to improve health and livelihood outcomes.",
        "devin_body": r'''
## When to use

You are deploying AI to improve outcomes in education, health, agriculture, humanitarian aid, or economic inclusion, especially in low-resource or marginalized communities.

## Usage

- Deliver personalized, low-bandwidth tutoring and educational support with adaptive learning systems.
- Evaluate impact with randomized or quasi-experimental designs and cost-effectiveness analysis.
- Support smallholder agriculture with crop-health monitoring, yield prediction, and extension chatbots.
- Triage information, assess needs, and match resources in humanitarian and crisis response.

## Steps

1. Engage affected communities and domain partners to define the problem, outcomes, and ethical constraints.
2. Co-design a low-cost, low-bandwidth, and accessible AI solution (chatbot, advisory app, monitoring tool).
3. Collect local data and train or adapt models, ensuring local language and cultural relevance.
4. Run a pilot with an RCT, A/B test, or quasi-experimental design to measure learning, adoption, or welfare outcomes.
5. Assess cost-effectiveness, equity, and unintended consequences compared to non-AI alternatives.
6. Iterate with community feedback, scale responsibly, and monitor for harm and drift.

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
