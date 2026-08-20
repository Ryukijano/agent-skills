SKILLS = [
    {
        "name": "ai-for-longitudinal-studies",
        "title": "AI for Longitudinal Studies",
        "description": "Machine learning and deep learning for repeated measurements, time-varying covariates, missing data, trajectories, and outcomes in longitudinal cohorts and EHR data.",
        "devin_body": r'''## When to use

You are analyzing repeated observations over time, predicting future trajectories, or handling attrition and irregular sampling in longitudinal health, social, or behavioral data.

## Usage

- **Trajectory modeling**: predict individual or population-level progression over time.
- **Missing-data handling**: impute or model informative dropout and irregular visits.
- **Feature engineering**: encode time-varying covariates, slopes, and exposure histories.
- **Causal longitudinal analysis**: estimate dynamic treatment effects with sequential ignorability.

## Steps

1. Structure the data into long format with subject, time, and outcome columns.
2. Encode temporal patterns (lags, rolling summaries, time-since-event).
3. Choose a model suited to repeated measures (mixed-effects, RNN, transformer, or survival model).
4. Evaluate with time-aware cross-validation and check temporal leakage.
5. Report uncertainty and sensitivity to missing-data assumptions.

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

## References

- https://doi.org/10.3390/math14122084
- https://doi.org/10.1007/s10462-023-10561-w
- https://doi.org/10.1007/s10462-023-10677-z
- https://doi.org/10.1093/jamia/ocad168
''',
        "references": [
            "https://doi.org/10.3390/math14122084",
            "https://doi.org/10.1007/s10462-023-10561-w",
            "https://doi.org/10.1007/s10462-023-10677-z",
            "https://doi.org/10.1093/jamia/ocad168",
        ],
    },
    {
        "name": "ai-for-cohort-studies",
        "title": "AI for Cohort Studies",
        "description": "Machine learning for risk prediction, confounding control, survival analysis, and biomarker discovery in prospective and retrospective cohort studies.",
        "devin_body": r'''## When to use

You are building risk or prognostic models, identifying risk factors, or estimating exposure-outcome associations in a defined cohort followed over time.

## Usage

- **Cohort risk prediction**: forecast disease onset, progression, or mortality.
- **Feature discovery**: find non-linear risk factors and interactions in large biobanks.
- **Survival modeling**: handle censored outcomes and time-to-event data.
- **Confounder adjustment**: control for selection bias and measured confounders.

## Steps

1. Define the cohort, eligibility window, and follow-up period.
2. Create a tabular feature set at baseline or as time-varying covariates.
3. Split by calendar time or admission date to mimic prospective use.
4. Train risk models with appropriate survival or classification objectives.
5. Validate calibration, discrimination, and generalizability to new cohorts.

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

## References

- https://link.springer.com/article/10.1007/s10654-024-01173-x
- https://pubmed.ncbi.nlm.nih.gov/40701371/
- https://link.springer.com/article/10.1186/s12874-023-01837-4
- https://www.nature.com/articles/s41598-021-02476-9
''',
        "references": [
            "https://link.springer.com/article/10.1007/s10654-024-01173-x",
            "https://pubmed.ncbi.nlm.nih.gov/40701371/",
            "https://link.springer.com/article/10.1186/s12874-023-01837-4",
            "https://www.nature.com/articles/s41598-021-02476-9",
        ],
    },
    {
        "name": "ai-for-clinical-trials",
        "title": "AI for Clinical Trials",
        "description": "Machine learning for clinical-trial design, patient eligibility, cohort selection, outcome prediction, and operational monitoring across the trial lifecycle.",
        "devin_body": r'''## When to use

You are designing a clinical trial, forecasting enrollment, selecting eligible participants, or monitoring safety and operational metrics during trial conduct.

## Usage

- **Trial feasibility**: predict enrollment, dropout, and site performance.
- **Eligibility screening**: parse unstructured criteria and match patients to protocols.
- **Outcome prediction**: forecast treatment response and safety events.
- **Site and data monitoring**: detect anomalies, drift, and data-quality issues.

## Steps

1. Translate the protocol into structured eligibility and endpoint definitions.
2. Link EHR or registry data to candidate participants using structured and NLP features.
3. Build and validate prediction models for enrollment, response, or adverse events.
4. Deploy models under prospective monitoring with human oversight.
5. Retrain and validate when protocols, sites, or populations change.

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

## References

- https://trialsjournal.biomedcentral.com/counter/pdf/10.1186/s13063-021-05489-x.pdf
- https://www.nature.com/articles/s41571-026-01189-0
- https://www.nature.com/articles/s41467-026-74501-2
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11319878/
''',
        "references": [
            "https://trialsjournal.biomedcentral.com/counter/pdf/10.1186/s13063-021-05489-x.pdf",
            "https://www.nature.com/articles/s41571-026-01189-0",
            "https://www.nature.com/articles/s41467-026-74501-2",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11319878/",
        ],
    },
    {
        "name": "ai-for-randomized-trials",
        "title": "AI for Randomized Trials",
        "description": "Machine learning for heterogeneous treatment effects, covariate adjustment, adaptive randomization, and efficient inference in randomized controlled trials.",
        "devin_body": r'''## When to use

You are analyzing an RCT and want to estimate average or heterogeneous treatment effects, adjust for covariates to improve power, or design adaptive randomization and interim analyses.

## Usage

- **Heterogeneous treatment effects**: identify subgroups that benefit most or least.
- **Covariate adjustment**: improve precision using baseline prognostic variables.
- **Adaptive designs**: inform response-adaptive randomization and enrichment.
- **Efficient inference**: combine machine learning with valid randomization inference.

## Steps

1. Lock the analysis plan, including adjustment variables and subgroups, before unblinding.
2. Fit flexible outcome and propensity nuisance models with cross-fitting.
3. Estimate average and conditional treatment effects with appropriate inference.
4. Test for treatment-effect heterogeneity using pre-specified subgroups or learned partitions.
5. Report confidence intervals and control the family-wise error rate for subgroup analyses.

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

## References

- https://www.nber.org/system/files/working_papers/w24678/w24678.pdf
- https://proceedings.mlr.press/v286/chen25b.html
- https://www.nature.com/articles/s41598-025-10566-1
- https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2800273
- https://link.springer.com/article/10.1186/s13063-020-4076-y
''',
        "references": [
            "https://www.nber.org/system/files/working_papers/w24678/w24678.pdf",
            "https://proceedings.mlr.press/v286/chen25b.html",
            "https://www.nature.com/articles/s41598-025-10566-1",
            "https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2800273",
            "https://link.springer.com/article/10.1186/s13063-020-4076-y",
        ],
    },
    {
        "name": "ai-for-observational-studies",
        "title": "AI for Observational Studies",
        "description": "Causal machine learning for treatment-effect estimation, propensity scoring, confounding adjustment, and sensitivity analysis in observational data.",
        "devin_body": r'''## When to use

You are estimating causal effects, treatment responses, or policy impacts from observational data where treatment assignment was not randomized.

## Usage

- **Propensity and inverse probability weighting**: balance treatment groups.
- **Doubly robust estimation**: combine outcome and treatment models for robust inference.
- **Representation learning**: learn low-dimensional adjustment sets from high-dimensional covariates.
- **Sensitivity analysis**: quantify robustness to unmeasured confounding.

## Steps

1. Define the causal estimand, treatment, outcome, and covariates.
2. Assess overlap and trim units outside the common support.
3. Fit flexible outcome and propensity models with cross-fitting.
4. Estimate the effect using AIPW, targeted maximum likelihood, or matching.
5. Conduct sensitivity analyses and report bounds under confounding scenarios.

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

## References

- https://arxiv.org/html/2501.00755v1
- https://doi.org/10.3386/w30302
- https://pubmed.ncbi.nlm.nih.gov/34652613/
- https://proceedings.mlr.press/v161/shi21a/shi21a.pdf
''',
        "references": [
            "https://arxiv.org/html/2501.00755v1",
            "https://doi.org/10.3386/w30302",
            "https://pubmed.ncbi.nlm.nih.gov/34652613/",
            "https://proceedings.mlr.press/v161/shi21a/shi21a.pdf",
        ],
    },
    {
        "name": "ai-for-registry-studies",
        "title": "AI for Registry Studies",
        "description": "Machine learning for patient registries, disease surveillance, regulatory-grade real-world evidence, and longitudinal outcome tracking.",
        "devin_body": r'''## When to use

You are using a disease, product, or population registry to generate real-world evidence, monitor outcomes, or support regulatory and health-technology decisions.

## Usage

- **Registry-based outcome prediction**: forecast events and treatment responses.
- **Quality and completeness assessment**: identify missing data and reporting gaps.
- **Comparative effectiveness**: emulate target trials within registry populations.
- **Surveillance and safety monitoring**: detect signals of adverse events or product issues.

## Steps

1. Understand registry design, inclusion criteria, and variable definitions.
2. Clean and link registry records, handling duplicates and missingness.
3. Define the target population and time-at-risk for the analysis.
4. Train and validate models appropriate to the registry structure and outcomes.
5. Produce transparent reports with clear limitations about generalizability.

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

## References

- https://link.springer.com/article/10.1007/s44250-026-00373-4
- https://doi.org/10.2196/71873
- https://www.real4reg.eu/
- https://cordis.europa.eu/project/id/101095479
''',
        "references": [
            "https://link.springer.com/article/10.1007/s44250-026-00373-4",
            "https://doi.org/10.2196/71873",
            "https://www.real4reg.eu/",
            "https://cordis.europa.eu/project/id/101095479",
        ],
    },
    {
        "name": "ai-for-real-world-evidence",
        "title": "AI for Real-World Evidence",
        "description": "Machine learning for extracting, validating, and synthesizing real-world evidence from EHRs, claims, registries, and wearables for regulatory and clinical decisions.",
        "devin_body": r'''## When to use

You need to generate or evaluate clinical evidence from routinely collected data to support regulatory, reimbursement, or treatment decisions.

## Usage

- **RWE generation**: design and analyze non-interventional studies from RWD.
- **Data fit-for-purpose assessment**: evaluate reliability and relevance of RWD sources.
- **Target trial emulation**: mimic an RCT design using observational data.
- **Decision support**: translate RWE into individualized treatment recommendations.

## Steps

1. Define the research question and regulatory or decision context.
2. Map RWD sources (EHR, claims, registries, wearables) to study variables.
3. Apply causal inference and ML methods with appropriate validation.
4. Assess data quality, representativeness, and bias.
5. Document fit-for-purpose and produce reproducible evidence packages.

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

## References

- https://www.fda.gov/drugs/development-resources/advancing-real-world-evidence-program-frequently-asked-questions
- https://uscode.house.gov/view.xhtml?req=%28title%3A21+section%3A355g+edition%3Aprelim%29
- https://bmcmedinformdecismak.biomedcentral.com/counter/pdf/10.1186/s12911-021-01403-2.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9189725/
- https://www.nature.com/articles/s43588-025-00901-x
''',
        "references": [
            "https://www.fda.gov/drugs/development-resources/advancing-real-world-evidence-program-frequently-asked-questions",
            "https://uscode.house.gov/view.xhtml?req=%28title%3A21+section%3A355g+edition%3Aprelim%29",
            "https://bmcmedinformdecismak.biomedcentral.com/counter/pdf/10.1186/s12911-021-01403-2.pdf",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC9189725/",
            "https://www.nature.com/articles/s43588-025-00901-x",
        ],
    },
    {
        "name": "ai-for-patient-reported-outcomes",
        "title": "AI for Patient-Reported Outcomes",
        "description": "Machine learning for predicting, personalizing, and reducing the burden of patient-reported outcome measures and PRO-based treatment decisions.",
        "devin_body": r'''## When to use

You are collecting, analyzing, or predicting patient-reported outcomes, quality of life, symptom trajectories, or treatment satisfaction data.

## Usage

- **PRO prediction**: forecast post-treatment PRO scores from baseline and clinical data.
- **Computer adaptive testing**: select the most informative PRO items per patient.
- **Personalized interventions**: target patients whose PROs indicate high risk or unmet need.
- **Burden reduction**: minimize questionnaire length while preserving measurement precision.

## Steps

1. Map the PRO instrument, response scale, and recall period to the analysis goal.
2. Engineer baseline and longitudinal features (scores, trends, change from baseline).
3. Train models for prediction, classification, or item response theory.
4. Validate predictive accuracy and measurement properties in a held-out sample.
5. Assess clinical utility and patient acceptability before deployment.

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

## References

- https://link.springer.com/article/10.1186/s12955-025-02365-z
- https://link.springer.com/article/10.1186/s12911-025-03083-8
- https://link.springer.com/article/10.1186/s41687-026-00992-8
- https://link.springer.com/article/10.1186/s41687-024-00808-7
''',
        "references": [
            "https://link.springer.com/article/10.1186/s12955-025-02365-z",
            "https://link.springer.com/article/10.1186/s12911-025-03083-8",
            "https://link.springer.com/article/10.1186/s41687-026-00992-8",
            "https://link.springer.com/article/10.1186/s41687-024-00808-7",
        ],
    },
    {
        "name": "ai-for-biomarkers",
        "title": "AI for Biomarkers",
        "description": "Machine learning for omics-based biomarker discovery, sparse signature selection, multi-modal integration, and clinical validation.",
        "devin_body": r'''## When to use

You are discovering, validating, or translating biomarkers from high-dimensional omics, imaging, or multi-modal clinical data.

## Usage

- **Signature discovery**: identify sparse, reproducible biomarker panels.
- **Multi-omic integration**: combine genomics, proteomics, metabolomics, and imaging.
- **Predictive vs prognostic markers**: distinguish treatment-modifying from disease-risk biomarkers.
- **Clinical validation**: lock models and test on independent cohorts and intended-use populations.

## Steps

1. Assemble discovery and validation cohorts with clear inclusion/exclusion criteria.
2. Preprocess and harmonize multi-modal data and batch-correct where needed.
3. Apply sparse or regularized ML to select candidate biomarkers.
4. Lock the model and evaluate on an independent validation cohort.
5. Assess biological plausibility, regulatory path, and clinical actionability.

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

## References

- https://www.nature.com/articles/s41587-023-02033-x
- https://doi.org/10.1371/journal.pcbi.1010357
- https://doi.org/10.1136/bmjopen-2021-053674
- https://ai.nejm.org/doi/full/10.1056/AIoa2400867
''',
        "references": [
            "https://www.nature.com/articles/s41587-023-02033-x",
            "https://doi.org/10.1371/journal.pcbi.1010357",
            "https://doi.org/10.1136/bmjopen-2021-053674",
            "https://ai.nejm.org/doi/full/10.1056/AIoa2400867",
        ],
    },
    {
        "name": "ai-for-synthetic-controls",
        "title": "AI for Synthetic Controls",
        "description": "Machine learning for constructing, validating, and extending synthetic and virtual control arms from observational data to augment clinical and policy evaluation.",
        "devin_body": r'''## When to use

You have one or a few treated units and many untreated donor units, and need a credible counterfactual trajectory from a weighted combination of donors.

## Usage

- **Classic synthetic controls**: build a weighted donor pool to match pre-treatment outcomes.
- **Penalized and sparse synthetic controls**: regularize unit and feature weights.
- **Deep representation learning**: learn low-dimensional embeddings for better donor matching.
- **External and virtual control arms**: augment single-arm trials with historical or real-world controls.

## Steps

1. Define the treated unit, pre-treatment period, donor pool, and outcome of interest.
2. Select predictor variables and fit a weighted combination of donors to pre-treatment outcomes.
3. Evaluate pre-treatment fit and generate the counterfactual trajectory.
4. Compute treatment effects and placebo-based inferential procedures.
5. Assess robustness to donor pool composition and weight sparsity.

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

## References

- https://www.bis.org/publ/work1181.pdf
- https://doi.org/10.22541/au.176072431.11742213/v1
- https://arxiv.org/html/2602.04611
- https://microsoft.github.io/SparseSC/
- https://www.mit.edu/~jhainm/Paper/ccs.pdf
''',
        "references": [
            "https://www.bis.org/publ/work1181.pdf",
            "https://doi.org/10.22541/au.176072431.11742213/v1",
            "https://arxiv.org/html/2602.04611",
            "https://microsoft.github.io/SparseSC/",
            "https://www.mit.edu/~jhainm/Paper/ccs.pdf",
        ],
    },
    {
        "name": "ai-for-meta-analysis",
        "title": "AI for Meta-Analysis",
        "description": "Machine learning and LLMs for automating literature search, screening, data extraction, effect-size estimation, and heterogeneity assessment in meta-analyses.",
        "devin_body": r'''## When to use

You are conducting a meta-analysis or systematic review and want to automate or augment screening, extraction, effect estimation, or heterogeneity analysis.

## Usage

- **Automated literature search and screening**: classify and rank citations for inclusion.
- **Data extraction**: parse study characteristics, outcomes, and effect sizes from PDFs.
- **Statistical modeling**: estimate pooled effects, heterogeneity, and subgroup differences.
- **Network meta-analysis**: synthesize direct and indirect treatment comparisons.

## Steps

1. Register the protocol and define PICO/PECO and analysis plan.
2. Run a reproducible search and import citations into an AI-assisted screening tool.
3. Use ML or LLMs to extract study data with human verification.
4. Compute effect sizes and pooled estimates using appropriate models (fixed, random, Bayesian).
5. Assess risk of bias, heterogeneity, and sensitivity to study inclusion.

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

## References

- https://doi.org/10.1017/rsm.2025.10065
- https://arxiv.org/html/2606.28363
- https://www.ncbi.nlm.nih.gov/pmc/articles/13035263
- https://www.ncbi.nlm.nih.gov/books/NBK620201/
- https://link.springer.com/article/10.1007/s41669-024-00476-9
''',
        "references": [
            "https://doi.org/10.1017/rsm.2025.10065",
            "https://arxiv.org/html/2606.28363",
            "https://www.ncbi.nlm.nih.gov/pmc/articles/13035263",
            "https://www.ncbi.nlm.nih.gov/books/NBK620201/",
            "https://link.springer.com/article/10.1007/s41669-024-00476-9",
        ],
    },
    {
        "name": "ai-for-evidence-synthesis",
        "title": "AI for Evidence Synthesis",
        "description": "AI and LLMs for systematic review automation, risk-of-bias assessment, evidence mapping, and trustworthy synthesis of research findings.",
        "devin_body": r'''## When to use

You need to synthesize a body of literature, produce a systematic review, evidence map, or summary of research findings, and want to use AI responsibly.

## Usage

- **Automated screening and extraction**: speed up systematic review production.
- **Risk-of-bias and quality assessment**: flag concerns and support appraisal.
- **Evidence maps and gap analysis**: categorize studies and identify research gaps.
- **Synthesis and manuscript support**: draft plain-language and technical summaries.

## Steps

1. Define the review question, scope, and search strategy in a registered protocol.
2. Run the search, deduplicate, and prepare title/abstract and full-text records.
3. Deploy AI-assisted screening and extraction with independent human checks.
4. Appraise risk of bias and synthesize findings narratively or quantitatively.
5. Verify claims against original sources and report AI contributions transparently.

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

## References

- https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis/2DACF6D129AA6E46CB8A8740A03D0675
- https://www.ncbi.nlm.nih.gov/books/NBK620201/
- https://www.ncbi.nlm.nih.gov/pmc/articles/13035263
- https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.ED000178/full
- https://doi.org/10.1093/jamia/ocaf030
''',
        "references": [
            "https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis/2DACF6D129AA6E46CB8A8740A03D0675",
            "https://www.ncbi.nlm.nih.gov/books/NBK620201/",
            "https://www.ncbi.nlm.nih.gov/pmc/articles/13035263",
            "https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.ED000178/full",
            "https://doi.org/10.1093/jamia/ocaf030",
        ],
    },
]
