SKILLS = [
    {
        "name": "ai-for-aerospace",
        "title": "AI for Aerospace",
        "description": 'Use machine learning to design aircraft and spacecraft, optimize aerodynamics, monitor structural health, and certify safety-critical aerospace systems.',
        "devin_body": r'''## When to use

You are designing aircraft or spacecraft, analyzing flight/structural data, building digital twins, or certifying ML for safety-critical aerospace applications.

## Usage

- Build surrogate and reduced-order models for aerodynamic and structural analysis.
- Detect damage and predict remaining useful life from vibration, acoustic, and strain data.
- Forecast power, thermal, and telemetry anomalies for satellites and missions.
- Document certification evidence and uncertainty for airborne AI.

## Steps

1. Collect flight, structural, or telemetry data with physics-informed preprocessing.
2. Train a surrogate or anomaly detector with safety-critical validation splits.
3. Compare the model to high-fidelity CFD, FEM, or flight-test baselines.
4. Quantify uncertainty and trace data provenance for certification.
5. Deploy with human-in-the-loop overrides and continuous monitoring.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import IsolationForest

# Aerospace vibration feature matrix for SHM
X = np.load("aircraft_vibration_features.npy")
model = IsolationForest(contamination=0.02, random_state=42).fit(X)
anomaly_scores = model.decision_function(X)
```

## Tuning notes

- Aerospace data is safety-critical and often scarce; use physics-informed or hybrid modeling.
- Validate against high-fidelity simulations and flight test data.
- Track certification evidence (dataset provenance, test coverage, uncertainty estimates).

## Verification

1. Train an SHM anomaly detector on a benchmark aircraft vibration dataset.
2. Build a surrogate model for an airfoil lift curve and compare to CFD.
3. Demonstrate uncertainty quantification on a flight-relevant prediction.
''',
        "references": [
            "https://arc.aiaa.org/doi/10.2514/1.J060131",
            "https://doi.org/10.1016/j.ast.2023.108354",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12526691/",
            "https://doi.org/10.3389/fpace.2024.1475139",
        ],
    },
    {
        "name": "ai-for-aviation",
        "title": "AI for Aviation",
        "description": 'Use machine learning to predict component failures, optimize flight operations, recover from disruptions, and improve fleet reliability in aviation.',
        "devin_body": r'''## When to use

You are optimizing airline operations, forecasting aircraft component failures, recovering from schedule disruptions, or improving fleet reliability.

## Usage

- Predict remaining useful life from engine and component sensor data.
- Optimize fuel burn, crew rostering, turnaround, and delay recovery.
- Consolidate in-flight and maintenance data for fleet-health dashboards.
- Classify safety incidents and predict unscheduled maintenance.

## Steps

1. Ingest time-series sensor and maintenance logs with chronological train/test splits.
2. Engineer degradation features and handle censoring and class imbalance.
3. Train a survival, regression, or classification model for RUL or failure risk.
4. Validate predictions against actual failure events and false-positive rates.
5. Integrate the model into maintenance planning and disruption-recovery workflows.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Predict remaining useful life from engine sensors
X = pd.read_csv("engine_sensor_data.csv")
y = pd.read_csv("rul_labels.csv")["RUL"]
model = RandomForestRegressor(n_estimators=200).fit(X, y)
```

## Tuning notes

- Use chronological splits to avoid leakage from future maintenance records.
- Engine data is noisy and high-dimensional; prefer gradient boosting or LSTM for sequential patterns.
- Calibrate RUL predictions and validate against true failure events.

## Verification

1. Train a PdM model on a public aviation turbofan dataset and evaluate RUL RMSE.
2. Predict unscheduled maintenance events from fleet-level historical data.
3. Build a simple disruption-recovery dashboard for a simulated airline schedule.
''',
        "references": [
            "https://doi.org/10.3390/app16073381",
            "https://doi.org/10.1049/dgt2.70029",
            "https://www.aircraft.airbus.com/en/services/enhance/skywise-digital-solutions/skywise-fleet-performance",
            "https://doi.org/10.1007/s13272-025-00818-1",
        ],
    },
    {
        "name": "ai-for-maritime",
        "title": "AI for Maritime",
        "description": 'Use machine learning to route vessels autonomously, avoid collisions, predict traffic, and optimize port logistics and schedules.',
        "devin_body": r'''## When to use

You are routing ships autonomously, predicting maritime traffic, avoiding collisions, or optimizing port operations and schedules.

## Usage

- Plan COLREGs-aware paths and predict collision risk from AIS and radar.
- Fuse AIS, camera, LiDAR, and GNSS for maritime situational awareness.
- Optimize weather routing, fuel use, and just-in-time arrival.
- Schedule berths, cargo, and supply-chain synchronization.

## Steps

1. Collect and clean AIS tracks, weather forecasts, and port schedules.
2. Train a route-prediction or collision-risk model with historical encounter data.
3. Validate against rule-based CPA and expert maritime assessments.
4. Implement a simulator test for COLREGs give-way behavior.
5. Deploy in a closed loop with human oversight on the bridge.

## Code pattern

```python
import pandas as pd
from sklearn.cluster import DBSCAN

# Cluster vessel AIS tracks to identify common routes
ais = pd.read_csv("ais_tracks.csv")
coords = ais[["lon", "lat", "cog", "sog"]].dropna()
routes = DBSCAN(eps=0.5, min_samples=10).fit_predict(coords)
```

## Tuning notes

- Maritime environments are harsh; ensure robustness to sensor occlusion and adverse weather.
- COLREGs and safety constraints must be encoded in the planning layer, not learned blindly.
- AIS data can be sparse or spoofed; cross-validate with radar/camera.

## Verification

1. Predict collision risk from AIS encounter data and compare to rule-based CPA.
2. Plan a COLREGs-aware trajectory in a simulator and verify give-way behavior.
3. Cluster real vessel tracks and validate route interpretability with maritime experts.
''',
        "references": [
            "https://journal.hep.com.cn/jomsaa/EN/10.1007/s11804-023-00367-1",
            "https://doi.org/10.1017/s0373463326101428",
            "https://doi.org/10.1109/tits.2020.3023957",
            "https://doi.org/10.1016/j.oceaneng.2025.121988",
        ],
    },
    {
        "name": "ai-for-rail",
        "title": "AI for Rail",
        "description": 'Use machine learning to monitor rail infrastructure, predict failures, optimize timetables, and manage service disruptions.',
        "devin_body": r'''## When to use

You are monitoring track and rolling stock, predicting rail failures, optimizing timetables, or managing service disruptions.

## Usage

- Detect rail, sleeper, and track-geometry defects from inspection and sensor data.
- Predict wheelset, bearing, brake, and HVAC failures in rolling stock.
- Optimize timetables and rescheduling under delays.
- Forecast passenger flow and energy use for eco-driving.

## Steps

1. Aggregate track geometry, inspection images, and rolling-stock sensor streams.
2. Engineer per-route features to account for geography and seasonality.
3. Train an anomaly or survival model for rare infrastructure and component failures.
4. Validate recall and false-positive trade-offs with maintenance crews.
5. Integrate predictions into timetable optimization and dispatch dashboards.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import IsolationForest

# Detect anomalies in track geometry measurements
X = np.load("track_geometry_features.npy")
clf = IsolationForest(contamination=0.01, random_state=42).fit(X)
anomalies = clf.predict(X)
```

## Tuning notes

- Railway data is highly seasonal and geographically variable; model per route or line.
- Infrastructure failures are rare; use anomaly detection or survival models.
- Safety and service availability constraints dominate cost optimization.

## Verification

1. Train a track-defect detector on geometry/inspection data and evaluate recall.
2. Build a train delay prediction model from historical operations data.
3. Simulate a timetable disruption and compare an optimization-based recovery plan to a manual baseline.
''',
        "references": [
            "https://doi.org/10.3390/s26030906",
            "https://www.networkrail.co.uk/industry-and-commercial/insight-using-ai-to-run-a-reliable-railway/",
            "https://doi.org/10.1016/j.autcon.2026.107102",
            "https://doi.org/10.1007/s10994-024-06559-2",
        ],
    },
    {
        "name": "ai-for-automotive",
        "title": "AI for Automotive",
        "description": 'Inspect automotive spot welds and brake cylinders with vision models to catch micro-defects on the assembly line at 25 frames per second or faster.',
        "devin_body": r'''## When to use

You are optimizing automotive design or manufacturing, forecasting battery state of health, detecting quality defects, or improving supply chain, production, and after-sales operations.

## Usage

- Build ML surrogates for crash, NVH, and aerodynamic simulations.
- Predict battery state of health and charge from voltage, current, and temperature.
- Detect weld, paint, and assembly defects with computer vision.
- Forecast demand, schedule production, and optimize after-sales analytics.

## Steps

1. Collect design-simulation data or battery-cycle logs with variant metadata.
2. Train a surrogate, regression, or vision model with physics-aware features.
3. Validate against electrochemical, CFD, or human-inspection baselines.
4. Run edge-case and V&V tests for safety-related models.
5. Deploy into design loops, battery management, or shop-floor inspection.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict Li-ion battery state of health from cycle features
X = pd.read_csv("battery_cycles.csv")[["cycle", "avg_temp", "c_rate"]]
y = pd.read_csv("battery_soh_labels.csv")["SOH"]
model = GradientBoostingRegressor().fit(X, y)
```

## Tuning notes

- Automotive data spans many vehicle variants; ensure robust generalization.
- Battery aging is non-linear and chemistry-dependent; use physics-informed features.
- Validate safety-related models through rigorous V&V and edge-case tests.

## Verification

1. Predict battery SOH and compare error to an electrochemical model.
2. Train a weld or paint defect classifier on shop-floor images.
3. Build a production scheduling optimizer and benchmark against current planning.
''',
        "references": [
            "https://www.sciencedirect.com/science/article/abs/pii/S0736584525000882",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11902312/",
            "https://www.audi-mediacenter.com/en/press-releases/audi-scales-up-deployment-of-artificial-intelligence-in-production-17002",
            "https://www.bcg.com/publications/2026/turbocharging-automotive-operations-with-genai",
        ],
    },
    {
        "name": "ai-for-industrial-robotics",
        "title": "AI for Industrial Robotics",
        "description": 'Use machine learning to automate precision assembly, bin picking, cable routing, and force-guided manipulation in manufacturing cells.',
        "devin_body": r'''## When to use

You are automating precision assembly, cable routing, bin picking, or contact-rich tasks in a manufacturing cell.

## Usage

- Learn end-to-end manipulation and diffusion policies with force/torque feedback.
- Transfer skills from simulation to real with domain randomization.
- Ground natural-language assembly instructions in vision-language-action models.
- Curate multimodal teleoperation datasets for factory-relevant skills.

## Steps

1. Set up a robot cell with cameras, force sensors, and teleoperation recording.
2. Collect small, high-quality demonstrations for the target assembly skill.
3. Train an imitation, diffusion, or VLA policy with appropriate augmentations.
4. Validate success rate on real hardware, not just simulation.
5. Iterate with force feedback and failure analysis for contact-rich tasks.

## Code pattern

```python
import torch
import torch.nn as nn

# Simple end-effector force-guided policy network
class ForcePolicy(nn.Module):
    def __init__(self, in_dim=7, out_dim=6):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 64), nn.ReLU(),
            nn.Linear(64, out_dim)
        )

    def forward(self, x):
        return self.net(x)
```

## Tuning notes

- Contact-rich tasks need force/torque or tactile sensing, not just vision.
- Collect small but high-quality teleoperated demonstrations per skill.
- Test on real hardware early; simulation gap is large for insertion and deformation.

## Verification

1. Train a peg/insertion policy on force-torque data and measure success rate.
2. Fine-tune a VLA model on a small set of natural-language assembly instructions.
3. Compare a learned policy to a classical force controller on a contact-rich task.
''',
        "references": [
            "https://arxiv.org/abs/2607.14021v2",
            "https://www.nature.com/articles/s42256-026-01292-y",
            "https://arxiv.org/abs/2604.20246",
            "https://arxiv.org/abs/2608.17962",
        ],
    },
    {
        "name": "ai-for-drones",
        "title": "AI for Drones",
        "description": 'Assess earthquake and flood damage from UAV imagery in real time to prioritize rescue routes and distribute aid.',
        "devin_body": r'''## When to use

You are building autonomous drones for inspection, delivery, search and rescue, mapping, or natural-language-guided navigation.

## Usage

- Run visual-inertial odometry, SLAM, and object detection on embedded GPUs.
- Plan missions and allocate tasks across multi-UAV swarms.
- Use vision-language models and LLM planners for language-guided flight.
- Bridge photorealistic simulation to real flight with domain transfer.

## Steps

1. Select a lightweight model and TensorRT/ONNX runtime for the onboard computer.
2. Train perception and navigation networks on simulated and real flight data.
3. Implement geofencing, fail-safe, and low-latency obstacle avoidance.
4. Test in simulation for wind, lighting, and GNSS-denied scenarios.
5. Fly limited real-world missions and log metrics for retraining.

## Code pattern

```python
from ultralytics import YOLO
import cv2

# Detect objects from a drone camera feed for inspection
model = YOLO("yolov8n.pt")
frame = cv2.imread("drone_frame.jpg")
results = model(frame)
```

## Tuning notes

- Drones are resource-constrained; use lightweight models and TensorRT/ONNX for inference.
- Safety critical: enforce geofencing, fail-safe, and low-latency obstacle avoidance.
- Outdoor flight needs robustness to wind, lighting, and GNSS-denied conditions.

## Verification

1. Run a real-time object detector on a drone video feed and report FPS/accuracy.
2. Implement vision-based navigation in a simulator and test waypoint following.
3. Deploy a multi-drone task-allocation algorithm in a simulated swarm scenario.
''',
        "references": [
            "https://doi.org/10.1016/j.array.2024.100361",
            "https://arxiv.org/abs/2606.12142",
            "https://arxiv.org/abs/2509.18610",
            "https://doi.org/10.13111/2066-8201.2026.18.2.9",
        ],
    },
    {
        "name": "ai-for-smart-manufacturing",
        "title": "AI for Smart Manufacturing",
        "description": 'Use machine learning to build digital twins, optimize processes in real time, predict maintenance, and improve sustainability in cyber-physical factories.',
        "devin_body": r'''## When to use

You are designing cyber-physical factories, building digital twins, optimizing processes in real time, or deploying predictive maintenance across production lines.

## Usage

- Synchronize virtual-physical twins with IoT and OT data.
- Optimize process parameters with Bayesian or reinforcement learning.
- Predict in-line defects and remaining useful life of machine tools.
- Optimize energy, waste, and circular-economy metrics.

## Steps

1. Ingest and time-align machine, process, and quality data from OT/IT systems.
2. Build a digital twin of the process and validate against real telemetry.
3. Train a predictive model for quality or energy KPIs.
4. Optimize parameters with Bayesian or RL and measure KPI improvement.
5. Close the loop with interpretable dashboards for operators.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict a manufacturing KPI from machine and process features
X = pd.read_csv("process_features.csv")
y = pd.read_csv("kpi_labels.csv")["energy_per_part"]
model = GradientBoostingRegressor().fit(X, y)
```

## Tuning notes

- Integrate OT/IT data carefully; time synchronization and data quality are key.
- Models must be interpretable for operators and maintainable on the shop floor.
- Validate digital twins against real machine behavior before closed-loop control.

## Verification

1. Build a digital twin of a simple manufacturing process and compare to real telemetry.
2. Optimize process parameters with Bayesian optimization and measure KPI improvement.
3. Predict equipment failures from sensor streams and evaluate lead time vs false positives.
''',
        "references": [
            "https://iopscience.iop.org/article/10.1088/3049-4761/ae5967",
            "https://www.mdpi.com/2076-3417/13/3/1903",
            "https://doi.org/10.1016/j.cirp.2024.04.101",
            "https://www.nature.com/articles/s41598-025-25413-6",
        ],
    },
    {
        "name": "ai-for-quality-control",
        "title": "AI for Quality Control",
        "description": 'Use machine learning and computer vision to inspect products, detect defects, monitor process stability, and move toward zero-defect manufacturing.',
        "devin_body": r'''## When to use

You are automating visual inspection, detecting product defects, monitoring process stability, or building zero-defect manufacturing systems.

## Usage

- Classify and segment scratches, dents, and contamination from production images.
- Track control charts and process capability for drift and out-of-control points.
- Detect novel defects with unsupervised or few-shot anomaly models.
- Deploy real-time inspection on cameras and PLCs at the edge.

## Steps

1. Collect nominal and defect images from real production, not just clean labs.
2. Balance the dataset with augmentation, weighted loss, or anomaly methods.
3. Train and calibrate a classifier or segmentation model for false-accept/reject trade-offs.
4. Validate on a hold-out production sample with operator review.
5. Deploy at the edge and monitor drift over shifts and suppliers.

## Code pattern

```python
import torch
import torchvision.models as models

# Fine-tune a ResNet for binary defect classification
model = models.resnet18(pretrained=True)
model.fc = torch.nn.Linear(model.fc.in_features, 2)
# dataloader = DataLoader(...)  # nominal vs defect images
```

## Tuning notes

- Defect datasets are highly imbalanced; use augmentation, weighted loss, or anomaly detection.
- Optimize for both false-accept and false-reject rates based on business cost.
- Calibrate inspection systems on real production samples, not only clean lab images.

## Verification

1. Train a defect classifier on an industrial image dataset and measure precision/recall.
2. Build an SPC dashboard and flag out-of-control points in a process time series.
3. Compare an unsupervised anomaly model to supervised training with few labels.
''',
        "references": [
            "https://link.springer.com/article/10.1007/s44245-026-00320-w",
            "https://www.mitutoyo.com/aiinspect/",
            "https://roboflow.com/ai/quality-control",
            "https://doi.org/10.3390/app16010037",
        ],
    },
    {
        "name": "ai-for-warehouse-robotics",
        "title": "AI for Warehouse Robotics",
        "description": 'Use machine learning to route mobile robots, allocate tasks, avoid congestion, and manage traffic in goods-to-person warehouses.',
        "devin_body": r'''## When to use

You are deploying mobile robots in a warehouse, coordinating fleets, allocating pick/place tasks, or optimizing traffic and throughput.

## Usage

- Solve conflict-free multi-agent path finding for large robot fleets.
- Assign orders to robots and stations under deadlines and capacity constraints.
- Predict traffic and congestion to learn-augment planning.
- Integrate barcode scanning, shelf picking, and obstacle detection.

## Steps

1. Model the warehouse as a graph or grid with zones, charging, and stations.
2. Implement a MAPF or task-allocation baseline and a greedy comparator.
3. Train a congestion-prediction or learning-augmented policy on trajectory data.
4. Validate throughput and latency in a discrete-event simulator.
5. Deploy with online replanning for dynamic obstacles and order spikes.

## Code pattern

```python
import networkx as nx

# Simple warehouse graph for shortest-path routing
G = nx.grid_2d_graph(20, 20)
pos = (0, 0)
goal = (15, 18)
route = nx.shortest_path(G, pos, goal)
```

## Tuning notes

- Warehouse environments are dynamic; replan online around new obstacles and tasks.
- Prioritize throughput and latency, but also battery and maintenance constraints.
- Use simulation to validate MAPF and task-allocation policies before live deployment.

## Verification

1. Implement a MAPF solver and compare throughput to a greedy routing baseline.
2. Train a traffic-prediction model on warehouse robot trajectory data.
3. Run a pick-assignment policy in a discrete-event warehouse simulation.
''',
        "references": [
            "https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination",
            "https://news.mit.edu/2026/ai-system-keeps-warehouse-robot-traffic-running-smoothly-0326",
            "https://www.nature.com/articles/s41598-026-63868-3",
            "https://doi.org/10.1613/jair.1.20611",
        ],
    },
    {
        "name": "ai-for-field-robotics",
        "title": "AI for Field Robotics",
        "description": 'Navigate autonomous robots through farms and construction sites to target weeds, harvest crops, and inspect hazards.',
        "devin_body": r'''## When to use

You are building robots for crop monitoring, infrastructure inspection, environmental survey, mining, construction, or search-and-rescue in unstructured terrain.

## Usage

- Estimate terrain traversability and build semantic maps for off-road navigation.
- Detect crops, weeds, and stress with agricultural robots.
- Assess damage and locate humans in disaster and inspection missions.
- Fuse aerial and ground observations for field situational awareness.

## Steps

1. Collect diverse, georeferenced sensor data across weather and lighting.
2. Train a terrain or crop segmentation model with field labels.
3. Validate across locations and seasons for robustness.
4. Plan autonomous missions in a high-fidelity simulator with power/comms constraints.
5. Run a real-world field test and compare coverage and safety to baseline.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Classify crop health from field robot sensor features
X = np.load("field_spectra_features.npy")
y = np.load("crop_health_labels.npy")
clf = RandomForestClassifier(n_estimators=200).fit(X, y)
```

## Tuning notes

- Field data is highly variable; collect diverse, georeferenced training data.
- Power, communication, and mobility constraints are stricter than indoor robots.
- Combine aerial and ground observations for a richer field understanding.

## Verification

1. Train a crop-stress classifier on field sensor data and validate across locations.
2. Build a terrain-traversability map from LiDAR/camera data and compare to human labels.
3. Run an autonomous inspection mission in a field simulator and measure coverage.
''',
        "references": [
            "https://www.sciopen.com/article/10.1016/j.plaphe.2025.100085",
            "https://doi.org/10.48550/arxiv.2502.09379",
            "https://ojs.aaai.org/index.php/AAAI/article/view/41474",
            "https://link.springer.com/article/10.1007/s44163-026-01504-9",
        ],
    },
    {
        "name": "ai-for-exoskeletons",
        "title": "AI for Exoskeletons",
        "description": 'Use machine learning to recognize gait and intent, personalize assistance, and control wearable exoskeletons for rehabilitation and industrial augmentation.',
        "devin_body": r'''## When to use

You are designing control for an exoskeleton or exosuit, predicting user gait intention, personalizing assistance, or rehabilitating movement disorders.

## Usage

- Classify gait phase and activity from EMG, IMU, and motion-capture data.
- Estimate biological joint moments and adapt assistance in real time.
- Personalize rehabilitation therapy with assistance-as-needed control.
- Design soft exosuit control for energy-efficient, comfortable support.

## Steps

1. Collect wearable sensor and motion-capture data during walking and tasks.
2. Calibrate subject-specific models and segment gait phases.
3. Train an intention/phase classifier or a reinforcement-learning controller.
4. Validate with clinical populations and real-world activities, not only lab walking.
5. Measure effort or metabolic reduction and iterate the assistance profile.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Classify gait phase from IMU/EMG features for exoskeleton timing
X = np.load("gait_features.npy")
y = np.load("gait_phases.npy")
clf = RandomForestClassifier(n_estimators=200).fit(X, y)
```

## Tuning notes

- Wearable systems must be safe, comfortable, and responsive with low latency.
- Use subject-specific calibration and online adaptation for gait changes.
- Validate with clinical populations and real-world activities, not only lab walking.

## Verification

1. Classify gait phases from wearable sensor data and compare to ground-truth motion capture.
2. Implement an assistive torque profile and test metabolic/effort reduction.
3. Evaluate a reinforcement-learning controller for stable walking under perturbations.
''',
        "references": [
            "https://www.science.org/doi/10.1126/scirobotics.adt7329",
            "https://link.springer.com/article/10.1007/s42235-025-00836-z",
            "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1341580/full",
            "https://www.nature.com/articles/s41586-024-08157-7",
        ],
    },
]
