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


## X Bookmarks & Feed - New AI Papers & Posts (July 11-14, 2026)

### Vision Foundation Models
- [ ] GenCeption (Google DeepMind) - Single feed-forward vision model matching specialist depth, surface normals, and 3D pose/segmentation networks - Task: Evaluate GenCeption as unified encoder for DINO-Endo replacing separate depth/seg heads
- [ ] Vision Pretraining for Dense Spatial Perception (Trending on Papers with Code, Jul 12) - Task: Read and compare dense pretraining strategy vs. V-JEPA 2 masked spatiotemporal prediction for surgical scene understanding
- [ ] LingBot-Vision (Ant Group, Jul 11) - Self-supervised ViT backbone with masked boundary modeling for dense spatial perception; strong on depth, segmentation, embodied tasks - Task: Benchmark as drop-in encoder replacement for DINO-Endo
- [ ] SenseNova-Vision (Dahua Lin / SenseTime) - Unifies wide range of vision tasks into a single generative model - Task: Evaluate unified generative vision for multi-task surgical scene understanding
- [ ] State-Prediction Separation Hypothesis (alphaXiv, arXiv 2607.012.8v1, Cornell/Harvard) - Separates hidden state into two streams (memory vs. prediction); improves downstream task performance significantly at 1-4B params - Task: Apply state-prediction separation to V-JEPA 2 fine-tuning for surgical phase memory vs. frame prediction

### Embodied AI & Robotics
- [ ] UniVR-34B (ByteDance) - 34B model learning complex reasoning, physical dynamics, and long-term planning directly from visual demonstrations; dataset on HuggingFace - Task: Study visual demonstration learning for surgical skill acquisition
- [ ] LingBot-VA 2.0 (Yinghao Xu) - Native video-action foundation model for generalizable robot control - Task: Adapt video-action architecture for surgical instrument control from endoscopic video
- [ ] π*0.6 (Physical Intelligence, Laura Smith, RSS 2026) - New iteration of pi-zero policy presented at RSS 2026 VLA session - Task: Study pi-zero policy architecture for dexterous surgical manipulation
- [ ] BEHAVIOR Challenge Year 2 (Fei-Fei Li / Stanford) - Complex long-horizon tasks with 1950 hours of human teleoperation data, 200 demos/task, rich language annotations - Task: Use BEHAVIOR-style long-horizon evaluation framework for surgical workflow benchmarking
- [ ] Instance (Lucy Cai) - Success detector for robot rollouts; describe task + drop in dataset → judges success/fail with detailed subtask captions; outperforms Claude Opus 4.8 at lower latency - Task: Directly relevant — adapt Instance-style success detection for surgical phase completion verification
- [ ] RoboLab (NVIDIA Robotics) - Framework for evaluating robot policies for real-world deployment; general-purpose evaluation for general-purpose robots - Task: Benchmark surgical robot policies using RoboLab real-world evaluation protocol
- [ ] PyRoki (Ilir Aliu) - 1.7x faster GPU-accelerated inverse kinematics in pure Python; open-source; supports IK, trajectory optimization, motion retargeting - Task: Integrate PyRoki for real-time surgical instrument kinematic optimization
- [ ] RoboDojo (Cybernetic Labs) - Unifies sim-and-real evaluation to measure sim-to-real gap for manipulation policies - Task: Apply sim-to-real evaluation methodology for surgical robot policy validation
- [ ] SuperMap (ShiboZhaoSLAM, RSS 2026) - Spatio-temporal SLAM system for visual-language navigation; living spatial memory that perceives, remembers evolution, and supports reasoning/action - Task: Directly relevant — apply SuperMap's living spatial memory to endoscopic scene understanding across a procedure

### World Models & Streaming Video
- [ ] UniVR-34B (ByteDance) - Learns physical dynamics and long-term planning from video; VR-X-SFT-RL training dataset - Task: Evaluate ByteDance VR data pipeline for surgical video world model pretraining
- [ ] Wan-Streamer v0.2 (Alibaba, DailyPapers Jul 11) - Latency-preserving video streamer 192p to 640x368 at 25 FPS with ~200ms model latency; scene-grounded mid-shot agents for clearer video calls - Task: Adapt streaming video generation for real-time surgical video prediction at low latency
- [ ] Vidu S1 (Tsinghua University, arXiv 2607.07165v1) - Real-time interactive video generation model supporting voice-controlled digital character animation; infinite-length real-time video at up to 42 FPS on consumer GPUs - Task: Study real-time video generation for interactive surgical simulation
- [ ] TC-WM (Biwei Huang, UC San Diego, arXiv 2605.25620) - Task-Centric World Model learning grounded dynamics in compact latent space keeping scalability of video foundation models - Task: Core reference — TC-WM's task-centric latent space directly relevant to surgical phase-aware world modeling

