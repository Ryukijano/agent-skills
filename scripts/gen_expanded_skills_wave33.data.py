SKILLS = [
    {
        "name": "ai-for-digital-health",
        "title": "AI for Digital Health",
        "description": "Consumer-facing health apps, wearable biosensors, remote monitoring, patient portals, and data-driven digital wellness interventions.",
        "devin_body": r'''## When to use

You are building or evaluating consumer-facing digital health tools, integrating wearable or sensor data, or conducting remote monitoring and digital-biomarker studies.

## Key concepts

- **mHealth and digital biomarkers**: smartphone apps, wearables, and connected sensors that capture physiology and behavior.
- **Remote patient monitoring and digital clinical trials**: decentralized data collection, telehealth integration, and virtual trial endpoints.
- **Wearable signal processing**: PPG, accelerometry, sleep staging, and activity recognition from consumer devices.
- **Digital phenotyping and ecological momentary assessment**: in-situ, high-frequency behavioral and symptom measurement.
- **Regulatory and evidence standards**: FDA 510(k)/De Novo, Digital Health Software Precertification, and clinical-validation requirements.

## Code pattern

```python
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

# Heart-rate peaks from a wearable PPG signal
peaks, _ = find_peaks(ppg_signal, distance=50)
hr = 60 * fs / np.diff(peaks)
```

## Tuning notes

- Validate against reference devices and clinical measurements; sensor placement and motion artifacts matter.
- Protect privacy of continuous, fine-grained behavioral and physiological data.
- Distinguish wellness claims from regulated medical-device claims.
- Use time-series cross-validation because wearables generate streaming, autocorrelated data.

## Verification

1. Extract a digital biomarker from wearable data and compare it to a clinical gold standard.
2. Build a remote-monitoring dashboard with anomaly alerts for a simulated cohort.
3. Assess class balance and subgroup calibration for a digital health risk model.
''',
        "references": [
            "https://doi.org/10.1038/s41591-021-01614-0",
            "https://doi.org/10.1038/s41591-022-01981-2",
            "https://doi.org/10.1038/s41591-018-0307-0",
            "https://doi.org/10.1038/s41591-026-04229-5",
        ],
    },
    {
        "name": "ai-for-health-informatics",
        "title": "AI for Health Informatics",
        "description": "Electronic health records, clinical data standards, interoperability, and AI-enabled analytics for healthcare delivery and research.",
        "devin_body": r'''## When to use

You need to structure, integrate, and analyze healthcare data across systems using standards such as HL7 FHIR, OMOP, and LOINC.

## Key concepts

- **Health data standards and interoperability**: HL7 FHIR, OMOP CDM, DICOM, and terminologies such as SNOMED-CT, ICD, RxNorm, and LOINC.
- **EHR phenotyping and clinical data warehouses**: extracting computable cohorts and longitudinal patient features.
- **Natural language processing for clinical text**: named-entity recognition, entity normalization, de-identification, and information extraction.
- **Clinical decision support and alert systems**: rules-based and ML-driven recommendations embedded in workflows.
- **Privacy, security, and governance**: HIPAA, GDPR, de-identification, and role-based access control.

## Code pattern

```python
import pandas as pd

# Flatten FHIR Observation resources from a Bundle
observations = [
    r['resource'] for r in bundle['entry']
    if r['resource']['resourceType'] == 'Observation'
]
df = pd.json_normalize(observations)
```

## Tuning notes

- Normalize terminologies before modeling and reconcile conflicting code systems.
- Handle missing, longitudinal, and irregularly sampled EHR data.
- Avoid label leakage from future encounters; use time-split validation.
- Audit for bias across sites, documentation practices, and patient populations.

## Verification

1. Extract a computable phenotype from EHR data and compare it to manual chart review.
2. Map free-text diagnoses to ICD/SNOMED-CT codes with an NLP pipeline.
3. Evaluate a predictive model with temporal cross-validation across hospitals.
''',
        "references": [
            "https://doi.org/10.1093/jamia/ocae074",
            "https://doi.org/10.1093/jamia/ocac095",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11700560/",
            "https://doi.org/10.1093/jamia/ocaf131",
        ],
    },
    {
        "name": "ai-for-behavioral-science",
        "title": "AI for Behavioral Science",
        "description": "Computational modeling of human behavior, n-of-1 and ecological momentary assessment, digital interventions, and experimentally validated behavior change.",
        "devin_body": r'''## When to use

You are studying or influencing human behavior using digital experiments, sensor data, reinforcement learning, or generative models of behavior.

## Key concepts

- **Behavioral experiments and A/B testing**: randomized and within-subject designs for digital interventions.
- **Ecological momentary assessment (EMA) and digital phenotyping**: in-the-moment, repeated measurements in natural environments.
- **N-of-1 trials and personalized intervention optimization**: single-participant designs and adaptive optimization.
- **Computational psychiatry and reinforcement learning models of choice**: model-based and model-free learning, drift-diffusion, and reward models.
- **Causal and mechanistic behavior-change frameworks**: identifying drivers and mediators of behavior change.

## Code pattern

```python
import pandas as pd
import statsmodels.api as sm

# Estimate treatment effect in an n-of-1 crossover trial
df['period'] = (df['day'] // n).astype(int)
X = sm.add_constant(df[['treatment', 'period', 'day']])
model = sm.OLS(df['outcome'], X).fit()
print(model.params['treatment'])
```

## Tuning notes

- Behavioral data is noisy and context-dependent; model within-person dynamics.
- Use causal inference (fixed effects, synthetic control) for observational behavior data.
- Replicate and pre-register digital experiments.
- Respect participant autonomy and informed consent in EMA studies.

## Verification

1. Analyze an EMA dataset to detect triggers of a target behavior.
2. Design and simulate an n-of-1 adaptive intervention.
3. Evaluate a behavior-change chatbot against a control in a randomized pilot.
''',
        "references": [
            "https://www.sciencedirect.com/science/article/abs/pii/S2352250X24000484",
            "https://link.springer.com/article/10.1007/s10462-025-11297-5",
            "https://link.springer.com/article/10.1038/s44159-026-00551-4",
            "https://www.sciencedirect.com/science/article/abs/pii/S2352250X2400085X",
        ],
    },
    {
        "name": "ai-for-cognitive-science",
        "title": "AI for Cognitive Science",
        "description": "Computational models of perception, memory, language, reasoning, and human-like cognition, bridging AI and psychological theory.",
        "devin_body": r'''## When to use

You want to build or evaluate computational models of human cognition, compare AI behavior to human data, or use AI as a model organism for cognitive theory.

## Key concepts

- **Computational modeling of perception, memory, and decision-making**: symbolic, Bayesian, and neural-network cognitive models.
- **Cognitive architectures**: ACT-R, SOAR, and subsymbolic neural models of cognition.
- **Psychophysical and behavioral experiments**: linking model predictions to human measurements.
- **Large language models as cognitive models**: evaluating emergent reasoning, semantic processing, and language production.
- **Symbolic versus subsymbolic representations**: trade-offs between interpretability and scalability.

## Code pattern

```python
import torch
from transformers import AutoModel, AutoTokenizer

# Compare LLM next-token probabilities to human cloze responses
tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
model = AutoModel.from_pretrained("openai-community/gpt2", output_hidden_states=True)
inputs = tokenizer("The cat sat on the ___", return_tensors="pt")
outputs = model(**inputs)
```

## Tuning notes

- Match training scale and stimuli to human experience for valid comparisons.
- Use likelihood, reaction time, and error-pattern metrics, not just accuracy.
- Distinguish performance from competence and test out-of-distribution generalization.
- Combine top-down theory with bottom-up model fits.

## Verification

1. Fit a cognitive model to a choice-reaction-time dataset and recover parameters.
2. Compare LLM and human predictions on a semantic reasoning task.
3. Probe a neural network for symbolic compositionality and report failure modes.
''',
        "references": [
            "https://doi.org/10.1146/annurev-psych-030625-040748",
            "https://www.nature.com/articles/s41593-018-0210-5",
            "https://doi.org/10.15212/bioi-2025-0199",
            "https://www.cambridge.org/core/books/cambridge-handbook-of-computational-cognitive-sciences/2713AC0C8AC0B0F2B9E97DB010813883",
        ],
    },
    {
        "name": "ai-for-neuroinformatics",
        "title": "AI for Neuroinformatics",
        "description": "Data science for brain imaging, neural signals, connectomics, and computational neuroscience workflows.",
        "devin_body": r'''## When to use

You are integrating, analyzing, or sharing large-scale neuroscience data such as neuroimaging, electrophysiology, genomics, and connectomics.

## Key concepts

- **Neuroimaging data formats and pipelines**: NIfTI, CIFTI, BIDS, and tools such as fMRIPrep and FreeSurfer.
- **Electrophysiology and calcium imaging analysis**: spike sorting, local field potentials, and time-series neural data.
- **Brain connectomics and network neuroscience**: structural and functional connectivity, graph theory, and network dynamics.
- **Open neuroscience data repositories and standards**: OpenNeuro, NeuroVault, and data-sharing conventions.
- **Multimodal fusion of neural, genetic, and behavioral data**: integrating across scales and modalities.

## Code pattern

```python
import nibabel as nib
from nilearn import datasets, plotting

# Load and plot a functional brain atlas
atlas = datasets.fetch_atlas_harvard_oxford('cort-maxprob-thr25-2mm')
atlas_img = nib.load(atlas.maps)
plotting.plot_roi(atlas_img, title="Harvard-Oxford Atlas")
```

## Tuning notes

- Use BIDS for data organization and reproducibility.
- Correct for multiple comparisons and control false positives in neuroimaging.
- Report effect sizes and confidence intervals, not just p-values.
- Share preprocessed data and code through open repositories.

## Verification

1. Preprocess an fMRI dataset and derive a group-level connectivity matrix.
2. Train a classifier to decode a cognitive state from EEG or fMRI data.
3. Publish a BIDS-organized dataset and analysis pipeline on an open repository.
''',
        "references": [
            "https://doi.org/10.1007/s12021-024-09692-4",
            "https://doi.org/10.3390/jcm14020550",
            "https://doi.org/10.1016/j.metrad.2026.100224",
            "https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2024.1399931/full",
        ],
    },
    {
        "name": "ai-for-cancer-bioinformatics",
        "title": "AI for Cancer Bioinformatics",
        "description": "Multi-omics integration, tumor subtyping, biomarker discovery, and precision oncology using AI.",
        "devin_body": r'''## When to use

You are analyzing cancer genomics, transcriptomics, proteomics, pathology images, or clinical data to identify biomarkers or guide oncology decisions.

## Key concepts

- **Multi-omics data integration**: genomics, transcriptomics, epigenomics, proteomics, and metabolomics for a holistic tumor view.
- **Tumor classification and subtyping**: molecular subtypes, histology, and consensus clustering.
- **Somatic mutation and copy-number analysis**: driver mutations, mutational signatures, and tumor heterogeneity.
- **Pathology image and radiomics analysis**: whole-slide imaging and quantitative imaging features.
- **Immunotherapy and targeted-therapy response prediction**: biomarkers such as tumor mutational burden and microsatellite instability.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Predict molecular subtype from multi-omics features
X = df[['gene_exp_pc1', 'mutational_burden', 'cnv_score', 'tmb']]
y = df['molecular_subtype']
model = RandomForestClassifier(class_weight='balanced', random_state=42).fit(X, y)
```

## Tuning notes

- Account for tumor heterogeneity and microenvironment.
- Use cross-study and external validation; avoid leakage from molecular profiles.
- Handle high dimensionality, batch effects, and missing omics.
- Interpret models for biological plausibility and clinical actionability.

## Verification

1. Integrate two omics layers and cluster tumor samples into subtypes.
2. Predict survival or treatment response and validate on an external cohort.
3. Identify top biomarkers and check consistency with known cancer pathways.
''',
        "references": [
            "https://doi.org/10.1016/bs.acr.2024.06.005",
            "https://bmjoncology.bmj.com/content/3/1/e000134",
            "https://link.springer.com/article/10.1186/s13073-024-01315-6",
            "https://www.mdpi.com/2072-6694/16/13/2448",
        ],
    },
    {
        "name": "ai-for-immunoinformatics",
        "title": "AI for Immunoinformatics",
        "description": "Machine learning for immune repertoire analysis, epitope prediction, vaccine design, and immunotherapy optimization.",
        "devin_body": r'''## When to use

You are working with immune sequencing, epitope prediction, vaccine design, or predicting response to immunotherapy.

## Key concepts

- **B-cell and T-cell receptor repertoire analysis**: V(D)J recombination, clonality, and diversity metrics.
- **MHC/peptide binding and epitope prediction**: prediction of immunogenic peptides and antigen presentation.
- **Antigen specificity and immunogenicity modeling**: TCR/pMHC and BCR/antigen interaction prediction.
- **Single-cell immunoprofiling and spatial transcriptomics**: immune-cell states and tissue microenvironment.
- **Vaccine and immunotherapy design**: CAR-T, checkpoint inhibitors, and personalized cancer vaccines.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Predict peptide-MHC binding from sequence features
X = df[['peptide_length', 'hydrophobicity', 'anchor_positions']]
y = df['binder']
model = GradientBoostingClassifier().fit(X, y)
```

## Tuning notes

- Use well-curated epitope databases (IEDB) and cross-allele validation.
- Immune data is highly diverse; control for HLA and species differences.
- Combine sequence and structural features for binding prediction.
- Validate predicted epitopes with experimental binding assays when possible.

## Verification

1. Train an epitope predictor and evaluate per-allele AUC on a held-out set.
2. Analyze a single-cell immune-repertoire dataset to identify clonal expansions.
3. Compare predicted immunogenic peptides to experimental IEDB assay data.
''',
        "references": [
            "https://doi.org/10.71373/saov9257",
            "https://doi.org/10.1038/s41592-024-02351-1",
            "https://www.annualreviews.org/content/journals/10.1146/annurev-chembioeng-101420-125021",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC7108239/",
        ],
    },
    {
        "name": "ai-for-clinical-informatics",
        "title": "AI for Clinical Informatics",
        "description": "AI-enabled clinical decision support, EHR integration, workflow optimization, and evaluation in real-world care settings.",
        "devin_body": r'''## When to use

You are building, deploying, or evaluating AI tools inside clinical workflows, such as decision support, risk scores, or automated alerts.

## Key concepts

- **Clinical decision support systems (CDSS) and human-AI teaming**: alerts, order sets, and recommendations embedded in the EHR.
- **EHR integration, FHIR, and interoperability**: deploying models within existing clinical information systems.
- **Risk prediction, triage, and prognostic models**: early warning, deterioration, and readmission scores.
- **Implementation science and workflow integration**: adoption, usability, and clinical workflow redesign.
- **Safety, fairness, and continuous monitoring of clinical AI**: drift, alert fatigue, and health-equity audits.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import TimeSeriesSplit

# Temporal validation for an inpatient deterioration model
X = df[['vitals_last_4h', 'labs', 'comorbidity_score']]
y = df['deterioration_24h']
for train_idx, test_idx in TimeSeriesSplit(n_splits=3).split(X):
    model = GradientBoostingClassifier().fit(X.iloc[train_idx], y.iloc[train_idx])
    y_pred = model.predict_proba(X.iloc[test_idx])[:, 1]
```

## Tuning notes

- Validate using chronological splits and external sites.
- Integrate with clinician workflow; avoid alert fatigue and over-trust.
- Monitor for performance drift and distributional shift.
- Address fairness across race, sex, age, and socioeconomic groups.

## Verification

1. Build a clinical risk model and evaluate with time-split and site-split validation.
2. Design a decision-support interface and gather clinician usability feedback.
3. Deploy a drift monitor on model inputs and outputs in a simulated EHR stream.
''',
        "references": [
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC10751141/",
            "https://medinform.jmir.org/2023/1/e48297",
            "https://journals.plos.org/digitalhealth/article?id=10.1371%2Fjournal.pdig.0000514",
            "https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1550731/full",
        ],
    },
    {
        "name": "ai-for-health-economics",
        "title": "AI for Health Economics",
        "description": "Cost-effectiveness, health technology assessment, demand and pricing models, and machine learning for health outcomes research.",
        "devin_body": r'''## When to use

You are evaluating the economic value, cost-effectiveness, or budget impact of health technologies and interventions using ML.

## Key concepts

- **Health economic evaluation**: cost-effectiveness, cost-utility, and budget-impact analysis.
- **Health technology assessment (HTA) and pricing**: value frameworks and reimbursement decisions.
- **Causal inference for treatment effects and policy evaluation**: observational methods and quasi-experiments.
- **Real-world evidence and claims data analysis**: large administrative and EHR datasets for economic outcomes.
- **Equity and distributional cost-effectiveness analysis**: trade-offs across population groups.

## Code pattern

```python
import numpy as np

# Compute incremental cost-effectiveness ratio (ICER)
delta_cost = mean_cost_new - mean_cost_standard
delta_qaly = mean_qaly_new - mean_qaly_standard
icer = delta_cost / delta_qaly
print("ICER:", icer)
```

## Tuning notes

- Align cost and outcome perspectives (payer, societal, health system).
- Use bootstrapping or probabilistic sensitivity analysis for uncertainty.
- Account for treatment selection bias with propensity scores or instrumental variables.
- Report incremental net health benefit and cost-effectiveness acceptability curves.

## Verification

1. Replicate a cost-effectiveness analysis with bootstrapped confidence intervals.
2. Estimate a causal treatment effect from observational claims data.
3. Build an acceptability curve and compare it to a cost-effectiveness threshold.
''',
        "references": [
            "https://doi.org/10.1016/j.jval.2026.01.014",
            "https://link.springer.com/article/10.1186/s13561-025-00645-4",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11786987/",
            "https://doi.org/10.1016/j.jval.2023.09.2123",
        ],
    },
    {
        "name": "ai-for-precision-public-health",
        "title": "AI for Precision Public Health",
        "description": "Subpopulation-targeted prevention, genomics-guided public health, geospatial risk modeling, and equitable intervention targeting.",
        "devin_body": r'''## When to use

You are designing data-driven public health interventions that tailor prevention, screening, or resource allocation to specific populations or contexts.

## Key concepts

- **Precision public health and stratified prevention**: delivering the right intervention to the right population at the right time.
- **Genomics, exposomics, and social determinants of health integration**: layered risk modeling.
- **Geospatial and spatiotemporal risk modeling**: identifying local disease clusters and hotspots.
- **Targeted intervention allocation and microplanning**: prioritizing communities, facilities, or individuals under constraints.
- **Equity, ethics, and community engagement**: avoiding stigma and ensuring fair distribution of benefits.

## Code pattern

```python
import geopandas as gpd
from sklearn.ensemble import GradientBoostingRegressor

# Predict local disease risk and rank areas for intervention
X = gdf[['socioeconomic_index', 'environmental_score', 'demographic_pct']]
gdf['risk_score'] = model.predict(X)
priority_areas = gdf.sort_values('risk_score', ascending=False).head(20)
```

## Tuning notes

- Avoid stereotyping or stigmatizing communities with risk scores.
- Combine public-health surveillance with genomic, environmental, and social data.
- Use causal or quasi-experimental designs to estimate intervention impacts.
- Prioritize health equity and community trust over pure predictive accuracy.

## Verification

1. Build a subpopulation risk model and audit for geographic and demographic fairness.
2. Simulate targeted versus universal intervention allocation under a budget constraint.
3. Evaluate equity metrics before and after deploying a precision prevention strategy.
''',
        "references": [
            "https://www.nature.com/articles/s41591-024-03098-0",
            "https://doi.org/10.1159/000538141",
            "https://link.springer.com/article/10.1186/s40537-025-01201-x",
            "https://publichealth.jmir.org/2025/1/e68952",
        ],
    },
    {
        "name": "ai-for-global-health",
        "title": "AI for Global Health",
        "description": "AI for disease burden, healthcare systems, and health equity in low- and middle-income countries and resource-limited settings.",
        "devin_body": r'''## When to use

You are designing or evaluating AI for health challenges in global or resource-limited settings, with a focus on equity, access, and implementation.

## Key concepts

- **Global health equity and context-specific validation**: performance, acceptability, and fairness in diverse settings.
- **Low-resource deployment, mobile health, and task shifting**: point-of-care and community health tools.
- **Open data, data sovereignty, and local capacity building**: community-owned data and workforce development.
- **AI for tropical and neglected diseases, maternal/child health, and outbreak response**: priority conditions in LMICs.
- **Implementation and cost-effectiveness in LMICs**: real-world evidence and scalability.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Portable triage model for a low-resource clinic
features = ['fever', 'cough', 'respiratory_rate', 'oxygen_saturation', 'age']
X = df[features]
y = df['referral_needed']
model = RandomForestClassifier(class_weight='balanced').fit(X, y)
```

## Tuning notes

- Co-design with local clinicians and communities; respect data sovereignty.
- Validate on local devices, connectivity, and infrastructure constraints.
- Consider fairness across geography, language, and health-system tier.
- Evaluate cost-effectiveness and scalability relative to standard care.

## Verification

1. Validate a diagnostic or triage model on data from the target country or region.
2. Assess model performance across facility types and demographic groups.
3. Estimate cost-effectiveness and implementation feasibility in a local health system.
''',
        "references": [
            "https://annalsofglobalhealth.org/articles/10.5334/aogh.5268",
            "https://doi.org/10.1016/s0140-6736(20)30226-9",
            "https://doi.org/10.1038/s41746-022-00700-y",
            "https://doi.org/10.1016/S2214-109X(25)00473-5",
        ],
    },
    {
        "name": "ai-for-health-services-research",
        "title": "AI for Health Services Research",
        "description": "AI for healthcare access, quality, utilization, policy, workforce, and health-system performance.",
        "devin_body": r'''## When to use

You are studying healthcare delivery, access, quality, utilization, or policy using observational data and machine learning.

## Key concepts

- **Health services research methods and quasi-experimental designs**: difference-in-differences, regression discontinuity, and interrupted time series.
- **Healthcare utilization, access, and disparities**: inpatient, outpatient, emergency, and preventive service use.
- **Quality measurement and patient safety**: readmissions, adverse events, and process-of-care metrics.
- **Health policy and economic evaluation**: policy impact, HTA, and resource allocation.
- **Machine learning for evidence synthesis and health system optimization**: systematic review automation and operations research.

## Code pattern

```python
import pandas as pd
import statsmodels.formula.api as smf

# Difference-in-differences evaluation of a policy on hospital utilization
model = smf.ols('utilization ~ treatment_post + treatment + post + controls', data=df).fit()
print(model.params['treatment_post'])
```

## Tuning notes

- Use appropriate causal designs for policy and implementation studies.
- Address confounding and selection bias in observational claims or EHR data.
- Measure outcomes that matter to patients and health systems.
- Interpret findings for policy action and implementation feasibility.

## Verification

1. Evaluate a healthcare policy change using a difference-in-differences design.
2. Predict hospital readmissions and identify modifiable utilization drivers.
3. Map AI implementation barriers from a mixed-methods health services study.
''',
        "references": [
            "https://link.springer.com/article/10.1186/s12913-025-12664-2",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC9582911/",
            "https://link.springer.com/article/10.1186/s12913-023-10462-2",
            "https://www.ncbi.nlm.nih.gov/books/NBK620201/",
        ],
    },
]
