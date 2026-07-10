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


## X Bookmarks - New AI Papers & Posts (July 2026)

### Embodied World Models & Robotics
- [ ] RynnWorld-4D (Alibaba) - 4D embodied world model predicting RGB, depth & optical flow from RGB-D + instruction; tri-branch diffusion; bridges world prediction and robot control - Task: Study 4D prediction branch for surgical scene forecasting
- [ ] AdaJEPA - Adaptive world model that plans, acts, and adapts in closed loop - Task: Compare with V-JEPA 2 on adaptive surgical phase tracking
- [ ] OMG: Omni-Modal Motion Generation for Generalist Humanoid Control (Tsinghua) - scalable brain generating motions from language, audio or reference - Task: Explore multi-modal control signals for surgical robot guidance
- [ ] HDFlow - Hierarchical Diffusion-Flow Planning for long-horizon robotic tasks (ICML 2026 Spotlight) - Task: Apply hierarchical planning to multi-step surgical workflows
- [ ] Qwen-RobotManip (Alibaba) - VLA foundation model for robotic manipulation trained on ~38,100 hours of open-source data - Task: Benchmark VLA alignment techniques for surgical instrument control

### 3D Vision & Reconstruction
- [ ] Volume Transformer (ECCV 2026) - Revisits vanilla Transformers for 3D scene understanding via volumetric patch tokens - Task: Compare volumetric tokenization with COSMOS tokenizer for endoscopic 3D
- [ ] GS-SDF - LiDAR-Augmented Gaussian Splatting + Neural SDF for geometrically consistent rendering and reconstruction - Task: Adapt for depth-consistent surgical scene reconstruction
- [ ] SuperFlex (CVPR 2026) - Compact & explicit 3D object/scene representations via superquadric decomposition - Task: Explore superquadric representations for surgical instrument shape priors
- [ ] FoundObj (ICML 2026, arXiv 2605.27178) - Self-supervised 2D/3D foundation models as RL rewards to segment 3D scenes without scene-level labels - Task: Apply to endoscopic 3D anatomy segmentation without dense annotations
- [ ] FreeOrbit4D (UIUC/UPenn/Eyeline Labs) - Training-free monocular video re-rendering to any new camera path - Task: Evaluate novel-view synthesis for surgical camera trajectory planning

### Efficient Models & Training Tricks
- [ ] Sparse Delta Memory / SDM (Loic cabannes PhD) - GatedDeltaNet + Product Key sparsity; recurrent state 3000x larger at same FLOPs - Task: Investigate sparse memory for long surgical video context modeling
- [ ] DFlash (Zhijian Liu, ICML 2026) - Speculative decoding with block diffusion; 6.2x lossless speedup on Qwen3-8B - Task: Apply fast LLM decoding for real-time surgical instruction generation
- [ ] MrFlow - 10x training-free diffusion acceleration via staged sampling + single high-res refinement step; works with FLUX/Qwen-Image - Task: Accelerate COSMOS diffusion for surgical video prediction
- [ ] Is One Layer Enough? (arXiv 2407.11535) - Single transformer layer training matches full-parameter RL training; most gains concentrated in middle layers - Task: Study layer-selective fine-tuning for V-JEPA 2 surgical adaptation

### VLA & Robot Policies
- [ ] VLA-Corrector (Alibaba/ZJU) - Lightweight plug-in for action-chunked policies that monitors latent visual dynamics, drops stale actions and replans on the fly - Task: Adapt latent drift detection for surgical phase transition handling
- [ ] LabVLA (ZJU/Shanghai AI Lab/HIT) - VLA for real-lab experiment robots using RoboGenesis simulation engine - Task: Study simulation-to-real transfer strategy for surgical robot training
- [ ] Semantic Action RL (Levine et al.) - RL over VLA prompts enables new tasks and faster learning in real world - Task: Investigate RL-based prompt optimization for surgical phase commands

### Benchmarks & Evaluation
- [ ] Video-MME-Logical - Controlled benchmark for video temporal-logical reasoning across 25 tasks; exposes MLLM reasoning gap - Task: Evaluate surgical video MLLMs on temporal reasoning about procedure steps
- [ ] LLM-as-a-Verifier (arXiv 2607.05591) - General-purpose verification framework for LLM agents; SOTA on Terminal-Bench V2, SWE-Bench, RobotBench - Task: Use verification framework to evaluate surgical procedure completion quality


## X Feed - New AI Posts (July 10, 2026 - Not Bookmarked)