### Memory & Long-Context Agents
- [ ] LLMs Need Sleep / Memory Consolidation (Ali Behrouz / Google) - Sleep phase where model consolidates short-term memories into stable long-term memories (dreaming) - Task: Apply sleep-phase memory consolidation to surgical workflow agents for multi-session learning
- [ ] BRAID (DailyPapers) - Multi-turn text-image-text reasoning as unified Markov decision process; joint RL optimization of textual and visual generation - Task: Apply unified text-image RL for surgical instruction-following with visual feedback
- [ ] PaperPilot - Multi-turn literature search agent with executable DAG workflows for improved retrieval accuracy - Task: Use for automated surgical CV literature monitoring

### Efficient Inference & Quantization
- [ ] Molt (NVIDIA NeMo + vLLM) - Agentic-first RL framework using vLLM as rollout engine; fast async serving up to 1T-class MoE scale - Task: Evaluate Molt for scaling surgical scene reasoning with large MoE models
- [ ] NVIDIA Nemotron Ultra on Ollama - Fastest growing open-source model on Ollama; unlocking complex, longer-running tasks for developers - Task: Test Nemotron Ultra for on-device surgical assistance reasoning
- [ ] AI Model Co-Design series (NVIDIA AI) - Exploring synergy between model dimensions and GPU architecture; how model size influences compute-memory bound tradeoffs - Task: Apply co-design principles when sizing V-JEPA 2 variants for HPC deployment

### Quantum Computing
- [ ] Quantum Circuits via Lie Group Diffusion Models (Jyotirmai Singh, arXiv 2606.29636) - Encodes physical structure of quantum gates natively on Lie group SU(2) instead of normal diffusion - Task: Directly relevant to quantum work — study Lie group diffusion for VQE circuit design

### 3D Vision & Geometry
- [ ] Point Cloud Geometry as Statistical Manifold (Giseop Kim, RSS 2026, arXiv 2605.10456) - Theory and practice for learning 3D point cloud geometry on statistical manifolds - Task: Apply manifold geometry learning to endoscopic 3D point cloud reconstruction
- [ ] StereoGS (Kwang Moo Yi) - Sparse-view 3D Gaussian Splatting with stereo priors as regularizers during training - Task: Evaluate stereo-prior regularization for surgical stereo endoscope Gaussian splatting
- [ ] Doppelganger Problem in 3D (Gabriele Berton) - Identical-looking scenes breaking 3D reconstruction pipelines; using doppelgangers as hard negatives for matching training - Task: Address surgical scene repetition (similar bowel loops, tissue folds) in endoscopic 3D
- [ ]
- [ ] ## X Bookmarks & Feed - New AI Papers & Posts (July 14-18, 2026)

### World Models (New Architectures)
- [ ] Mechanistic World Models (Ingmar Posner, arXiv 2607.12474) - Scientific discovery requires uncovering the mechanisms generating observations; proposes mechanistic rather than correlational world models - Task: Core theoretical reference — read for mechanistic inductive biases in surgical world model design
- [ ] Xiaomi-Robotics-U0 (Xiuyu Li) - 38B autoregressive world foundation model for multi-view embodied synthesis; improves out-of-distribution real-robot policy success from 36.9% to 63.2% - Task: Study autoregressive world model architecture for out-of-distribution surgical scene generalization
- [ ] Mira Mini (hugo) - Minimal world model: 364M params, open weights, reproduced in a week — "how small can you make a world model?" - Task: Benchmark minimal world model footprint for resource-constrained HPC surgical inference
- [ ] TC-WM / Task-Centric World Model (UC San Diego, arXiv 2605.25620) - Grounds dynamics in compact task-centric latent space while maintaining scalability of video foundation models - Task: Core reference — implement task-centric latent spaces for surgical phase-aware world modeling
- [ ] CW-VAE / Clockwork VAE (Sasha Malysheva, NeurIPS 2021, arXiv 2102.09532) - Hierarchical VAE with temporal abstraction over 4 levels; foundational paper predating JEPA-style joint-embedding predictors - Task: Study hierarchical latent temporal abstraction for multi-scale surgical phase/step modeling

