SKILLS = [
    {
        "name": "ai-for-synthetic-biology",
        "title": "AI for Synthetic Biology",
        "description": "Machine learning for genetic circuit design, promoter and RBS optimization, metabolic pathway engineering, and closed-loop Design-Build-Test-Learn biofoundry pipelines.",
        "devin_body": r'''
## When to use

You are engineering genetic circuits, optimizing promoters/RBSs, or automating a DBTL cycle for a synthetic biology project.

## Key concepts

- **Genetic parts**: promoters, ribosome binding sites (RBS), terminators, coding sequences, and their context dependence.
- **DBTL cycle**: Design, Build, Test, Learn closed-loop iteration.
- **Predictive part models**: regression and sequence models trained on part activity data.
- **Metabolic engineering**: pathway design, flux balance analysis, retro-biosynthesis.
- **Active learning / Bayesian optimization**: pick the next strain or part to test.
- **Biological constraints**: chassis dependency, toxicity, genetic load, and modularity limits.

## Code pattern

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor

# One-hot encode promoter sequences (A,C,G,T)
def one_hot(seq):
    mapping = {'A': [1,0,0,0], 'C': [0,1,0,0], 'G': [0,0,1,0], 'T': [0,0,0,1], 'N': [0,0,0,0]}
    return np.array([mapping[s] for s in seq.upper()]).flatten()

df = pd.read_csv('promoters.csv')  # columns: sequence, expression
X = np.vstack(df['sequence'].apply(one_hot))
y = df['expression'].values

model = GradientBoostingRegressor(n_estimators=200, max_depth=4)
score = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
print('CV RMSE:', np.mean(-score) ** 0.5)

model.fit(X, y)
# Predict expression of a new promoter
new_seq = 'TTGACATGATAACAGTAA...'
print(model.predict(one_hot(new_seq).reshape(1, -1)))
```

## Tuning notes

- Match training data to the intended chassis (e.g., E. coli, S. cerevisiae, mammalian cells).
- One-hot encoding works for short parts; for longer sequences consider k-mer counts or language models.
- Watch for context effects and promoter crosstalk; use paired designs when possible.
- Active learning reduces the number of experimental builds needed by 2-5x.
- Always validate in the target biological system; in silico predictors are noisy.

## Verification

1. Train an expression predictor on synthetic promoter data and report cross-validated error.
2. Suggest a set of promoters that spans low, medium, and high predicted expression.
3. Compare predicted and measured activity for at least 5 designed constructs.
''',
        "references": [
            "https://doi.org/10.1016/j.cobme.2024.100553",
            "https://doi.org/10.1021/acssynbio.4c00091",
            "https://github.com/JBEI/ART",
            "https://github.com/snap-stanford/BioDiscoveryAgent",
            "https://biocomplete.it/",
        ],
    },
    {
        "name": "ai-for-protein-design",
        "title": "AI for Protein Design",
        "description": "Inverse folding, generative backbone design, and binder engineering with ProteinMPNN, RFdiffusion, structure predictors, and Rosetta validation.",
        "devin_body": r'''
## When to use

You need a protein sequence for a fixed backbone, a de novo protein binder, or a new scaffold with specified structure or function.

## Key concepts

- **Inverse folding**: predict an amino-acid sequence that folds into a target backbone.
- **ProteinMPNN**: message-passing neural network for sequence design.
- **RFdiffusion**: diffusion model for generating protein backbones and binders.
- **Structure prediction**: AlphaFold2, ESMFold, or OpenFold to validate designs.
- **Interface metrics**: pLDDT, pAE, interface RMSD, binding energy.
- **Mutagenesis**: design focused libraries and assess stability.

## Code pattern

```python
import subprocess

# 1. Generate a backbone with RFdiffusion (requires installed environment)
subprocess.run([
    'python', 'scripts/run_inference.py',
    'inference.output_prefix=outputs/binder',
    'inference.num_designs=10',
    'contigmap.contigs=[150-150]',
], check=True)

# 2. Design sequences with ProteinMPNN
subprocess.run([
    'python', 'proteinmpnn_run.py',
    '--pdb_path', 'outputs/binder_0.pdb',
    '--out_folder', 'mpnn_outputs',
    '--num_seq_per_target', '8',
], check=True)

# 3. Validate with a structure predictor (ESMFold, AlphaFold2, or OpenFold)
# Fold the top sequences and inspect pLDDT plus interface residues.
```

## Tuning notes

- Start with a high-quality backbone; RFdiffusion works best with clear design objectives.
- Use `num_seq_per_target` >= 8 to explore sequence space.
- Filter designs by pLDDT > 80 and low pAE at the binding interface.
- For binders, check shape complementarity and hotspot residues.
- Experimental validation (yeast display, BLI, SPR) is the ground truth.

## Verification

1. Design 10 sequences for a fixed backbone and run them through ESMFold/AlphaFold2.
2. Compare predicted structures to the target backbone (RMSD < 2 A for monomers).
3. Design a binder to a target, dock/validate it, and rank by interface pLDDT.
''',
        "references": [
            "https://github.com/dauparas/ProteinMPNN",
            "https://doi.org/10.1126/science.add2187",
            "https://github.com/RosettaCommons/RFdiffusion",
            "https://doi.org/10.1038/s41586-023-06415-8",
            "https://doi.org/10.1038/s41467-023-38328-5",
        ],
    },
    {
        "name": "ai-for-immunology",
        "title": "AI for Immunology",
        "description": "Machine learning for adaptive immune receptor repertoires, epitope-MHC binding, immune cell phenotyping, and vaccine/immunotherapy design.",
        "devin_body": r'''
## When to use

You are analyzing B-cell or T-cell receptor repertoires, predicting epitope binding, or prioritizing vaccine/immunotherapy candidates.

## Key concepts

- **AIRR**: adaptive immune receptor repertoire sequencing.
- **BCR/TCR clonotypes**: V(D)J rearranged receptor sequences.
- **MHC binding**: peptide presentation by class I and class II MHC molecules.
- **Epitope prediction**: mapping receptors to antigens.
- **Immune cell phenotyping**: flow/mass cytometry, single-cell RNA/CITE-seq.
- **Vaccine design**: immunogen selection, epitope mapping, mRNA optimization.

## Code pattern

```python
from mhcflurry import Class1AffinityPredictor

predictor = Class1AffinityPredictor.load()

peptides = ['SIINFEKL', 'SLYNTVATL', 'GILGFVFTL']
result = predictor.predict_to_dataframe(
    peptides=peptides,
    allele='HLA-A*02:01',
)
print(result[['peptide', 'allele', 'prediction']])
```

## Tuning notes

- MHCflurry covers common HLA alleles; rare alleles may need custom training.
- Use appropriate peptide lengths (8-11 for class I, 13-25 for class II).
- For AIRR, normalize by sampling depth and PCR/UMI errors.
- Pair immune repertoire labels with clinical metadata carefully.
- Validate predictions with ELISPOT, tetramer, or MHC multimer assays.

## Verification

1. Predict class-I MHC binding for a set of peptides and compare to experimental IC50 data.
2. Load a small AIRR dataset into immuneML and run a classification workflow.
3. Cluster clonotypes and check whether clusters correlate with disease status.
''',
        "references": [
            "https://immuneml.uio.no/",
            "https://doi.org/10.1038/s42256-021-00413-z",
            "https://github.com/openvax/mhcflurry",
            "https://doi.org/10.1016/j.csbj.2025.10.007",
            "https://immunomind.github.io/docs/",
        ],
    },
    {
        "name": "ai-for-neuroscience",
        "title": "AI for Neuroscience",
        "description": "Deep learning for neural recordings, brain decoding, neuroimaging analysis, connectomics, and NeuroAI foundation models.",
        "devin_body": r'''
## When to use

You are analyzing EEG, MEG, fMRI, calcium imaging, or spike data and want to decode neural states, detect biomarkers, or build NeuroAI models.

## Key concepts

- **Neural encoding / decoding**: mapping stimuli to neural activity or vice versa.
- **Spike sorting**: separating single-unit activity from extracellular recordings.
- **Time-series models**: CNNs, RNNs, transformers for neural signals.
- **Neuroimaging pipelines**: fMRI/EEG preprocessing with MNE/FSL/AFNI.
- **Connectomics**: mapping structural and functional brain connectivity.
- **NeuroAI benchmarks**: NeuralBench, brain foundation models.

## Code pattern

```python
import mne
import numpy as np
import torch
import torch.nn as nn

# Load and epoch an EEG recording
raw = mne.io.read_raw_edf('subject_01.edf', preload=True)
events = mne.make_fixed_length_events(raw, duration=2.0)
epochs = mne.Epochs(raw, events, tmin=0, tmax=2.0, baseline=None, preload=True)

X = epochs.get_data()  # (n_epochs, n_channels, n_times)
y = epochs.metadata['condition']

# Simple 1D CNN over time per channel
class SimpleCNN(nn.Module):
    def __init__(self, n_channels, n_classes):
        super().__init__()
        self.conv1 = nn.Conv1d(n_channels, 32, kernel_size=25, stride=2)
        self.pool = nn.AdaptiveAvgPool1d(1)
        self.fc = nn.Linear(32, n_classes)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = self.pool(x).squeeze(-1)
        return self.fc(x)

model = SimpleCNN(X.shape[1], len(np.unique(y)))
print(model)
```

## Tuning notes

- Standardize channel layouts and sampling rates across subjects.
- Reject epochs with excessive movement or EMG artifact before training.
- Use cross-subject validation to estimate real-world generalization.
- Temporal alignment matters for ERP/ERF analyses.
- Interpret models with SHAP or channel-wise saliency maps.

## Verification

1. Train a CNN to classify two cognitive conditions from EEG and report accuracy.
2. Visualize topographic activation for important time windows.
3. Compare a subject-specific model to a leave-one-subject-out model.
''',
        "references": [
            "https://mne.tools/",
            "https://github.com/facebookresearch/neuroai",
            "https://github.com/catalystneuro/neuroconv",
            "https://doi.org/10.1016/j.neures.2024.06.003",
            "https://doi.org/10.1088/1741-2552/ae4455",
        ],
    },
    {
        "name": "ai-for-precision-medicine",
        "title": "AI for Precision Medicine",
        "description": "Multimodal machine learning for personalized diagnosis, treatment selection, risk prediction, and integration of genomics, EHRs, imaging, and wearables.",
        "devin_body": r'''
## When to use

You need to build a personalized risk model, recommend therapy, integrate multi-omic and clinical data, or stratify patients for a trial.

## Key concepts

- **Multi-modal patient data**: genomics, EHRs, medical imaging, wearables, lab tests.
- **Biomarker discovery**: identifying predictive, prognostic, or pharmacodynamic markers.
- **Treatment response prediction**: matching patients to therapies.
- **Risk stratification**: time-to-event models, survival analysis.
- **Federated learning**: training across institutions without centralizing sensitive data.
- **Explainability and fairness**: clinical AI must be interpretable and unbiased.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

# Tabular patient data: features + binary outcome
df = pd.read_csv('patients.csv')
feature_cols = ['age', 'bmi', 'genetic_risk_score', 'biomarker_x', 'comorbidity_count']
X = df[feature_cols]
y = df['responder']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
model = RandomForestClassifier(n_estimators=200, class_weight='balanced')
model.fit(X_train, y_train)

y_proba = model.predict_proba(X_test)[:, 1]
print('AUC-ROC:', roc_auc_score(y_test, y_proba))
```

## Tuning notes

- Harmonize data across sites and time; missingness is often informative.
- Include protected attributes only to audit for bias, not as predictors unless justified.
- Validate on external cohorts; internal validation overestimates clinical utility.
- Use time-split validation when temporal drift is likely.
- Integrate expert priors and clinical guidelines into model constraints.

## Verification

1. Train a responder vs non-responder classifier on a multi-modal cohort.
2. Compare AUC on internal and external test sets.
3. Generate SHAP values and check whether top features match clinical knowledge.
''',
        "references": [
            "https://doi.org/10.3389/fpubh.2025.1656603",
            "https://link.springer.com/article/10.1038/s41746-025-02259-w",
            "https://ascpt.onlinelibrary.wiley.com/doi/10.1002/cpt.3152",
            "https://www.nature.com/articles/s41576-026-00992-w",
            "https://allofus.nih.gov/",
        ],
    },
    {
        "name": "ai-for-biofoundries",
        "title": "AI for Biofoundries",
        "description": "AI/ML-driven lab automation, robotic liquid handling, closed-loop DBTL, and self-driving laboratories for synthetic biology.",
        "devin_body": r'''
## When to use

You are running high-throughput synthetic biology experiments in a biofoundry, automating liquid handling, or closing the DBTL loop with predictive models.

## Key concepts

- **Biofoundry infrastructure**: robotic liquid handlers, plate readers, bioreactors, LIMS.
- **DBTL automation**: design, build, test, learn cycles executed with minimal human intervention.
- **Self-driving labs**: active learning + automation to select and run the next experiments.
- **Workflow abstraction**: unit operations, workflows, projects.
- **Digital twins**: models that simulate expected experimental outcomes.
- **Data standards**: metadata capture, FAIR principles, programmable APIs.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from skopt import gp_minimize
from skopt.space import Real, Integer

# Measured titers from previous DBTL cycle
df = pd.read_csv('biofoundry_results.csv')
X = df[['promoter_strength', 'rbs_strength', 'copy_number', 'induction']]
y = df['titer']

surrogate = RandomForestRegressor().fit(X, y)

space = [
    Real(0.0, 1.0, name='promoter_strength'),
    Real(0.0, 1.0, name='rbs_strength'),
    Integer(1, 10, name='copy_number'),
    Real(0.0, 1.0, name='induction'),
]

def objective(params):
    return -surrogate.predict([params])[0]

result = gp_minimize(objective, space, n_calls=20)
print('Next best design:', result.x)
```

## Tuning notes

- Integrate the robot API and LIMS for true closed-loop operation.
- Use constrained optimization to respect hardware and biology limits.
- Track batch and instrument effects as features.
- Keep human-in-the-loop for safety and protocol validation.
- Start with simple designs and incrementally add combinatorial complexity.

## Verification

1. Build a surrogate model of titer from historical biofoundry runs.
2. Run a Bayesian optimization loop and compare predicted vs measured titer.
3. Document a reproducible workflow from design to data using a LIMS/ELN.
''',
        "references": [
            "https://ibiofoundry.illinois.edu/",
            "https://doi.org/10.1016/j.copbio.2025.103380",
            "https://doi.org/10.1016/j.copbio.2026.103503",
            "https://github.com/sblabkribb/biofoundry_workflows",
            "https://doi.org/10.3389/fsybi.2025.1630026",
        ],
    },
    {
        "name": "ai-for-rare-disease",
        "title": "AI for Rare Disease",
        "description": "AI for rare disease diagnosis, target prioritization, drug repurposing, natural history modeling, and diagnostic-odyssey support.",
        "devin_body": r'''
## When to use

You are diagnosing an undiagnosed patient, prioritizing drug targets, or building models for rare and ultra-rare diseases with limited data.

## Key concepts

- **Diagnostic odyssey**: long, multi-specialty path to a rare disease diagnosis.
- **Phenotype ontologies**: Human Phenotype Ontology (HPO) terms.
- **Small-sample ML**: transfer learning, federated learning, synthetic data.
- **Genotype-phenotype integration**: exome/variant + HPO matching.
- **Target prioritization**: genetic, functional, and literature evidence.
- **Drug repurposing for rare diseases**: identifying existing drugs for new rare indications.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# Rare disease diagnosis from HPO terms
hpo_df = pd.read_csv('hpo_patient_terms.csv')
vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(';'), lowercase=False)
X = vectorizer.fit_transform(hpo_df['hpo_terms'])
y = hpo_df['diagnosis']

clf = RandomForestClassifier(class_weight='balanced')
clf.fit(X, y)

# Predict top-3 differential diagnoses for a new patient
new_terms = 'HP:0001250;HP:0001263;HP:0002119'
proba = clf.predict_proba(vectorizer.transform([new_terms]))[0]
top3 = proba.argsort()[-3:][::-1]
print([clf.classes_[i] for i in top3])
```

## Tuning notes

- Rare classes are extremely imbalanced; use class weights, resampling, or ensembling.
- Combine HPO with variant features for multi-modal diagnosis.
- Transfer learning from common diseases can bootstrap rare-disease models.
- Validate on external case reports and prospective cases.
- Maintain explainability; clinicians need transparent reasoning.

## Verification

1. Train a top-k rare-disease classifier on HPO term profiles.
2. Add VCF variant features and measure gain in top-1/Recall@5.
3. Compare predictions against a clinical genetics pipeline such as Exomiser.
''',
        "references": [
            "https://raresource.nih.gov/",
            "https://doi.org/10.1038/s41586-025-10097-9",
            "https://github.com/MAGIC-AI4Med/DeepRare",
            "https://doi.org/10.1186/s13073-026-01671-5",
            "https://www.microsoft.com/en-us/research/publication/evidence-aggregator-ai-reasoning-applied-to-rare-disease-diagnostics/",
        ],
    },
    {
        "name": "ai-for-longevity",
        "title": "AI for Longevity",
        "description": "Biological aging clocks, biomarkers of aging, longevity intervention mining, and integrative multi-omic models of aging.",
        "devin_body": r'''
## When to use

You are estimating biological age, mining longevity interventions, or integrating multi-omic data to understand aging trajectories.

## Key concepts

- **Aging clocks**: predictors trained on DNA methylation, transcriptomics, proteomics, etc.
- **Biomarkers of aging**: clocks that correlate with mortality and morbidity.
- **Longevity interventions**: drugs, diet, and genetic manipulations that extend lifespan.
- **Multi-omic integration**: DNA methylation + RNA + metabolites + clinical labs.
- **Survival analysis**: Cox models, accelerated failure time.
- **Comparative biology**: cross-species aging mechanisms.

## Code pattern

```python
import anndata
import pyaging

# Load an anndata object with methylation CpGs as .var_names
adata = anndata.read_h5ad('methylation_betas.h5ad')

# Apply one or more aging clocks
adata = pyaging.predict._pred.predict_age(
    adata,
    clock_names=['horvath2013', 'hannum'],
    device='auto',
)
print(adata.obs[['horvath2013', 'hannum']].head())
```

## Tuning notes

- Choose a clock trained on the same tissue as your data.
- Missing CpG sites can be imputed from a reference; results are sensitive to imputation.
- Adjust for chronological age and confounders when evaluating intervention effects.
- Use longitudinal data to assess within-individual aging rate.
- Validate clocks against health outcomes, not just chronological age.

## Verification

1. Predict biological age with at least two clocks and compare correlation with chronological age.
2. Test whether a longevity intervention shifts predicted age in a cohort.
3. Reproduce one published aging clock from its original CpG list and beta coefficients.
''',
        "references": [
            "https://github.com/lucascamillomd/pyaging",
            "https://doi.org/10.1093/bioinformatics/btae200",
            "https://www.genomics.senescence.info/",
            "https://www.clockbase.org/",
            "https://gladyshevlab.org/mSALT/",
        ],
    },
    {
        "name": "ai-for-nutrition",
        "title": "AI for Nutrition",
        "description": "Machine learning and generative AI for personalized nutrition, dietary assessment, meal planning, food recognition, and nutrition-health modeling.",
        "devin_body": r'''
## When to use

You are building a personalized diet recommendation system, analyzing food intake, or predicting metabolic response from multi-modal data.

## Key concepts

- **Precision nutrition**: tailoring dietary advice to genetics, microbiome, metabolome, and lifestyle.
- **Dietary assessment**: food diaries, image-based food logging, automated nutrient estimation.
- **Food effect prediction**: postprandial glucose, insulin, and metabolite response.
- **Meal planning**: constraint optimization over nutrients, preferences, and costs.
- **Compositional data**: macronutrient ratios sum to 100%; use log-ratios or Dirichlet models.
- **Bias and equity**: cultural, socioeconomic, and access factors affect recommendations.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Predict postprandial glucose from meal composition and personal features
df = pd.read_csv('meals.csv')
features = ['carbs_g', 'fiber_g', 'protein_g', 'fat_g', 'bmi', 'fasting_glucose']
X = df[features]
y = df['glucose_2h_auc']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = RandomForestRegressor(n_estimators=200)
model.fit(X_train, y_train)

print('R2:', model.score(X_test, y_test))

# Feature importance
importance = pd.Series(model.feature_importances_, index=features)
print(importance.sort_values(ascending=False))
```

## Tuning notes

- Personalize with per-user random effects or meta-learning.
- Handle repeated measures and meal timing; food is episodic and context-dependent.
- Validate dietary logging against biomarkers (e.g., doubly labeled water) when possible.
- Use causal or quasi-experimental designs to claim health effects.
- Be cautious with LLM meal plans; ground advice in clinical guidelines.

## Verification

1. Train a model to predict a metabolic response from meal and participant data.
2. Compare a personalized vs one-size-fits-all model using per-user cross-validation.
3. Evaluate a meal recommendation engine against nutrient targets and user constraints.
''',
        "references": [
            "https://doi.org/10.1038/s41467-026-75004-w",
            "https://doi.org/10.1016/j.advnut.2025.100398",
            "https://doi.org/10.3390/nu18010045",
            "https://doi.org/10.3389/fnut.2025.1636980",
            "https://www.mdpi.com/2072-6643/18/6/938",
        ],
    },
    {
        "name": "ai-for-sleep",
        "title": "AI for Sleep",
        "description": "Machine learning for sleep staging, sleep disorder detection, wearable PSG analysis, and sleep health monitoring.",
        "devin_body": r'''
## When to use

You are analyzing polysomnography (PSG), wearable sleep recordings, or building a tool to detect sleep disorders and stages.

## Key concepts

- **Sleep stages**: W, N1, N2, N3, REM; scored from EEG/EOG/EMG.
- **PSG**: gold-standard overnight multi-channel recording.
- **Wearable sleep monitoring**: actigraphy, PPG, single-channel EEG headbands.
- **Sleep disorders**: obstructive sleep apnea, insomnia, narcolepsy, restless legs.
- **Sleep foundation models**: large-scale pre-training on PSG/EEG data.
- **Event detection**: apneas, hypopneas, arousals, limb movements.

## Code pattern

```python
import mne
import numpy as np
from scipy.signal import welch
from sklearn.ensemble import RandomForestClassifier

# Load an EDF and extract fixed-length epochs
raw = mne.io.read_raw_edf('sleep.edf', preload=True)
events = mne.make_fixed_length_events(raw, duration=30.0)
epochs = mne.Epochs(raw, events, tmin=0, tmax=30.0, baseline=None, preload=True)

# Extract band power features from one EEG channel
sfreq = raw.info['sfreq']
data = epochs.get_data()[:, 0, :]  # first EEG channel
f, psd = welch(data, fs=sfreq, nperseg=sfreq*2)

delta = psd[:, (f >= 0.5) & (f < 4)].mean(axis=1)
theta = psd[:, (f >= 4) & (f < 8)].mean(axis=1)
alpha = psd[:, (f >= 8) & (f < 13)].mean(axis=1)
features = np.column_stack([delta, theta, alpha])

# Train a simple sleep-stage model (labels needed)
clf = RandomForestClassifier(n_estimators=100)
# clf.fit(features, labels)
```

## Tuning notes

- Apply the AASM scoring rules as the reference standard.
- Handle class imbalance across sleep stages (N2 usually dominates).
- Use time context (adjacent epochs) to improve staging.
- Validate wearable models against concurrent PSG.
- Watch for channel mismatches across recording devices.

## Verification

1. Train a sleep-stage classifier on 30-s PSG epochs and compare to human scoring.
2. Extract delta/theta/alpha features and visualize their distribution by stage.
3. Evaluate a model on data from a different device/sensor.
''',
        "references": [
            "https://www.physionet.org/content/dreamt/2.2.0/",
            "https://yang-ai-lab.github.io/osf/",
            "https://doi.org/10.3390/bioengineering11030206",
            "https://link.springer.com/article/10.1186/s12911-025-03129-x",
            "https://www.nature.com/articles/s41746-025-02237-2",
        ],
    },
    {
        "name": "ai-for-digital-organism",
        "title": "AI for Digital Organism",
        "description": "Computational models, simulations, and multiscale foundation models of living systems as AI-driven digital organisms.",
        "devin_body": r'''
## When to use

You want to simulate evolution, cellular behavior, or multiscale biological systems in silico as an alternative to risky or expensive wet-lab experiments.

## Key concepts

- **Digital organisms**: self-replicating programs or agents that evolve in a virtual environment.
- **Artificial life (ALife)**: simulation of living systems and open-ended evolution.
- **Multiscale foundation models**: AIDO-style integration from molecules to organisms.
- **Agent-based models**: individuals interact, compete, and reproduce.
- **Genotype-phenotype maps**: how genotypic changes translate to phenotypes.
- **Evolutionary dynamics**: selection, mutation, drift, robustness, evolvability.

## Code pattern

```python
import numpy as np

# Conceptual grid-based digital ecosystem with four species
grid = np.random.randint(0, 4, (64, 64))

def propose_updates(grid, n_species=4):
    # Each species proposes a growth score for every cell
    return [np.random.rand(*grid.shape) + 0.1 * (grid == sp) for sp in range(n_species)]

def compete(proposals, grid):
    scores = np.stack(proposals)
    winner = scores.argmax(axis=0)
    # Keep current cell if its score is the highest
    return np.where(scores.max(axis=0) > 0.5, winner, grid)

for step in range(100):
    proposals = propose_updates(grid)
    grid = compete(proposals, grid)
    if step % 10 == 0:
        print('Step', step, 'dominant species:', np.bincount(grid.flat).argmax())
```

## Tuning notes

- Match simulation complexity to the question; simpler is better for hypothesis testing.
- Track phylogenies and fitness landscapes to understand evolvability.
- Reproducibility is critical; fix random seeds and log parameters.
- Use Parquet/standard formats for long-running simulation outputs.
- Compare digital-evolution results to known biological theory when possible.

## Verification

1. Evolve a population of digital organisms and plot diversity over time.
2. Reproduce a known evolutionary dynamics pattern (e.g., Muller plot, clonal interference).
3. Connect a digital-organism prediction to a wet-lab validation experiment.
''',
        "references": [
            "https://www.nature.com/articles/s41591-026-04595-0",
            "https://doi.org/10.48550/arxiv.2412.06993",
            "https://evochora.org/",
            "https://github.com/mauriceling/dose",
            "https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005414",
        ],
    },
    {
        "name": "ai-for-drug-repurposing",
        "title": "AI for Drug Repurposing",
        "description": "Graph ML, knowledge graphs, LLMs, and transcriptomics for identifying new indications for existing drugs.",
        "devin_body": r'''
## When to use

You want to find a new therapeutic use for an existing drug, rank candidates for a disease, or explain mechanistic rationale for off-label use.

## Key concepts

- **Drug repurposing (repositioning)**: finding new indications for approved drugs.
- **Knowledge graphs**: nodes for drugs, diseases, genes, pathways; edges for known relations.
- **Graph neural networks**: TxGNN and similar models for zero-shot indication prediction.
- **Signature matching**: match disease and drug transcriptomic signatures (e.g., LINCS, CMap).
- **Mechanistic grounding**: pathways, targets, and literature support.
- **Contraindications**: predicting when a repurposed drug is unsafe.

## Code pattern

```python
from txgnn import TxData, TxGNN, TxEval

# Load the TxGNN knowledge graph
tx_data = TxData('./data/')
txg = TxGNN(model='.', data=tx_data, weight_bias_save='./weights/')

# Predict indication for a disease
txg.predict(indications=True, drug='DRUG_NAME', disease='DISEASE_NAME')

# Generate a mechanistic explanation for the prediction
txg.explain('DRUG_NAME', 'DISEASE_NAME')
```

## Tuning notes

- Zero-shot models need diseases not seen during training for a fair test.
- Combine in silico predictions with real-world evidence (claims, EHR, trial data).
- Use graph explainability to build a mechanistic case for experimental follow-up.
- Filter by safety, contraindications, and pharmacokinetics.
- Prioritize drugs with known human safety data to de-risk trials.

## Verification

1. Run TxGNN or DrugKLM for a query disease and inspect top-ranked drugs.
2. Check whether top candidates have supporting literature in PubMed.
3. Compare GNN predictions to signature-matching results for the same disease.
''',
        "references": [
            "https://github.com/mims-harvard/TxGNN",
            "https://doi.org/10.1038/s41591-024-03233-x",
            "https://github.com/ncbi-nlp/DrugKLM",
            "https://doi.org/10.48550/arxiv.2604.19815",
            "https://github.com/SynDRep/SynDRep",
        ],
    },
]
