SKILLS = [
    {
        "name": "ai-for-cybersecurity",
        "title": "AI for Cybersecurity",
        "description": "Network intrusion detection, malware and phishing classification, "
                       "vulnerability discovery, adversarial ML, and SOC automation.",
        "devin_body": r'''
## When to use

You are defending networks, endpoints, or cloud environments against
intrusions, malware, phishing, or adversarial ML attacks.

## Key concepts

- **AI-driven intrusion detection**: anomaly and signature detection on
  network and host telemetry.
- **Malware and phishing classification**: static/dynamic analysis and
  URL or email content models.
- **Vulnerability discovery**: ML-assisted fuzzing, static analysis, and
  patch prioritization.
- **Adversarial ML**: evasion, poisoning, model extraction, and
  hardening defenses.
- **SOC automation**: triage, correlation, and response playbooks with
  LLM agents.

## Code pattern

```python
from sklearn.ensemble import IsolationForest

# Anomaly detector on network-flow features
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X_train)
scores = model.decision_function(X_test)
```

## Tuning notes

- Use chronological train/test splits to prevent label leakage in logs.
- Balance extreme class imbalance with cost-sensitive learning.
- Validate against adversarial evasion on a holdout attack set.
- Combine rule-based and ML detectors for auditable alerts.

## Verification

1. Train a network-IDS model and report precision-recall at the top 1%.
2. Build a phishing URL classifier and evaluate on a time-separated test.
3. Run an adversarial-evasion test against a trained malware detector.
''',
        "references": [
            "https://www.mdpi.com/1424-8220/26/5/1518",
            "https://arxiv.org/abs/2405.04760",
            "https://arxiv.org/abs/2601.05293",
            "https://attack.mitre.org/",
        ],
    },
    {
        "name": "ai-for-physical-security",
        "title": "AI for Physical Security",
        "description": "Perimeter intrusion detection, access control analytics, "
                       "video anomaly detection, and AI-augmented guard operations.",
        "devin_body": r'''
## When to use

You are protecting facilities, people, and assets with cameras, sensors,
and access-control systems that must detect and respond to anomalies.

## Key concepts

- **Video anomaly detection**: unusual behaviors, loitering, line-crossing,
  and abandoned objects.
- **Access control analytics**: tailgating, credential sharing, and
  unauthorized zone entry.
- **Perimeter and seismic sensing**: multi-modal fusion for intrusion
  detection.
- **Guard force augmentation**: AI-generated incident summaries and
  alarm triage.

## Code pattern

```python
from sklearn.ensemble import IsolationForest

# Train on surveillance feature vectors (motion, object counts, etc.)
clf = IsolationForest(contamination=0.02, random_state=42)
clf.fit(X_train)
anomaly_scores = clf.decision_function(X_test)
```

## Tuning notes

- Calibrate false-alarm rates to avoid alert fatigue in 24/7 operations.
- Respect privacy; blur faces and limit retention where not required.
- Combine edge and cloud processing for latency and cost trade-offs.
- Test under varying lighting, weather, and camera angles.

## Verification

1. Detect anomalous events in a surveillance video dataset and report AUC.
2. Build an access-control anomaly detector and measure precision@k.
3. Compare edge-only vs cloud-only latency on a live camera feed.
''',
        "references": [
            "https://arxiv.org/html/2409.05383",
            "https://arxiv.org/html/2508.14203",
            "https://doi.org/10.1109/access.2023.3321800",
            "https://arxiv.org/html/2405.19387v1",
        ],
    },
    {
        "name": "ai-for-search-and-rescue",
        "title": "AI for Search and Rescue",
        "description": "UAV and robot search planning, victim detection from imagery "
                       "and sensors, and SAR mission coordination with AI.",
        "devin_body": r'''
## When to use

You are coordinating air, ground, or maritime search-and-rescue missions
in GNSS-denied, cluttered, or time-critical environments.

## Key concepts

- **Search planning**: coverage path planning, information-theoretic
  search, and multi-UAV task allocation.
- **Victim detection**: vision, thermal, and acoustic detection of
  persons and distress signals.
- **Rescue robotics**: autonomous navigation, manipulation, and
  payload delivery in rough terrain.
- **Human-robot teaming**: shared situational awareness and safe
  proximity navigation.

## Code pattern

```python
import numpy as np

# Score grid cells by probability of detection and accessibility
prior = np.ones_like(terrain_map) / terrain_map.size
likelihood = detectability_map * prior
best_cell = np.unravel_index(likelihood.argmax(), likelihood.shape)
```

## Tuning notes

- Integrate heterogeneous sensors (RGB, thermal, LiDAR, sound) with
  care for calibration and time synchronization.
- Plan for limited battery, communication range, and weather constraints.
- Use simulation environments to stress-test before field deployment.
- Include human override for safety-critical decisions.

## Verification

1. Run a coverage planner in a high-fidelity SAR simulation.
2. Evaluate victim-detection accuracy on a held-out aerial image set.
3. Compare a learned task-allocation policy to a greedy baseline.
''',
        "references": [
            "https://arxiv.org/abs/2502.20326",
            "https://arxiv.org/html/2503.02465v2",
            "https://arxiv.org/html/2601.14973v2",
            "https://arxiv.org/abs/2306.02911",
        ],
    },
    {
        "name": "ai-for-emergency-management",
        "title": "AI for Emergency Management",
        "description": "Incident prediction, resource allocation, damage assessment, "
                       "and generative AI for emergency operations.",
        "devin_body": r'''
## When to use

You are preparing for, responding to, or recovering from natural or
human-made incidents that require fast coordination of people and assets.

## Key concepts

- **Incident prediction and forecasting**: spatiotemporal models for
  calls, accidents, fires, and service demand.
- **Resource dispatch and allocation**: optimization under uncertainty
  for ambulances, fire, and police units.
- **Damage assessment**: remote sensing, social media, and generative AI
  for rapid situational awareness.
- **Crisis informatics**: extracting needs, offers, and actionable
  information from large message streams.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingRegressor

# Predict incident counts by time, location, and weather features
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)
forecast = model.predict(X_test)
```

## Tuning notes

- Use time-based validation; future data must not leak into training.
- Combine model predictions with human judgment in EOC workflows.
- Tune dispatch objectives for equity and response-time trade-offs.
- Evaluate generative outputs for accuracy before public distribution.

## Verification

1. Build an incident-prediction model and measure RMSE on rolling
   cross-validation.
2. Optimize a dispatch schedule and compare response times to baseline.
3. Generate a damage-assessment summary and verify against ground truth.
''',
        "references": [
            "https://arxiv.org/pdf/2505.08202",
            "https://doi.org/10.48550/arxiv.2501.06932",
            "https://arxiv.org/html/2306.10068",
            "https://link.springer.com/article/10.1007/s11069-025-07667-5",
        ],
    },
    {
        "name": "ai-for-border-security",
        "title": "AI for Border Security",
        "description": "Biometric identity verification, contraband and anomaly "
                       "detection, and multi-sensor fusion at ports of entry.",
        "devin_body": r'''
## When to use

You are securing air, land, and sea borders with biometric checks,
cargo inspection, and surveillance of people, vehicles, and vessels.

## Key concepts

- **Biometric verification**: facial and iris matching for entry/exit
  and identity confirmation.
- **Cargo and baggage screening**: X-ray and multi-spectral anomaly
  detection for contraband.
- **Perimeter and maritime surveillance**: radar, video, and seismic
  sensor fusion.
- **Risk-based targeting**: machine learning for traveler and shipment
  risk scoring.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Risk score for travelers/shipments based on historical patterns
clf = RandomForestClassifier(class_weight="balanced", random_state=42)
clf.fit(X_train, y_train)
risk_score = clf.predict_proba(X_test)[:, 1]
```

## Tuning notes

- Ensure biometric systems operate at very low false-match rates and
  are audited for demographic fairness.
- Balance security gains with traveler facilitation and privacy rights.
- Use multi-modal sensor fusion to reduce false alarms in harsh
  environments.
- Validate against adversarial evasion and presentation attacks.

## Verification

1. Evaluate a biometric matcher on an in-the-wild dataset and report
   FMR/FNMR at an operating threshold.
2. Detect anomalies in cargo X-ray images and compare to officer baselines.
3. Test a risk-scoring model for disparate impact across groups.
''',
        "references": [
            "https://www.dhs.gov/ai/use-case-inventory/cbp",
            "https://www.cbp.gov/travel/biometrics/overview",
            "https://arxiv.org/html/2511.14698",
            "https://ar5iv.labs.arxiv.org/html/2004.13076",
            "https://arxiv.org/html/2607.13515",
        ],
    },
    {
        "name": "ai-for-surveillance-ethics",
        "title": "AI for Surveillance Ethics",
        "description": "Fairness, privacy, proportionality, and algorithmic "
                       "accountability for AI surveillance and facial recognition.",
        "devin_body": r'''
## When to use

You are designing, deploying, or auditing surveillance or biometric
systems where privacy, human rights, and societal trust are at stake.

## Key concepts

- **Proportionality and necessity**: balancing security gains against
  individual rights and freedoms.
- **Algorithmic fairness**: auditing demographic disparities in
  detection and recognition rates.
- **Privacy by design**: data minimization, retention limits, and
  anonymization.
- **Transparency and accountability**: explainability, audit trails,
  and redress mechanisms.
- **Regulatory compliance**: AI Act, biometric data rules, and sector
  guidelines.

## Code pattern

```python
from sklearn.metrics import classification_report

# Audit subgroup performance for a recognition or detection model
print(classification_report(y_true, y_pred, target_names=groups))
```

## Tuning notes

- Conduct independent audits before and after deployment.
- Document the purpose, data sources, and decision logic for oversight.
- Implement human-in-the-loop review for high-stakes identifications.
- Apply the least intrusive means to achieve a legitimate security goal.

## Verification

1. Audit a facial-recognition model for equalized odds across groups.
2. Write a proportionality assessment for a proposed surveillance use.
3. Verify that audit logs and deletion policies meet the stated policy.
''',
        "references": [
            "https://arxiv.org/html/2402.05731",
            "https://dl.acm.org/doi/10.1145/3375627.3375820",
            "https://arxiv.org/html/2503.04866v1",
            "https://arxiv.org/html/2606.07628v1",
            "https://www.frontiersin.org/articles/10.3389/fdata.2024.1337465",
        ],
    },
    {
        "name": "ai-for-threat-intelligence",
        "title": "AI for Threat Intelligence",
        "description": "Cyber threat intelligence extraction, attribution, knowledge "
                       "graphs, and automated indicator analysis with ML and LLMs.",
        "devin_body": r'''
## When to use

You are turning large volumes of security reports, logs, and dark-web
sources into structured, actionable intelligence about threats.

## Key concepts

- **Indicator extraction and normalization**: IoCs, TTPs, and
  MITRE ATT&CK mapping.
- **Threat actor attribution**: behavioral and artifact similarity
  analysis.
- **Knowledge graphs**: entity-relationship models for multi-hop
  reasoning over CTI.
- **Natural language processing**: LLM summarization, question
  answering, and report triage.
- **Prioritization and situational awareness**: risk scoring and
  alert enrichment.

## Code pattern

```python
import spacy

# Extract named entities from a threat report
nlp = spacy.load("en_core_web_sm")
doc = nlp(report_text)
entities = [(ent.text, ent.label_) for ent in doc.ents]
```

## Tuning notes

- Normalize entities to a shared taxonomy for correlation.
- Combine structured and unstructured sources; ground LLM answers in
  retrieved evidence.
- Track data provenance and confidence to avoid circular reporting.
- Automate low-confidence triage but keep analyst-in-the-loop for
  attribution.

## Verification

1. Extract IoCs from a report corpus and compare to a labeled gold set.
2. Build a CTI knowledge graph and answer multi-hop attribution queries.
3. Evaluate an LLM summarization pipeline against analyst summaries.
''',
        "references": [
            "https://arxiv.org/abs/2604.11419v1",
            "https://link.springer.com/article/10.1007/s10462-025-11338-z",
            "https://arxiv.org/abs/2603.05068v1",
            "https://arxiv.org/abs/2511.01144v1",
            "https://attack.mitre.org/",
        ],
    },
    {
        "name": "ai-for-public-safety",
        "title": "AI for Public Safety",
        "description": "Emergency call dispatch, response-time optimization, "
                       "situational awareness, and fairness-aware public safety analytics.",
        "devin_body": r'''
## When to use

You are helping police, fire, EMS, and 911 systems respond faster and
more equitably while respecting civil liberties.

## Key concepts

- **Call triage and dispatch**: natural-language and audio classifiers
  for priority and unit assignment.
- **Spatiotemporal incident prediction**: forecasting call volumes and
  demand hotspots.
- **Response optimization**: patrol, unit positioning, and routing
  under constraints.
- **Situational awareness**: video, social media, and IoT fusion for
  live events.
- **Fairness and oversight**: auditing for biased deployment and
  feedback loops.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Classify 911 call priority from text and metadata
clf = RandomForestClassifier(class_weight="balanced", random_state=42)
clf.fit(X_train, y_train)
priority = clf.predict(X_test)
```

## Tuning notes

- Validate on chronological splits to avoid leakage from future events.
- Balance response time with equitable coverage across neighborhoods.
- Use interpretable models where decisions affect policing or service.
- Continuously audit for feedback loops between predictions and patrol.

## Verification

1. Train a call-priority classifier and report macro-F1 across call types.
2. Optimize unit positioning and measure response-time improvement.
3. Audit a hotspot-prediction model for demographic fairness.
''',
        "references": [
            "https://arxiv.org/html/2409.02246",
            "https://arxiv.org/pdf/2106.08307",
            "https://arxiv.org/html/2408.04193",
            "https://doi.org/10.48550/arxiv.2604.18644",
        ],
    },
    {
        "name": "ai-for-cyber-physical-security",
        "title": "AI for Cyber-Physical Security",
        "description": "Securing industrial control systems, SCADA anomaly detection, "
                       "physical invariants, and cross-layer intrusion detection.",
        "devin_body": r'''
## When to use

You are protecting power, water, manufacturing, or transport systems
where IT, OT, and physical processes must be defended together.

## Key concepts

- **ICS/SCADA security**: network and process telemetry monitoring.
- **Anomaly detection with invariants**: learning normal physical and
  logical relationships in sensor data.
- **Attack detection and attribution**: multi-stage cyber-physical
  attack chains and provenance analysis.
- **Resilient control**: safe fallback and recovery for compromised
  processes.
- **Digital twins**: simulation-based stress testing and response
  planning.

## Code pattern

```python
import numpy as np
from scipy.stats import zscore

# Detect physical-process anomalies from normalized sensor residuals
residuals = y_true - y_predicted
flags = np.abs(zscore(residuals)) > 3.5
```

## Tuning notes

- Model both network and physical behavior; attackers may hide in one
  layer while affecting the other.
- Use physics-aware features and known invariants to reduce false positives.
- Validate against labeled ICS/CPS datasets such as SWaT or WADI.
- Plan safe fallback procedures before deploying automated responses.

## Verification

1. Run an anomaly detector on a labeled CPS dataset and report F1 and FPR.
2. Identify a multi-stage attack chain using process and network logs.
3. Verify that a control fallback keeps the process within safe limits.
''',
        "references": [
            "https://arxiv.org/html/2411.10918",
            "https://arxiv.org/html/2607.05989",
            "https://arxiv.org/abs/2603.16588v1",
            "https://arxiv.org/html/2507.14387",
            "https://arxiv.org/html/2603.10676v2",
        ],
    },
    {
        "name": "ai-for-crisis-communication",
        "title": "AI for Crisis Communication",
        "description": "Automated situational awareness, rumor detection, "
                       "multilingual crisis summarization, and public information chatbots.",
        "devin_body": r'''
## When to use

You must quickly extract, verify, and disseminate accurate information
during a disaster, emergency, or rapidly evolving public event.

## Key concepts

- **Situational awareness from social media**: event detection,
  classification, and geolocation.
- **Rumor and misinformation detection**: claim verification and source
  credibility scoring.
- **Multilingual and cross-cultural communication**: machine
  translation and summarization for diverse populations.
- **Chatbots and public alerts**: LLM-driven, retrieval-grounded
  response systems.
- **Needs-offers matching**: connecting requests and resources during
  a crisis.

## Code pattern

```python
from transformers import pipeline

# Classify crisis-related social media posts by information type
classifier = pipeline(
    "text-classification",
    model="your-crisis-bert",
)
labels = classifier(posts)
```

## Tuning notes

- Integrate uncertainty signals; distinguish confirmed reports from
  unverified claims.
- Ground LLM responses in approved sources to prevent hallucination.
- Support low-connectivity and low-literacy audiences with simple
  formats and multiple languages.
- Coordinate messaging with official channels to avoid confusion.

## Verification

1. Classify social media posts into situational categories and report
   F1 per class.
2. Detect a rumor outbreak and compare against fact-checked reports.
3. Generate multilingual crisis briefs and evaluate clarity with
   domain experts.
''',
        "references": [
            "https://arxiv.org/html/2605.00829",
            "https://arxiv.org/pdf/2504.00046",
            "https://arxiv.org/html/2402.10908",
            "https://arxiv.org/html/2405.11897",
            "https://ojs.iscram.org/index.php/Proceedings/article/view/152",
        ],
    },
    {
        "name": "ai-for-resilience",
        "title": "AI for Resilience",
        "description": "Critical infrastructure resilience, disaster recovery planning, "
                       "stress testing, and learning-based restoration optimization.",
        "devin_body": r'''
## When to use

You need to prepare critical systems and communities to absorb shocks,
recover quickly, and adapt after disruptions.

## Key concepts

- **Resilience metrics**: robustness, redundancy, resourcefulness, and
  rapidity.
- **Critical infrastructure interdependencies**: power, water, telecom,
  and transport network modeling.
- **Recovery optimization**: resource allocation and restoration
  sequencing under uncertainty.
- **Scenario and stress testing**: simulation, digital twins, and
  counterfactual analysis.
- **Learning for adaptation**: online learning and reinforcement
  learning for recovery policies.

## Code pattern

```python
import networkx as nx

# Compute a basic resilience indicator from a critical-infrastructure
# graph after component failure
G = nx.read_gml("infrastructure.gml")
nodes_lost = len(G) - len(list(nx.connected_components(G))[0])
```

## Tuning notes

- Capture interdependencies across sectors; failures cascade.
- Include equity metrics so recovery does not leave vulnerable groups
  behind.
- Validate simulation models with historical disruption events.
- Maintain human oversight for life-safety restoration decisions.

## Verification

1. Model cascading failures across an interdependent network.
2. Optimize a restoration schedule and compare to a greedy baseline.
3. Stress-test a recovery plan against a range of disruption scenarios.
''',
        "references": [
            "https://doi.org/10.34133/cesci.0013",
            "https://doi.org/10.3390/su18115297",
            "https://ieomsociety.org/proceedings/2024dubai/109.pdf",
            "https://doi.org/10.6028/NIST.RB.6",
            "https://www.dhs.gov/sites/default/files/2024-04/24_0426_dhs_ai-ci-safety-security-guidelines-508c.pdf",
        ],
    },
    {
        "name": "ai-for-disaster-preparedness",
        "title": "AI for Disaster Preparedness",
        "description": "Hazard risk assessment, early warning systems, scenario "
                       "simulation, and mitigation planning with AI.",
        "devin_body": r'''
## When to use

You are working before a disaster strikes to assess risk, issue timely
warnings, and plan mitigations that reduce harm.

## Key concepts

- **Hazard and risk modeling**: flood, fire, earthquake, and weather
  risk estimation.
- **Early warning systems**: multi-hazard forecasting, trigger models,
  and dissemination.
- **Pre-event impact simulation**: building-level damage and
  population-exposure estimation.
- **Preparedness planning**: evacuation routes, shelter allocation, and
  resource pre-positioning.
- **Generative AI for scenarios**: LLM-based tabletop exercises and
  public communication.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingRegressor

# Predict building-level damage risk from hazard and structure features
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)
risk = model.predict(X_test)
```

## Tuning notes

- Combine physical models, remote sensing, and historical event data.
- Evaluate warning systems by lead time, false-alarm rate, and
  protective-action uptake.
- Use probabilistic and ensemble forecasts to communicate uncertainty.
- Co-design tools with communities to ensure trust and accessibility.

## Verification

1. Train a hazard-risk model and validate against a historical event.
2. Simulate an early warning pipeline and measure end-to-end latency.
3. Compare an AI-preparedness plan to a status-quo plan under stress
   tests.
''',
        "references": [
            "https://arxiv.org/html/2607.24588",
            "https://arxiv.org/pdf/2601.18308",
            "https://arxiv.org/html/2506.06355",
            "https://ar5iv.labs.arxiv.org/html/2112.13465",
            "https://www.undrr.org/publication/leveraging-ai-enhance-multi-hazard-early-warning-systems",
        ],
    },
]
