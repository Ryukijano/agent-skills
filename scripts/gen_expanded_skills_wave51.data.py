SKILLS = [
    {
        "name": "ai-for-additive-manufacturing",
        "title": "AI for Additive Manufacturing",
        "description": "Machine learning for powder-bed fusion, directed energy deposition, in-situ monitoring, defect detection, build simulation, and process parameter optimization in additive manufacturing.",
        "devin_body": r'''## When to use

You are optimizing metal or polymer additive manufacturing processes, predicting part quality from build parameters, detecting defects from in-situ sensor data, or training surrogate models for residual stress and distortion.

## Key concepts

- **Process parameter mapping**: laser power, scan speed, hatch spacing, layer thickness, and energy density windows.
- **In-situ sensing**: melt-pool images, photodiodes, thermal cameras, acoustic emission, and spatter monitoring.
- **Defect classification**: porosity, lack of fusion, balling, keyholing, and crack detection from image or time-series data.
- **Build planning**: support design, orientation, scan strategy, and thermal history effects on microstructure.
- **Digital twins and surrogate models**: fast prediction of distortion, residual stress, and mechanical properties.

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
        "description": "Machine learning for automated fiber placement, tape laying, resin infusion, cure monitoring, defect detection, and process optimization in composite part manufacturing.",
        "devin_body": r'''## When to use

You are manufacturing fiber-reinforced composite parts and need to detect layup defects, predict cure state, optimize AFP/ATL process parameters, or build digital twins for autoclave and resin-infusion processes.

## Key concepts

- **AFP/ATL defects**: tow gaps, overlaps, wrinkles, foreign objects, and fiber deviation from programmed paths.
- **Cure and consolidation**: temperature cycle, degree of cure, resin viscosity, exotherm, and void evolution.
- **Resin flow and permeability**: variability in preform architecture and flow-front monitoring for RTM/infusion.
- **Non-destructive evaluation**: ultrasonic, thermography, and laser profilometry for defect triangulation.
- **Multimodal process control**: fusing thermal, vision, and point-cloud data for real-time control.

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
        "description": "Machine learning for semiconductor fabrication yield enhancement, wafer defect detection, equipment fault classification, process control, and advanced lithography/etch modeling.",
        "devin_body": r'''## When to use

You are working with wafer fabrication data, trying to predict die yield, classify wafer or equipment faults, build virtual metrology models, or optimize lithography and etch processes.

## Key concepts

- **Yield and WAT prediction**: models that map equipment, process, and inline metrology data to final test yield.
- **Fault detection and classification (FDC)**: anomaly detection on tool trace data for chamber drift or misprocess.
- **Virtual metrology**: inferring wafer properties from process data when inline measurement is sparse.
- **Lithography and etch**: hotspot detection, overlay correction, critical dimension prediction, and endpoint control.
- **Run-to-run control**: adaptive adjustment of recipe parameters using feedback from measured outputs.

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
        "description": "Machine learning for nanoscale fabrication, roll-to-roll processing, nanoimprint lithography, self-assembly, nanoscale metrology, and process control.",
        "devin_body": r'''## When to use

You are developing scalable nanomanufacturing processes such as roll-to-roll nanoimprint, directed self-assembly, or top-down patterning, and need to model process–structure relationships, optimize throughput, or detect nanoscale defects.

## Key concepts

- **Top-down and bottom-up processes**: nanoimprint, photolithography, electron-beam patterning, self-assembly, and atomic layer deposition.
- **Roll-to-roll control**: web tension, speed, registration, coating uniformity, and defect propagation.
- **Nanoscale metrology**: SEM, AFM, scatterometry, and optical scatter for pattern quality.
- **Defect and yield modeling**: classification of bridging, missing features, line-edge roughness, and particles.
- **Multimodal data fusion**: combining in-line optical, electrical, and dimensional measurements.

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
            "https://par.nsf.gov/biblio/10642916",
        ],
    },
    {
        "name": "ai-for-textile-manufacturing",
        "title": "AI for Textile Manufacturing",
        "description": "Machine learning for yarn, fabric, and garment manufacturing: spinning, weaving, knitting, dyeing, finishing, quality inspection, and production optimization.",
        "devin_body": r'''## When to use

You are automating textile production lines, detecting fabric defects, predicting dye recipes, optimizing loom parameters, or monitoring the quality of spinning, weaving, and finishing processes.

## Key concepts

- **Fabric defect detection**: holes, stains, weft and warp breaks, pattern misalignments, and foreign fibers.
- **Yarn and spinning quality**: count, strength, evenness, hairiness, and breakage prediction.
- **Dyeing and finishing**: color prediction, dye recipe recommendation, K/S value, exhaustion rate, and shade matching.
- **Process monitoring**: loom stoppages, tension, machine vibration, and predictive maintenance.
- **Sustainability**: waste reduction, water/energy optimization, and recycled fiber traceability.

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
        "description": "Machine learning for extrusion, injection molding, blow molding, compounding, mixing, and polymer recycling process optimization and quality control.",
        "devin_body": r'''## When to use

You are running polymer processing equipment and need to set initial operating points, predict part quality, monitor melt quality, detect process instabilities, or optimize energy and material use in extrusion, injection, or blow molding.

## Key concepts

- **Injection molding**: plasticizing, filling, packing, cooling, shrinkage, warpage, and cycle time.
- **Extrusion and compounding**: screw geometry, throughput, melt temperature, mixing, and residence time.
- **Process signatures**: pressure, temperature, torque, and inline rheometry or NIR spectra.
- **Quality prediction**: dimensional accuracy, sink marks, flash, short shots, and mechanical properties.
- **Recycling and variability**: handling post-consumer, post-industrial, and mixed feedstocks.

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
        "description": "Machine learning for sheet-metal stamping, deep drawing, forging, rolling, extrusion, springback prediction, die design, and forming-limit prediction.",
        "devin_body": r'''## When to use

You are designing or troubleshooting sheet-metal, forging, or extrusion processes and need to predict springback, wrinkling, or tearing, optimize blank geometry, select forming parameters, or build fast surrogate models from finite element analysis.

## Key concepts

- **Springback and distortion**: elastic recovery after forming, influenced by material, friction, and tooling.
- **Forming limits**: necking, wrinkling, and fracture in stamping and deep drawing.
- **Process parameters**: blank holder force, die radius, drawbead geometry, punch speed, and lubrication.
- **FEA surrogates**: graph and image-based models that replace expensive nonlinear simulations.
- **Blank shape optimization**: inverse design to minimize material use and trimming.

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
        "description": "Machine learning for sand, investment, die, and continuous casting: defect prediction, mold filling, solidification, microstructure, and process optimization.",
        "devin_body": r'''## When to use

You are producing cast metal components and need to predict porosity, hot tearing, or shrinkage, optimize gating and risering, build digital twins of solidification, or improve energy and material efficiency in foundries.

## Key concepts

- **Casting defects**: porosity, shrinkage, hot tearing, cold shuts, inclusions, and surface defects.
- **Solidification modeling**: thermal history, dendrite arm spacing, phase fraction, and microstructure.
- **Process parameters**: pouring temperature, mold temperature, pouring rate, cooling rate, and alloy composition.
- **ICME and digital twins**: coupling thermodynamic, macro/micro-scale simulation with data-driven models.
- **High-pressure and continuous casting**: cycle time, die wear, and real-time quality control.

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
        "description": "Machine learning for arc, laser, and resistance welding: penetration prediction, defect detection, bead geometry, process monitoring, and parameter optimization.",
        "devin_body": r'''## When to use

You are automating welding quality assurance, predicting penetration or bead geometry from sensor data, detecting weld defects in real time, or optimizing process parameters for arc, laser, or resistance welding.

## Key concepts

- **Melt-pool and arc sensing**: high-speed cameras, photodiodes, acoustic emission, and spectral emissions.
- **Penetration and geometry prediction**: keyhole state, fusion width, bead width, and reinforcement.
- **Defect detection**: porosity, lack of fusion, spatter, undercut, burn-through, and cracks.
- **Multimodal fusion**: combining visual, acoustic, and electrical signals for robust monitoring.
- **Seam tracking and robot welding**: path planning, torch orientation, and adaptive control.

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
        "description": "Machine learning for surface modification processes: thermal spray, laser cladding/peening, shot peening, plasma electrolytic oxidation, surface texturing, and residual stress optimization.",
        "devin_body": r'''## When to use

You are modifying a component's surface to improve wear, fatigue, or corrosion resistance, and need to optimize thermal spray, laser surface treatment, peening, or surface texturing parameters and predict surface integrity.

## Key concepts

- **Thermal spraying**: HVOF, HVAF, plasma spray, cold spray, and coating microstructure/property prediction.
- **Laser surface treatments**: laser cladding, shock peening, texturing, and surface alloying.
- **Mechanical surface enhancement**: shot peening, laser peening, and deep rolling for residual stress.
- **Surface integrity metrics**: roughness, hardness, residual stress, coating thickness, and adhesion.
- **Functional surfaces**: texture, wettability, friction, and fatigue life optimization.

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
        "description": "Machine learning for coating formulation, deposition, thickness, microstructure, adhesion, corrosion protection, and service-life prediction.",
        "devin_body": r'''## When to use

You are designing or applying protective and functional coatings and need to select formulations, predict coating properties and service life, optimize deposition parameters, or interpret electrochemical and exposure test data.

## Key concepts

- **Formulation design**: pigment, binder, solvent, additive selection, and multi-objective optimization.
- **Deposition and process control**: PVD, CVD, thermal spray, dip, spin, and roll-to-roll coating.
- **Coating properties**: thickness, porosity, hardness, adhesion, and barrier performance.
- **Corrosion and degradation**: salt spray, cyclic testing, electrochemical impedance, and lifetime prediction.
- **Functional coatings**: self-healing, anti-fouling, thermal barrier, and optical coatings.

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
        "description": "Machine learning for corrosion rate prediction, risk-based inspection, cathodic protection, coating lifetime, EIS interpretation, and materials selection.",
        "devin_body": r'''## When to use

You are managing corrosion risk in infrastructure, pipelines, marine, automotive, or energy assets and need to predict corrosion rates, interpret electrochemical data, schedule inspections, select materials, or evaluate protection systems.

## Key concepts

- **Corrosion informatics**: data-driven prediction of corrosion rate and form from environment and material data.
- **Electrochemical sensing**: EIS, polarization, Tafel, and open-circuit potential interpretation.
- **Coating and inhibitor lifetime**: barrier breakdown, water uptake, and inhibitor release prediction.
- **Risk-based inspection**: prioritizing assets using degradation forecasts and consequence analysis.
- **Cathodic protection**: optimizing anode layout and current density with data-driven models.

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
