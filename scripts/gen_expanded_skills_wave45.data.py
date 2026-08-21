SKILLS = [
    {
        "name": "ai-for-network-optimization",
        "title": "AI for Network Optimization",
        "description": "Optimize routing, traffic engineering, and resource allocation in communication networks.",
        "devin_body": r'''## When to use

You need to optimize routing, traffic engineering, resource allocation, load balancing, or network design in large-scale communication networks.

## Usage

- Solve traffic engineering with GRL-TE, RedTE, or TELGEN.
- Predict congestion and adjust routing with GNNs.
- Allocate bandwidth and paths across WAN and data-center fabrics.
- Optimize CDN and load-balancer decisions.
- Improve network utilization with deep reinforcement learning.

## Steps

1. Collect topology, traffic matrices, and performance metrics.
2. Build graph or path features for the network.
3. Train GNN, RL, or optimization surrogates.
4. Deploy recommendations to SDN or traffic-engineering controllers.
5. Validate against throughput, latency, and utilization KPIs.

## Code pattern

```python
import networkx as nx
import numpy as np

# Build a directed graph with link capacities
G = nx.DiGraph()
for u, v, c in [("A", "B", 100), ("B", "C", 80), ("A", "C", 50)]:
    G.add_edge(u, v, capacity=c, weight=1)

# Shortest paths subject to link weights; ML can predict dynamic weights
path = nx.shortest_path(G, source="A", target="C", weight="weight")
print(path)
```

## Tuning notes

- Use a graph-structured state representation that preserves topology and local demand.
- Reward shaping in DRL is critical; design rewards around latency, throughput, jitter, and cost.
- Validate against a strong baseline such as shortest-path or max-flow heuristics.
- Add robustness to distribution shift between training and live traffic.

## Verification

1. Train a DRL agent for load balancing and compare total delay to a baseline routing policy.
2. Use a traffic forecaster to drive a prescriptive bandwidth-allocation model.
3. Evaluate generalization when node/link failure patterns differ from training.
''',
        "references": ["https://doi.org/10.1186/s13174-018-0087-2", "https://arxiv.org/abs/2507.01773", "https://arxiv.org/abs/2308.05384v2", "https://arxiv.org/abs/2402.01665v1"],
    },
    {
        "name": "ai-for-network-security",
        "title": "AI for Network Security",
        "description": "Detect intrusions, malware, and anomalies in network traffic and infrastructure.",
        "devin_body": r'''## When to use

You need to detect intrusions, malware, anomalies, or adversarial threats in network traffic, logs, or endpoints.

## Usage

- Analyze Zeek, Suricata, and NetFlow logs with AutoZeekWatch.
- Detect DDoS, C2, and exfiltration patterns.
- Hunt threats with MITRE ATT&CK and ELK/Splunk.
- Identify anomalous hosts and lateral movement.
- Correlate alerts with SIEM and asset context.

## Steps

1. Collect packet captures, flow records, and alert logs.
2. Engineer features for hosts, ports, protocols, and payloads.
3. Train supervised or unsupervised anomaly/IDS models.
4. Integrate with SIEM and SOAR workflows.
5. Tune and retrain with red-team findings.

## Code pattern

```python
from sklearn.ensemble import IsolationForest
import pandas as pd

# Flow-level features: bytes, duration, packet count, port, protocol
X = df[["bytes_in", "bytes_out", "duration", "packets", "dst_port"]]

# Train an unsupervised anomaly detector
clf = IsolationForest(contamination=0.01, random_state=42)
df["anomaly_score"] = clf.decision_function(X)
```

## Tuning notes

- Security data is extremely imbalanced; use cost-sensitive learning and time-aware splits.
- Monitor concept drift because attack patterns evolve rapidly.
- Combine signature, statistical, and ML detectors for defense in depth.
- Validate adversarial robustness with known evasion techniques and anomaly injection.

## Verification

1. Train an intrusion detector and report precision-recall on a labeled test set.
2. Build a graph feature extractor and measure lift over tabular features.
3. Test robustness to adversarial perturbations of network-flow features.
''',
        "references": ["https://arxiv.org/abs/1911.02621", "https://arxiv.org/abs/2405.04760v3", "https://arxiv.org/abs/2504.07839", "https://arxiv.org/abs/2409.18736"],
    },
    {
        "name": "ai-for-software-defined-networks",
        "title": "AI for Software-Defined Networks",
        "description": "Apply AI to SDN control planes for traffic classification, routing, and security.",
        "devin_body": r'''## When to use

You are building or operating an SDN/NFV architecture and want to add intelligence for traffic classification, routing, QoS, or security.

## Usage

- Classify OpenFlow traffic in ONOS/RYU with SDN-CF.
- Detect and block malicious flows at the controller.
- Optimize routing and load balancing via northbound APIs.
- Enforce microsegmentation and QoS policies.
- Integrate with Mininet and OpenFlow switches.

## Steps

1. Set up SDN controller and network emulator.
2. Collect flow and packet-in events.
3. Train classification or optimization models.
4. Deploy control-plane applications (xApps, controller modules).
5. Validate with network metrics and security scenarios.

## Code pattern

```python
# Example: classify flows from OpenFlow statistics with a Random Forest
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

X = df[["packet_count", "byte_count", "flow_duration", "protocol"]]
y = df["application_label"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
predicted_app = model.predict(X)
```

## Tuning notes

- Keep inference latency low; many SDN decisions require sub-second reaction.
- Use the global network view from the controller but respect privacy and control-plane scalability.
- Integrate with OpenFlow or gRPC interfaces to update rules automatically.
- Validate policies in a Mininet testbed before production deployment.

## Verification

1. Deploy an ML-based traffic classifier in an SDN controller and measure accuracy.
2. Compare a learned routing policy to shortest-path routing on a Mininet topology.
3. Demonstrate DDoS mitigation by installing drop rules when an anomaly is detected.
''',
        "references": ["https://doi.org/10.1109/comst.2018.2866942", "https://doi.org/10.1007/s44230-023-00025-3", "https://doi.org/10.2478/jsiot-2023-0002", "https://doi.org/10.1109/ssd.2019.8893244"],
    },
    {
        "name": "ai-for-5g",
        "title": "AI for 5G",
        "description": "Optimize 5G RAN, network slicing, and beam management with AI and NWDAF.",
        "devin_body": r'''## When to use

You are optimizing 5G RAN, core, or transport functions such as network slicing, beam management, mobility, or resource allocation.

## Usage

- Predict RAN congestion and optimize beam prediction (3GPP Rel-18/19).
- Manage network slices with NWDAF and O-RAN RIC.
- Improve handover, coverage, and capacity optimization.
- Detect anomalies in 5G core and RAN KPIs.
- Optimize energy and resource allocation.

## Steps

1. Collect 5G RAN and core performance data.
2. Engineer beam, cell, slice, and mobility features.
3. Train prediction, classification, or RL models.
4. Deploy xApps/rApps in O-RAN or NWDAF frameworks.
5. Validate with 3GPP KPIs and drive tests.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict KPI from RAN metrics
features = ["rsrp", "sinr", "prb_usage", "ue_count", "throughput"]
X = df[features]
y = df["latency_ms"]

model = GradientBoostingRegressor(random_state=42)
model.fit(X, y)
```

## Tuning notes

- Use 3GPP network data analytics (NWDAF) as a data source when available.
- Respect real-time constraints; RAN control loops demand low inference latency.
- Combine model-driven signal processing with data-driven ML for hybrid gains.
- Validate on realistic drive-test or simulation traces with channel variation.

## Verification

1. Build a KPI predictor for latency or throughput and backtest on a 5G trace.
2. Compare a learned beam-selection policy to an exhaustive search baseline.
3. Demonstrate slice resource orchestration under varying load.
''',
        "references": ["https://arxiv.org/abs/2306.06178v1", "https://arxiv.org/pdf/2305.05092", "https://arxiv.org/abs/2009.04943", "https://arxiv.org/abs/1911.03585"],
    },
    {
        "name": "ai-for-6g",
        "title": "AI for 6G",
        "description": "Design AI-native 6G systems for semantic communication, ISAC, and non-terrestrial networks.",
        "devin_body": r'''## When to use

You are designing or prototyping future 6G systems involving semantic communications, ISAC, RIS, NTN, or AI-native architectures.

## Usage

- Build semantic communication and meaning-extraction models.
- Optimize integrated sensing and communication (ISAC).
- Manage reconfigurable intelligent surfaces and satellite links.
- Allocate resources in space-air-ground integrated networks.
- Simulate 6G scenarios in MATLAB/NS-3.

## Steps

1. Define 6G use case and channel model.
2. Generate or collect multi-domain dataset (terrestrial/satellite).
3. Train semantic, ISAC, or resource-allocation models.
4. Evaluate over-the-air or in simulation.
5. Iterate with RIS, RAN, and satellite constraints.

## Code pattern

```python
import numpy as np

# RIS phase optimization: random phases and simple SNR estimate
N = 64
phases = np.exp(1j * np.random.uniform(0, 2 * np.pi, N))
channel = np.random.randn(N) + 1j * np.random.randn(N)
snr = np.abs(np.sum(phases * channel)) ** 2
print("Estimated SNR:", snr)
```

## Tuning notes

- 6G is still emerging; use simulation testbeds (e.g., MATLAB, Sionna, ns-3) for validation.
- Integrate physics-based priors to improve data efficiency.
- Optimize for energy efficiency and sustainability from the start.
- Use digital twins to bridge simulation and real-world deployment.

## Verification

1. Simulate a semantic-communication system and compare rate-distortion to a conventional bit-level scheme.
2. Optimize RIS phases with DRL and verify channel gain improvement.
3. Model an ISAC scenario and evaluate sensing accuracy versus communication rate.
''',
        "references": ["https://arxiv.org/abs/2412.14538v3", "https://doi.org/10.1109/ojcoms.2026.3677293", "https://arxiv.org/abs/2207.13382", "https://arxiv.org/abs/2406.13335"],
    },
    {
        "name": "ai-for-iot",
        "title": "AI for IoT",
        "description": "Deploy TinyML and edge AI for monitoring, prediction, and control in IoT systems.",
        "devin_body": r'''## When to use

You are deploying intelligence on IoT sensors, gateways, or edge devices for monitoring, predictive maintenance, anomaly detection, or control.

## Usage

- Build anomaly detection on STM32 with NanoEdge AI Studio.
- Deploy time-series classifiers with tinyml-tensorlab.
- Predict equipment failure in industrial IoT (EsoCore).
- Optimize battery and bandwidth with on-device learning.
- Classify audio/vibration/IMU signals at the edge.

## Steps

1. Select MCU and sensors and collect edge data.
2. Train, prune, and quantize TinyML models.
3. Compile and deploy with CMSIS-NN or vendor tools.
4. Verify latency, memory, and power budgets.
5. Retrain on-device or via federated updates.

## Code pattern

```python
from sklearn.ensemble import IsolationForest
import pandas as pd

# Sensor time-series features: mean, std, min, max over a window
X = df[["temp_mean", "temp_std", "humidity_mean", "vibration_peak"]]

clf = IsolationForest(contamination=0.02, random_state=42)
df["anomaly"] = clf.fit_predict(X)
```

## Tuning notes

- IoT devices are resource-constrained; quantize, prune, or distill models.
- Use streaming/online learning to adapt to changing environments.
- Balance communication cost with model accuracy through offloading or federated learning.
- Validate on real device traces and consider class imbalance for rare events.

## Verification

1. Train a TinyML anomaly detector and measure inference latency on a target board.
2. Build a device-fingerprinting classifier and evaluate on unseen device models.
3. Predict equipment failure and compare to a rule-based maintenance schedule.
''',
        "references": ["https://arxiv.org/abs/2410.19998v1", "https://doi.org/10.1145/3690639", "https://arxiv.org/abs/2011.08612", "https://arxiv.org/abs/2406.03820"],
    },
    {
        "name": "ai-for-edge-computing",
        "title": "AI for Edge Computing",
        "description": "Optimize model inference, task offloading, and resource management at the network edge.",
        "devin_body": r'''## When to use

You need to deploy, orchestrate, or optimize ML inference and training at the edge for low latency, privacy, and bandwidth savings.

## Usage

- Deploy TensorFlow Lite or ONNX Runtime on edge devices.
- Optimize models with Triton Model Navigator or LiteRT.
- Schedule inference and offloading between edge and cloud.
- Manage edge clusters with Kubernetes/K3s.
- Profile latency and energy across edge nodes.

## Steps

1. Characterize edge hardware, network, and workloads.
2. Quantize, prune, and convert models for edge runtimes.
3. Build offloading and scheduling policies.
4. Deploy via edge serving frameworks.
5. Monitor latency, accuracy, and energy.

## Code pattern

```python
import numpy as np
from scipy.optimize import linear_sum_assignment

# Cost matrix: tasks x edge nodes (latency estimate)
cost = np.array([[10, 25, 60], [15, 8, 50], [30, 20, 12]])
row_ind, col_ind = linear_sum_assignment(cost)
print("Assignments:", list(zip(row_ind, col_ind)))
```

## Tuning notes

- Profile end-to-end latency, energy, and memory, not just model accuracy.
- Use quantization-aware training for integer accelerators.
- Cache popular models and data near users; monitor drift on edge telemetry.
- Validate offloading policies under bandwidth and battery constraints.

## Verification

1. Quantize a model and measure accuracy and latency on an edge device.
2. Optimize task offloading across a set of edge nodes and compare to a greedy baseline.
3. Run a small federated-learning round and evaluate convergence vs. centralized.
''',
        "references": ["https://doi.org/10.3390/fi17090417", "https://ieeexplore.ieee.org/document/9933792", "https://www.mdpi.com/2227-7080/12/6/81", "https://www.mdpi.com/2673-8732/5/2/16"],
    },
    {
        "name": "ai-for-fog-computing",
        "title": "AI for Fog Computing",
        "description": "Orchestrate tasks, resources, and services across fog and cloud tiers.",
        "devin_body": r'''## When to use

You are designing a fog layer between IoT devices and the cloud for low-latency, distributed processing and resource orchestration.

## Usage

- Schedule latency-sensitive tasks with FogSim and RL.
- Place containers and microservices across fog nodes.
- Predict workload and resource demands.
- Manage IoT data streams and actuation.
- Optimize energy and cost with tier-aware policies.

## Steps

1. Model the fog/cloud/edge topology and workloads.
2. Collect telemetry and latency data.
3. Train task-placement and resource-allocation models.
4. Deploy orchestration policies.
5. Validate end-to-end latency and throughput.

## Code pattern

```python
import pulp

# Fog task placement: binary decision variables
tasks = range(3)
nodes = range(2)
x = pulp.LpVariable.dicts("x", (tasks, nodes), cat="Binary")

prob = pulp.LpProblem("FogPlacement", pulp.LpMinimize)
# Cost: latency per assignment
cost = [[5, 12], [9, 4], [15, 7]]
prob += pulp.lpSum(cost[i][j] * x[i][j] for i in tasks for j in nodes)

# One node per task
for i in tasks:
    prob += pulp.lpSum(x[i][j] for j in nodes) == 1

prob.solve()
```

## Tuning notes

- Include queuing and network delay in the cost model, not just compute.
- Use multi-objective optimization when latency, energy, and cost conflict.
- Consider device mobility and intermittent connectivity.
- Validate in a simulated or containerized fog testbed.

## Verification

1. Formulate a fog task-placement problem and solve it with an optimizer.
2. Compare an RL scheduler against a greedy latency-minimizing baseline.
3. Evaluate end-to-end latency for a hybrid cloud-fog deployment.
''',
        "references": ["https://doi.org/10.1016/j.iot.2022.100674", "https://www.mdpi.com/1424-8220/25/3/687", "https://arxiv.org/abs/2208.00761", "https://arxiv.org/abs/2212.04645"],
    },
    {
        "name": "ai-for-satellite-communications",
        "title": "AI for Satellite Communications",
        "description": "Optimize beam hopping, resource allocation, and coverage in LEO and GEO constellations.",
        "devin_body": r'''## When to use

You are building AI for satellite systems, including constellation management, link prediction, beam hopping, resource allocation, and NTN integration.

## Usage

- Optimize beam-hopping patterns with multi-agent DRL.
- Allocate power and bandwidth for LEO/GEO networks.
- Build digital twins of satellite constellations.
- Manage inter-satellite links and handovers.
- Predict demand and traffic hotspots.

## Steps

1. Collect constellation ephemeris and traffic demand.
2. Build channel and demand models.
3. Train DRL or optimization policies for beam/power.
4. Evaluate in STK or custom simulators.
5. Deploy on-board or ground-based controllers.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict rain attenuation from weather features
X = df[["rain_rate", "elevation_angle", "frequency_ghz", "cloud_water"]]
y = df["attenuation_db"]

model = GradientBoostingRegressor(random_state=42)
model.fit(X, y)
```

## Tuning notes

- Satellite channels vary with weather, orbital dynamics, and interference; include temporal features.
- On-board compute is heavily constrained; use quantized or sparse models.
- NTN handover and timing advance are challenging; validate with realistic ephemeris.
- Combine link-level and network-level optimization for global throughput.

## Verification

1. Build a satellite link-quality predictor and evaluate on historical data.
2. Design a beam-hopping policy and compare to a fixed beam plan.
3. Simulate an NTN scenario and show throughput/latency trade-offs.
''',
        "references": ["https://doi.org/10.1109/comst.2025.3534617", "https://arxiv.org/abs/2304.13008", "https://doi.org/10.1002/sat.1482", "https://ieeexplore.ieee.org/document/10886927"],
    },
    {
        "name": "ai-for-optical-networks",
        "title": "AI for Optical Networks",
        "description": "Estimate QoT, assign spectrum, and route traffic in elastic optical networks.",
        "devin_body": r'''## When to use

You need to add intelligence to optical transport and access networks for performance monitoring, QoT estimation, traffic engineering, and fault management.

## Usage

- Predict OSNR, BER, and QoT with DNNs (OCATA).
- Solve QoT-aware routing and spectrum assignment (PtrNet-RSA).
- Detect physical-layer anomalies in multiband links.
- Optimize amplifier settings and launch power.
- Plan lightpaths with digital twins.

## Steps

1. Collect topology, traffic, and physical-layer parameters.
2. Build GN-model or data-driven QoT features.
3. Train QoT and RSA models.
4. Integrate with optical control plane.
5. Validate against BER/Q-factor and blocking rate.

## Code pattern

```python
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# QoT estimation from network and physical-layer features
X = df[["distance_km", "num_spans", "modulation", "launched_power"]]
y = df["osnr_db"]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)
```

## Tuning notes

- Use accurate physical-layer simulation or field data for labels; synthetic data may not transfer.
- Feature engineering from constellations, spectra, and impairment histograms helps.
- Consider uncertainty in QoT predictions to avoid service disruptions.
- Retrain frequently when amplifier, fiber, or load conditions change.

## Verification

1. Build a QoT estimator and validate against a physical-layer simulator.
2. Predict traffic demand and provision optical paths ahead of peak load.
3. Implement an ML-based nonlinearity precompensation and measure BER improvement.
''',
        "references": ["https://arxiv.org/abs/2003.05290", "https://doi.org/10.1016/j.osn.2017.12.006", "https://doi.org/10.1109/access.2023.3312387", "https://doi.org/10.1109/access.2025.3569559"],
    },
    {
        "name": "ai-for-wireless-communications",
        "title": "AI for Wireless Communications",
        "description": "Estimate channels, classify signals, and optimize MIMO and waveform design.",
        "devin_body": r'''## When to use

You are applying ML to physical-layer and MAC-layer wireless problems such as channel estimation, modulation recognition, MIMO, and spectrum sensing.

## Usage

- Classify modulation and detect signals with SigKit.
- Estimate MIMO-OFDM channels with diffusion or deep learning.
- Optimize beamforming and precoding.
- Detect anomalies and interference in RF data.
- Build over-the-air datasets with GNU Radio.

## Steps

1. Collect IQ samples, channel measurements, or SDR data.
2. Engineer RF features and impairments.
3. Train modulation, channel, or waveform models.
4. Validate over-the-air or with simulated channels.
5. Deploy on SDR or baseband platforms.

## Code pattern

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# IQ-sample features for modulation classification
iq_features = np.hstack([np.mean(IQ, axis=1), np.std(IQ, axis=1)])
X = pd.DataFrame(iq_features, columns=[f"f{i}" for i in range(iq_features.shape[1])])
y = labels

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Wireless data is highly domain-specific; include channel conditions, SNR, and hardware effects.
- Use physics-informed models or data augmentation to improve generalization across SNRs.
- Validate on over-the-air or high-fidelity simulator data, not just AWGN.
- Pay attention to standards (3GPP, IEEE 802.11) when deploying learned functions.

## Verification

1. Train a modulation classifier and report accuracy across SNR levels.
2. Build a learned channel estimator and compare to a pilot-based least-squares baseline.
3. Demonstrate spectrum sensing on a real or emulated RF dataset.
''',
        "references": ["https://arxiv.org/abs/1809.08707", "https://arxiv.org/abs/2407.11595", "https://arxiv.org/abs/2001.04561", "https://arxiv.org/abs/2007.05952"],
    },
    {
        "name": "ai-for-network-management",
        "title": "AI for Network Management",
        "description": "Use AIOps to correlate alerts, find root causes, and automate network remediation.",
        "devin_body": r'''## When to use

You are managing enterprise, cloud, or telecom networks and want to automate monitoring, troubleshooting, configuration, and capacity planning.

## Usage

- Correlate multi-source alerts with BigPanda or Moogsoft.
- Build IT/network knowledge graphs.
- Predict and prevent incidents with anomaly detection.
- Automate runbooks and remediation actions.
- Track SLA, MTTR, and change impact.

## Steps

1. Ingest logs, metrics, events, and topology data.
2. Build CMDB/knowledge graph and normalize alerts.
3. Train correlation, RCA, and prediction models.
4. Deploy AIOps playbooks and automation.
5. Measure incident response and refine.

## Code pattern

```python
from sklearn.ensemble import IsolationForest
import pandas as pd

# Network metrics: CPU, link utilization, error counters, latency
X = df[["cpu_pct", "link_util", "errors", "latency_ms"]]

clf = IsolationForest(contamination=0.05, random_state=42)
df["anomaly_score"] = clf.decision_function(X)
```

## Tuning notes

- Use time-aware splits and event correlation to avoid label leakage.
- Reduce alert fatigue by clustering and prioritizing anomalies.
- Combine structured telemetry with LLMs for triage and runbook generation.
- Ensure safe control boundaries before automating configuration changes.

## Verification

1. Build an anomaly detector on network telemetry and evaluate precision-recall.
2. Correlate alerts into incident clusters and compare to manual ticket data.
3. Prototype a configuration-risk classifier and test on historical change records.
''',
        "references": ["https://arxiv.org/abs/2507.12472v1", "https://arxiv.org/abs/2406.11213", "https://arxiv.org/abs/2605.12729v2", "https://arxiv.org/abs/2404.01363"],
    },
]