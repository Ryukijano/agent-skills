SKILLS = [
    {
        "name": "ai-for-astronomy",
        "title": "AI for Astronomy",
        "description": "Machine learning for survey-scale classification, transient detection, galaxy morphology, light-curve analysis, and telescope scheduling.",
        "devin_body": r'''## When to use

You are analyzing large imaging or time-domain astronomical surveys, classifying galaxies or transients, or prioritizing follow-up observations.

## Key concepts

- **Survey data**: Rubin/LSST, ZTF, TESS, JWST, and Euclid produce petabyte-scale catalogs.
- **Light curves and images**: time-series classification, anomaly detection, and image segmentation.
- **Simulation-based inference**: amortized posterior estimation for complex forward models.
- **Foundation models**: large-scale pre-training on unlabeled spectra or images.

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
        "description": "Machine learning for mission data analysis, terrain classification, crater detection, atmospheric retrievals, and exoplanet characterization.",
        "devin_body": r'''## When to use

You are analyzing spacecraft imagery, spectra, altimetry, or exoplanet light curves for Solar System or exoplanet science.

## Key concepts

- **Orbital imagery**: segmentation and classification of terrain, craters, and geologic units.
- **Spectral unmixing**: decomposing hyperspectral cubes into endmember compositions.
- **Radiative transfer**: fast forward models and retrieval of atmospheric properties.
- **Interior and orbital models**: emulation of planet structure and radial-velocity signals.

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
            "https://ui.adsabs.harvard.edu/abs/2025epsc.conf.1467K/abstract",
        ],
    },
    {
        "name": "ai-for-astrobiology",
        "title": "AI for Astrobiology",
        "description": "ML for biosignature detection, life-detection mass spectrometry, extremophile habitats, and mission autonomy in alien environments.",
        "devin_body": r'''## When to use

You are searching for biosignatures, analyzing mass spectra, or interpreting environmental sensor data from mission analogs or spaceflight instruments.

## Key concepts

- **Mass spectrometry and Raman**: pattern recognition in complex molecular spectra.
- **Biosignatures**: molecular, isotopic, and morphological indicators of life.
- **Habitability indices**: environmental proxies for water, energy, and nutrients.
- **Autonomous sampling**: closed-loop decision-making for in-situ exploration.

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
        "description": "ML for large-scale structure, weak lensing, CMB analysis, 21-cm cosmology, and cosmological parameter inference.",
        "devin_body": r'''## When to use

You are analyzing cosmic microwave background maps, galaxy surveys, weak-lensing convergence, or 21-cm tomography.

## Key concepts

- **N-body surrogates**: fast approximations of dark-matter structure formation.
- **Summary statistics**: power spectra, bispectra, peak counts, and Minkowski functionals.
- **Simulation-based inference**: neural posterior estimation and likelihood-free methods.
- **Emulation and Gaussian processes**: replacing expensive Boltzmann and radiative-transfer codes.

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
        "description": "ML for collider event classification, jet tagging, fast detector simulation, neutrino event reconstruction, and new-physics searches.",
        "devin_body": r'''## When to use

You are classifying high-energy physics events, accelerating detector simulation, or searching for rare signals in collider or neutrino data.

## Key concepts

- **Jet tagging and event classification**: CNNs, graph networks, and transformers on point clouds.
- **Fast simulation**: generative models for calorimeter showers and detector response.
- **Anomaly detection**: model-agnostic searches for new physics.
- **Lorentz and SE(3) equivariance**: respecting spacetime symmetries in architectures.

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
            "https://ar5iv.labs.arxiv.org/html/2102.02770",
            "https://arxiv.org/abs/2112.03769",
            "https://doi.org/10.1140/epjs/s11734-024-01364-3",
        ],
    },
    {
        "name": "ai-for-condensed-matter",
        "title": "AI for Condensed Matter",
        "description": "Machine learning for phase classification, topological order, Hamiltonian learning, density functional surrogates, and quantum many-body systems.",
        "devin_body": r'''## When to use

You are identifying phases and order parameters, learning interatomic potentials, or emulating quantum many-body Hamiltonians.

## Key concepts

- **Order parameters and phase transitions**: supervised classification of spin and electronic configurations.
- **Topological invariants**: learning hidden order without local order parameters.
- **ML potentials and DFT surrogates**: neural-network potentials and exchange-correlation functionals.
- **Quantum many-body systems**: tensor networks, neural quantum states, and variational ansätze.

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
        "description": "Computational imaging, lens design, wavefront shaping, optical metrology, and inverse scattering with deep learning.",
        "devin_body": r'''## When to use

You are reconstructing images from indirect optical measurements, designing phase masks, or calibrating complex optical systems.

## Key concepts

- **Inverse problems**: image reconstruction from undersampled or coded measurements.
- **Wave propagation**: Fourier optics, diffraction, and point-spread functions.
- **Coded apertures and phase masks**: jointly optimizing hardware and algorithms.
- **Phase retrieval**: recovering phase from intensity measurements.

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
        "description": "Machine learning for source localization, room acoustics, bioacoustics, structural health monitoring, and spatial audio.",
        "devin_body": r'''## When to use

You are analyzing acoustic recordings, localizing sources, classifying animal calls, or predicting sound fields.

## Key concepts

- **Spectrograms and mel features**: time-frequency representations for classification.
- **Beamforming and source separation**: multichannel spatial audio methods.
- **Room impulse responses**: reverberation and geometry inference.
- **Physics-informed acoustics**: wave-equation constraints in neural models.

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
        "description": "Deep learning for photonic device inverse design, metasurfaces, optical communications, and nanophotonic simulation surrogates.",
        "devin_body": r'''## When to use

You are designing photonic devices, metasurfaces, waveguides, or optimizing optical communication links.

## Key concepts

- **Inverse design**: neural networks and topology optimization for nanophotonic structures.
- **Metasurfaces and metamaterials**: subwavelength wavefront engineering.
- **Maxwell solvers and surrogates**: fast replacements for finite-difference time-domain.
- **Optical communications**: equalization, modulation, and link optimization.

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
        "description": "ML for nanoparticle design, nanomaterial discovery, nano-architectonics, nanoscale imaging, and nanomanufacturing optimization.",
        "devin_body": r'''## When to use

You are designing nanoparticles, predicting nanoscale properties, or optimizing synthesis and fabrication processes.

## Key concepts

- **Descriptors for nanomaterials**: composition, size, shape, surface ligands, and synthesis conditions.
- **Nano-architectonics**: bottom-up assembly and self-organization.
- **High-throughput imaging**: electron microscopy and scanning-probe segmentation.
- **Active learning and Bayesian optimization**: sparse, expensive experiments.

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
        "description": "Machine learning for droplet generation, lab-on-a-chip control, cell sorting, reaction optimization, and high-throughput screening.",
        "devin_body": r'''## When to use

You are controlling microfluidic droplets, analyzing high-throughput cell assays, or optimizing on-chip reactions.

## Key concepts

- **Droplet microfluidics**: flow-focusing, generation, and encapsulation.
- **Image-based sorting and analysis**: high-speed vision for cells and particles.
- **Reaction optimization**: Bayesian optimization of flow rates and reagents.
- **Organ-on-a-chip and organoids**: multiscale physiological models.

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
        "description": "Machine learning for molecular dynamics, free-energy landscapes, protein-ligand kinetics, single-molecule analysis, and membrane systems.",
        "devin_body": r'''## When to use

You are analyzing molecular dynamics trajectories, predicting free energies, or extracting kinetics from single-molecule measurements.

## Key concepts

- **Molecular dynamics and force fields**: ML potentials and coarse-grained models.
- **Free energy and kinetics**: Markov state models, umbrella sampling, and metadynamics.
- **Coarse graining**: learning low-dimensional representations of biomolecular motion.
- **Single-molecule biophysics**: hidden Markov models and dwell-time analysis.

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
