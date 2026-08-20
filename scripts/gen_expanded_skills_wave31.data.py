SKILLS = [
    {
        "name": "ai-for-biodiversity",
        "title": "AI for Biodiversity",
        "description": "Automated species detection, acoustic and eDNA monitoring, habitat suitability modeling, and biodiversity trend analysis for conservation.",
        "devin_body": r'''
## When to use

You are assessing species distributions, monitoring biodiversity change, or automating taxonomic identification from images, audio, or genetic samples.

## Key concepts

- **Camera-trap and image-based species ID**: deep learning classifiers and detectors for wildlife surveys.
- **Acoustic and eDNA monitoring**: automated call classification and metabarcoding pipelines.
- **Species distribution models (SDMs)**: relate occurrence records to environmental covariates.
- **Biodiversity indicators**: alpha/beta diversity, occupancy, and abundance trends.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Train a species distribution model from occurrence + environmental rasters
clf = RandomForestClassifier(n_estimators=500, class_weight="balanced")
clf.fit(X_env, y_presence)
```

## Tuning notes

- Use spatial block cross-validation to avoid overfitting from spatial autocorrelation.
- Combine presence-only data with background/pseudo-absence selection.
- Balance rare vs common species with class weights or focal loss.
- Align taxonomic labels across data sources before model training.

## Verification

1. Train a species classifier on camera-trap images and report per-species F1.
2. Compare SDM predictions against held-out occurrence records using AUC-PR.
3. Compute biodiversity trends and validate with independent field surveys.
''',
        "references": [
            "https://www.mdpi.com/1424-8220/24/24/8122",
            "https://doi.org/10.1002/2688-8319.70167",
            "https://github.com/google/cameratrapai/",
            "https://arxiv.org/html/2603.20509",
        ],
    },
    {
        "name": "ai-for-ecosystem-restoration",
        "title": "AI for Ecosystem Restoration",
        "description": "Monitoring rewilding, forest recovery, wetland restoration, and habitat reconstruction using remote sensing and biodiversity indicators.",
        "devin_body": r'''
## When to use

You need to measure restoration success, track rewilding progress, or prioritize interventions for degraded ecosystems.

## Key concepts

- **Restoration trajectories**: vegetation structure, species reassembly, and functional recovery.
- **Remote sensing indices**: NDVI, NDWI, LiDAR canopy structure, and multispectral time series.
- **Acoustic and camera-trap recovery metrics**: automated biodiversity indicators.
- **Treatment effectiveness**: compare restored, reference, and degraded sites.

## Code pattern

```python
from sklearn.ensemble import RandomForestRegressor

# Predict restoration success from annual spectral indices + structure
model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X_indices, y_recovery_score)
```

## Tuning notes

- Define clear reference conditions and baselines across space and time.
- Use change-detection methods to separate climate from management effects.
- Combine structural (remote sensing) and faunal (sensor) recovery metrics.
- Apply site-level blocking to avoid pseudo-replication.

## Verification

1. Map restoration-induced canopy change with pre/post satellite imagery.
2. Compare acoustic-derived community recovery to reference sites.
3. Relate remote-sensing recovery scores to field-measured biodiversity.
''',
        "references": [
            "https://doi.org/10.1371/journal.pone.0253148",
            "https://www.nature.com/articles/s41467-023-41693-w",
            "https://www.mdpi.com/2072-4292/18/2/346",
            "https://doi.org/10.5194/wbf2026-927",
        ],
    },
    {
        "name": "ai-for-conservation-planning",
        "title": "AI for Conservation Planning",
        "description": "Spatial prioritization, protected-area design, systematic conservation planning, and trade-off analysis using optimization and ML.",
        "devin_body": r'''
## When to use

You must decide where to protect, restore, or manage land/sea to meet biodiversity targets under budget and equity constraints.

## Key concepts

- **Systematic conservation planning (SCP)**: cost-effective selection of actions and areas (Marxan, Zonation).
- **AI-driven prioritization**: reinforcement learning for spatial conservation (CAPTAIN).
- **Trade-offs**: biodiversity, carbon, water, and livelihood objectives.
- **Connectivity and climate adaptation**: corridor design and climate-smart prioritization.

## Code pattern

```python
from sklearn.linear_model import LogisticRegression

# Predict site irreplaceability from species and cost features
irreplaceability = LogisticRegression(
    class_weight="balanced", max_iter=1000
).fit(X, y).predict_proba(X)[:, 1]
```

## Tuning notes

- Include acquisition/opportunity costs, threats, and connectivity constraints.
- Validate against complementarity and representation targets.
- Use scenario analysis to explore climate and land-use futures.
- Engage stakeholders to interpret trade-offs and ensure equity.

## Verification

1. Solve a small reserve-selection problem and compare cost to a greedy baseline.
2. Generate a 30x30 prioritization map and check target achievement.
3. Test robustness of priorities under climate-change scenarios.
''',
        "references": [
            "https://doi.org/10.1016/j.tree.2024.12.002",
            "https://www.nature.com/articles/s41893-022-00851-6",
            "https://doi.org/10.1101/2025.01.06.631540",
            "https://www.ijcai.org/proceedings/2025/1086.pdf",
        ],
    },
    {
        "name": "ai-for-natural-hazards",
        "title": "AI for Natural Hazards",
        "description": "Multi-hazard susceptibility mapping and early warning for landslides, floods, wildfires, and land subsidence with ML and remote sensing.",
        "devin_body": r'''
## When to use

You are mapping multi-hazard risk, forecasting imminent events, or designing early warning systems for landslides, floods, wildfires, or subsidence.

## Key concepts

- **Hazard susceptibility**: probabilistic mapping of where hazards may occur.
- **Multi-hazard assessment**: combined landslide, flood, wildfire, and subsidence modeling.
- **Early warning systems**: triggers, thresholds, and lead-time optimization.
- **Remote sensing and InSAR**: Sentinel-1/2, DEM, and ground deformation data.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Multi-hazard susceptibility from terrain, hydrology, and vegetation
clf = RandomForestClassifier(n_estimators=400, class_weight="balanced")
clf.fit(X_hazard, y_hazard_type)
```

## Tuning notes

- Treat hazards as multi-label when co-occurrence is possible.
- Use spatial cross-validation; susceptibility varies by region.
- Integrate physical-process models with ML for short-horizon forecasting.
- Calibrate warning thresholds with stakeholders and historical event data.

## Verification

1. Build landslide/flood/wildfire susceptibility maps and validate with AUC-ROC.
2. Compare an optimized RF to single-hazard baseline maps.
3. Test an early-warning trigger against past events and report lead time.
''',
        "references": [
            "https://link.springer.com/article/10.1038/s41598-025-15381-2",
            "https://iopscience.iop.org/article/10.1088/1748-9326/ae5f7f/meta",
            "https://doi.org/10.1038/s41598-020-69233-2",
            "https://www.nature.com/articles/s41598-026-52139-w",
        ],
    },
    {
        "name": "ai-for-wetlands",
        "title": "AI for Wetlands",
        "description": "Wetland mapping, inundation dynamics, cover-type classification, and hydrological trend monitoring from satellite time series.",
        "devin_body": r'''
## When to use

You are mapping wetland extent, tracking seasonal inundation, classifying cover types, or detecting hydrological change.

## Key concepts

- **Wetland extent and dynamics**: MNDWI, NDWI, Sentinel-1/2 time series.
- **Cover-type classification**: open water, aquatic vegetation, turbid water, moist soil.
- **Flood-pulse monitoring**: intra- and inter-annual inundation patterns.
- **Global wetland models**: Swamp-AI, WetlandMapper, GEE-based workflows.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Classify wetland cover types from multispectral + SAR stack
clf = RandomForestClassifier(n_estimators=300)
clf.fit(X, y_cover)
```

## Tuning notes

- Combine optical and SAR to handle clouds and vegetation.
- Account for seasonal water-level fluctuations and phenology.
- Use high-tide/low-tide or wet/dry season composites for training.
- Validate against field surveys and airborne LiDAR where possible.

## Verification

1. Map wetland extent and compare to a global wetland product.
2. Classify cover types and report producer/user accuracies.
3. Generate an annual inundation time series and compare to gauged water levels.
''',
        "references": [
            "https://www.nature.com/articles/s41598-026-39257-1",
            "https://doi.org/10.31223/x5jx93",
            "https://www.mdpi.com/2072-4292/14/23/6104",
            "https://www.sei.org/tools/wetsat-ml-wetlands-flooding-extent-and-trends-using-satellite-observations-and-machine-learning/",
        ],
    },
    {
        "name": "ai-for-coral-reefs",
        "title": "AI for Coral Reefs",
        "description": "Coral reef monitoring, bleaching detection, benthic classification, and reef-health assessment from underwater and drone imagery.",
        "devin_body": r'''
## When to use

You need to classify benthic habitats, detect coral bleaching, or monitor reef recovery from underwater, drone, or satellite imagery.

## Key concepts

- **Benthic image classification**: CoralNet, mRES-uNet, and point-count models.
- **Bleaching detection**: healthy vs bleached coral segmentation.
- **Reef-scale monitoring**: drone RGB, photo-quadrats, and satellite-derived bathymetry.
- **Underwater image correction**: color restoration and radiometric normalization.

## Code pattern

```python
import torch
from torchvision import models

# Fine-tune a CNN for healthy/bleached coral classification
model = models.resnet50(weights="IMAGENET1K_V2")
model.fc = torch.nn.Linear(model.fc.in_features, n_classes)
```

## Tuning notes

- Correct for light attenuation and color cast in underwater images.
- Use class weights for rare bleached colonies.
- Aggregate point/pixel predictions to colony or transect scale.
- Combine drone surveys with in-water validation by experts.

## Verification

1. Train a benthic classifier and report per-class F1 vs expert annotations.
2. Detect a bleaching event and compare to in-situ bleaching surveys.
3. Map coral cover change over time and validate with repeat surveys.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2511.00021",
            "https://doi.org/10.3390/rs15092238",
            "https://www.mdpi.com/2077-1312/12/8/1266",
            "https://coralnet.ucsd.edu/source/2947/",
        ],
    },
    {
        "name": "ai-for-glaciology",
        "title": "AI for Glaciology",
        "description": "Glacier mapping, surface mass balance estimation, snow/ice classification, and climate-change impact assessment.",
        "devin_body": r'''
## When to use

You are delineating glacier boundaries, estimating surface mass balance, classifying ice facies, or projecting glacier change.

## Key concepts

- **Glacier segmentation**: deep learning for clean-ice, debris-covered, and snow/firn mapping.
- **Surface mass balance (SMB)**: temperature-index and machine-learning models.
- **Geodetic and glaciological data fusion**: MassBalanceMachine, OGGM, ERA5.
- **Multi-sensor inputs**: optical, SAR, DEM, and meteorological reanalysis.

## Code pattern

```python
import segmentation_models_pytorch as smp

# U-Net/Transformer for glacier extent segmentation
model = smp.Unet("resnet50", in_channels=4, classes=3)
```

## Tuning notes

- Distinguish seasonal snow from glacier ice; use multi-temporal training.
- Fuse SAR and optical to improve cloud/debris-covered mapping.
- Calibrate SMB models with both point observations and geodetic mass balance.
- Use transfer learning from regional inventories to data-scarce glaciers.

## Verification

1. Segment glacier outlines and compare to manually digitized inventories.
2. Predict surface mass balance and evaluate against in-situ stakes.
3. Map debris-covered ice and quantify area change over a decade.
''',
        "references": [
            "https://doi.org/10.1038/s41467-024-54956-x",
            "https://doi.org/10.5194/egusphere-egu26-11039",
            "https://www.sciencedirect.com/science/article/pii/S1569843222001212",
            "https://tc.copernicus.org/articles/19/1675/2025/",
        ],
    },
    {
        "name": "ai-for-desertification",
        "title": "AI for Desertification",
        "description": "Land degradation and desertification risk mapping, sensitivity assessment, and early warning from remote sensing and ML.",
        "devin_body": r'''
## When to use

You are assessing desertification sensitivity, mapping degraded land, or forecasting land degradation in dryland regions.

## Key concepts

- **Desertification indices**: MEDALUS, NDVI, SAVI, BSI, LST, and land management.
- **Machine learning classifiers**: Random Forest, XGBoost, SVM for risk zones.
- **Spatiotemporal forecasting**: LSTM and DeepMLP for DSI time series.
- **Google Earth Engine pipelines**: scalable cloud-based monitoring.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Classify desertification risk from spectral/thermal/climate features
clf = RandomForestClassifier(n_estimators=300, class_weight="balanced")
clf.fit(X_risk, y_risk_class)
```

## Tuning notes

- Combine climate, soil, vegetation, and management indicators.
- Use long time series to separate interannual climate from degradation.
- Validate with ground photos and independent land-cover maps.
- Communicate uncertainty classes to land managers and policymakers.

## Verification

1. Map desertification sensitivity and compare to a MEDALUS baseline.
2. Predict land degradation trends with a temporal model and evaluate R²/RMSE.
3. Identify degradation hotspots and cross-check with field observations.
''',
        "references": [
            "https://www.mdpi.com/2072-4292/17/19/3350",
            "https://www.mdpi.com/2072-4292/16/23/4525",
            "https://www.nature.com/articles/s41598-023-46319-1",
            "https://doi.org/10.1007/s12665-025-12766-4",
        ],
    },
    {
        "name": "ai-for-ocean-conservation",
        "title": "AI for Ocean Conservation",
        "description": "Marine protected area monitoring, illegal fishing detection, species tracking, and ocean health assessment from satellite and vessel data.",
        "devin_body": r'''
## When to use

You are monitoring marine protected areas, detecting illegal fishing, tracking vessels, or assessing marine ecosystem health.

## Key concepts

- **Vessel monitoring**: AIS, VMS, and SAR-based dark-vessel detection.
- **Illegal fishing detection**: behavioral classification and anomaly detection.
- **Marine species and habitat mapping**: cetacean/sea-turtle detection, habitat suitability.
- **MPA performance**: compliance, spillover, and biodiversity indicators.

## Code pattern

```python
from sklearn.ensemble import IsolationForest

# Anomaly detection for fishing vessel behavior from AIS features
clf = IsolationForest(contamination=0.05, random_state=42)
clf.fit(X_ais)
```

## Tuning notes

- Fuse AIS, SAR, and optical imagery to detect vessels without AIS.
- Calibrate anomaly scores by region and gear type.
- Protect sensitive MPA data and respect maritime jurisdictions.
- Validate detections with patrol records and observer reports.

## Verification

1. Classify fishing vs non-fishing behavior and report AUC-ROC.
2. Detect anomalous vessel activity in an MPA and compare to patrol logs.
3. Map marine habitat and validate with survey or eDNA data.
''',
        "references": [
            "https://arxiv.org/html/2312.03207",
            "https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1798458/full",
            "https://doi.org/10.1016/j.procs.2026.06.143",
            "https://allenai.org/skylight",
        ],
    },
    {
        "name": "ai-for-air-quality",
        "title": "AI for Air Quality",
        "description": "Pollutant forecasting, spatiotemporal PM modeling, emission source apportionment, and early warning for air quality.",
        "devin_body": r'''
## When to use

You are forecasting pollutant levels, issuing air-quality alerts, or identifying emission sources for urban and regional scales.

## Key concepts

- **Pollutant forecasting**: PM2.5, PM10, NO2, O3, CO from meteorology and emissions.
- **Spatiotemporal deep learning**: ConvLSTM, transformers, and graph neural networks.
- **Source apportionment**: PMF, receptor models, and SHAP-based attribution.
- **Hybrid physical-ML models**: combine chemical-transport with deep learning.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingRegressor

# Multi-horizon PM2.5 forecast from meteorology + lagged concentrations
model = GradientBoostingRegressor(n_estimators=300)
model.fit(X, y_pm25)
```

## Tuning notes

- Use chronological splits; avoid future leakage from emissions or traffic.
- Include diurnal, weekly, and seasonal encodings.
- Evaluate both point forecasts and prediction interval coverage.
- Downscale coarse chemical-transport output with regional ML models.

## Verification

1. Forecast next-day PM2.5 and compare RMSE to persistence and CTM baselines.
2. Predict pollution exceedances and report precision/recall at regulatory monitors.
3. Attribute sources and compare apportionment to receptor-model estimates.
''',
        "references": [
            "https://link.springer.com/article/10.1007/s10462-026-11496-8",
            "https://link.springer.com/article/10.1007/s00477-026-03331-x",
            "https://www.nature.com/articles/s44407-026-00076-3",
            "https://doi.org/10.3390/su14169951",
        ],
    },
    {
        "name": "ai-for-waste-management",
        "title": "AI for Waste Management",
        "description": "Waste classification, automated sorting, route optimization, recycling quality, and lifecycle assessment with ML and robotics.",
        "devin_body": r'''
## When to use

You are designing waste-sorting systems, optimizing collection routes, or improving recycling quality and material recovery.

## Key concepts

- **Waste classification and detection**: CNNs and vision transformers for recyclable categories.
- **Robotic sorting**: AI-guided pick-and-place for municipal/recyclable waste.
- **Route and logistics optimization**: vehicle routing and bin-level IoT scheduling.
- **Lifecycle assessment (LCA)**: quantify environmental impact of waste pathways.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Classify waste stream by material from sensor features
clf = RandomForestClassifier(n_estimators=300)
clf.fit(X, y_material)
```

## Tuning notes

- Handle class imbalance and occlusion in cluttered waste images.
- Integrate hyperspectral/NIR sensors with RGB for material discrimination.
- Calibrate route-optimization models with real traffic and bin-fill data.
- Track purity and contamination of sorted output for downstream valorization.

## Verification

1. Train a waste image classifier and report top-k accuracy across material classes.
2. Benchmark an AI sorter's purity and recovery against manual baseline.
3. Optimize collection routes and measure fuel/time savings in simulation.
''',
        "references": [
            "https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2025.1670679/full",
            "https://www.mdpi.com/2079-9276/10/4/28",
            "https://link.springer.com/article/10.1007/s00521-024-10855-2",
            "https://research.google/blog/robotic-deep-rl-at-scale-sorting-waste-and-recyclables-with-a-fleet-of-robots/",
        ],
    },
    {
        "name": "ai-for-circular-economy",
        "title": "AI for Circular Economy",
        "description": "Material flow optimization, predictive recycling, product lifecycle extension, and circular supply-chain design with AI.",
        "devin_body": r'''
## When to use

You are optimizing material flows, designing reverse logistics, extending product life, or reducing waste across supply chains.

## Key concepts

- **Material flow analysis (MFA)**: track resource inflows, stocks, and outflows.
- **Predictive maintenance and reuse**: forecast product condition and remanufacturing potential.
- **Reverse supply chains**: collection, sorting, recycling, and remanufacturing optimization.
- **Reinforcement learning and MDPs**: dynamic decisions under uncertainty.

## Code pattern

```python
from sklearn.linear_model import LinearRegression

# Predict material recovery rate from product and process features
model = LinearRegression().fit(X, y_recovery)
```

## Tuning notes

- Embed lifecycle assessment (LCA) and carbon accounting into optimization.
- Model uncertainty in material quality, demand, and policy scenarios.
- Use multi-agent or industrial-symbiosis models for regional networks.
- Balance economic, environmental, and equity objectives.

## Verification

1. Build a material-flow prediction model and validate with waste-arisings data.
2. Optimize a reverse-logistics network and compare cost and carbon to baseline.
3. Estimate product remanufacturing potential and verify with refurbishment records.
''',
        "references": [
            "https://doi.org/10.1007/s43621-025-01846-x",
            "https://doi.org/10.3390/engproc2025120044",
            "https://www.mdpi.com/2673-4591/120/1/44",
            "https://www.mdpi.com/2673-4591/97/1/12",
        ],
    },
]