### Video & Diffusion Models
- [ ] Hex-Forcing (NVIDIA AI Research) - Video generation method that lets a single model switch between bidirectional and autoregressive generation modes at inference time - Task: Apply switchable generation mode for flexible surgical video prediction (structured phase vs. streaming frame-by-frame)
- [ ] LingBot-Video (alphaXiv) - Video model built for robotics that learns action, motion, and physical cause-and-effect rather than appearance - Task: Evaluate action-aware video representation for surgical instrument trajectory prediction
- [ ] Flex-Forcing (NVIDIA) - Flexible conditioning for video diffusion; single model handles both chunk-level bidirectional and autoregressive inference - Task: Test flex conditioning for controlled endoscopic frame generation
- [ ] MobileWan (Amir Habibian) - Wan 2.2 video generation ported to mobile devices with accompanying technical report - Task: Explore lightweight video generation for on-device surgical assistance

### Agents, Memory & Long-Context
- [ ] Remember When It Matters (Meta AI) - Proactive memory agent for long-horizon tasks; addresses behavioral state decay where agents forget previously-made decisions - Task: Apply proactive memory to multi-step surgical workflow agents
- [ ] KAT-Coder-V2.5 (KwaiKAT via alphaXiv, arXiv 2607.05471) - Coding agent rivaling GLM-5.2; argues better coding agents need better training worlds not just bigger models; uses AutoBuilder for curriculum - Task: Adapt self-improving training world concept for surgical scene simulation curricula
- [ ] HiLS-Attention (Tencent, 7B) - Sparse attention model with end-to-end learned chunk selection for ultra-long context - Task: Evaluate long-context attention for hours-long surgical video understanding
- [ ] GEA: Open-ended Agent Self-Improvement via Experience Sharing (UCSB AI, github.com/UCSB-AI/GEA) - Agents that continuously learn from live workloads via experience sharing - Task: Apply experience sharing to surgical workflow agent improvement
- [ ] Track2Map (Kwang Moo Yi) - Online deformable SLAM with motion-aware pose optimization for robotic surgery (CoTracker3 + Dynamic 3D Gaussians for endoscopy) - Task: Directly relevant — integrate Track2Map into DINO-Endo pipeline for scene SLAM

### Quantization & Efficient Inference
- [ ] NVFP4 RL Training Recipe (Humans AI, open-source) - Hardware-native 4-bit NVFP4 reinforcement learning training for Blackwell GPUs - Task: Profile NVFP4 quantization for V-JEPA 2 inference on HPC H100/H200 nodes
- [ ] NVFP4 Kimi-K2.7-Code (NVIDIA/HuggingPapers) - 1T-parameter model quantized to NVFP4 for Blackwell GPUs - Task: Study 1T-scale quantization strategies for large world model deployment
- [ ] VBR: Variable Bit Rate KV Cache (spiritbuun) - Dynamically quantizes KV cache layer-by-layer during inference - Task: Apply VBR to reduce KV cache memory for long surgical video context windows
- [ ] Qwen3.6 (UnslothAI) - New quants running 2.5x faster on GPU with improved tool calling, agent use, and looping - Task: Evaluate Qwen3.6 for surgical instruction following and phase command generation
- [ ] cuVSLAM (NVIDIA, now open-source on GitHub) - CUDA-accelerated visual SLAM with high-performance localization for drones and mobile robots, ROS 2 compatible - Task: Directly relevant — benchmark cuVSLAM for real-time endoscopic camera tracking vs. Track2Map

### Foundation Models & Frontier Releases
- [ ] GPT-5.6 Sol (OpenAI) - Best vision model from OpenAI; massive gains in object detection, counting, OCR - Task: Benchmark GPT-5.6 vision capabilities on surgical instrument detection and counting
- [ ] Grok 4.5 (xAI, now on free tier) - Frontier model available via Grok Build for any X or Grok account - Task: Compare Grok 4.5 vs GPT-5.6 on surgical phase reasoning benchmarks
- [ ] OpenFold3 on NVIDIA Blackwell (NVIDIA Healthcare) - Biomolecular structure prediction with 4x faster inference on Blackwell, MSA GPU search 177x faster - Task: Monitor protein structure prediction advances for potential surgical planning applications
- [ ] Tinker (Mira Murati / Thinking Machines) - Open weights model training platform for custom multimodal AI; anyone can train their own open-weights models - Task: Evaluate Tinker for fine-tuning surgical video understanding models
- [ ] Isaac Lab (NVIDIA Robotics, 1M downloads) - Open-source framework for training next-gen robots; milestone of 1M downloads reached - Task: Integrate Isaac Lab simulation environments for surgical robot skill learning
