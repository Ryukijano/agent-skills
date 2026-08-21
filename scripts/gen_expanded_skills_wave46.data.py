SKILLS = [
    {
        "name": "ai-for-plant-breeding",
        "title": "AI for Plant Breeding",
        "description": "Accelerate crop improvement by predicting trait performance, genomic breeding values, and envirotype effects.",
        "devin_body": r'''## When to use

You are selecting parents, predicting progeny performance, analysing genotype-by-environment interactions, or optimising crossing schemes in a crop or forage breeding programme.

## Usage

- Run genomic prediction with rrBLUP, BOLT-LMM, or AutoGP.
- Optimize training populations and cross designs.
- Integrate enviromic covariates and multi-environment trials.
- Predict genotype-by-environment interaction.
- Select parents and lines with multi-trait indices.

## Steps

1. Collect genotypic, phenotypic, and environmental data.
2. Impute and filter markers; build kinship or genomic relationship matrices.
3. Train genomic prediction or GWAS models.
4. Predict breeding values across environments.
5. Validate with cross-validation and independent trials.

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

''',
        "references": ["https://www.sciencedirect.com/science/article/pii/S1360138524003455", "https://doi.org/10.1093/genetics/iyae161", "https://link.springer.com/article/10.1186/s12864-020-07319-x", "https://www.sciencedirect.com/science/article/pii/S1674205224000807"],
    },
    {
        "name": "ai-for-crop-protection",
        "title": "AI for Crop Protection",
        "description": "Detect crop diseases and pests from imagery, sensors, and field scouting.",
        "devin_body": r'''## When to use

You need to diagnose crop health problems, detect disease or stress symptoms, or support fungicide, pesticide, and cultural control decisions from imagery and sensor data.

## Usage

- Diagnose diseases with PlantVillage Nuru or custom CNNs.
- Detect weeds and pests from drone and smartphone imagery.
- Predict disease pressure from weather and spore traps.
- Guide variable-rate spraying and IPM decisions.
- Build field-level risk maps.

## Steps

1. Collect crop images, weather, and scouting records.
2. Label symptoms and train classification/segmentation models.
3. Validate on held-out locations and seasons.
4. Deploy via mobile app, drone, or tractor-mounted sensors.
5. Update with new pest/disease images.

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

''',
        "references": ["https://link.springer.com/article/10.1007/s10343-025-01247-0", "https://link.springer.com/article/10.1007/s43621-026-03623-w", "https://link.springer.com/article/10.1007/s42452-026-08684-0", "https://link.springer.com/article/10.1007/s10462-024-11100-x"],
    },
    {
        "name": "ai-for-irrigation",
        "title": "AI for Irrigation",
        "description": "Optimize water use and irrigation schedules from weather, soil, and crop data.",
        "devin_body": r'''## When to use

You want to improve irrigation scheduling, estimate crop evapotranspiration, or automate water application based on soil, weather, crop, and sensor data.

## Usage

- Predict evapotranspiration with NeuralFAO56 or pyfao56.
- Schedule irrigation from soil moisture and weather forecasts.
- Detect water stress with satellite and drone imagery.
- Optimize deficit irrigation for yield and water savings.
- Integrate with drip, pivot, and automated valve systems.

## Steps

1. Collect weather, soil moisture, and crop growth data.
2. Compute reference ET and crop coefficients.
3. Train models for ET, soil moisture, or yield response.
4. Generate irrigation prescriptions and triggers.
5. Validate against soil moisture and yield outcomes.

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

''',
        "references": ["https://ideas.repec.org/a/eee/agiwat/v294y2024ics0378377424000453.html", "https://doi.org/10.1080/27525783.2025.2562418", "https://www.mdpi.com/1424-8220/24/23/7480", "https://www.mdpi.com/2624-7402/4/1/6"],
    },
    {
        "name": "ai-for-agricultural-robots",
        "title": "AI for Agricultural Robots",
        "description": "Enable autonomous robots for weeding, harvesting, and navigation in crop fields.",
        "devin_body": r'''## When to use

You are building or deploying an autonomous ground or aerial robot to perform precision tasks such as selective harvesting, weeding, spraying, or crop scouting.

## Usage

- Build perception with ROS 2, YOLO-World, and SAM.
- Plan navigation and manipulation in unstructured fields.
- Detect and localize fruits, weeds, and crop rows.
- Integrate with farm machinery and RTK-GPS.
- Evaluate with field benchmarks and safety standards.

## Steps

1. Select robot platform and task (weeding, picking, scouting).
2. Collect field images and sensor data.
3. Train perception and control models.
4. Simulate in Gazebo or field test.
5. Validate precision, speed, and crop damage.

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

''',
        "references": ["https://doi.org/10.1002/rob.22230", "https://onlinelibrary.wiley.com/doi/10.1002/rob.21525", "https://www.mdpi.com/2073-4395/14/10/2233", "https://www.mdpi.com/2218-6581/15/4/81"],
    },
    {
        "name": "ai-for-dairy",
        "title": "AI for Dairy",
        "description": "Monitor dairy cattle health, reproduction, and behavior with computer vision and wearables.",
        "devin_body": r'''## When to use

You are monitoring individual dairy cows to detect mastitis, lameness, oestrus, or metabolic disorders, or to forecast milk yield and body condition.

## Usage

- Detect mastitis, lameness, and heat with AiHerd or smaXtec.
- Track feeding, rumination, and activity with bolus/IMU sensors.
- Monitor body condition and mobility from cameras.
- Predict calving and metabolic disorders.
- Generate to-do lists and treatment alerts.

## Steps

1. Install cameras, wearables, or bolus sensors in the barn.
2. Collect and label health, behavior, and production records.
3. Train detection and prediction models.
4. Deploy dashboards and alert systems.
5. Validate against veterinarian diagnoses and production metrics.

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

''',
        "references": ["https://www.mdpi.com/2077-0472/13/10/1858", "https://www.sciencedirect.com/science/article/pii/S0167587720309211", "https://www.mdpi.com/2076-2615/15/14/2033", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8747441/"],
    },
    {
        "name": "ai-for-poultry",
        "title": "AI for Poultry",
        "description": "Monitor poultry welfare, behavior, and health with computer vision and edge sensors.",
        "devin_body": r'''## When to use

You are monitoring poultry flocks to detect disease, assess welfare, track behaviour, or manage feeding, ventilation, and stocking density.

## Usage

- Track feeding, drinking, and activity with computer vision.
- Detect coccidiosis and salmonellosis with Edge Impulse.
- Monitor environmental conditions (temperature, ammonia, light).
- Count and locate birds with UWB/IMU wearables.
- Assess gait, feather condition, and stress.

## Steps

1. Place cameras, wearables, or environmental sensors in the house.
2. Collect and label behavior and health outcomes.
3. Train edge-deployed classification and detection models.
4. Integrate with farm management software.
5. Validate against veterinary checks and welfare audits.

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

''',
        "references": ["https://doi.org/10.1016/j.japr.2025.100602", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11700577/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6770384/", "https://www.mdpi.com/2071-1050/12/4/1413"],
    },
    {
        "name": "ai-for-aquaculture",
        "title": "AI for Aquaculture",
        "description": "Optimize feeding, water quality, and disease management in fish and shrimp farms.",
        "devin_body": r'''## When to use

You are operating or designing a fish, shrimp, or shellfish farm and want to predict water quality, optimise feeding, detect disease, or estimate biomass.

## Usage

- Monitor water quality with DryDock and AquaGrid sensors.
- Detect pathogens on-site with Sentry or Celvera.
- Optimize feed rations with iQuatic/Cargill.
- Predict growth and harvest timing.
- Automate aeration and feeding based on sensor thresholds.

## Steps

1. Deploy water-quality and feeding sensors in ponds/tanks.
2. Collect growth, feed, and disease records.
3. Train models for water quality, growth, and disease risk.
4. Integrate with automated feeders and aerators.
5. Validate with survival, growth, and feed conversion.

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

''',
        "references": ["https://doi.org/10.1016/j.fraope.2026.100567", "https://www.sciencedirect.com/science/article/abs/pii/S0044848625014887", "https://doi.org/10.1016/j.aiia.2025.01.012", "https://doi.org/10.5772/intechopen.1014536"],
    },
    {
        "name": "ai-for-livestock",
        "title": "AI for Livestock",
        "description": "Track and predict health, behavior, and productivity across livestock.",
        "devin_body": r'''## When to use

You are monitoring livestock health, behaviour, or productivity across species and want data-driven insights for individual or herd management.

## Usage

- Monitor behavior and posture with AnimalFormer and WERS.
- Detect lameness, heat, and calving with video and wearables.
- Track individual animals with RFID, UWB, and computer vision.
- Predict weight gain and feed conversion.
- Build farm-level decision support dashboards.

## Steps

1. Select species and target traits (health, behavior, production).
2. Install cameras, wearables, or RFID readers.
3. Collect and annotate phenotypes and events.
4. Train species-specific models.
5. Validate against farm records and expert scoring.

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

''',
        "references": ["https://www.sciencedirect.com/science/article/pii/S0168169920317099", "https://doi.org/10.5713/ab.25.0289", "https://doi.org/10.1016/j.aiia.2026.04.013", "https://www.mdpi.com/1424-8220/23/12/5732"],
    },
    {
        "name": "ai-for-viticulture",
        "title": "AI for Viticulture",
        "description": "Improve grape quality, yield, and disease management with vineyard AI.",
        "devin_body": r'''## When to use

You are managing a vineyard and want to monitor vine health, detect diseases, estimate yield and grape quality, or optimise irrigation, fertilisation, and harvest timing.

## Usage

- Map vines, count buds, and detect diseases with Cropsy or AgScout.
- Predict yield and harvest windows from canopy and cluster data.
- Monitor virus and fungal disease risk.
- Optimize irrigation and spraying by zone.
- Track pruning and canopy development.

## Steps

1. Capture drone, tractor, or smartphone imagery by block.
2. Label vines, clusters, symptoms, and yield data.
3. Train detection, segmentation, and yield models.
4. Generate prescription maps for spray and irrigation.
5. Validate with harvest weights and lab analysis.

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

''',
        "references": ["https://doi.org/10.1111/1541-4337.70523", "https://doi.org/10.3390/horticulturae12060719", "https://doi.org/10.1016/j.aiia.2025.08.001", "https://www.mdpi.com/2076-3417/14/22/10277"],
    },
    {
        "name": "ai-for-pest-management",
        "title": "AI for Pest Management",
        "description": "Detect and count insect pests with smart traps, pheromones, and computer vision.",
        "devin_body": r'''## When to use

You need to detect, identify, count, or forecast insect pests to inform scouting, traps, biological control, or pesticide application decisions.

## Usage

- Deploy smart traps with YOLO-Evo, Yolo-pest, or YOLOv9-TrapPest.
- Monitor pest dynamics and degree-day models.
- Predict outbreak risk from weather and trap counts.
- Target spraying with IPM thresholds.
- Build georeferenced pest maps.

## Steps

1. Deploy pheromone traps with cameras and IoT.
2. Collect images and count labels across locations.
3. Train detection and counting models.
4. Integrate with weather and degree-day predictions.
5. Validate against manual scouting and treatment outcomes.

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

''',
        "references": ["https://www.mdpi.com/2073-4395/15/7/1629", "https://resjournals.onlinelibrary.wiley.com/doi/10.1111/afe.12630", "https://www.sciencedirect.com/science/article/abs/pii/S1161030126000596", "https://doi.org/10.22271/27889289.2026.v6.i3a.259"],
    },
    {
        "name": "ai-for-soil-health",
        "title": "AI for Soil Health",
        "description": "Estimate soil carbon, nutrients, and texture from spectra and remote sensing.",
        "devin_body": r'''## When to use

You are assessing soil health indicators, mapping soil properties, monitoring carbon sequestration, or guiding regenerative and precision management.

## Usage

- Predict SOC and NPK with vis-NIR spectroscopy and remote sensing.
- Map soil health with PRISMA/EnMAP hyperspectral data.
- Integrate field samples with Gaofen or Sentinel imagery.
- Assess spatial uncertainty with conformal calibration.
- Support carbon credit and fertilizer decisions.

## Steps

1. Collect soil samples, spectra, and remote sensing data.
2. Align field and image data to field boundaries.
3. Train regression models for soil properties.
4. Map properties and uncertainty across fields.
5. Validate with independent lab analysis.

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

''',
        "references": ["https://doi.org/10.1002/advs.202504152", "https://doi.org/10.3390/app16115412", "https://link.springer.com/article/10.1007/s11368-024-03913-8", "https://www.mdpi.com/2077-0472/15/5/567"],
    },
    {
        "name": "ai-for-agricultural-economics",
        "title": "AI for Agricultural Economics",
        "description": "Support farm decisions, commodity pricing, and risk management with AI.",
        "devin_body": r'''## When to use

You are evaluating the economic outcomes of farm technologies, forecasting prices or yields, modelling adoption and risk, or building decision support for farmers and policymakers.

## Usage

- Forecast grain prices and basis with Croploo or Quantum Hedging.
- Optimize grain marketing and hedging strategies.
- Predict input costs and farm profitability.
- Assess climate and policy risk scenarios.
- Build farm budgeting and decision support dashboards.

## Steps

1. Collect market, weather, and farm financial data.
2. Engineer features for price, basis, and yield.
3. Train forecasting and optimization models.
4. Deploy decision support tools and alerts.
5. Validate with realized prices and farm outcomes.

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

''',
        "references": ["https://www.annualreviews.org/content/journals/10.1146/annurev-resource-101623-092515", "https://doi.org/10.1007/s44279-026-00510-w", "https://doi.org/10.62486/latia2025326", "https://baylislab.ace.illinois.edu/wp-content/uploads/2019/09/Storm-et-al-ML-Review.pdf"],
    },
]