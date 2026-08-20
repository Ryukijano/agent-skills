# AI for Dermatology

## Description

Skin lesion classification, dermoscopy analysis, melanoma detection, teledermatology, and fairness across skin tones with deep learning.

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

## References

- https://doi.org/10.1038/nature21056
- https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2023.1305954/full
- https://www.mdpi.com/2072-6694/15/4/1183
- https://www.sciencedirect.com/science/article/pii/S0022202X23029640
- https://engineering.stanford.edu/news/how-researchers-trained-algorithm-diagnose-skin-cancer
