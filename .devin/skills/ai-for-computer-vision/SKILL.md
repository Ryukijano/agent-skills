# AI for Computer Vision

## Description

Image classification, detection, segmentation, vision-language models, generative vision, and efficient deep learning deployment.

## When to use

You are building visual perception systems for images: classification, detection, segmentation, vision-language, or image generation.

## Key concepts

- **Convolutional and transformer backbones**: ResNet, ViT, ConvNeXt, and EfficientNet.
- **Object detection and segmentation**: Faster R-CNN, YOLO, Mask R-CNN, and SAM.
- **Vision-language models**: CLIP, Flamingo, LLaVA, and Qwen-VL.
- **Generative vision**: GANs, diffusion models, and image editing.
- **Efficient deployment**: quantization, pruning, knowledge distillation, and NAS.

## Code pattern

```python
import torchvision
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from PIL import Image
import torchvision.transforms as T

model = fasterrcnn_resnet50_fpn(weights="DEFAULT").eval()
image = Image.open("scene.jpg").convert("RGB")
tensor = T.ToTensor()(image)
predictions = model([tensor])
```

## Tuning notes

- Use strong augmentations and pretrained backbones for small datasets.
- Choose model scale based on latency and accuracy trade-offs.
- Leverage foundation models with few-shot prompting or fine-tuning.
- Evaluate with mAP, mIoU, accuracy, and fairness metrics.

## Verification

1. Fine-tune an object detector on a custom dataset and report mAP.
2. Run a vision-language model on image QA and compare to a captioning baseline.
3. Apply a segmentation foundation model to a novel object category.

## References

- https://arxiv.org/abs/2308.13998
- https://arxiv.org/abs/2403.17561
- https://arxiv.org/abs/2304.00685
- https://arxiv.org/abs/2111.07624
- https://arxiv.org/abs/2402.16369
