SKILLS = [
    {
        "name": "ai-for-longitudinal-studies",
        "title": "AI for Longitudinal Studies",
        "description": "Model repeated measurements over time to track disease progression, treatment response, and biomarker trajectories.",
        "devin_body": r'''## When to use

You are analyzing repeated observations over time, predicting future trajectories, or handling attrition and irregular sampling in longitudinal health, social, or behavioral data.

## Usage

- Impute sparse EHR and wearable time series with MUSE-Net or SADI.
- Build mixed-effects and trajectory models in R lme4 or Python statsmodels.
- Detect change points in patient trajectories.
- Forecast future clinical events from longitudinal panels.
- Integrate EHR with accelerometer, glucose, or blood pressure wearables.

## Steps

1. Extract longitudinal patient records and define the outcome trajectory.
2. Handle irregular sampling, missing values, and informative dropout.
3. Engineer time-varying features (slopes, area-under-curve, lag windows).
4. Train mixed-effects, joint, or deep sequence models.
5. Evaluate with individual-specific predictions and calibration.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GroupKFold

# Long-format data with subject IDs
X = df[["time", "age", "biomarker", "treatment"]]
y = df["outcome"]
g = df["subject_id"]

model = GradientBoostingRegressor(random_state=42)
for train_idx, test_idx in GroupKFold(n_splits=5).split(X, y, g):
    model.fit(X.iloc[train_idx], y.iloc[train_idx])
    preds = model.predict(X.iloc[test_idx])
```

## Tuning notes

- Use subject-aware splitting to avoid leakage across individuals.
- Prefer models that handle varying sequence lengths (RNNs, transformers, mixed models).
- Inspect residuals for autocorrelation and heteroscedasticity over time.
- Document assumptions about missingness (MCAR, MAR, MNAR).

## Verification

1. Compare a longitudinal ML model to a mixed-effects baseline on held-out time points.
2. Show that predictions degrade gracefully when sequences are truncated or sparse.
3. Validate that temporal ordering is preserved in all train/test splits.

''',
        "references": ["https://doi.org/10.3390/math14122084", "https://doi.org/10.1007/s10462-023-10561-w", "https://doi.org/10.1007/s10462-023-10677-z", "https://doi.org/10.1093/jamia/ocad168"],
    },
    {
        "name": "ai-for-cohort-studies",
        "title": "AI for Cohort Studies",
        "description": "Analyze defined patient groups to estimate risk, survival, and treatment effects over time.",
        "devin_body": r'''## When to use

You are building risk or prognostic models, identifying risk factors, or estimating exposure-outcome associations in a defined cohort followed over time.

## Usage

- Predict incident disease with AutoPrognosis or MILTON on UK Biobank.
- Run survival analysis with Cox, random survival forests, or deep survival.
- Build propensity-matched cohorts from EHR and claims.
- Identify biomarker trajectories linked to outcomes.
- Stratify cohorts by genotype, exposure, or frailty.

## Steps

1. Define cohort inclusion/exclusion and baseline characteristics.
2. Curate linked data (EHR, claims, omics, registries).
3. Engineer survival or longitudinal features.
4. Train risk or survival models with cross-validation.
5. Report hazard ratios, C-indices, and subgroup effects.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = cohort_df[["age", "sex", "smoking", "systolic_bp", "biomarker"]]
y = cohort_df["event_within_5yr"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=42
)
model = RandomForestClassifier(class_weight="balanced", random_state=42).fit(X_train, y_train)
```

## Tuning notes

- Balance class weights or use resampling for rare outcomes.
- Avoid leakage by excluding post-baseline variables that are not available at prediction time.
- Report confidence intervals for performance metrics using bootstrapping.
- External validation on a temporally or geographically separate cohort is essential.

## Verification

1. Replicate a published cohort risk model and compare discrimination and calibration.
2. Test the model on a held-out time period or external cohort.
3. Audit key features for clinical plausibility and fairness across subgroups.

''',
        "references": ["https://link.springer.com/article/10.1007/s10654-024-01173-x", "https://pubmed.ncbi.nlm.nih.gov/40701371/", "https://link.springer.com/article/10.1186/s12874-023-01837-4", "https://www.nature.com/articles/s41598-021-02476-9"],
    },
    {
        "name": "ai-for-clinical-trials",
        "title": "AI for Clinical Trials",
        "description": "Optimize trial design, site selection, and enrollment for clinical studies.",
        "devin_body": r'''## When to use

You are designing a clinical trial, forecasting enrollment, selecting eligible participants, or monitoring safety and operational metrics during trial conduct.

## Usage

- Forecast patient enrollment and site performance (TrialEnroll, IBM).
- Match and predict eligibility from EHR and unstructured criteria.
- Optimize site selection with geographic and historical data.
- Predict missing outcomes and patient dropout.
- Automate clinical data queries and SDV prioritization.

## Steps

1. Define protocol, endpoints, and target population.
2. Ingest EHR, claims, and historical trial data.
3. Train enrollment, eligibility, and dropout models.
4. Simulate enrollment timelines and site scenarios.
5. Validate against actual trial performance and adapt.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Structured eligibility and baseline features
X = trial_df[["age", "stage", "prior_therapies", "ecog", "biomarker"]]
y = trial_df["eligible"]

clf = GradientBoostingClassifier(random_state=42).fit(X, y)
trial_df["eligible_score"] = clf.predict_proba(X)[:, 1]
```

## Tuning notes

- Ensure eligibility models use only pre-screening data and avoid outcome leakage.
- Validate on held-out sites to test generalizability across centers.
- Monitor for protocol drift and eligibility-criteria creep over time.
- Maintain audit trails and regulatory documentation for AI-derived decisions.

## Verification

1. Compare an ML eligibility screener to manual chart review on a validation set.
2. Forecast enrollment for a trial and compare to actual accrual.
3. Run a simulated sensitivity analysis for protocol amendments and drift.

''',
        "references": ["https://trialsjournal.biomedcentral.com/counter/pdf/10.1186/s13063-021-05489-x.pdf", "https://www.nature.com/articles/s41571-026-01189-0", "https://www.nature.com/articles/s41467-026-74501-2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11319878/"],
    },
    {
        "name": "ai-for-randomized-trials",
        "title": "AI for Randomized Trials",
        "description": "Estimate heterogeneous treatment effects and subgroup benefits in randomized experiments.",
        "devin_body": r'''## When to use

You are analyzing an RCT and want to estimate average or heterogeneous treatment effects, adjust for covariates to improve power, or design adaptive randomization and interim analyses.

## Usage

- Estimate conditional average treatment effects with causal forests (grf).
- Identify responder subgroups using uplift and ITE models.
- Adjust for covariates to improve precision of ATE.
- Detect treatment effect heterogeneity across sites and demographics.
- Power adaptive enrichment and basket trials.

## Steps

1. Lock the randomization schedule and outcome variables.
2. Pre-specify covariates and subgroup hypotheses.
3. Train causal forest or meta-learner models for CATE/ITE.
4. Rank subgroups by estimated benefit and uncertainty.
5. Validate with cross-fitting and false discovery control.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from econml.dml import LinearDML

# RCT data with randomized treatment
Y = rct_df["outcome"]
T = rct_df["treatment"]
X = rct_df[["age", "sex", "baseline_score"]]

est = LinearDML(
    model_y=GradientBoostingRegressor(random_state=42),
    model_t=GradientBoostingRegressor(random_state=42),
)
est.fit(Y, T, X=X)
print("ATE:", est.ate_)
```

## Tuning notes

- Preserve randomization-based inference; do not data-mine treatment assignment.
- Cross-fit nuisance models to avoid overfitting bias in doubly robust estimators.
- Pre-specify subgroups; post-hoc subgroup discovery requires multiplicity control.
- Use positive controls or simulations to verify type-I error and power.

## Verification

1. Replicate a published RCT analysis with an ML-adjusted estimator and compare SEs.
2. Simulate null and alternative scenarios to confirm valid coverage of confidence intervals.
3. Compare heterogeneous effect estimates between causal forest and linear interaction models.

''',
        "references": ["https://www.nber.org/system/files/working_papers/w24678/w24678.pdf", "https://proceedings.mlr.press/v286/chen25b.html", "https://www.nature.com/articles/s41598-025-10566-1", "https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2800273", "https://link.springer.com/article/10.1186/s13063-020-4076-y"],
    },
    {
        "name": "ai-for-observational-studies",
        "title": "AI for Observational Studies",
        "description": "Estimate causal effects from real-world data using propensity scores and double machine learning.",
        "devin_body": r'''## When to use

You are estimating causal effects, treatment responses, or policy impacts from observational data where treatment assignment was not randomized.

## Usage

- Build propensity scores and inverse probability weights with CausalForge.
- Apply double/debiased machine learning (EconML, DoubleML).
- Emulate target trials from EHR and claims databases.
- Adjust for high-dimensional confounding with proxy variables.
- Assess balance and sensitivity to unmeasured confounding.

## Steps

1. Define the causal question, exposure, and outcome.
2. Extract longitudinal observational data and confounders.
3. Estimate propensity scores or train nuisance models.
4. Compute ATE/CATE with DML or weighting.
5. Run sensitivity analyses and report robustness.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
from econml.dml import LinearDML

Y = obs_df["outcome"]
T = obs_df["treatment"]
X = obs_df[["age", "comorbidity", "lab_value"]]

est = LinearDML(
    model_y=GradientBoostingRegressor(random_state=42),
    model_t=GradientBoostingClassifier(random_state=42),
)
est.fit(Y, T, X=X)
print("CATE:", est.effect(X[:5]))
```

## Tuning notes

- Check positivity and overlap; extrapolation can bias causal estimates.
- Use cross-fitting and sample splitting to reduce overfitting in nuisance models.
- Validate with negative controls, placebo tests, or coarsened exact matching.
- Report sensitivity bounds for potential unmeasured confounders.

## Verification

1. Reproduce an observational benchmark (e.g., IHDP, Jobs, ACIC) and compare estimates.
2. Compare propensity-weighted, matching, and doubly robust estimates.
3. Run a sensitivity analysis and show how large an unmeasured confounder must be.

''',
        "references": ["https://arxiv.org/abs/2501.00755v1", "https://doi.org/10.3386/w30302", "https://pubmed.ncbi.nlm.nih.gov/34652613/", "https://proceedings.mlr.press/v161/shi21a/shi21a.pdf"],
    },
    {
        "name": "ai-for-registry-studies",
        "title": "AI for Registry Studies",
        "description": "Analyze disease and product registries to monitor safety, effectiveness, and utilization.",
        "devin_body": r'''## When to use

You are using a disease, product, or population registry to generate real-world evidence, monitor outcomes, or support regulatory and health-technology decisions.

## Usage

- Identify fit-for-purpose registries with AI-powered RWD catalogues.
- Define phenotypes using CQL, SNOMED, and FHIR (PhEMA).
- Track drug utilization and adverse events across registries.
- Benchmark outcomes against external controls.
- Generate real-world evidence for regulatory and HTA submissions.

## Steps

1. Identify relevant registries and assess data quality.
2. Define the study population and phenotype algorithms.
3. Extract exposure, outcome, and covariate records.
4. Apply epidemiological and ML methods for safety/effectiveness.
5. Prepare regulatory-grade reports and evidence packages.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Registry records with patient, event, and exposure flags
X = registry_df[["age", "sex", "disease_stage", "prior_treatment"]]
y = registry_df["outcome_event"]

clf = GradientBoostingClassifier(random_state=42).fit(X, y)
registry_df["risk_score"] = clf.predict_proba(X)[:, 1]
```

## Tuning notes

- Account for site and country effects if the registry spans multiple centers.
- Be explicit about data-quality flags and missingness mechanisms.
- Use time-dependent splits to avoid leakage from later enrollment periods.
- Align analyses with regulatory guidance and HTA evidentiary standards.

## Verification

1. Build a predictive model on a disease registry and validate on a temporally held-out sample.
2. Compare registry-derived estimates to published RCT estimates for the same treatment.
3. Report data-quality and completeness metrics alongside model performance.

''',
        "references": ["https://link.springer.com/article/10.1007/s44250-026-00373-4", "https://doi.org/10.2196/71873", "https://www.real4reg.eu/", "https://cordis.europa.eu/project/id/101095479"],
    },
    {
        "name": "ai-for-real-world-evidence",
        "title": "AI for Real-World Evidence",
        "description": "Generate regulatory and HTA evidence from EHR, claims, and registry data.",
        "devin_body": r'''## When to use

You need to generate or evaluate clinical evidence from routinely collected data to support regulatory, reimbursement, or treatment decisions.

## Usage

- Link RWD sources across EHR, claims, and disease registries.
- Apply fit-for-purpose assessments per FDA/EMA guidance.
- Run target trial emulation and causal inference.
- Build external control arms for single-arm studies.
- Create interactive evidence dashboards for HTA bodies.

## Steps

1. Define the research question and regulatory use case.
2. Assess RWD source fitness and data quality.
3. Curate exposure, outcome, and confounder variables.
4. Apply causal or predictive methods and sensitivity checks.
5. Document evidence in a regulatory/HTA submission package.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit

# RWE treatment-decision model with time-aware validation
X = rwd_df[["age", "comorbidity_count", "prior_hospitalizations"]]
y = rwd_df["treatment_response"]

tscv = TimeSeriesSplit(n_splits=3)
for train_idx, test_idx in tscv.split(X):
    model = RandomForestClassifier(random_state=42).fit(X.iloc[train_idx], y.iloc[train_idx])
    preds = model.predict(X.iloc[test_idx])
```

## Tuning notes

- Avoid immortal-time and prevalent-user biases in treatment comparisons.
- Validate on external data or against RCT estimates when possible.
- Use transparent, auditable pipelines for regulatory submissions.
- Track data provenance and versioning for all RWE analyses.

## Verification

1. Emulate a target trial in claims or EHR data and compare estimates to an RCT.
2. Evaluate model performance on a different RWD source or calendar period.
3. Produce a fit-for-purpose assessment using FDA or EMA guidance criteria.

''',
        "references": ["https://www.fda.gov/drugs/development-resources/advancing-real-world-evidence-program-frequently-asked-questions", "https://www.law.cornell.edu/uscode/text/21/355g", "https://bmcmedinformdecismak.biomedcentral.com/counter/pdf/10.1186/s12911-021-01403-2.pdf", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9189725/", "https://www.nature.com/articles/s43588-025-00901-x"],
    },
    {
        "name": "ai-for-patient-reported-outcomes",
        "title": "AI for Patient-Reported Outcomes",
        "description": "Use AI to administer, score, and interpret patient-reported outcome measures.",
        "devin_body": r'''## When to use

You are collecting, analyzing, or predicting patient-reported outcomes, quality of life, symptom trajectories, or treatment satisfaction data.

## Usage

- Deploy computer adaptive testing with PROMIS-CAT and REDCap.
- Generate and validate LLM-PROMs from patient language.
- Detect response patterns and missing-not-at-random signals.
- Correlate PROs with wearables and clinical events.
- Adapt item banks to minimize patient burden.

## Steps

1. Select the PRO concept and validated instrument.
2. Integrate CAT or LLM-generated items into data capture.
3. Clean responses and detect careless or inconsistent patterns.
4. Train models linking PROs to outcomes or adverse events.
5. Validate psychometric properties and iterate.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

X = pro_df[["baseline_pain", "function_score", "age", "comorbidities"]]
y = pro_df["follow_up_quality_of_life"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
pro_df["predicted_pro"] = model.predict(X)
```

## Tuning notes

- Respect floor and ceiling effects in PRO scales.
- Handle item-level missingness with appropriate imputation or latent models.
- Calibrate predictions for decision thresholds used in clinical workflows.
- Engage patients and clinicians in validating model outputs.

## Verification

1. Predict a PRO score at a future visit and compare to observed values on a test set.
2. Implement a short adaptive PRO form and compare measurement precision to the full form.
3. Evaluate whether PRO-based predictions improve shared decision-making outcomes.

''',
        "references": ["https://link.springer.com/article/10.1186/s12955-025-02365-z", "https://link.springer.com/article/10.1186/s12911-025-03083-8", "https://link.springer.com/article/10.1186/s41687-026-00992-8", "https://link.springer.com/article/10.1186/s41687-024-00808-7"],
    },
    {
        "name": "ai-for-biomarkers",
        "title": "AI for Biomarkers",
        "description": "Discover and validate biomarkers by integrating genomics, proteomics, and imaging data.",
        "devin_body": r'''## When to use

You are discovering, validating, or translating biomarkers from high-dimensional omics, imaging, or multi-modal clinical data.

## Usage

- Integrate multi-omics with Flexynesis, IntegrAO, or Omics BioAnalytics.
- Discover diagnostic and prognostic signatures with MILTON.
- Build predictive panels from blood, imaging, and digital biomarkers.
- Validate biomarkers in independent cohorts and trials.
- Interpret biological pathways with feature importance.

## Steps

1. Collect omics, imaging, and clinical phenotype data.
2. Normalize, impute, and align multi-modal features.
3. Train multi-omics integration and feature-selection models.
4. Validate in held-out and external cohorts.
5. Characterize biological mechanism and clinical utility.

## Code pattern

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif

X = omics_df.drop("outcome", axis=1)
y = omics_df["outcome"]

selector = SelectKBest(f_classif, k=20)
X_sel = selector.fit_transform(X, y)
model = LogisticRegression(max_iter=1000, penalty="l1", solver="liblinear").fit(X_sel, y)
```

## Tuning notes

- Keep discovery and validation data strictly separate and time-ordered.
- Use regularization and stability selection to avoid overfitting high-dimensional data.
- Validate batch effects, measurement platforms, and population diversity.
- Document the locked model, thresholds, and intended-use claim.

## Verification

1. Reproduce a published biomarker signature and test it on a held-out cohort.
2. Compare sparse ML-selected biomarkers to univariate ranking and stability-selection baselines.
3. Report sensitivity, specificity, and calibration in the intended-use population.

''',
        "references": ["https://www.nature.com/articles/s41587-023-02033-x", "https://doi.org/10.1371/journal.pcbi.1010357", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8650485/", "https://ai.nejm.org/doi/full/10.1056/AIoa2400867"],
    },
    {
        "name": "ai-for-synthetic-controls",
        "title": "AI for Synthetic Controls",
        "description": "Construct synthetic control arms from historical or real-world data to augment clinical evidence.",
        "devin_body": r'''## When to use

You have one or a few treated units and many untreated donor units, and need a credible counterfactual trajectory from a weighted combination of donors.

## Usage

- Build donor pools from aggregate and patient-level data.
- Estimate synthetic controls with penalized regression (pensynth).
- Quantify uncertainty with scpi prediction intervals.
- Validate pre-treatment fit and placebo tests.
- Support regulatory submissions with external comparators.

## Steps

1. Define the treated unit(s) and pre-treatment period.
2. Assemble a donor pool of similar historical controls.
3. Estimate donor weights and counterfactual trajectories.
4. Evaluate fit, placebo robustness, and sensitivity.
5. Report treatment effects with confidence intervals.

## Code pattern

```python
import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Pre-treatment outcome matrix: rows = time, columns = control units
Y_pre = donor_df.loc[donor_df["pre"] == 1, control_units].values
y_treated = treated_df.loc[treated_df["pre"] == 1, "outcome"].values

def sc_loss(w):
    return np.mean((Y_pre @ w - y_treated) ** 2)

res = minimize(sc_loss, x0=np.ones(Y_pre.shape[1]) / Y_pre.shape[1],
               method="SLSQP", bounds=[(0, 1)] * Y_pre.shape[1],
               constraints={"type": "eq", "fun": lambda w: np.sum(w) - 1})
```

## Tuning notes

- Exclude donors that are poor matches or place high weight on a single unit.
- Use cross-validation on pre-treatment periods to choose regularization.
- Apply placebo tests and leave-one-out robustness checks.
- Be cautious when using synthetic controls as primary evidence in regulatory settings.

## Verification

1. Replicate the California tobacco-control synthetic control case study.
2. Compare classic SCM, penalized SCM, and a learned-representation baseline.
3. Run placebo inference and show that treatment effects exceed the null distribution.

''',
        "references": ["https://www.bis.org/publ/work1181.pdf", "https://doi.org/10.22541/au.176072431.11742213/v1", "https://arxiv.org/abs/2602.04611", "https://microsoft.github.io/SparseSC/", "https://www.mit.edu/~jhainm/Paper/ccs.pdf"],
    },
    {
        "name": "ai-for-meta-analysis",
        "title": "AI for Meta-Analysis",
        "description": "Automate systematic reviews and synthesize effect sizes across clinical and epidemiological studies.",
        "devin_body": r'''## When to use

You are conducting a meta-analysis or systematic review and want to automate or augment screening, extraction, effect estimation, or heterogeneity analysis.

## Usage

- Screen citations with LLMs and Rayyan/AiReview.
- Extract study characteristics and outcomes with GPT-4 pipelines.
- Fit random-effects and Bayesian meta-analysis models.
- Assess heterogeneity, publication bias, and study quality.
- Update living systematic reviews continuously.

## Steps

1. Define the PICO question and search strategy.
2. Run automated screening and data extraction.
3. Appraise risk of bias and study quality.
4. Pool effect sizes with appropriate meta-analytic models.
5. Report forest plots, heterogeneity, and sensitivity.

## Code pattern

```python
import pandas as pd
import numpy as np
from statsmodels.stats.meta_analysis import combine_effects

# Data frame with effect sizes and standard errors
effects = meta_df["effect_size"]
se = meta_df["se"]

combined = combine_effects(effects, se, method_re="ml")
print("Pooled effect:", combined.effect)
print("I-squared:", combined.i2)
```

## Tuning notes

- Use human-in-the-loop validation for screening and extraction decisions.
- Choose effect-size metrics and models appropriate to the data types.
- Assess publication bias with funnel plots and Egger tests.
- Document all automation choices and review for errors or hallucinations.

## Verification

1. Reproduce a published meta-analysis using extracted data and compare pooled estimates.
2. Compare LLM-extracted data to manually extracted data on a validation set.
3. Run leave-one-out and subgroup meta-analyses to assess robustness.

''',
        "references": ["https://doi.org/10.1017/rsm.2025.10065", "https://arxiv.org/abs/2606.28363", "https://www.ncbi.nlm.nih.gov/pmc/articles/13035263", "https://www.ncbi.nlm.nih.gov/books/NBK620201/", "https://link.springer.com/article/10.1007/s41669-024-00476-9"],
    },
    {
        "name": "ai-for-evidence-synthesis",
        "title": "AI for Evidence Synthesis",
        "description": "Synthesize heterogeneous evidence, assess risk of bias, and generate decision-ready summaries.",
        "devin_body": r'''## When to use

You need to synthesize a body of literature, produce a systematic review, evidence map, or summary of research findings, and want to use AI responsibly.

## Usage

- Automate risk-of-bias assessment with LLMs (ROBINS-I, ROB2).
- Combine direct and indirect comparisons in network meta-analysis.
- Generate evidence maps and interactive summaries.
- Grade certainty with GRADE and robot reviewers.
- Produce plain-language summaries for guidelines.

## Steps

1. Frame the synthesis question and inclusion criteria.
2. Extract data, effects, and risk-of-bias judgments.
3. Choose a synthesis model (pairwise, network, dose-response).
4. Assess heterogeneity, inconsistency, and certainty.
5. Summarize findings for clinical and policy audiences.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Title/abstract screening with TF-IDF and logistic regression
vect = TfidfVectorizer(stop_words="english", max_features=5000)
X = vect.fit_transform(records_df["abstract"])
y = records_df["included"]

clf = LogisticRegression(class_weight="balanced", max_iter=1000).fit(X, y)
records_df["screening_score"] = clf.predict_proba(X)[:, 1]
```

## Tuning notes

- Maintain human accountability for all inclusion and synthesis decisions.
- Validate LLM outputs against full-text sources to avoid hallucinations.
- Use structured protocols and reporting standards (PRISMA, ENTREQ, ROBIS).
- Update the living review regularly with new search results.

## Verification

1. Reproduce a small published systematic review with AI-assisted screening.
2. Compare LLM-generated risk-of-bias ratings to human ratings on a gold-standard set.
3. Cross-check every synthesized claim against its source publication.

''',
        "references": ["https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis/2DACF6D129AA6E46CB8A8740A03D0675", "https://www.ncbi.nlm.nih.gov/books/NBK620201/", "https://www.ncbi.nlm.nih.gov/pmc/articles/13035263", "https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.ED000178/full", "https://doi.org/10.1093/jamia/ocaf030"],
    },
]