# AI for Ophthalmology

## Description

Diabetic retinopathy screening, OCT analysis, glaucoma detection, and AI for retinal disease diagnosis from fundus photography.

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

## References

- https://doi.org/10.1001/jama.2016.17216
- https://jamanetwork.com/journals/jama/fullarticle/2588763
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8063221/
- https://www.nature.com/articles/s41433-023-02720-8
