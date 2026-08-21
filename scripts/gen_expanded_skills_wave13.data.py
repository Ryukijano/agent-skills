SKILLS = [
    {
        "name": "ai-for-synthetic-biology",
        "title": "AI for Synthetic Biology",
        "description": "AI accelerates closed-loop Design-Build-Test-Learn cycles by predicting and optimizing genetic parts, pathways, and strains before they are built.",
        "devin_body": r'''
## When to use

You are engineering genetic circuits, optimizing promoters/RBSs, or automating a DBTL cycle for a synthetic biology project.

## Usage

- **Genetic-part prediction**: use regression and sequence models to score promoter, RBS, terminator, and coding-sequence activity in a chosen chassis.
- **DBTL acceleration**: close the Design-Build-Test-Learn loop by feeding assay data back into design models.
- **Pathway and strain optimization**: pick the next construct to build with active learning or Bayesian optimization.
- **Biological-constraint modeling**: account for chassis dependency, toxicity, genetic load, and context effects.
- **Assay interpretation**: apply ML to plate-reader, flow-cytometry, and proteomics outputs for phenotype calling.
- **Closed-loop biofoundry execution**: integrate predictions with robotic build and test workflows.

## Steps

1. Define the target function, host chassis, and constraints (titer, toxicity, genetic load).
2. Curate and encode genetic parts and historical part-activity data for that chassis.
3. Train predictive models for part activity, pathway flux, or strain phenotype.
4. Use active learning or Bayesian optimization to propose the next set of constructs.
5. Build and assay the proposed designs, then feed the measurements back into the model.
6. Validate top performers and transfer the best design to scaled production.

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
        "description": "Generate de novo binders and enzymes from target structures or reactions using inverse folding and diffusion models.",
        "devin_body": r'''
## When to use

You need a protein sequence for a fixed backbone, a de novo protein binder, or a new scaffold with specified structure or function.

## Usage

- **Inverse folding**: use ProteinMPNN or similar models to predict sequences for a fixed backbone.
- **Backbone generation**: design de novo scaffolds or binders around a target motif with RFdiffusion.
- **In silico validation**: refold designed sequences with AlphaFold2, ESMFold, or OpenFold and compute pLDDT/pAE/scRMSD.
- **Interface filtering**: rank candidates by interface pLDDT, pAE, shape complementarity, and hotspot residues.
- **Focused mutagenesis**: build stability or affinity libraries around promising designs.
- **Experimental triage**: move high-confidence binders to expression and biophysical assays (BLI, SPR, yeast display).

## Steps

1. Specify the target structure, epitope, or binding hotspot and the desired binder length/constraints.
2. Generate candidate backbones with RFdiffusion conditioned on the target motif or interface.
3. Design amino-acid sequences for each backbone using ProteinMPNN.
4. Refold designed sequences and compute self-consistency metrics (pLDDT, pAE, scRMSD, scTM).
5. Rank candidates by interface quality, hotspot coverage, and predicted expressability.
6. Express and validate top candidates with binding or activity assays (BLI, SPR, crystallography).

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
        "description": "Predict MHC-bound epitopes and vaccine candidates from receptor and omic data to prioritize immunotherapy and prophylaxis designs.",
        "devin_body": r'''
## When to use

You are analyzing B-cell or T-cell receptor repertoires, predicting epitope binding, or prioritizing vaccine/immunotherapy candidates.

## Usage

- **MHC/peptide prediction**: predict peptide presentation for class I and II alleles using MHCflurry/NetMHCpan.
- **AIRR analysis**: parse BCR/TCR clonotypes and link repertoire features to disease or response.
- **Receptor-antigen specificity**: model TCR/BCR recognition of epitopes and peptide-MHC complexes.
- **Vaccine and immunotherapy design**: select immunogens, map epitopes, and optimize mRNA or receptor constructs.
- **Immune-cell phenotyping**: classify cell types and states from flow, mass cytometry, or single-cell data.
- **Safety checking**: assess cross-reactivity, autoimmunity risk, and off-target binding of designed receptors.

## Steps

1. Gather peptide, MHC allele, receptor, or repertoire data and link them to the clinical question (vaccine, therapy, biomarker).
2. Predict peptide presentation and binding for candidate epitopes with allele-specific models.
3. Model TCR/BCR specificity using sequence, structure, or generative models (e.g., TCR-TRANSLATE, AlphaFold 3, HERMES).
4. Integrate immune repertoire and clinical labels to identify disease-associated clonotypes or cell states.
5. Prioritize vaccine epitopes or therapeutic receptors and check cross-reactivity and safety.
6. Validate with MHC multimer, ELISPOT, tetramer, or binding assays and refine the design.

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
        "description": "Decode speech and motor intent from electrocorticography to restore communication and movement via brain-computer interfaces.",
        "devin_body": r'''
## When to use

You are analyzing EEG, MEG, fMRI, calcium imaging, or spike data and want to decode neural states, detect biomarkers, or build NeuroAI models.

## Usage

- **Neural decoding**: predict cognitive states, movements, or stimuli from EEG, MEG, fMRI, or spike data.
- **Foundation models**: apply self-supervised models (DIVER-1, NeuroSTORM, AdaBrain) for cross-subject/cross-device representations.
- **Signal preprocessing**: use MNE, FSL, or AFNI to standardize, filter, and artifact-reject recordings.
- **Biomarker discovery**: identify neural signatures that correlate with disease, behavior, or treatment response.
- **Brain-computer interfaces**: build real-time decoders and map them to output devices or feedback.
- **Connectomics**: model structural and functional brain connectivity from imaging or electrophysiology.

## Steps

1. Choose the neural modality and task (e.g., sleep staging, motor BCI, naturalistic decoding) and curate datasets.
2. Preprocess signals: re-reference, filter, artifact-reject, and segment into epochs or trials.
3. Extract features (band power, spectrograms, connectivity) or load pretrained foundation-model embeddings.
4. Train a task-specific decoder with cross-subject or leave-one-subject validation.
5. Evaluate on held-out data and compare to expert or clinical annotations (accuracy, kappa, AUROC).
6. Deploy on the target hardware or device and validate in a real-time, closed-loop setting.

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
        "description": "Match patients to genotype-tailored therapies and clinical trials by integrating EHR, genomic, and biomarker data.",
        "devin_body": r'''
## When to use

You need to build a personalized risk model, recommend therapy, integrate multi-omic and clinical data, or stratify patients for a trial.

## Usage

- **Multi-modal integration**: fuse genomics, EHR, imaging, wearable, and lab data into a unified patient representation.
- **Treatment matching**: predict response, toxicity, or resistance to guide therapy selection.
- **Risk stratification**: estimate survival, progression, or adverse-event risk with time-to-event models.
- **Biomarker discovery**: find predictive, prognostic, or pharmacodynamic markers across cohorts.
- **Federated learning**: train models across institutions while keeping patient data local.
- **Clinical explainability**: audit models for bias and align predictions with clinical guidelines.

## Steps

1. Define the clinical decision (diagnosis, risk, or therapy response) and the relevant modalities.
2. Harmonize multi-omic, imaging, and clinical data; handle missing values, batch effects, and site differences.
3. Train a multimodal model (deep fusion, graph, or survival) with time-split or external validation.
4. Evaluate predictive performance and calibration on an external cohort.
5. Interpret model outputs with SHAP, attention, or feature importance and compare with clinical knowledge.
6. Deploy as decision support and monitor for distribution drift, bias, and changing practice patterns.

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
        "description": "Combine robotic automation, LIMS, and active learning to run closed-loop Design-Build-Test-Learn campaigns at scale.",
        "devin_body": r'''
## When to use

You are running high-throughput synthetic biology experiments in a biofoundry, automating liquid handling, or closing the DBTL loop with predictive models.

## Usage

- **Robotic execution**: use liquid-handling robots, plate readers, and bioreactors to build and assay designs at scale.
- **DBTL automation**: run Design-Build-Test-Learn cycles with minimal human intervention.
- **Self-driving labs**: let active-learning agents propose and schedule the next experiments.
- **Workflow abstraction**: encode protocols as unit operations and reusable workflows in a LIMS/scheduler.
- **Surrogate/digital-twin modeling**: predict titers, yields, or activity from process parameters.
- **FAIR data capture**: link samples, designs, and results through metadata, barcodes, and programmable APIs.

## Steps

1. Define the workflow (e.g., strain construction, enzyme screening, medium optimization) and map unit operations.
2. Encode protocols for robotic liquid handling, incubation, and analytical instruments in a LIMS/scheduler.
3. Run an initial design-of-experiments or active-learning batch to generate a training set.
4. Train surrogate models from instrument outputs (titers, fluorescence, growth) and process features.
5. Use Bayesian optimization to propose the next physical constructs to build and test.
6. Analyze results, update the model, and scale the best-performing designs.

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
        "description": "Integrate phenotypes, genotypes, and medical literature to shorten the diagnostic odyssey and prioritize rare-disease candidates.",
        "devin_body": r'''
## When to use

You are diagnosing an undiagnosed patient, prioritizing drug targets, or building models for rare and ultra-rare diseases with limited data.

## Usage

- **Phenotype-driven diagnosis**: match HPO terms, clinical notes, and images to rare-disease knowledge bases.
- **Genotype-phenotype integration**: combine exome/variant data with phenotype matching for gene/disease ranking.
- **Small-sample learning**: apply transfer learning, federated learning, or synthetic data to limited rare-disease cohorts.
- **Literature synthesis**: use ML or LLM tools to surface disease-gene evidence from PubMed and case reports.
- **Target and therapy prioritization**: rank candidate genes, pathways, or repurposed drugs for rare diseases.
- **Explainable differential diagnosis**: produce transparent, clinician-reviewable reasoning for each candidate.

## Steps

1. Assemble patient phenotypes (HPO terms, free text, imaging) and genomic variants (VCF/Exomiser).
2. Embed and match phenotypes to disease and gene knowledge bases plus primary literature.
3. Rank candidate diagnoses or genes using ML or LLM-based reasoning.
4. Integrate genotype evidence (pathogenicity, inheritance, allele frequency) with phenotype concordance.
5. Generate an explainable differential diagnosis with literature links for expert adjudication.
6. Validate against external case series, reanalysis, or functional studies.

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
        "description": "Estimate biological age and discover longevity interventions by applying epigenetic clocks and multi-omic aging models to molecular data.",
        "devin_body": r'''
## When to use

You are estimating biological age, mining longevity interventions, or integrating multi-omic data to understand aging trajectories.

## Usage

- **Biological-age estimation**: apply DNA methylation, transcriptomic, or proteomic clocks to estimate biological age.
- **Aging-biomarker discovery**: identify clocks and EpiScores that correlate with mortality, frailty, or disease risk.
- **Intervention mining**: screen public molecular compendia for drugs, diets, or genetic manipulations that modify biological age.
- **Multi-omic integration**: combine DNA methylation, RNA, metabolites, and clinical lab data.
- **Longitudinal tracking**: use repeated measures to assess within-individual aging trajectories.
- **Outcome validation**: test clock predictions against survival, health outcomes, or experimental models.

## Steps

1. Select the tissue/cell type and aging clock(s) appropriate for the biological question (e.g., Horvath, GrimAge, PhenoAge, DunedinPACE).
2. Preprocess and impute missing CpGs or features against a reference panel.
3. Compute biological age and residualized age-acceleration scores for each sample.
4. Correlate predicted age with interventions, exposures, or health outcomes in longitudinal or cross-sectional data.
5. Use systematic reanalysis or knowledge-graph tools to mine candidate geroprotective interventions.
6. Validate top candidates in independent cohorts or experimental models and update the clock as needed.

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
        "description": "Predict personal metabolic responses and automate dietary assessment to deliver personalized nutrition and meal planning.",
        "devin_body": r'''
## When to use

You are building a personalized diet recommendation system, analyzing food intake, or predicting metabolic response from multi-modal data.

## Usage

- **Postprandial response prediction**: predict personal glucose, insulin, or metabolite responses from meals and participant features.
- **Image-based dietary assessment**: recognize foods and estimate portions/nutrients from photos using computer vision or multimodal LLMs.
- **Personalized meal planning**: optimize menus against nutrient targets, preferences, costs, and health constraints.
- **Diet-health modeling**: link dietary intake, microbiome, metabolome, and clinical outcomes.
- **Compositional-data handling**: respect macronutrient sum-to-one with log-ratios or Dirichlet models.
- **Equity-aware recommendations**: account for cultural, socioeconomic, and access factors in advice.

## Steps

1. Collect multimodal input (food logs/images, CGM, anthropometrics, microbiome, blood markers).
2. Standardize and clean dietary data: meal timing, portion estimation, and macronutrient content.
3. Train a personalized PPGR or nutrient model with per-user features and cross-validation.
4. Generate personalized meal or diet recommendations by ranking predicted metabolic responses.
5. Validate predictions against continuous glucose monitoring, doubly labeled water, or clinical biomarkers.
6. Run a dietary intervention trial and compare glycemic/metabolic outcomes to standard advice.

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
        "description": "Automate sleep staging and sleep-disordered-breathing detection from PSG, wearables, and home sleep tests with deep learning.",
        "devin_body": r'''
## When to use

You are analyzing polysomnography (PSG), wearable sleep recordings, or building a tool to detect sleep disorders and stages.

## Usage

- **Sleep staging**: score 30-second epochs into W, N1, N2, N3, and REM from PSG, wearables, or EEG headbands.
- **Sleep-disordered-breathing detection**: detect and classify apneas, hypopneas, and arousals.
- **AHI estimation**: estimate apnea-hypopnea index and severity from oximetry, PPG, or other sensors.
- **Foundation models**: pre-train on large PSG/EEG corpora for cross-cohort and cross-device transfer.
- **Event-level analysis**: identify arousals, limb movements, and respiratory events with precise timing.
- **Clinical validation**: compare wearable or automated scoring to AASM expert-annotated PSG.

## Steps

1. Collect and annotate PSG or wearable recordings following AASM scoring rules.
2. Preprocess signals (filter, resample, align modalities) and create 30-second epochs with context windows.
3. Train a temporal/sequence model (CNN, ResNet+TCN+LSTM, Mamba, or transformer) for staging or event detection.
4. Evaluate against expert annotators using epoch/stage agreement (Cohen's kappa, AUROC, AUPRC).
5. Validate on external cohorts and compare wearable-only models to gold-standard PSG.
6. Deploy for home sleep testing or clinical decision support with nightly risk reports.

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
        "description": "Build multiscale AI models that simulate living systems from molecules to organisms to guide biology and medicine in silico.",
        "devin_body": r'''
## When to use

You want to simulate evolution, cellular behavior, or multiscale biological systems in silico as an alternative to risky or expensive wet-lab experiments.

## Usage

- **Multiscale simulation**: integrate DNA, RNA, protein, cell, and phenotype models across biological scales.
- **In silico perturbation**: predict the effects of mutations, drugs, or environmental changes at multiple levels.
- **Evolutionary simulation**: study selection, mutation, drift, robustness, and evolvability in digital organisms.
- **Agent-based modeling**: simulate individuals that interact, compete, and reproduce.
- **AIDO-style workflows**: use YAML-driven frameworks to assemble and benchmark component foundation models.
- **Wet-lab guidance**: compare in silico predictions to first-principles biology and targeted experiments.

## Steps

1. Define the biological scale and question (molecular, cellular, tissue, organism, or population).
2. Assemble multimodal training data (sequences, structures, omics, images, phenotypes, spatial-temporal data).
3. Select or pretrain component foundation models for each modality and scale.
4. Integrate models via hierarchical representation propagation, nested fine-tuning, or cross-scale links.
5. Run in silico perturbation or simulation experiments and compare outcomes to known biology.
6. Validate key predictions with targeted wet-lab experiments and iterate the multiscale model.

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
        "description": "Predict new indications for existing drugs by reasoning over biomedical knowledge graphs and transcriptomic signatures.",
        "devin_body": r'''
## When to use

You want to find a new therapeutic use for an existing drug, rank candidates for a disease, or explain mechanistic rationale for off-label use.

## Usage

- **Knowledge-graph reasoning**: use GNNs (e.g., TxGNN) to rank drug-disease indications and contraindications.
- **Transcriptomic signature matching**: match drug-perturbation and disease expression profiles (LINCS, CMap).
- **Real-world evidence integration**: combine in silico predictions with EHR, claims, or trial data.
- **Mechanistic explanation**: generate multi-hop graph paths or literature rationales for a prediction.
- **Safety filtering**: flag contraindications, adverse events, and pharmacokinetic concerns.
- **Candidate triage**: prioritize approved drugs with known human safety for faster experimental validation.

## Steps

1. Build or load a biomedical knowledge graph (diseases, drugs, genes, pathways) and/or a transcriptomic compendium.
2. Train or apply a graph/Siamese model to embed drugs and diseases (e.g., TxGNN, RPath, CellAwareGNN).
3. For a query disease, retrieve top drug candidates and compute indication and contraindication scores.
4. Cross-check candidates against opposing transcriptomic signatures and supporting literature.
5. Generate multi-hop mechanistic explanations and prioritize by safety and contraindication profiles.
6. Validate in cell or animal models, retrospective EHR, or clinical-trial registries.

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
