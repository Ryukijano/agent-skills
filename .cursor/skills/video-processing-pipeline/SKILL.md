---
name: video-processing-pipeline
description: >-
  Build GPU-accelerated video processing pipelines for medical/surgical video. Use when processing video frames, building extraction pipelines, or optimizing video I/O on DGX Spark.
---

# GPU-Accelerated Video Processing Pipeline

## Overview
Techniques for building efficient video processing pipelines on the DGX Spark (GB10), optimized for surgical/endoscopy video.

## Pipeline Architecture
```
Video Input → GPU Decode → Frame Processing → Model Inference → Output
     |              |              |                |              |
  ffmpeg       h264_cuvid     cvcuda ops      CUDA/TensorRT    frames/metrics
```

## GPU Video I/O on GB10

### Decoding
```bash
# GPU-accelerated decode with ffmpeg
ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i input.mp4 -f rawvideo -pix_fmt rgb24 pipe:1

# Or use PyNvVideoCodec for Python
import PyNvVideoCodec as nvc
dec = nvc.CreateDecoder(input)
```

### Encoding
```bash
# H.264 NVENC encoding
ffmpeg -i input.mp4 -c:v h264_nvenc -rc vbr -cq 23 -maxrate 6M -bufsize 6M output.mp4

# Fallback to libx264 if NVENC unavailable
ffmpeg -i input.mp4 -c:v libx264 -crf 23 output.mp4
```

## Frame Processing with cvcuda
```python
import cvcuda  # 0.16.0 in 3d_recon env

# GPU morphology
kernel = cvcuda.Tensor(...)
dst = cvcuda.morphology(src, kernel, cvcuda.MORPH_OPEN, stream=stream)

# GPU Gaussian blur
dst = cvcuda.gaussian_blur(src, kernel_size=(5,5), sigma=1.0, stream=stream)

# GPU color conversion
dst = cvcuda.cvtcolor(src, cvcuda.COLOR_BGR2RGB, stream=stream)

# GPU threshold
dst = cvcuda.threshold(src, thresh=128, maxval=255, type=cvcuda.THRESH_BINARY, stream=stream)
```

## Smart Frame Selection
For surgical video, not every frame needs model inference:
```python
# Stride-based: every Nth frame
stride = 5  # Process every 5th frame

# PPR-gated: only frames with detection confidence > threshold
ppr_threshold = 0.015  # 1.5% of frame area

# Top detection: select top-K frames by detection score
top_k = 6  # Max 6 frames for reconstruction
```

## Endosight Pipeline Integration
```bash
# Check pipeline status
python3 mcp_servers/endosight_pipeline/server.py --cli pipeline_status

# Trigger reconstruction
python3 mcp_servers/endosight_pipeline/server.py --cli run_reconstruction --video_path /path/to/video.mp4 --patient_id 20 --batch_id test_batch
```

## Performance Tips
- Batch frame processing (32-64 frames at once)
- Use CUDA streams for overlap I/O and compute
- Pin memory for CPU↔GPU transfers
- Use NVDEC for decode, cvcuda for processing, TensorRT for inference
- Avoid CPU round-trips: keep data on GPU between stages

## Reference Files
- Endosight: `/home/aimsgroupuol/endosight_project/endosight-3d/`
- MCP: `mcp_servers/endosight_pipeline/server.py`
- Skill: `surgical-video-analysis`

