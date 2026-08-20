SKILLS = [
    {
        "name": "ai-for-construction",
        "title": "AI for Construction",
        "description": "AI for construction site safety, progress monitoring, schedule and cost risk, robotics, and digital-twin-enabled project delivery.",
        "devin_body": r'''
## When to use

You are managing building or civil infrastructure projects and need to improve safety, track progress, forecast cost/schedule risk, or deploy robotic/autonomous systems.

## Key concepts

- **Computer vision for site safety**: detect PPE, worker posture, hazards, and near-miss events from site cameras or drones.
- **BIM and digital twins**: 4D/5D simulation, clash detection, and as-built vs. design comparison.
- **NLP for contracts and submittals**: extract obligations, risks, and change orders from project documents.
- **Predictive analytics**: cost overrun, delay, and productivity forecasting from schedule and cost data.
- **Robotics and autonomous equipment**: earthmoving, rebar tying, bricklaying, and autonomous haul trucks.

## Code pattern

```python
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms import functional as F

model = fasterrcnn_resnet50_fpn(weights="DEFAULT").eval()
img = F.to_tensor(image).unsqueeze(0)
with torch.no_grad():
    preds = model(img)

for box, label, score in zip(preds[0]["boxes"], preds[0]["labels"], preds[0]["scores"]):
    if score > 0.7:
        print(box.tolist(), int(label), float(score))
```

## Tuning notes

- Fine-tune object detectors on site-specific images; PPE classes are small and imbalanced.
- Combine BIM/GIS data to add spatial context to vision predictions.
- Use time-lapse or drone imagery for automated progress tracking.
- Validate safety alerts against human audits to control false positives.

## Verification

1. Train a hard-hat/vest detector and report mAP on a heldout site dataset.
2. Compare an ML cost/schedule risk forecast against earned-value baselines.
3. Detect a schedule slip from weekly progress photos and compare to the plan.
''',
        "references": [
            "https://doi.org/10.1016/j.autcon.2022.104440",
            "https://doi.org/10.3390/buildings16112225",
            "https://doi.org/10.1007/s42524-024-3128-5",
            "https://doi.org/10.1016/j.jobe.2020.101827",
        ],
    },
    {
        "name": "ai-for-architecture",
        "title": "AI for Architecture",
        "description": "AI for generative spatial layouts, floorplan synthesis, style exploration, and text/sketch-driven conceptual design.",
        "devin_body": r'''
## When to use

You are in early architectural concept design and want to generate massing, floorplans, spatial layouts, or style variations from text, sketches, or adjacency constraints.

## Key concepts

- **Language-driven layout generation**: prompt large language models to produce structured floorplan descriptions and adjacency graphs.
- **3D architectural synthesis**: autoregressive or diffusion models for building forms and interiors.
- **Sketch-to-architecture**: convert freehand sketches into 3D massing or floorplan renderings.
- **Graph and constraint-based layout**: encode room adjacencies and area constraints as optimization problems.
- **Space syntax and typology conditioning**: guide generation with circulation, daylight, and program rules.

## Code pattern

```python
import numpy as np
import networkx as nx

rooms = ["living", "kitchen", "bed1", "bed2", "bath"]
adj = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
])

G = nx.from_numpy_array(adj)
G = nx.relabel_nodes(G, {i: rooms[i] for i in range(len(rooms))})
pos = nx.spring_layout(G, seed=42)
# pos gives an initial spatial topology for refinement into a floorplan
```

## Tuning notes

- Use adjacency, area, and aspect-ratio constraints to filter invalid layouts.
- Fine-tune language models on domain-specific floorplan text or synthetic bubble diagrams.
- Combine parametric geometry (e.g., shapely, Rhino/Grasshopper) with generative models.
- Evaluate both design diversity and hard-constraint satisfaction, not just visual realism.

## Verification

1. Generate 100 layouts from text prompts and check valid room adjacencies.
2. Run a relevance or usefulness study with architects on generated concepts.
3. Compare generated floorplans to code-compliant area and accessibility guidelines.
''',
        "references": [
            "https://arxiv.org/abs/2303.07519",
            "https://arxiv.org/abs/2412.17957",
            "https://arxiv.org/abs/2403.20186",
            "https://arxiv.org/abs/2405.09997",
        ],
    },
    {
        "name": "ai-for-building-design",
        "title": "AI for Building Design",
        "description": "AI for energy, daylight, HVAC, envelope, and MEP performance optimization in the built environment.",
        "devin_body": r'''
## When to use

You need to reduce energy use intensity, improve thermal comfort, optimize daylighting, size HVAC/plant, or meet net-zero and code-compliance targets during building design.

## Key concepts

- **Surrogate models for building performance**: fast approximations of EnergyPlus, Radiance, or CFD simulations.
- **Physics-informed neural networks (PINNs)**: embed heat and mass transfer equations for better generalization.
- **Multi-objective optimization**: balance energy, cost, comfort, and carbon across geometry, facade, and systems.
- **BIM/IFC and building metadata**: extract geometry, materials, and systems from open standards.
- **Daylight glare, solar gain, and natural ventilation**: use ML to navigate high-dimensional envelope options.

## Code pattern

```python
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

X = df[["aspect_ratio", "wwr", "shgc", "u_wall", "u_window"]]
y = df["EUI_kwh_m2"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = XGBRegressor(n_estimators=200, learning_rate=0.05).fit(X_train, y_train)
y_pred = model.predict(X_test)
```

## Tuning notes

- Train surrogate models on parametric simulation datasets covering multiple climates and typologies.
- Use SHAP or feature importance to communicate which design levers matter most.
- Co-optimize geometry and MEP systems; avoid tuning each in isolation.
- Validate against high-fidelity EnergyPlus or Radiance runs before finalizing designs.

## Verification

1. Predict EUI within 5% of EnergyPlus on a heldout building.
2. Run a multi-objective design sweep and plot the Pareto front.
3. Explain top performance drivers to the design team using SHAP values.
''',
        "references": [
            "https://doi.org/10.3390/en18225921",
            "https://doi.org/10.1038/s41598-026-48460-z",
            "https://doi.org/10.1186/s42162-024-00426-z",
            "https://doi.org/10.3390/su18052379",
        ],
    },
    {
        "name": "ai-for-mining",
        "title": "AI for Mining",
        "description": "AI for mineral exploration, ore grade estimation, predictive maintenance, autonomous haulage, and mine safety.",
        "devin_body": r'''
## When to use

You are working with drill data, geophysical logs, equipment sensors, rock/core images, or tailings and need to improve exploration targeting, grade control, operations, or safety.

## Key concepts

- **Geostatistics + ML for grade estimation**: combine kriging with random forests or neural networks for ore grade and resource modeling.
- **Computer vision for rock and mineral identification**: classify lithology, texture, and alteration from core photos, thin sections, or conveyor images.
- **Predictive maintenance**: forecast crusher, mill, and haul-truck failures from vibration, oil, and telemetry data.
- **Autonomous haulage and fleet dispatch**: optimize routes, speeds, and shovel-truck matching.
- **Environmental monitoring**: track tailings, dust, water, and reclamation with remote sensing and IoT.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X = df[["depth", "xrf_cu", "xrf_fe", "magnetic_susceptibility", "density"]]
y = df["grade_cu_pct"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=200).fit(X_train, y_train)
y_pred = model.predict(X_test)
```

## Tuning notes

- Handle highly skewed grade distributions and sparse positive labels.
- Integrate domain geology; models should respect structure and contacts.
- Use spatial cross-validation to avoid optimistic estimates from clustered samples.
- Combine point cloud, hyperspectral, and geochemical data for richer features.

## Verification

1. Predict ore grade with R2 > 0.6 on a blind drill-hole test set.
2. Classify rock type from core images and compare to geologist logs.
3. Forecast a critical equipment failure with a useful maintenance horizon.
''',
        "references": [
            "https://doi.org/10.3390/a19030197",
            "https://doi.org/10.1007/s42797-025-00118-1",
            "https://www.bcg.com/publications/2026/the-ai-powered-mining-and-metals-company",
            "https://gmggroup.org/publication-foundations-of-ai-a-framework-for-ai-in-mining-updated-version/",
        ],
    },
    {
        "name": "ai-for-oil-and-gas",
        "title": "AI for Oil and Gas",
        "description": "AI for seismic interpretation, reservoir characterization, production forecasting, and predictive maintenance in energy operations.",
        "devin_body": r'''
## When to use

You are interpreting seismic and well-log data, characterizing reservoirs, forecasting production, or monitoring surface facilities and need data-driven or physics-aware models.

## Key concepts

- **Physics-informed neural networks (PINNs)**: embed reservoir flow equations for consistent simulation and history matching.
- **Computer vision for core and thin-section analysis**: automatic mineralogy, pore classification, and fracture detection.
- **Seismic facies and fault interpretation**: CNN and transformer models for structural interpretation.
- **Production forecasting**: LSTM, N-BEATS, and temporal fusion models for decline and well performance.
- **NLP for drilling and completion reports**: extract nonproductive time, lessons learned, and risk events.

## Code pattern

```python
import torch
import torch.nn as nn

class ProductionLSTM(nn.Module):
    def __init__(self, input_size=5, hidden_size=32, num_layers=2):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])

model = ProductionLSTM()
```

## Tuning notes

- Normalize rates, pressures, and temperatures; handle irregular sampling with interpolation or neural ODEs.
- Combine first-principles constraints (mass balance, Darcy flow) for better generalization across wells.
- Use transfer learning from analog reservoirs when target data are limited.
- Validate forecasts against decline-curve and material-balance baselines.

## Verification

1. Forecast monthly oil rate on a blind well with MAPE below 15%.
2. Classify seismic facies and compare predictions to interpreter picks.
3. Solve a 1D Buckley-Leverett flow problem with a PINN and match the analytical solution.
''',
        "references": [
            "https://www.sciopen.com/article/10.46690/ager.2025.09.01",
            "https://doi.org/10.3390/en18020391",
            "https://link.springer.com/article/10.1007/s44274-026-00797-y",
            "https://link.springer.com/book/10.1007/978-1-4842-6094-4",
        ],
    },
    {
        "name": "ai-for-textiles",
        "title": "AI for Textiles",
        "description": "AI for fabric defect detection, pattern and color design, sorting, and textile supply chain optimization.",
        "devin_body": r'''
## When to use

You are automating fabric inspection, generating prints and textures, grading yarns, forecasting textile demand, or optimizing dyeing and finishing processes.

## Key concepts

- **Anomaly detection for surface defects**: autoencoders or one-class classifiers for holes, stains, and weaving faults.
- **Pattern and texture generation**: GANs and diffusion models for textile print design.
- **Color science and shade matching**: use LAB/HSV color spaces and constancy algorithms.
- **Predictive maintenance for looms and dyeing machines**: vibration, temperature, and energy monitoring.
- **Traceability and supply chain**: digital product passports and blockchain for fiber provenance.

## Code pattern

```python
import tensorflow as tf
from tensorflow.keras import layers, Model

inputs = layers.Input(shape=(64, 64, 1))
x = layers.Conv2D(32, 3, activation="relu", padding="same")(inputs)
x = layers.MaxPooling2D(2, padding="same")(x)
x = layers.Conv2D(16, 3, activation="relu", padding="same")(x)
x = layers.UpSampling2D(2)(x)
outputs = layers.Conv2D(1, 3, activation="sigmoid", padding="same")(x)

autoencoder = Model(inputs, outputs)
autoencoder.compile(optimizer="adam", loss="mse")
```

## Tuning notes

- Train anomaly detectors only on normal/ defect-free fabric images; anomalies are rare.
- Data augmentation must preserve weave and texture statistics.
- Use LAB or HSV color spaces for dye and shade defects rather than RGB alone.
- Calibrate false-positive rates against human quality-control standards.

## Verification

1. Detect fabric defects on a labeled test set and report precision and recall.
2. Generate fabric patterns conditioned on a style and compute an image similarity or FID metric.
3. Predict loom downtime from sensor data and compare to maintenance logs.
''',
        "references": [
            "https://doi.org/10.1111/cote.70044",
            "https://doi.org/10.1177/00405175221130773",
            "https://doi.org/10.1155/2021/9948808",
            "https://doi.org/10.3390/electronics13183728",
        ],
    },
    {
        "name": "ai-for-fashion",
        "title": "AI for Fashion",
        "description": "AI for trend forecasting, outfit recommendation, virtual try-on, generative design, and personalized shopping.",
        "devin_body": r'''
## When to use

You are building e-commerce recommendation, styling, trend analysis, size/fit prediction, or generative garment design systems.

## Key concepts

- **Visual-language embeddings**: CLIP-style models for outfit compatibility and text-to-image retrieval.
- **Outfit recommendation and compatibility**: graph neural networks and metric learning for mix-and-match.
- **Virtual try-on and cloth simulation**: physics-aware generative models and 3D draping.
- **Fashion generation**: GANs and diffusion models for garment and pattern design.
- **Size and fit prediction**: combine body measurements, returns, and garment metadata.

## Code pattern

```python
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

inputs = processor(
    text=["red evening dress", "denim jacket"],
    images=[image],
    return_tensors="pt",
    padding=True,
)
logits = model(**inputs).logits_per_image
```

## Tuning notes

- Fine-tune catalog-specific embeddings; generic CLIP may miss fashion nuance.
- Address cold-start items with rich content-based features.
- Outfit compatibility is subjective; collect explicit human feedback for ranking.
- Watch for bias in body representation, size, and skin-tone inclusivity.

## Verification

1. Build an outfit compatibility scorer and measure AUC on a public dataset.
2. Retrieve or generate fashion images and run a human relevance study.
3. Predict size fit from historical returns and compare to baseline sizing.
''',
        "references": [
            "https://doi.org/10.1145/3624733",
            "https://doi.org/10.1109/access.2023.3306235",
            "https://doi.org/10.3390/info17010011",
            "https://doi.org/10.3390/informatics8030049",
        ],
    },
    {
        "name": "ai-for-cosmetics",
        "title": "AI for Cosmetics",
        "description": "AI for personalized skincare, formulation optimization, shade matching, safety/toxicity prediction, and consumer insight.",
        "devin_body": r'''
## When to use

You are analyzing skin from images, recommending products, optimizing formulations, matching shades, or predicting tolerability and safety in cosmetics and dermocosmetics.

## Key concepts

- **Computer vision for skin analysis**: classify type, condition, acne, wrinkles, pigmentation, and sensitivity.
- **Predictive formulation modeling**: forecast texture, stability, shelf life, and sensory properties.
- **In silico toxicology**: predict sensitization, irritation, and allergen risk with computational models.
- **Personalized skincare**: combine selfies, environment, lifestyle, and preference data.
- **Color science for shade matching**: foundation and makeup matching across skin tones.

## Code pattern

```python
import torch
import torch.nn as nn

class SkinNet(nn.Module):
    def __init__(self, num_classes=4):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.fc = nn.Linear(32 * 16 * 16, num_classes)

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)
```

## Tuning notes

- Train on diverse skin tones, Fitzpatrick types, and imaging conditions.
- Validate recommendations with dermatologists and comply with cosmetic regulations.
- Combine facial images with environment and historical data for personalization.
- Use class weights for rare skin conditions and balanced sampling across demographics.

## Verification

1. Classify skin type/condition with balanced accuracy across skin tones.
2. Predict product tolerability or stability from ingredient and formulation data.
3. Recommend a personalized routine and measure user-reported satisfaction.
''',
        "references": [
            "https://doi.org/10.3390/cosmetics12040157",
            "https://doi.org/10.2196/60883",
            "https://doi.org/10.7759/cureus.82510",
            "https://www.loreal.com/en/news/research-innovation/unveil-perso-the-worlds-first-aipowered-device-for-skincare-and-cosmetics/",
        ],
    },
    {
        "name": "ai-for-food-and-beverage",
        "title": "AI for Food and Beverage",
        "description": "AI for food safety, quality control, recipe and product development, shelf-life prediction, and supply chain optimization.",
        "devin_body": r'''
## When to use

You are inspecting food on a production line, predicting shelf life, generating recipes, forecasting demand, or monitoring cold-chain and traceability.

## Key concepts

- **Computer vision for quality inspection**: detect defects, foreign material, contamination, and label errors.
- **Predictive microbiology and shelf-life modeling**: time-temperature history and spoilage prediction.
- **NLP for recipes and sensory data**: mine flavors, ingredients, and consumer reviews.
- **Demand and supply-chain forecasting**: predict sales, yield, and inventory needs.
- **IoT and blockchain traceability**: track provenance, temperature, and freshness.

## Code pattern

```python
import torch
from torchvision.models import resnet18

model = resnet18(weights="DEFAULT")
model.fc = torch.nn.Linear(model.fc.in_features, 2)  # good / defective

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
# fine-tune on labeled food images
```

## Tuning notes

- Lighting, packaging, and product orientation create large variability; augment carefully.
- Use class weights for rare defects and validate against lab tests.
- Shelf-life models need temperature history as a continuous input.
- Keep compliance with food-safety regulations and HACCP/FSMA frameworks.

## Verification

1. Detect foreign material or defects on a conveyor belt with >95% recall.
2. Forecast shelf life and compare against microbiological assays.
3. Optimize a recipe by predicting sensory or nutrition scores.
''',
        "references": [
            "https://doi.org/10.1007/s11694-026-04088-1",
            "https://doi.org/10.3390/pr14030513",
            "https://doi.org/10.1007/s44163-025-00296-8",
            "https://doi.org/10.1007/s12393-026-09445-w",
        ],
    },
    {
        "name": "ai-for-hospitality",
        "title": "AI for Hospitality",
        "description": "AI for guest personalization, revenue management, dynamic pricing, operations, and conversational service.",
        "devin_body": r'''
## When to use

You are running hotels, restaurants, events, or travel services and need to forecast demand, set prices, staff operations, or personalize guest interactions.

## Key concepts

- **RevPAR and demand forecasting**: time-series models with seasonality, events, and competitor data.
- **Dynamic pricing and availability optimization**: adjust rates in real time based on demand signals.
- **NLP for reviews and chatbots**: sentiment, topic extraction, and conversational concierge.
- **Customer segmentation and personalization**: target offers, room upgrades, and loyalty rewards.
- **Workforce scheduling and maintenance**: optimize staffing and housekeeping routes.

## Code pattern

```python
from prophet import Prophet

df = df.rename(columns={"date": "ds", "bookings": "y"})
m = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    seasonality_mode="multiplicative",
)
m.fit(df)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
```

## Tuning notes

- Add holidays, events, competitor rates, and weather as regressors.
- Use chronological splits; do not leak future booking data into training.
- Calibrate price sensitivity with controlled A/B tests.
- Protect guest privacy and comply with GDPR and hospitality data policies.

## Verification

1. Forecast daily RevPAR and measure MAPE against actuals.
2. Run a dynamic-pricing A/B test and compare revenue lift to a baseline.
3. Build a review-sentiment model and align it with guest NPS.
''',
        "references": [
            "https://doi.org/10.11591/ijai.v15.i3.pp2024-2040",
            "https://www.bcg.com/publications/2026/ai-first-hotels-leaner-faster-smarter",
            "https://doi.org/10.1177/10963480231188663",
            "https://doi.org/10.47941/jmh.1957",
        ],
    },
    {
        "name": "ai-for-sports",
        "title": "AI for Sports",
        "description": "AI for athlete tracking, match analytics, performance prediction, injury risk, and tactical decision support.",
        "devin_body": r'''
## When to use

You are analyzing team or individual sports and want to track players, predict outcomes, assess tactics, forecast injuries, or support coaching decisions.

## Key concepts

- **Player and ball tracking**: computer vision and event data for pose and movement.
- **Expected goals and advanced metrics**: xG, xA, possession value, and efficiency ratings.
- **Wearable and biomechanical time series**: load, acceleration, heart rate, and sleep.
- **Match outcome and tactical prediction**: classify results and formations from match context.
- **Injury risk and load management**: combine training load, recovery, and history.

## Code pattern

```python
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

X = df[["home_xg", "away_xg", "home_possession", "home_rest_days", "away_form"]]
y = df["outcome"]  # 0=draw, 1=home, 2=away

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
model = XGBClassifier(
    objective="multi:softprob",
    num_class=3,
    n_estimators=200,
).fit(X_train, y_train)
```

## Tuning notes

- Preserve chronological match ordering to avoid data leakage from future results.
- Feature engineering is critical: recent form, fatigue, travel, and head-to-head records.
- Tracking data requires camera calibration and consistent player identity.
- Interpretability helps coaches trust and act on tactical recommendations.

## Verification

1. Predict match outcomes on a heldout season and report log-loss.
2. Track players from broadcast video and compare to official event data.
3. Estimate injury probability from workload and biomechanics data.
''',
        "references": [
            "https://doi.org/10.1080/02640414.2026.2636863",
            "https://doi.org/10.3390/app15137254",
            "https://link.springer.com/article/10.1186/s13102-025-01294-0",
            "https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2024.1383723/full",
        ],
    },
    {
        "name": "ai-for-media-and-entertainment",
        "title": "AI for Media and Entertainment",
        "description": "AI for content recommendation, personalization, generative media, audience analytics, and rights/compliance workflows.",
        "devin_body": r'''
## When to use

You are building streaming, music, gaming, social, editorial, advertising, or content-moderation products and need to recommend, create, or understand content and audiences.

## Key concepts

- **Collaborative and content-based recommendation**: matrix factorization, two-tower models, and sequential recommenders.
- **LLM-backed ranking**: use large language models for natural-language steerable recommendation.
- **Generative media**: audio, image, and video generation and editing.
- **Content understanding and moderation**: metadata extraction, toxicity, copyright, and compliance.
- **Audience and churn analytics**: segmentation, propensity, and lifetime value.

## Code pattern

```python
import torch
import torch.nn as nn

n_users, n_items, latent_dim = 10000, 5000, 64
user_emb = nn.Embedding(n_users, latent_dim)
item_emb = nn.Embedding(n_items, latent_dim)

scores = (user_emb(user_ids) * item_emb(item_ids)).sum(dim=1)
loss = torch.nn.functional.mse_loss(scores, ratings)
```

## Tuning notes

- Catalog grounding is essential: recommenders must return real, available items.
- Balance personalization with diversity, freshness, and fairness.
- LLM-based rankers are expensive; optimize serving with prefix caching, quantization, and prefill-only designs.
- A/B test online engagement and long-term satisfaction, not only offline ranking metrics.

## Verification

1. Train a collaborative filter and report RMSE and NDCG on a holdout set.
2. Build an LLM-based ranker with catalog grounding and compare to a matrix-factorization baseline.
3. Evaluate a content-moderation model on a labeled toxicity or rights-violation dataset.
''',
        "references": [
            "https://arxiv.org/abs/2608.10257",
            "https://netflixtechblog.com/genrec-towards-llm-native-recommendation-at-netflix-f20be6f643e3",
            "https://research.atspotify.com/2026/8/from-models-to-products-llms-for-recommendation-at-spotify-scale",
            "https://netflixtechblog.com/scaling-media-machine-learning-at-netflix-f19b400243",
        ],
    },
]
