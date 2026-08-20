SKILLS = [
    {
        "name": "ai-for-chemistry",
        "title": "AI for Chemistry",
        "description": "Molecular property prediction, generative chemistry, reaction prediction, and cheminformatics with deep learning.",
        "devin_body": r'''
## When to use

You are predicting molecular properties, designing new molecules, or forecasting chemical reactions.

## Key concepts

- **Molecular fingerprints / SMILES / SELFIES**: text or vector representations of molecules.
- **Graph neural networks for molecules**: GNNs operate on atom-bond graphs.
- **Generative chemistry**: VAE, diffusion, or flow models for molecule design.
- **Reaction prediction**: models that predict products from reactants and reagents.
- **Datasets**: QM9, ZINC, ChEMBL, PubChem.

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
            "https://www.rdkit.org/",
            "https://arxiv.org/abs/2401.14876",
            "https://doi.org/10.1038/s41586-023-06197-z"
        ],
    },
    {
        "name": "ai-for-biology",
        "title": "AI for Biology",
        "description": "Deep learning for genomics, transcriptomics, proteomics, cell imaging, and biological sequence modeling.",
        "devin_body": r'''
## When to use

You are analyzing biological sequences, microscopy images, single-cell data, or molecular structures.

## Key concepts

- **Sequence models for DNA/RNA/protein**: CNNs, transformers, and k-mer embeddings.
- **Foundation models for biology**: ESM, AlphaFold, scBERT, HyenaDNA.
- **Single-cell analysis**: cell type classification, perturbation prediction, trajectory inference.
- **Biomedical image analysis**: segmentation, classification, and phenotyping.

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
        "description": "Neural operators, surrogate models, and learned emulators for partial differential equations and physical systems.",
        "devin_body": r'''
## When to use

You want to speed up expensive physics simulations or learn emulators from data.

## Key concepts

- **Neural operators**: map between infinite-dimensional function spaces (FNO, DeepONet).
- **Surrogate models**: ML approximations of costly solvers.
- **Physics-informed neural networks (PINNs)**: embed PDE constraints in loss.
- **Digital twins**: online-learned models coupled to sensors.

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
        "description": "Machine learning for quantum state tomography, variational quantum algorithms, quantum control, and error mitigation.",
        "devin_body": r'''
## When to use

You are designing variational circuits, optimizing quantum controls, or mitigating errors in NISQ devices.

## Key concepts

- **Variational Quantum Eigensolver (VQE)**: hybrid quantum-classical optimization.
- **Quantum Neural Networks**: parameterized circuits as models.
- **Quantum control with RL/optimization**: pulse shaping and gate design.
- **Error mitigation**: zero-noise extrapolation, probabilistic error cancellation.
- **Simulators**: Qiskit, PennyLane, Cirq, cuQuantum.

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
        "description": "Imitation learning, reinforcement learning, sim-to-real, and foundation models for robot manipulation and navigation.",
        "devin_body": r'''
## When to use

You are building robot perception, control, or planning systems using learning.

## Key concepts

- **Imitation learning**: behavioral cloning, DAgger.
- **Reinforcement learning for control**: PPO, SAC, MBPO.
- **Sim-to-real**: domain randomization, adaptation, distillation.
- **Foundation models for robotics**: vision-language-action models (RT-X, Open X-Embodiment).
- **ROS / Isaac Sim / PyBullet**: common robot middleware and simulators.

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
        "description": "Perception, prediction, planning, and simulation for self-driving cars and mobile robots.",
        "devin_body": r'''
## When to use

You are working on perception, motion forecasting, path planning, or end-to-end driving for autonomous vehicles.

## Key concepts

- **Perception**: 3D object detection, tracking, lane detection, segmentation.
- **Prediction**: trajectory forecasting for agents in a scene.
- **Planning**: rule-based, sampling-based, or learned planners.
- **Simulation**: CARLA, nuPlan, Waymo Open, nuScenes.
- **Safety and redundancy**: functional safety, ODD, scenario coverage.

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
        "description": "Machine learning for time-series forecasting, risk modeling, algorithmic trading, and financial NLP.",
        "devin_body": r'''
## When to use

You are building predictive models for markets, credit, fraud, or financial documents.

## Key concepts

- **Time-series forecasting**: ARIMA, Prophet, deep state-space, transformers.
- **Risk modeling**: Value-at-Risk, stress testing, default prediction.
- **Fraud detection**: anomaly detection, imbalanced classification.
- **Financial NLP**: sentiment, earnings calls, filings, FinBERT.
- **Backtesting**: avoid lookahead bias and overfitting.

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
        "description": "Personalized learning, knowledge tracing, automated assessment, and intelligent tutoring systems.",
        "devin_body": r'''
## When to use

You are building adaptive learning, student modeling, or automated grading systems.

## Key concepts

- **Knowledge tracing**: predict what skills a student has mastered (BKT, DKT).
- **Personalized recommendation**: next-item or next-exercise suggestion.
- **Automated essay / code scoring**: LLM or learned rubric scoring.
- **Learning analytics**: engagement, dropout prediction, performance dashboards.
- **Fairness**: ensure models do not disadvantage subgroups.

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
        "description": "Legal document analysis, case law retrieval, contract review, and legal reasoning benchmarks.",
        "devin_body": r'''
## When to use

You are processing contracts, statutes, case law, or legal queries with NLP.

## Key concepts

- **Legal NLP**: NER, classification, summarization, question answering.
- **Case law retrieval**: dense and sparse retrieval over court opinions.
- **Contract review**: clause extraction, risk flagging, comparison.
- **Benchmarks**: LegalBench, COLIEE, Law School Admission Test tasks.
- **Hallucination**: citations and claims must be verifiable.

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
        "description": "Digital humanities, text analysis, image restoration, and creative AI for cultural heritage.",
        "devin_body": r'''
## When to use

You are applying ML to literature, history, art, archives, or cultural heritage collections.

## Key concepts

- **Textual analysis**: stylometry, topic modeling, named entity recognition.
- **OCR and handwriting**: transcribe historical documents.
- **Image restoration and colorization**: repair and enhance artworks.
- **Multimodal collections**: align text, images, audio, and metadata.
- **Ethics and provenance**: respect copyright, indigenous data sovereignty.

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
        "description": "Music generation, transcription, recommendation, and audio processing with deep learning.",
        "devin_body": r'''
## When to use

You are generating music, transcribing audio, or building music recommendation systems.

## Key concepts

- **Symbolic music models**: transformers on MIDI, ABC notation, or piano roll.
- **Audio generation**: diffusion, VAE, GAN, and autoregressive models.
- **Source separation**: isolate vocals, drums, bass, etc.
- **Music information retrieval**: beat tracking, key detection, genre classification.
- **Copyright**: be aware of training data and output ownership.

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
        "description": "Machine learning for digital phenotyping, diagnostic support, treatment prediction, and crisis detection.",
        "devin_body": r'''
## When to use

You are building models to support mental health diagnosis, monitoring, or personalized intervention.

## Key concepts

- **Digital phenotyping**: behavior signals from phones, wearables, or speech.
- **Crisis detection**: identify self-harm or suicidal ideation in text.
- **Treatment response prediction**: predict outcomes for therapy or medications.
- **Privacy and ethics**: mental health data is highly sensitive.
- **Clinical validation**: models must be evaluated with clinical experts.

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
