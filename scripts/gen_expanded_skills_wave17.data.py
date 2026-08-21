SKILLS = [
    {
        "name": "ai-for-materials-characterization",
        "title": "AI for Materials Characterization",
        "description": "Segment and quantify concrete and cement microstructure from X-ray and confocal microscopy to assess freeze-thaw durability.",
        "devin_body": r'''
## When to use

You need to extract quantitative structure-property insights from microscopy images, spectra, diffraction patterns, or hyperspectral characterization data at scale.

## Usage

- Segment microstructures and detect defects in SEM, TEM, EBSD, and AFM images.
- Automate phase identification, peak fitting, and composition inference from XRD, XPS, EDS, and spectroscopy data.
- Reconstruct, denoise, and compress 4D-STEM and electron tomography datasets.
- Fuse imaging, spectroscopy, and simulation data to predict material properties in self-driving laboratories.

## Steps

1. Ingest microscopy images, spectra, diffraction patterns, or 4D-STEM/tomography data for the target material.
2. Preprocess data (denoise, normalize, align, calibrate) and annotate a representative set with expert labels.
3. Train a segmentation, classification, or regression model for the target task (defects, phases, peaks, composition).
4. Validate with held-out data, comparing IoU, accuracy, or error to expert annotations and reference simulations.
5. Apply the model in a high-throughput or self-driving lab loop to guide further experiments.
6. Use interpretability tools (Grad-CAM, SHAP) to connect predictions back to physical microstructural features.

## Code pattern

```python
import torch
from torchvision.models.segmentation import fcn_resnet50

model = fcn_resnet50(pretrained=False, num_classes=4)
model.load_state_dict(torch.load("microstructure_seg.pth"))
output = model(img_tensor)["out"]
```

## Tuning notes

- Annotation quality and label consistency matter more than model size; use active learning to build labels efficiently.
- Watch for domain shift between instruments, sample batches, and imaging conditions.
- Interpretability tools (Grad-CAM, SHAP) help connect model predictions back to physical microstructural features.

## Verification

1. Train a microstructure segmentation model and compare IoU to expert annotations.
2. Run an XRD phase-identification classifier on a held-out powder dataset.
3. Denoise or reconstruct a 4D-STEM dataset and validate against a conventional slow acquisition.
''',
        "references": [
            "https://doi.org/10.1186/s42252-025-00073-x",
            "https://doi.org/10.1007/s11837-021-04805-9",
            "https://pubs.rsc.org/en/content/articlelanding/2022/nh/d2nh00377e",
            "https://doi.org/10.1116/6.0002809",
            "https://doi.org/10.31695/ijasre.2025.11.3",
        ],
    },
    {
        "name": "ai-for-ceramics",
        "title": "AI for Ceramics",
        "description": "Use data-driven models to design ceramics, optimize sintering and additive processes, and predict microstructure-property relationships.",
        "devin_body": r'''
## When to use

You are designing or processing functional, structural, or refractory ceramics and want to predict phase stability, sintering behavior, or mechanical/dielectric properties from composition and process parameters.

## Usage

- Design piezoelectric, dielectric, thermal-barrier, and structural ceramics from composition descriptors.
- Predict and optimize sintering densification, grain growth, and shrinkage with process parameters.
- Optimize additive manufacturing parameters (direct ink writing, binder jetting) and detect defects.
- Map microstructure to mechanical/dielectric properties using image analysis and multi-fidelity models.

## Steps

1. Collect composition, processing (temperature, time, atmosphere), microstructure, and property data.
2. Encode composition with element fractions or thermodynamic descriptors and split data by chemistry/process.
3. Train models to predict phase stability, sintering behavior, or properties from composition and process inputs.
4. Use Bayesian optimization or active learning to optimize firing profiles and additive-manufacturing settings.
5. Segment microstructure images and correlate features with measured properties.
6. Validate the best recipes with new synthesis runs and compare to CALPHAD/DFT or experimental baselines.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

df = pd.read_csv("ceramic_process_data.csv")  # composition + firing + properties
X = df[["Al2O3", "SiO2", "sinter_temp", "dwell_hr"]]
y = df["fracture_toughness"]
model = GradientBoostingRegressor().fit(X, y)
```

## Tuning notes

- Datasets are often small and experimentally noisy; use ensemble methods, Gaussian processes, or active learning.
- Encode composition as element fractions or use descriptors such as ionic radii and electronegativity.
- Validate predictions with new synthesis runs rather than relying solely on cross-validation.

## Verification

1. Predict fracture toughness or dielectric constant from composition and sintering conditions.
2. Optimize a sintering profile using Bayesian optimization and compare to baseline processing.
3. Segment ceramic micrographs and correlate microstructural features with measured properties.
''',
        "references": [
            "https://doi.org/10.1111/ijac.70195",
            "https://doi.org/10.1016/j.jeurceramsoc.2026.118426",
            "https://osf.io/d8bk9",
            "https://doi.org/10.1038/s41598-025-12011-9",
        ],
    },
    {
        "name": "ai-for-polymers",
        "title": "AI for Polymers",
        "description": "Use ML to predict polymer properties, generate novel structures, and optimize process-structure-property relationships for sustainable materials.",
        "devin_body": r'''
## When to use

You are discovering or optimizing polymeric materials for mechanical, thermal, electronic, or sustainable applications and need to navigate the vast polymer chemical and morphological space.

## Usage

- Represent polymers with SMILES, BigSMILES, fingerprints, graph neural networks, or polyBERT-style embeddings.
- Predict glass transition, viscosity, modulus, permeability, and degradation from structure.
- Generate novel polymer structures with VAEs, GANs, diffusion models, or reinforcement learning.
- Link synthesis, molecular weight, and morphology to performance for sustainable and recyclable design.

## Steps

1. Curate polymer structures and property data, choosing repeat-unit, oligomer, or bulk representations as appropriate.
2. Train property-prediction models for target properties (Tg, modulus, permeability, bandgap) with transfer learning.
3. Generate candidate polymers using a generative model and filter for synthetic accessibility and target property windows.
4. Incorporate process, molecular weight, crystallinity, and polydispersity descriptors into structure-property models.
5. Evaluate candidates for biodegradability, recyclability, or circularity with sustainability scoring.
6. Validate top candidates by synthesis and measurement, and retrain the models with new data.

## Code pattern

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("kuelumbus/polyBERT")
model = AutoModel.from_pretrained("kuelumbus/polyBERT")
inputs = tokenizer("[*]CC(C)C[*]", return_tensors="pt")
emb = model(**inputs).pooler_output
```

## Tuning notes

- Polymer data are sparse and highly heterogeneous; use transfer learning and multitask models where possible.
- Distinguish between repeat-unit, oligomer, and bulk-property predictions; the same SMILES can map to very different materials.
- Pay attention to polydispersity, crystallinity, and processing history when building descriptors.

## Verification

1. Train a polymer Tg or bandgap predictor and evaluate on a held-out test set.
2. Generate novel polymer candidates with a VAE and filter for synthesizability.
3. Predict rheological or permeability behavior and compare to experimental measurements.
''',
        "references": [
            "https://doi.org/10.1002/masy.202400185",
            "https://www.mdpi.com/2073-4360/17/12/1667",
            "https://pubs.acs.org/doi/abs/10.1021/accountsmr.3c00288",
            "https://doi.org/10.66640/ujp-2026-5-00001",
        ],
    },
    {
        "name": "ai-for-metals",
        "title": "AI for Metals and Alloys",
        "description": "Use ML to design alloys, predict phase stability and properties, quantify microstructure, and optimize metal processing and additive manufacturing.",
        "devin_body": r'''
## When to use

You are designing new alloys or optimizing metal processing and need to predict phase stability, mechanical behavior, corrosion resistance, or manufacturability from composition and processing history.

## Usage

- Predict composition-process-microstructure-property relationships for steels, aluminum, titanium, magnesium, and HEAs.
- Combine CALPHAD thermodynamics with ML for phase stability and transformation kinetics.
- Quantify microstructure (grain size, texture, precipitates, phase fractions) from EBSD/SEM images.
- Optimize additive manufacturing, heat treatment, and processing parameters for target properties.

## Steps

1. Collect composition, processing, microstructure, and property data for the alloy class of interest.
2. Encode composition with physically meaningful descriptors and train models for target properties or phase stability.
3. Segment and quantify microstructure images to extract grain, precipitate, and texture features.
4. Run CALPHAD-ML hybrids or phase-stability classifiers and validate against DFT or experiments.
5. Optimize processing (heat treatment, AM parameters, rolling) with Bayesian or active-learning methods.
6. Validate the best candidates with mechanical, corrosion, or creep tests and compare to known alloy baselines.

## Code pattern

```python
import matminer
from sklearn.ensemble import RandomForestRegressor

featurizer = matminer.featurizers.composition.ElementProperty.from_preset("magpie")
X = df["composition"].apply(featurizer.featurize)
y = df["yield_strength_MPa"]
model = RandomForestRegressor().fit(list(X), y)
```

## Tuning notes

- Use physically meaningful descriptors (elemental, thermodynamic, structural) rather than raw composition alone.
- Train separate models for distinct alloy classes or microstructural regimes.
- Validate with tensile/creep/fatigue experiments, not just property databases.

## Verification

1. Predict a mechanical or phase-stability property for a multi-component alloy and compare to DFT or experiment.
2. Build a classifier for single-phase HEA formation and validate against known systems.
3. Segment metal micrographs and extract grain-size or precipitate statistics.
''',
        "references": [
            "https://doi.org/10.3390/alloys5010007",
            "https://www.sciencedirect.com/science/article/abs/pii/S0927796X23000323",
            "https://bsg.byu.edu/docs/papers/NRM_ML_for_Alloys.pdf",
            "https://doi.org/10.1007/s10853-025-11154-4",
        ],
    },
    {
        "name": "ai-for-semiconductors",
        "title": "AI for Semiconductors",
        "description": "Apply ML to discover semiconductors, engineer bandgaps and defects, and optimize fabrication and layout processes.",
        "devin_body": r'''
## When to use

You are searching for new semiconductor compounds, optimizing doping or growth, or building surrogate models for electronic-structure and fabrication parameters.

## Usage

- Predict bandgap, carrier properties, and effective mass from DFT and experimental data.
- Classify wafer defects, predict yield, and perform root-cause analysis.
- Optimize lithography, etch, deposition, and design-technology co-optimization with ML.
- Generate candidate 2D and wide-bandgap semiconductors with GNNs or LLMs and validate with DFT.

## Steps

1. Collect DFT, experimental, and fabrication data from public databases (Materials Project, AFLOW) or proprietary sources.
2. Train property-prediction models for bandgap, effective mass, and carrier properties, using crystal-graph or composition descriptors.
3. Build defect-classification and yield-prediction models from wafer images and process logs.
4. Use ML to optimize lithography, etch, deposition, or layout parameters and check against process constraints.
5. Generate novel semiconductor candidates with inverse-design models and validate the most promising with DFT.
6. Fabricate and measure top candidates, feeding results back to refine the models.

## Code pattern

```python
from megnet.models import MEGNetModel
from pymatgen.core import Composition

model = MEGNetModel.from_dir("bandgap_megnet_model/")
pred = model.predict_structure(Composition("GaAs").get_structure())
```

## Tuning notes

- Semiconductor data are often proprietary and sparse; leverage public DFT databases (Materials Project, AFLOW) and transfer learning.
- Distinguish between bulk, thin-film, and device-level properties; the same compound can behave very differently.
- Validate generative or inverse-design candidates with DFT and, where possible, epitaxy or transport measurements.

## Verification

1. Predict bandgap or effective mass for a set of compounds and compare to DFT values.
2. Train a wafer-defect classifier and evaluate precision-recall per defect type.
3. Propose and DFT-validate a new semiconductor candidate generated by an inverse-design model.
''',
        "references": [
            "https://doi.org/10.1016/j.compstruct.2025.119419",
            "https://www.annualreviews.org/content/journals/10.1146/annurev-matsci-080423-011746",
            "https://pubs.rsc.org/en/content/articlehtml/2026/dd/d5dd00544b",
            "https://doi.org/10.1051/itmconf/20257803007",
        ],
    },
    {
        "name": "ai-for-battery-materials",
        "title": "AI for Battery Materials",
        "description": "Use battery informatics, ML potentials, and closed-loop optimization to discover electrode/electrolyte materials and optimize lifetime and fast-charging protocols.",
        "devin_body": r'''
## When to use

You are developing or optimizing materials and operating conditions for Li-ion, solid-state, or beyond-Li-ion batteries.

## Usage

- Discover cathode, anode, electrolyte, and separator materials with high-throughput screening.
- Simulate ion diffusion and interfacial reactions with machine-learning potentials.
- Forecast capacity fade and resistance rise from cycling data.
- Optimize fast-charging protocols that balance charge time and cycle life.

## Steps

1. Curate structural, compositional, and electrochemical data for battery materials and cycling protocols.
2. Screen candidates for ionic conductivity, voltage, stability, and capacity using ML models.
3. Train ML potentials to run fast atomistic simulations of diffusion, interfacial reactions, and degradation.
4. Build a lifetime-degradation model from cycle data and validate on independent cells.
5. Use closed-loop or Bayesian optimization to design fast-charging protocols that minimize degradation.
6. Test top materials and protocols in real cells and update the models with new cycling data.

## Code pattern

```python
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("battery_cycles.csv")  # cycle, voltage, temperature, capacity
features = ["cycle_number", "charge_time", "avg_temp", "coulombic_efficiency"]
X = df[features]
y = df["capacity_fade"]
model = RandomForestRegressor().fit(X, y)
```

## Tuning notes

- Battery data are noisy, batch-dependent, and slow to collect; use transfer learning and domain adaptation across chemistries.
- Incorporate physics-based features (voltage profiles, dQ/dV peaks) for better generalization.
- Calibrate uncertainty and validate on independent cells, not just splits from the same batch.

## Verification

1. Predict voltage, ionic conductivity, or formation energy for a new electrolyte or cathode candidate.
2. Forecast cycle life using early-cycle data and compare to actual end-of-life capacity.
3. Optimize a fast-charging protocol and test it against a baseline on real cells.
''',
        "references": [
            "https://www.nature.com/articles/s41524-022-00713-x",
            "https://www.nature.com/articles/s41578-022-00490-5",
            "https://pubs.rsc.org/en/content/articlelanding/2023/ya/d3ya00040k",
            "https://www.sciencedirect.com/science/article/abs/pii/S240582972400686X",
            "https://link.springer.com/article/10.1007/s42979-024-03046-2",
        ],
    },
    {
        "name": "ai-for-superconductors",
        "title": "AI for Superconductors",
        "description": "Apply ML to discover superconductors, predict critical temperature and electron-phonon coupling, and screen candidates through DFT-integrated pipelines.",
        "devin_body": r'''
## When to use

You are searching for new superconducting compounds or trying to predict $T_c$, critical fields, or electron-phonon coupling from crystal and electronic structure.

## Usage

- Predict $T_c$ and electron-phonon properties from crystal structure and DFT descriptors.
- Screen large databases for electron-phonon coupling, stability, and synthesizability.
- Use equivariant graph neural networks that respect crystal symmetries for superconducting properties.
- Combine generative models, ML potentials, and DFT in an AI-accelerated discovery pipeline.

## Steps

1. Curate the SuperCon database or DFT-derived electron-phonon data and compute composition/structure descriptors.
2. Train a classifier or regression model to predict $T_c$ and rank candidates for further study.
3. Screen databases with ML filters for structural stability, electron-phonon coupling, and synthesizability.
4. Apply equivariant GNNs to refine predictions using crystal-symmetry-aware representations.
5. Use generative models and ML potentials to propose novel candidates and relax them with DFT.
6. Validate the most promising candidates experimentally and report both MAE and true-positive rates.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

# Crystal-structure and composition features -> Tc
X = np.array([df["n_electrons"], df["avg_mass"], df["density"]]).T
y = df["Tc_K"]
model = GradientBoostingRegressor().fit(X, y)
```

## Tuning notes

- Superconductivity is a rare property; handle extreme class imbalance with appropriate sampling and metrics.
- Use DFT-validated electron-phonon spectral functions as high-fidelity training targets when available.
- Report both true-negative rate and mean absolute error; high precision on positive candidates is essential.

## Verification

1. Predict $T_c$ on a held-out test set and report MAE versus DFT or experimental values.
2. Screen a large database for likely superconductors and validate top candidates with DFT.
3. Synthesize and measure a predicted candidate to confirm superconductivity.
''',
        "references": [
            "https://doi.org/10.1007/s10948-026-07175-y",
            "https://doi.org/10.1038/s43246-021-00209-z",
            "https://link.springer.com/article/10.1038/s41524-026-01964-8",
            "https://ieeexplore.ieee.org/document/11017078",
            "https://openreview.net/pdf/2214f145d116ef5e783cb2e9e3899ed4ab18cd00.pdf",
        ],
    },
    {
        "name": "ai-for-catalysis",
        "title": "AI for Catalysis",
        "description": "Use catalysis informatics and active learning to discover catalysts, predict activity/selectivity, explore reaction networks, and optimize processes.",
        "devin_body": r'''
## When to use

You are designing heterogeneous, homogeneous, or enzymatic catalysts and need to predict activity, selectivity, stability, or optimal reaction conditions from structure and data.

## Usage

- Screen catalysts with structured datasets, reaction descriptors, and ML models.
- Predict adsorption energies and scaling relations as inputs to microkinetic simulations.
- Explore reaction networks and elementary steps with ML-guided search.
- Optimize catalyst synthesis and reaction conditions with active learning and Bayesian optimization.

## Steps

1. Curate catalyst-adsorbate datasets, harmonizing units, structures, and reaction conditions.
2. Compute or collect adsorption-energy, surface, and adsorbate descriptors for the target reaction.
3. Train ML models to predict activity, selectivity, or binding energy and validate against DFT.
4. Build microkinetic models using ML-predicted rate constants and compare to measured conversion/selectivity.
5. Use active learning or Bayesian optimization to choose the next catalyst composition or reaction condition.
6. Synthesize and test the selected catalysts, then feed results back to refine the models.

## Code pattern

```python
import numpy as np
from sklearn.kernel_ridge import KernelRidge

# Surface and adsorbate descriptors -> adsorption energy
X = df[["d_band_center", "coordination", "adsorbate_fingerprint"]]
y = df["adsorption_energy_eV"]
model = KernelRidge(kernel="rbf").fit(X, y)
```

## Tuning notes

- Catalytic performance is highly sensitive to surface structure, support, and conditions; include adsorption-site and environmental features.
- Reaction data are often scattered across literature; harmonize units, substrates, and catalyst loadings.
- Pair ML models with microkinetic simulations to interpret predictions mechanistically.

## Verification

1. Predict adsorption or activation energies for a set of catalyst-adsorbate pairs and compare to DFT.
2. Optimize a catalyst composition or reaction condition using Bayesian optimization and validate experimentally.
3. Reproduce a microkinetic model from ML-predicted rate constants and compare to measured conversion/selectivity.
''',
        "references": [
            "https://www.nature.com/articles/s41929-024-01150-3",
            "https://pubs.acs.org/doi/full/10.1021/acscatal.9b04186",
            "https://www.sciencedirect.com/science/article/pii/S2667325823003485",
            "https://www.nature.com/articles/s41929-022-00896-y",
            "https://pubs.rsc.org/en/content/articlelanding/2025/cc/d5cc05274b",
        ],
    },
    {
        "name": "ai-for-photovoltaics",
        "title": "AI for Photovoltaics",
        "description": "Use ML and high-throughput experimentation to discover solar-cell absorbers, optimize perovskite and organic PV, and predict device performance and stability.",
        "devin_body": r'''
## When to use

You are exploring new absorbers, interfaces, or processing conditions for perovskite, organic, silicon, or tandem solar cells.

## Usage

- Screen absorbers for bandgap, carrier mobility, defect tolerance, and toxicity.
- Optimize perovskite composition and processing with high-throughput experiments and robotic synthesis.
- Predict molecular and device properties for organic photovoltaics and non-fullerene acceptors.
- Forecast stability and degradation under light, heat, and humidity for candidate cells.

## Steps

1. Define target application (single-junction, tandem, flexible) and collect material and device datasets.
2. Train models to predict bandgap, carrier mobility, absorption, and defect tolerance for absorber candidates.
3. Run high-throughput or robotic experiments to synthesize and characterize perovskite/organic films.
4. Build a device-performance model that couples material descriptors to measured PCE, FF, and VOC.
5. Forecast stability under accelerated aging and identify degradation mechanisms.
6. Validate top candidates with real devices and iterate the model with new experimental results.

## Code pattern

```python
from rdkit import Chem
from rdkit.Chem import Descriptors

mol = Chem.MolFromSmiles("c1cc2c(s1)c1ccccc1C2=O")
homo_lumo = Descriptors.MolMR(mol)  # example descriptor placeholder
print(homo_lumo)
```

## Tuning notes

- PV datasets are often small and high-dimensional; use transfer learning and physics-informed descriptors (bandgap, dielectric constant, ion migration).
- Distinguish between molecular and device-level predictions; device performance depends strongly on morphology and processing.
- Stability is as important as efficiency; include degradation and hysteresis features in models.

## Verification

1. Predict power-conversion efficiency or bandgap for a set of PV absorbers and compare to experimental cells.
2. Optimize a perovskite composition or annealing protocol using an autonomous or ML-guided lab loop.
3. Forecast degradation under accelerated aging and compare to ground-truth stability measurements.
''',
        "references": [
            "https://pubs.rsc.org/en/content/articlehtml/2025/el/d5el00041f",
            "https://doi.org/10.1002/aenm.202506803",
            "https://www.sciencedirect.com/science/article/abs/pii/S0925838823021278",
            "https://www.sciencedirect.com/science/article/abs/pii/S209549562400161X",
            "https://pubs.rsc.org/en/content/articlehtml/2024/ta/d4ta01942c",
        ],
    },
    {
        "name": "ai-for-composites",
        "title": "AI for Composites",
        "description": "Apply ML to design composites, optimize manufacturing, detect defects, and predict multiscale mechanical and thermal properties.",
        "devin_body": r'''
## When to use

You are engineering fiber-reinforced, polymer-matrix, metal-matrix, or ceramic-matrix composites and need to predict or optimize mechanical, thermal, or processing behavior.

## Usage

- Link microstructure features (fiber orientation, volume fraction, voids) to stiffness, strength, and toughness.
- Detect delaminations, voids, and fiber waviness from ultrasonic, X-ray, and thermography data.
- Optimize resin infusion, automated fiber placement, curing, and consolidation parameters.
- Build multiscale surrogates and inverse-design tools for tailored anisotropic composite properties.

## Steps

1. Collect composite microstructure images, NDE data, manufacturing parameters, and mechanical/thermal test results.
2. Extract microstructural features and train models to predict stiffness, strength, toughness, or thermal conductivity.
3. Train defect-detection classifiers/segmenters on NDE images and validate against destructive inspection.
4. Optimize manufacturing parameters (temperature, pressure, feed rate) using Bayesian or physics-informed methods.
5. Build multiscale or FE surrogates and use them for rapid design-space exploration.
6. Validate predicted properties and process settings with mechanical tests and quality inspections.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("composites.csv")  # fiber, matrix, vf, void, process
X = df[["fiber_volume_fraction", "void_fraction", "cure_temp_C"]]
y = df["tensile_strength_MPa"]
model = RandomForestRegressor().fit(X, y)
```

## Tuning notes

- Composite data are highly process-dependent; include manufacturing parameters, not just composition.
- Anisotropy and damage evolution require direction-specific features and possibly recurrent or graph models.
- Use non-destructive evaluation data to augment sparse mechanical test datasets.

## Verification

1. Predict a mechanical property (tensile/flexural/modulus) and validate against a test standard.
2. Detect defects in composite NDE images and compare to ground-truth destructive inspection.
3. Optimize an automated fiber placement or curing process and measure the resulting part quality.
''',
        "references": [
            "https://link.springer.com/article/10.1007/s10443-025-10415-4",
            "https://doi.org/10.1002/pc.71029",
            "https://doi.org/10.1016/j.compositesb.2026.113658",
            "https://pubs.rsc.org/en/content/articlelanding/2025/ta/d5ta00982k",
            "https://accscience.com/journal/IJAMD/2/3/10.36922/IJAMD025210016",
        ],
    },
    {
        "name": "ai-for-membranes",
        "title": "AI for Membranes",
        "description": "Design polymer membranes for gas and carbon-capture separations using graph ML to surpass selectivity-permeability upper bounds.",
        "devin_body": r'''
## When to use

You are designing polymeric, ceramic, or 2D membranes for gas separation, water treatment, fuel cells, or energy applications.

## Usage

- Predict membrane permeability, selectivity, fouling resistance, and stability from chemical structure.
- Screen polymeric and 2D materials for gas, ion, or water-selective membranes.
- Model fouling, flux decline, and cleaning cycles from process data.
- Generate polymer repeat units or pore structures for target separation performance.

## Steps

1. Collect membrane chemical structures and measured performance data under relevant conditions.
2. Represent polymers and 2D materials with repeat units, fragments, and topological descriptors.
3. Train regression models for permeability/selectivity, applying log-transforms for wide-ranging targets.
4. Use explainable AI to identify structural drivers of free volume, pore size, and solubility.
5. Run virtual screening or inverse design to propose candidates and validate top performers with synthesis.
6. Model fouling and flux decline from process data and optimize cleaning and operating schedules.

## Code pattern

```python
from rdkit import Chem
from sklearn.ensemble import GradientBoostingRegressor

mol = Chem.MolFromSmiles("C1CCOC1")  # example repeat unit
X = [[mol.GetNumHeavyAtoms(), Descriptors.MolWt(mol), Descriptors.TPSA(mol)]]
y = [ permeability_value ]
model = GradientBoostingRegressor().fit(X, y)
```

## Tuning notes

- Use appropriate representations for polymers (repeat units, fragments, topological descriptors) rather than monomer SMILES alone.
- Permeability and selectivity often span many orders of magnitude; log-transform targets before regression.
- Include operational conditions (temperature, pressure, feed composition) for deployment-relevant models.

## Verification

1. Predict gas permeability or water flux for a membrane polymer and compare to experimental data.
2. Identify top candidates from a virtual screen and validate one with synthesis and permeation testing.
3. Model fouling rate under realistic feed conditions and compare to pilot-plant observations.
''',
        "references": [
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC10941251/",
            "https://www.mdpi.com/2077-0375/15/12/353",
            "https://pureadmin.qub.ac.uk/ws/portalfiles/portal/556052977/Machine_learning_for_membrane.pdf",
            "https://doi.org/10.1063/5.0205433",
            "https://europepmc.org/article/med/39680111",
        ],
    },
    {
        "name": "ai-for-corrosion",
        "title": "AI for Corrosion",
        "description": "Use corrosion informatics and ML to predict rates, design alloys and coatings, analyze electrochemical data, and monitor infrastructure degradation.",
        "devin_body": r'''
## When to use

You need to predict corrosion rates, identify corrosion-resistant materials, or monitor degradation in pipelines, structures, coatings, or batteries.

## Usage

- Predict corrosion rates and forms (pitting, galvanic, SCC) from material and environment data.
- Design corrosion-resistant alloys and coatings with ML-guided composition optimization.
- Interpret electrochemical data (EIS, polarization, Tafel) with automated models.
- Monitor infrastructure and coating degradation from time-series sensors and drone imagery.

## Steps

1. Collect corrosion data (material composition, environment, exposure time, test standards, images).
2. Train regression or classification models to predict corrosion rate and form from environment and material features.
3. Use ML to interpret EIS and polarization curves and extract Tafel parameters automatically.
4. Design coatings or alloy compositions with Bayesian optimization and validate with ASTM or electrochemical tests.
5. Deploy time-series anomaly detection on sensor data from pipelines, bridges, or offshore assets.
6. Detect rust and coating defects from drone or inspection images and integrate findings into a maintenance dashboard.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("corrosion_data.csv")  # alloy, environment, exposure
X = df[["pH", "Cl_ppm", "temperature_C", "alloy_Cr"]]
y = df["corrosion_rate_mmpy"]
model = RandomForestRegressor().fit(X, y)
```

## Tuning notes

- Corrosion is highly dependent on environment, time, and surface state; include exposure history and test standards.
- Corrosion data are heterogeneous and often proprietary; build shared, standardized datasets where possible.
- Combine physics-based corrosion models (e.g., electrochemical kinetics) with ML for extrapolation reliability.

## Verification

1. Predict corrosion rate in a given environment and compare to an ASTM immersion or electrochemical test.
2. Detect corrosion or coating defects in images and compare to expert-labeled ground truth.
3. Build a sensor-based degradation model and validate remaining-life predictions against field data.
''',
        "references": [
            "https://www.nature.com/articles/s41529-022-00218-4",
            "https://www.degruyterbrill.com/document/doi/10.1515/corrrev-2022-0089/html",
            "https://doi.org/10.1016/j.nxmate.2026.102484",
            "https://doi.org/10.54660/.jfmr.2023.4.1.362-380",
        ],
    },
]
