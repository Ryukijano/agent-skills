SKILLS = [
    {
        "name": "ai-for-plant-breeding",
        "title": "AI for Plant Breeding",
        "description": "Genomic selection, phenotype prediction, multi-environment trial analysis, and marker-assisted breeding with machine and deep learning.",
        "devin_body": r'''## When to use

You are selecting parents, predicting progeny performance, analysing genotype-by-environment interactions, or optimising crossing schemes in a crop or forage breeding programme.

## Usage

- **Genomic prediction**: predict quantitative traits from dense marker data using ML or statistical learning methods.
- **Multi-environment trial analysis**: model genotype x environment (GxE) interactions and stability across locations and years.
- **High-throughput phenotyping integration**: fuse remote sensing, spectral, and drone-derived traits with genotypes.
- **Parent selection and genetic diversity**: use prediction and diversity metrics to design optimal crosses.

## Steps

1. Collect high-quality genotype (e.g., SNP array, resequencing) and phenotype data across multiple environments.
2. Quality-control markers and phenotypes; account for population structure and kinship.
3. Train and validate prediction models for target traits (yield, quality, stress tolerance).
4. Evaluate prediction accuracy in independent environments and examine GxE patterns.
5. Integrate predictions into crossing plans and selection decisions, updating as new data arrive.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_predict

X = df[genomic_markers]
y = df["yield_kg_ha"]

y_pred = cross_val_predict(
    GradientBoostingRegressor(random_state=42), X, y, cv=5
)
```

## Tuning notes

- Include pedigree or kinship to borrow information across related lines; regularise when p >> n.
- Use environment-specific models and covariance structures to capture GxE.
- Combine genomic, transcriptomic, and phenomic data with multimodal fusion.
- Track linkage disequilibrium and marker density effects on prediction stability.

## Verification

1. Compare genomic prediction accuracy to a pedigree-BLUP or GBLUP baseline.
2. Run leave-one-environment-out cross-validation to assess GxE generalisation.
3. Estimate expected genetic gain from the predicted selection index.

## References

- https://www.sciencedirect.com/science/article/pii/S1360138524003455
- https://doi.org/10.1093/genetics/iyae161
- https://link.springer.com/article/10.1186/s12864-020-07319-x
- https://www.sciencedirect.com/science/article/pii/S1674205224000807
''',
        "references": [
            "https://www.sciencedirect.com/science/article/pii/S1360138524003455",
            "https://doi.org/10.1093/genetics/iyae161",
            "https://link.springer.com/article/10.1186/s12864-020-07319-x",
            "https://www.sciencedirect.com/science/article/pii/S1674205224000807",
        ],
    },
    {
        "name": "ai-for-crop-protection",
        "title": "AI for Crop Protection",
        "description": "Machine and deep learning for detecting crop diseases, pests, weeds, and abiotic stresses and for supporting timely, targeted protection decisions.",
        "devin_body": r'''## When to use

You need to diagnose crop health problems, detect disease or stress symptoms, or support fungicide, pesticide, and cultural control decisions from imagery and sensor data.

## Usage

- **Image-based disease diagnosis**: classify leaf, canopy, and fruit symptoms from smartphone, drone, or satellite images.
- **Drone and remote-sensing crop scouting**: map stress, disease, and weed patches across fields.
- **Pathogen and symptom identification**: integrate molecular or environmental signals with vision models.
- **Protection timing support**: build decision support for spray windows and intervention thresholds.

## Steps

1. Collect representative images or sensor data from healthy and diseased plants under field conditions.
2. Curate and augment a labelled dataset covering symptom variability and growth stages.
3. Train a classification, segmentation, or object-detection model suited to the symptom scale.
4. Validate in independent fields, seasons, and cultivars to measure robustness.
5. Deploy an edge, mobile, or cloud inference pipeline linked to agronomic advisories.

## Code pattern

```python
import torch
from torchvision import models, transforms
from PIL import Image

model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])
img = preprocess(Image.open("leaf.jpg")).unsqueeze(0)
```

## Tuning notes

- Expect strong class imbalance and domain shift between controlled and field imagery.
- Use transfer learning and few-shot adaptation for rare diseases.
- Include interpretability (Grad-CAM, SHAP) to build trust with agronomists.
- Monitor model drift as new races, pathogens, and environmental conditions emerge.

## Verification

1. Report precision, recall, and F1 on a held-out field dataset.
2. Compare AI diagnoses to expert ratings and laboratory confirmations.
3. Track fungicide or pesticide reduction and yield protection in a field trial.

## References

- https://link.springer.com/article/10.1007/s10343-025-01247-0
- https://link.springer.com/article/10.1007/s43621-026-03623-w
- https://link.springer.com/article/10.1007/s42452-026-08684-0
- https://link.springer.com/article/10.1007/s10462-024-11100-x
''',
        "references": [
            "https://link.springer.com/article/10.1007/s10343-025-01247-0",
            "https://link.springer.com/article/10.1007/s43621-026-03623-w",
            "https://link.springer.com/article/10.1007/s42452-026-08684-0",
            "https://link.springer.com/article/10.1007/s10462-024-11100-x",
        ],
    },
    {
        "name": "ai-for-irrigation",
        "title": "AI for Irrigation",
        "description": "Machine learning for predicting crop water demand, scheduling irrigation, and optimising water use through IoT and weather data integration.",
        "devin_body": r'''## When to use

You want to improve irrigation scheduling, estimate crop evapotranspiration, or automate water application based on soil, weather, crop, and sensor data.

## Usage

- **Soil moisture and water demand prediction**: forecast short-term crop water requirements.
- **Irrigation scheduling**: recommend timing, depth, and frequency of irrigation events.
- **Deficit and precision irrigation**: optimise water use under scarcity constraints.
- **Smart valve and pump control**: integrate ML forecasts with automated actuators.

## Steps

1. Assemble soil, weather, crop-stage, and (optionally) remote-sensing time series.
2. Define the target: soil moisture, evapotranspiration, or applied water volume.
3. Train a regression or time-series model with season-aware train/test splits.
4. Generate irrigation schedules and quantify expected water savings and yield effects.
5. Deploy the model with sensor feeds and feedback loops for continuous improvement.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

X = df[["soil_moisture", "temp", "humidity", "solar_rad", "crop_stage"]]
y = df["water_need_mm"]

model = RandomForestRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Calibrate crop coefficients and soil water-holding capacity for each field zone.
- Use physics-informed or hybrid models that respect water-balance constraints.
- Propagate weather uncertainty into irrigation recommendations.
- Handle missing or drifting sensors with imputation and outlier detection.

## Verification

1. Compare predicted evapotranspiration to FAO-56 Penman-Monteith estimates.
2. Simulate a season of ML-driven irrigation and compare water use to a farmer schedule.
3. Validate yield and crop-stress outcomes in a split-field or randomised trial.

## References

- https://ideas.repec.org/a/eee/agiwat/v294y2024ics0378377424000453.html
- https://doi.org/10.1080/27525783.2025.2562418
- https://www.mdpi.com/1424-8220/24/23/7480
- https://www.mdpi.com/2624-7402/4/1/6
''',
        "references": [
            "https://ideas.repec.org/a/eee/agiwat/v294y2024ics0378377424000453.html",
            "https://doi.org/10.1080/27525783.2025.2562418",
            "https://www.mdpi.com/1424-8220/24/23/7480",
            "https://www.mdpi.com/2624-7402/4/1/6",
        ],
    },
    {
        "name": "ai-for-agricultural-robots",
        "title": "AI for Agricultural Robots",
        "description": "Perception, motion planning, and control for autonomous robots that weed, spray, scout, and harvest in field and greenhouse environments.",
        "devin_body": r'''## When to use

You are building or deploying an autonomous ground or aerial robot to perform precision tasks such as selective harvesting, weeding, spraying, or crop scouting.

## Usage

- **Vision-based detection and localisation**: locate crops, fruit, weeds, and obstacles.
- **Autonomous navigation**: follow crop rows and avoid hazards without continuous GPS.
- **Selective actuation**: trigger sprayers, cutters, or grippers based on real-time perception.
- **Field coverage and task planning**: optimise routes and schedules across fields.

## Steps

1. Specify the target crop, task, platform, and field operating conditions.
2. Design the sensor stack (cameras, LiDAR, IMU, GPS) and data pipeline.
3. Train perception models for the target objects and field conditions.
4. Integrate localisation, motion planning, and end-effector control.
5. Validate progressively in simulation, controlled environments, and production fields.

## Code pattern

```python
import cv2
import numpy as np

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)
# Use Hough transform or learned row detector for navigation
```

## Tuning notes

- Robustify perception against variable lighting, occlusion, dust, and foliage.
- Plan for GPS-denied navigation and wheel-slip on uneven terrain.
- Prioritise safety, human-robot interaction, and energy budgets in large fields.
- Iterate hardware and software together; simulation alone rarely transfers fully.

## Verification

1. Measure navigation accuracy along crop rows over repeated runs.
2. Report harvest, pick, or weed-detection success rate in field conditions.
3. Quantify traversal time, energy use, and crop damage relative to a baseline.

## References

- https://doi.org/10.1002/rob.22230
- https://onlinelibrary.wiley.com/doi/10.1002/rob.21525
- https://www.mdpi.com/2073-4395/14/10/2233
- https://www.mdpi.com/2218-6581/15/4/81
''',
        "references": [
            "https://doi.org/10.1002/rob.22230",
            "https://onlinelibrary.wiley.com/doi/10.1002/rob.21525",
            "https://www.mdpi.com/2073-4395/14/10/2233",
            "https://www.mdpi.com/2218-6581/15/4/81",
        ],
    },
    {
        "name": "ai-for-dairy",
        "title": "AI for Dairy",
        "description": "Machine learning for health, fertility, behaviour, and production monitoring in dairy cattle and dairy farm decision support.",
        "devin_body": r'''## When to use

You are monitoring individual dairy cows to detect mastitis, lameness, oestrus, or metabolic disorders, or to forecast milk yield and body condition.

## Usage

- **Mastitis and disease detection**: classify early health events from milk, sensor, or image data.
- **Reproductive management**: predict heat, calving, and optimal insemination timing.
- **Milk yield and body-condition scoring**: forecast production and body reserves.
- **Feeding and behaviour monitoring**: detect changes in rumination, activity, and feed intake.

## Steps

1. Collect animal-level data from milking systems, wearables, cameras, and farm records.
2. Engineer time-series and per-cow features (lactation stage, parity, days in milk).
3. Train classification or regression models for each target health or production outcome.
4. Validate with chronological splits and across multiple farms or breeds.
5. Deploy real-time alerts and integrate with herd management software.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

X = df[["milk_yield", "scc", "activity", "rumination", "days_in_milk"]]
y = df["mastitis_7d"]

model = RandomForestClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Dairy data are highly imbalanced; use class weights, resampling, or cost-sensitive learning.
- Account for lactation curve, parity, season, and herd management effects.
- Sensors and milking systems drift; monitor and recalibrate models routinely.
- Keep animal welfare and data privacy central to model design and deployment.

## Verification

1. Report early mastitis detection AUC on a temporally held-out herd.
2. Compare heat-detection recall to visual oestrus detection.
3. Validate milk-yield forecasts against actual test-day records.

## References

- https://www.mdpi.com/2077-0472/13/10/1858
- https://www.sciencedirect.com/science/article/pii/S0167587720309211
- https://www.mdpi.com/2076-2615/15/14/2033
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8747441/
''',
        "references": [
            "https://www.mdpi.com/2077-0472/13/10/1858",
            "https://www.sciencedirect.com/science/article/pii/S0167587720309211",
            "https://www.mdpi.com/2076-2615/15/14/2033",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC8747441/",
        ],
    },
    {
        "name": "ai-for-poultry",
        "title": "AI for Poultry",
        "description": "AI for flock health, welfare, behaviour, environmental control, and productivity in broiler, layer, and turkey production.",
        "devin_body": r'''## When to use

You are monitoring poultry flocks to detect disease, assess welfare, track behaviour, or manage feeding, ventilation, and stocking density.

## Usage

- **Disease and mortality prediction**: detect sick birds or predict flock mortality from behaviour and environment.
- **Welfare and behaviour assessment**: monitor feather condition, gait, dust bathing, and stress indicators.
- **Vocalisation and sound analysis**: identify distress or respiratory issues from audio.
- **Feed, water, and environment control**: optimise intake and climate using sensor data.

## Steps

1. Install or collect video, audio, sensor, and environmental data from poultry houses.
2. Annotate behaviour, health, or welfare events at individual or flock level.
3. Train detection, classification, or regression models suited to poultry house conditions.
4. Validate on separate flocks, houses, and production cycles.
5. Provide clear, actionable alerts and integrate with farm management routines.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingClassifier

X = df[["temp", "humidity", "stocking_density", "feed_consumption", "water_consumption"]]
y = df["high_mortality_risk"]

model = GradientBoostingClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Handle heavy occlusion, variable lighting, and fast movement in dense flocks.
- Welfare assessments must align with recognised protocols (e.g., Welfare Quality).
- Generalise across breeds, housing systems, and seasonal conditions.
- Avoid welfare interventions that increase stress or conflict with regulatory standards.

## Verification

1. Detect sick or lame birds from video and compare to veterinary assessment.
2. Compare automated welfare scores to manual audit results.
3. Validate mortality or disease prediction on a held-out flock cycle.

## References

- https://doi.org/10.1016/j.japr.2025.100602
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11700577/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6770384/
- https://www.mdpi.com/2071-1050/12/4/1413
''',
        "references": [
            "https://doi.org/10.1016/j.japr.2025.100602",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11700577/",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC6770384/",
            "https://www.mdpi.com/2071-1050/12/4/1413",
        ],
    },
    {
        "name": "ai-for-aquaculture",
        "title": "AI for Aquaculture",
        "description": "Machine learning for water quality, feeding, disease, and stock management in fish, shrimp, and shellfish farming.",
        "devin_body": r'''## When to use

You are operating or designing a fish, shrimp, or shellfish farm and want to predict water quality, optimise feeding, detect disease, or estimate biomass.

## Usage

- **Water quality forecasting**: predict dissolved oxygen, pH, ammonia, and temperature dynamics.
- **Precision feeding and feed optimisation**: adjust rations based on appetite, biomass, and water conditions.
- **Disease early warning and health monitoring**: detect abnormal behaviour, gill conditions, or mortality trends.
- **Biomass and growth estimation**: estimate size distribution and stock weight from cameras and sensors.

## Steps

1. Deploy water-quality sensors, cameras, and/or acoustic devices in tanks, ponds, or cages.
2. Integrate time-series, image, and feeding records into a farm data platform.
3. Train models for each target: water forecast, feed response, health, or biomass.
4. Validate under different stocking densities, seasons, and species conditions.
5. Connect predictions to automated feeders, aerators, or management dashboards.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

X = df[["temperature", "dissolved_oxygen", "ph", "ammonia", "salinity"]]
y = df["oxygen_forecast_1h"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Calibrate species-specific growth and metabolism; salmon requirements differ from shrimp.
- Account for sensor fouling, biofouling, and harsh aquatic environments.
- Use hybrid models that combine mechanistic bioenergetics with ML.
- Consider edge computing for remote sites with limited connectivity.

## Verification

1. Forecast water quality and compare to measured sensor values.
2. Track feed conversion ratio and growth under ML-based feeding.
3. Detect mortality or disease events earlier than manual observation.

## References

- https://doi.org/10.1016/j.fraope.2026.100567
- https://www.sciencedirect.com/science/article/abs/pii/S0044848625014887
- https://doi.org/10.1016/j.aiia.2025.01.012
- https://doi.org/10.5772/intechopen.1014536
''',
        "references": [
            "https://doi.org/10.1016/j.fraope.2026.100567",
            "https://www.sciencedirect.com/science/article/abs/pii/S0044848625014887",
            "https://doi.org/10.1016/j.aiia.2025.01.012",
            "https://doi.org/10.5772/intechopen.1014536",
        ],
    },
    {
        "name": "ai-for-livestock",
        "title": "AI for Livestock",
        "description": "Machine learning for health, behaviour, welfare, grazing, and reproduction across cattle, pigs, sheep, goats, and other farm animals.",
        "devin_body": r'''## When to use

You are monitoring livestock health, behaviour, or productivity across species and want data-driven insights for individual or herd management.

## Usage

- **Animal health and disease detection**: identify lameness, respiratory issues, and metabolic disorders.
- **Behaviour and welfare monitoring**: classify feeding, resting, rumination, social, and heat behaviours.
- **Grazing and pasture management**: estimate intake, forage availability, and animal distribution.
- **Reproduction and growth tracking**: predict calving, farrowing, weight gain, and market readiness.

## Steps

1. Choose sensors appropriate to the species and environment (wearables, cameras, microphones, scales).
2. Identify and track individual animals with RFID, computer vision, or biometrics.
3. Engineer features and train models per target health, behaviour, or production outcome.
4. Validate across farms, breeds, seasons, and production systems.
5. Deploy alerts and integrate with farm management software and veterinary workflows.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

X = df[["activity", "feed_intake", "water_intake", "body_temp", "weight"]]
y = df["health_status"]

model = RandomForestClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Maintain per-animal models while allowing herd-level aggregation.
- Address species differences, housing types, and climatic variation.
- Handle long-tailed health events and rare abnormal behaviours.
- Ensure welfare, ethical review, and data governance for animal data.

## Verification

1. Detect a target disease or condition and report AUC on a held-out group of animals.
2. Compare automated behaviour classification to expert-annotated video.
3. Test model transfer to a different breed or farm without full retraining.

## References

- https://www.sciencedirect.com/science/article/pii/S0168169920317099
- https://doi.org/10.5713/ab.25.0289
- https://doi.org/10.1016/j.aiia.2026.04.013
- https://www.mdpi.com/1424-8220/23/12/5732
''',
        "references": [
            "https://www.sciencedirect.com/science/article/pii/S0168169920317099",
            "https://doi.org/10.5713/ab.25.0289",
            "https://doi.org/10.1016/j.aiia.2026.04.013",
            "https://www.mdpi.com/1424-8220/23/12/5732",
        ],
    },
    {
        "name": "ai-for-viticulture",
        "title": "AI for Viticulture",
        "description": "AI for vineyard monitoring, grape and canopy sensing, disease detection, yield and quality prediction, and harvest decision support.",
        "devin_body": r'''## When to use

You are managing a vineyard and want to monitor vine health, detect diseases, estimate yield and grape quality, or optimise irrigation, fertilisation, and harvest timing.

## Usage

- **Canopy and berry detection**: locate and count grape bunches from images and point clouds.
- **Disease and pest monitoring**: detect powdery mildew, downy mildew, and grapevine pests.
- **Yield and quality prediction**: forecast grape quantity and maturity (sugar, acidity).
- **Irrigation, fertilisation, and harvest scheduling**: support precision management and winery logistics.

## Steps

1. Collect drone, satellite, or proximal sensing data across vineyard blocks.
2. Gather weather, soil, and phenology records and link them to management zones.
3. Train detection and regression models for the specific grape variety and terroir.
4. Validate predictions at harvest and across multiple vintages.
5. Integrate outputs into vineyard management plans and winery receiving schedules.

## Code pattern

```python
import numpy as np

red = image[..., 2]   # red band
nir = image[..., 3]   # near-infrared band
ndvi = (nir - red) / (nir + red + 1e-8)
```

## Tuning notes

- Capture vineyard spatial heterogeneity (soil, slope, aspect, cultivar, age).
- Use multi-year data to separate seasonal effects from management effects.
- Calibrate maturity and quality models with laboratory measurements.
- Integrate with existing winegrowing practices and sustainability goals.

## Verification

1. Detect downy mildew or leafroll and compare to vineyard scouting.
2. Estimate yield per vine and compare to harvest weights.
3. Predict grape sugar and acidity and validate with lab results.

## References

- https://doi.org/10.1111/1541-4337.70523
- https://doi.org/10.3390/horticulturae12060719
- https://doi.org/10.1016/j.aiia.2025.08.001
- https://www.mdpi.com/2076-3417/14/22/10277
''',
        "references": [
            "https://doi.org/10.1111/1541-4337.70523",
            "https://doi.org/10.3390/horticulturae12060719",
            "https://doi.org/10.1016/j.aiia.2025.08.001",
            "https://www.mdpi.com/2076-3417/14/22/10277",
        ],
    },
    {
        "name": "ai-for-pest-management",
        "title": "AI for Pest Management",
        "description": "Machine and deep learning for pest detection, identification, population monitoring, and integrated pest management decision support.",
        "devin_body": r'''## When to use

You need to detect, identify, count, or forecast insect pests to inform scouting, traps, biological control, or pesticide application decisions.

## Usage

- **Insect pest image classification**: identify pest species from trap, camera, or smartphone images.
- **Automated pest monitoring**: process pheromone-trap, suction-trap, and smart-trap data.
- **Pest risk and population forecasting**: predict outbreaks using weather, crop, and trap data.
- **IPM decision support**: recommend thresholds, biocontrol, and targeted chemical interventions.

## Steps

1. Deploy traps, cameras, or sensors in representative field locations.
2. Build a labelled image or count dataset covering target species and look-alikes.
3. Train species classification or object-counting models.
4. Integrate weather, crop-stage, and historical trap data for risk forecasting.
5. Generate field-level risk maps and intervention recommendations for scouts.

## Code pattern

```python
from ultralytics import YOLO

model = YOLO("yolov8n-cls.pt")
model.train(data="pest_images", epochs=50, imgsz=224)
```

## Tuning notes

- Many pest species are rare and visually similar; use transfer learning and taxonomic experts.
- Avoid harming beneficial insects and pollinators in model training and deployment.
- Pest populations are dynamic; refresh models and thresholds by season and region.
- Combine economic thresholds with model confidence for decision support.

## Verification

1. Report precision and recall for pest detection on field-collected images.
2. Compare model-based trap counts to manual counts.
3. Evaluate spray-timing recommendations against a scouting-only baseline.

## References

- https://www.mdpi.com/2073-4395/15/7/1629
- https://resjournals.onlinelibrary.wiley.com/doi/10.1111/afe.12630
- https://www.sciencedirect.com/science/article/abs/pii/S1161030126000596
- https://doi.org/10.22271/27889289.2026.v6.i3a.259
''',
        "references": [
            "https://www.mdpi.com/2073-4395/15/7/1629",
            "https://resjournals.onlinelibrary.wiley.com/doi/10.1111/afe.12630",
            "https://www.sciencedirect.com/science/article/abs/pii/S1161030126000596",
            "https://doi.org/10.22271/27889289.2026.v6.i3a.259",
        ],
    },
    {
        "name": "ai-for-soil-health",
        "title": "AI for Soil Health",
        "description": "Machine learning for predicting soil carbon, nutrients, biology, compaction, erosion risk, and overall soil health from sensors and remote sensing.",
        "devin_body": r'''## When to use

You are assessing soil health indicators, mapping soil properties, monitoring carbon sequestration, or guiding regenerative and precision management.

## Usage

- **Soil organic carbon and organic matter prediction**: map SOC/SOM from spectra and covariates.
- **Nutrient and fertility status**: predict N, P, K, pH, and micronutrients.
- **Soil biology and microbiome**: infer biological activity and diversity from proxy data.
- **Compaction, erosion, and hydrology risk**: model soil structural degradation.
- **Management impact assessment**: evaluate cover crops, reduced tillage, and amendments.

## Steps

1. Collect soil samples with laboratory reference measurements and location data.
2. Add covariates: remote-sensing imagery, topography, climate, geology, and management history.
3. Preprocess spectroscopic or sensor data and engineer spatial features.
4. Train spatial prediction models and quantify uncertainty.
5. Generate soil health maps and management recommendations.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

X = df[["reflectance_1", "reflectance_2", "elevation", "clay_percent", "ndvi"]]
y = df["soil_organic_carbon_pct"]

model = RandomForestRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Account for spatial autocorrelation; avoid naive random cross-validation.
- Standardise and calibrate spectroscopic sensors across instruments.
- Depth matters; model by horizon when possible.
- Interpret models for agronomic relevance (feature importance, SHAP).

## Verification

1. Compare predicted soil carbon maps to an independent set of soil cores.
2. Validate nutrient predictions against wet-chemistry lab results.
3. Track changes in predicted soil health over years of management.

## References

- https://doi.org/10.1002/advs.202504152
- https://doi.org/10.3390/app16115412
- https://link.springer.com/article/10.1007/s11368-024-03913-8
- https://www.mdpi.com/2077-0472/15/5/567
''',
        "references": [
            "https://doi.org/10.1002/advs.202504152",
            "https://doi.org/10.3390/app16115412",
            "https://link.springer.com/article/10.1007/s11368-024-03913-8",
            "https://www.mdpi.com/2077-0472/15/5/567",
        ],
    },
    {
        "name": "ai-for-agricultural-economics",
        "title": "AI for Agricultural Economics",
        "description": "Machine learning and econometric ML for farm decision support, risk, policy, market analysis, adoption, and the economics of digital agriculture.",
        "devin_body": r'''## When to use

You are evaluating the economic outcomes of farm technologies, forecasting prices or yields, modelling adoption and risk, or building decision support for farmers and policymakers.

## Usage

- **Yield and price forecasting**: predict crop yields, commodity prices, and revenue at regional or farm scale.
- **Risk and insurance analytics**: estimate weather, yield, and price risk for crop insurance or hedging.
- **Adoption and impact evaluation**: model technology adoption, treatment effects, and farm-level impact.
- **Decision support systems**: build cost-benefit and farm-planning tools that integrate agronomic and economic models.
- **Policy and market analysis**: assess subsidies, trade, and supply-chain effects.

## Steps

1. Collect farm accounts, market, policy, weather, and agronomic data.
2. Define the economic outcome (profit, cost, revenue, adoption, risk).
3. Build predictive, causal, or optimisation models suited to the question.
4. Validate on held-out farms, regions, or time periods.
5. Translate results into actionable recommendations and policy briefs.

## Code pattern

```python
import pandas as pd
import statsmodels.api as sm

X = sm.add_constant(df[["input_cost", "weather_index", "output_price"]])
y = df["farm_profit"]

model = sm.OLS(y, X).fit()
print(model.summary())
```

## Tuning notes

- Address endogeneity, omitted variables, and selection bias when estimating causal effects.
- Reflect heterogeneity across farm sizes, regions, and production systems.
- Incorporate farmer behaviour, risk aversion, and adoption constraints.
- Validate with out-of-sample predictions and robustness checks.

## Verification

1. Forecast farm revenue and compare to actual end-of-season values.
2. Estimate price or input-cost elasticity and interpret economic significance.
3. Compare a DSS recommendation to historical farmer practice in a pilot region.

## References

- https://www.annualreviews.org/content/journals/10.1146/annurev-resource-101623-092515
- https://doi.org/10.1007/s44279-026-00510-w
- https://doi.org/10.62486/latia2025326
- https://baylislab.ace.illinois.edu/wp-content/uploads/2019/09/Storm-et-al-ML-Review.pdf
''',
        "references": [
            "https://www.annualreviews.org/content/journals/10.1146/annurev-resource-101623-092515",
            "https://doi.org/10.1007/s44279-026-00510-w",
            "https://doi.org/10.62486/latia2025326",
            "https://baylislab.ace.illinois.edu/wp-content/uploads/2019/09/Storm-et-al-ML-Review.pdf",
        ],
    },
]
