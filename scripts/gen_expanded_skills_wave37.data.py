SKILLS = [
    {
        "name": "ai-for-nephrology",
        "title": "AI for Nephrology",
        "description": "Use machine learning to predict chronic kidney disease progression, acute kidney injury, dialysis outcomes, and transplant success.",
        "devin_body": r'''
## When to use

You are building models to predict CKD progression, detect acute kidney injury early, optimize dialysis, allocate kidneys, or analyze renal biopsy and histopathology images.

## Usage

- Risk-stratify CKD progression using eGFR trajectories, albuminuria, and comorbidities.
- Build EHR-based early-warning models for in-hospital acute kidney injury.
- Optimize dialysis treatment adequacy and predict access failure.
- Match donors and recipients, predict rejection, and forecast graft survival.
- Segment and classify glomerular lesions in renal biopsy images.

## Steps

1. Assemble longitudinal EHR, labs, pathology, and imaging data for kidney-related endpoints.
2. Define prediction targets (AKI, CKD progression, graft survival, lesion type) and time windows.
3. Train and validate predictive models with time-based splits and competing-risk handling.
4. Integrate predictions into nephrology workflows as decision support.
5. Audit for disparities in race, ethnicity, geography, and access to care.
6. Monitor model performance across health systems and retrain as guidelines evolve.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import TimeSeriesSplit

# Predict 90-day AKI from structured EHR features
X = df[["age", "baseline_creatinine", "diabetes", "nephrotoxin_exposure"]]
y = df["aki_within_90d"]

cv = TimeSeriesSplit(n_splits=5)
model = GradientBoostingClassifier(random_state=42)
for train_idx, test_idx in cv.split(X):
    model.fit(X.iloc[train_idx], y.iloc[train_idx])
    print("AUROC:", model.score(X.iloc[test_idx], y.iloc[test_idx]))
```

## Tuning notes

- Use time-based splits; eGFR and creatinine are longitudinal and future labs must not leak.
- Competing risks (death, ESKD, transplant) often require survival or Fine-Gray models.
- External validate across health systems because CKD prevalence and lab assays vary.
- Monitor for disparities in race, ethnicity, and access to care.

## Verification

1. Train a CKD progression model and compare time-dependent AUC to KDIGO staging.
2. Build an AKI early-warning pipeline with hourly EHR windows and alert latency analysis.
3. Evaluate glomerulus segmentation on PAS-stained renal biopsy patches against pathologist annotations.
        ''',
        "references": [
            "https://doi.org/10.1016/j.xkme.2024.100927",
            "https://doi.org/10.1007/s11255-024-04165-8",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC10103234/",
            "https://doi.org/10.2215/CJN.0000000000000068",
        ],
    },
    {
        "name": "ai-for-endocrinology",
        "title": "AI for Endocrinology",
        "description": "Use machine learning to forecast glucose, stratify thyroid nodules, characterize adrenal and pituitary disorders, and assess bone metabolism.",
        "devin_body": r'''
## When to use

You are modeling endocrine disorders such as diabetes, thyroid disease, adrenal/pituitary lesions, osteoporosis, or polycystic ovary syndrome from EHR, imaging, wearable, or lab data.

## Usage

- Forecast continuous glucose monitor time series and insulin-dose response.
- Risk-stratify thyroid nodules from ultrasound TI-RADS features and cytology.
- Characterize adrenal and pituitary incidentalomas and hormone excess or deficiency.
- Predict fracture risk and bone density trends from clinical and imaging data.

## Steps

1. Collect CGM, EHR, lab, imaging, and wearable data for the target endocrine condition.
2. Define clinically relevant prediction windows and thresholds (e.g., hypoglycemia).
3. Train time-series or image models and validate temporally across devices and age groups.
4. Integrate predictions into insulin dosing, referral, or screening workflows.
5. Calibrate around decision thresholds and evaluate subgroup performance.
6. Prospectively validate in endocrine clinics and update as standards change.

## Code pattern

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Forecast next CGM value from a window of past readings
cgm_window = np.array([[120, 125, 132, 138, 145]])  # mg/dL
y = np.array([148])

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(cgm_window, y)
pred = model.predict([[125, 132, 138, 145, 150]])
print("Predicted glucose:", pred[0])
```

## Tuning notes

- Respect temporal structure in CGM and avoid data leakage from meal/bolus events.
- Thyroid models must handle class imbalance and high-resolution ultrasound variability.
- Calibrate predictions around clinically relevant thresholds (e.g., hypoglycemia <70 mg/dL).
- Validate across devices, patient age groups, and pregnancy status.

## Verification

1. Build a 30-minute glucose forecast and report MAE against a naive persistence model.
2. Train a thyroid nodule malignancy classifier with ultrasound features and compare to TI-RADS.
3. Predict 10-year osteoporotic fracture risk from clinical and bone-density data.
        ''',
        "references": [
            "https://doi.org/10.1007/s12020-025-04378-6",
            "https://pubmed.ncbi.nlm.nih.gov/37971630/",
            "https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2025.1578455/full",
            "https://doi.org/10.5937/mgiszm2495039k",
        ],
    },
    {
        "name": "ai-for-hematology",
        "title": "AI for Hematology",
        "description": "Use machine learning to classify blood cells, predict leukemia and lymphoma outcomes, and optimize transfusion and transplant care.",
        "devin_body": r'''
## When to use

You are analyzing peripheral blood smears, bone marrow samples, coagulation data, or transplant registries to improve hematologic diagnosis, risk stratification, and treatment planning.

## Usage

- Automate blood smear differential and classify anemia from CBC and iron studies.
- Integrate morphology, immunophenotyping, cytogenetics, and molecular data (MICM).
- Predict thrombosis, bleeding, and transfusion need from labs and EHR.
- Model risk in AML/MDS, lymphoma subtyping, and measurable residual disease.
- Predict engraftment, GVHD, and relapse in stem-cell transplants.

## Steps

1. Assemble CBC, smear images, flow cytometry, genetic, and EHR data.
2. Define prediction or classification targets (anemia type, blast detection, VTE, relapse).
3. Train models with class imbalance handling and stain normalization.
4. Validate against manual differential counts, flow cytometry, or expert review.
5. Integrate results into hematology lab and transplant workflows.
6. Monitor rare-class recall and multicenter drift.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Classify anemia type from CBC and iron/B12/folate labs
X = df[["hemoglobin", "mcv", "ferritin", "b12", "folate", "rdw"]]
y = df["anemia_type"]

model = GradientBoostingClassifier(random_state=42)
model.fit(X, y)
print("Feature importances:", model.feature_importances_)
```

## Tuning notes

- Hematologic conditions are often rare; use stratified sampling and class-weighted loss.
- Stain and scanner differences in smear images require domain adaptation or stain normalization.
- Distinguish transfusion effect from disease-related changes in sequential CBCs.
- Validate against manual differential counts and flow cytometry.

## Verification

1. Classify anemia type from CBC and iron studies and compare to hematologist review.
2. Predict VTE risk in hospitalized patients and report precision-recall at high-risk thresholds.
3. Segment and classify blast cells in peripheral smear images with pathologist-annotated ground truth.
        ''',
        "references": [
            "https://doi.org/10.1182/blood.2025029876",
            "https://link.springer.com/article/10.1007/s00277-025-06706-2",
            "https://doi.org/10.1016/j.cll.2025.07.011",
            "https://doi.org/10.4103/kkujhs.kkujhs_42_25",
        ],
    },
    {
        "name": "ai-for-infectious-disease",
        "title": "AI for Infectious Disease",
        "description": "Use machine learning to identify pathogens, predict antimicrobial resistance, detect sepsis, and monitor disease outbreaks.",
        "devin_body": r'''
## When to use

You need to detect sepsis early, predict antimicrobial resistance, identify pathogens from clinical or genomic data, or forecast infectious disease spread and outbreak dynamics.

## Usage

- Build EHR-based early-warning models for sepsis and time-to-antibiotics.
- Predict antimicrobial resistance from genomic markers, culture data, and phenotypes.
- Identify pathogens from MALDI-TOF, 16S/NGS, and metagenomic data.
- Optimize antibiotic stewardship with dosing, de-escalation, and drug-target predictions.
- Forecast outbreak spread with time-series and mobility models.

## Steps

1. Collect EHR, genomic, microbiology, and surveillance data for the target infection.
2. Define labels carefully to avoid leakage from cultures drawn after suspicion.
3. Train classifiers or genomic AMR models with appropriate feature representations.
4. Validate alert lead time, false-positive burden, and calibration.
5. Integrate predictions into stewardship, triage, or public-health dashboards.
6. Monitor for pathogen and resistance drift and update the model.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Sepsis early-warning model from structured EHR
X = df[["heart_rate", "resp_rate", "temp", "wbc", "lactate", "creatinine"]]
y = df["sepsis_next_6h"]

model = GradientBoostingClassifier(random_state=42)
model.fit(X, y)
df["sepsis_risk"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Time-to-antibiotic is critical; validate alert lead time and false-positive burden.
- Avoid label leakage from cultures drawn after suspicion of sepsis.
- Genomic AMR models benefit from k-mer or gene-family feature representations.
- Monitor for concept drift as pathogens and resistance patterns evolve.

## Verification

1. Build a 6-hour sepsis prediction model with time-based cross-validation and report AUROC.
2. Predict phenotypic antibiotic resistance from assembled genome k-mers and compare to AST.
3. Forecast weekly influenza-like illness at the regional level and evaluate against surveillance data.
        ''',
        "references": [
            "https://doi.org/10.1038/s44259-024-00068-x",
            "https://www.nature.com/articles/s44259-025-00085-4",
            "https://www.mdpi.com/2075-4418/15/15/1890",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12573687/",
        ],
    },
    {
        "name": "ai-for-rheumatology",
        "title": "AI for Rheumatology",
        "description": "Use machine learning to phenotype autoimmune disease, predict flares, forecast treatment response, and score joint inflammation.",
        "devin_body": r'''
## When to use

You are studying rheumatoid arthritis, systemic lupus erythematosus, spondyloarthritis, or other autoimmune rheumatic diseases and need predictive models for diagnosis, flares, or therapy selection.

## Usage

- Model disease activity with DAS28, CDAI, SLEDAI, and patient-reported outcomes.
- Integrate genetics, transcriptomics, cytokines, and autoantibody panels.
- Score ultrasound, MRI, and radiographic joint damage and inflammation.
- Predict response to biologics or JAK inhibitors and adverse events.
- Forecast flares from temporal clinical, lab, and patient-reported data.

## Steps

1. Curate EHR, multi-omics, imaging, and patient-reported data for the target rheumatic disease.
2. Define outcomes (flare, response, damage) and time windows for prediction.
3. Train predictive or image models and validate externally across sites.
4. Integrate predictions into treatment selection and flare monitoring workflows.
5. Address confounding from treatment effects using causal or time-varying methods.
6. Report subgroup performance and iterate with rheumatologist feedback.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Predict RA treatment response from clinical and serologic features
X = df[["das28", "crp", "rf", "anti_ccp", "prior_biologic", "erosion_count"]]
y = df["responded_to_tnf_inhibitor"]

model = RandomForestClassifier(class_weight="balanced", random_state=42)
model.fit(X, y)
print("Response probability:", model.predict_proba(X[:5])[:, 1])
```

## Tuning notes

- Rheumatic diseases are heterogeneous and low prevalence; use external validation.
- Treatment effects confound natural history; use causal or time-varying models.
- Imaging acquisition varies by machine and operator; normalize or calibrate across sites.
- Report subgroup performance by sex, ethnicity, and disease duration.

## Verification

1. Predict 12-month RA flare from EHR and patient-reported outcomes.
2. Classify SLE disease activity level and compare to SLEDAI scoring.
3. Quantify synovitis from ultrasound videos and validate against rheumatologist scores.
        ''',
        "references": [
            "https://doi.org/10.3390/rheumato5040017",
            "https://lupus.bmj.com/content/11/1/e001140",
            "https://www.jrheum.org/content/49/11/1191",
            "https://doi.org/10.7759/cureus.99108",
        ],
    },
    {
        "name": "ai-for-allergy-immunology",
        "title": "AI for Allergy and Immunology",
        "description": "Use machine learning to phenotype asthma, predict exacerbations, assess allergy risk, and screen immunodeficiency.",
        "devin_body": r'''
## When to use

You are modeling asthma, allergic rhinitis, atopic dermatitis, food or drug allergy, anaphylaxis risk, or primary immunodeficiency from clinical, wearable, laboratory, or genomic data.

## Usage

- Cluster asthma phenotypes by inflammation, spirometry, FeNO, and exacerbation patterns.
- Predict asthma exacerbations from environmental, medication, and physiological triggers.
- Interpret skin-prick, specific IgE, component-resolved diagnostics, and oral challenge data.
- Predict drug and food allergy risk and anaphylaxis severity.
- Screen primary immunodeficiency from infection history, cell counts, and genomics.

## Steps

1. Collect clinical, wearable, lab, genomic, and environmental data for the target allergy or immune condition.
2. Define outcomes (exacerbation, reaction severity, immunodeficiency flag) and windows.
3. Train models with seasonality, device standardization, and class imbalance in mind.
4. Validate against challenge-based labels and clinical expert review.
5. Integrate predictions into asthma action plans, allergy clinics, or screening tools.
6. Monitor pediatric and adult differences and update as immunological understanding evolves.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Predict asthma exacerbation in next 30 days
X = df[["fev1_fvc", "feNO", "exacerbations_12m", "ics_adherence", "smoking"]]
y = df["exacerbation_next_30d"]

model = GradientBoostingClassifier(random_state=42)
model.fit(X, y)
df["exacerbation_risk"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Seasonality and pollen/viral circulation affect asthma; include calendar features.
- Spirometry and FeNO devices vary; standardize by device and pediatric norms.
- Allergy outcomes are often self-reported; use challenge-based labels when possible.
- Pediatric and adult populations may need separate models.

## Verification

1. Predict 30-day asthma exacerbation and evaluate calibration across seasons.
2. Cluster asthma phenotypes and compare to Type-2 inflammation biomarkers.
3. Predict peanut allergy reaction severity from skin test, IgE, and component panels.
        ''',
        "references": [
            "https://doi.org/10.1016/j.jaci.2025.08.022",
            "https://doi.org/10.1111/all.15849",
            "https://www.sciencedirect.com/science/article/abs/pii/S2213219825005094",
            "https://erj.ersjournals.com/content/56/3/2000521",
        ],
    },
    {
        "name": "ai-for-plastic-surgery",
        "title": "AI for Plastic Surgery",
        "description": "Use machine learning to plan aesthetic and reconstructive surgery, assess outcomes, monitor flaps, and analyze craniofacial images.",
        "devin_body": r'''
## When to use

You are planning aesthetic or reconstructive procedures, predicting surgical outcomes, monitoring free flaps, or analyzing craniofacial images and patient-reported outcome measures.

## Usage

- Analyze 3D surface imaging and photogrammetry for facial and breast symmetry.
- Monitor free-tissue transfer flaps with computer vision and perfusion signals.
- Predict patient-reported satisfaction, scar quality, and complications.
- Assess wound and burn depth, infection, and healing trajectory from images.
- Measure craniofacial landmarks, dysmorphology, and growth.

## Steps

1. Collect de-identified 3D scans, photos, perfusion data, and patient-reported outcomes.
2. Define endpoints (complication, symmetry score, healing stage) with expert consensus.
3. Train segmentation, regression, or classification models on standardized images.
4. Validate against surgeon and patient ratings and across multicenter data.
5. Integrate tools into surgical planning, flap monitoring, or follow-up workflows.
6. Ensure privacy, consent, and standardization of acquisition protocols.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Predict breast reconstruction complication risk from preoperative features
X = df[["bmi", "smoking", "radiation_history", "age", "implant"]]
y = df["postop_complication"]

model = RandomForestClassifier(class_weight="balanced", random_state=42)
model.fit(X, y)
print("Complication risk:", model.predict_proba(X[:3])[:, 1])
```

## Tuning notes

- Plastic surgery images carry privacy and identity concerns; de-identify and secure consent.
- Aesthetic endpoints are subjective; validate against multiple surgeon and patient ratings.
- Small, single-center datasets limit generalizability; use multicenter or federated learning.
- Postoperative photos vary by lighting and pose; standardize acquisition.

## Verification

1. Predict a postoperative complication within 30 days of breast reconstruction.
2. Measure facial symmetry from 3D surface scans and compare to expert ratings.
3. Implement a free-flap monitoring pipeline from perfusion images or signals.
        ''',
        "references": [
            "https://doi.org/10.1016/j.jpra.2024.09.003",
            "https://www.frontiersin.org/journals/surgery/articles/10.3389/fsurg.2025.1640588/full",
            "https://pubmed.ncbi.nlm.nih.gov/41614695/",
            "https://doi.org/10.1007/s40137-026-00510-1",
        ],
    },
    {
        "name": "ai-for-orthopedics",
        "title": "AI for Orthopedics",
        "description": "Use machine learning to detect fractures, grade osteoarthritis, predict joint replacement outcomes, and plan orthopedic surgery.",
        "devin_body": r'''
## When to use

You are interpreting musculoskeletal imaging, predicting fracture risk or arthroplasty outcomes, grading osteoarthritis, or planning orthopedic surgery and rehabilitation.

## Usage

- Detect and classify fractures on radiographs and CT.
- Grade osteoarthritis with Kellgren-Lawrence, joint-space narrowing, and cartilage segmentation.
- Predict implant survival, revision risk, readmission, and patient-reported outcomes.
- Analyze sports and spine injuries (ACL, meniscus, rotator cuff, scoliosis).
- Support patient-specific templating, bone age, and 3D-printed instrumentation.

## Steps

1. Gather musculoskeletal imaging, EHR, and patient-reported outcome data.
2. Standardize image acquisition and annotate fracture, joint, or cartilage findings.
3. Train detection, segmentation, or regression models with augmentation and class imbalance.
4. Validate across hospitals, age groups, trauma centers, and implant vendors.
5. Integrate predictions into emergency triage, surgical planning, or follow-up.
6. Monitor for metal artifacts and positioning variability.

## Code pattern

```python
import torch
from torchvision.models import resnet18

# Fine-tune a ResNet for hip fracture detection on AP pelvis radiographs
model = resnet18(weights="DEFAULT")
model.fc = torch.nn.Linear(model.fc.in_features, 2)

# images is a Tensor of shape (B, 3, 224, 224)
out = model(images)
print("Fracture logits:", out[:3])
```

## Tuning notes

- Musculoskeletal imaging varies by patient positioning, hardware, and vendor; use augmentation.
- Fracture classes are imbalanced; evaluate with sensitivity at a fixed false-positive rate.
- External validation across hospitals, age groups, and trauma centers is essential.
- Implants create metal artifacts; isolate bone and implant regions when needed.

## Verification

1. Train a fracture-detection model on radiographs and compare sensitivity to emergency physicians.
2. Predict 90-day readmission after total joint arthroplasty from EHR features.
3. Segment knee cartilage on MRI and report Dice versus manual segmentations.
        ''',
        "references": [
            "https://doi.org/10.1002/jeo2.70549",
            "https://doi.org/10.3390/jcm15062165",
            "https://doi.org/10.1186/s43019-026-00317-5",
            "https://boneandjoint.org.uk/Article/10.1302/2633-1462.51.BJO-2023-0095.R1",
        ],
    },
    {
        "name": "ai-for-physical-medicine",
        "title": "AI for Physical Medicine",
        "description": "Use machine learning to interpret electrodiagnostic studies, musculoskeletal ultrasound, gait, and prosthetics data in physiatry.",
        "devin_body": r'''
## When to use

You are interpreting EMG and nerve conduction studies, musculoskeletal ultrasound, gait and balance data, or planning rehabilitation and assistive devices in physical medicine and rehabilitation.

## Usage

- Classify EMG and nerve conduction signals for neuropathic and myopathic patterns.
- Segment and detect pathology in tendon, ligament, nerve, and muscle ultrasound.
- Analyze gait, balance, and motion from IMUs, pressure sensors, and 3D capture.
- Decode myoelectric control intent and adapt prosthetics and orthotics.
- Predict functional assessment scores and rehabilitation outcomes.

## Steps

1. Collect EMG, nerve conduction, ultrasound, wearable, and functional assessment data.
2. Standardize recording parameters and filter motion artifacts.
3. Train signal, image, or time-series models for diagnosis or control.
4. Validate against electrophysiologist readings, instrumented walkways, or clinician scores.
5. Integrate into prosthetic control, gait analysis, or diagnostic workflows.
6. Ensure low latency for real-time control and adapt to individual patients.

## Code pattern

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Classify EMG pattern as neuropathic or myopathic from extracted features
X = df[["amplitude", "duration", "phases", "turns", "fibrillations"]]
y = df["emg_diagnosis"]

model = RandomForestClassifier(class_weight="balanced", random_state=42)
model.fit(X, y)
print("Predicted diagnoses:", model.predict(X[:5]))
```

## Tuning notes

- EMG and nerve conduction studies are operator dependent; standardize recording parameters.
- MSK ultrasound requires operator calibration; train on matched transducers and presets.
- Wearable gait data are noisy; filter motion artifacts and sensor drift.
- Functional outcome scales are ordinal; consider ordinal regression or survival models.

## Verification

1. Classify myopathic versus neuropathic EMG from motor-unit features.
2. Detect median nerve entrapment from musculoskeletal ultrasound images.
3. Predict prosthesis control intent from surface EMG with real-time latency metrics.
        ''',
        "references": [
            "https://journals.lww.com/ajpmr/fulltext/2019/11000/artificial_intelligence_and_applications_in_pm_r.18.aspx",
            "https://doi.org/10.1002/mus.28023",
            "https://doi.org/10.1007/s11547-024-01856-1",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC7758096/",
        ],
    },
    {
        "name": "ai-for-rehabilitation",
        "title": "AI for Rehabilitation",
        "description": "Use machine learning to predict recovery, personalize therapy, monitor home rehabilitation, and control assistive devices.",
        "devin_body": r'''
## When to use

You are predicting functional recovery, personalizing therapy dose, monitoring home-based rehabilitation, or controlling robotic, VR, or brain-computer interface systems for rehabilitation.

## Usage

- Predict functional recovery trajectories after stroke, spinal cord, or brain injury.
- Monitor rehabilitation with IMUs, sEMG, pressure insoles, and smartphones.
- Adapt robotic and VR therapy difficulty based on performance.
- Support telerehabilitation with remote exercise monitoring and digital coaching.
- Decode movement intent for brain-computer interfaces and neurofeedback.

## Steps

1. Collect baseline assessments, wearable data, and therapy logs for the target population.
2. Define recovery or adherence outcomes and appropriate time windows.
3. Train missing-data-aware models and handle engagement as a confounder.
4. Validate against standardized scales and functional tests.
5. Integrate into adaptive robotic or VR therapy or telerehabilitation platforms.
6. Monitor adherence, dropout, and generalizability across care settings.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict FIM motor gain from baseline and sensor-derived gait features
X = df[["baseline_fim", "days_since_onset", "gait_speed", "balance", "age"]]
y = df["fim_gain_90d"]

model = GradientBoostingRegressor(random_state=42)
model.fit(X, y)
print("Predicted FIM gain:", model.predict(X[:3]))
```

## Tuning notes

- Home-based data are sparse and variable; use missing-data-aware models.
- Patient adherence is a strong confounder; measure and report engagement.
- Functional scales are ordinal and may plateau; use appropriate metrics (MAE, Spearman).
- Equitable access to wearables and internet affects generalizability.

## Verification

1. Predict 90-day FIM motor gain after stroke from baseline and wearable data.
2. Classify gait phases from IMU signals and compare to instrumented walkway.
3. Evaluate a telerehabilitation AI for exercise completion and adherence.
        ''',
        "references": [
            "https://pubmed.ncbi.nlm.nih.gov/41424220/",
            "https://doi.org/10.3389/fdgth.2026.1737957",
            "https://doi.org/10.1007/s10916-026-02400-6",
            "https://doi.org/10.1186/s12984-025-01605-z",
        ],
    },
    {
        "name": "ai-for-anesthesiology",
        "title": "AI for Anesthesiology",
        "description": "Use machine learning to stratify preoperative risk, monitor hemodynamics, predict nausea and pain, and support closed-loop anesthesia.",
        "devin_body": r'''
## When to use

You are predicting perioperative risk, monitoring hemodynamics or anesthetic depth, optimizing pain and PONV prophylaxis, or building closed-loop control for anesthetic delivery.

## Usage

- Assess preoperative risk with ASA status, frailty, and comorbidity indices.
- Predict intraoperative hypotension and interpret arterial waveforms and EEG/BIS depth.
- Model pharmacokinetics and pharmacodynamics for target-controlled infusion.
- Predict postoperative nausea/vomiting and pain to guide multimodal analgesia.
- Support real-time closed-loop anesthetic, vasopressor, and fluid control.

## Steps

1. Integrate EHR, high-frequency waveforms, and anesthesia machine data.
2. Define prediction windows and clinical thresholds (e.g., hypotension within 15 minutes).
3. Train models with time-series features and calibrate probabilities for rare events.
4. Validate alarm lead time and false-positive burden with anesthesiologists.
5. Integrate into decision support or closed-loop control with safety limits.
6. Monitor latency and adapt to patient populations and surgical types.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Predict postoperative nausea and vomiting from patient and procedure features
X = df[["female", "nonsmoker", "history_ponv", "opioid_dose", "surgery_duration"]]
y = df["ponv"]

model = GradientBoostingClassifier(random_state=42)
model.fit(X, y)
print("PONV risk:", model.predict_proba(X[:3])[:, 1])
```

## Tuning notes

- High-frequency waveforms require careful feature engineering or deep learning on time windows.
- Many outcomes are rare and imbalanced; calibrate probability outputs for clinical thresholds.
- Real-time inference must meet latency and alarm-fatigue constraints.
- Integrate with anesthesia machines and EHR through validated, fault-tolerant interfaces.

## Verification

1. Predict intraoperative hypotension from arterial waveform features within a 15-minute horizon.
2. Build a PONV risk model and compare risk calibration to Apfel score.
3. Simulate a closed-loop propofol controller and evaluate stability and overshoot.
        ''',
        "references": [
            "https://link.springer.com/article/10.1007/s10877-026-01434-y",
            "https://doi.org/10.1177/03000605261454051",
            "https://link.springer.com/article/10.1186/s12871-024-02699-z",
            "https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1811197/full",
        ],
    },
    {
        "name": "ai-for-pain-management",
        "title": "AI for Pain Management",
        "description": "Use machine learning to phenotype chronic pain, predict treatment and opioid response, guide procedures, and support self-management.",
        "devin_body": r'''
## When to use

You are phenotyping chronic pain, predicting treatment response, assessing opioid misuse risk, guiding interventional procedures, or building self-management and digital-therapeutic tools.

## Usage

- Phenotype chronic pain by nociceptive, neuropathic, inflammatory, and centralized mechanisms.
- Predict response to physical therapy, CBT, medications, and neuromodulation.
- Assess opioid misuse, overdose, and dependence risk from EHR and psychosocial data.
- Guide nerve blocks and spinal procedures with ultrasound or fluoroscopy segmentation.
- Support digital diaries, CBT, and biofeedback for self-management.

## Steps

1. Collect validated pain scores, EHR, medication, psychosocial, and imaging data.
2. Define outcomes (phenotype, treatment response, opioid risk) and windows.
3. Train clustering, prediction, or segmentation models with class imbalance and missing data.
4. Validate against PROMIS/BPI and clinician assessments.
5. Integrate into multidisciplinary pain program and procedural planning.
6. Audit for fairness and avoid stigmatizing patients by pain condition or opioids.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Predict favorable response to multidisciplinary pain program
X = df[["pain_duration", "pain_intensity", "depression_score", "opioid_use", "disability"]]
y = df["responded_to_program"]

model = GradientBoostingClassifier(random_state=42)
model.fit(X, y)
print("Response probability:", model.predict_proba(X[:3])[:, 1])
```

## Tuning notes

- Pain is subjective and multidimensional; use validated PROMIS/BPI outcomes.
- Avoid stigmatizing opioid users; evaluate fairness across pain conditions and demographics.
- Missing data are common in self-reported diaries; use imputation or missingness indicators.
- Longitudinal pain trajectories may need joint models or time-to-event approaches.

## Verification

1. Cluster chronic low-back pain patients into clinically meaningful phenotypes.
2. Predict opioid misuse risk in a chronic pain population and audit false positives.
3. Predict response to a combined physical-therapy and CBT program versus usual care.
        ''',
        "references": [
            "https://doi.org/10.1002/ejp.4748",
            "https://doi.org/10.3390/app11073205",
            "https://pubmed.ncbi.nlm.nih.gov/38345695/",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC8681085/",
        ],
    },
]