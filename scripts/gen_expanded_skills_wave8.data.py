SKILLS = [
    {
        "name": "ai-for-chemistry",
        "title": "AI for Chemistry",
        "description": "Use deep learning to predict molecular properties, design novel molecules, and forecast chemical reactions and retrosynthetic routes.",
        "devin_body": r'''
## When to use

You are predicting molecular properties, designing new molecules, or forecasting chemical reactions.

## Usage

- Predict molecular properties (solubility, toxicity, binding affinity) from SMILES, SELFIES, or molecular graphs.
- Generate and optimize drug or material candidates with VAE, diffusion, or flow models.
- Propose retrosynthetic routes and reaction conditions to shorten the DMTA cycle.
- Represent molecules with SMILES, SELFIES, fingerprints, or atom-bond graphs for model input.
- Filter generated structures for chemical plausibility and synthesizability with cheminformatics tools.
- Benchmark and validate models on datasets like QM9, ZINC, ChEMBL, and PubChem.

## Steps

1. Featurize molecules (SMILES/SELFIES, fingerprints, or graph) from a chemical dataset.
2. Train or fine-tune a GNN or transformer to predict a target molecular property.
3. Generate candidate molecules with a generative or diffusion model against a desired property profile.
4. Filter candidates for chemical plausibility, synthesizability, and patentability using RDKit and retrosynthesis tools.
5. Predict reaction products or retrosynthetic routes for the most promising candidates.
6. Validate shortlisted compounds with experimental or high-fidelity computational assays.

## Code pattern

```python
import deepchem as dc
from deepchem.feat import ConvMolFeaturizer
from deepchem.models import GraphConvModel

featurizer = ConvMolFeaturizer()
loader = dc.data.CSVLoader(tasks=["task"], feature_field="smiles", featurizer=featurizer)
dataset = loader.create_dataset("data.csv")
model = GraphConvModel(n_tasks=1, mode="regression")
model.fit(dataset)
```

## Tuning notes

- Use scaffold splits for realistic generalization estimates.
- Validate generated molecules for chemical plausibility and synthesizability.
- For reaction prediction, keep atom-mapping and reaction templates in mind.

## Verification

1. Train a GNN to predict a molecular property from SMILES.
2. Generate a set of candidate molecules and filter with RDKit.
3. Predict a small reaction product and compare to known outcome.
''',
        "references": [
            "https://deepchem.io/",
            "https://github.com/rdkit/rdkit",
            "https://arxiv.org/abs/2401.14876",
            "https://doi.org/10.1038/s41586-023-06197-z"
        ],
    },
    {
        "name": "ai-for-biology",
        "title": "AI for Biology",
        "description": "Use deep learning to analyze biological sequences, single-cell and spatial omics, microscopy images, and molecular structures.",
        "devin_body": r'''
## When to use

You are analyzing biological sequences, microscopy images, single-cell data, or molecular structures.

## Usage

- Embed DNA, RNA, and protein sequences with transformer or CNN models (e.g., ESM, HyenaDNA).
- Classify cell types and infer trajectories from single-cell RNA-seq or spatial transcriptomics.
- Quantify proteins and cell phenotypes from multiplexed imaging or mass spectrometry proteomics.
- Predict protein structures and interactions from sequences (e.g., AlphaFold, ESM embeddings).
- Build disease or perturbation classifiers from multi-omics and imaging data.

## Steps

1. Load and quality-control sequence, omics, or imaging data for the target organism and tissue.
2. Featurize biological inputs (k-mers, embeddings, expression matrices, image patches).
3. Train or fine-tune a sequence, graph, or vision model for the prediction task (e.g., cell type, binding, biomarker).
4. Integrate multiple modalities (genomics, transcriptomics, proteomics, imaging) to improve robustness.
5. Control for batch effects and biological confounders with integration and harmonization methods.
6. Validate predictions with held-out patients, datasets, or expert biological annotations.

## Code pattern

```python
from transformers import EsmModel, EsmTokenizer

model = EsmModel.from_pretrained("facebook/esm2_t6_8M_UR50D")
tokenizer = EsmTokenizer.from_pretrained("facebook/esm2_t6_8M_UR50D")
inputs = tokenizer("MKTLL", return_tensors="pt")
outputs = model(**inputs)
```

## Tuning notes

- Use organism- and tissue-appropriate train/test splits.
- Single-cell models can be confounded by batch effects; use integration methods.
- Be cautious about genomic data privacy and consent.

## Verification

1. Embed a set of protein sequences and cluster by function.
2. Fine-tune a small sequence model on a binding prediction task.
3. Evaluate a cell-type classifier on a held-out patient or dataset.
''',
        "references": [
            "https://github.com/facebookresearch/esm",
            "https://www.nature.com/articles/s41586-021-03819-2",
            "https://arxiv.org/abs/2407.04446",
            "https://huggingface.co/",
            "https://www.biorxiv.org/content/10.1101/2023.01.11.523679"
        ],
    },
    {
        "name": "ai-for-physics-simulation",
        "title": "AI for Physics Simulation",
        "description": "Use neural operators and physics-informed surrogates to learn fast emulators of partial differential equations and physical systems.",
        "devin_body": r'''
## When to use

You want to speed up expensive physics simulations or learn emulators from data.

## Usage

- Train Fourier Neural Operators (FNO), DeepONet, or GNN surrogates to approximate PDE solutions.
- Embed physics constraints (PDEs, boundary conditions, conservation laws) into neural network losses (PINNs).
- Build real-time digital twins for CFD, structural mechanics, heat transfer, or additive manufacturing.
- Calibrate and update surrogates with sensor data for online monitoring and control.
- Accelerate engineering design loops with interactive, AI-powered simulation and visualization.

## Steps

1. Define the physics problem, governing PDEs, input distributions, and output quantities of interest.
2. Generate training data with a high-fidelity solver or experimental measurements across parameter ranges.
3. Build a surrogate model (FNO, DeepONet, GNN, or PINN) and train it on the generated data.
4. Validate the surrogate against the high-fidelity solver on out-of-distribution parameters and geometries.
5. Deploy the model inside a digital twin or design loop with real-time sensor feedback and uncertainty quantification.
6. Iterate: refine the surrogate with online data and retrain as the physical system or design space evolves.

## Code pattern

```python
from neuralop.models import FNO
import torch

model = FNO(n_modes=(16, 16), hidden_channels=64, in_channels=1, out_channels=1)
x = torch.randn(1, 1, 64, 64)
y = model(x)
```

## Tuning notes

- Neural operators work best when training data covers a broad distribution of inputs.
- PINNs can be hard to train for multi-scale or high-frequency problems.
- Validate against a high-fidelity solver on out-of-distribution initial conditions.

## Verification

1. Train an FNO on a 2D Darcy flow dataset.
2. Compare FNO inference time to a classical PDE solver.
3. Test generalization to unseen parameter values and geometries.
''',
        "references": [
            "https://github.com/neuraloperator/neuraloperator",
            "https://arxiv.org/abs/2010.08895",
            "https://arxiv.org/abs/2111.05512",
            "https://www.nature.com/articles/s41586-021-"
        ],
    },
    {
        "name": "ai-for-quantum-computing",
        "title": "AI for Quantum Computing",
        "description": "Use machine learning to design, optimize, and error-mitigate variational quantum algorithms and quantum control pulses.",
        "devin_body": r'''
## When to use

You are designing variational circuits, optimizing quantum controls, or mitigating errors in NISQ devices.

## Usage

- Optimize parameterized quantum circuits (VQE, QAOA) with hybrid quantum-classical loops.
- Discover high-fidelity, time-optimal control pulses for quantum gates and state preparation.
- Mitigate hardware noise with learned error models, zero-noise extrapolation, or probabilistic cancellation.
- Accelerate quantum state tomography and characterization from limited measurements.
- Benchmark and compare algorithms on simulators (Qiskit, PennyLane, Cirq) and real NISQ hardware.

## Steps

1. Encode the target problem (molecular Hamiltonian, optimization, or control target) into a quantum circuit or pulse ansatz.
2. Choose a simulator or NISQ backend and define the noise model and device constraints.
3. Optimize circuit parameters or control pulses with a classical optimizer, using parameter-shift or finite-difference gradients.
4. Apply error mitigation (ZNE, learned models, or probabilistic cancellation) to reduce noise in expectation values.
5. Verify results against exact or classically simulable baselines on small problem instances.
6. Benchmark on real hardware when feasible and iterate the ansatz, control, or mitigation strategy.

## Code pattern

```python
import pennylane as qml

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def circuit(params):
    qml.RX(params[0], wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0))

opt = qml.GradientDescentOptimizer(stepsize=0.4)
```

## Tuning notes

- Barren plateaus are a major challenge in deep quantum circuits.
- Use parameter-shift or finite-difference gradients on hardware.
- Simulators are useful; validate on real hardware when feasible.

## Verification

1. Run a VQE for a small molecule on a simulator.
2. Optimize a quantum control pulse to reach a target unitary.
3. Compare a quantum circuit output with and without error mitigation.
''',
        "references": [
            "https://pennylane.ai/",
            "https://qiskit.org/",
            "https://arxiv.org/abs/2312.06843",
            "https://developer.nvidia.com/cuquantum"
        ],
    },
    {
        "name": "ai-for-robotics",
        "title": "AI for Robotics",
        "description": "Use imitation learning, reinforcement learning, and foundation models to train robot manipulation and navigation policies that transfer from simulation to reality.",
        "devin_body": r'''
## When to use

You are building robot perception, control, or planning systems using learning.

## Usage

- Learn manipulation and navigation policies from human demonstrations or expert trajectories (imitation learning).
- Train control policies with reinforcement learning (PPO, SAC) in simulated environments.
- Close the sim-to-real gap with domain randomization, co-training, actuator gap estimation, and adaptation.
- Leverage vision-language-action (VLA) and foundation models (RT-X, GR00T, Open X-Embodiment) for generalist robot behavior.
- Integrate robot middleware and simulators (ROS, Isaac Sim, Isaac Lab, PyBullet) into data collection and deployment.

## Steps

1. Define the robot task, embodiment, sensor inputs, and action space.
2. Build or select a simulation environment and collect demonstration or replay data.
3. Train a policy with imitation learning, reinforcement learning, or a foundation VLA model.
4. Apply sim-to-real techniques (domain randomization, camera calibration, actuator modeling, co-training).
5. Validate the policy in simulation on task success, robustness, and safety metrics.
6. Deploy to the physical robot and compare real vs. simulated trajectories; iterate on the gap.

## Code pattern

```python
import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("Pendulum-v1")
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100_000)
```

## Tuning notes

- Simulators reduce cost but introduce reality gap; domain randomization helps.
- Safety is critical: use constraint-aware RL and sim validation.
- Data collection for robotics is expensive; consider offline RL and pre-training.

## Verification

1. Train PPO on a continuous control environment.
2. Fine-tune a small policy in simulation and deploy in a simple real task.
3. Compare sim and real trajectories to quantify the reality gap.
''',
        "references": [
            "https://github.com/google-deepmind/open_x_embodiment",
            "https://arxiv.org/abs/2403.08934",
            "https://stable-baselines3.readthedocs.io/",
            "https://github.com/bulletphysics/bullet3"
        ],
    },
    {
        "name": "ai-for-autonomous-vehicles",
        "title": "AI for Autonomous Vehicles",
        "description": "Use perception, motion forecasting, planning, and closed-loop simulation to develop safe autonomous driving and mobile robot systems.",
        "devin_body": r'''
## When to use

You are working on perception, motion forecasting, path planning, or end-to-end driving for autonomous vehicles.

## Usage

- Detect and track 3D objects, lanes, and road surfaces from camera, LiDAR, and radar data.
- Forecast the future trajectories of vehicles, pedestrians, and cyclists in a scene.
- Generate safe, comfortable ego-vehicle plans with rule-based, sampling-based, or learned planners.
- Test and benchmark perception, prediction, and planning in closed-loop simulation (CARLA, nuPlan, nuScenes, Waymo Open).
- Validate safety under diverse weather, lighting, geographic, and edge-case scenarios.

## Steps

1. Ingest and synchronize multi-sensor data (cameras, LiDAR, radar, GNSS/IMU, HD maps) for a driving scene.
2. Build or fine-tune perception models for 3D object detection, tracking, and lane/road segmentation.
3. Train motion-prediction models to forecast agent trajectories and interactions.
4. Implement a planner that combines predictions, map constraints, and comfort/safety objectives.
5. Evaluate the full stack in closed-loop simulation across diverse scenarios and weather/lighting conditions.
6. Track regression metrics, edge cases, and ODD coverage; iterate on data collection and model updates.

## Code pattern

```python
import av2

# Load a NuScenes-like scene and run a simple 3D detector
from nuscenes.nuscenes import NuScenes
nusc = NuScenes(version='v1.0-mini', dataroot='/data/nuscenes', verbose=False)
```

## Tuning notes

- Pay attention to class imbalance and rare objects (e.g., pedestrians, cyclists).
- Test under diverse weather, lighting, and geographic conditions.
- Use closed-loop simulation to evaluate planning, not just open-loop.

## Verification

1. Train a 2D or BEV object detector on a public AV dataset.
2. Run a simple motion-prediction baseline on nuScenes.
3. Evaluate a planner in closed-loop simulation (e.g., nuPlan).
''',
        "references": [
            "https://www.nuscenes.org/",
            "https://www.nuscenes.org/nuplan",
            "https://carla.org/",
            "https://arxiv.org/abs/2306.07962"
        ],
    },
    {
        "name": "ai-for-finance",
        "title": "AI for Finance",
        "description": "Use machine learning to forecast markets, model risk, detect fraud, and extract insight from financial documents and transactions.",
        "devin_body": r'''
## When to use

You are building predictive models for markets, credit, fraud, or financial documents.

## Usage

- Forecast prices, demand, or macro indicators with time-series and transformer models.
- Model credit, market, and operational risk (Value-at-Risk, default prediction, stress testing).
- Detect anomalous transactions, document forgeries, and fraud rings with classification, autoencoders, and LLM reasoning.
- Analyze financial documents, earnings calls, and filings with domain-tuned NLP (FinBERT, trade-assistant agents).
- Backtest strategies and reconciliation workflows with realistic costs, slippage, and temporal cross-validation.

## Steps

1. Curate financial data (prices, transactions, fundamentals, news, filings) and define the prediction or decision target.
2. Engineer temporal features and create train/validation/test splits that respect causality (no leakage).
3. Train a model for forecasting, risk scoring, fraud detection, or document classification.
4. Backtest or evaluate the model with realistic transaction costs, slippage, and temporal cross-validation.
5. Build guardrails (human-in-the-loop, explainability, audit logs) for high-stakes financial decisions.
6. Deploy with monitoring for distribution shift, market regime changes, and regulatory compliance.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Example: classify next-day direction from features
X, y = load_features_and_labels()
model = RandomForestClassifier(n_estimators=200, class_weight="balanced")
model.fit(X_train, y_train)
```

## Tuning notes

- Avoid data leakage: do not train on future information.
- Use proper temporal cross-validation.
- Transaction costs and slippage can erase paper profits.

## Verification

1. Build a time-series forecast and evaluate with temporal CV.
2. Run a backtest with realistic costs and report Sharpe ratio.
3. Classify financial news sentiment and compare to a baseline.
''',
        "references": [
            "https://arxiv.org/abs/2402.03740",
            "https://github.com/AI4Finance-Foundation/FinRobot",
            "https://huggingface.co/ProsusAI/finbert",
            "https://pyfolio.ml4trading.io/"
        ],
    },
    {
        "name": "ai-for-education",
        "title": "AI for Education",
        "description": "Use machine learning to personalize learning paths, trace student knowledge, automate assessment, and power intelligent tutoring systems.",
        "devin_body": r'''
## When to use

You are building adaptive learning, student modeling, or automated grading systems.

## Usage

- Trace student mastery of skills and predict next-exercise difficulty with BKT, DKT, and LLM-guided RL.
- Recommend personalized learning content, schedules, and interventions based on performance and engagement.
- Automate grading of essays, code, and quizzes with learned or LLM-based rubrics.
- Analyze learning analytics (engagement, dropout risk, completion) to support instructors.
- Evaluate fairness and pedagogical impact across student subgroups and educational settings.

## Steps

1. Collect and structure learning data (assessments, interactions, submissions, metadata) while protecting privacy.
2. Train a knowledge-tracing or student-embedding model to estimate current mastery and predict future performance.
3. Build an adaptive recommendation engine that selects the next problem, resource, or study plan.
4. Implement automated assessment (essay, code, or quiz scoring) aligned with human rubrics.
5. Surface dashboards and alerts for instructors on engagement, at-risk students, and learning gaps.
6. Run controlled evaluations (e.g., RCT or A/B tests) to measure learning gains, fairness, and safety.

## Code pattern

```python
import torch
import torch.nn as nn

class DKT(nn.Module):
    def __init__(self, n_questions, hidden_dim=128):
        super().__init__()
        self.lstm = nn.LSTM(n_questions, hidden_dim, batch_first=True)
        self.out = nn.Linear(hidden_dim, n_questions)

    def forward(self, x):
        h, _ = self.lstm(x)
        return torch.sigmoid(self.out(h))
```

## Tuning notes

- Student data is sensitive; protect privacy and obtain consent.
- Use temporally aware splits and avoid leakage.
- Interpretability helps teachers trust the system.

## Verification

1. Train a knowledge-tracing model on a public dataset (e.g., ASSISTments).
2. Recommend the next exercise and measure correctness improvement.
3. Evaluate an LLM grader against human rubrics.
''',
        "references": [
            "https://arxiv.org/abs/2402.12142",
            "https://sites.google.com/site/assistmentsdata/",
            "https://arxiv.org/abs/2404.03025",
            "https://pytorch.org/tutorials/"
        ],
    },
    {
        "name": "ai-for-law",
        "title": "AI for Law",
        "description": "Use NLP and retrieval systems to analyze contracts, retrieve case law, review clauses, and answer legal questions with verifiable sources.",
        "devin_body": r'''
## When to use

You are processing contracts, statutes, case law, or legal queries with NLP.

## Usage

- Classify, summarize, and extract clauses from contracts, statutes, and court opinions.
- Retrieve and synthesize case law, statutes, and regulations across jurisdictions with dense and sparse retrieval.
- Compare contracts against playbooks to flag risks, obligations, and deviations.
- Power legal research assistants that provide structured memos with verified citations.
- Benchmark legal reasoning on LegalBench, COLIEE, and jurisdiction-specific tasks.

## Steps

1. Ingest and parse legal documents (contracts, briefs, statutes, case law) into structured, retrievable chunks.
2. Build or fine-tune a legal-domain embedding or language model for classification, extraction, and summarization.
3. Implement retrieval over authoritative sources (case law, statutes, firm knowledge bases) with citation tracking.
4. Run contract review by comparing clauses to a playbook and scoring risk or missing provisions.
5. Generate research memos or answers that include verified citations and flag outdated or overruled authorities.
6. Validate outputs with legal experts, measure accuracy against annotations, and maintain auditability.

## Code pattern

```python
from transformers import pipeline

qa = pipeline("question-answering", model="pile-of-law/legalbert-large-1.7M-2")
result = qa(question="What is the governing law?", context=contract_text)
```

## Tuning notes

- Legal language is domain-specific; use legal-domain pretrained models.
- Ground outputs in cited sources; never fabricate citations.
- Bias and jurisdictional differences can affect model behavior.

## Verification

1. Fine-tune a legal document classifier on a public dataset.
2. Build a clause-extraction pipeline and compare to manual annotations.
3. Test a legal QA system on a fact-based question with a known case.
''',
        "references": [
            "https://arxiv.org/abs/2403.03873",
            "https://arxiv.org/abs/2404.05279",
            "https://case.law/",
            "https://huggingface.co/pile-of-law/legalbert-large-1.7M-2"
        ],
    },
    {
        "name": "ai-for-arts-humanities",
        "title": "AI for Arts and Humanities",
        "description": "Use machine learning to transcribe, restore, analyze, and enrich cultural heritage and humanities collections.",
        "devin_body": r'''
## When to use

You are applying ML to literature, history, art, archives, or cultural heritage collections.

## Usage

- Transcribe printed and handwritten historical documents with OCR/HTR and LLM post-correction.
- Restore, colorize, and enhance degraded images, artworks, and photographs.
- Analyze text corpora with stylometry, topic modeling, named-entity recognition, and sentiment analysis.
- Link and align multimodal collections (text, images, audio, metadata) for searchable digital archives.
- Address ethics, provenance, copyright, and indigenous data sovereignty in digital humanities projects.

## Steps

1. Digitize and preprocess source material (scans, photos, audio, metadata) for quality and consistency.
2. Train or apply OCR/HTR and image restoration models adapted to historical fonts, layouts, and degradation.
3. Extract named entities, topics, and stylistic patterns from transcribed texts.
4. Build multimodal indexes that link images, transcriptions, audio, and contextual metadata.
5. Enrich records with crowdsourced or expert annotations and reconcile errors through human-in-the-loop review.
6. Publish or archive the corpus with clear provenance, rights metadata, and access controls.

## Code pattern

```python
import pytesseract
from PIL import Image

text = pytesseract.image_to_string(Image.open("manuscript.jpg"), lang="eng")
print(text)
```

## Tuning notes

- Historical fonts and layouts often require specialized OCR training.
- Metadata and context matter as much as model predictions.
- Consider human-in-the-loop review for cultural sensitivity.

## Verification

1. OCR a set of historical pages and measure character accuracy.
2. Train a topic model on a corpus of historical texts.
3. Colorize or restore a small set of images and get expert review.
''',
        "references": [
            "https://arxiv.org/abs/2403.05055",
            "https://github.com/tesseract-ocr/tesseract",
            "https://arxiv.org/abs/2401.05889",
            "https://programminghistorian.org/"
        ],
    },
    {
        "name": "ai-for-music",
        "title": "AI for Music",
        "description": "Use deep learning to generate music, transcribe audio, recommend tracks, and process audio signals.",
        "devin_body": r'''
## When to use

You are generating music, transcribing audio, or building music recommendation systems.

## Usage

- Generate symbolic music (MIDI, ABC) or audio from text, style, or melodic prompts with transformer, diffusion, or GAN models.
- Transcribe melodies, chords, beats, and instruments from audio into symbolic notation.
- Recommend tracks and playlists from listening history, natural-language prompts, and catalog embeddings.
- Separate and process audio sources (vocals, drums, bass, other) with dedicated models.
- Track provenance and rights for AI-generated or assisted music before distribution.

## Steps

1. Curate audio or symbolic datasets and define the creative or analytical goal (generation, transcription, recommendation).
2. Train or select a model (transformer, diffusion, VAE, GAN, or MIR classifier) for the target task.
3. Generate, transcribe, classify, or separate audio and post-process for quality and style consistency.
4. Evaluate outputs against ground-truth labels, reference tracks, or perceptual listening tests.
5. Handle rights, provenance, and AI-disclosure metadata before publishing or distribution.
6. Iterate on prompts, conditioning, and model size to improve coherence, fidelity, and user satisfaction.

## Code pattern

```python
from transformers import AutoProcessor, AutoModel

processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = AutoModel.from_pretrained("facebook/musicgen-small")
inputs = processor(text=["upbeat electronic music"], return_tensors="pt")
audio = model.generate(**inputs, max_new_tokens=512)
```

## Tuning notes

- Audio models need large compute; start with small models.
- Long coherence is harder than short loops; use structure prompts.
- Validate perceptual quality with human listening tests.

## Verification

1. Generate a 10-second music clip from a text prompt.
2. Transcribe a simple melody and compare to ground truth.
3. Classify a set of tracks by genre and compare to labels.
''',
        "references": [
            "https://github.com/facebookresearch/audiocraft",
            "https://arxiv.org/abs/2408.08228",
            "https://magenta.tensorflow.org/",
            "https://librosa.org/doc/latest/index.html"
        ],
    },
    {
        "name": "ai-for-psychiatry-mental-health",
        "title": "AI for Psychiatry and Mental Health",
        "description": "Use machine learning and sensing to support mental-health monitoring, diagnostic decision support, treatment prediction, and crisis detection.",
        "devin_body": r'''
## When to use

You are building models to support mental health diagnosis, monitoring, or personalized intervention.

## Usage

- Detect symptom changes and crisis risk from smartphone, wearable, speech, text, and EHR signals.
- Predict treatment response to medications or therapy from clinical notes and structured data.
- Augment clinical decision support and documentation while preserving clinician oversight.
- Build conversational and digital therapeutic agents that deliver CBT, skills training, and triage.
- Evaluate safety, bias, privacy, and regulatory compliance before deployment in clinical settings.

## Steps

1. Collect and harmonize multimodal data (wearables, app usage, audio, EHR, clinical notes) with consent and governance.
2. Engineer behavioral and clinical features that capture symptom trajectories, sleep, activity, and mood.
3. Train classifiers or survival models to predict diagnosis, treatment response, or imminent crisis.
4. Integrate model outputs into clinician-facing dashboards or decision-support tools with human oversight.
5. Validate predictions against clinical expert judgment, structured outcomes, and representative populations.
6. Monitor for algorithmic bias, privacy breaches, and safety events; iterate under regulatory and ethical review.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingClassifier

# Example: classify crisis risk from textual features
model = GradientBoostingClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Tuning notes

- High-stakes predictions require human oversight and explainability.
- Avoid stigmatizing labels; use inclusive and representative data.
- Follow regulatory and institutional review requirements.

## Verification

1. Build a classifier for depression screening on a public dataset.
2. Analyze smartphone sensor features for sleep or activity patterns.
3. Have a clinician review model outputs for safety and utility.
''',
        "references": [
            "https://arxiv.org/abs/2401.09392",
            "https://arxiv.org/abs/2404.15239",
            "https://www.nature.com/articles/s41746-023-",
            "https://digitalphenotyping.com/"
        ],
    },
]
