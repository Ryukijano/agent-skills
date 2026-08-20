# AI for Medical Imaging

## Description

General medical image preprocessing, segmentation, classification, and deployment with DICOM, MONAI, nnU-Net, and clinical AI pipelines.

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

## References

- https://project-monai.github.io/
- https://docs.monai.io/en/stable/
- https://github.com/Project-MONAI/MONAI/
- https://www.nature.com/articles/s41592-020-01008-z
- https://github.com/mic-dkfz/nnunet/
