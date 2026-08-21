SKILLS = [
    {
        "name": "ai-for-additive-manufacturing",
        "title": "AI for Additive Manufacturing",
        "description": "Use machine learning on in-situ sensor and process data together with post-build inspection to detect defects, optimize build settings and certify metal or polymer additive parts.",
        "devin_body": r'''## When to use

You are optimizing metal or polymer additive manufacturing processes, predicting part quality from build parameters, detecting defects from in-situ sensor data, or training surrogate models for residual stress and distortion.

## Usage

- **Monitor in-situ**: analyze melt-pool images, photodiode signals, thermal data, and acoustic emissions.
- **Detect defects**: classify porosity, balling, lack of fusion, and cracks during the build.
- **Optimize parameters**: relate laser power, scan speed, and hatch spacing to density and microstructure.
- **Predict microstructure**: link thermal history to grain structure, phase, and mechanical properties.
- **Reduce inspection**: replace or prioritize destructive and CT testing with in-situ quality metrics.

## Steps

1. Collect in-situ sensor data and process logs synchronized to layer and build coordinates.
2. Label or segment anomalies using XCT, microscopy, or post-build NDT as ground truth.
3. Extract spatiotemporal features and train a defect classifier on layer-wise signals.
4. Relate process parameters and thermal history to porosity, microstructure, and properties.
5. Optimize process parameters with surrogate models or Bayesian optimization.
6. Validate in-situ predictions against physical tests and qualify the workflow.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Predict porosity class from PBF process features
X = df[["laser_power_W", "scan_speed_mm_s", "hatch_spacing_mm", "layer_thickness_mm"]]
y = df["porosity_class"]  # none / low / high
model = GradientBoostingClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Include physically meaningful features such as energy density and normalized enthalpy.
- In-situ data are high-rate and high-volume; downsample or window before model training.
- Class imbalance is common for defects; use stratified sampling, class weights, or anomaly detection.
- Validate across different machines, powder lots, and build geometries to check generalization.

## Verification

1. Train a defect classifier on melt-pool images and compare precision-recall per defect type.
2. Predict relative density from process parameters and compare to Archimedes or X-ray measurements.
3. Build a surrogate for distortion and validate against a full thermomechanical simulation.
''',
        "references": [
            "https://doi.org/10.1007/s10845-024-02490-4",
            "https://www.sciencedirect.com/science/article/pii/S2588840424000933",
            "https://www.sciencedirect.com/science/article/abs/pii/S1526612523005212",
            "https://www.sciencedirect.com/science/article/abs/pii/S1526612526003907",
            "https://doi.org/10.1080/17452759.2023.2196266",
        ],
    },
    {
        "name": "ai-for-composites-manufacturing",
        "title": "AI for Composites Manufacturing",
        "description": "Use computer vision and machine learning to inspect automated fiber placement and tape-laying processes, detect defects and optimize thermal and compaction parameters in composite curing.",
        "devin_body": r'''## When to use

You are manufacturing fiber-reinforced composite parts and need to detect layup defects, predict cure state, optimize AFP/ATL process parameters, or build digital twins for autoclave and resin-infusion processes.

## Usage

- **Inspect AFP**: detect gaps, overlaps, twists, and foreign objects with in-process cameras and laser profilometry.
- **Monitor cure**: use thermal sensors and dielectric analysis to track resin flow and degree of cure.
- **Predict quality**: relate tow placement, compaction, and temperature to voids and mechanical properties.
- **Optimize autoclave**: reduce cure cycle time and energy while meeting quality specs.
- **Build digital twins**: fuse process, inspection, and simulation data for closed-loop control.

## Steps

1. Collect in-process images, laser scans, and cure sensor data from AFP or ATL lines.
2. Annotate defect classes and register data to a 3D digital layup model.
3. Train CNN or segmentation models to detect and classify defects in real time.
4. Model cure kinetics and thermal history to predict degree of cure and residual stress.
5. Optimize placement and cure parameters with a surrogate or physics-informed model.
6. Validate part quality with ultrasound, CT, or mechanical testing and close the feedback loop.

## Code pattern

```python
import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Classify small image patches from AFP laser profilometry
patches = np.array([cv2.resize(img, (64, 64)).flatten() for img in patch_list])
labels = ["good", "gap", "overlap", "wrinkle"]
clf = RandomForestClassifier(n_estimators=200, random_state=42).fit(patches, labels)
```

## Tuning notes

- Defect classes are imbalanced; collect normal examples and use few-shot or anomaly learning.
- Cure data depend strongly on part geometry and tool thermal mass; normalize by thickness and heat transfer.
- Use sim-to-real techniques when real labeled data are limited.
- Align sensor and machine coordinate systems before mapping defects back to the layup.

## Verification

1. Detect and classify AFP defects on a labeled test set and compare to manual inspection.
2. Predict spring-in or fiber angle deviation and validate against CMM or destructive inspection.
3. Optimize a cure cycle with a surrogate and verify part porosity and Tg against baseline.
''',
        "references": [
            "https://doi.org/10.3390/polym17182557",
            "https://doi.org/10.1016/j.matdes.2024.113247",
            "https://www.sciencedirect.com/science/article/abs/pii/S0263822320313659",
            "https://doi.org/10.1016/j.addma.2023.103721",
            "https://doi.org/10.1007/s42452-026-08323-8",
        ],
    },
    {
        "name": "ai-for-semiconductor-manufacturing",
        "title": "AI for Semiconductor Manufacturing",
        "description": "Use AI to predict wafer yield, detect defects, run virtual metrology, schedule equipment and control advanced processes in high-volume semiconductor fabrication.",
        "devin_body": r'''## When to use

You are working with wafer fabrication data, trying to predict die yield, classify wafer or equipment faults, build virtual metrology models, or optimize lithography and etch processes.

## Usage

- **Virtual metrology**: predict wafer properties such as film thickness and CD from tool sensor data.
- **Defect detection**: classify wafer defects, reticle defects, and macro defects from images.
- **Yield prediction**: combine process parameters, tool data, and inspection results to forecast yield.
- **Predictive maintenance**: forecast tool failures, chamber matching issues, and unscheduled downtime.
- **Run-to-run control**: adjust process recipes based on real-time predictions and feedback.

## Steps

1. Collect tool sensor data, process parameters, and inspection/metrology results per wafer.
2. Build a virtual metrology model for target properties and validate against physical measurements.
3. Train defect classifiers on wafer images and review precision-recall for each defect type.
4. Engineer wafer-level features for yield prediction and rank root causes.
5. Deploy a run-to-run controller that updates recipe parameters based on predictions.
6. Continuously retrain models as tools, products, and processes evolve.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit

# Predict final test yield from chamber and metrology features
X = df[["etch_time", "chamber_pressure", "rf_power", "cd_inline", "film_thickness"]]
y = df["final_test_yield"]
model = RandomForestRegressor(random_state=42)
for train, test in TimeSeriesSplit(n_splits=5).split(X):
    model.fit(X.iloc[train], y.iloc[train])
```

## Tuning notes

- Semiconductor data are high-dimensional, sparse, and confidential; use dimensionality reduction and cross-fitting.
- Tool trace data are time series; include temporal features and rolling statistics, not just single values.
- Concept drift is common as chambers age or products change; monitor model performance continuously.
- Use explainability to identify root causes and avoid spurious correlations from correlated process steps.

## Verification

1. Predict wafer yield from equipment data and compare to actual final test results on a held-out lot.
2. Build an FDC model that flags anomalous chambers and validate against known maintenance events.
3. Train a virtual metrology model for film thickness and compare to inline measurement.
''',
        "references": [
            "https://doi.org/10.1109/AIAC63745.2024.10899729",
            "https://doi.org/10.1109/AIHCIR67580.2025.11404861",
            "https://doi.org/10.1007/s00170-026-18104-7",
            "https://www.mdpi.com/2076-3417/13/4/2660",
            "https://doi.org/10.1109/ACCESS.2021.3117576",
        ],
    },
    {
        "name": "ai-for-nanomanufacturing",
        "title": "AI for Nanomanufacturing",
        "description": "Use machine learning to control, inspect and optimize nanoimprint lithography, roll-to-roll patterning, self-assembly and nanoscale metrology for high-throughput nanofabrication.",
        "devin_body": r'''## When to use

You are developing scalable nanomanufacturing processes such as roll-to-roll nanoimprint, directed self-assembly, or top-down patterning, and need to model process–structure relationships, optimize throughput, or detect nanoscale defects.

## Usage

- **Control NIL**: tune pressure, temperature, and UV dose to minimize residual layer and defects.
- **In-line metrology**: use scatterometry, diffractometry, and hyperspectral imaging for CD and thickness.
- **Pattern inspection**: detect nanoscale defects and dimensional drift in roll-to-roll processes.
- **Model self-assembly**: predict block-copolymer or colloidal assembly morphologies.
- **Optimize process windows**: combine simulation, metrology, and ML for robust nanofabrication.

## Steps

1. Define critical dimensions and select in-line or off-line metrology for the nanofeature.
2. Collect process parameters and metrology data across conditions and materials.
3. Train a regression or classification model to predict CD, defects, or yield.
4. Use optical scatterometry or diffractometry to enable high-speed in-line inspection.
5. Optimize process settings with Bayesian or physics-informed surrogate models.
6. Validate nanoscale accuracy against SEM, AFM, or TEM and feed results back to the model.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

# Predict pattern yield from process parameters
X = df[["imprint_force_mN", "resist_thickness_nm", "temperature_C", "release_speed_mm_s"]]
y = df["pattern_yield"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Nanoscale signals are noisy; use domain-informed smoothing and feature normalization.
- Labeled defect data are scarce; leverage synthetic data and physics-based augmentation.
- Process models must respect physical constraints such as feature aspect ratios and resolution limits.
- Validate metrology models against calibrated reference standards such as CD-SEM.

## Verification

1. Predict line-edge roughness or critical dimension from process data and compare to metrology.
2. Detect nanoscale defects in SEM or scatterometry images and compute F-score vs expert labels.
3. Optimize a roll-to-roll recipe and demonstrate improved yield and throughput in a short run.
''',
        "references": [
            "https://doi.org/10.1088/1361-6528/add304",
            "https://doi.org/10.3390/ma17071621",
            "https://doi.org/10.3390/nano12152646",
            "https://doi.org/10.2174/9798898812942125010010",
            "https://doi.org/10.1515/revce-2024-0029",
        ],
    },
    {
        "name": "ai-for-textile-manufacturing",
        "title": "AI for Textile Manufacturing",
        "description": "Use computer vision and time-series machine learning with process control to inspect fabrics, optimize dyeing, reduce defects and predict loom and knitting machine performance in textile production.",
        "devin_body": r'''## When to use

You are automating textile production lines, detecting fabric defects, predicting dye recipes, optimizing loom parameters, or monitoring the quality of spinning, weaving, and finishing processes.

## Usage

- **Detect defects**: inspect woven, knitted, and printed fabric for stains, holes, broken yarns, and color variations.
- **Optimize dyeing**: control pH, temperature, and dye concentration using color feedback.
- **Predict maintenance**: forecast loom, spindle, and knitting faults from vibration and sound.
- **Classify fibers**: identify fiber types, blends, and yarn quality from images and spectra.
- **Reduce waste**: adjust process settings in real time to minimize defects and rework.

## Steps

1. Capture images or sensor data from looms, dyeing lines, or inspection stations.
2. Annotate fabric defects and color deviations with operators and reference standards.
3. Train detection or segmentation models and validate on production-line speed.
4. Build a color and chemistry feedback model for dyeing baths.
5. Implement predictive maintenance on machine health signals.
6. Measure defect reduction, color consistency, and throughput improvements.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

# Predict K/S color strength from dyeing recipe and process parameters
X = df[["dye_concentration_g_l", "temperature_C", "time_min", "salt_g_l", "pH"]]
y = df["K_S_value"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Textile data are highly variable due to fiber blends, finishing, and lighting conditions.
- Use color spaces (CIELAB, HSV) and color constancy for dye and shade tasks.
- Defect datasets are imbalanced; consider autoencoders or one-class classifiers.
- Generalize across loom types and suppliers by including machine-level features.

## Verification

1. Train a fabric defect detector and report precision-recall against human graders.
2. Predict a dye recipe from target color and compare delta-E to a reference formulation.
3. Forecast loom downtime from sensor data and compare to maintenance logs.
''',
        "references": [
            "https://doi.org/10.1177/00405175241268619",
            "https://www.mdpi.com/2673-7248/5/2/12",
            "https://www.mdpi.com/2078-2489/15/8/476",
            "https://doi.org/10.3390/info17070623",
            "https://doi.org/10.1109/ACCESS.2021.3117261",
        ],
    },
    {
        "name": "ai-for-polymer-processing",
        "title": "AI for Polymer Processing",
        "description": "Use machine learning on polymer processing data to predict part quality, detect instabilities, optimize cycle times and reduce scrap.",
        "devin_body": r'''## When to use

You are running polymer processing equipment and need to set initial operating points, predict part quality, monitor melt quality, detect process instabilities, or optimize energy and material use in extrusion, injection, or blow molding.

## Usage

- **Predict quality**: forecast dimensional, cosmetic, and mechanical properties from process data.
- **Detect instabilities**: identify flow-front, pressure, and temperature excursions.
- **Optimize parameters**: tune injection velocity, pack/hold, cooling, and extruder settings.
- **Monitor extrusion**: predict diameter, thickness, and die swell from in-line sensors.
- **Reduce scrap**: classify and trace defects to root process conditions.

## Steps

1. Install sensors for temperature, pressure, flow, and machine setpoints and log per-shot data.
2. Label quality outcomes and defects from inspection or SPC data.
3. Train regression or classification models to predict part quality or stability.
4. Identify key process parameters with feature importance and DOE validation.
5. Optimize settings with surrogate models and validate on production trials.
6. Deploy a real-time dashboard and controller to flag out-of-control conditions.

## Code pattern

```python
import pandas as pd
from sklearn.neural_network import MLPRegressor

# Predict part weight and warpage from molding settings
X = df[["melt_temp_C", "mold_temp_C", "injection_speed_mm_s", "packing_pressure_MPa", "cooling_time_s"]]
y = df[["part_weight_g", "warpage_mm"]]
model = MLPRegressor(hidden_layer_sizes=(64, 64), random_state=42, max_iter=2000).fit(X, y)
```

## Tuning notes

- Recycled polymers have variable properties; include rheology or MFI features where possible.
- Batch effects and machine differences are common; use domain adaptation or per-machine models.
- Optimize with simulation data but validate on real parts with DOE.
- Time-series process signatures need windowing and trend removal.

## Verification

1. Predict part quality metrics from machine settings and compare to measured dimensions.
2. Recommend initial screw speed and back pressure for a target plasticizing time.
3. Detect a short-shot or flash condition from pressure traces and confirm with part inspection.
''',
        "references": [
            "https://doi.org/10.3390/polym12061306",
            "https://www.mdpi.com/2073-4360/13/16/2652",
            "https://www.mdpi.com/2073-4360/16/16/2247",
            "https://doi.org/10.1039/d5fd00066a",
            "https://www.mdpi.com/2073-4360/17/7/940",
        ],
    },
    {
        "name": "ai-for-metal-forming",
        "title": "AI for Metal Forming",
        "description": "Use machine learning and finite-element surrogates to predict springback, wrinkling and tearing while optimizing die design and controlling stamping and deep-drawing or forging processes.",
        "devin_body": r'''## When to use

You are designing or troubleshooting sheet-metal, forging, or extrusion processes and need to predict springback, wrinkling, or tearing, optimize blank geometry, select forming parameters, or build fast surrogate models from finite element analysis.

## Usage

- **Predict springback**: build data-driven or physics-informed surrogate models from FEA data.
- **Optimize die geometry**: suggest addendum, radii, and drawbeads to reduce defects.
- **Classify defects**: detect wrinkles, splits, and surface defects from images or simulations.
- **Select parameters**: recommend blank holder force, friction, and punch speed.
- **Accelerate FEA**: replace expensive simulations with fast ML surrogates for design exploration.

## Steps

1. Generate or collect FEA simulation data with varying material, geometry, and process parameters.
2. Train surrogate models to predict springback, stress, or forming limit diagrams.
3. Use the surrogate to optimize die geometry and process parameters with search algorithms.
4. Validate surrogate predictions against physical stampings, deep draws, or forging trials.
5. Detect forming defects in images and trace them to process conditions.
6. Deploy the optimized parameters and monitor production for drift.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict springback angle from process and material features
X = df[["blank_holder_force_kN", "die_radius_mm", "friction_coeff", "yield_strength_MPa", "sheet_thickness_mm"]]
y = df["springback_angle_deg"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Material properties vary by batch; include tensile test or constitutive model features.
- FEA data are expensive; use active learning or Bayesian optimization to select simulations.
- Geometry matters: encode part geometry with SDFs, graphs, or simple shape descriptors.
- Uncertainty quantification is important because small parameter changes affect springback.

## Verification

1. Predict springback for a set of stamped parts and compare to CMM or FEA results.
2. Optimize blank shape with a surrogate and verify reduced scrap or springback.
3. Detect forming defects such as splits or wrinkles and compare to production data.
''',
        "references": [
            "https://doi.org/10.1007/s00170-025-15958-1",
            "https://doi.org/10.1088/1742-6596/3104/1/012060",
            "https://doi.org/10.3390/jmmp9060197",
            "https://doi.org/10.29081/jesr.v30i1.005",
            "https://www.sciencedirect.com/science/article/abs/pii/S0263224119301526",
        ],
    },
    {
        "name": "ai-for-casting",
        "title": "AI for Casting",
        "description": "Use AI and digital twins to predict casting defects, microstructure and mechanical properties and optimize gating and solidification in foundries.",
        "devin_body": r'''## When to use

You are producing cast metal components and need to predict porosity, hot tearing, or shrinkage, optimize gating and risering, build digital twins of solidification, or improve energy and material efficiency in foundries.

## Usage

- **Predict defects**: forecast porosity, shrinkage, hot tearing, and cold shuts from process data.
- **Model microstructure**: predict SDAS, grain size, and phase fractions from thermal history.
- **Simulate solidification**: use FEA, cellular automata, or phase-field methods.
- **Optimize gating and risering**: reduce scrap and improve yield with data-driven design.
- **Build digital twins**: synchronize foundry sensors with virtual models in real time.

## Steps

1. Collect geometry, alloy composition, mold, and process data for historical castings.
2. Run casting simulations and label defects and microstructure from inspection and testing.
3. Train ML models to predict defect probability and microstructure metrics.
4. Optimize gating, risering, and process settings with surrogate or physics-informed models.
5. Validate predictions with physical castings and NDT or mechanical tests.
6. Deploy a digital twin that updates from foundry sensors and predicts part quality.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Classify defect risk from casting parameters and alloy composition
X = df[["pour_temp_C", "mold_temp_C", "pour_time_s", "cooling_rate_C_s", "Si_pct", "Cu_pct"]]
y = df["defect_present"]
model = RandomForestClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Casting data are sparse and imbalanced; use rare-event metrics and balanced resampling.
- Multi-scale effects require features from both macro process and microstructure models.
- Defect labels are often post-process and delayed; incorporate defect type and location.
- Validate on physical castings, not only simulation, because turbulence and oxide effects are hard to model.

## Verification

1. Predict hot tearing or porosity from process data and compare to radiography or cut-up results.
2. Optimize a gating or riser design with a surrogate and verify improved yield.
3. Build a digital twin that synchronizes simulated and measured temperatures.
''',
        "references": [
            "https://doi.org/10.1007/s43939-026-00685-5",
            "https://www.mdpi.com/2076-3417/12/7/3264",
            "https://doi.org/10.24425/amm.2024.151428",
            "https://www.nature.com/articles/s41524-025-01524-6",
            "https://doi.org/10.2320/matertrans.mt-la2022038",
        ],
    },
    {
        "name": "ai-for-welding",
        "title": "AI for Welding",
        "description": "Use machine learning and multi-modal sensing to monitor weld quality, predict penetration and bead geometry, detect defects and optimize welding parameters in real time.",
        "devin_body": r'''## When to use

You are automating welding quality assurance, predicting penetration or bead geometry from sensor data, detecting weld defects in real time, or optimizing process parameters for arc, laser, or resistance welding.

## Usage

- **Monitor in-process**: collect arc sound, images, spectroscopy, and electrical signals.
- **Predict penetration**: estimate bead geometry and fusion from sensor data.
- **Detect defects**: identify porosity, burn-through, lack of fusion, and cracks.
- **Optimize parameters**: recommend voltage, current, speed, and shielding gas.
- **Support robotics**: close the loop for automated or cobot welding cells.

## Steps

1. Mount sensors for weld pool imaging, arc sound, current/voltage, and optical emission.
2. Capture bead geometry and cross-section ground truth for training.
3. Train multi-modal fusion models for penetration and defect detection.
4. Optimize welding parameters using the model and validate on coupons.
5. Deploy inference on a welding cell and adjust parameters in real time.
6. Validate weld quality with radiography, ultrasound, or mechanical testing.

## Code pattern

```python
import cv2
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Predict bead width from melt-pool geometric features
X = df[["pool_length_px", "pool_width_px", "pool_area_px2", "wire_feed_speed_m_min", "voltage_V"]]
y = df["bead_width_mm"]
model = RandomForestRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Welding images are noisy due to arc radiation and spatter; use narrow-band filtering or high dynamic range capture.
- Penetration labels are hard to obtain; use X-ray ground truth and rare-event metrics.
- Real-time inference requires lightweight models or edge deployment.
- Transfer across materials, joints, and shielding gases needs domain adaptation.

## Verification

1. Detect weld defects on a labeled radiography or visual dataset and report F1 per class.
2. Predict penetration state from front-side sensors and compare to cross-section measurements.
3. Optimize welding parameters for a target bead profile and validate with macrographs.
''',
        "references": [
            "https://doi.org/10.1016/j.aei.2025.103318",
            "https://doi.org/10.1007/s10845-025-02734-x",
            "https://doi.org/10.1007/s44196-026-01197-z",
            "https://doi.org/10.2351/7.0002067",
            "https://www.nature.com/articles/s41598-025-06324-y",
        ],
    },
    {
        "name": "ai-for-surface-engineering",
        "title": "AI for Surface Engineering",
        "description": "Use machine learning to optimize surface treatments such as thermal spray, laser cladding and shot peening while predicting residual stress and coating adhesion as well as wear resistance.",
        "devin_body": r'''## When to use

You are modifying a component's surface to improve wear, fatigue, or corrosion resistance, and need to optimize thermal spray, laser surface treatment, peening, or surface texturing parameters and predict surface integrity.

## Usage

- **Predict residual stress**: model peening, cladding, and thermal spray stress fields.
- **Optimize spray parameters**: tune gas flow, standoff, and powder feed for coating quality.
- **Select processes**: match surface treatments to wear, corrosion, and fatigue requirements.
- **Detect defects**: identify porosity, delamination, and cracks in coatings.
- **Build process-property maps**: link parameters to hardness, adhesion, and microstructure.

## Steps

1. Collect process parameters and post-treatment measurements for the surface process.
2. Train surrogate models to predict residual stress, coating thickness, and properties.
3. Use the models to optimize parameters and reduce DOE cost.
4. Validate predicted residual stress and microstructure with XRD, microscopy, or mechanical tests.
5. Inspect coatings for porosity, adhesion, and defects and feed results back.
6. Deploy optimized recipes and monitor for process drift.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict residual stress from peening or spray parameters
X = df[["laser_power_W", "spot_size_mm", "pulse_duration_ns", "overlap_pct", "material_yield_MPa"]]
y = df["surface_residual_stress_MPa"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Surface engineering datasets are small and expensive; use Gaussian processes or physics-informed models.
- Process parameters couple strongly with material and powder/particle properties.
- Residual stress and roughness depend on measurement method and location; standardize them.
- Validate microstructure and mechanical performance with cross-sectional microscopy and fatigue tests.

## Verification

1. Predict coating thickness or porosity from spray parameters and compare to SEM analysis.
2. Optimize shot peening parameters to reach a target residual stress profile.
3. Predict surface roughness after laser texturing and compare to profilometry.
''',
        "references": [
            "https://doi.org/10.1007/s44251-025-00113-5",
            "https://doi.org/10.1007/s11666-026-02258-7",
            "https://doi.org/10.1088/2053-1591/ad1a7f",
            "https://www.mdpi.com/2076-3417/11/7/2888",
            "https://doi.org/10.1007/s00339-026-09601-3",
        ],
    },
    {
        "name": "ai-for-coatings",
        "title": "AI for Coatings",
        "description": "Use machine learning to design formulations, predict thickness, optimize deposition and estimate corrosion protection and lifetime for functional coatings and films.",
        "devin_body": r'''## When to use

You are designing or applying protective and functional coatings and need to select formulations, predict coating properties and service life, optimize deposition parameters, or interpret electrochemical and exposure test data.

## Usage

- **Formulate coatings**: predict properties from ingredients and accelerate recipe design.
- **Control thickness**: model hot-dip, PVD, CVD, and spray coating thickness.
- **Predict lifetime**: estimate corrosion, UV, and wear degradation from environmental data.
- **Optimize curing**: tune temperature, time, and atmosphere for adhesion and hardness.
- **Inspect defects**: detect pinholes, runs, and color variations.

## Steps

1. Build a formulation database with ingredients, process parameters, and performance tests.
2. Train models to predict properties such as corrosion resistance, thickness, and adhesion.
3. Use the model to suggest new formulations and verify them in lab or field tests.
4. Optimize deposition or curing parameters with a surrogate model.
5. Validate lifetime predictions with accelerated aging and field exposure data.
6. Deploy the optimized coating process and track long-term performance.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Predict coating lifetime from formulation and exposure features
X = df[["pigment_vol_conc", "dry_film_thickness_um", "salt_spray_hours", "uv_exposure_h", "adhesion_MPa"]]
y = df["time_to_failure_h"]
model = RandomForestRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Coating data are sparse and formulation spaces are combinatorially large; use active learning.
- Include physicochemical descriptors and test standards for generalization.
- Lifetime data are right-censored; use survival models when failures are not all observed.
- Differentiate between application methods because film formation physics differs.

## Verification

1. Predict coating salt-spray life and compare to standardized exposure results.
2. Optimize deposition parameters for a target thickness and porosity.
3. Classify coating degradation stages from EIS or visual inspection.
''',
        "references": [
            "https://doi.org/10.1038/s41529-026-00771-2",
            "https://doi.org/10.1038/s41529-025-00709-0",
            "https://doi.org/10.1038/s41529-026-00760-5",
            "https://doi.org/10.1007/s00339-026-09565-4",
            "https://doi.org/10.3390/polym18010005",
        ],
    },
    {
        "name": "ai-for-corrosion-engineering",
        "title": "AI for Corrosion Engineering",
        "description": "Use AI to predict corrosion rates, monitor cathodic protection, optimize materials and coatings and extend asset life for pipelines and industrial infrastructure.",
        "devin_body": r'''## When to use

You are managing corrosion risk in infrastructure, pipelines, marine, automotive, or energy assets and need to predict corrosion rates, interpret electrochemical data, schedule inspections, select materials, or evaluate protection systems.

## Usage

- **Predict rates**: model corrosion from environment, material, coating, and operating data.
- **Monitor CP**: assess cathodic protection current, potential, and stray-current effects.
- **Estimate remaining life**: combine inspection, EIS, and thickness data.
- **Optimize materials**: select alloys, coatings, and inhibitors for the environment.
- **Plan inspections**: prioritize high-risk locations and extend in-line inspection intervals.

## Steps

1. Collect environmental, material, coating, and inspection data for the asset.
2. Train corrosion-rate or remaining-life models and validate against coupons or pull tests.
3. Integrate CP monitoring data and flag under- or over-protection conditions.
4. Map corrosion risk across the asset using a digital twin or knowledge graph.
5. Recommend materials, coatings, or inhibitors and simulate their effect.
6. Update the model with new inspections and optimize maintenance schedules.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict corrosion rate from environment and material features
X = df[["pH", "Cl_ppm", "temperature_C", "dissolved_O2_ppm", "alloy_Cr_pct"]]
y = df["corrosion_rate_mmpy"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Corrosion is highly environment- and time-dependent; include exposure duration and test standards.
- Data are often sparse and imbalanced; use transfer learning from similar environments.
- EIS spectra require careful preprocessing and equivalent-circuit assumptions.
- Combine physics-based electrochemical models with ML for extrapolation reliability.

## Verification

1. Predict corrosion rate for a given environment and compare to ASTM immersion or electrochemical tests.
2. Classify EIS spectra by equivalent circuit and validate against expert fitting.
3. Forecast remaining service life of a coating or component and compare to field pull data.
''',
        "references": [
            "https://doi.org/10.1002/maco.70127",
            "https://iopscience.iop.org/article/10.1149/1945-7111/aceab2",
            "https://www.nature.com/articles/s41598-025-18575-w",
            "https://doi.org/10.1007/s10791-026-10458-6",
            "https://doi.org/10.1038/s41529-022-00218-4",
        ],
    },
]