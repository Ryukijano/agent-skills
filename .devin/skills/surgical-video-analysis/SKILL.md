---
name: surgical-video-analysis
description: >-
  Analyze surgical video for MOT, detection, and scene understanding. Use when processing endoscopy video, running detection models, evaluating tracking, or building surgical AI pipelines.
---

# Surgical Video Analysis

## Overview
Guidance for building and evaluating surgical video analysis pipelines: multi-object tracking (MOT), instrument detection, polyp detection, and scene understanding.

## Key Datasets
- **CholecTrack20**: Surgical MOT benchmark with instrument annotations
- **CholecSeg8K**: Semantic segmentation of surgical scenes
- **EndoVis**: MICCAI sub-challenge datasets for surgical vision

## Pipeline Stages
1. **Frame extraction**: ffmpeg/nvdec for GPU-accelerated decoding
2. **Detection**: TGANet, RT-DETR, D-FINE for surgical instruments
3. **Tracking**: ByteTrack, BoT-SORT for MOT
4. **Evaluation**: HOTA, MOTA, mAP metrics
5. **Visualization**: Overlay bounding boxes, tracks, segmentation masks

## DGX Spark Optimization
- Use `h264_cuvid` / `h264_nvenc` for GPU video I/O
- cvcuda 0.16.0 for GPU morphology/gaussian/cvtcolor
- Batch frame processing to maximize GPU utilization
- Smart frame selection (stride 5, PPR gate) to reduce TGANet passes

## Evaluation Metrics
- **HOTA**: Higher Order Tracking Accuracy (primary MOT metric)
- **MOTA**: Multi-Object Tracking Accuracy
- **mAP**: mean Average Precision for detection
- **DetA / AssA**: Detection / Association components of HOTA

## Reference Files
- MOT repo: `/home/aimsgroupuol/Gyanateet_tracking/`
- Endosight: `/home/aimsgroupuol/endosight_project/endosight-3d/`
- Skills: `surgical-mot-eval`, `mot-training-workflow`, `tdv-pretrain`

