# world-model-surgical-adaptation

## Description
Adapt large-scale world models (V-JEPA 2, COSMOS) to surgical video domains for scene prediction, phase recognition, and instrument tracking. Combines self-supervised video pretraining with domain-specific fine-tuning to build a surgical world model that understands procedural context and can predict future states.

## Background
World models like V-JEPA 2 and NVIDIA COSMOS learn rich video representations through self-supervised prediction. Adapting these to surgical video enables: predicting next instrument positions, recognizing surgical phases without dense annotations, and building spatially-consistent scene representations for downstream tasks (MOT, segmentation, 3D reconstruction).

## Key Models
### V-JEPA 2 (Meta)
- Architecture: Vision Transformer (ViT-H/16) with joint embedding predictive architecture
- Pretraining: Predicts masked spatiotemporal patches in latent space (no pixel reconstruction)
- Surgical adaptation: Fine-tune on CholecT50/EndoVis with phase labels; use encoder for DINO-Endo features
- Key advantage: Extremely data-efficient fine-tuning (few-shot capable)

### COSMOS (NVIDIA)
- Architecture: Diffusion World Foundation Model (Video + 3D)
- Pretraining: Massive physical world simulation data + real video
- Surgical adaptation: Use COSMOS tokenizer to encode endoscopic frames; fine-tune on surgical trajectories
- Key advantage: Generates photorealistic future frame predictions for data augmentation

## Adaptation Pipeline
### Step 1: Data Preparation
```python
# Convert surgical video to V-JEPA format
# 16 frames per clip, 224x224, temporal stride=2
import decord
from pathlib import Path
def prepare_surgical_clips(video_path, output_dir, clip_len=16, stride=2):
    vr = decord.VideoReader(str(video_path))
    clips = []
    for start in range(0, len(vr) - clip_len * stride, clip_len):
        indices = [start + i * stride for i in range(clip_len)]
        clip = vr.get_batch(indices).asnumpy()
        clips.append(clip)
    return clips
```

### Step 2: V-JEPA 2 Fine-tuning
- Load pretrained V-JEPA 2 checkpoint
- Add linear probe for phase classification on top of frozen encoder
- Or full fine-tune with surgical video dataset for instrument-aware representations
- Training: 10-50 epochs, lr=1e-4, cosine decay, batch=32 on H100

### Step 3: Evaluation
- Phase recognition: Top-1 accuracy on CholecT50 phases (7 classes)
- Instrument detection: mAP on EndoVis 2017 instrument bounding boxes
- Temporal prediction: FID/FVD on predicted vs. actual future frames

## DINO-Endo Integration
The adapted world model encoder serves as the backbone for DINO-Endo:
1. Extract per-frame features using V-JEPA 2 encoder (1280-dim)
2. Feed into DETR detection head for instrument bounding boxes
3. Use temporal context from world model for multi-object tracking
4. Phase recognition head predicts surgical phase from sequence features

## Key Tips
- Start with V-JEPA 2 for feature extraction before attempting COSMOS generation
- Use CholecT50 for phase recognition and EndoVis 2018 for instrument segmentation
- Freeze encoder for first 5 epochs, then unfreeze top layers gradually
- Surgical video has high motion blur; use temporal augmentation (random speed change)
- Evaluate on per-phase metrics, not just overall accuracy (class imbalance is severe)

## References
- V-JEPA 2: https://ai.meta.com/research/publications/v-jepa-2/
- COSMOS: https://research.nvidia.com/labs/dir/cosmos/
- CholecT50: https://github.com/CAMMA-public/cholect50
- Related skills: vjepa-physics-world-model, surgical-mot-eval, tdv-pretrain, surgical-video-data-pipeline

## Paper Reading Tasks

### World Models
- [ ] V-JEPA 2 (Meta, 2025) - arXiv 2506.09985 - Task: Reproduce surgical phase classification on CholecT50
- [ ] COSMOS (NVIDIA, 2024) - arXiv 2501.03575 - Task: Run tokenizer on EndoVis18 clips
- [ ] DreamerV3 (Hafner et al., 2023) - arXiv 2301.04104 - Task: Study RSSM for surgical phase transitions
- [ ] UniSim (Yang et al., 2023) - arXiv 2308.01842 - Task: Synthetic surgical video generation for data aug

### Surgical Video Understanding
- [ ] CholecTrack20 (Nwoye et al., 2023) - arXiv 2312.07345 - Task: Evaluate GOT-JEPA baseline; identify failure modes
- [ ] SurgicalSAM (2023) - arXiv 2308.08423 - Task: Instrument mask pseudo-labels for world model training
- [ ] Temporal Difference in Vision (TDV) - Task: Integrate TDV pretraining into world model pipeline

### 3D Vision & Reconstruction
- [ ] EndoSurf (Zha et al., 2023) - arXiv 2307.11307 - Task: Depth estimation as world model input
- [ ] MonST3R (2024) - arXiv 2410.03825 - Task: Depth maps for scene representation enrichment

## Implementation Checklist
- [ ] Read V-JEPA 2 paper -> reproduce encoder fine-tune on CholecT50
- [ ] Run COSMOS tokenizer on 10 EndoVis clips -> measure reconstruction quality
- [ ] Compare V-JEPA 2 vs DINO-Endo features on CholecTrack20 detection task
- [ ] Study DreamerV3 RSSM -> sketch surgical phase transition model
- [ ] Integrate MonST3R depth as auxiliary channel in world model input
- [ ] Deploy SurgicalSAM for instrument mask pseudo-labels
