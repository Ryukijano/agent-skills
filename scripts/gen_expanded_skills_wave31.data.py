SKILLS = [
    {
        "name": 'ai-for-biodiversity',
        "title": 'AI for Biodiversity',
        "description": 'Identify species and assess abundance from camera-trap and acoustic recordings to track biodiversity change and flag at-risk populations.',
        "devin_body": r'''## When to use

You are assessing species distributions, monitoring biodiversity change, or automating taxonomic identification from images, audio, or genetic samples.

## Usage

- Assemble camera-trap, acoustic, eDNA, and occurrence datasets.
- Train deep-learning classifiers and detectors for species ID.
- Relate occurrence records to environmental covariates with SDMs.
- Compute biodiversity indicators (alpha/beta, occupancy, abundance).

## Steps

1. Assemble camera-trap, acoustic, eDNA, and occurrence datasets.
2. Train deep-learning classifiers and detectors for species ID.
3. Relate occurrence records to environmental covariates with SDMs.
4. Compute biodiversity indicators (alpha/beta, occupancy, abundance).
5. Validate against field surveys and reference datasets.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Compute biodiversity trends and validate with independent field surveys.''',
        "references": [
            'https://www.mdpi.com/1424-8220/24/24/8122',
            'https://doi.org/10.1002/2688-8319.70167',
            'https://github.com/google/cameratrapai/',
            'https://arxiv.org/abs/2603.20509',
        ],
    },
    {
        "name": 'ai-for-ecosystem-restoration',
        "title": 'AI for Ecosystem Restoration',
        "description": 'Use AI to measure restoration success, track rewilding progress, or prioritize interventions for degraded ecosystems.',
        "devin_body": r'''## When to use

You need to measure restoration success, track rewilding progress, or prioritize interventions for degraded ecosystems.

## Usage

- Define reference conditions and restoration baselines.
- Stack remote-sensing indices (NDVI, NDWI, LiDAR) over time.
- Track vegetation structure and species reassembly.
- Compare restored, reference, and degraded sites.

## Steps

1. Define reference conditions and restoration baselines.
2. Stack remote-sensing indices (NDVI, NDWI, LiDAR) over time.
3. Track vegetation structure and species reassembly.
4. Compare restored, reference, and degraded sites.
5. Validate recovery with field-measured biodiversity.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Relate remote-sensing recovery scores to field-measured biodiversity.''',
        "references": [
            'https://doi.org/10.1371/journal.pone.0253148',
            'https://www.nature.com/articles/s41467-023-41693-w',
            'https://www.mdpi.com/2072-4292/18/2/346',
            'https://doi.org/10.5194/wbf2026-927',
        ],
    },
    {
        "name": 'ai-for-conservation-planning',
        "title": 'AI for Conservation Planning',
        "description": 'Use AI to decide where to protect, restore, or manage land/sea to meet biodiversity targets under budget and equity constraints.',
        "devin_body": r'''## When to use

You must decide where to protect, restore, or manage land/sea to meet biodiversity targets under budget and equity constraints.

## Usage

- Compile species, cost, threat, and connectivity data.
- Model site irreplaceability and trade-offs.
- Run optimization (Marxan/Zonation/CAPTAIN) under budget.
- Generate prioritization maps for protection and restoration.

## Steps

1. Compile species, cost, threat, and connectivity data.
2. Model site irreplaceability and trade-offs.
3. Run optimization (Marxan/Zonation/CAPTAIN) under budget.
4. Generate prioritization maps for protection and restoration.
5. Stress-test priorities under climate and land-use scenarios.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Test robustness of priorities under climate-change scenarios.''',
        "references": [
            'https://doi.org/10.1016/j.tree.2024.12.002',
            'https://www.nature.com/articles/s41893-022-00851-6',
            'https://doi.org/10.1029/2025ef007560',
            'https://www.ijcai.org/proceedings/2025/1086.pdf',
        ],
    },
    {
        "name": 'ai-for-natural-hazards',
        "title": 'AI for Natural Hazards',
        "description": 'Predict landslide and wildfire risk from satellite and sensor data to trigger early warnings and protect infrastructure.',
        "devin_body": r'''## When to use

You are mapping multi-hazard risk, forecasting imminent events, or designing early warning systems for landslides, floods, wildfires, or subsidence.

## Usage

- Fuse terrain, hydrology, vegetation, and Sentinel-1/2 data.
- Model susceptibility for landslides, floods, wildfires, and subsidence.
- Calibrate warning thresholds with historical events.
- Build multi-hazard susceptibility maps.

## Steps

1. Fuse terrain, hydrology, vegetation, and Sentinel-1/2 data.
2. Model susceptibility for landslides, floods, wildfires, and subsidence.
3. Calibrate warning thresholds with historical events.
4. Build multi-hazard susceptibility maps.
5. Validate lead time and accuracy with stakeholders.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Test an early-warning trigger against past events and report lead time.''',
        "references": [
            'https://link.springer.com/article/10.1038/s41598-025-15381-2',
            'https://iopscience.iop.org/article/10.1088/1748-9326/ae5f7f/meta',
            'https://doi.org/10.1038/s41598-020-69233-2',
            'https://www.nature.com/articles/s41598-026-52139-w',
        ],
    },
    {
        "name": 'ai-for-wetlands',
        "title": 'AI for Wetlands',
        "description": 'Use AI to map wetland extent, tracking seasonal inundation, classify cover types, or detect hydrological change.',
        "devin_body": r'''## When to use

You are mapping wetland extent, tracking seasonal inundation, classifying cover types, or detecting hydrological change.

## Usage

- Stack Sentinel-1/2 and LiDAR time series.
- Map wetland extent with MNDWI/NDWI.
- Classify cover types (open water, vegetation, moist soil).
- Monitor intra- and inter-annual inundation.

## Steps

1. Stack Sentinel-1/2 and LiDAR time series.
2. Map wetland extent with MNDWI/NDWI.
3. Classify cover types (open water, vegetation, moist soil).
4. Monitor intra- and inter-annual inundation.
5. Validate against field surveys and gauged water levels.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Generate an annual inundation time series and compare to gauged water levels.''',
        "references": [
            'https://www.nature.com/articles/s41598-026-39257-1',
            'https://doi.org/10.31223/x5jx93',
            'https://www.mdpi.com/2072-4292/14/23/6104',
            'https://www.sei.org/tools/wetsat-ml-wetlands-flooding-extent-and-trends-using-satellite-observations-and-machine-learning/',
        ],
    },
    {
        "name": 'ai-for-coral-reefs',
        "title": 'AI for Coral Reefs',
        "description": 'Classify coral health and bleaching from underwater and drone imagery to quantify reef loss and guide conservation actions.',
        "devin_body": r'''## When to use

You need to classify benthic habitats, detect coral bleaching, or monitor reef recovery from underwater, drone, or satellite imagery.

## Usage

- Collect underwater, drone, and satellite imagery.
- Correct color and radiometry for underwater conditions.
- Train benthic classifiers and bleaching detectors.
- Aggregate point/pixel predictions to colony or transect scale.

## Steps

1. Collect underwater, drone, and satellite imagery.
2. Correct color and radiometry for underwater conditions.
3. Train benthic classifiers and bleaching detectors.
4. Aggregate point/pixel predictions to colony or transect scale.
5. Validate against in-situ bleaching and cover surveys.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Map coral cover change over time and validate with repeat surveys.''',
        "references": [
            'https://doi.org/10.48550/arxiv.2511.00021',
            'https://doi.org/10.3390/rs15092238',
            'https://www.mdpi.com/2077-1312/12/8/1266',
            'https://coralnet.ucsd.edu/source/2947/',
        ],
    },
    {
        "name": 'ai-for-glaciology',
        "title": 'AI for Glaciology',
        "description": 'Use AI to delineate glacier boundaries, estimating surface mass balance, classify ice facies, or project glacier change.',
        "devin_body": r'''## When to use

You are delineating glacier boundaries, estimating surface mass balance, classifying ice facies, or projecting glacier change.

## Usage

- Fuse optical, SAR, DEM, and meteorological reanalysis.
- Segment glacier outlines (clean ice, debris, snow/firn).
- Estimate surface mass balance with point and geodetic data.
- Track area and elevation change over time.

## Steps

1. Fuse optical, SAR, DEM, and meteorological reanalysis.
2. Segment glacier outlines (clean ice, debris, snow/firn).
3. Estimate surface mass balance with point and geodetic data.
4. Track area and elevation change over time.
5. Validate against manual inventories and in-situ stakes.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Map debris-covered ice and quantify area change over a decade.''',
        "references": [
            'https://doi.org/10.1038/s41467-024-54956-x',
            'https://doi.org/10.5194/egusphere-egu26-11039',
            'https://www.sciencedirect.com/science/article/pii/S1569843222001212',
            'https://tc.copernicus.org/articles/19/1675/2025/',
        ],
    },
    {
        "name": 'ai-for-desertification',
        "title": 'AI for Desertification',
        "description": 'Use AI to assess desertification sensitivity, map degraded land, or forecast land degradation in dryland regions.',
        "devin_body": r'''## When to use

You are assessing desertification sensitivity, mapping degraded land, or forecasting land degradation in dryland regions.

## Usage

- Combine NDVI, SAVI, BSI, LST, and management data.
- Classify desertification risk zones.
- Run temporal forecasting of land degradation.
- Identify hotspots and long-term trends.

## Steps

1. Combine NDVI, SAVI, BSI, LST, and management data.
2. Classify desertification risk zones.
3. Run temporal forecasting of land degradation.
4. Identify hotspots and long-term trends.
5. Cross-check with ground photos and land-cover maps.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Identify degradation hotspots and cross-check with field observations.''',
        "references": [
            'https://www.mdpi.com/2072-4292/17/19/3350',
            'https://www.mdpi.com/2072-4292/16/23/4525',
            'https://www.nature.com/articles/s41598-023-46319-1',
            'https://doi.org/10.1007/s12665-025-12766-4',
        ],
    },
    {
        "name": 'ai-for-ocean-conservation',
        "title": 'AI for Ocean Conservation',
        "description": 'Use AI to monitor marine protected areas, detect illegal fishing, tracking vessels, or assess marine ecosystem health.',
        "devin_body": r'''## When to use

You are monitoring marine protected areas, detecting illegal fishing, tracking vessels, or assessing marine ecosystem health.

## Usage

- Fuse AIS, SAR, and optical vessel data.
- Classify fishing vs. non-fishing behavior.
- Detect anomalous vessel activity in MPAs.
- Map marine habitats and species.

## Steps

1. Fuse AIS, SAR, and optical vessel data.
2. Classify fishing vs. non-fishing behavior.
3. Detect anomalous vessel activity in MPAs.
4. Map marine habitats and species.
5. Validate with patrol records and eDNA surveys.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Map marine habitat and validate with survey or eDNA data.''',
        "references": [
            'https://arxiv.org/abs/2312.03207',
            'https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1798458/full',
            'https://doi.org/10.1016/j.procs.2026.06.143',
            'https://allenai.org/skylight',
        ],
    },
    {
        "name": 'ai-for-air-quality',
        "title": 'AI for Air Quality',
        "description": 'Use AI to forecast pollutant levels, issuing air-quality alerts, or identify emission sources for urban and regional scales.',
        "devin_body": r'''## When to use

You are forecasting pollutant levels, issuing air-quality alerts, or identifying emission sources for urban and regional scales.

## Usage

- Ingest meteorology, emissions, and regulatory monitor data.
- Engineer diurnal, weekly, and seasonal features.
- Train spatiotemporal PM and pollutant forecasters.
- Attribute sources with receptor models and SHAP.

## Steps

1. Ingest meteorology, emissions, and regulatory monitor data.
2. Engineer diurnal, weekly, and seasonal features.
3. Train spatiotemporal PM and pollutant forecasters.
4. Attribute sources with receptor models and SHAP.
5. Compare forecasts to persistence and chemical-transport baselines.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Attribute sources and compare apportionment to receptor-model estimates.''',
        "references": [
            'https://link.springer.com/article/10.1007/s10462-026-11496-8',
            'https://link.springer.com/article/10.1007/s00477-026-03331-x',
            'https://www.nature.com/articles/s44407-026-00076-3',
            'https://doi.org/10.3390/su14169951',
        ],
    },
    {
        "name": 'ai-for-waste-management',
        "title": 'AI for Waste Management',
        "description": 'Use AI to design waste-sorting systems, optimize collection routes, or improve recycling quality and material recovery.',
        "devin_body": r'''## When to use

You are designing waste-sorting systems, optimizing collection routes, or improving recycling quality and material recovery.

## Usage

- Collect waste images and sensor data (RGB, NIR, hyperspectral).
- Train material classifiers and vision-transformer sorters.
- Optimize collection routes and bin scheduling.
- Track sorted-stream purity and contamination.

## Steps

1. Collect waste images and sensor data (RGB, NIR, hyperspectral).
2. Train material classifiers and vision-transformer sorters.
3. Optimize collection routes and bin scheduling.
4. Track sorted-stream purity and contamination.
5. Benchmark recovery and purity against manual sorting.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Optimize collection routes and measure fuel/time savings in simulation.''',
        "references": [
            'https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2025.1670679/full',
            'https://www.mdpi.com/2079-9276/10/4/28',
            'https://link.springer.com/article/10.1007/s00521-024-10855-2',
            'https://research.google/blog/robotic-deep-rl-at-scale-sorting-waste-and-recyclables-with-a-fleet-of-robots/',
        ],
    },
    {
        "name": 'ai-for-circular-economy',
        "title": 'AI for Circular Economy',
        "description": 'Use AI to optimize material flows, design reverse logistics, extend product life, or reducing waste across supply chains.',
        "devin_body": r'''## When to use

You are optimizing material flows, designing reverse logistics, extending product life, or reducing waste across supply chains.

## Usage

- Map material inflows, stocks, and outflows.
- Predict product condition and remanufacturing potential.
- Optimize reverse logistics and recycling flows.
- Embed LCA and carbon accounting into decisions.

## Steps

1. Map material inflows, stocks, and outflows.
2. Predict product condition and remanufacturing potential.
3. Optimize reverse logistics and recycling flows.
4. Embed LCA and carbon accounting into decisions.
5. Validate with waste-arisings and refurbishment records.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
3. Estimate product remanufacturing potential and verify with refurbishment records.''',
        "references": [
            'https://doi.org/10.1007/s43621-025-01846-x',
            'https://doi.org/10.3390/engproc2025120044',
            'https://www.mdpi.com/2673-4591/120/1/44',
            'https://www.mdpi.com/2673-4591/97/1/12',
        ],
    },
]