### Self-Supervised Learning & Representations
- [ ] VISReg (Haiyu Wu, Jul 14) - New regularization loss for SSL that replaces heuristic training tricks (EMA, teacher-student, layer freezing); best OOD performance, robust to low-quality data, data efficient - Task: Replace EMA-based training in V-JEPA 2 fine-tuning with VISReg for more stable surgical domain adaptation
- [ ] Predicting Latents > Predicting Tokens (Sasha Malysheva/DanKorchinski) - Paper showing data2vec/JEPA-style latent prediction outperforms token prediction on downstream tasks - Task: Empirically validate on surgical video: latent prediction (JEPA) vs. masked token prediction (MAE) for scene understanding
- [ ] Relative Representations (Moschella et al., ICLR 2023, arXiv 2209.15430) - Describes data points by similarity to fixed landmarks; enables model stitching without retraining - Task: Apply relative representations to align surgical video encoders from different modalities (endoscopic, laparoscopic, robotic)
- [ ] Diffusing Blame / Dale's Principle Network (Sakana AI, hardmaru) - Neural network that strictly follows Dale's principle (neurons either excite or inhibit neighbors, never both); uses backprop with routing - Task: Explore biologically-constrained network architectures for surgical signal routing (instrument ON vs. OFF signals)

### Embodied AI & Robotics (New)
- [ ] RxBrain (Tencent, DailyPapers Jul 15) - Embodied cognition foundation model unifying language reasoning, visual imagination, and world state prediction into single multi-modal framework - Task: Study tri-modal (language + imagination + world-state) fusion for surgical scene understanding and planning
- [ ] WALA (Robots Digest, Jul 14) - World-to-Action Learning via abundant human-world interaction videos; learns executable latent actions jointly from action-labeled robot demos + human videos - Task: Directly relevant — use WALA to bootstrap surgical instrument actions from laparoscopy training videos without robot labels
- [ ] B-spline Policy / BSP (Haoyu Xiong) - Parameterizes robot actions as continuous B-spline curves instead of discrete fixed-rate action chunks - Task: Apply B-spline action parameterization for smooth surgical instrument trajectory prediction
- [ ] LingBot-Depth (DataScienceHarp) - Vision transformer trained with missing depth-sensor pixels as natural masks for depth learning - Task: Adapt depth-mask pretraining for endoscopic depth estimation from partial/occluded surgical scene views
- [ ] SE(3)-LIO (Ryohei Sasaki, ICRA 2026) - Smooth IMU propagation with jointly distributed poses on SE(3) manifold for accurate LiDAR-Inertial Odometry - Task: Apply SE(3) manifold pose representation to endoscopic camera odometry for robust 3D tracking
- [ ] ACT-2 Laundry / Sunday Robotics (1000 memory developers milestone) - Long-horizon dexterous manipulation task with memory-augmented policy - Task: Study memory-augmented policies for long-horizon surgical procedures

### Efficient Architectures & Training
- [ ] Ring-Zero: Scaling Zero RL to a Trillion Parameters (HuggingPapers) - RL training pipeline with verifiable rewards; emergent reasoning including self-verification at scale - Task: Apply verifiable reward RL training for surgical phase classification with automatic correctness checking
- [ ] DeepLoop (Raj Dabre, arXiv 2607.13491) - Depth scaling for looped transformers; makes loop transformers stable and scalable - Task: Evaluate looped transformer depth scaling for test-time adaptation on new surgical procedure types
- [ ] xHC: Expanded Hyper-Connections (alphaXiv) - Expanded residual memory with causal conv writeback features for transformer efficiency - Task: Evaluate hyper-connections as efficient cross-frame memory for long surgical video processing
- [ ] LongStraw (Mind Lab, open-source) - Long-context RL beyond 2M tokens under fixed GPU budget; enables ultra-long context reasoning - Task: Apply long-context RL to multi-hour surgical procedure understanding within HPC memory budgets
- [ ] Sliding Window Attention overview (Niels Rogge) - SWA used in GPT-OSS, Gemma, Microsoft MAI to reduce KV-cache memory for long-context - Task: Benchmark SWA vs. HiLS-Attention for memory-efficient long surgical video processing
- [ ] KronQ (HuggingPapers) - Post-training quantization framework for Llama-3-70B achieving 7.93 perplexity at 2-bit - Task: Evaluate KronQ 2-bit quantization for surgical scene reasoning models on edge deployment
- [ ] Cosmos 3 Nano + LoRA post-training (NVIDIA AI) - LoRA post-training on COSMOS Nano improved zero-shot traffic signal identification 54.41% → 87.14% - Task: Directly relevant — replicate LoRA post-training on COSMOS Nano for zero-shot surgical instrument identification

