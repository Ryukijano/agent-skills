# AI for Radiology

## Description

Deep learning for X-ray, CT, MRI, and mammography interpretation, including lesion detection, segmentation, report generation, and radiology foundation models.

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

## References

- https://pubs.rsna.org/doi/10.1148/radiol.240597
- https://link.springer.com/article/10.1007/s10334-024-01173-8
- https://www.nature.com/articles/s41467-024-51202-2
- https://www.mdpi.com/2075-4418/15/3/282
- https://link.springer.com/article/10.1007/s00330-022-08784-6
