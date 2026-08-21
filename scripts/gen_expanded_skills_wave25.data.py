SKILLS = [
    {
        "name": "ai-for-astronomy",
        "title": "AI for Astronomy",
        "description": 'Use machine learning to triage survey alerts, classify celestial transients, and map galaxy morphology from petabyte-scale imaging and time-series data.',
        "devin_body": r'''## When to use

You are analyzing large imaging or time-domain astronomical surveys, classifying galaxies or transients, or prioritizing follow-up observations.

## Usage

- Triage LSST/ZTF/TESS alerts for supernovae, kilonovae, and variable stars in near real time.
- Classify galaxy morphology and estimate photometric redshifts from survey imaging.
- Detect anomalies in streaming time-domain data to prioritize follow-up observations.
- Emulate telescope scheduling and target-prioritization functions for survey operations.

## Steps

1. Ingest and calibrate multi-epoch imaging or light-curve data from a survey archive.
2. Extract physics-aware features (period, amplitude, color, host-galaxy offset) or train deep embeddings.
3. Train a classifier or anomaly detector and calibrate probabilities under class imbalance.
4. Validate on a held-out field and compare predictions to a trusted reference catalog.
5. Deploy the model into the alert broker to route high-priority targets to spectroscopic follow-up.

## Code pattern

```python
import lightkurve
from sklearn.ensemble import RandomForestClassifier

# Download a TESS light curve and extract simple features
lc = lightkurve.search_lightcurve("TIC 123456789", mission="TESS").download()
flux = lc.flux.value
features = extract_features(flux)  # period, amplitude, skew, etc.

# Train a simple variable/transient classifier
clf = RandomForestClassifier(n_estimators=200).fit(X, y)
```

## Tuning notes

- Use physically motivated features or augmentations (rotation, redshift, extinction).
- Account for class imbalance and survey selection effects.
- Calibrate probabilities before prioritizing follow-up targets.

## Verification

1. Replicate a galaxy morphology benchmark (e.g., Galaxy Zoo) with a CNN.
2. Train a variable-star classifier and evaluate on a held-out field.
3. Run simulation-based inference on a toy forward model and recover parameters.
''',
        "references": [
            "https://arxiv.org/abs/1904.07248",
            "https://doi.org/10.1002/widm.1349",
            "https://arxiv.org/abs/2304.00512",
            "https://doi.org/10.1146/annurev-astro-051024-021708",
        ],
    },
    {
        "name": "ai-for-planetary-science",
        "title": "AI for Planetary Science",
        "description": 'Use machine learning to classify planetary terrain, detect craters, retrieve atmospheres, and characterize exoplanets from spacecraft and telescope data.',
        "devin_body": r'''## When to use

You are analyzing spacecraft imagery, spectra, altimetry, or exoplanet light curves for Solar System or exoplanet science.

## Usage

- Segment terrain, craters, and geologic units from orbital imagery and digital elevation models.
- Unmix hyperspectral cubes to map endmember compositions and surface mineralogy.
- Retrieve atmospheric properties from exoplanet transmission and emission spectra.
- Emulate radiative-transfer and interior models to accelerate mission data analysis.

## Steps

1. Co-register and map-project orbital imagery, spectra, or altimetry for the target body.
2. Train a terrain or crater segmentation model on georeferenced, human-labeled regions.
3. Build a spectral unmixing or atmospheric retrieval surrogate validated against physics models.
4. Compare predictions to in-situ spectra or published geologic maps.
5. Integrate the model into a mission pipeline for target prioritization and downlink planning.

## Code pattern

```python
import numpy as np
import rasterio
from sklearn.ensemble import RandomForestClassifier

with rasterio.open("mars_dem.tif") as src:
    dem = src.read(1)

# Terrain classification from DEM and derived slope
slope = np.gradient(dem)
X = np.stack([dem, slope], axis=-1).reshape(-1, 2)
clf = RandomForestClassifier(n_estimators=200).fit(X, labels)
```

## Tuning notes

- Use map-projected, co-registered data with consistent illumination.
- Handle rare geologic classes with stratified sampling.
- Validate against human-labeled geologic maps and in-situ spectra.

## Verification

1. Segment craters on the Moon or Mars and compare to reference catalogs.
2. Classify spectral units from a planetary hyperspectral cube.
3. Fit an exoplanet transmission spectrum with a neural surrogate.
''',
        "references": [
            "https://doi.org/10.3847/25c2cfeb.aa328727",
            "https://arxiv.org/abs/2604.09152",
            "https://arxiv.org/abs/2310.17681",
            "https://doi.org/10.5194/epsc-dps2025-1467",
        ],
    },
    {
        "name": "ai-for-astrobiology",
        "title": "AI for Astrobiology",
        "description": 'Use machine learning to screen mass spectrometry and Raman spectra for biosignatures and guide autonomous life-detection decisions.',
        "devin_body": r'''## When to use

You are searching for biosignatures, analyzing mass spectra, or interpreting environmental sensor data from mission analogs or spaceflight instruments.

## Usage

- Distinguish biotic from abiotic organic signatures in mass-spectrometry and py-GC-MS data.
- Detect anomalies in Raman and LIMS measurements from Mars-analog and planetary samples.
- Score habitability from geochemical, mineralogical, and environmental sensor data.
- Prioritize sampling targets for rover, lander, and sample-return missions.

## Steps

1. Collect mass-spec, Raman, or sensor data with paired abiotic and biotic controls.
2. Extract peak-level or spectral features that are robust to instrument noise and contamination.
3. Train a classifier or anomaly detector to separate biotic chemistry from abiotic backgrounds.
4. Validate against terrestrial analogs and robust abiotic controls.
5. Deploy to rank samples or trigger autonomous follow-up measurements in the field.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import IsolationForest

# Anomaly detection on mass-spectrometry peak features
peaks = np.load("mass_spec_peaks.npy")
model = IsolationForest(contamination=0.05, random_state=42).fit(peaks)
scores = model.decision_function(peaks)
```

## Tuning notes

- Validate against robust abiotic controls and terrestrial analogs.
- Use contamination estimates or anomaly scores to flag novel chemistry.
- Incorporate geochemical context (mineralogy, redox, pH) into the model.

## Verification

1. Train a classifier to distinguish biotic from abiotic mass spectra.
2. Detect anomalies in a Mars-analog Raman dataset.
3. Rank samples by biosignature likelihood for a simulated rover traverse.
''',
        "references": [
            "https://www.nasa.gov/a-i-astrobiology-the-machine-learning-ml-and-artificial-intelligence-ai-guide/",
            "https://arxiv.org/abs/2407.19167",
            "https://doi.org/10.1177/15311074251403557",
            "https://doi.org/10.48550/arxiv.2503.23170",
        ],
    },
    {
        "name": "ai-for-cosmology",
        "title": "AI for Cosmology",
        "description": 'Emulate nonlinear structure formation and CMB observables to infer cosmological parameters 50x faster than full N-body simulations.',
        "devin_body": r'''## When to use

You are analyzing cosmic microwave background maps, galaxy surveys, weak-lensing convergence, or 21-cm tomography.

## Usage

- Emulate matter power spectra and N-body simulations with Gaussian processes or neural nets.
- Compress weak-lensing, galaxy, and 21-cm maps into informative summary statistics.
- Run simulation-based inference for cosmological parameters.
- Accelerate expensive Boltzmann and radiative-transfer codes.

## Steps

1. Generate a training set of cosmological parameters and high-fidelity observables from simulations.
2. Train an emulator for the power spectrum, peak counts, or full-field maps.
3. Validate the emulator outside the training range and propagate uncertainties into posteriors.
4. Use the emulator in a neural posterior-estimation or MCMC pipeline.
5. Compare inferred parameter constraints against two-point-statistics baselines.

## Code pattern

```python
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor

# Emulate a fast cosmological observable from parameters
params_train = np.load("cosmo_params_train.npy")
obs_train = np.load("power_spectrum_train.npy")
gp = GaussianProcessRegressor().fit(params_train, obs_train)
pred, sigma = gp.predict(params_test, return_std=True)
```

## Tuning notes

- Preserve physical symmetries (translation, rotation, scale) in architectures where relevant.
- Propagate uncertainties from emulators into posterior constraints.
- Validate emulators against high-fidelity simulations outside the training region.

## Verification

1. Emulate the matter power spectrum and compare to a Boltzmann code.
2. Train a weak-lensing map classifier or peak-count regressor.
3. Infer cosmological parameters with a neural posterior estimator.
''',
        "references": [
            "https://doi.org/10.1088/1361-6633/acd2ea",
            "https://doi.org/10.3390/galaxies13050114",
            "https://arxiv.org/abs/2605.12877",
            "https://arxiv.org/abs/2605.10105",
        ],
    },
    {
        "name": "ai-for-particle-physics",
        "title": "AI for Particle Physics",
        "description": 'Use machine learning to tag jets, reconstruct events, accelerate detector simulation, and search for anomalous signatures at colliders and neutrino experiments.',
        "devin_body": r'''## When to use

You are classifying high-energy physics events, accelerating detector simulation, or searching for rare signals in collider or neutrino data.

## Usage

- Classify jets, taus, and heavy-flavor decays from collider event data.
- Generate fast calorimeter and detector-response simulations.
- Search for new-physics anomalies in a model-agnostic way.
- Build Lorentz- and SE(3)-equivariant architectures for particle clouds.

## Steps

1. Preprocess detector events into point clouds or jet images with pile-up masks.
2. Train a permutation- or equivariant-aware classifier for the target physics object.
3. Calibrate confidence and test for adversarial robustness.
4. Build a fast generative surrogate for detector showers and validate against Geant4.
5. Run an anomaly-detection search on public collider data and report discovery significance.

## Code pattern

```python
import torch
import torch.nn as nn

class ParticleNet(nn.Module):
    def __init__(self, in_dim=3, out_dim=2):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv1d(in_dim, 64, 1), nn.ReLU(), nn.AdaptiveAvgPool1d(1)
        )
        self.head = nn.Linear(64, out_dim)

    def forward(self, x):
        return self.head(self.encoder(x).squeeze(-1))
```

## Tuning notes

- Handle pile-up, detector noise, and variable multiplicities with masking.
- Use equivariant or permutation-invariant architectures for particle clouds.
- Calibrate confidence and significance estimates for discovery claims.

## Verification

1. Train a top-quark jet tagger and compare to a rule-based baseline.
2. Generate fast calorimeter showers and compare shower shapes to Geant4.
3. Run an anomaly-detection search on a public collider dataset.
''',
        "references": [
            "https://arxiv.org/abs/1912.08245",
            "https://arxiv.org/abs/2102.02770",
            "https://arxiv.org/abs/2112.03769",
            "https://doi.org/10.1140/epjs/s11734-024-01364-3",
        ],
    },
    {
        "name": "ai-for-condensed-matter",
        "title": "AI for Condensed Matter",
        "description": 'Use machine learning to classify phases, learn interatomic potentials, and emulate quantum many-body and density-functional calculations.',
        "devin_body": r'''## When to use

You are identifying phases and order parameters, learning interatomic potentials, or emulating quantum many-body Hamiltonians.

## Usage

- Classify spin, electronic, and structural phases across phase diagrams.
- Learn neural-network interatomic potentials and DFT exchange-correlation surrogates.
- Identify topological invariants and hidden order parameters.
- Emulate quantum many-body systems with neural quantum states and tensor networks.

## Steps

1. Generate or load spin, electronic, and structural configurations with phase labels near critical points.
2. Design symmetry-respecting descriptors or graph representations for the material.
3. Train a classifier, neural potential, or DFT surrogate with physics-aware featurization.
4. Validate generalization at critical points, topological boundaries, and unseen compositions.
5. Use the model to screen structures or accelerate molecular-dynamics and DFT workflows.

## Code pattern

```python
import numpy as np
from sklearn.neural_network import MLPClassifier

# Classify spin configurations from a 2D Ising model
configs = np.load("ising_configs.npy")
labels = np.load("ising_labels.npy")
clf = MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=500).fit(configs, labels)
```

## Tuning notes

- Choose descriptors that respect lattice and gauge symmetries.
- Use transfer learning across related Hamiltonians when data is scarce.
- Check generalization near critical points and topological phase boundaries.

## Verification

1. Classify ordered versus disordered Ising phases and locate the critical point.
2. Train an ML potential for a small molecule or crystal and validate energies.
3. Identify a topological phase from entanglement or Wilson-loop data.
''',
        "references": [
            "https://doi.org/10.1088/1361-648x/abb895",
            "https://www.nature.com/articles/nphys4035",
            "https://doi.org/10.1103/revmodphys.91.045002",
            "https://www.nature.com/articles/s41524-019-0221-0",
        ],
    },
    {
        "name": "ai-for-optics",
        "title": "AI for Optics",
        "description": 'Use deep learning to reconstruct images, retrieve phase, design optical elements, and solve inverse scattering problems in computational imaging.',
        "devin_body": r'''## When to use

You are reconstructing images from indirect optical measurements, designing phase masks, or calibrating complex optical systems.

## Usage

- Reconstruct images from undersampled, coded, or indirect optical measurements.
- Retrieve phase from intensity-only measurements in microscopy and astronomy.
- Co-design phase masks, coded apertures, and metalenses with reconstruction networks.
- Deconvolve images from measured point-spread functions and aberrations.

## Steps

1. Formulate the physical forward model (PSF, diffraction, or scattering operator).
2. Acquire paired measurements and ground truth, or use self-supervised/physics-informed training.
3. Train an inversion network or optimize an optical element end-to-end.
4. Validate on realistic noise, aberrations, and sensor nonlinearities.
5. Compare reconstruction quality to classical methods such as Gerchberg-Saxton or deconvolution.

## Code pattern

```python
import numpy as np
from scipy.signal import convolve2d

# Forward model: image convolved with a known PSF
psf = np.load("psf.npy")
measurement = convolve2d(gt_image, psf, mode="same", boundary="wrap")
# A learned deconvolution network would invert this
```

## Tuning notes

- Encode the physical forward model in the loss or network architecture.
- Use self-supervised or physics-informed training when paired ground truth is scarce.
- Validate on realistic noise, aberrations, and sensor nonlinearities.

## Verification

1. Train a phase-retrieval network and compare to Gerchberg-Saxton.
2. Learn a coded aperture for compressive spectral imaging.
3. Reconstruct a microscopy stack from diffraction patterns.
''',
        "references": [
            "https://arxiv.org/abs/2210.16709",
            "https://arxiv.org/abs/2207.00164",
            "https://doi.org/10.1038/s41377-022-00714-x",
            "https://www.nature.com/articles/s41377-022-00743-6",
        ],
    },
    {
        "name": "ai-for-acoustics",
        "title": "AI for Acoustics",
        "description": 'Use machine learning to localize sources, classify bioacoustic events, monitor structural health, and model spatial sound fields.',
        "devin_body": r'''## When to use

You are analyzing acoustic recordings, localizing sources, classifying animal calls, or predicting sound fields.

## Usage

- Localize sound sources from microphone arrays using TDOA and beamforming features.
- Classify animal calls, marine mammals, and environmental sound events.
- Detect cracks and corrosion via acoustic emission and guided-wave analysis.
- Reconstruct room impulse responses and spatial audio scenes.

## Steps

1. Capture and time-synchronize multichannel audio or acoustic-emission waveforms.
2. Compute spectrograms, mel features, or TDOA embeddings matched to the signal of interest.
3. Train a classifier, localizer, or inverse model with physics-informed augmentations.
4. Validate against ground-truth labels or known source positions.
5. Deploy for real-time structural monitoring or ecological field surveys.

## Code pattern

```python
import librosa

# Load audio and compute a mel spectrogram
y, sr = librosa.load("recording.wav", sr=16000)
spec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=64)
spec_db = librosa.power_to_db(spec, ref=np.max)
```

## Tuning notes

- Match time-frequency resolution to the signal of interest.
- Augment with reverb, noise, and direction-of-arrival variations.
- Consider physical wave constraints and microphone array geometry.

## Verification

1. Classify environmental sound events on a labeled dataset.
2. Localize a sound source from multichannel recordings.
3. Reconstruct a room impulse response from sparse measurements.
''',
        "references": [
            "https://doi.org/10.1038/s44384-025-00021-w",
            "https://arxiv.org/abs/1905.04418",
            "https://arxiv.org/abs/2504.16289",
            "https://arxiv.org/abs/2508.21470",
        ],
    },
    {
        "name": "ai-for-photonics",
        "title": "AI for Photonics",
        "description": 'Use deep learning to inverse-design photonic devices, metasurfaces, and optical communication links while replacing expensive Maxwell solvers.',
        "devin_body": r'''## When to use

You are designing photonic devices, metasurfaces, waveguides, or optimizing optical communication links.

## Usage

- Inverse-design metasurfaces, metalenses, and waveguides for target phase or spectral responses.
- Train neural surrogates to replace FDTD or finite-element simulations.
- Optimize optical-communication modulators, demultiplexers, and equalizers.
- Enforce fabrication constraints and minimum feature sizes during design.

## Steps

1. Define the target optical response and a parameterization of the geometry.
2. Build a forward surrogate by training on FDTD/FEM simulations or experimental data.
3. Validate the surrogate against full-wave solvers on held-out designs.
4. Run inverse design or topology optimization with fabrication constraints.
5. Fabricate and characterize the device, then feed results back to refine the surrogate.

## Code pattern

```python
import torch
import torch.nn as nn

# Surrogate mapping geometry parameters to transmission spectrum
class PhotonicSurrogate(nn.Module):
    def __init__(self, in_dim=10, out_dim=100):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 128), nn.ReLU(), nn.Linear(128, out_dim)
        )

    def forward(self, x):
        return self.net(x)
```

## Tuning notes

- Enforce fabrication and minimum-feature constraints.
- Use active learning when full-wave simulations are expensive.
- Validate surrogate predictions against FDTD or finite-element solvers.

## Verification

1. Train a surrogate for a waveguide or grating transmission spectrum.
2. Optimize a metasurface geometry for a target phase profile.
3. Compare a neural inverse design to a gradient-based topology baseline.
''',
        "references": [
            "https://doi.org/10.1002/lpor.202100399",
            "https://doi.org/10.1088/1361-6633/abb4c7",
            "https://doi.org/10.1038/s41578-020-00260-1",
            "https://doi.org/10.1016/j.eng.2024.08.016",
        ],
    },
    {
        "name": "ai-for-nanotechnology",
        "title": "AI for Nanotechnology",
        "description": 'Use machine learning to design nanoparticles, predict nanoscale properties, and optimize synthesis and imaging workflows.',
        "devin_body": r'''## When to use

You are designing nanoparticles, predicting nanoscale properties, or optimizing synthesis and fabrication processes.

## Usage

- Predict plasmonic, catalytic, or mechanical properties from composition and morphology descriptors.
- Discover multimetallic nanoparticle compositions with active learning and Bayesian optimization.
- Segment and quantify nanoparticles in electron microscopy images.
- Optimize synthesis recipes and self-assembly conditions.

## Steps

1. Assemble descriptors for composition, size, shape, surface ligands, and synthesis conditions.
2. Curate property labels from experiments or simulations.
3. Train a small-data regression or segmentation model with physics-aware features.
4. Validate against electron microscopy, XRD, or optical spectroscopy.
5. Use the model to propose and iterate new syntheses via Bayesian optimization.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

# Predict a nanoparticle property from descriptors
X = np.array([[0.8, 5.0, 1.0], [0.5, 10.0, 2.0], [0.9, 7.0, 1.5]])
y = np.array([520.0, 580.0, 540.0])
model = GradientBoostingRegressor().fit(X, y)
```

## Tuning notes

- Represent size, shape, and surface chemistry explicitly.
- Use small-data methods and physics-aware featurization.
- Validate with electron microscopy, XRD, or optical spectroscopy.

## Verification

1. Predict nanoparticle plasmon resonance from composition and size descriptors.
2. Optimize a synthesis recipe with Bayesian optimization.
3. Segment nanoparticles in a TEM image and compare to manual counts.
''',
        "references": [
            "https://doi.org/10.3390/ijms252212368",
            "https://doi.org/10.1088/1361-6528/ac46d7",
            "https://www.nature.com/articles/s41578-021-00337-5",
            "https://doi.org/10.3390/ma17071621",
        ],
    },
    {
        "name": "ai-for-microfluidics",
        "title": "AI for Microfluidics",
        "description": 'Use machine learning to control droplet generation, sort cells, optimize reactions, and automate high-throughput screening on chip.',
        "devin_body": r'''## When to use

You are controlling microfluidic droplets, analyzing high-throughput cell assays, or optimizing on-chip reactions.

## Usage

- Classify and sort droplets, cells, and particles from high-speed video or sensor signals.
- Optimize flow rates and reagents for droplet size and encapsulation.
- Monitor organ-on-chip and single-cell assays in real time.
- Detect sorting errors and control actuators in closed loop.

## Steps

1. Set up high-speed imaging or impedance/fluorescence sensors synchronized with flow controls.
2. Extract droplet or cell features and train a real-time classifier or detector.
3. Validate sorting accuracy and throughput on labeled reference samples.
4. Optimize flow rates and reagent concentrations with Bayesian or reinforcement-learning control.
5. Close the loop with actuators and log drift for continuous retraining.

## Code pattern

```python
import cv2
import numpy as np

# Extract droplet features from a high-speed video frame
cap = cv2.VideoCapture("droplets.avi")
_, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
diameters = [2 * np.sqrt(cv2.contourArea(c) / np.pi) for c in contours]
```

## Tuning notes

- Handle low contrast, high speed, and out-of-focus frames.
- Synchronize video, pressure, and flow-rate sensors.
- Close the loop with actuators for real-time sorting or mixing.

## Verification

1. Detect and classify droplets in a microfluidic video.
2. Optimize droplet size by learning the flow-rate mapping.
3. Sort cells based on real-time image features.
''',
        "references": [
            "https://doi.org/10.1039/D2LC00254J",
            "https://doi.org/10.1016/j.matt.2020.08.034",
            "https://doi.org/10.1039/D3LC01012K",
            "https://doi.org/10.1039/D1NR06195J",
        ],
    },
    {
        "name": "ai-for-biophysics",
        "title": "AI for Biophysics",
        "description": 'Use machine learning to learn molecular dynamics, map free-energy landscapes, and extract kinetics from single-molecule measurements.',
        "devin_body": r'''## When to use

You are analyzing molecular dynamics trajectories, predicting free energies, or extracting kinetics from single-molecule measurements.

## Usage

- Learn neural-network potentials and coarse-grained models for biomolecular dynamics.
- Build Markov state models and free-energy landscapes from MD trajectories.
- Coarse-grain high-dimensional motion into interpretable collective variables.
- Segment single-molecule FRET and force-spectroscopy traces.

## Steps

1. Load and align MD trajectories or single-molecule time series.
2. Choose physically meaningful collective variables or learned embeddings.
3. Train a neural potential, Markov state model, or hidden-Markov model.
4. Validate against experimental observables such as NMR, FRET, or cryo-EM.
5. Use the model to predict rare events, binding kinetics, or free-energy differences.

## Code pattern

```python
import mdtraj
from sklearn.decomposition import PCA

# Reduce dimensionality of a protein trajectory
traj = mdtraj.load("trajectory.xtc", top="topology.pdb")
coords = traj.xyz.reshape(traj.n_frames, -1)
pca = PCA(n_components=2).fit_transform(coords)
```

## Tuning notes

- Choose collective variables with clear physical meaning.
- Validate against experimental observables (NMR, FRET, cryo-EM).
- Use uncertainty-aware models and enhanced sampling for rare events.

## Verification

1. Build a Markov state model and compare implied timescales.
2. Predict a binding free energy with a neural potential.
3. Segment single-molecule FRET trajectories into metastable states.
''',
        "references": [
            "https://doi.org/10.1063/5.0248589",
            "https://doi.org/10.1063/5.0082179",
            "https://doi.org/10.1146/annurev-physchem-042018-052331",
            "https://doi.org/10.1016/j.sbi.2023.102569",
        ],
    },
]
