SKILLS = [
    {
        "name": "ai-for-seismology",
        "title": "AI for Seismology",
        "description": "Use deep-learning models to detect, pick, classify, and denoise seismic events from continuous waveform data for earthquake monitoring and catalog building.",
        "devin_body": r'''
## When to use

You are processing seismic waveforms for earthquake monitoring, exploration geophysics, or event classification.

## Usage

- Detect and pick P- and S-wave arrivals automatically in continuous seismic streams.
- Classify earthquakes, explosions, quarry blasts, and cultural noise in near real time.
- Suppress non-stationary environmental and cultural noise to recover low-amplitude signals.
- Build ML-enhanced seismic catalogs by associating picks and locating events across networks.

## Steps

1. Ingest and preprocess continuous waveform data (response removal, filtering, resampling) from a seismic network.
2. Run a pretrained deep-learning picker (e.g., PhaseNet, EQTransformer) to detect P/S arrivals and event windows.
3. Associate picks across stations using a travel-time or ML-based associator (e.g., GaMMA) and locate events.
4. Classify events by source type and denoise signals with autoencoders or adaptive filtering if needed.
5. Build a catalog, compare picks and locations to a reference catalog, and compute residuals and precision/recall.
6. Deploy the pipeline for near-real-time monitoring or mine archived data to find previously missed events.

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
            "https://seisbench.readthedocs.io/en/latest/",
            "https://doi.org/10.1146/annurev-earth-071822-100323",
            "https://github.com/seisbench/seisbench"
        ],
    },
    {
        "name": "ai-for-volcanology",
        "title": "AI for Volcanology",
        "description": "Forecast eruption probability by fusing seismic, gas, and satellite data to issue early warnings at volcanoes like Whakaari.",
        "devin_body": r'''
## When to use

You are analyzing volcano seismic and infrasound data to detect unrest or forecast eruptions.

## Usage

- Classify volcano-seismic event types (VT, LP, VLP, tremor, explosion quakes) from continuous waveforms.
- Detect precursory anomalies and patterns in multi-sensor monitoring data before eruptions.
- Build time-to-eruption or eruption-probability models from seismic, deformation, gas, and thermal time series.
- Fuse seismic, infrasound, gas, thermal, and satellite observations into a unified hazard dashboard.

## Steps

1. Collect continuous seismic, infrasound, gas, deformation, and thermal observations for the target volcano.
2. Label or cluster volcanic events (VT, LP, VLP, tremor, explosion quakes) and train a classifier on waveform features.
3. Run unsupervised anomaly detection on long-duration monitoring streams to flag deviations from background behavior.
4. Train a time-to-eruption or probabilistic forecasting model using multi-sensor precursors and past eruption records.
5. Generate eruption-probability alerts and validate lead time against historical eruptions.
6. Combine forecasts with scenario-based hazard maps and observatory workflows for decision support.

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
        "description": "Use data-driven models to reconstruct ocean currents, detect mesoscale eddies, and forecast ocean state from satellite and in-situ observations.",
        "devin_body": r'''
## When to use

You are predicting ocean state, reconstructing currents, or detecting mesoscale features from satellite and in-situ data.

## Usage

- Reconstruct high-resolution surface currents by fusing sea surface height, temperature, and wind data.
- Detect and track mesoscale eddies in satellite altimetry and multi-modal ocean imagery.
- Build neural surrogates for ocean circulation and biogeochemical variables at nowcasting to seasonal lead times.
- Downscale and gap-fill satellite ocean fields using deep-learning super-resolution and data imputation.

## Steps

1. Ingest satellite altimetry, SST, wind, in-situ drifters, and model reanalysis for the target region.
2. Preprocess data (regrid, gap-fill, normalize) and derive dynamic variables such as SSH, EKE, and geostrophic currents.
3. Train a neural current-reconstruction model (e.g., U-Net, GESTNet) on matched SSH/SST/wind and drifter observations.
4. Run an eddy-detection model on the reconstructed fields and track eddy trajectories over time.
5. Validate current maps against independent drifter trajectories and eddy tracks against a reference catalog.
6. Deploy the workflow for operational nowcasting or downscale climate projections for ecosystem and shipping applications.

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
        "description": "Apply remote-sensing foundation models and deep learning to classify land cover, detect changes, and map disasters from satellite and aerial imagery.",
        "devin_body": r'''
## When to use

You are analyzing satellite or aerial imagery for land cover, change detection, or environmental monitoring.

## Usage

- Fine-tune remote-sensing foundation models for land-use/land-cover classification and few-shot EO tasks.
- Fuse optical, SAR, LiDAR, and hyperspectral data for robust multi-modal Earth observation.
- Detect land-cover and infrastructure changes between multi-temporal images.
- Segment and locate objects such as buildings, crops, forests, and water bodies at scale.

## Steps

1. Curate multi-temporal and multi-sensor imagery for the target region and task (classification, change, segmentation).
2. Choose a remote-sensing foundation model (e.g., SkySense++, Prithvi, SatMamba) and fine-tune it on labeled data.
3. Build a change-detection pipeline that aligns multi-temporal images and highlights altered pixels or polygons.
4. Run segmentation or object detection to map buildings, crops, forests, or water bodies and evaluate IoU/mAP.
5. Validate against ground-truth labels and cross-test generalization across geographies and seasons.
6. Deploy the pipeline for operational monitoring such as disaster response, urban growth, or agricultural surveys.

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
        "description": "Use deep learning to search for compact binary mergers, estimate source parameters, and classify glitches in LIGO/Virgo/KAGRA detector data.",
        "devin_body": r'''
## When to use

You are searching LIGO/Virgo/KAGRA data for compact binary mergers or estimating source parameters.

## Usage

- Search for compact binary coalescence (CBC) signals in noisy strain data with matched-filter or deep-learning pipelines.
- Classify and mitigate non-Gaussian transient noise (glitches) that mimic gravitational-wave signals.
- Estimate source parameters (masses, spins, sky location) with neural samplers such as normalizing flows.
- Run low-latency event validation and data-quality assessment for observational follow-up.

## Steps

1. Preprocess detector strain (whitening, conditioning) and generate time-frequency representations or SNR time series.
2. Search for CBC candidates using a matched-filter, template bank, or neural search pipeline.
3. Apply a glitch classifier (e.g., Gravity Spy, GSpyNetTree, CoBiTS) to separate true signals from transient noise artifacts.
4. Estimate source parameters with a neural sampler or normalizing-flow model and compare to injected parameters.
5. Compute false-alarm rates and produce candidate alerts for electromagnetic and multi-messenger follow-up.
6. Integrate the search, glitch mitigation, and parameter-estimation workflow into a low-latency online pipeline.

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
            "https://github.com/ML4GW/aframe"
        ],
    },
    {
        "name": "ai-for-nuclear-engineering",
        "title": "AI for Nuclear Engineering and Fusion",
        "description": "Apply machine learning to build fast surrogates, predict plasma disruptions, model material degradation, and optimize control in nuclear and fusion systems.",
        "devin_body": r'''
## When to use

You are modeling nuclear systems, plasma behavior, or fusion experiments.

## Usage

- Train fast surrogate models to replace expensive neutronics or MHD simulations for design and optimization.
- Predict and avoid plasma disruptions in tokamaks from multi-diagnostic time-series data.
- Model thermal, radiation, and fatigue degradation of reactor and plasma-facing materials.
- Optimize plasma shape, scenario, and control trajectories with reinforcement learning or model predictive control.

## Steps

1. Assemble high-fidelity simulation or experimental data for the target nuclear/fusion problem (e.g., DIII-D, ITER scenarios).
2. Train a physics-informed or data-driven surrogate for neutronics, MHD, or thermomechanical response.
3. Build a disruption-prediction classifier using plasma diagnostics and validate warning time on historical disruptions.
4. Integrate degradation models for plasma-facing or structural materials and propagate uncertainty into lifetime forecasts.
5. Use reinforcement learning or Bayesian optimization to tune control policies and plasma scenarios.
6. Validate all ML predictions against physics simulators and experimental measurements, then embed approved models in control loops.

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
            "https://doi.org/10.1126/science.adm8201",
            "https://fusion.gat.com/"
        ],
    },
    {
        "name": "ai-for-carbon-capture",
        "title": "AI for Carbon Capture",
        "description": "Use machine learning to screen CO2 adsorbents and solvents, build molecular-simulation surrogates, and optimize carbon-capture processes and materials.",
        "devin_body": r'''
## When to use

You are screening materials or optimizing processes for CO2 capture and storage.

## Usage

- Screen solid adsorbents and solvents for CO2 affinity, selectivity, working capacity, and stability.
- Replace expensive DFT or GCMC calculations with ML surrogates for adsorption and diffusion properties.
- Optimize capture-process operating conditions (temperature, pressure, cycling) with Bayesian or active-learning methods.
- Couple materials screening with process simulation and lifecycle assessment for techno-economic evaluation.

## Steps

1. Define capture process requirements (flue gas composition, purity, energy penalty) and collect adsorption/solvent data.
2. Compute or retrieve material descriptors and train ML models to predict CO2 affinity, selectivity, and working capacity.
3. Build ML surrogates for DFT/GCMC energies or adsorption isotherms to accelerate high-throughput screening.
4. Run Bayesian optimization or active-learning loops to select top candidates and refine process conditions.
5. Evaluate top candidates with process simulation and lifecycle/techno-economic analysis.
6. Validate predictions against experimental isotherms and pilot-plant data, then feed results back to retrain the models.

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
        "description": "Apply ML to forecast streamflow and floods, monitor water quality, detect leaks, and model hydrological and water-distribution systems.",
        "devin_body": r'''
## When to use

You are modeling water resources, contamination, distribution systems, or flood risk.

## Usage

- Forecast streamflow and rainfall-runoff with time-series and hybrid physical-ML models.
- Monitor water quality by detecting sensor anomalies and classifying contamination sources.
- Detect and localize leaks from pressure, flow, and acoustic data in water distribution networks.
- Map flood and drought risk using satellite, weather, and hydrological inputs.

## Steps

1. Ingest hydrometeorological time series, sensor networks, and remote-sensing data for the watershed or utility.
2. Engineer lag, seasonal, and catchment features and split data with proper temporal cross-validation.
3. Train a streamflow, water-quality, or flood-forecasting model and evaluate with NSE, KGE, or exceedance metrics.
4. Build a leak-detection model from pressure/flow residuals, graph transformers, or acoustic signatures.
5. Integrate predictions into a decision-support dashboard for reservoir operations, water-treatment, or emergency response.
6. Monitor model drift, update with new observations, and validate against regulatory or ground-truth records.

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
            "https://neuralhydrology.readthedocs.io/en/stable/",
            "https://github.com/neuralhydrology/neuralhydrology",
            "https://waterdata.usgs.gov/"
        ],
    },
    {
        "name": "ai-for-archaeology",
        "title": "AI for Archaeology",
        "description": "Map hidden archaeological features beneath dense vegetation from airborne LiDAR using deep segmentation to speed discovery of ancient settlements.",
        "devin_body": r'''
## When to use

You are discovering archaeological sites, classifying artifacts, or monitoring heritage sites.

## Usage

- Predict likely archaeological site locations from environmental and landscape covariates.
- Detect crop marks, microtopography, and buried features in airborne LiDAR and multispectral imagery.
- Classify artifacts (pottery, coins, lithics) and ecofacts from photographs and 3D scans.
- Reconstruct excavation contexts and monuments with photogrammetry and 3D mesh processing.

## Steps

1. Assemble remote-sensing, LiDAR, aerial photographs, and field-survey data for the study landscape.
2. Generate LiDAR visualizations (RVT hillshades, local relief) and train object detectors for mounds, enclosures, or barrows.
3. Build a predictive site model from environmental covariates and validate against known sites.
4. Collect artifact images or 3D models and train a classifier with transfer learning and few-shot augmentation.
5. Run photogrammetry or structured-light scanning to produce 3D records of contexts and monuments.
6. Curate results in a GIS, review with domain experts, and flag legal/ethical constraints before fieldwork.

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
        "description": "Use ML to detect deepfakes and image forgeries, attribute authorship, and surface anomalies in digital and network forensic evidence.",
        "devin_body": r'''
## When to use

You are verifying digital evidence, detecting synthetic media, or attributing authorship.

## Usage

- Detect GAN- or diffusion-generated deepfakes in images, audio, and video evidence.
- Identify image forgeries such as copy-move, splicing, and compression artifacts.
- Attribute authorship of text, code, or behavioral patterns using stylometry and biometrics.
- Find anomalies in logs, network traffic, or device telemetry that indicate intrusion or tampering.

## Steps

1. Collect and preserve the digital evidence with documented chain of custody and hashing.
2. Extract forensic features (noise, EXIF, compression, artifacts) and run deepfake or forgery detectors.
3. Use source-camera identification and manipulation-localization maps to pinpoint altered regions.
4. Build stylometric or behavioral-biometric models to attribute authorship of suspicious content.
5. Apply anomaly detection to logs and network traffic, correlating events with the media under investigation.
6. Package findings with confidence scores and explainable evidence for legal review and chain-of-custody reporting.

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
        "description": "Use ML and remote sensing to map crops, predict yields, detect pests and diseases, and guide variable-rate precision agriculture.",
        "devin_body": r'''
## When to use

You are monitoring crops, predicting yields, detecting disease, or managing irrigation and nutrients.

## Usage

- Map crop types and growth stages from satellite or drone imagery and time series.
- Predict yield by fusing weather, soil, and remote-sensing features into regression or hybrid models.
- Detect crop pests, diseases, and stress with computer vision on leaf and field images.
- Generate variable-rate recommendations for irrigation, fertilization, and pest control.

## Steps

1. Collect satellite, UAV, weather, soil, and farm-management data for the target fields and growing season.
2. Preprocess imagery (cloud masking, NDVI, radiometric calibration) and align it with field boundaries.
3. Train a crop classification or segmentation model and evaluate with ground-truth labels.
4. Build a yield-prediction model using time-series weather, soil, and vegetation indices, validated by harvest data.
5. Deploy a disease/pest detector on leaf or canopy images and trigger variable-rate treatment recommendations.
6. Integrate outputs into a farm decision-support dashboard and update models as new season data arrives.

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
            "https://github.com/jiaxuanyou/crop_yield_prediction",
            "https://arxiv.org/abs/2403.01724",
            "https://torchgeo.readthedocs.io/",
            "https://cropmonitor.org/"
        ],
    },
    {
        "name": "ai-for-materials-synthesis",
        "title": "AI for Materials Synthesis",
        "description": "Use machine learning to predict synthesis recipes, plan routes, optimize process conditions, and drive self-driving laboratory workflows.",
        "devin_body": r'''
## When to use

You are predicting how to make a material, optimizing a synthesis recipe, or exploring process parameters.

## Usage

- Predict whether a target material can be synthesized and recommend feasible precursor sets.
- Plan retrosynthetic or reaction pathways using language or graph models trained on literature recipes.
- Optimize synthesis conditions (temperature, pressure, precursors, atmosphere) with Bayesian or active-learning methods.
- Operate self-driving laboratories that design, execute, and learn from synthesis experiments in closed loops.

## Steps

1. Define target material(s) and collect synthesis recipes, precursors, and process data from literature or databases.
2. Train a synthesizability or retrosynthesis model to propose candidate recipes and rank precursor sets.
3. Use Bayesian optimization or active learning to plan the most informative next experiments.
4. Execute planned syntheses manually or with robotic lab automation, and characterize products (XRD, XRF, etc.).
5. Update models with new outcomes and iterate until the target yield, purity, or property is achieved.
6. Validate the final recipe against a reaction database and reproduce it in independent runs.

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