### 3D Vision (New)
- [ ] VGG-TTT: Offline Feed-Forward 3D Reconstruction at Scale (Kwang Moo Yi / Elflein et al.) - VGGT with test-time training to compress KV space; TTT reminiscent of scene coordinate regression networks - Task: Evaluate TTT-based 3D reconstruction for on-the-fly endoscopic scene mapping
- [ ] VGGT as MoE Experts (Kwang Moo Yi) - Feed-forward 3D models showing emergent behaviors; VGGT experts in Mixture of Experts for co-visibility prediction - Task: Study VGGT-MoE for multi-view surgical scene 3D understanding from multiple endoscope positions
- [ ] Uncertainty Quantification for Flow-Based VLA Models (arXiv 2606.18043) - UQ for vision-language-action flow policies - Task: Apply flow-based UQ to surgical instrument action prediction for safer robotic
- [ ]
- [ ] ## X Bookmarks, Feed & WhatsApp - New AI Papers & Links (July 18-21, 2026)

### World Models & Video Generators as World Models
- [ ] UniVR: Thinking in Visual Space for Unified Visual Reasoning (ByteDance/BJTU, arXiv 2607.128) - +25% on VR-X benchmark; fully open-source github.com/bytedance/UniVR - Task: Benchmark UniVR for surgical instrument state reasoning from video
- [ ] GenCeption (Google DeepMind, The Decoder) - Video generators repurposed for depth estimation and segmentation; implicit world models inside video generators - Task: Use GenCeption for zero-shot surgical depth and segmentation from COSMOS video generator
- [ ] GigaWorld-Policy-0.5 (HuggingFace papers/2607.13960) - Faster World Action Model (WAM) empowered by AutoResearch - Task: Study GigaWorld policy architecture for fast surgical world model inference
- [ ] Cosmos3-Edge (NVIDIA, huggingface.co/nvidia/Cosmos3-Edge) - Edge-optimized COSMOS model - Task: Deploy Cosmos3-Edge for on-device surgical video prediction at inference time
- [ ] AdaJEPA (agenticlearning.ai/adajepa/) - Adaptive JEPA world model for closed-loop planning/acting - Task: Integrate AdaJEPA adaptive loop into surgical phase tracking pipeline
- [ ] MOTIVE: Motion Attribution for Video Generation (NVIDIA SIL, ICML 2026 Oral, research.nvidia.com/labs/sil/projects/MOTIVE/) - Motion-centric data attribution for video generation - Task: Apply motion attribution to understand what training data drives surgical scene generation quality

### Self-Supervised Learning (X Bookmarks, Jul 18-20)
- [ ] Slot-Attention / Object-Centric SSL (Sasha Malysheva, Jul 19) - Mechanistic hypothesis: EMA teachers in DINO/JEPA models drive object-level structure in attention maps - Task: Investigate EMA teacher role in V-JEPA 2 object segmentation emergence for surgical instruments

### Robotics & Robot Policies (WhatsApp + X)
- [ ] RoboTTT: Context Scaling for Robot Policies (NVIDIA, research.nvidia.com/labs/gear/robottt/) - Test-Time Training into robot foundation models; scales visuomotor context to 8K timesteps without growing inference latency - Task: Directly relevant — apply TTT context scaling for long surgical video robot policy adaptation
- [ ] Triflow (derkleineli.github.io/triflow/) - 3D flow-based model/framework - Task: Evaluate for surgical video 3D optical flow estimation
- [ ] SHELLS: Topologically Consistent Multi-view 3D Head Reconstruction (syntec-research.github.io/SHELLS/) - Semantic head estimation via layered local sampling - Task: Study multi-view 3D consistency techniques for endoscopic organ reconstruction

