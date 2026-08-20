SKILLS = [
    {
        "name": "battery-materials-ml",
        "title": "Battery Materials and Energy Storage ML",
        "description": "GNNs, Gaussian processes, and high-throughput screening for battery materials, redox flow batteries, and carbon capture solvents.",
        "devin_body": '''
## When to use

You are using ML to discover or optimize battery materials, electrolytes, or energy storage systems.

## Key concepts

- **GNNs for materials**: predict redox potentials, ionic conductivity, stability.
- **Gaussian process regression**: small-data screening with uncertainty.
- **High-throughput DFT**: train on computed properties, screen millions of candidates.
- **Carbon capture solvents**: ML for CO2 binding energy, viscosity, degradation.
- **Datasets**: Materials Project, OQMD, PubChem, battery-specific datasets.

## Code pattern

```python
from dgl import DGLGraph
import torch

# GNN predicting a battery property
model = GNN(in_feats=10, hidden_feats=64, n_tasks=1)
model = model.to('cuda')
```

## Tuning notes

- Use crystal graph convolutions (CGCNN, MEGNet, ALIGNN) for periodic structures.
- Transfer learning from Materials Project to battery datasets.
- Use uncertainty to guide expensive experiments.

## Verification

1. Train a GNN on a battery property and compare MAE to a random forest baseline.
2. Screen 10k candidates and verify top candidates with DFT/experiment.
3. Check model uncertainty correlates with prediction error.
''',
        "references": [
            "https://pubs.acs.org/doi/full/10.1021/jacsau.5c00526",
            "https://www.frontiersin.org/journals/environmental-science/articles/10.3389/fenvs.2023.1204690/full",
            "https://materialsproject.org/"
        ],
    },
    {
        "name": "renewable-energy-forecasting",
        "title": "Renewable Energy Forecasting and Grid Optimization",
        "description": "Spatio-temporal diffusion, FNO, attention, and RL for solar/wind forecasting and energy dispatch.",
        "devin_body": '''
## When to use

You are forecasting solar/wind power or optimizing energy systems with ML.

## Key concepts

- **Solar/wind forecasting**: time-series, spatio-temporal diffusion, FNO, transformers.
- **Grid optimization**: unit commitment, economic dispatch, RL for battery management.
- **Carbon capture scheduling**: integrate forecasts with equipment control.
- **Datasets**: ERA5, NREL, Open Power System Data.

## Code pattern

```python
import torch
from neuralop.models import FNO

fno = FNO(n_modes=(16, 16), hidden_channels=64, in_channels=3, out_channels=1)
fno = fno.to('cuda')
```

## Tuning notes

- Use historical weather and satellite data as inputs.
- Probabilistic forecasts are often required for grid planning.
- RL can reduce operational regret by 76-93% in some battery dispatch tasks.

## Verification

1. Train a wind/solar forecasting model and compare RMSE to persistence baseline.
2. Run an RL battery dispatch simulation and measure cost reduction.
3. Backtest on a held-out year of data.
''',
        "references": [
            "https://arxiv.org/abs/2509.06925",
            "https://www.mdpi.com/2071-1050/18/2/738",
            "https://www.nrel.gov/"
        ],
    },
    {
        "name": "agritech-phenotyping",
        "title": "Agritech and Plant Phenotyping",
        "description": "UAV/drone imaging, vision-language models, yield estimation, disease detection, and crop monitoring on GPU.",
        "devin_body": '''
## When to use

You are applying ML to agriculture: crop yield, disease, pest, or phenotype analysis.

## Key concepts

- **UAV/drone imaging**: RGB, multispectral, hyperspectral, thermal.
- **Phenotyping**: plant height, biomass, head count, disease score.
- **Vision-language models**: PaliGemma, Syngenta Gemma for field reports.
- **Datasets**: PlantVillage, UAV crop datasets, Global Wheat Head Detection.

## Code pattern

```python
from transformers import PaliGemmaForConditionalImageGeneration, PaliGemmaProcessor

model = PaliGemmaForConditionalImageGeneration.from_pretrained("...")
inputs = processor(images=img, text="count wheat heads").to('cuda')
```

## Tuning notes

- Use NDVI and other vegetation indices from multispectral sensors.
- Class imbalance is common; use focal loss or oversampling.
- Georeference outputs for precision agriculture maps.

## Verification

1. Train a wheat head detector and compare F1 to published baselines.
2. Estimate yield for a genotype and compare to harvest measurements.
3. Run inference on drone imagery and visualize disease maps.
''',
        "references": [
            "https://link.springer.com/article/10.1007/s11119-026-10371-4",
            "https://deepmind.google/models/gemma/gemmaverse/syngenta/",
            "https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1554193/full"
        ],
    },
    {
        "name": "lab-robotics-digital-twins",
        "title": "Laboratory Robotics and Digital Twins",
        "description": "MATTERIX, LucidGrasp, 6D pose, sim-to-real, and digital twins for autonomous science labs.",
        "devin_body": '''
## When to use

You are automating a wet lab with robots and want to use vision, simulation, and digital twins.

## Key concepts

- **Lab digital twins**: MATTERIX, Pipette; photorealistic rendering + physics (PhysX).
- **6D pose estimation**: LucidGrasp for transparent labware.
- **Sim-to-real**: domain randomization, synthetic data.
- **Embodied AI**: robotic sample handling, liquid transfer, colony picking.

## Code pattern

```python
# Example: pose estimation pipeline
import torch
from lucidgrasp import PoseEstimator

estimator = PoseEstimator(...)
pose = estimator.predict(rgb, depth)
```

## Tuning notes

- Synthetic data is crucial due to limited real lab demonstrations.
- Transparent/reflective objects need special handling.
- Digital twins can pre-validate protocols before real execution.

## Verification

1. Run a 6D pose estimator on lab objects and compare to ground-truth poses.
2. Execute a pick-and-place task in simulation and then on real hardware.
3. Measure success rate and cycle time for a lab protocol.
''',
        "references": [
            "https://www.nature.com/articles/s43588-025-00924-4",
            "https://github.com/AccelerationConsortium/Matterix/",
            "https://arxiv.org/abs/2410.07801"
        ],
    },
    {
        "name": "proteomics-metabolomics-ml",
        "title": "Proteomics and Metabolomics ML",
        "description": "Mass spectrometry, peptide identification, DelPi, DIA-BERT, GiCOPS, ANN-SoLo, and metabolite annotation on GPU.",
        "devin_body": '''
## When to use

You are analyzing mass spectrometry data for protein/metabolite identification and annotation.

## Key concepts

- **Peptide identification**: DelPi (DIA), DIA-BERT (transformer), GiCOPS (database search).
- **Spectral library search**: ANN-SoLo with approximate nearest neighbors.
- **Metabolite annotation**: CSI:FingerID, Sirius, GNPS.
- **GPU**: PyTorch/CUDA for transformers and ANN search.

## Code pattern

```python
# DelPi inference
from delpi import DelPi
model = DelPi.from_pretrained("...")
model = model.to('cuda')
```

## Tuning notes

- DIA-BERT needs 40GB+ GPU (V100/A100) for training; smaller for inference.
- Use FDR control at 1% for peptide-spectrum matches.
- Metabolite annotation often combines MS/MS with molecular DBs.

## Verification

1. Run DelPi/DIA-BERT on a DIA dataset and compare IDs to DDA.
2. Run ANN-SoLo and measure sensitivity vs runtime.
3. Validate protein identifications with a known standard mixture.
''',
        "references": [
            "https://github.com/bertis-informatics/delpi",
            "https://github.com/guomics-lab/DIA-BERT",
            "https://github.com/pcdslab/gicops",
            "https://doi.org/10.5281/zenodo.3831054"
        ],
    },
    {
        "name": "spatial-transcriptomics-gpu",
        "title": "Spatial Transcriptomics on GPU",
        "description": "Cell segmentation, transcript assignment, BIDCell, segger, PanoSpace, and foundation models for spatial omics.",
        "devin_body": '''
## When to use

You are processing imaging-based spatial transcriptomics (Xenium, CosMx, MERFISH, Stereo-seq) on GPU.

## Key concepts

- **Cell segmentation**: BIDCell (self-supervised), segger (GNN), CellSAM (foundation).
- **Transcript assignment**: assign mRNA spots to cells.
- **GNNs**: heterogeneous graph of transcripts and cells.
- **Integration**: combine with scRNA-seq for cell typing.

## Code pattern

```python
import torch
# segger example
from segger import SeggerData, Segger

dataset = SeggerData(...)
model = Segger(...)
model.fit(dataset)
```

## Tuning notes

- Requires 12-32GB GPU memory depending on tissue complexity.
- Use cell morphology and cell-type priors in loss functions.
- Downstream: cell-type deconvolution, neighborhood analysis.

## Verification

1. Segment a Xenium or CosMx sample and compare to manual annotations.
2. Count transcripts per cell and check distribution.
3. Integrate with scVI/scRNA-seq and confirm cell-type consistency.
''',
        "references": [
            "https://github.com/sydneybiox/bidcell/",
            "https://github.com/dpeerlab/segger",
            "https://github.com/hehuifeng/PanoSpace-core",
            "https://cellsam.deepcell.org/"
        ],
    },
    {
        "name": "biodiversity-edna-ml",
        "title": "Biodiversity and eDNA Analysis with ML",
        "description": "Environmental DNA, species distribution modeling, zero-shot taxonomic assignment, and biodiversity monitoring on GPU.",
        "devin_body": '''
## When to use

You are using eDNA or camera-trap data to monitor biodiversity and species distributions.

## Key concepts

- **eDNA metabarcoding**: classify short reads to taxonomy.
- **Zero-shot annotation**: embedding-based assignment for unknown species.
- **Species distribution models (SDM)**: DeepSDM, attention U-Net.
- **Camera traps**: MegaDetector, SpeciesNet for automated classification.

## Code pattern

```python
# eDNA classifier
import torch
from metanode import MetAnoDe

model = MetAnoDe(...)
model = model.to('cuda')
```

## Tuning notes

- Reference databases are incomplete; use alignment-free methods and embeddings.
- Combine eDNA with environmental covariates (climate, soil).
- Handle class imbalance due to rare species.

## Verification

1. Classify eDNA samples and compare to known mock communities.
2. Run a species distribution model and evaluate AUC on held-out species.
3. Compare ML taxonomic assignment to BLAST/qiime2.
''',
        "references": [
            "https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013776",
            "https://github.com/KLKua/DeepSDM",
            "https://github.com/chiras/MetAnoDe"
        ],
    },
    {
        "name": "epidemiology-disease-surveillance",
        "title": "Epidemiological Modeling and Disease Surveillance",
        "description": "SIR/SEIR models, GNNs, Gaussian processes, and transfer learning for outbreak prediction and disease dynamics.",
        "devin_body": '''
## When to use

You are modeling infectious disease spread or building surveillance systems.

## Key concepts

- **Compartmental models**: SIR, SEIR, metapopulation models.
- **Agent-based simulations**: contact networks, superspreader events.
- **GNNs**: for spatio-temporal outbreak prediction.
- **Surveillance**: nowcasting, anomaly detection, early warning.

## Code pattern

```python
import torch
from torch_geometric.nn import GCNConv

class EpidemicGNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = GCNConv(10, 64)
        self.conv2 = GCNConv(64, 1)
```

## Tuning notes

- Real data is noisy and delayed; use nowcasting to correct reporting delay.
- Combine mechanistic models with ML for hybrid forecasts.
- Respect privacy and ethics in surveillance data.

## Verification

1. Fit an SIR/SEIR model to historical data and compare to observed peaks.
2. Run a GNN forecast and compute MAE/CRPS.
3. Test early-warning system on past outbreaks.
''',
        "references": [
            "https://link.springer.com/article/10.1186/s12911-025-03310-2",
            "https://arxiv.org/abs/2411.05556",
            "https://www.nature.com/articles/s41586-024-08564-w"
        ],
    },
    {
        "name": "social-simulation-ml",
        "title": "Social Simulation and Agent-Based Modeling with ML",
        "description": "AgentTorch, LLM-based agents, differentiable ABM, and causal discovery for social and economic systems.",
        "devin_body": '''
## When to use

You are simulating social, economic, or policy scenarios with agent-based models and ML.

## Key concepts

- **Agent-based models (ABM)**: agents, rules, emergent behavior.
- **LLM agents**: AgentTorch, GASim, CAMO; agents with LLM reasoning.
- **Differentiable ABM**: gradient-based calibration and optimization.
- **Causal discovery**: infer micro-to-macro mechanisms.

## Code pattern

```python
import agent_torch

# Define agents, environment, policy
cfg = agent_torch.Config(...)
runner = agent_torch.Runner(cfg)
runner.execute()
```

## Tuning notes

- Validate ABMs against real-world aggregate data.
- LLM agents can be expensive; use smaller models or caching.
- Use sensitivity analysis to understand parameter effects.

## Verification

1. Reproduce a known social phenomenon (e.g., market bubble) in simulation.
2. Compare aggregate ABM output to real data.
3. Calibrate ABM parameters with gradient descent or ABC.
''',
        "references": [
            "https://github.com/AgentTorch/AgentTorch",
            "https://aclanthology.org/2026.acl-long.569/",
            "https://aclanthology.org/2026.findings-acl.1224.pdf"
        ],
    },
    {
        "name": "industry-4-predictive-maintenance",
        "title": "Industry 4.0, Predictive Maintenance, and Digital Twins",
        "description": "RAPIDS, NVIDIA Omniverse, XGBoost, anomaly detection, and digital twins for manufacturing.",
        "devin_body": '''
## When to use

You are applying ML to manufacturing: predictive maintenance, defect detection, process optimization.

## Key concepts

- **Predictive maintenance**: RUL estimation, anomaly detection, vibration/sensor data.
- **Defect detection**: computer vision for quality control.
- **Digital twins**: NVIDIA Omniverse, OpenUSD, PEGAVERSE for factory simulation.
- **Time-series**: LSTM, TCN, transformers for sensor data.

## Code pattern

```python
import xgboost as xgb
import cudf

X = cudf.read_csv("sensors.csv")
model = xgb.XGBRegressor(tree_method="hist", device="cuda")
model.fit(X, y)
```

## Tuning notes

- Use imbalanced learning techniques for rare failures.
- Digital twins need CAD/3D models and real-time sensor feeds.
- Combine physics-based degradation models with ML.

## Verification

1. Train an RUL model and evaluate on a held-out test set.
2. Run anomaly detection on sensor data and compare to known failures.
3. Build a small digital twin and verify it mirrors real process behavior.
''',
        "references": [
            "https://developer.nvidia.com/blog/accelerating-predictive-maintenance-in-manufacturing-with-rapids-ai/",
            "https://developer.nvidia.com/blog/pegatron-simulates-and-optimizes-factory-operations-with-ai-enabled-digital-twins/",
            "https://www.mdpi.com/2076-3417/15/6/3166"
        ],
    },
    {
        "name": "sports-biomechanics-ml",
        "title": "Sports Biomechanics and Injury Prediction",
        "description": "Wearable sensors, ST-GNNs, federated learning, and multimodal fusion for athlete performance and injury risk.",
        "devin_body": '''
## When to use

You are analyzing athlete biomechanics, wearable data, or injury risk.

## Key concepts

- **Wearable sensors**: IMU, sEMG, PPG, accelerometers.
- **Skeleton graphs**: spatio-temporal GNNs on human pose.
- **Injury prediction**: load monitoring, recovery, biomechanical markers.
- **Federated learning**: train across teams/institutions without centralizing data.

## Code pattern

```python
import torch
from stgcn import STGCN

model = STGCN(in_channels=3, num_classes=2)
model = model.to('cuda')
```

## Tuning notes

- Data is highly personal; handle privacy carefully.
- Cross-sport transfer can help with limited data.
- Combine video pose estimation with wearable signals.

## Verification

1. Train an ankle injury prediction model and report AUC/sensitivity.
2. Compare injury predictions to actual injury records.
3. Validate with leave-one-athlete-out cross-validation.
''',
        "references": [
            "https://doi.org/10.1177/18724981251380391",
            "https://link.springer.com/article/10.1186/s13102-026-01625-9",
            "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1687895/full"
        ],
    },
    {
        "name": "high-energy-physics-ml",
        "title": "High-Energy Physics and LHC ML",
        "description": "Jet tagging, event reconstruction, Particle Transformer, Hypergraph, and ROOT/Geant4 integration on GPU.",
        "devin_body": '''
## When to use

You are applying ML to particle physics data from the LHC or similar experiments.

## Key concepts

- **Jet tagging**: GNNs, Particle Transformer (ParT), point-cloud jets.
- **Event reconstruction**: particle-flow, full-event reconstruction.
- **Hypergraph networks**: for complex decay chains.
- **ROOT/Geant4**: standard HEP data and simulation tools.

## Code pattern

```python
import torch
from particle_transformer import ParticleTransformer

model = ParticleTransformer(in_channels=4, num_classes=5)
model = model.to('cuda')
```

## Tuning notes

- HEP datasets are large but sparse; use efficient data loaders (uproot, awkward-array).
- Physical symmetries (Lorentz, permutation) matter.
- Inference must fit within trigger/online latency budgets.

## Verification

1. Train a jet tagger and compare ROC-AUC to a baseline.
2. Process a ROOT file through a PyTorch DataLoader.
3. Measure inference time per event on target hardware.
''',
        "references": [
            "https://arxiv.org/abs/2601.17554",
            "https://github.com/key4hep/k4MLJetTagger",
            "https://link.springer.com/article/10.1140/epjc/s10052-023-11677-7",
            "https://uproot.readthedocs.io/"
        ],
    },
]
