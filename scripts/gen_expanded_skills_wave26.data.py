SKILLS = [
    {
        "name": "ai-for-aerospace",
        "title": "AI for Aerospace",
        "description": "Machine learning for aircraft and spacecraft design, aerodynamic optimization, structural health monitoring, satellite operations, and certification of safety-critical aerospace systems.",
        "devin_body": r'''## When to use

You are designing aircraft or spacecraft, analyzing flight/structural data, building digital twins, or certifying ML for safety-critical aerospace applications.

## Key concepts

- **Aerodynamic and structural ML**: surrogate models, reduced-order models, and shape optimization for wings and airframes.
- **Structural health monitoring (SHM)**: vibration, acoustic, and strain-based damage detection and remaining useful life.
- **Satellite and mission operations**: telemetry anomaly detection, power/thermal forecasting, and autonomous scheduling.
- **Certification and assurance**: interpretability, verification, and validation for airborne AI.

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
        "description": "AI for airline and airport operations, including predictive maintenance, crew and fleet scheduling, disruption recovery, fuel optimization, and safety analytics.",
        "devin_body": r'''## When to use

You are optimizing airline operations, forecasting aircraft component failures, recovering from schedule disruptions, or improving fleet reliability.

## Key concepts

- **Predictive maintenance (PdM)**: time-series and survival models on engine and component sensor data (e.g., C-MAPSS).
- **Flight operations optimization**: fuel burn, crew rostering, turnaround, and delay recovery.
- **Fleet health platforms**: consolidation of in-flight and maintenance data for failure prediction.
- **Safety and reliability analytics**: risk prediction, incident classification, and maintenance planning.

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
        "description": "AI for maritime autonomous surface ships, route and weather routing optimization, collision avoidance, port logistics, and vessel situational awareness.",
        "devin_body": r'''## When to use

You are routing ships autonomously, predicting maritime traffic, avoiding collisions, or optimizing port operations and schedules.

## Key concepts

- **Maritime Autonomous Surface Ships (MASS)**: COLREGs-compliant navigation, path planning, and decision-making.
- **Situational awareness**: sensor fusion across AIS, radar, LiDAR, cameras, and GNSS.
- **Route optimization**: weather routing, fuel minimization, and just-in-time arrival.
- **Port and logistics AI**: berth scheduling, cargo handling, and supply-chain synchronization.

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
        "description": "AI for railway infrastructure health, predictive maintenance, train scheduling, energy optimization, and real-time disruption management.",
        "devin_body": r'''## When to use

You are monitoring track and rolling stock, predicting rail failures, optimizing timetables, or managing service disruptions.

## Key concepts

- **Track geometry and infrastructure monitoring**: ride quality, rail/sleeper defects, and ultrasonic/vision inspection.
- **Predictive maintenance for rolling stock**: wheelset bearing, brake, and HVAC prognostics.
- **Timetabling and traffic control**: mixed-integer programming, reinforcement learning, and rescheduling under delays.
- **Energy and operations**: eco-driving, regenerative braking, and passenger flow forecasting.

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
        "description": "AI for automotive design, manufacturing, battery management, ADAS, quality control, and supply-chain optimization across the vehicle lifecycle.",
        "devin_body": r'''## When to use

You are optimizing automotive design or manufacturing, forecasting battery state of health, detecting quality defects, or improving supply chain, production, and after-sales operations.

## Key concepts

- **Computer-aided engineering and design**: ML surrogates for crash, NVH, and aerodynamic simulations.
- **Battery management and state estimation**: SOH/SOC prediction from voltage, current, and temperature.
- **Factory and supply-chain AI**: predictive maintenance, demand forecasting, quality analytics, and production scheduling.
- **Connected-vehicle and after-sales analytics**: telematics, warranty prediction, and customer-vehicle health insights.

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
        "description": "Machine learning for factory manipulation, assembly, pick-and-place, force control, sim-to-real, and vision-language-action models in industrial settings.",
        "devin_body": r'''## When to use

You are automating precision assembly, cable routing, bin picking, or contact-rich tasks in a manufacturing cell.

## Key concepts

- **Industrial dexterity and manipulation**: end-to-end imitation and diffusion policies, force/torque and tactile feedback.
- **Sim-to-real transfer**: domain randomization, teacher-student distillation, and synthetic datasets.
- **Vision-language-action (VLA) models**: grounding natural-language instructions in robot policies.
- **Multimodal datasets and benchmarks**: PRISM, Industrial Dexterity Benchmark, and factory-relevant skills.

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
        "description": "AI for UAV perception, navigation, obstacle avoidance, mission planning, multi-drone coordination, and vision-language drone control.",
        "devin_body": r'''## When to use

You are building autonomous drones for inspection, delivery, search and rescue, mapping, or natural-language-guided navigation.

## Key concepts

- **Vision-based drone navigation**: VIO, visual SLAM, and object detection on embedded GPUs.
- **Foundation models for drones**: vision-language navigation, LLM mission planners, and neural policies.
- **Swarm and multi-UAV coordination**: task allocation, collision avoidance, and communication-constrained control.
- **Sim-to-real**: AirSim, Gazebo, and photorealistic simulators with domain transfer.

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
        "description": "AI for cyber-physical manufacturing, digital twins, real-time process optimization, predictive maintenance, and sustainable Industry 4.0/5.0 systems.",
        "devin_body": r'''## When to use

You are designing cyber-physical factories, building digital twins, optimizing processes in real time, or deploying predictive maintenance across production lines.

## Key concepts

- **Digital twins and real-time analytics**: virtual-physical synchronization, IoT data integration, and closed-loop control.
- **Smart process optimization**: Bayesian optimization, reinforcement learning, and multi-objective parameter tuning.
- **Predictive quality and maintenance**: in-line defect prediction and remaining useful life for machine tools.
- **Sustainable manufacturing**: energy optimization, waste reduction, and circular-economy analytics.

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
            "https://par.nsf.gov/servlets/purl/10544873",
            "https://www.nature.com/articles/s41598-025-25413-6",
        ],
    },
    {
        "name": "ai-for-quality-control",
        "title": "AI for Quality Control",
        "description": "Machine learning and computer vision for automated inspection, defect detection, statistical process control, and zero-defect manufacturing.",
        "devin_body": r'''## When to use

You are automating visual inspection, detecting product defects, monitoring process stability, or building zero-defect manufacturing systems.

## Key concepts

- **Machine-vision defect detection**: CNNs, transformers, and anomaly segmentation for scratches, dents, and contamination.
- **Statistical process control (SPC)**: control charts, process capability, and drift monitoring.
- **Unsupervised and few-shot learning**: training on nominal samples and detecting novel defects.
- **Edge deployment**: real-time inference on cameras and PLCs on the factory floor.

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
        "description": "AI for autonomous mobile robots, goods-to-person systems, picking, multi-agent path finding, task allocation, and warehouse traffic management.",
        "devin_body": r'''## When to use

You are deploying mobile robots in a warehouse, coordinating fleets, allocating pick/place tasks, or optimizing traffic and throughput.

## Key concepts

- **Multi-Agent Path Finding (MAPF)**: conflict-free routing for large robot fleets in grid-based or graph warehouses.
- **Task allocation and scheduling**: assignment of orders to robots and stations under deadlines and capacity.
- **Foundation models for fleet prediction**: traffic prediction, congestion management, and learning-augmented planning.
- **Perception and manipulation**: barcode scanning, shelf picking, and obstacle detection.

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
        "description": "AI for robots operating in outdoor, unstructured environments such as agriculture, construction, mining, environmental monitoring, and disaster response.",
        "devin_body": r'''## When to use

You are building robots for crop monitoring, infrastructure inspection, environmental survey, mining, construction, or search-and-rescue in unstructured terrain.

## Key concepts

- **Terrain perception and navigation**: SLAM, semantic segmentation, and traversability estimation in off-road environments.
- **Agricultural and environmental robotics**: phenotyping, weed detection, and precision spraying.
- **Disaster and inspection robotics**: damage assessment, human detection, and autonomous traverse in hazardous zones.
- **Robustness to field conditions**: weather, dust, lighting variation, and GPS-denied operation.

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
        "description": "AI for wearable exoskeleton and exosuit control, gait and intention recognition, human-robot interaction, rehabilitation, and assistive augmentation.",
        "devin_body": r'''## When to use

You are designing control for an exoskeleton or exosuit, predicting user gait intention, personalizing assistance, or rehabilitating movement disorders.

## Key concepts

- **Intention and gait recognition**: EMG, IMU, and motion-capture-based classification of gait phase and activity.
- **Task-agnostic and adaptive control**: biological joint-moment estimation, reinforcement learning, and human-in-the-loop optimization.
- **Rehabilitation robotics**: personalized therapy, assistance-as-needed, and outcome monitoring.
- **Soft exosuits and assistive devices**: lightweight textiles, cable drives, and energy-efficient control.

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
