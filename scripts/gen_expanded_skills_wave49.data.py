SKILLS = [
    {
        "name": "ai-for-property-valuation",
        "title": "AI for Property Valuation",
        "description": "Automated valuation models, hedonic pricing, spatial machine learning, and deep learning for residential and commercial property appraisal.",
        "devin_body": r'''## When to use

You need to estimate market values, support appraisal workflows, or build automated valuation models (AVMs) for residential or commercial properties.

## Usage

- **Hedonic and comparable-sales models**: combine property attributes, location, and market conditions to estimate value.
- **Spatial ML**: capture neighborhood effects, walkability, and distance to amenities with geospatial features.
- **Deep learning AVMs**: use CNNs or graph neural networks to ingest imagery, maps, or transaction graphs.
- **Explainability and fairness**: use SHAP to attribute value drivers and detect bias in valuations.

## Steps

1. Gather sales transactions, property characteristics, and geospatial attributes.
2. Engineer features for size, age, locational amenities, and spatial lags.
3. Train and validate regression/AVM models (XGBoost, LightGBM, DNN, GNN).
4. Evaluate with MAPE, RMSE, and cross-validation across neighborhoods.
5. Deploy a monitoring pipeline for drift and appraisal-review workflow.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

X = df[['sqft', 'lot_size', 'bedrooms', 'bathrooms', 'location_score']]
y = df['sale_price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = GradientBoostingRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
mape = (abs(y_test - pred) / y_test).mean()
print(f'MAPE: {mape:.2%}')
```

## Tuning notes

- Include spatial features and temporal market adjustments.
- Use out-of-time splits for realistic AVM evaluation.
- Watch for data leakage from future transactions or duplicate listings.

## Verification

1. Replicate an AVM on a public assessor dataset and report MAPE.
2. Compare model predictions to appraised values on a holdout set.
3. Use SHAP to identify the top five value drivers.

## References

- https://www.sciencedirect.com/science/article/pii/S0264275124003299
- https://arxiv.org/html/2405.06553
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0318701
- https://link.springer.com/article/10.1007/s00168-023-01212-7
- https://dl.acm.org/doi/10.1145/3567430
''',
        "references": [
            "https://www.sciencedirect.com/science/article/pii/S0264275124003299",
            "https://arxiv.org/html/2405.06553",
            "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0318701",
            "https://link.springer.com/article/10.1007/s00168-023-01212-7",
            "https://dl.acm.org/doi/10.1145/3567430",
        ],
    },
    {
        "name": "ai-for-real-estate-investment",
        "title": "AI for Real Estate Investment",
        "description": "Predictive analytics, investment screening, REIT return forecasting, and risk-adjusted underwriting for real estate investment decisions.",
        "devin_body": r'''## When to use

You are evaluating acquisitions, forecasting REIT returns, screening markets, or optimizing capital allocation across real estate assets.

## Usage

- **Market-timing and cycle analysis**: use macro, credit, and rent-growth indicators to time investments.
- **Asset-level underwriting**: forecast cash flows, cap rates, and scenario stress tests.
- **REIT return prediction**: apply ML to firm characteristics and macro variables.
- **Risk decomposition**: model spatial, sector, leverage, and liquidity exposures.

## Steps

1. Define investment thesis, asset universe, and performance target.
2. Collect macro, market, and asset-level features.
3. Train predictive models (gradient boosting, GMDH, econometric-ML hybrids).
4. Backtest strategies across market regimes.
5. Generate sensitivity and scenario reports for capital-committee decisions.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score

X = df[['cap_rate', 'rent_growth', 'unemployment', 'credit_spread', 'sector']]
y = df['total_return']
model = GradientBoostingRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print('R2:', r2_score(y_test, pred))
```

## Tuning notes

- Use panel data and fixed effects to handle unobserved heterogeneity.
- Distinguish in-sample fit from out-of-time predictive power.
- Incorporate transaction costs and liquidity constraints.

## Verification

1. Backtest an investment-screening model on a public REIT dataset.
2. Compare ML forecasts to a simple historical-mean benchmark.
3. Evaluate risk-adjusted returns after transaction costs.

## References

- https://doi.org/10.1111/1540-6229.12483
- https://doi.org/10.1186/s40854-023-00486-2
- https://www.landecon.cam.ac.uk/sites/default/files/2024-08/CRERC_2024-02%20WP.pdf
- https://www.reri.org/research/files/2023funded_commercial-real-estate-pricing-dynamics.pdf
- https://link.springer.com/article/10.1007/s11146-023-09944-1
''',
        "references": [
            "https://doi.org/10.1111/1540-6229.12483",
            "https://doi.org/10.1186/s40854-023-00486-2",
            "https://www.landecon.cam.ac.uk/sites/default/files/2024-08/CRERC_2024-02%20WP.pdf",
            "https://www.reri.org/research/files/2023funded_commercial-real-estate-pricing-dynamics.pdf",
            "https://link.springer.com/article/10.1007/s11146-023-09944-1",
        ],
    },
    {
        "name": "ai-for-urban-development",
        "title": "AI for Urban Development",
        "description": "GeoAI, spatial modeling, generative urban design, and scenario simulation for sustainable, equitable, and data-driven urban development.",
        "devin_body": r'''## When to use

You are planning urban growth, evaluating zoning or land-use scenarios, modeling housing and infrastructure needs, or assessing climate resilience.

## Usage

- **GeoAI and remote sensing**: classify urban fabric, monitor informality, and map green/gray infrastructure.
- **Scenario simulation**: use agent-based, cellular automata, and land-use change models.
- **Participatory planning**: synthesize public input and design options with LLMs.
- **Sustainable development metrics**: evaluate density, accessibility, emissions, and equity.

## Steps

1. Define planning objectives, boundaries, and stakeholder questions.
2. Integrate geospatial, demographic, economic, and mobility datasets.
3. Build or train spatial ML and generative models.
4. Run scenarios and quantify impacts across sustainability and equity metrics.
5. Co-design and iterate with planners and communities.

## Code pattern

```python
import geopandas as gpd
import rasterio
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Land-use/land-cover classification from satellite bands
X = np.stack([band.read(1).flatten() for band in bands], axis=1)
y = reference_classes.flatten()
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Validate spatially with out-of-bag or spatial cross-validation.
- Watch for data bias toward Global North cities.
- Couple models with governance and participatory review.

## Verification

1. Classify urban land cover and compare with ground-truth labels.
2. Run a scenario simulation and report key indicator changes.
3. Generate an LLM-assisted public-comment summary for a zoning proposal.

## References

- https://www.mdpi.com/2413-8851/10/3/148
- https://www.mdpi.com/2413-8851/9/12/508
- https://www.nature.com/articles/s44284-026-00492-2
- https://www.nature.com/articles/s43588-025-00846-1
- https://www.sciopen.com/article/10.1016/j.ese.2025.100526
''',
        "references": [
            "https://www.mdpi.com/2413-8851/10/3/148",
            "https://www.mdpi.com/2413-8851/9/12/508",
            "https://www.nature.com/articles/s44284-026-00492-2",
            "https://www.nature.com/articles/s43588-025-00846-1",
            "https://www.sciopen.com/article/10.1016/j.ese.2025.100526",
        ],
    },
    {
        "name": "ai-for-city-modeling",
        "title": "AI for City Modeling",
        "description": "Urban digital twins, 3D city reconstruction, generative city models, and AI-driven urban simulation for planning and operations.",
        "devin_body": r'''## When to use

You are building or querying a digital twin, synthesizing urban environments, or running what-if simulations of city systems.

## Usage

- **3D city reconstruction**: use photogrammetry, NeRF, Gaussian splatting, and point clouds.
- **Urban digital twins**: integrate IoT, BIM/GIS, and simulation layers.
- **Generative city modeling**: use LLMs, diffusion, and flow models for streetscapes and layouts.
- **Embodied AI benchmarks**: city-scale simulators for navigation and reinforcement learning.

## Steps

1. Gather geospatial, sensor, and asset data for the target city.
2. Reconstruct 3D geometry and semantics.
3. Integrate data streams into a digital twin or simulator platform.
4. Train and validate AI models for prediction and scenario analysis.
5. Visualize and continuously update the model.

## Code pattern

```python
import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud('city_block.ply')
pcd.estimate_normals()
o3d.visualization.draw_geometries([pcd])
```

## Tuning notes

- Use Level-of-Detail (LoD) and tiling for large models.
- Ensure interoperability with CityGML/CityJSON standards.
- Maintain privacy and safety in public-space sensing.

## Verification

1. Reconstruct a small neighborhood and evaluate geometric accuracy.
2. Build a digital-twin dashboard for a building or block.
3. Benchmark a generative model against real street-view imagery.

## References

- https://arxiv.org/html/2505.07396v1
- https://www.mdpi.com/2624-6511/8/1/28
- https://www.nature.com/articles/s43588-024-00606-7
- https://ojs.aaai.org/index.php/AAAI/article/view/42379
- https://www.sciopen.com/article/10.1016/j.ese.2025.100526
''',
        "references": [
            "https://arxiv.org/html/2505.07396v1",
            "https://www.mdpi.com/2624-6511/8/1/28",
            "https://www.nature.com/articles/s43588-024-00606-7",
            "https://ojs.aaai.org/index.php/AAAI/article/view/42379",
            "https://www.sciopen.com/article/10.1016/j.ese.2025.100526",
        ],
    },
    {
        "name": "ai-for-construction-management",
        "title": "AI for Construction Management",
        "description": "BIM-NLP integration, 4D/5D digital twins, computer-vision progress monitoring, and AI-driven scheduling and cost control for construction.",
        "devin_body": r'''## When to use

You are planning, scheduling, monitoring, or controlling construction projects with AI for cost, schedule, quality, and safety.

## Usage

- **4D/5D BIM**: integrate schedule, cost, and model data for predictive control.
- **NLP for planning**: extract activities, durations, and logic from documents and drawings.
- **Computer vision**: monitor progress, productivity, and safety from site images and drones.
- **Reinforcement learning**: resource leveling and schedule optimization.

## Steps

1. Collect project model, schedule, cost, and site data.
2. Build a 4D/5D knowledge graph and digital-twin environment.
3. Train NLP/vision/RL models for task-specific automation.
4. Validate against actual progress and cost reports.
5. Deploy real-time dashboards and alerts.

## Code pattern

```python
from ultralytics import YOLO

# Detect workers and equipment for progress monitoring
model = YOLO('yolov8n.pt')
results = model('site_photo.jpg')
for r in results:
    print(r.boxes.data)
```

## Tuning notes

- Align BIM objects with scheduling and cost codes.
- Use probabilistic CPM and Bayesian updating for uncertainty.
- Combine rule-based checks with learned models for safety.

## Verification

1. Generate an automated schedule from a BIM model and compare with baseline.
2. Track construction progress with vision and compare to planned percent complete.
3. Run a what-if resource-leveling simulation.

## References

- https://doi.org/10.48550/arxiv.2511.03684
- https://www.sciencedirect.com/science/article/abs/pii/S0926580525005217
- https://www.mdpi.com/2673-4591/112/1/3
- https://www.mdpi.com/2411-9660/10/2/43
- https://www.ideals.illinois.edu/items/137190
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2511.03684",
            "https://www.sciencedirect.com/science/article/abs/pii/S0926580525005217",
            "https://www.mdpi.com/2673-4591/112/1/3",
            "https://www.mdpi.com/2411-9660/10/2/43",
            "https://www.ideals.illinois.edu/items/137190",
        ],
    },
    {
        "name": "ai-for-facilities-management",
        "title": "AI for Facilities Management",
        "description": "Predictive maintenance, fault detection, digital twins, and AI-enabled asset lifecycle management for built facilities.",
        "devin_body": r'''## When to use

You are managing maintenance, energy, and asset performance in commercial, industrial, or institutional facilities.

## Usage

- **Predictive maintenance**: forecast equipment faults and remaining useful life.
- **Fault detection and diagnostics**: use rule-ML hybrids for HVAC, lighting, and AHU.
- **Asset digital twins**: update condition models from IoT and work orders.
- **Energy optimization**: use ML and RL to reduce operating cost and carbon.

## Steps

1. Ingest sensor, BMS, CMMS, and asset master data.
2. Label faults, failures, and maintenance events.
3. Train predictive models (XGBoost, LSTM, autoencoders).
4. Deploy real-time anomaly alerts and work-order integration.
5. Continuously retrain on new data and feedback.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import IsolationForest

# Anomaly detection on HVAC time series
X = df[['supply_temp', 'return_temp', 'fan_speed', 'damper_pos']]
clf = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = clf.fit_predict(X)
```

## Tuning notes

- Balance class imbalance with resampling or cost-sensitive learning.
- Use physics-aware features such as delta-T and setpoint deviations.
- Integrate human-in-the-loop for maintenance decisions.

## Verification

1. Predict AHU faults on a labeled building dataset.
2. Compare predictive maintenance alerts to a calendar-based program.
3. Show reduction in unplanned downtime or energy cost.

## References

- https://doi.org/10.1108/f-02-2025-0032
- https://www.mdpi.com/2075-5309/15/4/630
- https://doi.org/10.3389/fbuil.2025.1734945
- https://doi.org/10.3390/buildings15224129
- https://ec-3.org/publication/ec32025_369/
''',
        "references": [
            "https://doi.org/10.1108/f-02-2025-0032",
            "https://www.mdpi.com/2075-5309/15/4/630",
            "https://doi.org/10.3389/fbuil.2025.1734945",
            "https://doi.org/10.3390/buildings15224129",
            "https://ec-3.org/publication/ec32025_369/",
        ],
    },
    {
        "name": "ai-for-building-operations",
        "title": "AI for Building Operations",
        "description": "Smart building control, energy optimization, occupant-centric HVAC and lighting, and IoT-BMS integration for operational performance.",
        "devin_body": r'''## When to use

You are optimizing energy, comfort, and resilience in the day-to-day operation of smart buildings and campuses.

## Usage

- **Energy management**: forecast loads, optimize HVAC setpoints, and shift demand.
- **IoT-BMS integration**: unify sensor, weather, occupancy, and tariff data.
- **Reinforcement learning for control**: agent-based chiller plant or VAV optimization.
- **Fault detection and diagnostics**: real-time alerts and performance drift.

## Steps

1. Connect BMS, IoT, weather, and utility data streams.
2. Define control objectives (energy, comfort, cost, carbon).
3. Train forecasting and control models (MPC, RL, supervised).
4. Simulate and safely deploy in shadow or pilot mode.
5. Monitor KPIs and retrain seasonally.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Forecast next-hour building energy use
X = df[['hour', 'outdoor_temp', 'occupancy', 'setpoint']]
y = df['total_kw']
model = GradientBoostingRegressor(random_state=42)
model.fit(X, y)
```

## Tuning notes

- Use physics-informed constraints and safety limits in control.
- Account for occupancy patterns and weather forecasts.
- Validate energy savings with counterfactual baselines.

## Verification

1. Build an energy-forecasting model and compare against a persistence baseline.
2. Run a simulation of optimized setpoints and report savings.
3. Monitor indoor comfort metrics during a pilot deployment.

## References

- https://link.springer.com/article/10.1186/s42162-025-00592-8
- https://doi.org/10.1145/3765611.3815366
- https://www.mdpi.com/2076-3417/15/14/7682
- https://doi.org/10.3390/su172210313
- https://www.nature.com/articles/s41467-024-50088-4
''',
        "references": [
            "https://link.springer.com/article/10.1186/s42162-025-00592-8",
            "https://doi.org/10.1145/3765611.3815366",
            "https://www.mdpi.com/2076-3417/15/14/7682",
            "https://doi.org/10.3390/su172210313",
            "https://www.nature.com/articles/s41467-024-50088-4",
        ],
    },
    {
        "name": "ai-for-tenant-experience",
        "title": "AI for Tenant Experience",
        "description": "Personalization, occupancy analytics, indoor environmental quality, and tenant engagement for workplace and residential environments.",
        "devin_body": r'''## When to use

You want to improve tenant satisfaction, engagement, retention, and workplace productivity in commercial or residential buildings.

## Usage

- **Indoor environmental quality**: predict thermal, visual, acoustic, and air-quality satisfaction.
- **Personalization**: adjust lighting, temperature, and space recommendations.
- **Occupancy analytics**: understand space utilization and preferences.
- **Tenant apps and services**: AI chatbots, maintenance ticketing, and amenity booking.

## Steps

1. Collect post-occupancy evaluation, sensor, and app engagement data.
2. Link environmental conditions to satisfaction scores.
3. Train preference and satisfaction models (Random Forest, LSTM, attention).
4. Deploy personalization rules and feedback loops.
5. Track NPS, retention, and utilization KPIs.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Predict tenant satisfaction category
X = df[['temperature', 'light_level', 'noise', 'air_quality']]
y = df['satisfaction_label']
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Respect privacy and consent for occupant data.
- Use explainable models to avoid black-box comfort controls.
- Account for individual and seasonal preference variation.

## Verification

1. Predict satisfaction on a post-occupancy evaluation dataset.
2. A/B test personalized setpoints against default settings.
3. Correlate experience improvements with retention or NPS.

## References

- https://doi.org/10.1108/sasbe-03-2025-0161
- https://www.mdpi.com/1424-8220/18/5/1602
- https://www.mdpi.com/2071-1050/16/10/4258
- https://doi.org/10.1038/s41598-025-10086-y
''',
        "references": [
            "https://doi.org/10.1108/sasbe-03-2025-0161",
            "https://www.mdpi.com/1424-8220/18/5/1602",
            "https://www.mdpi.com/2071-1050/16/10/4258",
            "https://doi.org/10.1038/s41598-025-10086-y",
        ],
    },
    {
        "name": "ai-for-lease-management",
        "title": "AI for Lease Management",
        "description": "NLP-based lease abstraction, clause extraction, compliance tracking, and predictive analytics for commercial and residential lease portfolios.",
        "devin_body": r'''## When to use

You need to abstract, structure, monitor, and analyze lease contracts at scale across a portfolio.

## Usage

- **Lease abstraction**: extract key terms, dates, rent, options, and obligations.
- **Clause classification**: identify renewal, termination, escalation, and default clauses.
- **Compliance and accounting**: feed structured data into IFRS 16 / ASC 842 workflows.
- **Portfolio analytics**: monitor rent roll, expirations, and option exposures.

## Steps

1. Collect lease documents (PDFs, Word, scanned) and define an abstraction schema.
2. Preprocess and OCR documents, segment pages and clauses.
3. Fine-tune an NER or extractive model on annotated lease data.
4. Validate extraction against human-reviewed gold data.
5. Load structured output into CMMS/ERP and analytics dashboards.

## Code pattern

```python
import re

# Simple regex extraction for base rent and commencement date
text = open('lease.txt', encoding='utf-8').read()
rent_match = re.search(r'base rent.*?\$([\d,]+\.\d{2})', text, re.IGNORECASE)
date_match = re.search(r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}\b', text, re.IGNORECASE)
print('rent:', rent_match.group(1) if rent_match else None)
print('date:', date_match.group(0) if date_match else None)
```

## Tuning notes

- Build a structured schema aligned with accounting standards.
- Use layout-aware or document-aware models for scanned PDFs.
- Validate high-stakes terms with legal review.

## Verification

1. Extract key fields from a sample lease and compute F1 vs human review.
2. Identify all renewal and termination clauses across a portfolio.
3. Generate a rent roll and expiration dashboard from abstracts.

## References

- https://www.irma-international.org/chapter/natural-language-processing-based-information-extraction-and-abstraction-for-lease-documents/245091
- https://ideas.repec.org/a/aza/crej00/y2019v8i4p307-311.html
- https://ideas.repec.org/a/aza/crej00/y2019v9i2p121-129.html
- https://www.bauhaus-legal.com/case-studies/jll-cadastral-leverton-ai-lease-abstraction
- https://www.ijset.in/synthesizing-ai-data-driven-frameworks-real-estate-lease-management/
''',
        "references": [
            "https://www.irma-international.org/chapter/natural-language-processing-based-information-extraction-and-abstraction-for-lease-documents/245091",
            "https://ideas.repec.org/a/aza/crej00/y2019v8i4p307-311.html",
            "https://ideas.repec.org/a/aza/crej00/y2019v9i2p121-129.html",
            "https://www.bauhaus-legal.com/case-studies/jll-cadastral-leverton-ai-lease-abstraction",
            "https://www.ijset.in/synthesizing-ai-data-driven-frameworks-real-estate-lease-management/",
        ],
    },
    {
        "name": "ai-for-portfolio-optimization",
        "title": "AI for Portfolio Optimization",
        "description": "Diversification, risk-return balancing, rebalancing strategies, and generative-AI analytics for real estate and mixed-asset portfolios.",
        "devin_body": r'''## When to use

You are allocating capital, rebalancing holdings, managing concentration risk, or forecasting portfolio-level returns in real estate.

## Usage

- **Risk-return optimization**: mean-variance, CVaR, or genetic-algorithm approaches.
- **Diversification**: analyze geography, sector, tenant, and lease-maturity exposures.
- **Scenario stress testing**: market shocks, interest-rate, and vacancy scenarios.
- **AI agents**: autonomous monitoring and rebalancing recommendations.

## Steps

1. Define portfolio objectives, constraints, and investable universe.
2. Collect asset-level cash flows, market, and risk-factor data.
3. Estimate return forecasts and covariance or risk matrices.
4. Run optimization under constraints and scenarios.
5. Monitor and rebalance on a regular cadence.

## Code pattern

```python
import cvxpy as cp
import numpy as np

# Mean-variance allocation across property sectors
n = len(sectors)
w = cp.Variable(n)
ret = forecast_returns @ w
risk = cp.quad_form(w, cov)
prob = cp.Problem(cp.Maximize(ret - 0.5 * risk), [cp.sum(w) == 1, w >= 0])
prob.solve()
print(w.value)
```

## Tuning notes

- Use out-of-sample backtests, not only in-sample optimization.
- Account for transaction costs, illiquidity, and leverage.
- Avoid overconcentration from return overfitting.

## Verification

1. Backtest an optimized REIT or mixed portfolio against a benchmark.
2. Compute Sharpe, max drawdown, and turnover.
3. Stress test under a 2008-style or COVID scenario.

## References

- https://doi.org/10.1111/1540-6229.12483
- https://www.tandfonline.com/doi/abs/10.1080/10835547.2025.2513145
- https://journals.sagepub.com/doi/10.1177/27533743241313464
- https://www.mdpi.com/2227-7390/13/21/3413
- https://ijaidsml.org/index.php/ijaidsml/article/view/494
''',
        "references": [
            "https://doi.org/10.1111/1540-6229.12483",
            "https://www.tandfonline.com/doi/abs/10.1080/10835547.2025.2513145",
            "https://journals.sagepub.com/doi/10.1177/27533743241313464",
            "https://www.mdpi.com/2227-7390/13/21/3413",
            "https://ijaidsml.org/index.php/ijaidsml/article/view/494",
        ],
    },
    {
        "name": "ai-for-site-selection",
        "title": "AI for Site Selection",
        "description": "Geospatial ML, graph neural networks, urban knowledge graphs, and location analytics for retail, logistics, and facility siting.",
        "devin_body": r'''## When to use

You are choosing locations for stores, warehouses, facilities, or services based on demographics, competition, transport, and imagery.

## Usage

- **Location analytics**: integrate POI, mobility, satellite, and census data.
- **Graph neural networks**: model spatial interactions and neighborhood effects.
- **Urban knowledge graphs**: combine semantic urban facts with site scoring.
- **Multi-criteria decision**: balance revenue, cost, accessibility, and risk.

## Steps

1. Define site type, catchment, and success metric (revenue, footfall, ROI).
2. Assemble geospatial, mobility, demographic, and competitor data.
3. Build features and train spatial, GNN, or knowledge-graph models.
4. Score and rank candidate sites.
5. Validate with actual site performance.

## Code pattern

```python
import networkx as nx
import torch

# Build a site-neighborhood graph from a transport network
G = nx.read_graphml('transport.graphml')
# Convert to PyTorch Geometric and train a GCN for site attractiveness
```

## Tuning notes

- Use spatial cross-validation to avoid leakage.
- Combine model scores with domain knowledge and zoning.
- Update models as new sites open and competitors move.

## Verification

1. Predict sales or footfall for a set of retail sites.
2. Compare GCN scores to a baseline XGBoost location model.
3. Generate an explainable site report for stakeholders.

## References

- https://dl.acm.org/doi/10.1145/3372406
- https://doi.org/10.1108/mscra-03-2019-0010
- https://mdpi-res.com/d_attachment/remotesensing/remotesensing-14-03579/article_deploy/remotesensing-14-03579-v2.pdf?version=1659596819
- https://fi.ee.tsinghua.edu.cn/~dingjingtao/papers/KnowSite-Sigspatial23.pdf
- https://onlinelibrary.wiley.com/doi/10.1111/tgis.12553
''',
        "references": [
            "https://dl.acm.org/doi/10.1145/3372406",
            "https://doi.org/10.1108/mscra-03-2019-0010",
            "https://mdpi-res.com/d_attachment/remotesensing/remotesensing-14-03579/article_deploy/remotesensing-14-03579-v2.pdf?version=1659596819",
            "https://fi.ee.tsinghua.edu.cn/~dingjingtao/papers/KnowSite-Sigspatial23.pdf",
            "https://onlinelibrary.wiley.com/doi/10.1111/tgis.12553",
        ],
    },
    {
        "name": "ai-for-land-use",
        "title": "AI for Land Use",
        "description": "Remote sensing, multi-source data fusion, functional-zone mapping, and neural-symbolic planning for land-use analysis and policy.",
        "devin_body": r'''## When to use

You want to map, monitor, and plan land use; identify functional zones; or support zoning and environmental policy.

## Usage

- **Land-use/land-cover mapping**: use CNNs, vision transformers, and large vision-language models on remote sensing.
- **Functional zone identification**: fuse imagery, POI, building, mobility, and nightlight data.
- **Change detection**: monitor urban expansion, informal settlement, and land conversion.
- **Planning support**: combine neural predictions with planning rules and objectives.

## Steps

1. Define land-use classes and study area.
2. Gather multi-source geospatial and socio-economic data.
3. Train and validate multi-modal deep learning models.
4. Produce land-use maps and uncertainty estimates.
5. Translate maps into planning dashboards and policy inputs.

## Code pattern

```python
import torch
import torchgeo.models

# Load a pretrained remote-sensing backbone and inspect
model = torchgeo.models.resnet18(weights='sentinel2_all')
print(model)
```

## Tuning notes

- Use multi-scale and multi-temporal inputs.
- Validate against field surveys and official zoning data.
- Address class imbalance and spectral confusion in urban scenes.

## Verification

1. Classify urban land use and compute accuracy and kappa.
2. Identify functional zones in a city and compare to census/POI data.
3. Detect land-use change over a multi-year period.

## References

- https://www.sciencedirect.com/science/article/abs/pii/S0924271626001760
- https://www.frontiersin.org/journals/sustainable-cities/articles/10.3389/frsc.2026.1736773/full
- https://www.mdpi.com/2072-4292/17/6/990
- https://link.springer.com/article/10.1007/s42452-026-08351-4
- https://isprs-archives.copernicus.org/articles/XLVIII-G-2025/1647/2025/isprs-archives-XLVIII-G-2025-1647-2025.pdf
''',
        "references": [
            "https://www.sciencedirect.com/science/article/abs/pii/S0924271626001760",
            "https://www.frontiersin.org/journals/sustainable-cities/articles/10.3389/frsc.2026.1736773/full",
            "https://www.mdpi.com/2072-4292/17/6/990",
            "https://link.springer.com/article/10.1007/s42452-026-08351-4",
            "https://isprs-archives.copernicus.org/articles/XLVIII-G-2025/1647/2025/isprs-archives-XLVIII-G-2025-1647-2025.pdf",
        ],
    },
]