### New Foundation Models & Infrastructure (X Feed, Jul 21)
- [ ] JEPA-DNA (NVIDIA, HuggingPapers) - Genomic foundation model using JEPA pretraining for DNA sequences - Task: Study how JEPA objective extends to DNA sequences — analogous challenge to surgical video domain adaptation
- [ ] Laguna S 2.1 (Poolside, 118B) - New SOTA on SWE-Bench Pro for coding - Task: Evaluate Laguna S for automated surgical training code and SLURM script generation
- [ ] Gemini 3.6 Flash + 3.5 Flash-Lite (Google DeepMind, Jul 20) - Three new models: faster, cheaper, smarter at scale - Task: Benchmark Gemini 3.6 Flash for real-time surgical phase reasoning and report generation
- [ ] OpenEnv (Mervé Noyan) - Agentic training environment making models that see and act; early August launch - Task: Evaluate OpenEnv for training surgical scene understanding agents
- [ ] World Labs Acquires SceniX - SceniX advancing AI robotics simulations - Task: Monitor World Labs simulation platform for surgical training environment generation
- [ ] AlphaEvolve (Google Cloud, cloud.google.com/blog/products/ai-machine-learning/alphaevolve-is-available-for-everyone) - Code optimization and discovery agent built on Gemini - Task: Use AlphaEvolve for auto-optimizing V-JEPA 2 training configs
- [ ] LiteRT.js (Google) - Edge AI runtime for web browsers via WebGPU/WebNN - Task: Deploy lightweight surgical AI inference in browser for clinical demo
- [ ] Morpheus RL Benchmark (morpheus.skyfall.ai/) - RL benchmark for robot policies - Task: Benchmark surgical robot policies on Morpheus evaluation suite

### Nature Papers (WhatsApp Self-Chat, Jul 19-21)
- [ ] Radiologists' Gaze VLM (npj AI, nature.com/articles/s44387-026-00136-9) - Foundational VLM trained on radiologists' gaze and reasoning patterns - Task: Adapt radiologist gaze supervision for surgical endoscopist attention modeling in DINO-Endo
- [ ] Neural Superposition to Sparse Interpretable Codes (Nature Machine Intelligence, s42256-026-01259-z) - Unifying framework for superposition in neural networks - Task: Apply sparse interpretable codes for surgical feature disentanglement in JEPA latents
- [ ] Free Recall Neural Network (Nature Machine Intelligence, s42256-026-01274-0) - RNNs optimized for free recall discover diverse human-like memory strategies - Task: Investigate RNN memory strategies for surgical procedure sequence modeling
- [ ] Physics-Informed ML playlist (YouTube, PLcgrvuVJuClg) - Modeling, Planning, Control, Estimation of Physical Systems - Task: Watch for physics-informed world model techniques applicable to surgical kinematics

### Quantum Papers (WhatsApp Self-Chat)
- [ ] Fully Autonomous Tuning of a Spin Qubit (Nature Electronics, s41928-025-01562-4) - Deep learning + Bayesian optimization + computer vision to tune semiconductor spin qubits - Task: Integrate autonomous tuning approach into SKQD/Syndrome-Net qubit characterization pipeline
- [ ] Digital Quantum Magnetism on Trapped-Ion Quantum Computer (Nature, s41586-026-10445-3) - Demonstrates digital quantum computers for continuous-time dynamics - Task: Study trapped-ion results for hardware comparison with superconducting qubit VQE work
- [ ] NVIDIA Ising Decoding Cuts Color Code Logical Error Rates >300x (developer.nvidia.com) - Quantum error correction decoder - Task: Directly relevant — evaluate NVIDIA Ising decoder against Syndrome-Net QEC approach
- [ ] Error Correction of Logical Qubit in Single Atomic Ion (Nature Physics, s41567-026-03315-2) - Encodes and corrects qubit within multiple internal states of single ion - Task: Study single-ion qubit encoding for multi-logical-qubit VQE circuit design
- [ ] All-Mechanical Coherence Protection of Spin Qubit (Nature Physics, s41567-026-03369-2) - Acoustic waves protect spin coherence in phononic quantum devices - Task: Explore phononic coherence protection for longer-lived VQE qubit states
- [ ] Bloqade SDK (bloqade.quera.com/dev/quick_start/circuits/) - Neutral atom SDK for digital quantum computing - Task: Port SKQD algorithms to Bloqade neutral-atom platform for broader hardware benchmarking

### NVIDIA Hackathon / Your Projects (WhatsApp Robotics Vision Group, Jul 21)
- [ ] NV-Disruptron (github.com/Ryukijano/NV-Disruptron) - Your NVIDIA hackathon project: AV/infra/robotics vision stack with lane detection, scene understanding, control - Task: Port NV-Disruptron robotics vision modules to surgical scene understanding pipeline
- [ ] NVIDIA Open Models Codefest (events.nvidia.com/open-models-codefest) - Broader NVIDIA hackathon using pretrained models for robotics vision - Task: Submit surgical video world model demo to NVIDIA Open Models Codefestassistancereconstruction

## X Bookmarks, Feed & WhatsApp - New AI Papers & Links (July 21-24, 2026)

