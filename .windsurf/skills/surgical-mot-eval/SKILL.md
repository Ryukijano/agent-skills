---
name: surgical-mot-eval
description: Evaluate surgical multi-object tracking models on CholecTrack20. Use when running MOT evaluation, computing mAP/MOTA/MOTAP metrics, analyzing tracking results, or comparing detection performance across configurations.
---

## Surgical MOT Evaluation on CholecTrack20

### Dataset structure

```
cholectrack20/
├── Training/
│   ├── VID02/  (frames + annotations)
│   ├── VID04/
│   └── ...
├── Validation/
│   ├── VID30/
│   └── VID110/
└── Testing/
    ├── VID01/
    └── ...
```

7 surgical tools: `Grasper`, `Bipolar Forceps`, `Clipper`, `Hook`, `Scissors`, `Irrigator`, `Specimen Bag`

### Key metrics

| Metric | Description | Target |
|--------|-------------|--------|
| mAP@50 | Mean Average Precision at IoU=0.5 | ≥ 0.35 |
| mAP@[.5:.95] | COCO-style mAP | ≥ 0.15 |
| MOTA | Multi-Object Tracking Accuracy | ≥ 60 |
| MOTAP | MOT Average Precision | ≥ 40 |
| IDF1 | ID F1 Score | ≥ 50 |
| Track precision | Bounding box precision per track | ≥ 0.7 |

### Evaluation script

```bash
python scripts/eval_mot.py \
    --config configs/train_mot/dinov2/cholec20-mot-stage1-lora-detect.yaml \
    --checkpoint outputs/mot/<run_name>/best.pth \
    --split val \
    --output outputs/mot/<run_name>/eval_results/
```

### Analyzing results

```python
# Load evaluation results
import json
with open('outputs/mot/<run>/eval_results/metrics.json') as f:
    metrics = json.load(f)

# Per-tool AP
for tool, ap in metrics['per_tool_ap50'].items():
    print(f"{tool}: AP@50 = {ap:.3f}")

# Identify failure modes
low_ap_tools = {t: ap for t, ap in metrics['per_tool_ap50'].items() if ap < 0.2}
if low_ap_tools:
    print(f"Low AP tools: {low_ap_tools}")
    # Check: insufficient training data, small objects, occlusion
```

### Common failure modes

1. **Low mAP on small tools** (Scissors, Clipper): Add multi-scale features, increase image resolution
2. **ID switches**: Increase ReID embedding dimension, add appearance loss
3. **Missed detections in occluded frames**: Use temporal smoothing, increase `max_age` in tracker
4. **False positives on specular reflections**: Add hard negative mining, increase `infer_score_threshold`
5. **Query collapse** (all queries predict same location): Use DN-DETR denoising, deformable attention

### Leak-free evaluation

**Never** evaluate on videos that overlap with SSL pretraining corpus:
- CT20 Test: VID01, VID06, VID07, VID12, VID25, VID39, VID92, VID111
- CT20 Val: VID30, VID110
- These must be excluded from all SSL/training stages
