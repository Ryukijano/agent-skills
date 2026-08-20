SKILLS = [
    {
        "name": "ai-for-radiology",
        "title": "AI for Radiology",
        "description": "Deep learning for X-ray, CT, MRI, and mammography interpretation, including lesion detection, segmentation, report generation, and radiology foundation models.",
        "devin_body": r'''
## When to use

You need to detect, classify, or segment abnormalities on radiological images; build foundation models for radiology; or integrate an AI triage tool into a PACS/DICOM workflow.

## Key concepts

- **Modality-aware preprocessing**: HU scaling for CT, window/level for X-ray, bias field correction and intensity normalization for MRI.
- **Lesion segmentation**: U-Net, nnU-Net, SwinUNETR, and VISTA-3D for 2D/3D anatomy.
- **Radiology foundation models**: self-supervised pretraining on large radiology corpora (e.g., RADImageNet, CheXzero, MedImageInsight).
- **Workflow integration**: DICOM/FHIR I/O, AI result routing, worklist prioritization, and structured reporting.
- **Safety and equity**: external validation, underdiagnosis bias in underserved populations, and confidence calibration.

## Code pattern

```python
import monai
from monai.transforms import LoadImage, EnsureChannelFirst, ScaleIntensity
from monai.networks.nets import UNet

# Load and preprocess a 3D CT volume
loader = LoadImage(image_only=True)
img = loader("ct_scan.nii.gz")
img = ScaleIntensity()(EnsureChannelFirst()(img))

model = UNet(
    spatial_dims=3,
    in_channels=1,
    out_channels=2,
    channels=(16, 32, 64, 128),
    strides=(2, 2, 2)
)
```

## Tuning notes

- Use clinically relevant CT window/level and HU ranges; avoid training on unwindowed DICOM pixel values.
- Account for slice thickness, in-plane resolution, and scanner variability with resampling to a common spacing.
- Validate on external cohorts and report AUC/Dice with confidence intervals.
- Monitor for underdiagnosis bias across sex, race, age, and socioeconomic strata.

## Verification

1. Train a lesion segmentation model and compare Dice to an inter-reader benchmark.
2. Run external validation across hospitals and compare sensitivity/specificity.
3. Implement a DICOM inference pipeline and measure report turnaround time.
''',
        "references": [
            "https://pubs.rsna.org/doi/10.1148/radiol.240597",
            "https://link.springer.com/article/10.1007/s10334-024-01173-8",
            "https://www.nature.com/articles/s41467-024-51202-2",
            "https://www.mdpi.com/2075-4418/15/3/282",
            "https://link.springer.com/article/10.1007/s00330-022-08784-6",
        ],
    },
    {
        "name": "ai-for-pathology",
        "title": "AI for Pathology",
        "description": "Computational pathology, whole-slide image analysis, cancer subtyping, biomarker discovery, and vision-language models for histopathology.",
        "devin_body": r'''
## When to use

You are analyzing whole-slide images (WSIs), grading tumors, predicting molecular biomarkers, or building AI-assisted pathology workflows.

## Key concepts

- **WSI tiling and patch sampling**: gigapixel images are processed as small patches because full slides do not fit in GPU memory.
- **Multiple instance learning (MIL)**: train on slide-level labels when pixel annotations are scarce.
- **Foundation and vision-language models**: pathology FMs (UNI, CONCH, PathChat) enable few-shot and multimodal analysis.
- **Cancer subtyping and biomarkers**: predict tumor origin, grade, prognosis, and therapy response from H&E slides.
- **Domain shift and stain normalization**: scanners, staining, and labs introduce significant batch effects.

## Code pattern

```python
import openslide
import torch
from torch.utils.data import DataLoader

# Open a WSI and extract a patch
slide = openslide.OpenSlide("tissue.svs")
patch = slide.read_region((10000, 10000), 0, (256, 256)).convert("RGB")

# Typical pipeline: tiles -> feature encoder -> aggregator (MIL/Transformer)
tensor = torch.from_numpy(np.array(patch)).permute(2, 0, 1).unsqueeze(0).float() / 255.0
```

## Tuning notes

- Normalize for staining and scanner differences (Macenko, Vahadane, or learned stain transfer).
- Use weak or noisy labels and bag-level losses for MIL.
- Evaluate with pathologist concordance and external test sets.
- Balance across tissue types and cancer grades.

## Verification

1. Train a MIL classifier on WSI patches and compare to pathologist grading.
2. Apply stain normalization and measure domain-shift robustness.
3. Extract attention heatmaps and validate against pathologist annotations.
''',
        "references": [
            "https://doi.org/10.1016/j.csbj.2024.12.033",
            "https://arxiv.org/abs/2401.06148",
            "https://arxiv.org/abs/2408.14496v1",
            "https://www.sciencedirect.com/science/article/pii/S0895611124000144",
            "https://link.springer.com/article/10.1007/s00424-024-03002-2",
        ],
    },
    {
        "name": "ai-for-dermatology",
        "title": "AI for Dermatology",
        "description": "Skin lesion classification, dermoscopy analysis, melanoma detection, teledermatology, and fairness across skin tones with deep learning.",
        "devin_body": r'''
## When to use

You are classifying skin lesions from dermoscopy or clinical photos, triaging suspicious lesions, or building teledermatology and mobile screening tools.

## Key concepts

- **Dermoscopy and clinical imaging**: polarized light, magnification, and standardized fields of view.
- **Convolutional and efficient architectures**: EfficientNet, ResNet, and Vision Transformers for lesion classification.
- **Melanoma vs. benign nevi/keratinocyte carcinoma**: high-stakes binary and multi-class tasks.
- **Teledermatology**: smartphone capture, asynchronous image review, and regulatory clearance.
- **Equity and skin tone**: model performance can degrade on darker skin if training data are unbalanced.

## Code pattern

```python
from PIL import Image
from torchvision import transforms, models
import torch

preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

img = preprocess(Image.open("lesion.jpg")).unsqueeze(0)
model = models.efficientnet_b0(weights="IMAGENET1K_V1")
model.classifier[1] = torch.nn.Linear(model.classifier[1].in_features, 2)
```

## Tuning notes

- Fine-tune from ImageNet or use publicly available dermoscopy pretrained weights.
- Address class imbalance with weighted sampling or focal loss.
- Validate on images from different devices and Fitzpatrick skin types.
- Interpret predictions with Grad-CAM or segmentation masks.

## Verification

1. Fine-tune a lesion classifier and compare AUC to dermatologist diagnoses.
2. Evaluate performance across Fitzpatrick skin types.
3. Deploy as an API and test with real teledermatology cases.
''',
        "references": [
            "https://doi.org/10.1038/nature21056",
            "https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2023.1305954/full",
            "https://www.mdpi.com/2072-6694/15/4/1183",
            "https://www.sciencedirect.com/science/article/pii/S0022202X23029640",
            "https://engineering.stanford.edu/news/how-researchers-trained-algorithm-diagnose-skin-cancer",
        ],
    },
    {
        "name": "ai-for-ophthalmology",
        "title": "AI for Ophthalmology",
        "description": "Diabetic retinopathy screening, OCT analysis, glaucoma detection, and AI for retinal disease diagnosis from fundus photography.",
        "devin_body": r'''
## When to use

You are screening for diabetic retinopathy, analyzing OCT volumes, detecting glaucoma, or building AI for retinal disease diagnosis and triage.

## Key concepts

- **Fundus photography grading**: diabetic retinopathy severity, diabetic macular edema, and referable thresholds.
- **OCT segmentation**: intraretinal fluid, subretinal fluid, retinal nerve fiber layer, and pigment epithelium detachment.
- **Glaucoma detection**: RNFL thickness maps, optic nerve head analysis, and visual field prediction.
- **Teleophthalmology and autonomous screening**: point-of-care deployment in primary care.
- **Regulatory pathways**: FDA/CE-marked AI systems for diabetic eye disease.

## Code pattern

```python
import cv2
import torch
from torchvision import transforms

# Preprocess a fundus image
img = cv2.imread("fundus.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

preprocess = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((512, 512)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

tensor = preprocess(img).unsqueeze(0)
```

## Tuning notes

- Ensure consistent image quality, field-of-view, and pupil dilation.
- Use data augmentation (rotation, brightness) appropriate to fundus images.
- Calibrate operating point for high sensitivity in screening workflows.
- Validate on racially and ethnically diverse cohorts.

## Verification

1. Train a diabetic retinopathy classifier and compute sensitivity/specificity at the referral threshold.
2. Segment OCT fluid compartments and compare with manual grading.
3. Validate in a prospective screening workflow.
''',
        "references": [
            "https://doi.org/10.1001/jama.2016.17216",
            "https://jamanetwork.com/journals/jama/fullarticle/2588763",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC8063221/",
            "https://www.nature.com/articles/s41433-023-02720-8",
        ],
    },
    {
        "name": "ai-for-cardiology",
        "title": "AI for Cardiology",
        "description": "ECG interpretation, arrhythmia detection, heart failure screening, echocardiography analysis, and cardiovascular risk stratification with deep learning.",
        "devin_body": r'''
## When to use

You are interpreting ECGs, detecting arrhythmias, predicting heart failure or ejection fraction, or integrating wearables into cardiovascular care.

## Key concepts

- **ECG signal processing**: filtering, baseline wander removal, R-peak detection, and resampling to a standard rate.
- **Arrhythmia detection**: atrial fibrillation, flutter, premature ventricular contractions, and blocks.
- **Convolutional and 1D networks for 12-lead ECG classification**.
- **AI-enabled ECG**: detect low ejection fraction or prior AF even during sinus rhythm.
- **Holter and wearable monitoring**: long-term, low-fidelity single-lead data.

## Code pattern

```python
import wfdb
import torch
from torch import nn

# Load a 12-lead ECG record
record = wfdb.rdrecord("ptbxl/00001", pn_dir="ptbxl")
# shape: (time, 12)

ecg = torch.tensor(record.p_signal.T, dtype=torch.float32).unsqueeze(0)
model = nn.Sequential(
    nn.Conv1d(12, 32, kernel_size=7),
    nn.ReLU(),
    nn.AdaptiveAvgPool1d(1),
    nn.Flatten(),
    nn.Linear(32, 2)
)
```

## Tuning notes

- Standardize sampling rate (e.g., 500 Hz) and lead order across datasets.
- Use patient-level or time-based splits to avoid leakage.
- Align with AAMI/ESC annotation standards.
- Calibrate scores and integrate with clinical workflows (EMR, ECG carts).

## Verification

1. Train an atrial fibrillation classifier and report F1 on an external test set.
2. Compare AI-ECG ejection fraction screening to echocardiography.
3. Validate real-time inference on Holter data.
''',
        "references": [
            "https://www.nature.com/articles/s41591-018-0240-2",
            "https://doi.org/10.1016/s0140-6736(19)31721-0",
            "https://openheart.bmj.com/content/12/1/e003185",
            "https://www.mdpi.com/1424-8220/25/13/4109",
        ],
    },
    {
        "name": "ai-for-pulmonology",
        "title": "AI for Pulmonology",
        "description": "Chest X-ray and CT interpretation, COPD and asthma assessment, respiratory sound analysis, and pulmonary disease risk prediction.",
        "devin_body": r'''
## When to use

You are interpreting chest X-rays and CTs, diagnosing COPD or asthma, analyzing respiratory sounds, or predicting respiratory disease outcomes.

## Key concepts

- **Chest X-ray abnormality detection**: nodules, consolidation, pleural effusion, and pneumothorax.
- **CT-based pulmonary assessment**: emphysema quantification, airway wall thickness, and lung cancer screening.
- **COPD severity and GOLD staging** with deep learning.
- **Respiratory sound analysis**: cough, breath sounds, and spirometry curves.
- **Longitudinal risk prediction**: lung disease mortality and exacerbation risk.

## Code pattern

```python
import pydicom
import numpy as np
from PIL import Image

# Convert a chest X-ray DICOM to a normalized array
ds = pydicom.dcmread("chest_xray.dcm")
img = ds.pixel_array.astype(np.float32)

if "RescaleSlope" in ds:
    img = img * ds.RescaleSlope + ds.RescaleIntercept
img = (img - img.min()) / (img.max() - img.min())
img = np.stack([img, img, img], axis=0)  # pseudo-RGB for pretrained encoders
```

## Tuning notes

- Apply DICOM windowing and handle rescale slope/intercept.
- Use large public datasets (CheXpert, MIMIC-CXR, PadChest) for pretraining.
- Address label noise, class imbalance, and hidden confounders (pneumothorax drains).
- Evaluate for subgroup bias across age, sex, race, and disease severity.

## Verification

1. Train a chest X-ray pathology classifier and compare with radiologist reads.
2. Predict COPD from CT or chest X-ray and validate against spirometry.
3. Test on an external dataset and measure subgroup performance.
''',
        "references": [
            "https://www.mdpi.com/2227-7080/14/3/147",
            "https://bmcpulmmed.biomedcentral.com/articles/10.1186/s12890-024-02945-7",
            "https://www.nature.com/articles/s41467-023-37758-5",
            "https://www.nature.com/articles/s41591-021-01595-0",
            "https://www.nature.com/articles/s41598-024-76608-2",
        ],
    },
    {
        "name": "ai-for-gastroenterology",
        "title": "AI for Gastroenterology",
        "description": "AI-assisted endoscopy, real-time polyp detection and characterization, colonoscopy quality, and colorectal cancer screening.",
        "devin_body": r'''
## When to use

You are building AI to assist endoscopy, detect polyps, classify diminutive lesions, or improve colorectal cancer screening quality.

## Key concepts

- **Computer-aided detection (CADe)**: real-time polyp detection during colonoscopy.
- **Computer-aided characterization (CADx)**: optical diagnosis of adenoma vs. hyperplastic polyp.
- **Adenoma detection rate (ADR)**, polyp detection rate, and sessile serrated lesion detection.
- **Endoscopy video analysis**: object detection, tracking, and temporal smoothing.
- **Resect-and-discard and preservation-and-discard strategies** for diminutive polyps.

## Code pattern

```python
import cv2
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn

# Load endoscopy video and detect polyps frame-by-frame
cap = cv2.VideoCapture("colonoscopy.avi")
model = fasterrcnn_resnet50_fpn(pretrained=False, num_classes=2)
model.eval()

ret, frame = cap.read()
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
tensor = torch.from_numpy(frame_rgb).permute(2, 0, 1).unsqueeze(0).float() / 255.0

with torch.no_grad():
    preds = model(tensor)
```

## Tuning notes

- Train on diverse endoscopy systems, bowel preparations, and lighting conditions.
- Optimize for real-time latency (< 100 ms per frame) on endoscopy processors.
- Combine detection with histology classification for CADx.
- Validate with ADR and polyp miss rate metrics in clinical studies.

## Verification

1. Build a polyp detector and evaluate per-image sensitivity/specificity.
2. Compare ADR with and without AI in a retrospective or pilot study.
3. Validate optical diagnosis accuracy against histopathology.
''',
        "references": [
            "https://www.nature.com/articles/s41551-018-0301-3",
            "https://gut.bmj.com/content/68/10/1813",
            "https://gut.bmj.com/content/69/5/799",
            "https://www.acpjournals.org/doi/10.7326/ANNALS-24-00981",
        ],
    },
    {
        "name": "ai-for-neurology",
        "title": "AI for Neurology",
        "description": "Neuroimaging and EEG analysis for stroke, brain tumors, epilepsy, and neurodegeneration, including lesion segmentation and outcome prediction.",
        "devin_body": r'''
## When to use

You are analyzing neuroimaging, EEG, or clinical data for stroke, brain tumors, epilepsy, neurodegeneration, or brain-computer interfaces.

## Key concepts

- **Acute ischemic stroke imaging**: non-contrast CT, CT angiography, perfusion, and DWI MRI.
- **Lesion segmentation**: DeepISLES, nnU-Net, and U-Net for ischemic core and penumbra.
- **Outcome prediction**: mRS and NIHSS prediction from imaging plus clinical data.
- **EEG-based neurological monitoring**: seizure, stroke, and sleep stage analysis.
- **Multimodal fusion**: MRI + CT + EEG + clinical variables.

## Code pattern

```python
import nibabel as nib
import torch
from monai.networks.nets import UNet

# Load a DWI volume and segment the stroke lesion
img = nib.load("dwi.nii.gz").get_fdata()
img = torch.tensor(img).unsqueeze(0).unsqueeze(0).float()

model = UNet(
    spatial_dims=3,
    in_channels=1,
    out_channels=2,
    channels=(16, 32, 64, 128),
    strides=(2, 2, 2)
)
```

## Tuning notes

- Register images to a common template for lesion-location-based analyses.
- Balance small lesion sizes with weighted loss and data augmentation.
- Combine imaging features with NIHSS and time-to-treatment.
- Address cross-scanner and cross-hospital generalization.

## Verification

1. Segment ischemic stroke lesions and report Dice vs. expert.
2. Predict 90-day modified Rankin Scale from imaging and clinical variables.
3. Detect EEG abnormalities and compare to neurologist interpretation.
''',
        "references": [
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12083563/",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11229702/",
            "https://www.nature.com/articles/s41467-025-62373-x",
            "https://link.springer.com/article/10.1007/s44163-026-00926-9",
        ],
    },
    {
        "name": "ai-for-oncology",
        "title": "AI for Oncology",
        "description": "AI for cancer detection, subtyping, treatment response, prognosis, radiomics, pathology, and clinical trial matching.",
        "devin_body": r'''
## When to use

You are building AI for cancer detection, tumor subtyping, treatment response prediction, prognosis, or matching patients to clinical trials.

## Key concepts

- **Radiomics and deep learning for tumor imaging**: high-throughput feature extraction and CNN-based biomarkers.
- **Digital and computational pathology**: molecular biomarker prediction from H&E slides.
- **Treatment response and survival prediction**: from imaging, genomics, and EHR data.
- **Multimodal data fusion**: imaging, genomics, pathology, and clinical variables.
- **Clinical trial matching and real-world evidence**: NLP and eligibility criteria.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Predict treatment response from radiomic features
X = df[['texture_contrast', 'shape_volume', 'wavelet_HLL_glcm_entropy']]
y = df['response']

model = RandomForestClassifier(n_estimators=200, class_weight='balanced')
model.fit(X, y)
```

## Tuning notes

- Use standardized radiomic feature extraction (e.g., pyradiomics with IBSI filters).
- Validate with external and prospective cohorts, not just public leaderboards.
- Integrate pathology, genomics, and clinical data when available.
- Report uncertainty and ensure models support clinical decisions.

## Verification

1. Train a tumor classification or response model and compare with standard care.
2. Extract radiomic features and assess repeatability across scanners.
3. Validate a multimodal survival prediction on an external cohort.
''',
        "references": [
            "https://link.springer.com/article/10.1186/s12943-025-02450-3",
            "https://www.cancerbiomed.org/content/22/1/6",
            "https://bmjoncology.bmj.com/content/3/1/e000134",
            "https://link.springer.com/article/10.1186/s12967-025-07308-2",
            "https://www.nature.com/articles/s41416-023-02317-8",
        ],
    },
    {
        "name": "ai-for-medical-imaging",
        "title": "AI for Medical Imaging",
        "description": "General medical image preprocessing, segmentation, classification, and deployment with DICOM, MONAI, nnU-Net, and clinical AI pipelines.",
        "devin_body": r'''
## When to use

You need a general framework for medical image preprocessing, segmentation, classification, or deployment into clinical DICOM/NIfTI workflows.

## Key concepts

- **DICOM and NIfTI I/O**: loading, metadata handling, windowing, and orientation.
- **MONAI**: PyTorch-based framework with medical-specific transforms and networks.
- **nnU-Net**: self-configuring segmentation framework that automatically sets preprocessing and architecture.
- **3D architectures**: UNETR, SwinUNETR, VISTA-3D, and generative models like MAISI.
- **Clinical deployment**: containerized MONAI Application Packages (MAP), FHIR, and DICOM routers.

## Code pattern

```python
from monai.data import Dataset, DataLoader
from monai.transforms import Compose, LoadImaged, EnsureChannelFirstd, RandRotated
from monai.networks.nets import UNETR

# Build a MONAI 3D segmentation pipeline
data = [{"image": "ct.nii.gz", "label": "mask.nii.gz"}]
transform = Compose([
    LoadImaged(keys=["image", "label"]),
    EnsureChannelFirstd(keys=["image", "label"]),
    RandRotated(keys=["image", "label"], range_x=0.3),
])

dataloader = DataLoader(Dataset(data, transform=transform), batch_size=1)
model = UNETR(
    in_channels=1,
    out_channels=2,
    img_size=(96, 96, 96),
    feature_size=16,
    hidden_size=768,
    mlp_dim=3072,
    num_heads=12
)
```

## Tuning notes

- Match patch sizes and batch sizes to available GPU memory.
- Use MONAI's Auto3DSeg or nnU-Net to avoid manual pipeline tuning.
- Ensure reproducibility with containerized MAP packaging.
- Validate with clinical metrics: Dice, Hausdorff distance, and surface distance.

## Verification

1. Train a 3D segmentation model on a public medical imaging benchmark.
2. Use nnU-Net with no manual hyperparameter tuning and compare results.
3. Package a model as a MONAI Deploy MAP and run DICOM inference.
''',
        "references": [
            "https://project-monai.github.io/",
            "https://docs.monai.io/en/stable/",
            "https://github.com/Project-MONAI/MONAI/",
            "https://www.nature.com/articles/s41592-020-01008-z",
            "https://github.com/mic-dkfz/nnunet/",
        ],
    },
    {
        "name": "ai-for-clinical-nlp",
        "title": "AI for Clinical NLP",
        "description": "Natural language processing for electronic health records, clinical entity extraction, term normalization, de-identification, and question answering.",
        "devin_body": r'''
## When to use

You are extracting information from clinical notes, building EHR question-answering, normalizing medical terms, or de-identifying protected health information.

## Key concepts

- **Clinical named entity recognition (NER)**: symptoms, medications, diagnoses, procedures, and adverse events.
- **Domain-specific language models**: ClinicalBERT, BioBERT, GatorTron, and clinical LLMs.
- **Entity normalization**: mapping mentions to UMLS, SNOMED-CT, RxNorm, and ICD.
- **De-identification**: removing or surrogates of protected health information (PHI).
- **Clinical corpora and tasks**: MIMIC-III/IV, n2c2, MACCROBAT, and MedNLI.

## Code pattern

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

# Load a clinical NER model
tokenizer = AutoTokenizer.from_pretrained("samrawal/bert-base-uncased_clinical-ner")
model = AutoModelForTokenClassification.from_pretrained("samrawal/bert-base-uncased_clinical-ner")

text = "Patient was prescribed metformin 500 mg for type 2 diabetes."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
```

## Tuning notes

- Use domain-specific tokenizers and vocabularies for clinical abbreviations.
- Handle long documents with sliding windows or hierarchical encoders.
- De-identify notes before model training and external sharing.
- Evaluate with entity-level F1 and normalization accuracy.

## Verification

1. Fine-tune a clinical NER model on the n2c2 or MACCROBAT dataset.
2. Map extracted entities to UMLS/SNOMED-CT and measure F1.
3. Build a pipeline to extract diagnosis-procedure relations from discharge summaries.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.1904.05342",
            "https://mimic.mit.edu/docs/iii/",
            "https://www.nature.com/articles/sdata201635",
            "https://aclanthology.org/W19-1909/",
            "https://par.nsf.gov/servlets/purl/10580364",
        ],
    },
    {
        "name": "ai-for-digital-therapeutics",
        "title": "AI for Digital Therapeutics",
        "description": "Software-as-a-medical-device interventions for mental health, substance use, sleep, ADHD, and chronic disease delivered through apps and wearables.",
        "devin_body": r'''
## When to use

You are building software-only, evidence-based interventions (prescription digital therapeutics) for mental health, substance use, sleep, ADHD, or chronic disease.

## Key concepts

- **Prescription digital therapeutics (PDTs)**: FDA-cleared software as a medical device requiring a prescription.
- **Software as a Medical Device (SaMD) and FDA 510(k)/De Novo pathways**.
- **Cognitive behavioral therapy (CBT)** and other behavioral interventions delivered via apps.
- **Real-time biometric feedback**: smartwatch, smartphone sensors, and ecological momentary assessment.
- **Evidence and deployment**: RCTs, real-world evidence, reimbursement, and clinician dashboards.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Predict engagement or response from app usage and sensor data
X = df[['sessions_week', 'cbt_modules_completed', 'sleep_hours', 'heart_rate_variability']]
y = df['responder']

model = GradientBoostingClassifier().fit(X, y)
```

## Tuning notes

- Follow FDA/CE regulatory pathways and provide clinical evidence for intended claims.
- Design for engagement, adherence, and low dropout.
- Protect privacy and secure biometric and patient-reported data.
- Validate with randomized controlled trials and patient-reported outcomes.

## Verification

1. Analyze app usage data to predict treatment adherence.
2. Build a dashboard for clinicians to monitor patient progress.
3. Compare engagement and outcomes between the digital therapeutic and standard care.
''',
        "references": [
            "https://www.healthaffairs.org/doi/10.1377/hlthaff.2024.00159",
            "https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2023.1086219/full",
            "https://doi.org/10.1377/hlthaff.2023.00384",
            "https://doi.org/10.3390/pharmacy13010019",
            "https://accessgudid.nlm.nih.gov/devices/10851580008064",
        ],
    },
]