### Model Merging & Representation Theory (X Bookmarks, Jul 21-24)
- [ ] Task Arithmetic / Task Vectors (Sasha Malysheva, Jul 24 - arXiv 2212.04089, Ilharco et al.) - Fine-tuning deltas behave like actual vectors: add, subtract, combine task vectors on pretrained weights. Task: Apply task arithmetic to surgical domain adaptation — add a 'surgical phase' delta to V-JEPA 2 base without retraining from scratch
- [ ] Git Re-Basin (Sasha Malysheva, Jul 21 - arXiv 2209.04836, Ainsworth et al.) - ResNet50 has 10^55109 ways to relabel neurons yet compute same function. Enables averaging model weights across permutation symmetries. Task: Apply Git Re-Basin for merging surgical-domain V-JEPA 2 checkpoints from different training runs
- [ ] Relative Representations (Moschella et al., ICLR 2023 - arXiv 2209.15430) - Describes data points via similarity to fixed anchors, enabling zero-shot model stitching across architectures. Task: Use for cross-modal surgical representation alignment (endoscopy encoder ↔ RGB encoder)
- [ ] Convergent Evolution Theory (Daniel Yamins, danyamins.substack.com) - Mathematical theory on AI and brain convergence; zippering theorems. Task: Read for theoretical grounding of why JEPA-style representations align with neural representations for surgical perception

### Video & World Models (X Bookmarks, Jul 21-24)
- [ ] CW-VAE / Clockwork Variational Autoencoder (Saxena et al., NeurIPS 2021 - arXiv 2102.09532) - Hierarchical latent sequence model with temporal abstraction at multiple time scales. Task: Apply for surgical video temporal hierarchy modeling — slow phases vs fast instrument motion
- [ ] Mechanistic World Models (Posner et al., Jul 24 - arXiv 2607.12474) - Framework for uncovering mechanisms from observations. Task: Apply mechanistic interpretation to surgical world model latents
- [ ] UniVR / Unified Visual Reasoning (ByteDance & BJTU, arXiv 2607.128) - Framework for unified visual reasoning; +25% on VR-X benchmark. Task: Benchmark UniVR for surgical instrument state reasoning from video
- [ ] GigaWorld-Policy-0.5 (huggingface.co/papers/2607.13960) - Video world model policy. Task: Study for robot policy learning from surgical video
- [ ] FLUX-mimic / 1T1X-mimic (mimicrobotics, Jul 23) - Next-gen Video-Action Model (VAM) for general-purpose dexterity, developed with BFL AI. Task: Study FLUX-mimic video-action architecture for surgical instrument manipulation learning from demonstrations

### Robotics & Foundation Models (X Bookmarks, Jul 21-24)
- [ ] Xiaomi-Robotics-1 (DailyPapers, Jul 20) - Scalable VLA foundation model pretrained on 100,000+ hours of real-world manipulation trajectories. Task: Benchmark Xiaomi-Robotics-1 as pretrained backbone for surgical robot manipulation
- [ ] NV-JEPA-DNA / JEPA-DNA-DNABERT2 (NVIDIA, Jul 21 - huggingface.co/nvidia/NV-JEPA-DNA-DNABERT2) - Genomic foundation model using JEPA pretraining beyond masked LM to learn functional DNA meaning. Task: Study JEPA pretraining objective applied to sequence data (DNA) as analog for adapting JEPA to surgical procedure sequences

### Mathematical Foundations (X Bookmarks, Jul 21-24)
- [ ] Optimal Transport / Helmholtz Decomposition (Peyman Milanfar, Jul 22) - Polar matrix factorization and Helmholtz decomposition all implied by Brenier's theorem — cornerstone of Optimal Transport theory. Task: Study OT for latent space regularization in surgical world models and for aligning multi-modal surgical distributions
- [ ] Planar Homographies Visualization (@CSProfKGD - csprofkgd.github.io/planar-homogra) - Task: Reference for geometric transformation understanding in surgical camera calibration and multi-view reconstruction

### 3D & Vision Tools (X Feed, Jul 24)
- [ ] Google GMN - Parametric Differentiable 3D Head Model (Jul 24, HuggingFace Spaces: hf.co/spaces/hugging) - Runs on CPU; parametric differentiable 3D model. Task: Study parametric 3D modeling for surgical anatomy reconstruction and organ surface modeling

