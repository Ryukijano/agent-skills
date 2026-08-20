SKILLS = [
    {
        "name": "ai-for-seismology",
        "title": "AI for Seismology",
        "description": "Machine learning for earthquake detection, phase picking, denoising, and seismic signal classification.",
        "devin_body": r'''
## When to use

You are processing seismic waveforms for earthquake monitoring, exploration geophysics, or event classification.

## Key concepts

- **Phase picking**: detect P- and S-wave arrivals automatically.
- **Event detection/classification**: distinguish earthquakes, explosions, quarry blasts, and noise.
- **Denoising and denoising autoencoders**: suppress cultural and environmental noise.
- **CataLog building**: ML-enhanced seismic catalogs from continuous data.

## Code pattern

```python
import seisbench

# Load a pretrained phase-picking model
picker = seisbench.models.PhaseNet.from_pretrained("instance")
annotations = picker.annotate(stream)
```

## Tuning notes

- Annotate with domain-specific data; transfer from pretrained models helps.
- Pay attention to non-stationary noise and station-specific effects.
- Validate detections against an expert-reviewed catalog.

## Verification

1. Pick phases on a small continuous seismic stream.
2. Compare picks to a reference catalog and compute residuals.
3. Run a detection model on noisy data and report precision/recall.
''',
        "references": [
            "https://arxiv.org/abs/2603.17855",
            "https://seisbench.gempa.de/",
            "https://doi.org/10.1146/annurev-earth-071822-100323",
            "https://github.com/seisbench/seisbench"
        ],
    },
    {
        "name": "ai-for-volcanology",
        "title": "AI for Volcanology",
        "description": "Machine learning for eruption forecasting, volcanic seismicity classification, and hazard assessment.",
        "devin_body": r'''
## When to use

You are analyzing volcano seismic and infrasound data to detect unrest or forecast eruptions.

## Key concepts

- **Volcano-seismic event classes**: VT, LP, VLP, tremor, explosion quakes.
- **Unsupervised anomaly detection**: identify precursory signals in continuous data.
- **Eruption forecasting**: time-to-eruption models from multi-sensor time series.
- **Multi-sensor fusion**: seismic, deformation, gas, thermal, and satellite data.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import IsolationForest

# Anomaly detection on feature vectors extracted from seismic streams
clf = IsolationForest(contamination=0.05)
clf.fit(event_features)
outliers = clf.predict(event_features)
```

## Tuning notes

- Classifiers must generalize across volcanoes; use transfer learning cautiously.
- Unsupervised methods can reveal unknown precursors but need careful validation.
- Combine with physical models and expert interpretation.

## Verification

1. Classify a small labeled set of volcanic events.
2. Run anomaly detection before a known eruption and inspect lead time.
3. Compare an ML forecast to a physics-based baseline.
''',
        "references": [
            "https://arxiv.org/abs/2603.17855",
            "https://doi.org/10.1029/2024gl108631",
            "https://doi.org/10.1007/978-3-031-15432-4",
            "https://github.com/darren-tpk/voiss-net"
        ],
    },
    {
        "name": "ai-for-oceanography",
        "title": "AI for Oceanography",
        "description": "Data-driven ocean forecasting, current reconstruction, eddy detection, and marine ecosystem modeling.",
        "devin_body": r'''
## When to use

You are predicting ocean state, reconstructing currents, or detecting mesoscale features from satellite and in-situ data.

## Key concepts

- **Neural ocean models**: data-driven surrogates for ocean circulation.
- **Eddy detection**: identify and track mesoscale eddies in satellite altimetry.
- **Current reconstruction**: fuse sea-level, wind, and in-situ observations.
- **Nowcasting to seasonal forecasting**: lead-time-specific prediction tasks.

## Code pattern

```python
import xarray as xr
from scipy.ndimage import gaussian_filter

# Load sea-surface height and detect extrema as eddy candidates
ssh = xr.open_dataset("ssh.nc").ssh
candidates = detect_extrema(ssh, threshold=0.05)
```

## Tuning notes

- Incorporate physical constraints such as mass and momentum conservation.
- Satellite data is noisy and gappy; use data imputation and multi-sensor fusion.
- Validate against reanalysis products and mooring observations.

## Verification

1. Train a small neural network to forecast SSH at a point.
2. Detect and track eddies and compare to a manual catalog.
3. Reconstruct surface currents and compare to drifter trajectories.
''',
        "references": [
            "https://sp.copernicus.org/articles/5-opsr/22/2025/",
            "https://doi.org/10.1029/2025jh000686",
            "https://os.copernicus.org/articles/21/1065/2025/",
            "https://xgcm.readthedocs.io/"
        ],
    },
    {
        "name": "ai-for-satellite-imaging",
        "title": "AI for Satellite Imaging",
        "description": "Earth observation foundation models, land-use classification, change detection, and disaster mapping.",
        "devin_body": r'''
## When to use

You are analyzing satellite or aerial imagery for land cover, change detection, or environmental monitoring.

## Key concepts

- **Remote sensing foundation models**: pretrained backbones for EO imagery.
- **Multi-modal fusion**: optical, SAR, LiDAR, and hyperspectral sensors.
- **Change detection**: identify changes between multi-temporal images.
- **Segmentation and object detection**: buildings, crops, forests, water bodies.

## Code pattern

```python
import torch
from torchgeo.models import resnet50

# Load a pretrained remote-sensing model and fine-tune on your data
model = resnet50(pretrained=True)
features = model(image)
```

## Tuning notes

- Use sensors appropriate for the task and region (cloud cover, resolution).
- Augment with rotation, scaling, and radiometric jitter specific to EO.
- Be cautious about geospatial data drift across regions and seasons.

## Verification

1. Fine-tune a foundation model on a land-cover classification dataset.
2. Run change detection between two satellite images and compare to labels.
3. Evaluate zero-shot transfer to a different geography.
''',
        "references": [
            "https://www.nature.com/articles/s42256-025-01078-8",
            "https://github.com/zhu-xlab/Copernicus-FM",
            "https://github.com/gastruc/AnySat",
            "https://torchgeo.readthedocs.io/"
        ],
    },
    {
        "name": "ai-for-gravitational-waves",
        "title": "AI for Gravitational-Wave Astronomy",
        "description": "Deep learning for compact binary coalescence search, parameter estimation, and glitch classification.",
        "devin_body": r'''
## When to use

You are searching LIGO/Virgo/KAGRA data for compact binary mergers or estimating source parameters.

## Key concepts

- **Matched filtering vs deep learning**: trade-offs and hybrid pipelines.
- **Signal-to-noise time series**: deep-learning classifiers on SNR data.
- **Parameter estimation with normalizing flows**: AMPLFI, DINGO.
- **Glitch detection and mitigation**: separate non-Gaussian transients.

## Code pattern

```python
import numpy as np

# Simplified: train a 1D CNN on whitened strain snippets
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

model = Sequential([Conv1D(32, 16, activation='relu', input_shape=(4096, 1)),
                    MaxPooling1D(4), Flatten(), Dense(1, activation='sigmoid')])
```

## Tuning notes

- Data is highly imbalanced; use synthetic injections and background samples.
- Models must generalize across detector noise and hardware configurations.
- Calibrate output probabilities and report false-alarm rates.

## Verification

1. Train a detector on simulated binary black-hole waveforms.
2. Measure sensitivity at a fixed false-alarm rate.
3. Estimate chirp mass and compare to injected parameters.
''',
        "references": [
            "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.111.024035",
            "https://arxiv.org/abs/2501.13846",
            "https://a3d3.ai/a3d3-team-leads-the-first-end-to-end-machine-learning-based-real-time-search-for-binary-black-holes/",
            "https://github.com/alecgunny/deep-crackle"
        ],
    },
    {
        "name": "ai-for-nuclear-engineering",
        "title": "AI for Nuclear Engineering and Fusion",
        "description": "Machine learning for reactor design, plasma control, material degradation, and fusion ignition prediction.",
        "devin_body": r'''
## When to use

You are modeling nuclear systems, plasma behavior, or fusion experiments.

## Key concepts

- **Surrogate models for expensive simulations**: replace neutronics or MHD solvers.
- **Disruption prediction**: forecast and avoid plasma disruptions in tokamaks.
- **Material degradation**: thermal stress, radiation damage, fatigue.
- **Reinforcement learning for control**: shape and trajectory optimization.

## Code pattern

```python
import jax
import jax.numpy as jnp

# Neural state-space model for plasma dynamics
from jax import random
params = model.init(random.PRNGKey(0), x, u)
predictions = model.apply(params, x, u)
```

## Tuning notes

- Safety-critical: validate predictions with physical simulators and experiments.
- Data is scarce; leverage physics-informed and multi-fidelity methods.
- UQ is essential for high-consequence decisions.

## Verification

1. Build a surrogate for a simple reactor physics model and compare to a high-fidelity run.
2. Train a disruption predictor on a public tokamak dataset.
3. Propagate uncertainty and compute safety margins.
''',
        "references": [
            "https://www.nature.com/articles/s41467-025-63917-x",
            "https://iopscience.iop.org/article/10.1088/1741-4326/ade8fd",
            "https://www.osti.gov/biblio/2589559",
            "https://fusion.gat.com/"
        ],
    },
    {
        "name": "ai-for-carbon-capture",
        "title": "AI for Carbon Capture",
        "description": "Machine learning for adsorbent and solvent screening, process optimization, and carbon capture materials design.",
        "devin_body": r'''
## When to use

You are screening materials or optimizing processes for CO2 capture and storage.

## Key concepts

- **Material screening**: predict CO2 affinity, selectivity, and capacity.
- **Molecular simulation surrogates**: replace DFT / GCMC with ML models.
- **Process optimization**: optimize operating conditions with reinforcement learning or Bayesian optimization.
- **Lifecycle assessment**: account for energy, emissions, and cost.

## Code pattern

```python
from sklearn.ensemble import RandomForestRegressor

# Train a model to predict CO2 working capacity from material descriptors
model = RandomForestRegressor(n_estimators=200)
model.fit(X_train, y_train)
```

## Tuning notes

- Use experimentally validated adsorption isotherms where possible.
- Surrogate models must extrapolate cautiously to unseen chemistries.
- Couple with process simulation for techno-economic analysis.

## Verification

1. Predict adsorption capacity on a held-out test set of materials.
2. Optimize a process variable and compare to a baseline.
3. Validate top candidates with a physics-based simulation.
''',
        "references": [
            "https://arxiv.org/abs/2401.07181",
            "https://www.nature.com/articles/s41586-022-05422-5",
            "https://doi.org/10.1029/2024gl108631",
            "https://github.com/zikribayraktar/Carbon_Capture_ML"
        ],
    },
    {
        "name": "ai-for-water-security",
        "title": "AI for Water Security",
        "description": "ML for water quality prediction, leak detection, flood forecasting, and hydrological modeling.",
        "devin_body": r'''
## When to use

You are modeling water resources, contamination, distribution systems, or flood risk.

## Key concepts

- **Hydrological forecasting**: rainfall-runoff, streamflow prediction.
- **Water quality monitoring**: sensor anomaly detection and contaminant classification.
- **Leak detection**: pressure and flow anomaly detection in distribution networks.
- **Flood and drought mapping**: satellite and weather-driven risk models.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict streamflow from lagged precipitation and temperature
model = GradientBoostingRegressor()
model.fit(X_train, y_train)
```

## Tuning notes

- Include seasonality and lag features.
- Missing and irregular sensor data are common; use imputation.
- Evaluate with proper temporal cross-validation.

## Verification

1. Forecast streamflow for a small watershed and compare to observations.
2. Detect simulated leaks from pressure time series.
3. Map a flood event and compare to satellite-based flood extent.
''',
        "references": [
            "https://arxiv.org/abs/2402.08989",
            "https://www.hydrosdk.org/",
            "https://github.com/neuralhydrology/neuralhydrology",
            "https://waterdata.usgs.gov/"
        ],
    },
    {
        "name": "ai-for-archaeology",
        "title": "AI for Archaeology",
        "description": "Remote sensing, LiDAR, and computer vision for site detection, artifact analysis, and heritage preservation.",
        "devin_body": r'''
## When to use

You are discovering archaeological sites, classifying artifacts, or monitoring heritage sites.

## Key concepts

- **Predictive modeling**: identify likely site locations from environmental covariates.
- **Remote sensing and LiDAR**: detect crop marks, microtopography, and buried features.
- **Artifact classification**: pottery, coins, lithics from images.
- **3D reconstruction and photogrammetry**: document excavation and monuments.

## Code pattern

```python
from PIL import Image
import numpy as np

# Example: object detection on aerial imagery
from torchvision.models.detection import fasterrcnn_resnet50_fpn
model = fasterrcnn_resnet50_fpn(pretrained=True)
```

## Tuning notes

- Archaeological datasets are small; use foundation models and few-shot fine-tuning.
- Collaborate with domain experts to avoid false positives.
- Respect ethical and legal constraints on excavation data.

## Verification

1. Train an object detector on a small annotated imagery dataset.
2. Generate a predictive site map and compare to known sites.
3. Process a LiDAR point cloud and visualize archaeological microtopography.
''',
        "references": [
            "https://journal.caa-international.org/articles/10.5334/jcaa.207",
            "https://doi.org/10.3390/geomatics5040052",
            "https://doi.org/10.1038/s40494-025-01994-3",
            "https://doi.org/10.1371/journal.pone.0330419"
        ],
    },
    {
        "name": "ai-for-forensics",
        "title": "AI for Digital Forensics",
        "description": "ML for image authentication, deepfake detection, authorship attribution, and anomaly detection in forensic evidence.",
        "devin_body": r'''
## When to use

You are verifying digital evidence, detecting synthetic media, or attributing authorship.

## Key concepts

- **Deepfake detection**: identify GAN or diffusion-generated images, audio, video.
- **Image forgery detection**: copy-move, splicing, and manipulation traces.
- **Authorship attribution**: stylometry and behavioral biometrics.
- **Anomaly detection**: identify unusual patterns in logs or network traffic.

## Code pattern

```python
from transformers import AutoModelForImageClassification, AutoImageProcessor

processor = AutoImageProcessor.from_pretrained("prithivMLmods/Deepfake-vs-Real-8000")
model = AutoModelForImageClassification.from_pretrained("prithivMLmods/Deepfake-vs-Real-8000")
```

## Tuning notes

- Adversarial generators evolve quickly; use ensemble and metadata checks.
- Report confidence and uncertainty; legal evidence needs transparency.
- Maintain chain of custody and avoid altering evidence.

## Verification

1. Build a deepfake detector and test on held-out generation methods.
2. Detect a copy-move forgery in an image.
3. Attribute authorship of a short text and evaluate robustness.
''',
        "references": [
            "https://arxiv.org/abs/2404.11163",
            "https://github.com/grip-unina/TruFor",
            "https://github.com/polimi-ispl/icpr2020dfdc",
            "https://pages.nist.gov/frvt/"
        ],
    },
    {
        "name": "ai-for-agriculture",
        "title": "AI for Agriculture",
        "description": "Crop monitoring, yield prediction, pest detection, and precision agriculture with ML and remote sensing.",
        "devin_body": r'''
## When to use

You are monitoring crops, predicting yields, detecting disease, or managing irrigation and nutrients.

## Key concepts

- **Crop classification and mapping**: from satellite or drone imagery.
- **Yield prediction**: combine weather, soil, and remote-sensing features.
- **Pest and disease detection**: computer vision on leaf and field images.
- **Precision agriculture**: variable-rate input recommendations.

## Code pattern

```python
from torchvision.models import resnet18
import torch

model = resnet18(pretrained=True)
# Replace the final layer for crop-disease classification
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
```

## Tuning notes

- Season and region dominate; use domain-adaptation or fine-tuning.
- Ground-truth data is expensive; use weak and semi-supervised learning.
- Consider environmental and economic impact in deployment.

## Verification

1. Classify crop types from Sentinel-2 time series.
2. Predict yield for a small region and compare to reported values.
3. Detect a plant disease from leaf images with a small model.
''',
        "references": [
            "https://github.com/Project-Platypus/Rivanna",
            "https://arxiv.org/abs/2403.01724",
            "https://torchgeo.readthedocs.io/",
            "https://cropmonitor.org/"
        ],
    },
    {
        "name": "ai-for-materials-synthesis",
        "title": "AI for Materials Synthesis",
        "description": "Machine learning for synthesis route prediction, process optimization, and inverse design of materials.",
        "devin_body": r'''
## When to use

You are predicting how to make a material, optimizing a synthesis recipe, or exploring process parameters.

## Key concepts

- **Synthesisability prediction**: estimate whether a target compound can be made.
- **Retrosynthesis and reaction prediction**: plan synthesis pathways.
- **Process optimization**: Bayesian optimization of temperature, pressure, precursors.
- **Lab automation**: self-driving labs for closed-loop materials discovery.

## Code pattern

```python
from ax.service.ax_client import AxClient

# Optimize synthesis conditions
ax = AxClient()
ax.create_experiment(
    name="synthesis",
    parameters=[{"name": "temp", "type": "range", "bounds": [300.0, 800.0]}],
    objective_name="yield",
)
```

## Tuning notes

- Use literature-extracted reaction data and domain constraints.
- Bayesian optimization is useful when experiments are expensive.
- Validate predicted routes with chemists and lab experiments.

## Verification

1. Predict synthesis conditions for a set of known compounds.
2. Optimize a process using a few rounds of Bayesian optimization.
3. Cross-check a proposed route with a reaction database.
''',
        "references": [
            "https://doi.org/10.1038/s41586-023-06197-z",
            "https://citrine.io/",
            "https://github.com/aspuru-guzik-group/chemos",
            "https://ax.dev/"
        ],
    },
]
