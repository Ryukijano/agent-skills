SKILLS = [
    {
        "name": "ai-for-geology",
        "title": "AI for Geology",
        "description": "Use ML and remote sensing to map lithology, assess mineral prospectivity, run geophysical inversions, and analyze drill-core and geologic data.",
        "devin_body": r'''
## When to use

You are working with geologic, geophysical, geochemical, or remote-sensing data and want to map lithology, structures, or mineral potential.

## Usage

- Classify lithology and structural units from multispectral/hyperspectral imagery and DEMs.
- Integrate geologic, geochemical, and geophysical layers for mineral prospectivity mapping.
- Build ML surrogates for fast magnetic, gravity, and electromagnetic geophysical inversion.
- Log drill-core images, detect fractures, and estimate mineral abundance from photos and XRF scans.

## Steps

1. Co-register geology, geophysics, geochemistry, and remote-sensing rasters to a common CRS and resolution.
2. Build a lithology/alteration classifier from satellite or airborne imagery and validate with field observations.
3. Generate multi-source evidential layers and rank mineral prospectivity with a weighted or ML-based model.
4. Train a neural operator or surrogate for geophysical inversion and compare predicted fields to forward models.
5. Process drill-core imagery and XRF data to log lithology, detect fractures, and estimate mineral abundance.
6. Produce GIS-ready maps and integrate them into exploration targeting and geologic interpretation workflows.

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
        "description": "Identify and quantify mineral phases from powder XRD patterns in near real time to automate geological and recycling workflows.",
        "devin_body": r'''
## When to use

You need to identify, classify, or segment minerals from spectroscopic, diffraction, or image data.

## Usage

- Identify mineral phases from XRD powder patterns and compare against reference libraries.
- Segment grains and classify mineral phases from SEM-EDS elemental maps and images.
- Classify minerals from Raman and hyperspectral signatures.
- Separate mineral grains in thin-section or drill-core imagery.

## Steps

1. Collect XRD, Raman, SEM-EDS, hyperspectral, or image data and normalize/background-correct spectra.
2. Augment data with shifts, scaling, and noise and compare CNNs against spectral-angle mapping and traditional methods.
3. Train a mineral classifier and validate against expert labels and reference libraries (e.g., RRUFF, XRD-AutoAnalyzer).
4. Segment mineral grains in images and compute mask IoU against hand-labeled masks.
5. Interpret predictions with attention maps or SHAP to identify diagnostic peaks or elemental features.
6. Integrate the pipeline into a core-logging or thin-section analysis workflow and update with new standards.

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
        "description": "Segment fossil CT volumes with minimal annotated data to extract fragile 3D anatomy and accelerate taxonomic study.",
        "devin_body": r'''
## When to use

You are analyzing fossil images, CT scans, or 3D models and want to speed up identification, segmentation, or morphological quantification.

## Usage

- Classify macro- and microfossil images with deep learning for taxonomic identification.
- Segment bone, shell, or tooth structures from CT or photogrammetry meshes.
- Extract landmark-free geometric morphometrics from segmented shapes.
- Infer habitat, diet, or climate from fossil morphology.

## Steps

1. Gather fossil images, CT scans, or 3D models from museums, publications, or field collections.
2. Preprocess images and use ImageNet or domain pretraining to fine-tune a fossil classifier.
3. Segment 3D specimens with strong augmentation and validate per-clade accuracy with taxonomists.
4. Extract morphometric measurements from segmentations and compare to manual landmarks.
5. Build models that link morphology to paleoecological variables (habitat, diet, climate).
6. Apply XAI to highlight diagnostic morphological features and publish validated datasets.

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
        "description": "Use ML and remote sensing to model species distributions, map habitat suitability, monitor biodiversity, and forecast ecological change.",
        "devin_body": r'''
## When to use

You are modeling species distributions, predicting biodiversity, or analyzing ecological communities across space and time.

## Usage

- Correlate species occurrence or abundance with environmental covariates in species distribution models.
- Map habitat suitability under current and future climate scenarios.
- Automate acoustic and camera-trap detection and classification.
- Forecast phenology, migrations, and ecosystem state changes.

## Steps

1. Compile species occurrence, abundance, and environmental covariate data (climate, topography, remote sensing).
2. Choose background/pseudo-absence points carefully and account for sampling bias.
3. Train an SDM or habitat-suitability model using spatial cross-validation to avoid optimistic estimates.
4. Validate against independent survey data and project models within the range of training conditions.
5. Deploy acoustic/camera-trap classifiers and integrate detections into occupancy or abundance models.
6. Forecast ecological changes under future scenarios and interpret partial dependence for ecological plausibility.

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
        "description": "Use remote sensing and integrated modeling to map land cover, monitor ecosystems, and assess environmental change and risk.",
        "devin_body": r'''
## When to use

You are analyzing environmental systems using satellite, in-situ, or model data and need classification, regression, or change detection.

## Usage

- Map land use and land cover from satellite or drone imagery.
- Monitor vegetation, water bodies, snow/ice, and urban expansion over time.
- Predict pollutant transport and ecological exposure with integrated models.
- Detect anomalies and trends from multi-temporal remote-sensing indices.

## Steps

1. Collect satellite, in-situ, and model data; apply atmospheric correction, cloud masking, and spectral indices.
2. Build time-composited training datasets and define a land-cover or ecosystem-change classification scheme.
3. Train a classifier (e.g., Random Forest, U-Net) and validate with spatial cross-validation and a reference product.
4. Compute overall accuracy, kappa, and per-class F1; generate land-cover and change maps.
5. Run integrated assessment or pollutant-fate models and compare to observations.
6. Deploy the monitoring pipeline and update maps as new imagery becomes available.

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
        "description": "Use camera-trap and acoustic ML to identify species, re-identify individuals, and detect poaching and habitat threats for wildlife conservation.",
        "devin_body": r'''
## When to use

You need to monitor wildlife, automate species identification from images or audio, or detect threats such as poaching and habitat loss.

## Usage

- Detect, classify species, and identify individuals from camera-trap images.
- Classify animal calls, gunshots, and chainsaw noise from audio recordings.
- Re-identify individuals by coat patterns, fin shapes, or facial features.
- Prioritize habitats and corridors and detect poaching activity from movement and occupancy data.

## Steps

1. Collect camera-trap or acoustic data and label/curate images or recordings with species and individual IDs.
2. Fine-tune an object detector (e.g., MegaDetector) to filter empties and localize animals, people, and vehicles.
3. Train a species classifier and re-identification model, handling severe class imbalance with active learning.
4. Deploy acoustic classifiers to detect animal calls and anthropogenic threats (gunshots, chainsaws).
5. Analyze occupancy, movement, and corridor-use patterns to inform conservation planning.
6. Validate with field experts, push alerts to rangers, and deploy lightweight edge models in low-bandwidth settings.

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
        "description": "Use remote sensing and LiDAR to inventory forests, segment trees, estimate biomass, and map species and disturbances.",
        "devin_body": r'''
## When to use

You are measuring, mapping, or monitoring forests using field plots, aerial/satellite imagery, or LiDAR point clouds.

## Usage

- Estimate forest inventory variables (tree counts, DBH, height, volume) from field and remote-sensing data.
- Detect and segment individual tree crowns from CHM or LiDAR point clouds.
- Predict above-ground biomass by regressing LiDAR structural metrics against field plots.
- Classify forest types and disturbance (fire, insects, harvest) from multi-temporal imagery.

## Steps

1. Collect field inventory plots, airborne/satellite imagery, and LiDAR point clouds for the forest area.
2. Preprocess LiDAR (ground classification, CHM, normalization) and extract structural features per plot.
3. Train a tree-crown segmentation or detection model and validate counts against field inventory.
4. Build an AGB regression model using LiDAR metrics and independent field-measured biomass.
5. Classify forest species and disturbance from spectral/temporal features and validate with aerial photo interpretation.
6. Map uncertainty, integrate with forest management systems, and update with new acquisitions.

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
        "description": "Detect illegal, unreported, and unregulated fishing by fusing AIS tracks with satellite radar and vessel behavior models.",
        "devin_body": r'''
## When to use

You are managing or studying fisheries, aquaculture, or marine ecosystems and need to predict catch, identify species, or detect illegal fishing.

## Usage

- Forecast catch or abundance from environmental and effort covariates.
- Detect species from eDNA metabarcoding and sequence-classification workflows.
- Classify acoustic/sonar echograms and estimate fish biomass.
- Monitor aquaculture water quality, feeding, disease, and welfare, and detect IUU vessel activity.

## Steps

1. Ingest catch/effort, eDNA, acoustic, AIS, and environmental (SST, chlorophyll, depth) data.
2. Engineer spatial-temporal features and train a catch/CPUE forecast model, handling zero-inflation and seasonality.
3. Classify eDNA reads or metabarcoding sequences and compare taxonomic assignments to reference databases.
4. Process acoustic/sonar data to detect schools and estimate biomass, validating with trawl or visual surveys.
5. Build aquaculture monitoring models for water quality, feeding, and disease, and detect anomalous vessel trajectories for IUU activity.
6. Integrate forecasts and detections into fishery management dashboards and compare to surplus-production baselines.

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
        "description": "Use ML and physics-informed models to predict rainfall-runoff, forecast streamflow, predict floods, and build digital twins for water systems.",
        "devin_body": r'''
## When to use

You are modeling rainfall-runoff, streamflow, floods, or water quality and want data-driven forecasts or surrogates.

## Usage

- Predict discharge from precipitation and catchment properties.
- Forecast streamflow with LSTM, transformers, or NARX time-series models.
- Classify or forecast flood events from meteorological and hydrological inputs.
- Embed mass and momentum conservation with PINNs and build real-time digital twins of water systems.

## Steps

1. Collect precipitation, streamflow, catchment attributes, and weather data for target basins.
2. Normalize inputs by catchment area and long-term statistics; engineer lag and sequence features.
3. Train a rainfall-runoff or streamflow model (LSTM, transformer, NARX) and evaluate with NSE/KGE/bias.
4. Build a flood-forecasting or classification pipeline and validate on extreme events not seen in training.
5. Add physics-informed constraints or a digital-twin layer that assimilates real-time sensor data.
6. Compare with conceptual/physical hydrologic models and deploy the best model for operational forecasting.

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
        "description": "Nowcast extreme precipitation from radar with physics-embedded deep generative models to improve flood and hydropower decisions.",
        "devin_body": r'''
## When to use

You need to forecast weather, downscale climate output, nowcast precipitation, or detect extreme-weather events.

## Usage

- Nowcast precipitation and storms (<6 h) from radar and satellite data.
- Emulate or bias-correct numerical weather prediction (NWP) with fast neural surrogates.
- Apply weather foundation models (GraphCast, FourCastNet, Pangu-Weather, FengWu, Aurora, ClimaX) for medium-range forecasts.
- Downscale and bias-correct model output, and detect tropical cyclones, atmospheric rivers, and convective hazards.

## Steps

1. Ingest radar, satellite, NWP, reanalysis, and climate-projection data for the target region and lead time.
2. Train a precipitation nowcaster (ConvLSTM, diffusion) and compare RMSE/CSI to persistence and NWP baselines.
3. Fine-tune or run a weather foundation model for deterministic or probabilistic medium-range forecasting.
4. Downscale and bias-correct model output with super-resolution or statistical adjustment methods.
5. Detect and track extreme events (cyclones, atmospheric rivers, convective hazards) and compare to labeled databases.
6. Evaluate with CRPS, CSI, Brier score, and physical-conservation metrics, then deploy operationally with ensemble post-processing.

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
        "description": "Use ML to map soil properties, build pedotransfer functions, predict soil carbon from spectra, and assess soil health.",
        "devin_body": r'''
## When to use

You are mapping soil properties, predicting soil carbon, or analyzing spectroscopic and legacy soil data.

## Usage

- Predict soil classes and properties from environmental covariates with digital soil mapping.
- Infer hydraulic and mechanical properties from easier-to-measure data with pedotransfer functions.
- Predict organic carbon, texture, and nutrients from visible-infrared (VIS-NIR) spectra.
- Assess soil health by integrating biological, chemical, and physical indicators.

## Steps

1. Compile legacy soil maps, lab records, and new observations; harmonize units and depths.
2. Collect environmental covariates (terrain, climate, geology, remote sensing) for the target area.
3. Standardize spectra, remove water/CO2 absorption bands, and train models to predict SOC, texture, or nutrients.
4. Build DSM or PTF models using spatial cross-validation and pedological knowledge for plausible predictions.
5. Map uncertainty and flag extrapolation outside the training covariate space.
6. Validate against independent lab samples and integrate maps into land-management or carbon-accounting systems.

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
        "description": "Forecast air and water pollutant exceedances from sensor and satellite data to guide regulatory alerts and remediation.",
        "devin_body": r'''
## When to use

You need to monitor pollutant concentrations, identify sources, forecast exceedances, or prioritize remediation.

## Usage

- Forecast PM2.5, PM10, NO2, O3, and other pollutants from meteorology and emissions data.
- Estimate nutrient, heavy-metal, and pathogen levels in water from in-situ and remote-sensing data.
- Map soil contamination from reflectance spectroscopy or multisensor data.
- Attribute pollution to sources and detect regulatory threshold exceedances.

## Steps

1. Ingest air, water, or soil monitoring data plus meteorology, emissions, traffic, and remote-sensing covariates.
2. Engineer lag, diurnal, and seasonal features and handle missing sensors with imputation.
3. Train pollutant-concentration or exceedance-forecasting models and evaluate against persistence and regulatory monitors.
4. Apply source-apportionment methods or SHAP-based attribution to identify traffic, industry, and natural contributions.
5. Map soil or water contamination with spectroscopic or multisensor models and validate with lab samples.
6. Build a decision-support dashboard for exceedance alerts, compliance reporting, and remediation prioritization.

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
