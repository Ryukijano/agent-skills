# Wave 39: AI in Social Impact and Development
SKILLS = [
    {
        "name": "ai-for-poverty-alleviation",
        "title": "AI for Poverty Alleviation",
        "description": "Use machine learning to map poverty, estimate consumption, target social transfers, and improve social protection in low-resource settings.",
        "devin_body": r'''
## When to use

You need to estimate economic well-being, target cash transfers, or map poverty at high spatial resolution where traditional survey data are sparse or outdated.

## Usage

- Combine satellite imagery, nighttime lights, and built-environment features with household surveys.
- Build proxy means testing scoring to identify eligible beneficiaries.
- Use mobile data such as call-detail records and airtime as proxies for income shocks.
- Monitor exclusion and inclusion errors across gender, ethnicity, and geography.

## Steps

1. Assemble household surveys, geospatial layers, and mobile or administrative data.
2. Train consumption or wealth prediction models with spatial or temporal cross-validation.
3. Use predictions to produce high-resolution poverty maps and rank households for targeting.
4. Measure targeting quality by exclusion/inclusion errors and coverage of the poorest quintile.
5. Audit for disparities and protect sensitive mobile/geospatial data.
6. Integrate with government or NGO targeting systems and update as conditions change.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# Predict consumption expenditure from satellite and demographic features
X = df[["nighttime_lights", "road_density", "building_count", "vegetation_index", "hh_size"]]
y = df["consumption_per_capita"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = GradientBoostingRegressor(random_state=42).fit(X_train, y_train)
```

## Tuning notes

- Use cross-validation with spatial or temporal splits; poverty features are highly correlated across nearby villages.
- Down-weight nighttime lights where electrification is uneven; include daytime texture features.
- Validate targeting quality by exclusion/inclusion error, not just R2.
- Protect sensitive mobile and geospatial data with differential privacy or aggregation.

## Verification

1. Replicate a small-area poverty map and compare it to a recent census or survey estimate.
2. Train a PMT and measure how well it captures the poorest quintile in a holdout region.
3. Audit the model for disparities across protected groups before deployment.
        ''',
        "references": [
            "https://www.science.org/doi/10.1126/science.aaf7894",
            "https://pubmed.ncbi.nlm.nih.gov/35914150/",
            "https://www.nature.com/articles/s41586-022-05422-504484-9",
            "https://doi.org/10.1257/aer.20221650",
            "https://arxiv.org/abs/2202.00109",
        ],
    },
    {
        "name": "ai-for-hunger-relief",
        "title": "AI for Hunger Relief",
        "description": "Use AI/ML to forecast food insecurity, monitor crops, and target emergency food assistance.",
        "devin_body": r'''
## When to use

You are building or improving early warning systems for famine, food-insecurity phase classification, or allocation of emergency food assistance.

## Usage

- Forecast Integrated Food Security Phase Classification (IPC) phases.
- Use NDVI/EVI, rainfall (CHIRPS), and temperature as crop-failure signals.
- Incorporate cereal prices, market access, and conflict events into short-term forecasts.
- Collect high-frequency food consumption and coping-strategy data via mobile surveys.

## Steps

1. Gather IPC, remote-sensing, market, conflict, and survey data for the target region.
2. Build a time-series or classification model for food-insecurity phase transitions.
3. Use time-based splits and avoid leakage from future market prices.
4. Calibrate probabilities to match donor and response budgets.
5. Combine model outputs with expert judgment and maintain human escalation paths.
6. Backtest against official IPC assessments and refine as shocks evolve.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Classify food-insecurity phase from agro-climatic and market features
X = df[["ndvi_anomaly", "rainfall_deficit", "cereal_price_index", "conflict_events", "market_access"]]
y = df["ipc_phase"]

clf = RandomForestClassifier(class_weight="balanced", random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Treat class imbalance with class weights or resampling; famine events are rare but high cost.
- Use time-based splits and avoid leakage from future market prices.
- Combine model outputs with expert judgment; maintain human-in-the-loop escalation paths.
- Calibrate probabilities so thresholds match donor and response budgets.

## Verification

1. Build a 90-day-ahead IPC forecast and backtest against official IPC assessments.
2. Compare the model to a rainfall-only baseline in a drought-affected region.
3. Evaluate how early the system flags an emerging food crisis compared to standard triggers.
        ''',
        "references": [
            "https://www.nature.com/articles/s43016-026-01400-6",
            "https://sfcs.fao.org/docs/devhlpelibraries/default-document-library/hlpe-fsn-ai-note.pdf",
            "https://www.mdpi.com/2077-0472/13/10/2037",
            "https://doi.org/10.1038/s43247-024-01698-9",
        ],
    },
    {
        "name": "ai-for-refugees",
        "title": "AI for Refugees",
        "description": "Use machine learning to forecast displacement, map refugee camps, and allocate humanitarian resources.",
        "devin_body": r'''
## When to use

You need to anticipate refugee or asylum-seeker arrivals, map camp infrastructure, or allocate resources before displacement peaks.

## Usage

- Forecast cross-border flows from violence, governance, economic, and environmental indicators.
- Detect shelters, service points, and population density in satellite/VHR imagery.
- Estimate destination-country distribution with gravity and network models.
- Run counterfactual scenario analysis for conflict or drought shocks.

## Steps

1. Collect origin-country stressors, displacement statistics, and camp imagery.
2. Train panel models with origin, destination, and time fixed effects.
3. Build a camp-mapping or shelter-detection pipeline from VHR imagery.
4. Validate out-of-sample across crisis periods and geographic regions.
5. Run scenario forecasts and share uncertainty with policymakers.
6. Integrate with UNHCR or humanitarian planning workflows.

## Code pattern

```python
import pandas as pd
from sklearn.linear_model import ElasticNet

# Forecast asylum-seeker arrivals from origin-country stressors
X = df[["conflict_intensity", "food_price_index", "governance_index", "distance_km", "border_open"]]
y = df["asylum_seekers"]

model = ElasticNet(alpha=0.1, l1_ratio=0.5)
model.fit(X, y)
```

## Tuning notes

- Use panel-data models with origin, destination, and time fixed effects.
- Handle structural breaks and zero-inflation; many origin-destination pairs have no arrivals.
- Validate out-of-sample across different crisis periods, not just random rows.
- Be transparent about assumptions and uncertainty in forecasts used for policy.

## Verification

1. Build a 12-month displacement forecast for a set of fragile countries and compare to UNHCR planning figures.
2. Detect tents or built structures in a VHR refugee-camp image and compare to manual counts.
3. Evaluate destination-choice model with rank-based metrics on a heldout year.
        ''',
        "references": [
            "https://www.cambridge.org/core/journals/data-and-policy/article/developing-ai-predictive-migration-tools-to-enhance-humanitarian-support-the-case-of-eumigratool/54E3FF814CD44FF426272335AFDD76AE",
            "https://ojs.aaai.org/index.php/AAAI/article/view/26846",
            "https://drc.ngo/en/pages/foresight-displacement-forecasts/",
            "https://www.microsoft.com/en-us/research/publication/mapping-refugee-camps-with-ai-a-benchmark-dataset-and-baseline-models-for-humanitarian-applications/",
            "https://doi.org/10.1287/opre.2021.0534",
        ],
    },
    {
        "name": "ai-for-humanitarian-aid",
        "title": "AI for Humanitarian Aid",
        "description": "Use AI across the crisis management cycle for needs assessment, resource allocation, damage mapping, and early warning.",
        "devin_body": r'''
## When to use

You are coordinating relief in natural or man-made crises and need faster needs assessment, logistics, or damage mapping.

## Usage

- Support early warning, preparedness, response, and recovery with AI.
- Coordinate multi-agent relief planning, routing, and information triage.
- Classify post-disaster building damage from satellite, drone, or social-media imagery.
- Integrate mobile, survey, and geospatial data for beneficiary targeting.

## Steps

1. Identify the crisis phase and assemble relevant data (imagery, needs reports, logistics).
2. Train or configure models for damage classification, routing, or needs triage.
3. Use heuristics or solvers for rapid-onset logistics where exact methods are too slow.
4. Keep human responders in the loop for life-safety and ethical decisions.
5. Map data biases from social media or satellite sources to avoid undercounting.
6. Run simulated responses and iterate with frontline feedback.

## Code pattern

```python
import networkx as nx
import pandas as pd
from sklearn.cluster import KMeans

# Cluster affected zones by need and connect them to supply depots
need_points = df[["lat", "lon", "population", "severity"]]
clusters = KMeans(n_clusters=5, random_state=42, n_init="auto").fit(need_points)

G = nx.Graph()
# Add depot and demand nodes; solve a capacitated vehicle routing problem
```

## Tuning notes

- Balance speed and optimality during rapid-onset events; use heuristics when exact solvers are too slow.
- Keep human responders in the loop for life-safety and ethical decisions.
- Integrate offline mobile AI for connectivity-poor field settings.
- Map data biases from social-media or satellite sources to avoid undercounting rural areas.

## Verification

1. Run a simulated flood/earthquake response and compare AI-optimized routing to a baseline dispatch rule.
2. Classify post-disaster building damage on xBD or similar benchmark and report F1.
3. Test an LLM-based triage agent for correctness, safety, and escalation behavior.
        ''',
        "references": [
            "https://doi.org/10.1016/j.technovation.2025.103415",
            "https://doi.org/10.3390/su18021014",
            "https://www.nature.com/articles/s41467-025-68216-z",
            "https://www.nature.com/articles/s41586-022-05422-504484-9",
        ],
    },
    {
        "name": "ai-for-disability-inclusion",
        "title": "AI for Disability Inclusion",
        "description": "Use accessible, disability-aware AI to improve assistive technologies and reduce algorithmic harm for people with disabilities.",
        "devin_body": r'''
## When to use

You are building AI systems used by, or about, people with disabilities and want to avoid ableism and improve accessibility.

## Usage

- Benchmark models for stereotypes, factual errors, and sentiment on disability-related queries.
- Build assistive AI such as speech-to-text, image captioning, and sign-language recognition.
- Involve people with disabilities in co-design, data collection, and deployment.
- Detect representational, allocative, quality-of-service, and interpersonal harms.

## Steps

1. Identify the disability community and use case and establish CRPD-aligned governance.
2. Collect representative, consent-based data that captures diverse disability experiences.
3. Train or adapt speech, vision, or language models for the assistive task.
4. Audit for bias against mobility, sensory, cognitive, and psychosocial disability groups.
5. Build human override and explainability into high-stakes decisions.
6. Pilot with disabled users and iterate on model and UI decisions.

## Code pattern

```python
from transformers import pipeline

# Generate image captions for screen-reader users
captioner = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
caption = captioner("https://example.org/accessible-sign.jpg")
```

## Tuning notes

- Use representative, consent-based data that captures diverse disability experiences.
- Audit for bias against specific disability types (mobility, sensory, cognitive, psychosocial).
- Provide human override and explainability, especially for high-stakes decisions.
- Follow CRPD principles: autonomy, inclusion, participation, and non-discrimination.

## Verification

1. Evaluate an LLM on a disability-bias benchmark and compare neutral vs. disability-aware prompts.
2. Build a sign-language or speech-recognition demo and measure word/sign error rates with disabled users.
3. Conduct a co-design session and document how feedback changed model or UI decisions.
        ''',
        "references": [
            "https://ojs.aaai.org/index.php/AIES/article/download/36745/38883/40820",
            "https://aclanthology.org/2025.emnlp-main.1653/",
            "https://link.springer.com/article/10.1007/s00146-025-02642-x",
            "https://cdt.org/wp-content/uploads/2025/03/2025-03-11-CDT-Building-A-Disability-Inclusive-AI-Ecosystem-report-final.pdf",
        ],
    },
    {
        "name": "ai-for-aging",
        "title": "AI for Aging",
        "description": "Use machine learning to support older adults with health monitoring, fall prevention, cognitive and social support, and age-friendly design.",
        "devin_body": r'''
## When to use

You are supporting older adults to age safely at home, manage chronic conditions, or maintain cognitive and social well-being.

## Usage

- Sense activity, gait, sleep, and falls with passive environmental and wearable sensors.
- Support memory, mood, and loneliness with conversational agents and personalized content.
- Predict hospitalization, frailty, and functional decline from EHR and sensor streams.
- Design legible, voice-enabled interfaces and digital literacy support.

## Steps

1. Define the aging outcome (fall, hospitalization, isolation) and data sources (sensors, EHR).
2. Collect longitudinal data and use time-aware validation.
3. Train predictive or conversational models and handle class imbalance.
4. Prioritize on-device or edge processing for privacy.
5. Involve older adults and caregivers in interface and alert design.
6. Pilot in aging-in-place or care settings and measure adherence and outcomes.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Fall-risk prediction from wearable and home-sensor features
X = df[["gait_speed", "sleep_quality", "medication_count", "balance_score", "prior_falls"]]
y = df["fall_event"]

clf = GradientBoostingClassifier(random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Use time-aware validation because aging trajectories change over time.
- Handle class imbalance; falls and hospitalizations are rare relative to sensor windows.
- Prioritize privacy by processing data on-device or at the edge when possible.
- Involve older adults and caregivers in interface and alert design.

## Verification

1. Train a fall-risk model and compare its recall to a clinical frailty index.
2. Build a medication or activity reminder chatbot and measure adherence in a pilot.
3. Run an age-inclusive usability test and iterate on accessibility findings.
        ''',
        "references": [
            "https://link.springer.com/article/10.1186/s12877-026-07798-9",
            "https://ai.jmir.org/2026/1/e84695",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC8979827/",
            "https://www.mdpi.com/2227-9032/13/5/446",
        ],
    },
    {
        "name": "ai-for-dementia-care",
        "title": "AI for Dementia Care",
        "description": "Use machine learning to screen for cognitive decline, stratify dementia risk, and support caregivers.",
        "devin_body": r'''
## When to use

You need to detect cognitive decline early, triage memory-clinic referrals, or support people with dementia and their caregivers.

## Usage

- Screen for cognitive impairment from voice, language, and questionnaire responses.
- Build EHR-based dementia risk models with low-burden inputs.
- Combine neuropsychology, imaging, and biomarkers for differential diagnosis.
- Tier models from basic demographics to full neuropsych batteries.

## Steps

1. Collect voice, EHR, imaging, and neuropsych data with careful timestamping.
2. Define the screening or risk target and avoid leakage from future visits.
3. Train minimal-input screeners and more comprehensive diagnostic models.
4. Validate across health systems, countries, and cognitive assessment norms.
5. Balance sensitivity and specificity and provide explanations to clinicians.
6. Integrate into memory clinic triage and monitor referral outcomes.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Dementia risk stratification from structured EHR and cognitive scores
X = df[["age", "mmse", "cdr", "education_years", "functional_status", "comorbidity_count"]]
y = df["dementia"]

clf = RandomForestClassifier(class_weight="balanced", random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Avoid temporal leakage from future visits, tests, or diagnoses.
- External-validate across health systems, countries, and cognitive assessment norms.
- Balance sensitivity and specificity to avoid unnecessary anxiety and missed cases.
- Provide explanations to clinicians and caregivers; avoid opaque risk scores.

## Verification

1. Build a minimal-input dementia screener and compare AUC to a full neuropsych battery.
2. Analyze a voice-recording dataset for cognitive-impairment detection and report AUC.
3. Validate the model on an independent EHR cohort and check subgroup calibration.
        ''',
        "references": [
            "https://link.springer.com/article/10.1186/s13195-026-02006-7",
            "https://www.nature.com/articles/s41467-026-76071-9",
            "https://www.nature.com/articles/s44400-025-00040-0",
            "https://www.nature.com/articles/s41591-024-03118-z",
        ],
    },
    {
        "name": "ai-for-palliative-care",
        "title": "AI for Palliative Care",
        "description": "Use machine learning for prognostication, symptom management, hospice suitability, and advance care planning in end-of-life care.",
        "devin_body": r'''
## When to use

You need to identify patients who may benefit from palliative or hospice care, forecast prognosis, or personalize symptom management.

## Usage

- Estimate 6- or 12-month mortality from EHR for referral triggers.
- Classify optimal care models (home, inpatient, shared) from health assessments.
- Extract pain, dyspnea, fatigue, and psychosocial distress from clinical notes.
- Alert clinicians to goals-of-care conversations and documentation needs.

## Steps

1. Define the palliative outcome (mortality, symptom, care setting) and assemble EHR.
2. Use time-stamped EHR splits and avoid labels that depend on the referral decision itself.
3. Train prognostic or NLP symptom models and calibrate probabilities.
4. Validate against palliative screening rules and chart review.
5. Integrate as decision support, keeping clinicians and patients at the center.
6. Monitor for bias in access to hospice and palliative services across groups.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Palliative-care referral trigger from structured EHR
X = df[["age", "comorbidity_count", "performance_status", "hospitalizations_90d", "symptom_burden"]]
y = df["palliative_referral_needed"]

clf = GradientBoostingClassifier(random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Keep clinicians and patients at the center; models should support, not replace, compassionate judgment.
- Use time-stamped EHR splits and avoid labels that depend on the referral decision itself.
- Calibrate predicted probabilities so clinicians can trust risk thresholds.
- Monitor for bias in access to hospice and palliative services across groups.

## Verification

1. Train a 6-month mortality model and compare to a palliative-screening rule.
2. Build an NLP symptom extractor and evaluate against manual chart review.
3. Pilot a referral decision-support tool and measure time-to-palliative consult.
        ''',
        "references": [
            "https://pubmed.ncbi.nlm.nih.gov/40849027/",
            "https://link.springer.com/article/10.1186/s12911-025-03289-w",
            "https://www.nature.com/articles/s41746-026-02429-4",
            "https://sage.cnpereading.com/doi/10.1177/10499091251358379",
            "https://pubmed.ncbi.nlm.nih.gov/36842541/",
        ],
    },
    {
        "name": "ai-for-maternal-health",
        "title": "AI for Maternal Health",
        "description": "Use machine learning to stratify maternal risk, predict preterm birth, support obstetric decisions, and forecast neonatal outcomes.",
        "devin_body": r'''
## When to use

You are building tools to predict adverse pregnancy outcomes, triage antenatal care, or support low-resource maternal-health platforms.

## Usage

- Integrate clinical history, vitals, labs, and social determinants of health (SDoH).
- Predict preterm birth from longitudinal EHR, cervical measurements, and biomarkers.
- Detect fetal growth, anomalies, and placental issues from ultrasound.
- Provide triage and decision support via WhatsApp/telehealth platforms.

## Steps

1. Assemble antenatal EHR, SDoH, imaging, and telehealth data.
2. Define adverse outcomes and use chronological splits avoiding post-delivery leakage.
3. Train risk models that include SDoH and access variables for equity.
4. Validate on Medicaid or LMIC cohorts, not just privileged populations.
5. Build a decision-support interface for midwives, nurses, and patients.
6. Monitor outcomes and disparities across racial, ethnic, and geographic groups.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Maternal adverse-outcome risk from clinical and SDoH features
X = df[["age", "parity", "systolic_bp", "bmi", "diabetes", "provider_density", "travel_distance"]]
y = df["adverse_pregnancy_outcome"]

clf = GradientBoostingClassifier(random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Use chronological splits and avoid leakage from post-delivery diagnoses.
- Include SDoH and access variables; they can improve equity as well as accuracy.
- Validate on Medicaid or LMIC cohorts, not just privileged populations.
- Calibrate and explain risk scores for midwives, nurses, and patients.

## Verification

1. Train an adverse-pregnancy model and measure the lead time before clinical symptoms appear.
2. Compare clinical-only vs. clinical-plus-SDoH model performance across racial/ethnic subgroups.
3. Test a symptom-checker integration on a government WhatsApp maternal-health platform.
        ''',
        "references": [
            "https://doi.org/10.1038/s44482-025-00003-5",
            "https://link.springer.com/article/10.1186/s12884-026-09784-w",
            "https://link.springer.com/article/10.1186/s12962-026-00730-3",
            "https://www.nature.com/articles/s44360-026-00125-x",
        ],
    },
    {
        "name": "ai-for-child-health",
        "title": "AI for Child Health",
        "description": "Use machine learning to support pediatric diagnostics, developmental surveillance, and risk stratification.",
        "devin_body": r'''
## When to use

You are building AI tools for pediatric screening, diagnosis, monitoring, or treatment planning across neonatal, childhood, and adolescent populations.

## Usage

- Track age-adjusted growth, developmental milestones, and anomaly detection.
- Support diagnosis of pneumonia, sepsis, congenital heart disease, and retinopathy of prematurity.
- Integrate EHR notes, imaging, labs, and parent-reported outcomes into pediatric models.
- Apply pediatric AI readiness (PAIR) governance, validation, and child-centric design.

## Steps

1. Collect pediatric data and normalize by age, sex, and developmental stage.
2. Define diagnosis or screening targets with child-appropriate reference ranges.
3. Train models with class imbalance and data-scarcity handling (transfer, federated learning).
4. Validate across pediatric subgroups and institutions.
5. Complete a pediatric AI readiness checklist and address low-resource adaptation.
6. Integrate into pediatric workflows with guardian consent and age-appropriate interfaces.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Pediatric sepsis early-warning from vital signs and labs
X = df[["age_months", "temperature", "heart_rate", "wbc", "lactate", "respiratory_rate"]]
y = df["sepsis"]

clf = RandomForestClassifier(class_weight="balanced", random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Normalize features by age, sex, and developmental stage; pediatric physiology changes rapidly.
- Use child-appropriate reference ranges and avoid adult-biased training data.
- Address data scarcity with federated learning or transfer learning from adult cohorts.
- Validate across pediatric subgroups and institutions; children are under-represented in many datasets.

## Verification

1. Build a pediatric sepsis early-warning model and evaluate time-to-detection vs. clinician alerts.
2. Train an image classifier on pediatric pneumonia X-rays and report sensitivity and specificity.
3. Complete the PAIR readiness checklist for a pediatric AI deployment.
        ''',
        "references": [
            "https://www.mdpi.com/2077-0383/14/3/807",
            "https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1800047/full",
            "https://medinform.jmir.org/2026/1/e80163",
            "https://tp.amegroups.org/article/view/153038/html",
            "https://link.springer.com/article/10.1186/s12887-026-06711-y",
        ],
    },
    {
        "name": "ai-for-rural-health",
        "title": "AI for Rural Health",
        "description": "Deliver mobile AI-assisted diabetic retinopathy and cardiac screening to remote communities with limited specialist access.",
        "devin_body": r'''
## When to use

You are deploying AI in rural, remote, or low-resource health settings where specialists, connectivity, and infrastructure are limited.

## Usage

- Provide real-time AI decision support during virtual consultations.
- Run point-of-care diagnostics on mobile or edge devices for imaging and triage.
- Reduce digital literacy, bandwidth, language, and trust barriers.
- Optimize staffing, transport, and supply distribution across large geographies.

## Steps

1. Assess infrastructure, connectivity, and device constraints in the target rural area.
2. Curate representative rural data and avoid urban-academic bias.
3. Train lightweight, offline-capable models for imaging or triage.
4. Test latency, battery, and usability on the target hardware.
5. Involve rural clinicians and community health workers in deployment.
6. Monitor whether the tool narrows or widens rural-urban outcome disparities.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Rural triage/referral support from clinic data and travel context
X = df[["symptom_severity", "vitals_risk_score", "telemedicine_available", "travel_distance_km", "chronic_conditions"]]
y = df["referral_needed"]

clf = GradientBoostingClassifier(random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Test on low-end devices and intermittent connectivity; prefer on-device or offline models.
- Involve rural clinicians and community health workers in design and validation.
- Use federated or representative rural data to avoid urban-academic bias.
- Monitor equity across race, ethnicity, language, and insurance status.

## Verification

1. Deploy a diagnostic aid in a rural clinic and compare concordance with specialist referrals.
2. Measure model latency and battery use on the target hardware.
3. Evaluate whether the tool narrows or widens rural-urban outcome disparities.
        ''',
        "references": [
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12892150/",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12262758/",
            "https://www.mdpi.com/2227-9032/13/3/324",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12863373/",
        ],
    },
    {
        "name": "ai-for-mental-health-services",
        "title": "AI for Mental Health Services",
        "description": "Use LLMs and multimodal AI to screen, triage, monitor, and support mental-health care at scale.",
        "devin_body": r'''
## When to use

You are building tools to screen, triage, monitor, or support mental-health care at scale, especially when clinicians are scarce.

## Usage

- Combine text, speech, wearables, and neuroimaging for early detection and monitoring.
- Deploy CBT-based conversational agents for depression, anxiety, and stress.
- Triage psychosocial risks such as suicidality, intimate partner violence, and substance misuse.
- Support clinical interviews with multi-agent LLM frameworks.

## Steps

1. Collect representative, demographically diverse, clinically validated mental-health data.
2. Fine-tune or prompt a triage, screening, or CBT model with safety guardrails.
3. Build human escalation and crisis pathways; never use AI as the sole diagnostic tool.
4. Validate against clinician-rated vignettes and standard symptom scales.
5. Monitor for hallucinations, biased responses, and false reassurance.
6. Protect privacy and obtain informed consent before deployment.

## Code pattern

```python
from transformers import pipeline

# Triage mental-health risk from patient text
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
text = "I feel hopeless and cannot sleep."
result = classifier(text)
```

## Tuning notes

- Never use AI as a sole diagnostic or crisis tool; always provide human escalation.
- Validate on clinically representative, demographically diverse data.
- Monitor for hallucinations, biased responses, and false reassurance in generative chatbots.
- Protect privacy and obtain informed consent for sensitive mental-health data.

## Verification

1. Fine-tune a mental-health triage classifier on a clinical dataset and compare to a general sentiment model.
2. Run a CBT chatbot pilot and measure symptom change and user safety.
3. Evaluate a psychosocial-risk LLM assessment against clinician-rated vignettes.
        ''',
        "references": [
            "https://link.springer.com/article/10.1007/s10462-026-11649-9",
            "https://www.nature.com/articles/s41746-026-02886-x",
            "https://ai.nejm.org/doi/full/10.1056/AIoa2400802",
            "https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0001352",
        ],
    },
]