# notebooklm-research-workflow

## Description
Organize and sync research papers, arXiv links, GitHub repos, and web resources from X (Twitter) bookmarks and WhatsApp conversations into Google NotebookLM notebooks by topic domain. Supports quantum computing, computer vision, world models, robotics, and ML research workflows.

## Key Sources (July 2026)

### Quantum Computing & Error Correction
- arXiv:2605.01138 - Crossing 12,000-atom barrier with heterogeneous quantum-classical supercomputing
- arXiv:2605.04604 - Generative Quantum-inspired Kolmogorov-Arnold Eigensolver
- arXiv:2604.08358 - Scalable Neural Decoders for Practical Fault-Tolerant QC
- arXiv:2603.15381v1 - Why AI systems don't learn and what to do about it
- arXiv:2601.16169v1 - Scaling Sample-Based Quantum Diagonalization on GPU (OpenMP)
- Nature s41586-026-10628-y - Improved quantum processor logical error rates
- Nature s41567-026-03353-w - Exchange-mediated spin-electric control of single molecules
- Nature s42254-025-00914-5 - Simulating fermions with a digital quantum computer
- PRX Quantum: partially fault-tolerant molecular energy computation (trapped-ion)
- IBM Qiskit Paulice blog post
- Microsoft + Quantinuum: major gains in quantum error correction (The Quantum Insider)
- SUTD Quantum Computing Research Positions: https://fanerst.github.io/positions/quantum-computing-recruitment/
- Zlatko Minev ML-QEM talks: https://github.com/zlatko-minev/zlatko-minev-quantum-repository

### World Models & V-JEPA
- AdaJEPA (Adaptive Latent World Model): https://agenticlearning.ai/adajepa/
- DeltaWorld / A Frame is Worth One Token: arXiv:2604.04913, https://deltatok.github.io
- SLS-WM (Structured Label Smoothing for Joint-Embedding Discrete World Models): https://github.com/Tariolle/sls-wm
- HWM (Hierarchical World Model): https://kevinghst.github.io/HWM/
- World-Tracing: https://haoz19.github.io/world-tracing-page/
- mu0 world model: https://mu0-wm.github.io/
- Facebook JEPA: https://github.com/facebookresearch/jepa
- DeepMind Decoupled DiLoCo: https://deepmind.google/blog/decoupled-diloco/
- World model for factory (Reddit ML news)

### 3D Vision, Gaussian Splatting & Reconstruction
- GS-SDF (LiDAR-Augmented Gaussian Splatting): https://github.com/hku-mars/GS-SDF
- SuperFlex (SuperQuadrics @ ECCV 2026): https://superflex3d.github.io
- FoundObj (ICML 2026, 3D scene segmentation): arXiv:2605.27178
- ST-FLIP (SIGGRAPH 2026, particle space-time): https://ge.in.tum.de/download/ST-FLIP
- AeroTransformer (aerodynamic foundation model): arXiv:2604.18062, https://github.com/tum-pbs/AeroTr
- RayRoPE (multi-view transformers): https://rayrope.github.io
- COLIPRI (3D vision-language encoder, MSFTResearch): https://aka.ms/colipri
- IronSight (4D reconstruction from Meta Ray-Bans)
- Boosting 3D Foundation Models with Edge-based Pose Optimization
- MotionBricks (NVIDIA NVLabs): https://nvlabs.github.io/motionbricks/
- Gaussian Splatting + LiDAR Field Guide: https://lidarnews.com/gaussian-splatting-and-lidar-a-practitioners-field-guide/
- SLAM Handbook (PDF): https://github.com/SLAM-Handbook-contributors
- LeJEPA Identifiability: https://klindtlab.github.io/lejepa-identifiability/
- Swift Sampling (temporal sampling): https://kim-dahye.github.io/swift-sampling/
- Stationary TPAMI: https://niccobiondi.github.io/projects/stationary-tpami/

### Robotics & Physical AI
- NVIDIA ArtiFixer (SIGGRAPH 2026, geometry fill-in): https://nvda.ws/4oILqNd
- NVIDIA HALOS (full-stack functional safety for robotics): NVIDIA Developer Blog
- NVIDIA Isaac Sim (building robots tutorial): NVIDIA Learning Docs
- NVIDIA NCore (data platform for physical AI)
- ETH Zurich Robot Learning Lectures: https://cvg.ethz.ch/lectures/Robot-Learning/
- Open-H (open healthcare robotics embodiment): https://github.com/open-h/open-h-embodiment
- Sim-to-real robot policy boosting using cheap simulation (Ilir Aliu, ICML)
- World Action Models (NVIDIA Blog): https://developer.nvidia.com/blog/pretrained-to-imagine-fine-tuned-to-act

