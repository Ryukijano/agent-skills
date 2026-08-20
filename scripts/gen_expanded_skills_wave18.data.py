SKILLS = [
    {
        "name": "ai-for-geology",
        "title": "AI for Geology",
        "description": "Geologic mapping, mineral prospectivity, geophysical inversion, drill-core imagery, and remote sensing with ML and deep learning.",
        "devin_body": r'''
## When to use

You are working with geologic, geophysical, geochemical, or remote-sensing data and want to map lithology, structures, or mineral potential.

## Key concepts

- **Geologic mapping**: supervised classification of lithology and structural units from multispectral/hyperspectral imagery and DEMs.
- **Mineral prospectivity mapping (MPM)**: integrate multi-source evidential layers to rank exploration targets.
- **Geophysical inversion**: ML surrogates and neural operators for fast magnetic, gravity, and EM inversion.
- **Drill-core imagery**: core logging, fracture detection, and mineral abundance from drill-core photos and XRF scans.
- **Remote sensing**: satellite and airborne data for alteration mapping and structural interpretation.

## Code pattern

```python
import rasterio
import geopandas as gpd
from sklearn.ensemble import RandomForestClassifier

# Stack of geology, geophysics, and remote-sensing layers
with rasterio.open("geology_stack.tif") as src:
    X = src.read().reshape(src.count, -1).T

gdf = gpd.read_file("training_labels.gpkg")
y = gdf["lithology"].values

clf = RandomForestClassifier(n_estimators=300, class_weight="balanced")
clf.fit(X, y)
```

## Tuning notes

- Co-register all raster and vector layers to a common CRS and resolution.
- Use stratified or spatial cross-validation; geology data are often spatially autocorrelated.
- Incorporate physical or geologic constraints to keep predictions geologically consistent.
- Balance rare lithology/mineral classes and quantify uncertainty.

## Verification

1. Train a lithology classifier on a multispectral stack and report per-class F1 and overall accuracy.
2. Compare mineral prospectivity scores to known deposits and generate a ROC curve.
3. Run a geophysical inversion surrogate and compare predicted fields to forward models.
''',
        "references": [
            "https://doi.org/10.1016/j.earscirev.2024.104941",
            "https://doi.org/10.3390/min16060584",
            "https://doi.org/10.1515/geo-2025-0765",
            "https://doi.org/10.1007/s10712-025-09904-9",
        ],
    },
    {
        "name": "ai-for-mineralogy",
        "title": "AI for Mineralogy",
        "description": "XRD, SEM-EDS, Raman, and hyperspectral imaging for automated mineral identification, classification, and segmentation.",
        "devin_body": r'''
## When to use

You need to identify, classify, or segment minerals from spectroscopic, diffraction, or image data.

## Key concepts

- **XRD phase identification**: classify powder diffraction patterns into mineral assemblages.
- **SEM-EDS and microanalysis**: segment grains and classify mineral phases from elemental maps.
- **Raman and hyperspectral spectroscopy**: identify minerals from spectral signatures.
- **Mineral segmentation**: separate mineral grains in thin-section or drill-core imagery.
- **Spectral libraries**: use reference libraries such as RRUFF for training and validation.

## Code pattern

```python
import torch
import torch.nn as nn

class MineralCNN1D(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv1d(1, 32, kernel_size=7, padding=3),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1),
        )
        self.head = nn.Linear(32, num_classes)

    def forward(self, x):
        return self.head(self.conv(x).squeeze(-1))

# x: (batch, 1, spectral_bins)
model = MineralCNN1D(num_classes=20)
```

## Tuning notes

- Normalize spectra and remove baseline/background before training.
- Use data augmentation (shift, scale, noise) and domain constraints for physical plausibility.
- Compare CNNs against traditional classifiers and spectral-angle mapping.
- Interpret predictions with attention maps or SHAP to identify diagnostic peaks.

## Verification

1. Train a mineral classifier on XRD or Raman data and report confusion matrix vs expert labels.
2. Segment mineral grains in a SEM image and compare mask IoU to hand-labeled masks.
3. Evaluate transfer from a public spectral library to a new sample batch.
''',
        "references": [
            "https://doi.org/10.1016/j.earscirev.2026.105514",
            "https://doi.org/10.3390/app13179992",
            "https://doi.org/10.1016/j.matt.2025.102272",
            "https://doi.org/10.3390/jsan11030050",
        ],
    },
    {
        "name": "ai-for-paleontology",
        "title": "AI for Paleontology",
        "description": "Automated fossil identification, morphometric analysis, 3D segmentation, and taxonomic classification from images and point clouds.",
        "devin_body": r'''
## When to use

You are analyzing fossil images, CT scans, or 3D models and want to speed up identification, segmentation, or morphological quantification.

## Key concepts

- **Fossil image classification**: deep learning for taxonomic identification of macro- and microfossils.
- **3D segmentation**: segment bone, shell, or tooth structures from CT or photogrammetry meshes.
- **Morphometrics**: landmark-free geometric morphometrics from segmented shapes.
- **Paleoecological inference**: predict habitat, diet, or climate from fossil morphology.
- **Citizen-science and dark data**: leverage web-crawled and museum images to build training sets.

## Code pattern

```python
import torch
from torchvision import models, transforms

model = models.resnet50(weights="IMAGENET1K_V2")
model.fc = torch.nn.Linear(model.fc.in_features, num_fossil_classes)

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
```

## Tuning notes

- Start with ImageNet pretraining; fossil datasets are often small.
- Use strong augmentation, class weighting, and ensemble models to handle imbalance.
- Validate against expert taxonomists and track per-clade accuracy.
- Apply XAI to highlight morphological features that drive classification.

## Verification

1. Fine-tune a classifier on a fossil image dataset and compare accuracy to human annotations.
2. Segment a CT-scanned specimen and extract morphometric measurements.
3. Compare model predictions across microfossil and macrofossil clades and analyze failure modes.
''',
        "references": [
            "https://doi.org/10.1007/s10462-024-11080-y",
            "https://doi.org/10.1016/j.earscirev.2024.104765",
            "https://doi.org/10.1017/pab.2022.14",
            "https://doi.org/10.1002/gj.70007",
        ],
    },
    {
        "name": "ai-for-ecology",
        "title": "AI for Ecology",
        "description": "Species distribution modeling, habitat suitability, biodiversity monitoring, and ecological forecasting using ML and remote sensing.",
        "devin_body": r'''
## When to use

You are modeling species distributions, predicting biodiversity, or analyzing ecological communities across space and time.

## Key concepts

- **Species distribution models (SDMs)**: correlate occurrence or abundance with environmental covariates.
- **Habitat suitability**: estimate the probability of species presence under current and future conditions.
- **Acoustic and camera-trap monitoring**: automate detection and classification of vocalizations and images.
- **Occupancy and abundance models**: hierarchical models for imperfect detection.
- **Ecological forecasting**: predict phenology, migrations, and ecosystem state changes.

## Code pattern

```python
import xarray as xr
from sklearn.ensemble import GradientBoostingClassifier

# Environmental covariates from raster stack
cov = xr.open_dataset("environmental_covariates.nc")
X = cov.to_dataframe().dropna()
y = presence_absence_labels  # 1/0 at sampled locations

model = GradientBoostingClassifier(n_estimators=200)
model.fit(X, y)
```

## Tuning notes

- Use spatial cross-validation to avoid optimistic performance estimates.
- Choose background/pseudo-absence points carefully and account for sampling bias.
- Project models to future climate only within the range of training conditions.
- Interpret partial dependence and response curves for ecological plausibility.

## Verification

1. Train an SDM on presence/absence data and evaluate with spatial CV AUC-PR.
2. Generate a habitat-suitability map and compare to independent survey data.
3. Test transfer to a different region or time period and quantify extrapolation.
''',
        "references": [
            "https://doi.org/10.1145/3460112.3471966",
            "https://doi.org/10.1007/s10462-024-11074-w",
            "https://doi.org/10.1146/annurev.ecolsys.110308.120159",
            "https://doi.org/10.1038/s41559-024-02435-3",
        ],
    },
    {
        "name": "ai-for-environmental-science",
        "title": "AI for Environmental Science",
        "description": "Remote sensing, land-cover mapping, ecosystem service assessment, and integrated modeling for environmental monitoring and analysis.",
        "devin_body": r'''
## When to use

You are analyzing environmental systems using satellite, in-situ, or model data and need classification, regression, or change detection.

## Key concepts

- **Land-use/land-cover mapping**: classify satellite or drone imagery into thematic classes.
- **Ecosystem monitoring**: track vegetation condition, water bodies, snow/ice, and urban expansion.
- **Environmental fate and exposure**: predict pollutant transport and ecological risk.
- **Integrated assessment models**: couple physical, ecological, and socio-economic data.
- **Remote sensing time series**: use multi-temporal indices to detect anomalies and trends.

## Code pattern

```python
import rioxarray
from sklearn.ensemble import RandomForestClassifier

# Sentinel/Landsat raster stack
rds = rioxarray.open_rasterio("satellite_stack.tif")
X = rds.stack(pixel=("y", "x")).T.values
y = land_cover_reference_values

clf = RandomForestClassifier(n_estimators=300, class_weight="balanced")
clf.fit(X, y)
```

## Tuning notes

- Apply atmospheric correction, cloud masking, and spectral indices (NDVI, NDWI).
- Composite images over time to reduce noise and missing data.
- Use spatial or block cross-validation because pixels are spatially correlated.
- Consider class hierarchy and label noise in land-cover products.

## Verification

1. Classify a satellite image and compare to a validated land-cover reference.
2. Compute overall accuracy, kappa, and per-class F1 scores.
3. Detect land-cover change between two time periods and validate with ground data.
''',
        "references": [
            "https://doi.org/10.1016/j.scitotenv.2023.167705",
            "https://doi.org/10.1007/s44163-024-00198-1",
            "https://doi.org/10.3389/fenvs.2024.1336088",
            "https://doi.org/10.1016/j.envsoft.2024.106312",
        ],
    },
    {
        "name": "ai-for-wildlife-conservation",
        "title": "AI for Wildlife Conservation",
        "description": "Camera-trap image classification, acoustic monitoring, animal re-identification, and anti-poaching analytics.",
        "devin_body": r'''
## When to use

You need to monitor wildlife, automate species identification from images or audio, or detect threats such as poaching and habitat loss.

## Key concepts

- **Camera-trap analytics**: automated detection, species classification, and individual ID.
- **Acoustic monitoring**: classify animal calls, gunshots, and chainsaw noise in audio recordings.
- **MegaDetector and open models**: use pre-trained animal/empty/human/vehicle detectors.
- **Animal re-identification**: match individuals by coat patterns, fin shapes, or facial features.
- **Conservation planning**: prioritize habitats and corridors using movement and occupancy data.

## Code pattern

```python
import torch
from torchvision import models

model = models.mobilenet_v3_large(weights="IMAGENET1K_V2")
model.classifier[-1] = torch.nn.Linear(
    model.classifier[-1].in_features, n_species
)

# Typical camera-trap workflow: detect -> classify species -> filter empties
```

## Tuning notes

- Pretrain on large camera-trap datasets (e.g., Snapshot Serengeti) when available.
- Filter false triggers and handle severe class imbalance across species.
- Use active learning to prioritize human review of uncertain images.
- Deploy edge models for real-time alerts in low-bandwidth field settings.

## Verification

1. Fine-tune a species classifier on camera-trap data and report per-species precision/recall.
2. Compare an empty-vs-animal detector to a manual blank-filtering baseline.
3. Test re-identification accuracy across multiple encounters of the same individual.
''',
        "references": [
            "https://doi.org/10.1111/2041-210X.13120",
            "https://doi.org/10.1016/j.ecoinf.2024.102815",
            "https://doi.org/10.24072/pcjournal.261",
            "https://doi.org/10.48550/arxiv.2202.02283",
        ],
    },
    {
        "name": "ai-for-forestry",
        "title": "AI for Forestry",
        "description": "Forest inventory, tree segmentation, biomass estimation, and species mapping from remote sensing and LiDAR.",
        "devin_body": r'''
## When to use

You are measuring, mapping, or monitoring forests using field plots, aerial/satellite imagery, or LiDAR point clouds.

## Key concepts

- **Forest inventory**: estimate tree counts, diameter, height, and volume.
- **Individual tree detection (ITD)**: segment crowns from CHM or point clouds.
- **LiDAR point clouds**: derive height, canopy density, intensity, and 3D structure metrics.
- **Above-ground biomass (AGB)**: regress structural metrics against field-measured biomass.
- **Species and disturbance mapping**: classify forest types, fire, insect, and harvest events.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# LiDAR/structural features per plot
X = features[["h_mean", "canopy_density", "intensity_mean", "chm_max"]]
y = field_measured_agb

rfr = RandomForestRegressor(n_estimators=300, random_state=42)
rfr.fit(X, y)
```

## Tuning notes

- Normalize and classify LiDAR point clouds; remove non-ground returns carefully.
- Use CHM-based or point-cloud deep learning (e.g., PointNet, Point Transformer) for ITD.
- Consider mixed-effects or hierarchical models to pool limited field plots.
- Validate against independent inventory plots and propagate uncertainty.

## Verification

1. Predict AGB from LiDAR features and report RMSE and R2 vs field plots.
2. Segment individual tree crowns and compare counts to field inventory.
3. Map forest disturbance and validate with aerial photo interpretation.
''',
        "references": [
            "https://doi.org/10.1007/s40725-024-00234-4",
            "https://doi.org/10.1007/s40725-024-00223-7",
            "https://doi.org/10.3390/rs11111260",
            "https://doi.org/10.3390/electronics13204139",
        ],
    },
    {
        "name": "ai-for-fisheries",
        "title": "AI for Fisheries",
        "description": "Fish stock assessment, catch forecasting, aquaculture monitoring, eDNA, and IUU fishing detection with ML.",
        "devin_body": r'''
## When to use

You are managing or studying fisheries, aquaculture, or marine ecosystems and need to predict catch, identify species, or detect illegal fishing.

## Key concepts

- **Stock assessment and catch forecasting**: relate catch or abundance to environmental and effort covariates.
- **eDNA metabarcoding**: detect species from environmental samples using sequencing and ML classifiers.
- **Acoustic and sonar surveys**: classify echograms and estimate fish biomass.
- **Aquaculture monitoring**: water quality, feeding, disease, and welfare prediction.
- **IUU detection**: analyze vessel AIS trajectories and imagery for illegal activity.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

df = pd.read_csv("fisheries_catch.csv")
X = df[["sst", "chlorophyll", "depth", "effort_hours"]]
y = df["catch_kg"]

model = GradientBoostingRegressor(n_estimators=200)
model.fit(X, y)
```

## Tuning notes

- Catch data are often zero-inflated; consider hurdle or zero-inflated models.
- Use spatial or temporal cross-validation to avoid data leakage.
- Integrate biological priors and management scenarios for decision support.
- Interpret models with SHAP to understand driver importance.

## Verification

1. Forecast catch or CPUE and compare against a surplus-production model.
2. Classify species from eDNA reads and evaluate taxonomic assignment accuracy.
3. Detect anomalous vessel tracks and compare to known IUU incident records.
''',
        "references": [
            "https://doi.org/10.3390/bdcc10010019",
            "https://doi.org/10.1080/23308249.2024.2423189",
            "https://doi.org/10.3390/fishes10020074",
            "https://doi.org/10.1016/j.aquaculture.2025.743602",
        ],
    },
    {
        "name": "ai-for-hydrology",
        "title": "AI for Hydrology",
        "description": "Rainfall-runoff modeling, streamflow forecasting, flood prediction, and physics-informed deep learning for water systems.",
        "devin_body": r'''
## When to use

You are modeling rainfall-runoff, streamflow, floods, or water quality and want data-driven forecasts or surrogates.

## Key concepts

- **Rainfall-runoff modeling**: predict discharge from precipitation and catchment properties.
- **Streamflow forecasting**: use LSTM, transformers, or NARX networks for time-series prediction.
- **Flood prediction**: classify or forecast flood events from meteorological and hydrological inputs.
- **Physics-informed neural networks (PINNs)**: embed mass and momentum conservation into neural networks.
- **Digital twins**: integrate real-time sensor data with AI models for operational forecasting.

## Code pattern

```python
import torch

class LSTMFlow(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers):
        super().__init__()
        self.lstm = torch.nn.LSTM(
            input_dim, hidden_dim, num_layers, batch_first=True
        )
        self.fc = torch.nn.Linear(hidden_dim, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])

model = LSTMFlow(input_dim=5, hidden_dim=64, num_layers=2)
```

## Tuning notes

- Normalize inputs by catchment area and long-term statistics.
- Choose appropriate sequence length and lag structure for the basin response time.
- Use NSE, KGE, and bias metrics for hydrologic model evaluation.
- Quantify uncertainty with ensembling or Bayesian methods.

## Verification

1. Train an LSTM on rainfall-runoff data and report NSE and KGE on an unseen basin.
2. Compare with a conceptual or physical model for flood events.
3. Validate on an extreme event period not included in the training set.
''',
        "references": [
            "https://doi.org/10.3390/w18010119",
            "https://doi.org/10.1007/s42990-025-00201-6",
            "https://doi.org/10.1007/s40899-021-00584-y",
            "https://doi.org/10.3390/w17152281",
        ],
    },
    {
        "name": "ai-for-meteorology",
        "title": "AI for Meteorology",
        "description": "Numerical weather prediction emulators, precipitation nowcasting, extreme-weather detection, and weather foundation models.",
        "devin_body": r'''
## When to use

You need to forecast weather, downscale climate output, nowcast precipitation, or detect extreme-weather events.

## Key concepts

- **Nowcasting**: short-term (<6 h) prediction of precipitation and storms from radar/satellite.
- **NWP emulators and surrogates**: ML models that emulate or bias-correct numerical weather prediction.
- **Foundation models**: GraphCast, FourCastNet, Pangu-Weather, FengWu, ClimaX.
- **Downscaling and bias correction**: super-resolution and statistical adjustment of model output.
- **Extreme weather detection**: identify tropical cyclones, atmospheric rivers, and convective hazards.

## Code pattern

```python
import torch

class ConvLSTMNowcast(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels):
        super().__init__()
        self.encoder = torch.nn.Conv2d(in_channels, hidden_channels, 3, padding=1)
        self.decoder = torch.nn.Conv2d(hidden_channels, 1, 3, padding=1)

    def forward(self, x):
        return self.decoder(torch.relu(self.encoder(x)))

model = ConvLSTMNowcast(in_channels=10, hidden_channels=32)
```

## Tuning notes

- Use physics-informed or constrained loss functions to respect conservation laws.
- Tune lead time, spatial resolution, and input channels for the target variable.
- Apply bias correction and ensembling before operational use.
- Evaluate with CRPS, CSI, and Brier score for probabilistic forecasts.

## Verification

1. Train a precipitation nowcaster and compare RMSE/CSI to persistence and NWP baseline.
2. Fine-tune a weather foundation model on a regional reanalysis and evaluate downscaling.
3. Detect extreme events and compare to a labeled event database.
''',
        "references": [
            "https://doi.org/10.3390/atmos16010082",
            "https://doi.org/10.1016/j.engappai.2025.112335",
            "https://doi.org/10.48550/arxiv.2501.06907",
            "https://doi.org/10.5194/gmd-16-6433-2023",
        ],
    },
    {
        "name": "ai-for-soil-science",
        "title": "AI for Soil Science",
        "description": "Digital soil mapping, pedotransfer functions, spectroscopic prediction, and soil health assessment with ML.",
        "devin_body": r'''
## When to use

You are mapping soil properties, predicting soil carbon, or analyzing spectroscopic and legacy soil data.

## Key concepts

- **Digital soil mapping (DSM)**: predict soil classes or properties from environmental covariates using the SCORPAN model.
- **Pedotransfer functions (PTFs)**: infer hydraulic or mechanical properties from easier-to-measure soil data.
- **Visible-infrared (VIS-NIR) spectroscopy**: predict organic carbon, texture, and nutrients from spectra.
- **Soil health indicators**: biological, chemical, and physical proxies of soil function.
- **Legacy data integration**: harmonize old soil maps and lab records with new observations.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Spectral + terrain covariates
X = np.column_stack([visnir_spectra, elevation, slope, twi])
y = organic_carbon_measured

model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X, y)
```

## Tuning notes

- Standardize spectra and remove water/CO2 absorption regions when needed.
- Use spatial cross-validation to account for spatial autocorrelation in soil data.
- Combine pedological knowledge with machine learning for physically plausible predictions.
- Map uncertainty and flag extrapolation outside the training covariate space.

## Verification

1. Predict soil organic carbon and report R2 and RMSE vs lab reference samples.
2. Generate a digital soil map and validate with an independent holdout set.
3. Compare spectroscopic predictions to wet-chemistry measurements across soil types.
''',
        "references": [
            "https://doi.org/10.1111/ejss.70080",
            "https://doi.org/10.1016/j.earscirev.2020.103359",
            "https://doi.org/10.5194/soil-5-79-2019",
            "https://doi.org/10.3390/land15020331",
        ],
    },
    {
        "name": "ai-for-pollution",
        "title": "AI for Pollution",
        "description": "Air, water, and soil pollution monitoring, source apportionment, forecasting, and regulatory compliance with ML.",
        "devin_body": r'''
## When to use

You need to monitor pollutant concentrations, identify sources, forecast exceedances, or prioritize remediation.

## Key concepts

- **Air quality forecasting**: predict PM2.5, PM10, NO2, O3 from meteorology and emissions data.
- **Water quality monitoring**: estimate nutrient, heavy metal, and pathogen levels from in-situ and remote-sensing data.
- **Soil pollution detection**: map contamination from reflectance spectroscopy or multisensor data.
- **Source apportionment**: attribute pollution to sectors, traffic, industry, or natural sources.
- **Regulatory compliance**: detect threshold exceedances and support emission-control decisions.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("air_quality.csv")
X = df[["temperature", "humidity", "wind_speed", "traffic_index", "hour"]]
y = df["pm25"]

model = RandomForestRegressor(n_estimators=300)
model.fit(X, y)
```

## Tuning notes

- Handle missing sensors and non-stationary pollution patterns over time.
- Include lag features and diurnal/seasonal encodings.
- Use classification or survival models for exceedance probability.
- Interpret drivers with feature importance and SHAP for stakeholders.

## Verification

1. Forecast daily PM2.5 and compare RMSE/MAE to a persistence baseline.
2. Detect pollution exceedances and report precision/recall against regulatory monitors.
3. Identify dominant sources and compare apportionment results to receptor models.
''',
        "references": [
            "https://doi.org/10.3389/fenvs.2024.1336088",
            "https://doi.org/10.1016/j.envsoft.2024.106312",
            "https://doi.org/10.1007/s44163-024-00198-1",
            "https://doi.org/10.3390/rs17071207",
        ],
    },
]
