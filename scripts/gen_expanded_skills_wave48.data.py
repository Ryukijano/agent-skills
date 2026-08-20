SKILLS = [
    {
        "name": "ai-for-renewable-energy",
        "title": "AI for Renewable Energy",
        "description": "Machine learning for solar, wind, and other renewable energy forecasting, resource assessment, yield optimization, and predictive O&M.",
        "devin_body": r'''## When to use

You are developing, operating, or investing in solar, wind, or other renewable assets and need data-driven forecasts, site assessment, or performance optimization.

## Usage

- **Resource assessment and site screening**: estimate long-term energy yield and geospatial suitability for new projects.
- **Generation forecasting**: predict solar and wind output from weather and satellite data for grid and market operations.
- **Yield optimization**: detect underperformance, curtailment, and inverter or turbine degradation.
- **Predictive O&M**: schedule maintenance and identify faults before they lead to major losses.

## Steps

1. Acquire historical weather, satellite imagery, SCADA, and asset metadata.
2. Curate and align geospatial and time-series datasets by project location and time.
3. Train forecasting, regression, or classification models for the target application.
4. Validate with rolling or spatial cross-validation against physical baselines.
5. Deploy forecasts and insights into dispatch, trading, or maintenance workflows.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict wind or solar power from weather features
X = df[["wind_speed", "temperature", "solar_irradiance", "cloud_cover"]]
y = df["power_output_mw"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Match model complexity to data volume and forecast horizon; satellite/nowcasting needs fast inference.
- Incorporate physical constraints such as power curves, inverter clipping, and wake effects for realism.
- Use probabilistic outputs when integrating with reserve scheduling or electricity markets.

## Verification

1. Compare deterministic and probabilistic forecasts to a persistence and climatology baseline.
2. Validate a site-assessment model on an independent measurement campaign.
3. Measure operational value such as cost savings or curtailment reduction in a backtest.

## References

- https://link.springer.com/article/10.1186/s43067-025-00239-4
- https://doi.org/10.3390/en13081979
- https://github.com/NREL/sup3r
- https://www.nrel.gov/research/software/rev-the-renewable-energy-potential-model-open-source
''',
        "references": [
            "https://link.springer.com/article/10.1186/s43067-025-00239-4",
            "https://doi.org/10.3390/en13081979",
            "https://github.com/NREL/sup3r",
            "https://www.nrel.gov/research/software/rev-the-renewable-energy-potential-model-open-source",
        ],
    },
    {
        "name": "ai-for-energy-storage",
        "title": "AI for Energy Storage",
        "description": "Machine learning for battery state estimation, degradation modeling, storage dispatch, and energy storage asset optimization.",
        "devin_body": r'''## When to use

You need to estimate battery state, predict degradation, optimize storage dispatch, or improve safety in stationary or mobile energy storage systems.

## Usage

- **State estimation**: predict state-of-charge (SOC) and state-of-health (SOH) from voltage, current, and temperature.
- **Degradation and RUL forecasting**: estimate capacity fade and remaining useful life under different operating conditions.
- **Storage dispatch**: optimize charge/discharge for arbitrage, peak shaving, or grid services.
- **Thermal and safety monitoring**: detect abnormal temperature or impedance trends.

## Steps

1. Collect voltage, current, temperature, and cycle data at appropriate sampling rates.
2. Engineer features for capacity fade, impedance growth, and thermal dynamics.
3. Train regression, time-series, or physics-informed models for SOC, SOH, or RUL.
4. Validate on independent cells or operating periods with known end-of-life.
5. Integrate estimates into a battery management or energy management system.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

X = df[["voltage", "current", "temperature", "cycle_count"]]
y = df["state_of_health"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Use physics-informed or equivalent-circuit features to improve generalization across chemistries.
- Account for temperature, C-rate, and depth-of-discharge in degradation models.
- Online SOC/SOH estimators need uncertainty quantification and routine recalibration.

## Verification

1. Compare SOC/SOH estimates to lab reference measurements.
2. Predict end-of-life capacity fade and validate against a hold-out aging test.
3. Backtest storage arbitrage policy against a simple rule-based dispatch.

## References

- https://www.mdpi.com/1996-1073/14/2/306
- https://www.mdpi.com/1996-1073/16/10/4243
- https://doi.org/10.1109/tte.2025.3525742
- https://www.nrel.gov/transportation/battery-lifespan.html
''',
        "references": [
            "https://www.mdpi.com/1996-1073/14/2/306",
            "https://www.mdpi.com/1996-1073/16/10/4243",
            "https://doi.org/10.1109/tte.2025.3525742",
            "https://www.nrel.gov/transportation/battery-lifespan.html",
        ],
    },
    {
        "name": "ai-for-smart-grid",
        "title": "AI for Smart Grid",
        "description": "AI and machine learning for load and renewable forecasting, grid state estimation, optimal power flow, and smart-grid control.",
        "devin_body": r'''## When to use

You are operating or designing a smart power grid and need accurate forecasts, fast state estimation, or scalable grid optimization.

## Usage

- **Load and renewable forecasting**: short- to medium-term predictions for operations and markets.
- **State estimation and bad-data detection**: infer grid states from SCADA and AMI measurements.
- **Optimal power flow surrogates**: accelerate AC OPF with learned approximations.
- **Anomaly and event detection**: identify disturbances, faults, and cyber-physical anomalies.

## Steps

1. Assemble grid topology, historical loads, generation, and weather data.
2. Build or train forecasting, estimation, or OPF-surrogate models.
3. Validate against physical power-flow solvers and held-out operating data.
4. Tune for reliability, latency, and constraint satisfaction.
5. Integrate with energy management, market, or control systems.

## Code pattern

```python
import pandapower as pp
import pandapower.networks as pn

net = pn.case_ieee30()
pp.runpp(net)
print(net.res_bus.vm_pu.min(), net.res_bus.vm_pu.max())
```

## Tuning notes

- Respect voltage, thermal, and ramp-rate constraints in all surrogate outputs.
- Use time-based splits and avoid leakage from future grid states.
- Combine model-based and learning-based approaches for safety-critical decisions.

## Verification

1. Run a power-flow benchmark and compare bus voltages and branch loadings.
2. Backtest a load-forecast model with rolling cross-validation.
3. Evaluate an OPF surrogate against a conventional solver on out-of-sample cases.

## References

- https://www.mdpi.com/1996-1073/18/16/4408
- https://www.mdpi.com/1996-1073/17/6/1381
- https://arxiv.org/html/2507.14117v1
- https://www.mdpi.com/2071-1050/15/6/5453
''',
        "references": [
            "https://www.mdpi.com/1996-1073/18/16/4408",
            "https://www.mdpi.com/1996-1073/17/6/1381",
            "https://arxiv.org/html/2507.14117v1",
            "https://www.mdpi.com/2071-1050/15/6/5453",
        ],
    },
    {
        "name": "ai-for-distributed-energy",
        "title": "AI for Distributed Energy",
        "description": "Machine learning and multi-agent methods for DER forecasting, microgrid optimization, peer-to-peer trading, and prosumer coordination.",
        "devin_body": r'''## When to use

You are coordinating distributed energy resources such as rooftop solar, batteries, EVs, and flexible loads behind the meter.

## Usage

- **DER generation and load forecasting**: predict net load and behind-the-meter generation.
- **Microgrid energy management**: schedule generation, storage, and load for islanded or grid-connected operation.
- **Peer-to-peer and transactive energy trading**: design local markets among prosumers.
- **Grid-aware coordination**: manage rooftop PV, batteries, and EVs under network constraints.

## Steps

1. Model the mix of DER assets, network topology, and market rules.
2. Collect smart-meter, inverter, and weather data at the distribution level.
3. Train forecasting, optimization, or reinforcement learning agents.
4. Validate in co-simulation or a digital-twin environment.
5. Deploy with aggregation, settlement, and cybersecurity controls.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Forecast net load at a prosumer site
X = df[["pv_generation", "battery_soc", "ev_demand", "hour", "temp"]]
y = df["net_load"]

model = RandomForestRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Preserve network constraints such as voltage and capacity in local and P2P trades.
- Use privacy-preserving or federated learning when data are distributed.
- Account for behavioral heterogeneity and non-stationarity among prosumers.

## Verification

1. Simulate DER coordination and compare cost and self-consumption to a baseline.
2. Test a P2P trading policy for feasibility and fairness in a multi-agent setting.
3. Validate microgrid scheduling against real operating constraints.

## References

- https://www.nature.com/articles/s41598-026-58710-9
- https://doi.org/10.1016/j.egyr.2026.109367
- https://doi.org/10.1016/j.apenergy.2025.125485
- https://arxiv.org/html/2605.21396
''',
        "references": [
            "https://www.nature.com/articles/s41598-026-58710-9",
            "https://doi.org/10.1016/j.egyr.2026.109367",
            "https://doi.org/10.1016/j.apenergy.2025.125485",
            "https://arxiv.org/html/2605.21396",
        ],
    },
    {
        "name": "ai-for-demand-response",
        "title": "AI for Demand Response",
        "description": "Machine learning for load flexibility estimation, demand response program design, virtual power plant dispatch, and dynamic pricing.",
        "devin_body": r'''## When to use

You need to unlock flexible load, operate a virtual power plant, design demand-response programs, or optimize time-varying tariffs.

## Usage

- **Baseline load estimation**: estimate counterfactual consumption for settlement.
- **Virtual power plant dispatch**: aggregate and control distributed flexible resources.
- **Dynamic pricing and tariffs**: optimize time-of-use or real-time prices.
- **Customer segmentation and targeting**: enroll and nudge the most flexible participants.

## Steps

1. Collect AMI, thermostat, EV, and building energy data with timestamps.
2. Identify flexible loads and estimate counterfactual baselines.
3. Train forecasting, classification, or reinforcement learning models.
4. Validate on randomized pilots or natural experiments.
5. Deploy dispatch and pricing signals with feedback and telemetry.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Estimate flexible capacity from historical load and weather
X = df[["hour", "temperature", "baseline_load", "tariff"]]
y = df["flexible_load"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Control for weather, occupancy, and economic confounders in baseline estimation.
- Use causal estimators when evaluating demand-response effects.
- Provide customer comfort and fairness constraints in automated control.

## Verification

1. Compare predicted baseline to a control group or weather-normalized baseline.
2. Run a DR event and measure actual vs. predicted load curtailment.
3. Backtest a VPP dispatch policy in a distribution system simulator.

## References

- https://www.mdpi.com/1996-1073/19/4/1084
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0339606
- https://www.mdpi.com/1996-1073/18/23/6341
- https://www.mdpi.com/1996-1073/18/18/4844
''',
        "references": [
            "https://www.mdpi.com/1996-1073/19/4/1084",
            "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0339606",
            "https://www.mdpi.com/1996-1073/18/23/6341",
            "https://www.mdpi.com/1996-1073/18/18/4844",
        ],
    },
    {
        "name": "ai-for-energy-trading",
        "title": "AI for Energy Trading",
        "description": "Machine learning for electricity price forecasting, algorithmic trading, arbitrage, and bidding in day-ahead, intraday, and balancing markets.",
        "devin_body": r'''## When to use

You need to forecast electricity prices, bid into wholesale or balancing markets, or trade energy across time and markets.

## Usage

- **Price forecasting**: day-ahead, intraday, and balancing market price prediction.
- **Statistical arbitrage and position management**: exploit price differences across markets.
- **Asset bidding strategies**: optimize bids for batteries, renewables, and VPPs.
- **Risk and imbalance management**: manage exposure and penalty costs.

## Steps

1. Gather historical prices, order books, weather, and fuel/renewable forecasts.
2. Engineer features for seasonality, calendar effects, and cross-market spreads.
3. Train time-series, quantile, or reinforcement learning models.
4. Validate with walk-forward backtests that respect market settlement rules.
5. Deploy with position sizing, risk limits, and human oversight.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict next-hour day-ahead price from demand and renewable forecasts
X = df[["load_forecast", "wind_forecast", "solar_forecast", "hour"]]
y = df["price_eur_mwh"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Avoid look-ahead bias and use chronological cross-validation.
- Use probabilistic or quantile forecasts to size positions and manage risk.
- Consider transaction costs, imbalance penalties, and market coupling.

## Verification

1. Backtest a trading strategy against a buy-and-hold or benchmark forecaster.
2. Report directional accuracy, profit/loss, and Sharpe-like metrics.
3. Compare predicted price distributions to actual clearing prices.

## References

- https://doi.org/10.1016/j.segan.2023.101023
- https://doi.org/10.48550/arxiv.2506.00044
- https://doi.org/10.1016/j.egyai.2022.100139
- https://arxiv.org/html/2602.10071v2
''',
        "references": [
            "https://doi.org/10.1016/j.segan.2023.101023",
            "https://doi.org/10.48550/arxiv.2506.00044",
            "https://doi.org/10.1016/j.egyai.2022.100139",
            "https://arxiv.org/html/2602.10071v2",
        ],
    },
    {
        "name": "ai-for-water-utilities",
        "title": "AI for Water Utilities",
        "description": "Machine learning for water demand forecasting, leak detection, quality monitoring, pump scheduling, and smart water distribution.",
        "devin_body": r'''## When to use

You manage a water distribution network and want to reduce losses, improve demand forecasting, monitor quality, or optimize pumping energy.

## Usage

- **Water demand forecasting**: predict consumption at district metered area or customer level.
- **Leak and burst detection**: identify anomalies from pressure and flow sensors.
- **Water quality monitoring**: detect contamination and source tracking.
- **Pump and energy optimization**: schedule pumps to reduce energy and pressure transients.

## Steps

1. Deploy smart meters, pressure sensors, and quality monitors across the network.
2. Integrate GIS, SCADA, and weather data into a data platform.
3. Train time-series, anomaly, or optimization models for each use case.
4. Validate geographically and temporally on independent district metered areas.
5. Integrate alerts and control with maintenance and operations teams.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import IsolationForest

X = df[["flow_rate", "pressure", "hour", "day_of_week"]]
clf = IsolationForest(contamination=0.01, random_state=42)
clf.fit(X)
df["anomaly_score"] = clf.decision_function(X)
```

## Tuning notes

- Water data are noisy and seasonal; use robust normalization and calendar features.
- Combine physical hydraulic models with ML for anomaly localization.
- Maintain data privacy and security for customer-level metering.

## Verification

1. Detect leaks and bursts and compare to reported maintenance records.
2. Backtest demand forecasts against actual consumption.
3. Measure pump energy savings from optimized scheduling.

## References

- https://link.springer.com/article/10.1007/s10462-024-11093-7
- https://doi.org/10.1016/j.asoc.2026.115061
- https://www.mdpi.com/2073-4441/16/23/3410
- https://link.springer.com/article/10.1007/s43832-026-00365-8
''',
        "references": [
            "https://link.springer.com/article/10.1007/s10462-024-11093-7",
            "https://doi.org/10.1016/j.asoc.2026.115061",
            "https://www.mdpi.com/2073-4441/16/23/3410",
            "https://link.springer.com/article/10.1007/s43832-026-00365-8",
        ],
    },
    {
        "name": "ai-for-wastewater",
        "title": "AI for Wastewater",
        "description": "Machine learning for process monitoring, anomaly detection, influent forecasting, and control in wastewater treatment plants.",
        "devin_body": r'''## When to use

You operate or design a wastewater treatment plant and need to forecast influent loads, detect process anomalies, or optimize energy and chemical use.

## Usage

- **Influent flow and load forecasting**: predict hydraulic and organic loading.
- **Anomaly and fault detection**: detect process upsets, sensor faults, and cyber intrusions.
- **Sensor calibration and data quality**: self-calibrate and impute missing sensor values.
- **Aeration and dosing control**: optimize energy and chemical consumption.

## Steps

1. Install or access SCADA, lab, and online sensor data from the plant.
2. Clean multivariate time-series and label known process upsets.
3. Train forecasting, classification, or control models for each target.
4. Validate across seasons, influent conditions, and plant configurations.
5. Deploy with operator-facing dashboards and control-loop integration.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

X = df[["influent_flow", "cod", "nh3n", "do", "mlss"]]
y = df["process_anomaly"]

model = RandomForestClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Wastewater processes are non-stationary; retrain models with seasonal data.
- Use interpretable models or SHAP for operator trust.
- Ensure regulatory compliance for effluent quality when using ML for control.

## Verification

1. Predict influent load and compare to lab measurements.
2. Detect anomalies and verify against operator event logs.
3. Measure energy or chemical savings from optimized aeration or dosing.

## References

- https://doi.org/10.1016/j.jenvman.2025.126886
- https://doi.org/10.5194/egusphere-egu26-13096
- https://link.springer.com/article/10.1007/s11431-025-3110-2
- https://doi.org/10.3390/w17192842
''',
        "references": [
            "https://doi.org/10.1016/j.jenvman.2025.126886",
            "https://doi.org/10.5194/egusphere-egu26-13096",
            "https://link.springer.com/article/10.1007/s11431-025-3110-2",
            "https://doi.org/10.3390/w17192842",
        ],
    },
    {
        "name": "ai-for-gas-utilities",
        "title": "AI for Gas Utilities",
        "description": "Machine learning for natural gas demand forecasting, pipeline leak detection, compressor optimization, and asset integrity.",
        "devin_body": r'''## When to use

You operate a natural gas distribution or transmission network and need to forecast demand, detect leaks, optimize compression, or manage asset integrity.

## Usage

- **Short-term gas demand and line-pack forecasting**: predict consumption and network storage.
- **Pipeline leak detection and localization**: identify and locate leaks from pressure and flow data.
- **Asset condition and risk-based maintenance**: prioritize inspections and replacements.
- **Customer and billing analytics**: detect anomalies and support demand-side programs.

## Steps

1. Collect flow, pressure, temperature, and weather data across the network.
2. Build network topology and asset condition datasets.
3. Train forecasting, classification, or optimization models.
4. Validate with geographical and temporal holdouts.
5. Integrate with SCADA, GIS, and enterprise asset management.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Forecast short-term gas demand from weather and calendar
X = df[["temperature", "hour", "day_of_week", "industrial_load"]]
y = df["gas_demand"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Gas demand is highly weather and industrial-driven; include heating-degree days.
- Leak detection needs real-time pressure and flow monitoring plus ground truthing.
- Ensure safety and regulatory compliance for any automated control.

## Verification

1. Backtest demand forecasts against actual city-gate or customer consumption.
2. Evaluate leak detection precision and recall on confirmed incidents.
3. Measure compressor energy savings from optimized scheduling.

## References

- https://doi.org/10.3390/en19041101
- https://www.mdpi.com/1996-1073/17/21/5517
- https://www.osti.gov/biblio/1996417
- https://doi.org/10.3389/fenvs.2025.1569621
''',
        "references": [
            "https://doi.org/10.3390/en19041101",
            "https://www.mdpi.com/1996-1073/17/21/5517",
            "https://www.osti.gov/biblio/1996417",
            "https://doi.org/10.3389/fenvs.2025.1569621",
        ],
    },
    {
        "name": "ai-for-electric-vehicles",
        "title": "AI for Electric Vehicles",
        "description": "Machine learning for battery management, range and energy consumption prediction, predictive maintenance, and EV powertrain optimization.",
        "devin_body": r'''## When to use

You are developing or operating electric vehicles and need to predict range, estimate battery state, diagnose faults, or optimize energy use.

## Usage

- **Range and energy consumption prediction**: estimate remaining driving range and trip energy.
- **Battery state and health estimation**: infer SOC and SOH from onboard data.
- **Predictive diagnostics and thermal management**: detect faults and manage battery temperature.
- **Driver behavior and route optimization**: personalize energy estimates and charging plans.

## Steps

1. Collect CAN bus, telemetry, battery, weather, and route data.
2. Engineer features for driving behavior, state of charge, and battery health.
3. Train regression or time-series models for range, SOC, or SOH.
4. Validate on diverse routes, climates, and driving styles.
5. Deploy in the vehicle, mobile app, or fleet platform.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict trip energy consumption
X = df[["distance_km", "avg_speed", "temp", "soc_start", "elevation"]]
y = df["energy_kwh"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Include real-time driving behavior, HVAC, and battery state for accuracy.
- Update models as the battery ages; track state-of-health online.
- Consider edge inference latency and safety-critical validation.

## Verification

1. Compare predicted range to actual trip consumption on a hold-out set.
2. Validate battery SOH predictions with periodic diagnostic cycles.
3. Measure improvement in route and energy planning versus nominal ratings.

## References

- https://www.sciencedirect.com/science/article/abs/pii/S1361920925002056
- https://link.springer.com/article/10.1007/s44163-025-00721-y
- https://doi.org/10.1038/s41598-026-49119-5
- https://www.sciencedirect.com/science/article/abs/pii/S0360544225032062
''',
        "references": [
            "https://www.sciencedirect.com/science/article/abs/pii/S1361920925002056",
            "https://link.springer.com/article/10.1007/s44163-025-00721-y",
            "https://doi.org/10.1038/s41598-026-49119-5",
            "https://www.sciencedirect.com/science/article/abs/pii/S0360544225032062",
        ],
    },
    {
        "name": "ai-for-charging-infrastructure",
        "title": "AI for Charging Infrastructure",
        "description": "Machine learning for EV charging demand forecasting, station scheduling, load balancing, and grid-integrated charging control.",
        "devin_body": r'''## When to use

You are planning, operating, or controlling EV charging infrastructure and need to forecast demand, balance load, or integrate with the grid.

## Usage

- **Charging demand and occupancy forecasting**: predict station utilization.
- **Smart charge scheduling and load balancing**: shift and throttle charging to reduce grid impact.
- **Station placement and utilization optimization**: plan new sites and capacity.
- **Anomaly detection and predictive maintenance**: identify faulty chargers before users do.

## Steps

1. Collect charging-session, grid, and EV fleet data from charge point systems.
2. Engineer features for time, location, tariff, and grid state.
3. Train forecasting, scheduling, or reinforcement learning models.
4. Validate with simulation or A/B testing at live stations.
5. Deploy via OCPP or grid-aware control interfaces.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Forecast station occupancy
X = df[["hour", "day_of_week", "temperature", "tariff", "nearby_events"]]
y = df["occupancy"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Respect transformer capacity and grid constraints in charging schedules.
- Use fair scheduling that limits excessive user delays.
- Combine edge and cloud inference for low-latency control.

## Verification

1. Backtest charging demand forecasts at individual stations.
2. Simulate load balancing and measure peak reduction and cost savings.
3. Detect charger faults and compare to maintenance logs.

## References

- https://doi.org/10.1038/s41598-026-49535-7
- https://link.springer.com/article/10.1007/s10586-026-06174-x
- https://www.mdpi.com/2032-6653/16/3/184
- https://www.nature.com/articles/s41598-025-22482-5
''',
        "references": [
            "https://doi.org/10.1038/s41598-026-49535-7",
            "https://link.springer.com/article/10.1007/s10586-026-06174-x",
            "https://www.mdpi.com/2032-6653/16/3/184",
            "https://www.nature.com/articles/s41598-025-22482-5",
        ],
    },
    {
        "name": "ai-for-grid-resilience",
        "title": "AI for Grid Resilience",
        "description": "Machine learning for outage prediction, storm hardening, restoration planning, and cyber-physical resilience of power systems.",
        "devin_body": r'''## When to use

You need to prepare for, respond to, or recover from extreme events, cyber threats, and asset failures affecting power systems.

## Usage

- **Storm and weather-driven outage prediction**: forecast outage occurrence, duration, and damage.
- **Grid hardening and vegetation management prioritization**: target investments to reduce risk.
- **Post-event restoration and crew routing**: optimize repair sequences and resource staging.
- **Cyber and physical anomaly detection**: identify intrusions and equipment misoperation.

## Steps

1. Integrate weather, asset, vegetation, outage, and AMI data.
2. Build predictive models for outage occurrence, duration, and damage.
3. Evaluate hardening and resource-staging scenarios.
4. Validate on historical storm events and counterfactual analysis.
5. Deploy with emergency operations and grid control centers.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Predict outage risk for distribution segments before a storm
X = df[["max_wind_speed", "precipitation", "tree_density", "pole_age"]]
y = df["outage_occurred"]

model = RandomForestClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Use spatiotemporal and graph-aware models for network propagation.
- Account for extreme-event rarity and class imbalance.
- Combine physics-based fragility models with ML for trustworthy hardening decisions.

## Verification

1. Backtest outage prediction on historical storms and report AUC and precision-recall.
2. Compare hardening plans under budget constraints with a cost-benefit metric.
3. Validate restoration time estimates against actual crew dispatch records.

## References

- https://doi.org/10.3390/electronics15102001
- https://doi.org/10.3390/en19020506
- https://doi.org/10.1016/j.ress.2024.110169
- https://doi.org/10.1186/s43065-025-00154-y
''',
        "references": [
            "https://doi.org/10.3390/electronics15102001",
            "https://doi.org/10.3390/en19020506",
            "https://doi.org/10.1016/j.ress.2024.110169",
            "https://doi.org/10.1186/s43065-025-00154-y",
        ],
    },
]
