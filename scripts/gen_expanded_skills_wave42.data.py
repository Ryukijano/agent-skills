SKILLS = [
    {
        "name": "ai-for-civil-engineering",
        "title": "AI for Civil Engineering",
        "description": "Machine learning for structural health monitoring, geotechnical prediction, transportation systems, water resources, and resilient infrastructure.",
        "devin_body": r'''## When to use

You are designing, monitoring, or maintaining civil infrastructure such as bridges, buildings, dams, roads, or water systems and want data-driven predictions or inspections.

## Usage

- **Structural health monitoring (SHM)**: vibration, strain, and vision-based damage detection.
- **Geotechnical prediction**: soil liquefaction, slope stability, and settlement models.
- **Transportation and traffic**: flow forecasting, incident detection, and route optimization.
- **Water resources**: flood, water quality, and demand forecasting.
- **BIM and digital twins**: as-built vs. design comparison and lifecycle simulation.

## Steps

1. Collect structural, geotechnical, traffic, or water-resource data and define the prediction target.
2. Engineer domain features (vibration spectra, image patches, sensor time-series, weather inputs).
3. Train and validate a model with time-aware or site-aware splits.
4. Integrate the model with BIM, GIS, or digital-twin dashboards.
5. Monitor and retrain as conditions or codes change.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import IsolationForest

# Flag anomalous vibration readings from a bridge sensor
X = np.load("bridge_vibration.npy")
model = IsolationForest(contamination=0.02, random_state=42).fit(X)
scores = model.decision_function(X)
```

## Tuning notes

- Use physics-informed or hybrid models for safety-critical predictions.
- Combine IoT and drone imagery for spatial coverage.
- Validate against code requirements and expert inspections.

## Verification

1. Train a crack-detection model on concrete images and report precision-recall.
2. Forecast traffic flow for an intersection and compare to a seasonal baseline.
3. Predict concrete compressive strength and compare to lab results.

''',
        "references": [
            "https://doi.org/10.3390/app151910499",
            "https://doi.org/10.1016/j.kscej.2025.100203",
            "https://link.springer.com/article/10.1007/s41872-025-00364-z",
            "https://www.frontiersin.org/journals/built-environment/articles/10.3389/fbuil.2022.1007886/full",
        ],
    },
    {
        "name": "ai-for-mechanical-engineering",
        "title": "AI for Mechanical Engineering",
        "description": "AI for mechanical design, predictive maintenance, digital twins, dynamic systems, and manufacturing process optimization.",
        "devin_body": r'''## When to use

You are designing mechanical components or systems, monitoring rotating machinery, optimizing maintenance, or simulating dynamics and controls.

## Usage

- **Predictive maintenance and RUL**: vibration and acoustic fault diagnosis, remaining useful life.
- **Digital twins**: real-time virtual replicas of mechanical assets.
- **Generative design and topology optimization**: AI-candidate shapes and lightweighting.
- **System dynamics and control**: physics-informed neural ODEs and RL for control.
- **Manufacturing process modeling**: machining, additive, and forming.

## Steps

1. Collect sensor data (vibration, acoustic, torque) and failure logs from mechanical assets.
2. Extract condition indicators, time-domain features, and operating context.
3. Train a fault-detection or RUL model and validate against physical baselines.
4. Deploy the model on edge devices or in a digital twin.
5. Retrain when machinery, materials, or operating regimes change.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Classify bearing fault type from vibration features
X = df[["rms", "kurtosis", "crest_factor", "skewness"]]
y = df["fault_type"]
model = RandomForestClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Use chronological splits and domain adaptation for machinery data.
- Balance imbalanced fault classes with weights or resampling.
- Validate digital twins against high-fidelity physics simulators.

## Verification

1. Train a bearing-fault classifier and report accuracy on a holdout test set.
2. Build a digital twin of a simple mechanical system and compare to an ODE model.
3. Run a topology optimization and check stress constraints.

''',
        "references": [
            "https://doi.org/10.1016/j.jmsy.2023.10.010",
            "https://doi.org/10.1016/j.jmsy.2025.07.006",
            "https://www.nature.com/articles/s41598-024-63990-0",
            "https://link.springer.com/article/10.1007/s40684-025-00750-z",
        ],
    },
    {
        "name": "ai-for-electrical-engineering",
        "title": "AI for Electrical Engineering",
        "description": "AI for power systems, smart grids, renewable integration, power electronics, fault diagnosis, and energy management.",
        "devin_body": r'''## When to use

You are analyzing or operating power systems, smart grids, renewable plants, or power electronics and need accurate detection, forecasting, or control.

## Usage

- **Fault detection and location**: transient classification and protection schemes.
- **Load and renewable forecasting**: solar, wind, and demand prediction.
- **Power quality and stability**: anomaly detection and dynamic security assessment.
- **Smart grid optimization**: unit commitment, voltage control, and demand response.
- **Power electronics**: converter health monitoring and control design.

## Steps

1. Collect PMU, SCADA, AMI, or power-electronics data and label fault/quality events.
2. Engineer time- and frequency-domain features and respect grid topology.
3. Train a fault or forecasting model with chronological cross-validation.
4. Validate against power-flow or digital-twin simulations before deployment.
5. Monitor for concept drift and renewable/load changes.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Classify power-line fault signatures from PMU data
X = df[["voltage_mag", "current_mag", "phase_angle"]]
y = df["fault_type"]
model = RandomForestClassifier(class_weight="balanced", random_state=42).fit(X, y)
```

## Tuning notes

- Use time-based splits to avoid leakage in time-series data.
- Handle class imbalance and noisy labels in fault datasets.
- Validate stability-critical decisions with power-flow simulators.

## Verification

1. Train a fault classifier and report precision-recall for rare faults.
2. Build a day-ahead solar or load forecast and compare to a baseline.
3. Detect power-quality anomalies and verify against event logs.

''',
        "references": [
            "https://www.mdpi.com/1996-1073/18/18/4983",
            "https://www.mdpi.com/2227-9717/13/1/48",
            "https://doi.org/10.1016/j.rineng.2024.103884",
            "https://www.frontiersin.org/journals/smart-grids/articles/10.3389/frsgr.2024.1371153/full",
        ],
    },
    {
        "name": "ai-for-chemical-engineering",
        "title": "AI for Chemical Engineering",
        "description": "AI for process design, optimization, control, reaction engineering, materials discovery, and digital chemical plants.",
        "devin_body": r'''## When to use

You are designing or operating chemical processes, building surrogate models of reactors or separations, or automating process control.

## Usage

- **Process optimization and control**: surrogate-based and reinforcement-learning control.
- **Reaction and kinetic modeling**: neural ODEs and graph neural networks for chemistry.
- **Molecular and materials design**: generative models, property prediction, retrosynthesis.
- **Digital twins of plants**: real-time soft sensors and anomaly detection.
- **Safety and quality control**: fault detection and product quality prediction.

## Steps

1. Collect process data, lab assays, reaction conditions, and simulation outputs.
2. Build a dataset that respects mass/energy balances and operating constraints.
3. Train a surrogate, control, or property-prediction model.
4. Validate against first-principles simulators and pilot-plant data.
5. Deploy with real-time monitoring and periodic retraining.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict product yield from reactor conditions
X = df[["temperature", "pressure", "catalyst_load", "residence_time"]]
y = df["yield"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Respect physical constraints (mass/energy balances) in data-driven models.
- Use multi-fidelity data and active learning for expensive simulations.
- Validate control policies against first-principles simulators.

## Verification

1. Train a surrogate for a reaction yield and compare to a mechanistic model.
2. Build a soft sensor for an unmeasured quality variable.
3. Implement an RL or MPC policy and show stable setpoint tracking.

''',
        "references": [
            "https://doi.org/10.1002/cjce.70032",
            "https://www.mdpi.com/2227-9717/11/2/330",
            "https://doi.org/10.1002/cjce.24246",
            "https://doi.org/10.48550/arxiv.2412.18529",
        ],
    },
    {
        "name": "ai-for-aerospace-engineering",
        "title": "AI for Aerospace Engineering",
        "description": "AI for aerodynamic design, propulsion, structural analysis, flight dynamics, GNC, and certification of aerospace vehicles.",
        "devin_body": r'''## When to use

You are designing aircraft or spacecraft, building reduced-order models, optimizing aerodynamic/structural/propulsion systems, or certifying aerospace engineering decisions.

## Usage

- **Aerodynamic surrogate and shape optimization**: data-driven lift/drag models and adjoint-free design.
- **Structural analysis and loads**: surrogate models for finite-element and fatigue life.
- **Propulsion and combustion**: reduced-order models and design-space exploration.
- **Flight dynamics and GNC**: learning-based control and trajectory optimization.
- **Certification and assurance**: UQ, explainability, and verification for aerospace AI.

## Steps

1. Collect aerodynamic, structural, propulsion, or flight-dynamics data.
2. Build multi-fidelity datasets combining low- and high-fidelity simulations.
3. Train a surrogate or control model with physics-informed constraints.
4. Validate against CFD, wind tunnel, or flight test data.
5. Document uncertainty and certification evidence before deployment.

## Code pattern

```python
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor

# Build a surrogate for an airfoil lift coefficient
X = design_params  # e.g., [angle_of_attack, camber, thickness]
y = cl_values
model = GaussianProcessRegressor(normalize_y=True).fit(X, y)
```

## Tuning notes

- Aerospace data is expensive; use active learning and multi-fidelity models.
- Preserve physical invariants (conservation laws, smoothness).
- Validate against CFD, wind tunnel, or flight test data.

## Verification

1. Train a surrogate for an airfoil and compare to a CFD run.
2. Run an aerodynamic shape optimization and check convergence.
3. Demonstrate uncertainty quantification for a flight-relevant prediction.

''',
        "references": [
            "https://doi.org/10.1016/j.paerosci.2022.100849",
            "https://journals.sagepub.com/doi/10.1177/0954410019864485",
            "https://doi.org/10.1016/j.oceaneng.2024.119263",
            "https://www.ccs.upm.es/research/publications/a-review-of-surrogate-modeling-techniques-for-aerodynamic-analysis-and-optimization-current-limitations-and-future-challenges-in-industry/",
        ],
    },
    {
        "name": "ai-for-biomedical-engineering",
        "title": "AI for Biomedical Engineering",
        "description": "AI for medical devices, wearable biosensors, biomechanics, neural engineering, tissue engineering, and clinical diagnostics.",
        "devin_body": r'''## When to use

You are developing wearable or implantable devices, analyzing biosignals, designing medical imaging classifiers, or modeling biomechanical systems.

## Usage

- **Biosignal analysis**: ECG, EEG, EMG, PPG, and motion-signal processing.
- **Wearable and point-of-care devices**: continuous monitoring and edge AI.
- **Medical imaging and diagnostics**: classification, segmentation, and anomaly detection.
- **Biomechanics and neural engineering**: movement analysis, neural interfaces, and prosthetics.
- **Tissue and biomaterials**: generative design and property prediction.

## Steps

1. Collect biosignal, imaging, wearable, or biomechanical data with ethical approvals.
2. Preprocess signals to remove artifacts and standardize patient cohorts.
3. Train a diagnostic, monitoring, or device-control model.
4. Validate with clinical reference standards and across demographic groups.
5. Deploy under regulatory pathways with continuous safety monitoring.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Classify ECG beat type from time-series features
X = np.load("ecg_features.npy")
y = np.load("beat_labels.npy")
model = RandomForestClassifier(class_weight="balanced", random_state=42).fit(X, y)
```

## Tuning notes

- Prioritize patient safety, FDA/CE regulatory pathways, and clinical validation.
- Address label noise, class imbalance, and sensor artifacts.
- Validate on multi-site data to ensure equitable performance.

## Verification

1. Train a biosignal classifier and report sensitivity/specificity.
2. Build a wearables inference pipeline and measure battery/latency tradeoffs.
3. Compare an AI diagnostic to a clinical reference standard on a holdout set.

''',
        "references": [
            "https://doi.org/10.3390/bios15070410",
            "https://doi.org/10.3390/jpm14020203",
            "https://doi.org/10.1039/D5MH00451A",
            "https://doi.org/10.3390/bios14040183",
        ],
    },
    {
        "name": "ai-for-software-engineering",
        "title": "AI for Software Engineering",
        "description": "AI for code generation, testing, debugging, program repair, code review, and design assistance.",
        "devin_body": r'''## When to use

You are building, maintaining, or reviewing software and want to use AI to generate, test, debug, or document code.

## Usage

- **Code generation and completion**: large language models and code-specific foundation models.
- **Automated testing and fuzzing**: generating test cases and oracles.
- **Bug detection and program repair**: static analysis, code review, and patch generation.
- **Requirements and design**: natural-language-to-code, architecture suggestion.
- **Software verification and security**: formal methods, vulnerability detection.

## Steps

1. Collect code repositories, issue trackers, test suites, and documentation.
2. Preprocess and chunk code, add retrieval context, and build prompts.
3. Fine-tune or prompt a code model for generation, test, or repair tasks.
4. Validate generated outputs with compilers, linters, and CI tests.
5. Iterate with developer feedback and versioned benchmarks.

## Code pattern

```python
from transformers import pipeline

# Generate code from a docstring
generator = pipeline("text-generation", model="codellama/CodeLlama-7b-hf")
output = generator("def is_palindrome(s: str) -> bool:")
```

## Tuning notes

- Use retrieval and RAG for large, proprietary codebases.
- Validate generated code with compilers, linters, and test suites.
- Watch for hallucinated APIs, license issues, and security vulnerabilities.

## Verification

1. Generate tests for a set of functions and measure line/branch coverage.
2. Run a bug-localization model and compare to issue labels.
3. Review generated patches in a real pull request setting.

''',
        "references": [
            "https://link.springer.com/article/10.1007/s11432-025-4670-0",
            "https://link.springer.com/article/10.1007/s11432-025-4632-8",
            "https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1655469/full",
            "https://proceedings.mlr.press/v267/lu25f.html",
        ],
    },
    {
        "name": "ai-for-systems-engineering",
        "title": "AI for Systems Engineering",
        "description": "AI for architecting complex systems, model-based systems engineering (MBSE), requirements analysis, trade studies, and verification.",
        "devin_body": r'''## When to use

You are architecting a complex system, managing requirements, running trade studies, building MBSE models, or planning verification and validation.

## Usage

- **Model-based systems engineering (MBSE)**: SysML models and AI-augmented authoring.
- **Requirements engineering**: extraction, consistency checking, and traceability.
- **Trade studies and design-space exploration**: multi-objective optimization and digital threads.
- **Verification and validation (V&V)**: test planning, simulation-based validation, assurance cases.
- **Digital twins and digital threads**: linking lifecycle data to system models.

## Steps

1. Collect requirements, MBSE models, trade-study data, and test plans.
2. Structure data into traceable requirements and architecture elements.
3. Train a requirements/traceability/optimization model with human review.
4. Validate against system simulations and stakeholder review.
5. Maintain model provenance as the design evolves.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Cluster system requirements by topic
docs = df["requirement_text"].fillna("")
X = TfidfVectorizer(stop_words="english").fit_transform(docs)
df["cluster"] = KMeans(n_clusters=5, random_state=42, n_init="auto").fit_predict(X)
```

## Tuning notes

- Integrate AI with SysML/MBSE tools and versioned repositories.
- Use human-in-the-loop for safety-critical and mission-critical systems.
- Maintain traceability between generated artifacts and source requirements.

## Verification

1. Extract requirements from a document and measure coverage vs. a gold set.
2. Run a trade-study optimizer and compare to a baseline architecture.
3. Verify an MBSE model consistency against a set of rules.

''',
        "references": [
            "https://doi.org/10.1017/pds.2025.10058",
            "https://doi.org/10.48550/arxiv.2606.06727",
            "https://www.mdpi.com/2079-8954/13/7/584",
            "https://doi.org/10.23919/JSEE.2024.000066",
        ],
    },
    {
        "name": "ai-for-industrial-engineering",
        "title": "AI for Industrial Engineering",
        "description": "AI for production planning, scheduling, quality control, ergonomics, operations research, and process improvement.",
        "devin_body": r'''## When to use

You are optimizing production, scheduling jobs, controlling quality, balancing assembly lines, or improving supply-chain operations.

## Usage

- **Production planning and scheduling**: job-shop, flow-shop, and real-time rescheduling.
- **Quality control and SPC**: defect detection, predictive quality, and root-cause analysis.
- **Operations research and optimization**: MILP, constraint programming, and heuristics.
- **Ergonomics and human factors**: motion analysis, workload, and safety.
- **Digital lean and process mining**: bottleneck detection and value-stream analysis.

## Steps

1. Collect MES/ERP/IoT data on production, quality, maintenance, and schedules.
2. Engineer features for throughput, quality, and resource utilization.
3. Train scheduling, quality, or maintenance optimization models.
4. Validate against baseline KPIs and constraints in simulation.
5. Deploy and retrain with live production feedback.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict a quality metric from process parameters
X = df[["temperature", "pressure", "cycle_time", "operator_shift"]]
y = df["defect_rate"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Use chronological splits and respect production constraints.
- Balance throughput, quality, and energy objectives.
- Integrate AI with MES, ERP, and IoT data for real-world impact.

## Verification

1. Build a predictive quality model and compare to an SPC control chart.
2. Schedule a small job shop and compare makespan to a rule-based schedule.
3. Detect a bottleneck from process-mining event logs.

''',
        "references": [
            "https://doi.org/10.1016/j.cie.2023.109662",
            "https://doi.org/10.1016/j.cirp.2024.04.101",
            "https://dl.acm.org/doi/10.1145/3800000.3800162",
            "https://doi.org/10.46254/gc03.20250318",
        ],
    },
    {
        "name": "ai-for-environmental-engineering",
        "title": "AI for Environmental Engineering",
        "description": "AI for water and wastewater treatment, air quality, climate modeling, waste management, and environmental monitoring.",
        "devin_body": r'''## When to use

You are modeling or managing environmental systems, monitoring pollutants, optimizing treatment processes, or assessing climate and sustainability risks.

## Usage

- **Water and wastewater treatment**: process control, soft sensors, and nutrient removal.
- **Air quality and emissions**: forecasting, source apportionment, and anomaly detection.
- **Climate and hydrology**: flood, drought, and rainfall-runoff modeling.
- **Waste and circular economy**: sorting, recycling, and lifecycle optimization.
- **Environmental monitoring**: IoT, remote sensing, and digital twins.

## Steps

1. Collect sensor, satellite, regulatory, and process data for the target environmental system.
2. Engineer time- and spatially-aware features and handle missing data.
3. Train a forecasting, anomaly, or optimization model.
4. Validate against field samples and first-principles models.
5. Monitor for seasonal drift and new pollution/emission sources.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Predict water quality from sensor and weather inputs
X = df[["ph", "temperature", "conductivity", "rainfall"]]
y = df["contaminant_level"]
model = RandomForestRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Combine physics-based and data-driven models for environmental dynamics.
- Handle missing data, seasonality, and non-stationarity.
- Validate against regulatory standards and field samples.

## Verification

1. Build a water-quality forecast and check against lab measurements.
2. Detect an air-quality anomaly and correlate with emission sources.
3. Model a treatment process and compare to a first-principles simulator.

''',
        "references": [
            "https://doi.org/10.1016/j.scitotenv.2023.167705",
            "https://doi.org/10.18845/tm.v37i7.7304",
            "https://doi.org/10.54691/v0t9k322",
            "https://doi.org/10.67054/auij/.v1i1.58",
        ],
    },
    {
        "name": "ai-for-petroleum-engineering",
        "title": "AI for Petroleum Engineering",
        "description": "AI for reservoir characterization, production optimization, well placement, drilling, and digital oilfield twins.",
        "devin_body": r'''## When to use

You are characterizing reservoirs, optimizing production, planning wells, or monitoring drilling and completion operations.

## Usage

- **Reservoir characterization**: facies, porosity, and permeability prediction from logs/seismic.
- **Surrogate reservoir simulation**: deep-learning proxy models to replace expensive flow simulators.
- **Production optimization**: well control, waterflooding, and life-cycle NPV.
- **Drilling and completion**: rate-of-penetration, stuck-pipe, and well-placement risk.
- **Digital oilfield twins**: integrated asset models and real-time surveillance.

## Steps

1. Collect well logs, seismic, production history, and reservoir simulation data.
2. Build multi-fidelity datasets and define NPV/objective functions.
3. Train a surrogate, characterization, or optimization model.
4. Validate against history-matched simulation and field data.
5. Update the model as new wells and reservoir data arrive.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict oil production from well and reservoir features
X = df[["permeability", "porosity", "well_spacing", "bhp"]]
y = df["cumulative_oil"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Honor geological and multiphase physics in feature engineering.
- Use transfer learning and multi-fidelity models for sparse data.
- Validate forecasts against history-matched simulation.

## Verification

1. Build a reservoir-property prediction and compare to core measurements.
2. Train a surrogate production model and benchmark against a simulator.
3. Optimize well controls and compare NPV to a baseline strategy.

''',
        "references": [
            "https://www.sciopen.com/article/10.1016/j.petsci.2025.02.014",
            "https://www.sciencedirect.com/science/article/abs/pii/S2949891024006432",
            "https://www.earthdoc.org/content/papers/10.3997/2214-4609.202437090",
            "https://link.springer.com/article/10.1007/s13202-025-01938-4",
        ],
    },
    {
        "name": "ai-for-telecommunications",
        "title": "AI for Telecommunications",
        "description": "AI for wireless networks, 5G/6G, network optimization, traffic forecasting, security, and edge intelligence.",
        "devin_body": r'''## When to use

You are designing, optimizing, or operating telecom networks, including RAN, core, transport, or edge, and need data-driven automation.

## Usage

- **Radio access network (RAN) intelligence**: beam management, channel estimation, and resource allocation.
- **Network slicing and orchestration**: traffic prediction and dynamic slice scaling.
- **Self-organizing networks (SON)**: auto-configuration, optimization, and healing.
- **Network security and fraud detection**: anomaly detection and intrusion prevention.
- **Edge and cloud optimization**: caching, compute offloading, and energy efficiency.

## Steps

1. Collect RAN/core/edge/transport KPIs, traffic traces, and alarm logs.
2. Engineer temporal, spatial, and graph features for network state.
3. Train a forecasting, optimization, or anomaly model.
4. Validate in a network simulator or with A/B testing on live traffic.
5. Monitor SLA compliance and retrain for new services and topologies.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import IsolationForest

# Detect anomalous network KPI patterns
X = df[["throughput", "latency", "jitter", "packet_loss"]]
model = IsolationForest(contamination=0.01, random_state=42).fit(X)
df["anomaly_score"] = model.decision_function(X)
```

## Tuning notes

- Use time-series and graph models for network dynamics.
- Balance latency, throughput, and energy under SLAs.
- Validate on real network traces and edge constraints.

## Verification

1. Forecast network traffic and compare to a seasonal baseline.
2. Detect anomalous cells or users and validate against trouble tickets.
3. Optimize resource allocation in a simple network simulator.

''',
        "references": [
            "https://doi.org/10.3390/fi18030155",
            "https://doi.org/10.3390/technologies13120559",
            "https://doi.org/10.3390/app16042071",
            "https://doi.org/10.3390/sym17081279",
        ],
    },
]
