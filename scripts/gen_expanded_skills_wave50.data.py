SKILLS = [
    {
        "name": "ai-for-process-manufacturing",
        "title": "AI for Process Manufacturing",
        "description": "Builds soft sensors, optimizes recipes, and controls continuous or batch chemical and pharmaceutical processes in real time.",
        "devin_body": r'''## When to use

You are optimizing continuous or batch processes where quality is inferred from sensor trajectories, recipes must adapt to disturbances, and energy/yield trade-offs matter.

## Usage

- **Soft sensing**: predict hard-to-measure quality variables from process data using Gaussian process or neural surrogates.
- **Recipe optimization**: set initial conditions and temperature/feed profiles for batch reactors.
- **Advanced process control (APC)**: model-predictive control, real-time optimization, and constrained control.
- **Process digital twins**: build physics-informed or data-driven surrogate models of reactors and separations.
- **Batch-to-batch learning**: update models using historical batch outcomes.

## Steps

1. Collect sensor, lab, and recipe data; align timestamps to batch/phase boundaries.
2. Build a soft sensor or surrogate model for the target quality or yield.
3. Validate predictions against lab measurements on hold-out batches.
4. Use the model to optimize recipes or setpoints subject to safety constraints.
5. Deploy and monitor residuals for drift; retrain when process conditions shift.

## Code pattern

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np

# Soft sensor: predict product quality from reactor conditions
X = df[["temperature", "pressure", "agitator_speed"]].values
y = df["yield"].values
model = GaussianProcessRegressor().fit(X, y)
y_hat, sigma = model.predict(X_new, return_std=True)
```

## Tuning notes

- Align sampling and process dynamics; use time-lagged features where causality matters.
- Respect safety and hard constraints in optimization; combine ML with first-principles models.
- Handle uneven batch lengths with dynamic time warping or padded sequence models.

## Verification

1. Build a soft sensor and compare its predictions to lab measurements on a hold-out batch.
2. Optimize a recipe profile and validate against a simulator or historical best practice.
3. Monitor prediction residuals for sensor drift and retrain when process conditions shift.
''',
        "references": [
            "https://doi.org/10.1088/2632-2153/ae2382",
            "https://doi.org/10.1515/revce-2024-0060",
            "https://doi.org/10.1088/1361-6501/ad8be6",
            "https://doi.org/10.1021/acsomega.5c01274",
            "https://doi.org/10.1021/acs.iecr.0c03806",
        ],
    },
    {
        "name": "ai-for-discrete-manufacturing",
        "title": "AI for Discrete Manufacturing",
        "description": "Schedules jobs, routes work through machines, and coordinates robotic cells for assembly and machining operations.",
        "devin_body": r'''## When to use

You are making distinct parts or assembling them, and need to schedule jobs, allocate resources, plan process routes, or coordinate robotic work cells.

## Usage

- **Integrated process planning and scheduling (IPPS)**: combine operation sequencing and machine allocation.
- **Job-shop and flexible job-shop scheduling**: minimize makespan, tardiness, or energy use.
- **Robotic assembly and pick-and-place**: sequence and motion planning for SCARA, cobots, and gantries.
- **Work-in-progress tracking**: trace parts through operations using MES and RFID/barcode data.
- **Learning heuristics**: GNN/RL dispatching rules for dynamic shop floors.

## Steps

1. Collect job, machine, route, and WIP data from the MES or ERP.
2. Engineer features for operations, setups, due dates, and resource availability.
3. Build an optimization or learning-based scheduler with OR-Tools CP-SAT or Petri-net DQN.
4. Validate schedules with a discrete-event simulator against baseline rules.
5. Deploy to the shop floor and measure makespan, tardiness, and throughput.

## Code pattern

```python
from ortools.sat.python import cp_model

# Simple flexible job-shop model
model = cp_model.CpModel()
start = {(j, o): model.NewIntVar(0, horizon, f"s_{j}_{o}") for j, o in jobs_ops}
machine = {(j, o): model.NewIntVarFromDomain(domains[j, o], f"m_{j}_{o}") for j, o in jobs_ops}
model.AddNoOverlap(intervals)
solver = cp_model.CpSolver()
solver.Solve(model)
```

## Tuning notes

- Use chronological or route-constrained data splits to avoid future-information leakage.
- Balance throughput, due-date performance, and energy in the objective.
- Validate schedules with a discrete-event simulator before deployment.

## Verification

1. Solve a small job-shop and compare makespan to a greedy priority rule.
2. Train a learned dispatching policy and benchmark against shortest-processing-time.
3. Track a part through a simulated line and verify WIP accuracy against MES events.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2409.00968",
            "https://link.springer.com/article/10.1007/s10845-023-02309-8",
            "https://link.springer.com/article/10.1007/s11740-024-01306-x",
            "https://dl.acm.org/doi/10.1007/s10845-024-02423-1",
        ],
    },
    {
        "name": "ai-for-lean-manufacturing",
        "title": "AI for Lean Manufacturing",
        "description": "Quantifies waste, maps value streams, and prioritizes kaizen actions using real-time production event data.",
        "devin_body": r'''## When to use

You are running a lean transformation and need to identify muda, quantify value-added time, prioritize improvement actions, and sustain pull-based flow.

## Usage

- **Waste identification**: classify overproduction, waiting, transport, over-processing, inventory, motion, and defects.
- **Value stream mapping (VSM)**: visualize material and information flow and compute value-added ratio.
- **Process mining for lean**: discover actual flows from event logs and quantify non-value-added time.
- **Bottleneck and line balancing**: detect constraints limiting takt time and throughput.
- **Kaizen prioritization**: use Pareto, GUT matrix, and 5-Why analysis guided by data.

## Steps

1. Extract event logs, process maps, and time-study data from MES or SCADA.
2. Compute value-added, necessary non-value-added, and non-value-added time.
3. Identify the biggest wastes and bottlenecks with Pareto and flow analysis.
4. Prioritize kaizen actions and simulate their impact on lead time and WIP.
5. Track before/after metrics and update the digital value stream map.

## Code pattern

```python
import pandas as pd

# Compute value-added ratio from event log
log = pd.read_csv("production_events.csv", parse_dates=["start", "end"])
log["duration"] = (log["end"] - log["start"]).dt.total_seconds()
va_time = log.loc[log["activity_type"] == "value_added", "duration"].sum()
total_time = log["duration"].sum()
print("Value-added ratio:", va_time / total_time)
```

## Tuning notes

- Distinguish value-added from necessary non-value-added using domain definitions.
- Update VSMs with real-time data rather than static time studies.
- Tie analytics to actionable kaizen actions and track before/after metrics.

## Verification

1. Build a digital value stream map and compare lead time to the manual version.
2. Identify the top three wastes with a Pareto chart and validate with shop-floor observation.
3. Run a kaizen experiment and measure lead-time or WIP reduction.
''',
        "references": [
            "https://doi.org/10.1108/ijlss-03-2024-0059",
            "https://doi.org/10.1080/00207543.2021.1906460",
            "https://doi.org/10.3390/su16041694",
            "https://doi.org/10.1016/j.eswa.2019.01.026",
            "https://doi.org/10.3390/jmmp10030098",
        ],
    },
    {
        "name": "ai-for-six-sigma",
        "title": "AI for Six Sigma",
        "description": "Augments DMAIC projects with defect prediction, statistical process control, and designed-experiment optimization.",
        "devin_body": r'''## When to use

You are running a Six Sigma or Lean Six Sigma project and want to speed up DMAIC with machine learning for pattern detection, prediction, and prescriptive action.

## Usage

- **DMAIC augmentation**: support Define, Measure, Analyze, Improve, Control with data-driven methods.
- **Statistical process control (SPC)**: control charts, process capability (Cp/Cpk), and drift monitoring.
- **Defect prediction**: classify or regress defect risk from process parameters.
- **Design of experiments (DOE)**: optimize factor settings with fewer experimental runs.
- **XAI for Six Sigma**: use SHAP and LIME for interpretable cause prioritization.

## Steps

1. Define the problem, CTQ, and project scope with stakeholders.
2. Measure process performance and collect historical defect and parameter data.
3. Analyze data with SPC, capability analysis, and ML defect-prediction models such as Random Forest or CART.
4. Improve by optimizing process settings and piloting changes.
5. Control with monitoring dashboards and retrain models as conditions change.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Predict defect probability during the Analyze/Improve phase
X = df[["feed_rate", "spindle_speed", "coolant_flow", "ambient_temp"]]
y = df["defective"]
model = GradientBoostingClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Use phase-appropriate models and metrics; control charts need stability, not just accuracy.
- Avoid data leakage from future inspections into the Measure/Analyze data.
- Combine statistical rigor with ML; validate predictions against designed experiments.

## Verification

1. Build a defect-prediction model and compare precision/recall to the current SPC rules.
2. Compute Cpk before and after an improvement and confirm it meets the target.
3. Use SHAP values to rank root causes and validate with a fishbone session.
''',
        "references": [
            "https://doi.org/10.1109/tem.2023.3335237",
            "https://doi.org/10.1109/tem.2023.3324542",
            "https://doi.org/10.1109/tem.2025.3634836",
            "https://doi.org/10.1109/access.2021.3103931",
            "https://www.isixsigma.com/artificial-intelligence/how-ai-can-be-used-in-the-dmaic-process/",
        ],
    },
    {
        "name": "ai-for-total-productive-maintenance",
        "title": "AI for Total Productive Maintenance",
        "description": "Predicts equipment failures, supports autonomous maintenance, and improves OEE across the eight TPM pillars.",
        "devin_body": r'''## When to use

You are implementing Total Productive Maintenance and want to use AI to improve OEE, eliminate breakdowns, and empower operators to maintain equipment autonomously.

## Usage

- **Eight TPM pillars**: support autonomous, planned, quality, focused, early-equipment, training, safety, and office TPM.
- **OEE analytics**: measure and improve Availability x Performance x Quality.
- **Condition-based maintenance (CBM)**: monitor vibration, temperature, current, oil, and acoustics.
- **Autonomous maintenance**: enable operators to clean, inspect, and lubricate with AI-guided diagnostics.
- **Kaizen for equipment**: drive small, data-driven improvements to reduce minor stops and defects.

## Steps

1. Collect sensor, work-order, and OEE data for critical equipment.
2. Engineer condition indicators and OEE-loss labels from historical failures.
3. Train CBM and failure-risk models to prioritize maintenance actions.
4. Integrate alerts into operator rounds and maintenance planning systems.
5. Track OEE, MTBF, MTTR, and false-alarm rate to validate impact.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Predict unplanned downtime from sensor features
X = df[["vibration_rms", "temperature", "motor_current", "cycle_count"]]
y = df["failure_next_24h"]
model = RandomForestClassifier(class_weight="balanced", random_state=42).fit(X, y)
```

## Tuning notes

- Balance recall for failure risk with false-alarm rate to avoid alert fatigue.
- Use OEE loss history to label maintenance priority, not just binary failure.
- Integrate operator annotations; domain knowledge is critical for the Autonomous Maintenance pillar.

## Verification

1. Train a failure-prediction model and measure lead time to the next breakdown.
2. Compare OEE before and after a pilot on one line or cell.
3. Verify that alerts lead to operator actions and track mean time to repair (MTTR).
''',
        "references": [
            "https://doi.org/10.1016/j.eswa.2024.126283",
            "https://doi.org/10.1016/j.cie.2021.107267",
            "https://doi.org/10.3390/app11156953",
            "https://doi.org/10.1108/jqme-07-2022-0041",
            "https://hal.science/hal-05001680",
        ],
    },
    {
        "name": "ai-for-root-cause-analysis",
        "title": "AI for Root Cause Analysis",
        "description": "Traces faults to originating causes using causal discovery, knowledge graphs, and SHAP-based diagnostics.",
        "devin_body": r'''## When to use

A quality, safety, or equipment failure has occurred and you need to trace it to the originating cause, not just its symptoms, across interacting processes and machines.

## Usage

- **5-Why and fishbone**: structured qualitative root-cause exploration.
- **Causal discovery**: learn causal graphs from time-series or tabular data with PC, GES, or NOTEARS.
- **Knowledge graphs**: model equipment, materials, recipes, and fault propagation.
- **Graph neural networks**: propagate fault evidence and rank root-cause variables.
- **SHAP and counterfactuals**: attribute defect or failure to specific sensors and settings.

## Steps

1. Gather event logs, sensor data, and failure records for the incident window.
2. Build a knowledge graph of equipment, materials, and process dependencies.
3. Run causal discovery with DoWhy or DirectLiNGAM, or train an attribution model to score suspect variables.
4. Cross-check the top candidates with domain experts and known incidents.
5. Document the validated root cause and prescribe corrective actions.

## Code pattern

```python
from shap import TreeExplainer
import xgboost as xgb

# Train a defect model and explain predictions
X = df.drop("defect", axis=1)
y = df["defect"]
model = xgb.XGBClassifier().fit(X, y)
explainer = TreeExplainer(model)
shap_values = explainer.shap_values(X.iloc[:100])
```

## Tuning notes

- Separate common-cause correlation from true causal links with interventional data or expert priors.
- Build knowledge graphs from P&IDs, asset hierarchies, and BOMs to ground reasoning.
- Validate root-cause rankings against known historical incidents and domain expertise.

## Verification

1. Identify the root cause of a historical defect and compare the AI ranking to the manual RCA.
2. Build a causal graph and verify a key edge with a controlled experiment or do-calculus.
3. Use SHAP to show that the top feature is actionable, not just a downstream symptom.
''',
        "references": [
            "https://doi.org/10.1109/jsen.2025.3649083",
            "https://doi.org/10.1109/raai67517.2025.11423096",
            "https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=1633&context=aii_fac_pub",
            "https://dl.acm.org/doi/10.1016/j.engappai.2025.110152",
            "https://www.sciencedirect.com/science/article/abs/pii/S147403462600100X",
        ],
    },
    {
        "name": "ai-for-defect-detection",
        "title": "AI for Defect Detection",
        "description": "Detects surface, assembly, and component defects with computer vision and anomaly segmentation.",
        "devin_body": r'''## When to use

You need to replace or augment manual inspection by automatically detecting scratches, dents, contamination, missing components, or dimensional deviations in production.

## Usage

- **Supervised defect classification**: CNNs and vision transformers trained on labeled defect images.
- **Anomaly detection**: train on good samples and flag deviations with autoencoders, feature distance, or PatchCore.
- **Segmentation**: pixel-level defect localization for repair or scrap decisions.
- **Semi-supervised and few-shot learning**: reduce labeling cost with synthetic or weak labels, or with foundation models such as CLIP and Amazon Nova Pro.
- **Edge deployment**: run inspection models on factory cameras or PLC vision systems.

## Steps

1. Collect and label defect and nominal images from production.
2. Choose a supervised, anomaly, or segmentation approach based on label availability.
3. Train and validate the model with appropriate metrics for false-accept and false-reject.
4. Optimize latency and deploy on the target camera or edge device.
5. Monitor performance and retrain when new defect modes appear.

## Code pattern

```python
from anomalib.models import Patchcore
from anomalib.data import MVTec

# Train an anomaly detector on nominal images
model = Patchcore(backbone="wide_resnet_50_2")
datamodule = MVTec(category="bottle")
```

## Tuning notes

- Balance false-accept and false-reject rates based on downstream cost.
- Use augmentations, synthetic defects, and domain randomization to improve generalization.
- Calibrate on real production samples; lab images may not match lighting and texture.

## Verification

1. Train a defect classifier and report precision/recall on a held-out production set.
2. Compare an anomaly model to a supervised baseline when labels are scarce.
3. Measure inference latency on the target camera or edge device.
''',
        "references": [
            "https://www.mdpi.com/2076-3417/14/15/6774",
            "https://link.springer.com/article/10.1007/s10845-025-02680-8",
            "https://www.nature.com/articles/s41598-026-54269-7",
            "https://www.mdpi.com/1424-8220/26/4/1085",
            "https://www.sciencedirect.com/science/article/abs/pii/S0957417426002277",
        ],
    },
    {
        "name": "ai-for-predictive-quality",
        "title": "AI for Predictive Quality",
        "description": "Forecasts final part quality from in-process sensor data to enable early rework, scrap, or recipe adjustment.",
        "devin_body": r'''## When to use

You want to predict whether a part or batch will meet quality specifications while it is still in process, enabling early rework, scrap, or process adjustment.

## Usage

- **Virtual metrology (VM)**: estimate wafer or part properties from process sensor data without physical measurement.
- **In-situ quality prediction**: use tool-level data to forecast dimensional, mechanical, or electrical outcomes.
- **Causal quality models**: identify which process parameters causally drive quality variation.
- **Transfer learning**: adapt a quality model across recipes, tools, or factories.
- **Online updating**: refresh models with new metrology samples to handle drift.

## Steps

1. Collect tool sensor data and corresponding quality metrology aligned by part/batch.
2. Build a regression or classification model for the target quality characteristic.
3. Validate predictions on hold-out wafers or parts using time-aware splits.
4. Use feature attribution or causal analysis to identify controllable drivers.
5. Deploy inline and update the model as recipes or tools change.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingRegressor

# In-process quality prediction from tool sensor features
X = df[["power", "pressure", "duration", "gas_flow", "chuck_temp"]]
y = df["critical_dimension"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Ensure sensor data are sampled before the quality measurement to avoid target leakage.
- Use physics-aware features and recipe context to improve generalization.
- Track model drift as tools, consumables, and recipes change; retrain with active learning.

## Verification

1. Build a virtual metrology model and compare RMSE to actual metrology on hold-out wafers.
2. Predict scrap vs. good parts before final test and measure early rejection accuracy.
3. Validate causal drivers through a designed experiment or sensitivity analysis.
''',
        "references": [
            "https://iopscience.iop.org/article/10.1088/1361-6501/adb05a",
            "https://link.springer.com/article/10.1007/s40962-025-01702-8",
            "https://www.mdpi.com/2227-9717/10/10/1966",
            "https://www.mdpi.com/2227-9717/13/4/962",
            "https://doi.org/10.1109/tsm.2017.2787550",
        ],
    },
    {
        "name": "ai-for-digital-manufacturing",
        "title": "AI for Digital Manufacturing",
        "description": "Builds digital twins, validates control logic through virtual commissioning, and synchronizes real-time factory data.",
        "devin_body": r'''## When to use

You are building a digital replica of a product, process, or factory to simulate behavior, commission systems virtually, and make real-time decisions from integrated data.

## Usage

- **Digital twin hierarchy**: build component, machine, cell, shop-floor, and enterprise twins.
- **Virtual commissioning**: validate PLC code and robot programs in simulation before deployment.
- **Real-time synchronization**: keep the twin aligned with physical assets through IoT and MES.
- **Simulation and optimization**: use discrete-event, agent-based, and physics-based co-simulation.
- **OpenUSD and interoperability**: share 3D and behavioral models across tools.

## Steps

1. Model the assets, processes, and data sources in the digital twin.
2. Connect the twin to live IoT/MES data for real-time synchronization.
3. Calibrate the model against real equipment behavior under steady-state and transients.
4. Run what-if scenarios for scheduling, maintenance, and control logic.
5. Deploy validated decisions back to the physical system and measure KPIs.

## Code pattern

```python
import simpy

# Simple discrete-event model of a production line
env = simpy.Environment()
machine = simpy.Resource(env, capacity=1)

def part(env, name, machine, processing_time):
    with machine.request() as req:
        yield req
        yield env.timeout(processing_time)

env.process(part(env, "p1", machine, 2.5))
env.run(until=20)
```

## Tuning notes

- Validate the twin against real equipment behavior under steady-state and transient conditions.
- Use the twin to stress-test schedules, maintenance policies, and control logic safely.
- Keep model fidelity appropriate for the decision; not every twin needs full physics.

## Verification

1. Compare a digital twin's throughput prediction to actual production over one week.
2. Virtual-commission a new control sequence and confirm it runs on the real PLC.
3. Use the twin to optimize a schedule and measure KPI improvement on the shop floor.
''',
        "references": [
            "https://www.mdpi.com/1424-8220/26/1/124",
            "https://www.mdpi.com/1424-8220/21/19/6340",
            "https://www.mdpi.com/2079-9292/14/4/646",
            "https://link.springer.com/article/10.1007/s40684-025-00750-z",
            "https://www.mdpi.com/2504-4494/9/7/211",
        ],
    },
    {
        "name": "ai-for-factory-automation",
        "title": "AI for Factory Automation",
        "description": "Runs ML inference on PLCs, edge devices, and robot controllers for low-latency motion and quality control.",
        "devin_body": r'''## When to use

You are deploying AI directly into automation systems: PLCs, edge devices, robot controllers, and SCADA to make control decisions with low latency and high reliability.

## Usage

- **PLC-based ML**: execute regression, classification, or neural networks on IEC 61131-3 controllers.
- **Industrial edge computing**: run ONNX or TensorFlow Lite models close to sensors and actuators.
- **AI motion control**: use reinforcement learning for path planning, positioning, and energy/force optimization.
- **OPC UA and MQTT**: standard protocols for real-time data exchange between controllers and AI.
- **Safety and determinism**: respect real-time cycles, guard limits, and fail-safe behavior.

## Steps

1. Profile latency, memory, and cycle-time constraints of the target controller.
2. Select and quantize a model suitable for PLC or edge execution.
3. Implement data exchange through OPC UA, MQTT, or shared memory.
4. Validate control behavior in simulation and with safe operating limits.
5. Deploy, monitor inference latency, and log all AI-driven actions.

## Code pattern

```python
import onnxruntime as ort

# Run an ONNX model on an industrial edge device
session = ort.InferenceSession("defect_classifier.onnx", providers=["CPUExecutionProvider"])
input_name = session.get_inputs()[0].name
outputs = session.run(None, {input_name: image_batch})
```

## Tuning notes

- Quantize and prune models to meet PLC or edge latency and memory budgets.
- Co-ordinate inference with control scan cycles; output jitter can destabilize control.
- Keep human oversight for safety-critical decisions and log all AI-driven actions.

## Verification

1. Deploy a lightweight model on a PLC or edge gateway and measure inference latency.
2. Compare an AI-optimized motion profile to a classical controller on cycle time and energy.
3. Test fail-safe behavior when the AI model returns an out-of-distribution prediction.
''',
        "references": [
            "https://doi.org/10.1109/ETFA61755.2024.10710938",
            "https://www.mdpi.com/1424-8220/24/3/843",
            "https://doi.org/10.1007/978-3-030-99108-1_34",
            "https://doi.org/10.3390/computers13070172",
            "https://www.mdpi.com/2075-1702/13/12/1140",
        ],
    },
    {
        "name": "ai-for-industrial-iot",
        "title": "AI for Industrial IoT",
        "description": "Connects machines, sensors, and actuators over edge-fog-cloud architectures for real-time monitoring and predictive maintenance.",
        "devin_body": r'''## When to use

You are connecting machines, sensors, and actuators across a plant or supply chain and need scalable, low-latency data pipelines for AI-driven operations.

## Usage

- **IIoT architecture**: design sensor, edge gateway, fog node, cloud, and digital thread layers.
- **Protocols**: use OPC UA, MQTT, Modbus, DDS, and Time-Sensitive Networking.
- **Edge AI and TinyML**: process data locally to reduce bandwidth and latency.
- **Time-series and streaming analytics**: use Kafka, InfluxDB, and anomaly detection on streams.
- **Security and data sovereignty**: implement encryption, device identity, and on-premise inference.

## Steps

1. Define the asset model, data sources, and latency/privacy requirements.
2. Deploy sensors, gateways, and a message broker or historian.
3. Ingest and time-align telemetry; build a streaming or batch analytics pipeline.
4. Train and deploy edge or cloud ML models for monitoring and prediction.
5. Secure devices, manage OTA updates, and monitor end-to-end data quality.

## Code pattern

```python
import paho.mqtt.client as mqtt
import json

# Subscribe to a machine telemetry topic
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    # stream into InfluxDB or run anomaly detector
    print(payload)

client = mqtt.Client()
client.on_message = on_message
client.connect("edge-broker.local")
client.subscribe("factory/line1/press/telemetry")
client.loop_forever()
```

## Tuning notes

- Choose edge vs. cloud based on latency, bandwidth, and privacy requirements.
- Handle missing, delayed, and out-of-sequence sensor messages with robust buffering.
- Plan device management, OTA updates, and model versioning from the start.

## Verification

1. Ingest telemetry from at least one machine and verify end-to-end latency.
2. Deploy an edge anomaly detector and compare its recall to a cloud-based model.
3. Test security by validating device certificates and encrypted transport.
''',
        "references": [
            "https://doi.org/10.1109/jsyst.2022.3193200",
            "https://dl.acm.org/doi/10.1145/3732287",
            "https://doi.org/10.3390/s25247636",
            "https://www.mdpi.com/1424-8220/24/24/7918",
            "https://ieeexplore.ieee.org/document/9784867",
        ],
    },
    {
        "name": "ai-for-manufacturing-analytics",
        "title": "AI for Manufacturing Analytics",
        "description": "Turns MES and ERP data into OEE dashboards and predictive KPIs for prescriptive manufacturing decisions.",
        "devin_body": r'''## When to use

You need to turn MES, ERP, quality, and maintenance data into actionable performance insights, from historical dashboards to predictive and prescriptive recommendations.

## Usage

- **Manufacturing KPIs**: track OEE, OLE, MTBF, MTTR, scrap rate, first-pass yield, and takt time.
- **Descriptive analytics**: build dashboards, Pareto charts, loss analysis, and trend reports.
- **Diagnostic analytics**: drill down into downtime, defect, and bottleneck causes.
- **Predictive and prescriptive**: forecast KPIs, simulate interventions, and recommend actions.
- **Association rule mining**: discover co-occurring conditions that drive losses.

## Steps

1. Integrate MES, ERP, quality, and maintenance data into a clean data model.
2. Define and compute consistent KPIs across shifts, lines, and plants.
3. Build dashboards and diagnostic views to find top losses and trends.
4. Train predictive models for KPIs and generate prescriptive recommendations.
5. Pilot recommendations, measure impact, and iterate.

## Code pattern

```python
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Find frequent patterns in downtime events
basket = pd.get_dummies(df[["machine", "shift", "downtime_category"]])
frequent = apriori(basket, min_support=0.05, use_colnames=True)
rules = association_rules(frequent, metric="lift", min_threshold=1.5)
```

## Tuning notes

- Define KPIs consistently across shifts, lines, and plants before modeling.
- Combine OEE with cost and sustainability metrics for a balanced view.
- Use controlled pilots to validate prescriptive recommendations before scaling.

## Verification

1. Build an OEE dashboard and reconcile it with manual production reports.
2. Predict next-week OEE and compare to a naive baseline.
3. Implement a prescriptive recommendation and measure actual KPI improvement.
''',
        "references": [
            "https://doi.org/10.1108/ijqrm-01-2023-0012",
            "https://www.mdpi.com/2504-2289/7/3/138",
            "https://www.mdpi.com/2504-4494/6/3/59",
            "https://doi.org/10.2478/scjme-2024-0026",
        ],
    },
]
