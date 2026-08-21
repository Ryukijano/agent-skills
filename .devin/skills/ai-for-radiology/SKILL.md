# AI for Radiology

## Description

Use AI for Radiology to detect, segment and report abnormalities in radiological images such as X-ray, CT, MRI and mammography.

## When to use

You need to detect, classify, or segment abnormalities on radiological images; build foundation models for radiology; or integrate an AI triage tool into a PACS/DICOM workflow.


## Usage


- **Modality-aware preprocessing**: HU scaling for CT, window/level for X-ray, bias field correction and intensity normalization for MRI.
- **Lesion segmentation**: U-Net, nnU-Net, SwinUNETR, and VISTA-3D for 2D/3D anatomy.
- **Radiology foundation models**: Self-supervised pretraining on large radiology corpora (e.g., RADImageNet, CheXzero, MedImageInsight).
- **Workflow integration**: DICOM/FHIR I/O, AI result routing, worklist prioritization, and structured reporting.
- **Safety and equity**: External validation, underdiagnosis bias in underserved populations, and confidence calibration.

## Steps

1. Collect and prepare DICOM/NIfTI studies and radiology reports.
2. Detect, classify, or segment abnormalities on radiological images.
3. Build foundation models for radiology.
4. Integrate an AI triage tool into a PACS/DICOM workflow.
5. Validate by training a lesion segmentation model and compare Dice to an inter-reader benchmark.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

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

## References

- https://pubs.rsna.org/doi/10.1148/radiol.240597
- https://link.springer.com/article/10.1007/s10334-024-01173-8
- https://www.nature.com/articles/s41467-024-51202-2
- https://www.mdpi.com/2075-4418/15/3/282
- https://link.springer.com/article/10.1007/s00330-022-08784-6
