# AI for Neurology

## Description

Neuroimaging and EEG analysis for stroke, brain tumors, epilepsy, and neurodegeneration, including lesion segmentation and outcome prediction.

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

## References

- https://pmc.ncbi.nlm.nih.gov/articles/PMC12083563/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11229702/
- https://www.nature.com/articles/s41467-025-62373-x
- https://link.springer.com/article/10.1007/s44163-026-00926-9