### X Feed Updates (Jul 24)
- [ ] Jensen Huang First X Post - Open weights and American AI leadership letter: 'AI will transform every industry, power every company, and be built by every country.' Task: Track NVIDIA open model strategy and open weight releases for surgical AI deployment
- [ ] Google Gemini 3.6 Flash + 3.5 Flash-Lite (Jul 24) - New faster Gemini models launched. Task: Evaluate for real-time surgical report generation and on-device inference
- [ ] Unitree AS2-W Wheeled Quadruped (Jul 24) - New wheeled quadruped for rough terrain; demonstrates Unitree hardware-software co-design. Task: Monitor locomotion control algorithms applicable to surgical robot base mobility
- [ ] Nature Machine Intelligence: Unifying Framework (s42256-026-01259-z) - New unifying framework paper. Task: Read for unifying perspective on world models relevant to surgical AI

### WhatsApp Self-Chat Additional Links (Jul 21-24)
- [ ] Nature Machine Intelligence: Memory Strategies / Free Recall (s42256-026-01274-0) - RNNs optimized for free recall discover diverse human-like memory strategies. Task: Investigate RNN memory strategies for surgical procedure sequence modeling
- [ ] Nature Machine Intelligence: Cognitive Maps / Generative Models (s42256-026-01254-4) - Neural sampling from cognitive map enables planning and goal-directed imagination. Task: Apply cognitive map + neural sampling for surgical phase planning and future state imagination
- [ ] The Decoder: Google DeepMind Video Generators as World Models (the-decoder.com) - Google DeepMind argues video generators already contain the world models computer vision has been missing. Task: Integrate insights into V-JEPA 2 / COSMOS surgical world model architecture decisions
- [ ] NVIDIA Cosmos3-Edge (huggingface.co/nvidia/Cosmos3-Edge) - Edge-optimized COSMOS model. Task: Deploy Cosmos3-Edge for on-device surgical video prediction at inference time
- [ ] Nature: AI-Redesigned Protein Evolution (s41586-026-10820-0) - AI workflow redesigning starting points to evolve proteins. Task: Study AI-guided protein evolution methodology for AI-guided surgical procedure optimization
- [ ] Communications Chemistry: Neuromorphic Chip Screening (s42004-026-02122-3) - 19 billion compounds screened for drug discovery using neuromorphic chip. Task: Study neuromorphic hardware acceleration for surgical scene inference
- [ ] Physics-Informed ML playlist (YouTube, PLcgrvuVJuClg, from Gyanateet Jio) - Modeling, Planning, Control, Estimation of Physical Systems. Task: Watch for physics-informed world model techniques applicable to surgical 

## X Bookmarks, Feed & WhatsApp - New AI Papers & Links (July 29 - August 2, 2026)

### Video & World Models (X Bookmarks, Jul 29 - Aug 2)
- [ ] Wonder: Video World Model Done Better (alphaXiv/Adobe Research, Jul 31 - arXiv 2607.26603) - Fixes drifting controls, fading memories, and latency in world models via co-designed camera control. Task: Apply Wonder's drift-fix techniques to V-JEPA 2 surgical video world model latent rollouts
- [ ] Explorative: Third Pretraining Axis (Alexi Gladstone @AlexiGlad, Jul 31) - Exploration as third pretraining axis beyond parameters and data; improves image/video/language generation. Task: Incorporate exploration-based pretraining into surgical video world model training pipeline
- [ ] Open Dreamer / Frontier-Level World Model (next-state.github.io/open-dreamer, Jul 25) - Full open-source recipe for training a frontier-level world model with live playable demo. Task: Study training methodology and open-source recipe for building surgical world model
- [ ] Dream Cubed / Dreaming in Voxels (hardmaru/Sakana AI, pub.sakana.ai/dream-cubed, Jul 29) - Generative AI for playable interactive 3D Minecraft worlds trained on billions of cubes. Task: Study 3D generative world model approach for surgical scene volumetric prediction
- [ ] NVIDIA Cosmos-H-Dreams: Real-Time Generative Simulation for Surgical Robotics (huggingface.co/blog/nvidia/cosmos-h-dreams, Jul 26) - Real-time generative simulation pipeline for surgical robotics using COSMOS. Task: Deploy Cosmos-H-Dreams for surgical trajectory simulation and data augmentation
- [ ] NVIDIA-NeMo Labs-MOLT (github.com/NVIDIA-NeMo/labs-molt, Jul 26) - NeMo multi-modal language-trajectory model. Task: Study MOLT architecture for surgical report + trajectory joint modeling
- [ ] arXiv 2602.24281 (Jul 26) - Task: Read and catalog paper for V-JEPA/world model context

