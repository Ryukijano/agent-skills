SKILLS = [
    {
        "name": "ai-for-materials-characterization",
        "title": "AI for Materials Characterization",
        "description": "Machine learning for automated interpretation of microscopy, spectroscopy, diffraction, and tomography data in materials science.",
        "devin_body": r'''
## When to use

You need to extract quantitative structure-property insights from microscopy images, spectra, diffraction patterns, or hyperspectral characterization data at scale.

## Key concepts

- **Image-driven microstructure analysis**: semantic segmentation, defect detection, and phase identification in SEM/TEM/EBSD images.
- **Spectroscopy and diffraction ML**: automated peak fitting, phase identification from XRD, and composition inference from XPS/EDS.
- **4D-STEM and electron tomography**: ML reconstruction, denoising, and compressed sensing for high-dimensional data.
- **Multimodal data fusion**: combine imaging, spectroscopy, and simulation for robust property predictions.
- **Self-driving laboratories**: closed-loop control of characterization instruments guided by real-time inference.

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
            "https://par.nsf.gov/biblio/10621556-materials-characterization-can-artificial-intelligence-used-address-reproducibility-challenges",
            "https://doi.org/10.31695/ijasre.2025.11.3",
        ],
    },
    {
        "name": "ai-for-ceramics",
        "title": "AI for Ceramics",
        "description": "Data-driven design, processing optimization, and microstructure-property prediction for ceramic and refractory materials.",
        "devin_body": r'''
## When to use

You are designing or processing functional, structural, or refractory ceramics and want to predict phase stability, sintering behavior, or mechanical/dielectric properties from composition and process parameters.

## Key concepts

- **High-entropy and functional ceramics**: composition design for piezoelectric, dielectric, thermal-barrier, and structural ceramics.
- **Sintering and process optimization**: ML models for densification, grain growth, and shrinkage as a function of time, temperature, and atmosphere.
- **Additive manufacturing of ceramics**: direct ink writing and binder jetting parameter optimization, defect detection, and print-path planning.
- **Microstructure-property mapping**: computer-vision analysis of ceramic micrographs and property prediction.
- **Digital twins and physics-informed ML**: integrate CALPHAD/DFT with data-driven models for constrained optimization.

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
            "https://ijsrmt.com/index.php/ijsrmt/article/view/1033",
        ],
    },
    {
        "name": "ai-for-polymers",
        "title": "AI for Polymers",
        "description": "Machine learning for polymer property prediction, generative design, process optimization, and structure representation.",
        "devin_body": r'''
## When to use

You are discovering or optimizing polymeric materials for mechanical, thermal, electronic, or sustainable applications and need to navigate the vast polymer chemical and morphological space.

## Key concepts

- **Polymer representations**: SMILES, BigSMILES, fingerprints, graph neural networks, and polyBERT-style sequence embeddings.
- **Property prediction**: glass transition, viscosity, modulus, permeability, and degradation from structure.
- **Generative and inverse design**: VAEs, GANs, diffusion models, and reinforcement learning for novel polymer structures.
- **Process-structure-property relationships**: linking synthesis conditions, molecular weight, and morphology to performance.
- **Sustainable and recyclable polymers**: ML-guided biodegradability, upcycling, and circular material design.

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
        "description": "Machine learning for alloy design, phase stability, mechanical properties, process optimization, and microstructure-property mapping.",
        "devin_body": r'''
## When to use

You are designing new alloys or optimizing metal processing and need to predict phase stability, mechanical behavior, corrosion resistance, or manufacturability from composition and processing history.

## Key concepts

- **Alloy design and property prediction**: composition-process-microstructure-property models for steels, aluminum, magnesium, titanium, and high-entropy alloys.
- **Phase diagrams and CALPHAD-ML hybrids**: integrate thermodynamic databases with ML for phase stability and transformation kinetics.
- **Microstructure quantification**: grain size, texture, precipitate distributions, and phase fractions from EBSD/SEM images.
- **High-entropy alloys (HEAs) and metallic glasses**: ML-driven search for solid solutions, single-phase regions, and glass-forming ability.
- **Additive manufacturing and processing**: porosity, crack susceptibility, and heat-treatment optimization.

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
        "description": "Machine learning for semiconductor materials discovery, bandgap engineering, defect analysis, and fabrication process optimization.",
        "devin_body": r'''
## When to use

You are searching for new semiconductor compounds, optimizing doping or growth, or building surrogate models for electronic-structure and fabrication parameters.

## Key concepts

- **Bandgap and carrier-property prediction**: ML models trained on DFT and experimental data for inorganic and organic semiconductors.
- **Defect and yield engineering**: wafer-level defect classification, failure prediction, and root-cause analysis.
- **Layout and process optimization**: AI-assisted lithography, etch, deposition, and design-technology co-optimization.
- **Inverse design with LLMs and GNNs**: large language and graph models for generating candidate semiconductors.
- **2D and wide-bandgap materials**: discovery of novel 2D semiconductors and power electronics materials.

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
        "description": "Machine learning for cathode, anode, electrolyte, and separator discovery, as well as battery lifetime and charging protocol optimization.",
        "devin_body": r'''
## When to use

You are developing or optimizing materials and operating conditions for Li-ion, solid-state, or beyond-Li-ion batteries.

## Key concepts

- **Battery informatics**: data-driven discovery of electrode and electrolyte materials using structural, compositional, and electrochemical descriptors.
- **Machine learning potentials**: fast atomistic simulation of ion diffusion, interfacial reactions, and degradation.
- **Lifetime and degradation prediction**: forecasting capacity fade and resistance rise from cycling data.
- **Fast-charging optimization**: closed-loop, ML-guided protocols that balance cycle life and charge time.
- **High-throughput screening**: virtual screening of thousands of candidate materials for ionic conductivity, voltage, and stability.

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
        "description": "Machine learning for superconductor discovery, critical temperature prediction, electron-phonon modeling, and materials screening.",
        "devin_body": r'''
## When to use

You are searching for new superconducting compounds or trying to predict $T_c$, critical fields, or electron-phonon coupling from crystal and electronic structure.

## Key concepts

- **Critical temperature prediction**: supervised models trained on the SuperCon database and DFT descriptors.
- **High-throughput screening**: ML filters for electron-phonon coupling, structural stability, and thermodynamic synthesizability.
- **Equivariant graph neural networks**: structure-aware models that respect crystal symmetries for superconducting properties.
- **AI-accelerated discovery pipelines**: combine generative models, interatomic potentials, and DFT to propose and validate candidates.
- **Unconventional and topological superconductivity**: data-driven searches for non-phonon pairing mechanisms and quantum materials.

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
        "description": "Machine learning for catalyst discovery, reaction mechanism elucidation, activity and selectivity prediction, and catalytic process optimization.",
        "devin_body": r'''
## When to use

You are designing heterogeneous, homogeneous, or enzymatic catalysts and need to predict activity, selectivity, stability, or optimal reaction conditions from structure and data.

## Key concepts

- **Catalysis informatics**: structured datasets, reaction descriptors, and ML models for catalyst screening.
- **Adsorption-energy and scaling-relation models**: predict binding energies and use them as microkinetic inputs.
- **Reaction network exploration**: ML-guided discovery of elementary steps and kinetic rate laws.
- **Active learning and Bayesian optimization**: efficient experimental campaigns for catalyst synthesis and testing.
- **Single-atom, electrocatalyst, and photocatalyst design**: data-driven design for energy and sustainable chemistry.

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
        "description": "Machine learning for solar-cell materials discovery, perovskite and organic PV optimization, device engineering, and stability prediction.",
        "devin_body": r'''
## When to use

You are exploring new absorbers, interfaces, or processing conditions for perovskite, organic, silicon, or tandem solar cells.

## Key concepts

- **Materials screening for absorbers**: bandgap, carrier mobility, defect tolerance, and toxicity prediction.
- **Perovskite composition and process design**: high-throughput experiments, robotic synthesis, and AI-guided optimization.
- **Organic photovoltaic (OPV) design**: molecular property prediction, non-fullerene acceptor discovery, and device-performance modeling.
- **Stability and degradation forecasting**: predict long-term performance under light, heat, and humidity.
- **Tandem and emerging architectures**: bandgap matching and current-matching for multi-junction cells.

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
        "description": "Machine learning for composite material design, manufacturing process optimization, defect detection, and multiscale property prediction.",
        "devin_body": r'''
## When to use

You are engineering fiber-reinforced, polymer-matrix, metal-matrix, or ceramic-matrix composites and need to predict or optimize mechanical, thermal, or processing behavior.

## Key concepts

- **Microstructure-property prediction**: link fiber orientation, volume fraction, void content, and interface properties to stiffness, strength, and toughness.
- **Defect detection and NDE**: ultrasonic, X-ray, and thermography image analysis for delaminations, voids, and fiber waviness.
- **Manufacturing process modeling**: resin infusion, automated fiber placement, curing, and consolidation parameter optimization.
- **Multiscale and surrogate modeling**: homogenization, finite-element surrogates, and data-driven multiscale simulators.
- **Inverse design of architected composites**: topology optimization and generative design for tailored anisotropic properties.

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
        "description": "Machine learning for membrane material design, permeability and selectivity prediction, fouling control, and separation process optimization.",
        "devin_body": r'''
## When to use

You are designing polymeric, ceramic, or 2D membranes for gas separation, water treatment, fuel cells, or energy applications.

## Key concepts

- **Membrane property prediction**: permeability, selectivity, fouling resistance, and mechanical/chemical stability from structure.
- **Polymeric and 2D material screening**: ML-accelerated virtual screening of gas- and ion-selective membranes.
- **Fouling and process modeling**: predict transmembrane pressure, flux decline, and cleaning schedules.
- **Explainable AI for transport mechanisms**: identify structural features controlling free volume, pore size, and solubility.
- **Inverse design and optimization**: generate polymer repeat units or nanopore structures for target separation performance.

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
        "description": "Machine learning for corrosion rate prediction, corrosion-resistant alloy design, protective coating optimization, and infrastructure degradation monitoring.",
        "devin_body": r'''
## When to use

You need to predict corrosion rates, identify corrosion-resistant materials, or monitor degradation in pipelines, structures, coatings, or batteries.

## Key concepts

- **Corrosion informatics**: data-driven prediction of corrosion rates and forms (pitting, galvanic, stress corrosion cracking) from environment and material data.
- **Corrosion-resistant alloy and coating design**: ML-guided composition and surface treatment optimization.
- **Electrochemical data analysis**: automated interpretation of EIS, polarization, and Tafel measurements.
- **Time-series and sensor-based monitoring**: predictive maintenance for pipelines, bridges, and offshore structures.
- **Image-based corrosion detection**: classification and segmentation of rust, cracks, and coating defects from visual and drone imagery.

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
            "https://ecoconference.kpi.ua/article/download/363309/353696/858709",
            "https://doi.org/10.54660/.jfmr.2023.4.1.362-380",
        ],
    },
]
