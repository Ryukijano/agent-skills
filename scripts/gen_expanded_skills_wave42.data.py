SKILLS = [
    {
        "name": "ai-for-civil-engineering",
        "title": "AI for Civil Engineering",
        "description": "Build predictive models for civil infrastructure, natural hazards, and water resources.",
        "devin_body": r'''## When to use

You are designing, monitoring, or maintaining civil infrastructure such as bridges, buildings, dams, roads, or water systems and want data-driven predictions or inspections.

## Usage

- Monitor bridges and dams with vibration, strain, and drone-vision sensors.
- Predict soil liquefaction and slope stability from geotechnical logs.
- Forecast traffic flow and incidents using loop-detector and GPS data.
- Model flood risk and water quality with SWAT and HEC-RAS.
- Create digital twins of assets in Autodesk Revit/Navisworks.

## Steps

1. Collect structural, geotechnical, traffic, or water data and define the prediction target.
2. Engineer features from vibration spectra, image patches, or sensor time series.
3. Train and validate models with time-aware or site-aware splits.
4. Integrate predictions with BIM, GIS, or digital-twin dashboards.
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
        "references": ["https://doi.org/10.3390/app151910499", "https://doi.org/10.1016/j.kscej.2025.100203", "https://link.springer.com/article/10.1007/s41872-025-00364-z", "https://www.frontiersin.org/journals/built-environment/articles/10.3389/fbuil.2022.1007886/full"],
    },
    {
        "name": "ai-for-mechanical-engineering",
        "title": "AI for Mechanical Engineering",
        "description": "Apply AI to design, maintenance, and manufacturing optimization.",
        "devin_body": r'''## When to use

You are designing mechanical components or systems, monitoring rotating machinery, optimizing maintenance, or simulating dynamics and controls.

## Usage

- Predict bearing, gear, and motor failures from vibration and thermal data.
- Optimize topology and generative designs in nTopology or Fusion 360.
- Build reduced-order models from CFD/FEA simulations.
- Monitor equipment health with digital twins (Azure Digital Twins).
- Improve quality control with machine vision on production lines.

## Steps

1. Collect operational sensor data and define failure or quality targets.
2. Extract frequency-domain features and degradation indicators.
3. Train survival, classification, or anomaly models.
4. Deploy in edge or MES systems with real-time feedback.
5. Validate with A/B shutdown/quality outcomes and retrain.

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
        "references": ["https://doi.org/10.1016/j.jmsy.2023.10.010", "https://doi.org/10.1016/j.jmsy.2025.07.006", "https://www.nature.com/articles/s41598-024-63990-0", "https://link.springer.com/article/10.1007/s40684-025-00750-z"],
    },
    {
        "name": "ai-for-electrical-engineering",
        "title": "AI for Electrical Engineering",
        "description": "Use AI for power-system forecasting, fault detection, and smart-grid control.",
        "devin_body": r'''## When to use

You are analyzing or operating power systems, smart grids, renewable plants, or power electronics and need accurate detection, forecasting, or control.

## Usage

- Forecast renewable generation and EV load in GridLAB-D or PyPSA.
- Detect transmission-line faults and power-quality anomalies.
- Optimize microgrid dispatch and battery scheduling.
- Automate circuit sizing and PCB design checks.
- Identify transformer or inverter degradation.

## Steps

1. Ingest SCADA, AMI, or PMU time series and weather data.
2. Engineer features for load, generation, and voltage stability.
3. Train forecasting, classification, or control models.
4. Integrate with EMS/DMS or digital-twin platforms.
5. Validate against grid codes and continuously retrain.

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
        "references": ["https://www.mdpi.com/1996-1073/18/18/4983", "https://www.mdpi.com/2227-9717/13/1/48", "https://doi.org/10.1016/j.rineng.2024.103884", "https://www.frontiersin.org/journals/smart-grids/articles/10.3389/frsgr.2024.1371153/full"],
    },
    {
        "name": "ai-for-chemical-engineering",
        "title": "AI for Chemical Engineering",
        "description": "Apply AI to chemical process modeling, yield optimization, and reactor control.",
        "devin_body": r'''## When to use

You are designing or operating chemical processes, building surrogate models of reactors or separations, or automating process control.

## Usage

- Predict product quality from spectroscopic or chromatographic data.
- Optimize reactor conditions with Aspen Plus or gPROMS integrations.
- Detect process drift and abnormal events in DCS historians.
- Design molecules and formulations with generative models.
- Forecast energy and raw-material demand.

## Steps

1. Collect batch/continuous process data and lab assay labels.
2. Align sensor and laboratory timestamps into feature matrices.
3. Train regression or time-series models for quality or yield.
4. Deploy predictions to APC/MES or via Python API.
5. Track model drift against lab reference and retrain.

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
        "references": ["https://doi.org/10.1002/cjce.70032", "https://www.mdpi.com/2227-9717/11/2/330", "https://doi.org/10.1002/cjce.24246", "https://doi.org/10.48550/arxiv.2412.18529"],
    },
    {
        "name": "ai-for-aerospace-engineering",
        "title": "AI for Aerospace Engineering",
        "description": "Use AI for flight-dynamics prediction, structural-health monitoring, and mission planning.",
        "devin_body": r'''## When to use

You are designing aircraft or spacecraft, building reduced-order models, optimizing aerodynamic/structural/propulsion systems, or certifying aerospace engineering decisions.

## Usage

- Detect aircraft engine anomalies and predict remaining useful life.
- Model aerodynamic loads and flutter from wind-tunnel or flight data.
- Plan UAV routes and swarm coordination.
- Monitor composite structures with guided-wave or image sensors.
- Support trajectory optimization and air-traffic predictions.

## Steps

1. Collect flight, vibration, or structural sensor data.
2. Build physics-informed or data-driven flight/structural models.
3. Train anomaly detection and RUL estimators.
4. Integrate with maintenance planning or GCS dashboards.
5. Validate against flight-test or simulated benchmarks.

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
        "references": ["https://doi.org/10.1016/j.paerosci.2022.100849", "https://journals.sagepub.com/doi/10.1177/0954410019864485", "https://doi.org/10.1016/j.oceaneng.2024.119263", "https://www.ccs.upm.es/research/publications/a-review-of-surrogate-modeling-techniques-for-aerodynamic-analysis-and-optimization-current-limitations-and-future-challenges-in-industry/"],
    },
    {
        "name": "ai-for-biomedical-engineering",
        "title": "AI for Biomedical Engineering",
        "description": "Apply AI to medical imaging, biosignal monitoring, and medical-device design.",
        "devin_body": r'''## When to use

You are developing wearable or implantable devices, analyzing biosignals, designing medical imaging classifiers, or modeling biomechanical systems.

## Usage

- Segment lesions or organs in MRI/CT with MONAI or nnU-Net.
- Classify ECG/EEG arrhythmias and sleep stages.
- Predict glucose or sepsis risk from wearable streams.
- Optimize prosthetics and implants via generative design.
- Monitor ICU devices and detect alarm fatigue patterns.

## Steps

1. Collect imaging, waveform, or wearable data with ethics approval.
2. Preprocess and annotate using clinical tools (3D Slicer, XNAT).
3. Train CNN or time-series classifiers with cross-site validation.
4. Deploy in PACS, edge devices, or clinical decision support.
5. Validate against clinician labels and track performance.

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
        "references": ["https://doi.org/10.3390/bios15070410", "https://doi.org/10.3390/jpm14020203", "https://doi.org/10.1039/D5MH00451A", "https://doi.org/10.3390/bios14040183"],
    },
    {
        "name": "ai-for-software-engineering",
        "title": "AI for Software Engineering",
        "description": "Use AI to generate, review, and test code across the software lifecycle.",
        "devin_body": r'''## When to use

You are building, maintaining, or reviewing software and want to use AI to generate, test, debug, or document code.

## Usage

- Complete and refactor code with GitHub Copilot or Cody.
- Run static analysis with SonarQube and ESLint.
- Generate unit tests and property-based checks.
- Predict bug-prone files and triage CI failures.
- Summarize code and documentation with LLMs.

## Steps

1. Index repositories and set up code-quality baselines.
2. Fine-tune or prompt LLMs on internal style and APIs.
3. Automate generation, review, and test coverage checks in CI.
4. Track bug-proneness and build-failure trends.
5. Measure impact on cycle time and defect escape rate.

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
        "references": ["https://link.springer.com/article/10.1007/s11432-025-4670-0", "https://link.springer.com/article/10.1007/s11432-025-4632-8", "https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1655469/full", "https://proceedings.mlr.press/v267/lu25f.html"],
    },
    {
        "name": "ai-for-systems-engineering",
        "title": "AI for Systems Engineering",
        "description": "Apply AI to requirements, MBSE, and system reliability verification.",
        "devin_body": r'''## When to use

You are architecting a complex system, managing requirements, running trade studies, building MBSE models, or planning verification and validation.

## Usage

- Parse requirements with NLP and flag inconsistencies.
- Build SysML/MBSE models in Cameo/MagicDraw with AI assist.
- Predict reliability and failure modes from digital threads.
- Optimize system architectures with multi-objective search.
- Verify and validate designs through simulation and digital twins.

## Steps

1. Elicit and structure requirements in DOORS or Jama.
2. Build or import SysML/UML models and system digital threads.
3. Train NLP or simulation models for risk and V&V.
4. Integrate predictions into MBSE and PLM workflows.
5. Update models as requirements and architectures evolve.

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
        "references": ["https://doi.org/10.1017/pds.2025.10058", "https://doi.org/10.48550/arxiv.2606.06727", "https://www.mdpi.com/2079-8954/13/7/584", "https://doi.org/10.23919/JSEE.2024.000066"],
    },
    {
        "name": "ai-for-industrial-engineering",
        "title": "AI for Industrial Engineering",
        "description": "Use AI to optimize production scheduling, quality control, and supply chains.",
        "devin_body": r'''## When to use

You are optimizing production, scheduling jobs, controlling quality, balancing assembly lines, or improving supply-chain operations.

## Usage

- Predict job-shop bottlenecks and optimize schedules with OR-Tools.
- Detect process mining patterns and inefficiencies (ProM, Celonis).
- Forecast demand and inventory levels across the supply chain.
- Predict defect risk in manufacturing with SPC and vision.
- Optimize workstation ergonomics and labor allocation.

## Steps

1. Map the production process and data sources (ERP, MES, IoT).
2. Extract features for throughput, quality, and resource utilization.
3. Train scheduling, forecasting, or classification models.
4. Deploy into APS, MES, or planning dashboards.
5. Measure KPIs and retrain on new production runs.

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
        "references": ["https://doi.org/10.1016/j.cie.2023.109662", "https://doi.org/10.1016/j.cirp.2024.04.101", "https://dl.acm.org/doi/10.1145/3800000.3800162", "https://doi.org/10.46254/gc03.20250318"],
    },
    {
        "name": "ai-for-environmental-engineering",
        "title": "AI for Environmental Engineering",
        "description": "Use AI to monitor air and water quality, model ecosystems, and manage environmental risk.",
        "devin_body": r'''## When to use

You are modeling or managing environmental systems, monitoring pollutants, optimizing treatment processes, or assessing climate and sustainability risks.

## Usage

- Predict pollutant levels from sensor and satellite data.
- Model watershed and flood dynamics with SWAT and HEC-RAS.
- Detect illegal dumping and land-use change from imagery.
- Optimize wastewater treatment and energy recovery.
- Map carbon and biodiversity hotspots.

## Steps

1. Gather environmental sensor, satellite, or survey data.
2. Engineer spatiotemporal and meteorological features.
3. Train regression or classification models for quality or risk.
4. Integrate with GIS and EHS dashboards.
5. Validate against regulatory standards and field samples.

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
        "references": ["https://doi.org/10.1016/j.scitotenv.2023.167705", "https://doi.org/10.18845/tm.v37i7.7304", "https://doi.org/10.54691/v0t9k322", "https://doi.org/10.67054/auij/.v1i1.58"],
    },
    {
        "name": "ai-for-petroleum-engineering",
        "title": "AI for Petroleum Engineering",
        "description": "Apply AI to reservoir characterization, production optimization, and predictive maintenance.",
        "devin_body": r'''## When to use

You are characterizing reservoirs, optimizing production, planning wells, or monitoring drilling and completion operations.

## Usage

- Predict reservoir properties from well logs and seismic.
- Optimize well spacing and hydraulic-fracture design.
- Detect kicks, stuck pipe, and equipment failures.
- Forecast production and decline curves.
- Model CO2 storage and enhanced oil recovery.

## Steps

1. Collect well logs, seismic, and production time series.
2. Build geostatistical and physics-informed features.
3. Train regression and time-series forecasting models.
4. Integrate with reservoir simulation or SCADA.
5. Validate with decline-curve analysis and field trials.

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
        "references": ["https://www.sciopen.com/article/10.1016/j.petsci.2025.02.014", "https://www.sciencedirect.com/science/article/abs/pii/S2949891024006432", "https://www.earthdoc.org/content/papers/10.3997/2214-4609.202437090", "https://link.springer.com/article/10.1007/s13202-025-01938-4"],
    },
    {
        "name": "ai-for-telecommunications",
        "title": "AI for Telecommunications",
        "description": "Use AI to optimize 5G and 6G RAN, network slicing, and self-organizing networks.",
        "devin_body": r'''## When to use

You are designing, optimizing, or operating telecom networks, including RAN, core, transport, or edge, and need data-driven automation.

## Usage

- Predict RAN congestion and optimize beam management.
- Automate network slicing and resource allocation with O-RAN.
- Detect fraud and anomalies in CDRs and traffic.
- Optimize cell handover and coverage with SON.
- Model customer churn and QoE from probes and CRM.

## Steps

1. Collect CDR, PM/FM, and geospatial network data.
2. Engineer KPI and traffic features across cells and slices.
3. Train forecasting, classification, or RL models.
4. Deploy via O-RAN RIC xApps or AIOps platforms.
5. Validate with network KPIs and drive-test data.

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
        "references": ["https://doi.org/10.3390/fi18030155", "https://doi.org/10.3390/technologies13120559", "https://doi.org/10.3390/app16042071", "https://doi.org/10.3390/sym17081279"],
    },
]