### Agentic AI & Reasoning (X Bookmarks, Jul 29 - Aug 2)
- [ ] Beacon: Knowing When and How to Use Tools (HuggingPapers, Aug 1) - Mode Adaptiveness + Tool Effect framework preventing indiscriminate tool use in agentic visual reasoning. Task: Apply Beacon's selective tool-use framework to surgical AI agent for instrument segmentation decisions
- [ ] Relay-OPD: On-Policy Distillation for Reasoning (HuggingPapers, Jul 29) - Novel on-policy distillation framework fixing prefix failure in LLM reasoning by letting teachers take over at failure points. Task: Apply Relay-OPD to improve surgical phase reasoning chain robustness
- [ ] Kimi K3 Preserved Thinking History (Niels Rogge @NielsRogge, Jul 30) - Multi-turn conversations with Kimi K3 require passing back complete assistant message with preserved thinking history. Task: Implement preserved-thinking multi-turn for surgical AI diagnostic reasoning chains

### Language Models & Architectures (X Bookmarks, Jul 29 - Aug 2)
- [ ] LeRoPE: Learnable RoPE Frequencies (alphaXiv, Jul 29) - Learns rather than hand-picks RoPE frequencies; improves language modeling across scales with only 32 extra parameters. Task: Apply learnable positional encoding to surgical phase sequence modeling
- [ ] Ensembles in RL Production Systems (Sasha Malysheva @aimalysheva, Aug 1) - Real-world RL systems rely on ensembles for reliability despite trend toward single clean models. Task: Implement ensemble surgical policy for uncertainty estimation in autonomous instrument control
- [ ] ML Researcher Impact Theory (Horace He @cHHillee, Jul 29) - Impact proportional to infrastructure pain caused. Task: Calibrate research/engineering effort balance for surgical AI deployment
- [ ] DeepSeek Kill Zone Analysis (Jen Zhu @jenzhuscott, Aug 1) - AI models inferior and significantly more expensive vs. DeepSeek should enter survival mode. Task: Track competitive landscape for surgical AI foundation model strategy

### Quantum & Photonics (WhatsApp, Jul 24-26)
- [ ] Long-lived Ytterbium States for Quantum Computing (phys.org, Jul 26) - Long-lived Yb states sharpen quantum computing and atomic clock precision. Task: Monitor ytterbium-based qubit advances for quantum error correction implementation
- [ ] Beyond Quantum Linear Optics: Adaptive Boson Sampling (Nature Photonics, s41566-026-01959-3, Jul 25) - Adaptive boson sampling beyond quantum linear optics. Task: Study adaptive quantum photonics for quantum-ML interface
- [ ] Breaking the Power Wall in Programmable Photonics (Nature Photonics, s41566-026-01960-w, Jul 26) - Photonic computing power wall breakthrough. Task: Track photonic hardware for ultra-efficient surgical AI inference
- [ ] Enhanced Inverse Compton Scattering via Coated Plasma Mirror (Nature Photonics, s41566-026-01958-4, Jul 25) - Novel gamma-ray source generation technique. Task: Background reading for photon-based sensing in surgical imaging

### Nanotechnology & Chemistry (WhatsApp, Jul 24-26)
- [ ] Upconverting Nanoparticles for Angstrom-Precision Super-Resolution (Nature Nanotechnology, s41565-026-02233-x, Jul 26) - Spontaneous and indefinite blinking in upconverting nanoparticles enables multi-colour super-resolution at angstrom precision. Task: Monitor for next-gen surgical tissue imaging at nanoscale
- [ ] Alkyl-Sulfur Compounds via N2 Extrusion (Nature Chemistry, s41557-026-02212-8, Jul 24) - Chemoselective access to alkyl-sulfur compounds. Task: Background for AI-guided organic synthesis and surgical biomaterial design
- [ ] Oligonucleotide Functionalization via On-Support Phosphitylation (Nature Chemistry, s41557-026-02214-6, Jul 25) - Versatile strategy for oligonucleotide functionalization. Task: Study for AI-guided nucleotide drug delivery in surgical oncology
- [ ] Enhancer Bursting Dynamics (Nature Genetics, s41588-026-02693-w, Jul 25) - Genomic position of enhancer modulates bursting dynamics of cognate promoter. Task: Background for AI-guided gene regulation modeling

### Hardware & Kernel Engineering (WhatsApp, Jul 25 / X Bookmarks)
- [ ] tensormux/kernel-skills (github.com/tensormux/kernel-skills, Jul 25) - Open-source skill library for AI coding agents to write, optimize, and debug high-performance compute kernels across CUDA, Triton, and quantized workloads. Task: Use kernel-skills for optimizing DINO-Endo and V-JEPA 2 CUDA inference kernelskinematic modeling
