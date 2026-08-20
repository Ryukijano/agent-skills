SKILLS = [
    {
        "name": "ai-for-nephrology",
        "title": "AI for Nephrology",
        "description": "Machine learning for chronic kidney disease progression, acute kidney injury prediction, dialysis adequacy, kidney transplant outcomes, and renal pathology image analysis.",
        "devin_body": r'''## When to use

You are building models to predict CKD progression, detect acute kidney injury early, optimize dialysis, allocate kidneys, or analyze renal biopsy and histopathology images.

## Key concepts

- **CKD risk stratification**: eGFR trajectory, albuminuria, and comorbidity-driven models for progression to ESKD.
- **AKI early warning**: EHR-based vitals, labs, and medication triggers for in-hospital AKI.
- **Dialysis optimization**: treatment adequacy, access failure prediction, and personalized ultrafiltration.
- **Transplant analytics**: donor-recipient matching, rejection risk, and graft survival prediction.
- **Renal pathology AI**: segmentation and classification of glomerular lesions in biopsy images.

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
        "description": "Machine learning for diabetes prediction and glucose forecasting, thyroid nodule risk stratification, adrenal and pituitary disorders, and bone mineral metabolism.",
        "devin_body": r'''## When to use

You are modeling endocrine disorders such as diabetes, thyroid disease, adrenal/pituitary lesions, osteoporosis, or polycystic ovary syndrome from EHR, imaging, wearable, or lab data.

## Key concepts

- **Diabetes and CGM**: continuous glucose monitor time series, HbA1c, and insulin-dose forecasting.
- **Thyroid nodule risk**: ultrasound TI-RADS features, cytology, and molecular testing for malignancy.
- **Adrenal and pituitary**: incidentaloma characterization and hormone excess/deficiency patterns.
- **Bone and mineral**: fracture risk, bone density trends, and calcium-phosphate metabolism.
- **Phenotyping**: subtyping endocrine patients with clustering and multimodal fusion.

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
        "description": "Machine learning for blood cell morphology, leukemia and lymphoma classification, thrombosis and bleeding risk, transfusion optimization, and stem-cell transplant outcomes.",
        "devin_body": r'''## When to use

You are analyzing peripheral blood smears, bone marrow samples, coagulation data, or transplant registries to improve hematologic diagnosis, risk stratification, and treatment planning.

## Key concepts

- **CBC and smear morphology**: automated differential, anemia classification, and blast detection.
- **MICM classification**: integration of morphology, immunophenotyping, cytogenetics, and molecular data.
- **Coagulation and thrombosis**: VTE, bleeding, and transfusion-need prediction from labs and EHR.
- **Hematologic malignancies**: AML/MDS risk, lymphoma subtyping, and MRD monitoring.
- **Transplant analytics**: engraftment, GVHD, and relapse risk in stem-cell transplants.

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
        "description": "Machine learning for pathogen identification, antimicrobial resistance prediction, sepsis early warning, and infectious disease outbreak surveillance.",
        "devin_body": r'''## When to use

You need to detect sepsis early, predict antimicrobial resistance, identify pathogens from clinical or genomic data, or forecast infectious disease spread and outbreak dynamics.

## Key concepts

- **Sepsis early warning**: EHR-based models using vitals, labs, and demographics for timely antibiotics.
- **AMR prediction**: genomic markers, culture data, and phenotypic resistance forecasting.
- **Pathogen identification**: MALDI-TOF, 16S/NGS, and metagenomic classification.
- **Antibiotic stewardship**: dosing optimization, de-escalation, and drug-target interaction prediction.
- **Epidemiological surveillance**: time-series and mobility models for outbreak detection.

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
        "description": "Machine learning for autoimmune disease diagnosis and phenotyping, flare prediction, treatment response in RA and SLE, and imaging-based joint inflammation scoring.",
        "devin_body": r'''## When to use

You are studying rheumatoid arthritis, systemic lupus erythematosus, spondyloarthritis, or other autoimmune rheumatic diseases and need predictive models for diagnosis, flares, or therapy selection.

## Key concepts

- **Disease activity indices**: DAS28, CDAI, SLEDAI, and patient-reported outcomes.
- **Multi-omics integration**: genetics, transcriptomics, cytokines, and autoantibody panels.
- **Imaging biomarkers**: ultrasound power Doppler, MRI synovitis/erosion, and radiographic damage.
- **Treatment response**: prediction of biologic or JAK inhibitor response and adverse events.
- **Flare prediction**: temporal clustering of clinical, lab, and patient-reported signals.

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
        "description": "Machine learning for asthma phenotyping and exacerbation prediction, allergic rhinitis and food/drug allergy risk, anaphylaxis, and primary immunodeficiency screening.",
        "devin_body": r'''## When to use

You are modeling asthma, allergic rhinitis, atopic dermatitis, food or drug allergy, anaphylaxis risk, or primary immunodeficiency from clinical, wearable, laboratory, or genomic data.

## Key concepts

- **Asthma phenotyping**: clustering by inflammation, spirometry, FeNO, and exacerbation patterns.
- **Exacerbation prediction**: environmental, medication, and physiological triggers.
- **Allergy diagnostics**: skin-prick tests, specific IgE, component-resolved diagnostics, and oral food challenges.
- **Drug and food allergy risk**: medication exposure, reaction history, and biologics.
- **Immunodeficiency screening**: infection frequency, immune cell counts, and genomic variants.

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
        "description": "Machine learning for aesthetic and reconstructive surgical planning, facial analysis, flap monitoring, wound assessment, and patient-reported outcomes.",
        "devin_body": r'''## When to use

You are planning aesthetic or reconstructive procedures, predicting surgical outcomes, monitoring free flaps, or analyzing craniofacial images and patient-reported outcome measures.

## Key concepts

- **3D surface imaging and photogrammetry**: facial and breast symmetry, volumetric change, and surgical simulation.
- **Flap monitoring**: computer vision and perfusion signal analysis for free-tissue transfer.
- **Aesthetic outcome prediction**: patient-reported satisfaction, scar quality, and complications.
- **Wound and burn assessment**: image-based depth, infection, and healing trajectory.
- **Craniofacial analysis**: cephalometric landmarks, dysmorphology, and growth prediction.

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
        "description": "Machine learning for fracture detection and classification, osteoarthritis grading, joint replacement outcomes, spine analysis, and sports injury risk.",
        "devin_body": r'''## When to use

You are interpreting musculoskeletal imaging, predicting fracture risk or arthroplasty outcomes, grading osteoarthritis, or planning orthopedic surgery and rehabilitation.

## Key concepts

- **Fracture detection and classification**: deep learning on radiographs for trauma, osteoporosis, and pediatric fractures.
- **Osteoarthritis grading**: Kellgren-Lawrence, joint-space narrowing, and cartilage segmentation from MRI.
- **Arthroplasty outcomes**: implant survival, revision risk, readmission, and patient-reported outcomes.
- **Sports and spine**: ACL, meniscus, rotator cuff, scoliosis, and disc degeneration.
- **Patient-specific planning**: bone age, templating, and 3D-printed instrumentation.

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
        "description": "Machine learning for electrodiagnostic studies, musculoskeletal ultrasound, gait and motion analysis, prosthetics/orthotics, and functional assessment in physiatry.",
        "devin_body": r'''## When to use

You are interpreting EMG and nerve conduction studies, musculoskeletal ultrasound, gait and balance data, or planning rehabilitation and assistive devices in physical medicine and rehabilitation.

## Key concepts

- **Electrodiagnostics**: EMG signal classification, motor-unit action potentials, and nerve conduction parameter prediction.
- **Musculoskeletal ultrasound**: automated tendon, ligament, nerve, and muscle segmentation and pathology detection.
- **Gait and motion analysis**: inertial measurement units, pressure sensors, and 3D motion capture.
- **Prosthetics and orthotics**: myoelectric control intent and exoskeleton adaptation.
- **Functional assessment**: FIM, Barthel, and disability-specific outcome prediction.

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
        "description": "Machine learning for stroke, spinal cord, and traumatic brain injury rehabilitation, robotic and virtual-reality therapy, telerehabilitation, and wearable sensor monitoring.",
        "devin_body": r'''## When to use

You are predicting functional recovery, personalizing therapy dose, monitoring home-based rehabilitation, or controlling robotic, VR, or brain-computer interface systems for rehabilitation.

## Key concepts

- **Functional recovery prediction**: FIM, Barthel, WMFT, and gait-speed trajectories after stroke or SCI.
- **Wearable and sensor-based monitoring**: IMUs, sEMG, pressure insoles, and smartphone activity.
- **Robotic and VR therapy**: adaptive difficulty, performance-based dosing, and motor-learning feedback.
- **Telerehabilitation**: remote exercise monitoring, adherence prediction, and digital coaching.
- **Brain-computer interfaces**: movement intent decoding and neurofeedback.

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
        "description": "Machine learning for preoperative risk stratification, intraoperative hemodynamic monitoring, anesthetic depth, postoperative nausea and pain, and closed-loop anesthesia.",
        "devin_body": r'''## When to use

You are predicting perioperative risk, monitoring hemodynamics or anesthetic depth, optimizing pain and PONV prophylaxis, or building closed-loop control for anesthetic delivery.

## Key concepts

- **Preoperative risk assessment**: ASA status, frailty, comorbidity indices, and procedure-specific complication models.
- **Intraoperative monitoring**: hypotension prediction index, arterial waveform analysis, and BIS/EEG depth monitoring.
- **Pharmacokinetic and pharmacodynamic modeling**: target-controlled infusion and individual dose-response.
- **PONV and pain prediction**: risk scores and multimodal analgesia planning.
- **Closed-loop control**: real-time anesthetic, vasopressor, and fluid administration.

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
        "description": "Machine learning for chronic pain phenotyping, opioid and analgesic response prediction, procedural guidance, and patient self-management and monitoring.",
        "devin_body": r'''## When to use

You are phenotyping chronic pain, predicting treatment response, assessing opioid misuse risk, guiding interventional procedures, or building self-management and digital-therapeutic tools.

## Key concepts

- **Pain phenotyping**: clustering by nociceptive, neuropathic, inflammatory, and centralized mechanisms.
- **Treatment response prediction**: response to physical therapy, CBT, medications, and neuromodulation.
- **Opioid risk assessment**: misuse, overdose, and dependence prediction from EHR and psychosocial data.
- **Procedural guidance**: ultrasound or fluoroscopy image segmentation for nerve blocks and spinal procedures.
- **Self-management**: digital diaries, cognitive behavioral interventions, and biofeedback.

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