### ML Research & LLMs
- Energy Matching (NeurIPS 2025): arXiv:2504.10612, https://github.com/m1balcerak/Energy-Matching
- Contrastive Flow Matching (5x fewer diffusion steps)
- ThinkMorph (thinking in modalities): arXiv:2510.27492
- Spherical Equivariant Graph Transformers: arXiv:2512.13927
- Natural Language Autoencoders (Anthropic): https://www.anthropic.com/research/natural-language-autoencoders
- ACE: Agentic Context Engineering (Stanford) - replaces fine-tuning with context
- Multi-Head Latent Attention: https://github.com/rasbt/LLMs-from-scratch
- Flash Linear Attention: https://github.com/fla-org/flash-linear-attention
- DARLING (Diversity Aware RL): arXiv:2509.02534
- StepWiser: arXiv:2508.19229
- Open-YOLO 3D (ICLR 2025 Oral): https://github.com/aminebdj/OpenYOLO3D
- Video-MME-Logical: https://mrakas.github.io/video-mme-logi
- DAIR.AI Top AI Papers (June 28 - July 5, 2026): RLMF, AutoMem, Red Queen Godel Machine, Generative Skill Composition
- LLM-JEPA (JEPA-style training for LLMs)
- Vision Banana (Google DeepMind): https://vision-banana.github.io/
- Goodfire: The World Inside Neural Networks: https://www.goodfire.ai/research/the-world-inside-neural-networks
- WarpSpeed (DoubleAI, Blackwell speed-of-light): https://www.doubleai.com/research/warpspeed-approaches-speed-of-light-on-blackwell

### AI for Science
- Google ERA (Empirical Research Assistance): https://research.google/blog/empirical-research-assistance-era
- Optimizing AI for surgery (npj Digital Medicine): Nature s41746-026-02763-7
- SpecGP (glycopeptide analysis transformer, Nature Machine Intelligence): Nature s42256-026-01246-4
- Uncovering local integrability in quantum many-body dynamics: Nature s41467-025-57623-x
- Protenix (ByteDance protein folding): https://github.com/bytedance/Protenix
- CERN record: https://cds.cern.ch/record/2939204
- CuspAI KUPS (molecular simulation engine): https://medium.com/@CuspAI/kups
- PCOS Edge Agent: https://github.com/Ryukijano/pcos-edge-agent

### Agent & Tool Skills
- NVIDIA Kaggle Agent Skills: https://github.com/NVIDIA/nvidia-kaggle
- Groq Agentic Research Assistant (LangGraph): https://github.com/Marktechpost/AI-Agents-Projects-Tutorials
- gitmcp.io (MCP for GitHub): https://gitmcp.io
- Parlance Labs: https://github.com/parlance-labs/
- Science-T2I: https://jialuo-li.github.io/Science-T2I-We
- NVIDIA GPU process viewer (nvitop): https://github.com/XuehaiPan/nvitop

## NotebookLM Notebook Mapping

| Research Area | Notebook Name |
|---|---|
| Quantum error correction, fault-tolerant QC, QEM | `Quantum_error_correction` |
| World models, V-JEPA, AdaJEPA, JEPA variants | `V-JEPA: Next Steps in Human-like AI Learning2` |
| 3D reconstruction, Gaussian splatting, SLAM, ECCV/SIGGRAPH | `CVPR 2026 Conference Schedule and Paper Directory` |
| Robotics, RL, physical AI, sim-to-real | `RL, Robotics, Planning & Interpretability` |
| Diffusion, flow matching, energy matching, generative models | `Flow Matching: Generative Modeling via Continuous Normalizing Flows` |
| AI for science, computational physics, ERA, molecular sim | `AI-Native Scientific Discovery & Computational Physics` |
| Quantum many-body, quantum chemistry, quantum ML | `Quantum Information Theory` |
| Medical AI, surgical video, endoscopy | `V-JEPA: Next Steps in Human-like AI Learning2` |

## Workflow

1. Collect bookmarks from X (Twitter) - scroll through all bookmarks extracting arxiv links, GitHub repos, project pages
2. Check WhatsApp conversations: `Gyanateet Jio` and `(You)` saved messages for shared research links
3. Categorize links by research domain
4. Open corresponding NotebookLM notebook
5. Click `Add sources` → `Websites` → paste batch of up to 10 URLs
6. Repeat for each notebook
7. Update this SKILL.md with new sources found

## Tags
notebooklm, research-organization, literature-review, arxiv, quantum-computing, world-models, 3d-vision, robotics, ml-research
