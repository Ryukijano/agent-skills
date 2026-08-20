# agent-skills

Reusable **Devin** and **Cursor** skills and workflows for cross-project AI-assisted development.
Designed for research scientists and software engineers working on ML projects (surgical video MOT, HPC, DGX Spark, 3D recon, agentic loops) and **PCOS edge agent** development.

## Overview

| Platform | Skills | Workflows / Commands |
|----------|--------|----------------------|
| **Devin** (`.devin/`) | 800 | 786 workflows (`/name`) |
| **Cursor** (`.cursor/`) | 813 | 796 commands (`/name`) |
| **MCP Servers** (`mcp_servers/`) | 7 servers | 72 tools (dual CLI + MCP) |
| **Hugging Face Skills** | 12 | Hub, datasets, training, eval, papers, Gradio |
| **NVIDIA Skills** | 22 | NeMo, Megatron-Core, DALI, CUDA-Q, DeepStream |

- Every major topic has both a **skill** and a **workflow/command**.
- **MCP servers** provide live tools that agents call at runtime — GPU monitoring, CUDA profiling, distributed training, cloud GPU SSH, TPU/JAX, endosight pipeline, and research workflows.
- **Hugging Face skills** (installed via `npx skills add huggingface/skills`) give agents access to the HF Hub: model search, dataset exploration, LLM/vision training, evaluation, paper lookup, and Gradio demos.
- **NVIDIA skills** (installed via `npx skills add nvidia/skills`) provide NeMo distributed training, Megatron-Core, DALI, CUDA-Q, and DeepStream expertise.

Every major topic has both a **skill** (reference knowledge, auto-suggested) and a **workflow/command** (step-by-step procedure).

Skills use **progressive disclosure**: only `name` and `description` are loaded until the agent invokes them, keeping context lean.

## Skills (800)

### Research Scientist (13)

| Skill | Description |
|-------|-------------|
| `reproducibility` | Seeds, config logging, environment capture, deterministic training |
| `reproducibility-checklist` | Audit project for reproducibility gaps before submission |
| `experiment-tracking` | Structured logging, hyperparameter management, result comparison |
| `data-management` | Dataset versioning, hashing, leak-free partitioning |
| `paper-code-release` | Prepare code for public release alongside paper |
| `paper-submission-prep` | Finalize repo for conference submission deadline |
| `ablation-study` | Design systematic ablation studies comparing model variants |
| `tdv-pretrain` | TDV (Temporal Difference in Vision) pretraining on surgical video |
| `surgical-mot-eval` | Evaluate surgical MOT models on CholecTrack20 |
| `lora-finetune` | LoRA fine-tuning for vision transformers (DINOv2, ViT) |
| `pretrain-and-evaluate` | Full Stage 0 pretrain → Stage 1 detect → eval pipeline |
| `continual-learning` | Cross-session context persistence with progress files |
| `deep-research` | Systematic web research and deep reasoning for complex technical questions |

### Software Engineering (10)

| Skill | Description |
|-------|-------------|
| `code-quality` | Formatting, linting, type checking with ruff + basedpyright |
| `code-review` | ML-focused code review checklist (correctness, perf, safety) |
| `testing-strategy` | Unit, integration, smoke, and property-based tests for ML code |
| `dependency-management` | Lock files, pyproject.toml, version conflicts, uv migration |
| `ci-cd-setup` | GitHub Actions workflows for automated testing and linting |
| `pre-commit-setup` | Pre-commit hooks with ruff and common checks |
| `release-checklist` | Versioned releases, changelogs, PyPI publishing |
| `refactor-extract-module` | Safely extract code into separate modules |
| `git-branch-workflow` | Branch naming, commit conventions, PR templates |
| `address-pr-comments` | Systematically address PR review comments via GitHub CLI |

### Infrastructure & Debugging (11)

| Skill | Description |
|-------|-------------|
| `aire-slurm-submit` | Submit and monitor Slurm jobs on AIRE HPC cluster |
| `submit-gpu-job` | Submit GPU training job with smoke test + monitoring |
| `conda-env-setup` | Create conda environments with CUDA PyTorch on AIRE |
| `debug-pytorch-gpu` | Diagnose OOM, DDP hangs, NCCL errors, gradient instability |
| `debug-training` | Debug NaN loss, OOM, DDP hangs, poor convergence by symptom |
| `checkpoint-to-deployment` | Convert training checkpoint to deployment-ready format |
| `setup-ml-project` | Scaffold new ML research project with standard structure |
| `wandb-experiment` | Weights & Biases experiment tracking setup and debugging |
| `mot-training-workflow` | Surgical MOT 4-stage pipeline training workflow |
| `mot-repo-orientation` | Navigate the GOT-JEPA surgical MOT codebase structure |
| `mot-browser-research` | Research SOTA MOT methods via web search and paper discovery |

### Science & Bioinformatics (34)

| Skill | Description |
|-------|-------------|
| `alphafold-database-fetch-and-analyze` | Retrieve and analyze AlphaFold predicted structures |
| `alphagenome-single-variant-analysis` | Analyze genetic variant effects on gene expression |
| `chembl-database` | Query ChEMBL for bioactive molecules and drug targets |
| `clinical-trials-database` | Search ClinicalTrials.gov for clinical trials |
| `clinvar-database` | Clinical significance and pathogenicity classifications |
| `dbsnp-database` | Look up and map short genetic variants (SNPs) |
| `embl-ebi-ols` | Query EMBL-EBI Ontology Lookup Service |
| `encode-ccres-database` | Query ENCODE Registry of cis-Regulatory Elements |
| `ensembl-database` | Resolve gene, transcript, and protein IDs via Ensembl |
| `foldseek-structural-search` | 3D structural search of proteins |
| `gnomad-database` | Query Genome Aggregation Database for allele frequencies |
| `gtex-database` | Retrieve RNA expression data and variant associations |
| `human-protein-atlas-database` | Retrieve protein expression and localization data |
| `interpro-database` | Identify protein domains, families, and sites |
| `jaspar-database` | Query JASPAR for transcription factor binding profiles |
| `literature-search-arxiv` | Search arXiv for scientific preprints |
| `literature-search-biorxiv` | Browse and download bioRxiv preprints |
| `literature-search-europepmc` | Search Europe PMC for scientific literature |
| `literature-search-openalex` | Query OpenAlex scholarly database |
| `ncbi-sequence-fetch` | Retrieve protein and nucleotide sequences from NCBI |
| `openfda-database` | Query openFDA API for drugs, devices, and food |
| `opentargets-database` | Query Open Targets for target-disease associations |
| `pdb-database` | Search and download experimentally-determined 3D structures |
| `protein-sequence-msa` | Multiple sequence alignment with Clustal Omega |
| `protein-sequence-similarity-search` | Search for homologous proteins with MMseqs2/BLAST |
| `pubchem-database` | Query PubChem for compounds, properties, and assays |
| `pubmed-database` | Search PubMed for scientific literature |
| `pymol` | Visualize and render protein structures with PyMOL |
| `quickgo-database` | Query QuickGO for Gene Ontology terms and mappings |
| `reactome-database` | Query Reactome for pathway analysis and enrichment |
| `string-database` | Query STRING for protein-protein interactions |
| `ucsc-conservation-and-tfbs` | Fetch conservation scores and TF binding sites from UCSC |
| `unibind-database` | Query UniBind for experimentally validated TF binding sites |
| `uniprot-database` | Access protein metadata, sequences, and annotations |

### Documents & Creative (6)

| Skill | Description |
|-------|-------------|
| `pdf` | Read, extract, merge, split, create, and OCR PDF files |
| `docx` | Create, edit, and analyze Word documents with tracked changes |
| `xlsx` | Create Excel spreadsheets with formulas, financial models, data analysis |
| `pptx` | Create presentations and slide decks with design QA |
| `canvas-design` | Design visual art in PNG and PDF formats |
| `algorithmic-art` | Create generative art using p5.js with seeded randomness |

### PCOS Edge Agent (6)

| Skill | Description |
|-------|-------------|
| `pcos-routing` | PCOS context routing decision tree, surface selection, Chrome API selection |
| `pcos-chrome-ai` | Chrome Built-in AI API integration (Prompt, Summarizer, Translator, etc.) |
| `pcos-android-litert` | Android on-device inference with LiteRT-LM v0.13+ and Gemma models |
| `pcos-bridge` | Chrome ↔ Android WebSocket bridge via broker relay hub |
| `pcos-privacy` | PII stripping, cloud escalation gating, privacy-first routing policies |
| `pcos-deploy` | PCOS deployment, CI/CD, observability, HF Space, MkDocs docs site |

### Development & Tooling (10)

| Skill | Description |
|-------|-------------|
| `webapp-testing` | Test local web apps with Playwright (screenshots, logs, UI automation) |
| `mcp-builder` | Build MCP servers to expose tools and APIs to AI agents |
| `frontend-design` | Frontend UI/UX design with modern CSS and accessibility |
| `git-advanced-workflows` | Interactive rebase, cherry-pick, bisect, reflog, worktrees, conflict resolution |
| `tdd-workflow` | Red-Green-Refactor TDD cycle with best practices |
| `pair-programming` | Structured AI pair programming with driver-navigator pattern |
| `security-audit` | OWASP Top 10 checklist, vulnerability scanning, access control audit |
| `data-visualization` | Charts and plots with matplotlib, seaborn, plotly |
| `docker-containerization` | Dockerfiles, multi-stage builds, docker-compose |
| `api-design` | REST API design with FastAPI, best practices, OpenAPI docs |

### Engineering Practice (8)

| Skill | Description |
|-------|-------------|
| `spec-driven-development` | Spec → plan → tasks → implement gated workflow |
| `context-engineering` | Manage AI agent context: rules, specs, source, errors |
| `incremental-implementation` | Small verifiable increments, compilable, rollback-friendly |
| `debugging-and-error-recovery` | Systematic debugging: reproduce, localize, fix root cause |
| `code-simplification` | Simplify code preserving behavior, clarity over cleverness |
| `performance-optimization` | Profile → identify bottlenecks → optimize → measure |
| `observability-and-instrumentation` | Logging, metrics, tracing, health checks |
| `planning-and-task-breakdown` | Break complex tasks into small verifiable subtasks |

### AI/ML Research & Training (13)

| Skill | Description |
|-------|-------------|
| `autoresearch` | Two-loop autonomous research orchestration |
| `ml-paper-writing` | Publication-ready papers for NeurIPS, ICML, ICLR with LaTeX |
| `academic-plotting` | Publication-quality figures with venue-specific styling |
| `research-brainstorming` | Structured ideation for high-impact research directions |
| `vllm-serving` | High-throughput LLM serving with PagedAttention |
| `flash-attention` | 2-4x faster attention with O(N) memory |
| `peft-finetuning` | LoRA, QLoRA, DoRA — adapt LLMs with minimal params |
| `deepspeed-training` | ZeRO optimization for distributed training of large models |
| `model-quantization` | 8-bit/4-bit quantization with bitsandbytes, GPTQ, AWQ, GGUF |
| `knowledge-distillation` | Compress large models into smaller ones via distillation |
| `speculative-decoding` | 1.5-3.6x faster LLM inference with draft models |
| `rag-pipelines` | RAG with vector databases, embeddings, and LLMs |
| `model-merging` | Combine models with TIES, DARE, SLERP using mergekit |

### AlphaEvolve & Evolutionary Optimization (7)

| Skill | Description |
|-------|-------------|
| `alphaevolve-orchestrator` | Full 4-phase AlphaEvolve workflow: design → run → monitor → post-experiment |
| `alphaevolve-experiment-design` | Design experiments: seed program, EVOLVE-BLOCK markers, evaluator, project structure |
| `alphaevolve-runner` | Launch experiments on GCP: configure, verify evaluator, create & start evolution loop |
| `alphaevolve-monitor` | Monitor running experiments: progress tracking, metrics, failure analysis, reports |
| `alphaevolve-post-experiment` | Post-experiment: code review, score progression charts, integrate evolved code |
| `alphaevolve-consultant` | Expert reference: architecture, suitability, evaluator design, troubleshooting |
| `evolutionary-code-optimization` | General LLM-based evolutionary code optimization (with or without AlphaEvolve) |

### MCP Servers (7 servers, 90 tools)

Custom MCP (Model Context Protocol) servers with dual CLI + MCP interface. Each server works as a direct terminal tool AND as an MCP tool for AI agents (Cursor, Devin, Claude, Windsurf, Gemini).

| Server | Tools | Description |
|--------|-------|-------------|
| `dgx-monitor` | 15 | GPU status (GB10 unified memory fallback), processes, Docker, conda, CUDA info, kernel compilation, NVDEC/NVENC, bandwidth tests |
| `cuda-profiling` | 13 | nsys/ncu profiling, compute-sanitizer (memcheck/racecheck/initcheck), SASS/PTX dump, benchmarking, GPU info, kernel compilation |
| `distributed-training` | 12 | Multi-GPU discovery, NVLink/PCIe topology, NCCL diagnostics, DDP/FSDP setup, training job management, checkpoints |
| `cloud-gpu-ssh` | 16 | Remote GPU machines (Lambda/RunPod/Vast/SSH), remote commands, SFTP file sync, GPU pricing |
| `tpu-jax` | 10 | JAX device discovery, TPU topology, gcloud TPU VM management, JAX profiling, XLA HLO compilation |
| `endosight-pipeline` | 13 | Pipeline status, clip listing, reconstruction stats, crop/QA/export, logs, validation, clinical clip sweep |
| `research-workflow` | 11 | ArXiv search, paper download, BibTeX management, repro bundles, experiment tracking, Semantic Scholar, citations |

**Install all servers:**
```bash
bash mcp_servers/install_all.sh
```

**Test in CLI mode:**
```bash
python3 mcp_servers/dgx_monitor/server.py --cli gpu_status
python3 mcp_servers/distributed_training/server.py --cli list_gpus
python3 mcp_servers/cloud_gpu_ssh/server.py --cli list_machines
```

**Also installed:** 22 NVIDIA agent skills (NeMo, Megatron-Core, DALI, CUDA-Q, DeepStream) via `npx skills add nvidia/skills`, plus community MCPs (W&B, MLflow, NVIDIA CUDA docs, Hugging Face).

See `mcp_servers/README.md` for full documentation.

### Hugging Face Skills (12)

Installed from `huggingface/skills` via `npx skills add huggingface/skills`. These skills teach agents how to use the Hugging Face Hub ecosystem.

| Skill | Description |
|-------|-------------|
| `hf-cli` | Hub CLI: download, upload, manage models/datasets/spaces/buckets/repos/papers/jobs |
| `huggingface-datasets` | Dataset Viewer API: paginate rows, search text, apply filters, download parquet |
| `huggingface-llm-trainer` | Train/fine-tune LLMs with TRL (SFT, DPO, GRPO) on HF Jobs |
| `huggingface-vision-trainer` | Train object detection (D-FINE, RT-DETR, DETR, YOLOS) and image classification |
| `huggingface-community-evals` | Run evaluations against Hub models on local hardware |
| `huggingface-trackio` | Track and visualize ML training experiments with Trackio |
| `huggingface-papers` | Look up and read Hugging Face paper pages in markdown |
| `huggingface-paper-publisher` | Publish and manage research papers on the Hub |
| `huggingface-tool-builder` | Build reusable scripts for HF API operations |
| `huggingface-gradio` | Build Gradio web UIs and demos in Python |
| `transformers-js` | Run ML models in JavaScript/TypeScript with WebGPU/WASM |
| `huggingface-best` | Find the best/recommended model for a task by benchmark scores |

**Install:**
```bash
npx skills add huggingface/skills --skill hf-cli --agent cursor --yes
npx skills add huggingface/skills --skill huggingface-llm-trainer --agent cursor --yes
# ... or install all 12 (see above)
```

**Hugging Face MCP Server** (hosted at `https://huggingface.co/mcp`):
- Search models, datasets, Spaces, and papers
- Run community tools via Gradio apps on Spaces
- Schedule and run Jobs on HF infrastructure
- Requires `HF_TOKEN` env var (get from huggingface.co/settings/tokens)

### Custom Research Skills (663)

Domain-specific skills for Gyanateet's research workflow.

| Skill | Description |
|-------|-------------|
| `surgical-video-analysis` | Surgical video MOT, detection, scene understanding on DGX Spark |
| `cuda-kernel-optimization` | Optimize CUDA kernels for GB10 (SM121, Blackwell, unified memory) |
| `cutile-python-gb10` | Tile-based programming with NVIDIA cuTile Python on GB10 |
| `cutile-persistent-matmul-gb10` | Persistent cuTile FP16/FP32 GEMM with ~2-wave launch on GB10 |
| `cutile-fmha-attention-gb10` | Fused multi-head attention with cuTile and online softmax on GB10 |
| `cooperative-groups-gb10` | Cooperative Groups and `cudaLaunchCooperativeKernel` on GB10 |
| `cooperative-groups-warp-tile-gb10` | Warp-level `tiled_partition` reduce/scan/shfl on GB10 |
| `cub-device-algorithms-gb10` | CUB device-wide reduce/scan/sort on GB10 |
| `cub-reduce-by-key-gb10` | CUB `DeviceReduce::ReduceByKey` on GB10 |
| `cub-segmented-sort-gb10` | CUB `DeviceSegmentedSort::SortKeys` on GB10 |
| `cuda-dynamic-parallelism-gb10` | CUDA Dynamic Parallelism (parent/child kernels) on GB10 |
| `cuda-dynamic-parallelism-quicksort-gb10` | Recursive CDP quicksort with `-rdc=true` on GB10 |
| `cuda-graphs-inference-gb10` | Capture/replay CUDA graphs for low-latency inference on GB10 |
| `fused-attention-inference-gb10` | FlashAttention-style fused attention for inference on GB10 |
| `fp8-fp4-quantization-inference-gb10` | FP8/FP4 post-training quantization for Blackwell inference |
| `fast-gemm-inference-gb10` | cuBLASLt and cuTile GEMM for low-latency inference on GB10 |
| `model-evaluation` | Systematic model evaluation, benchmarking, and reporting |
| `video-processing-pipeline` | GPU-accelerated video I/O with ffmpeg/cvcuda/NVDEC on GB10 |
| `thesis-writing` | PhD thesis structure, LaTeX, citation management, viva prep |
| `academic-poster` | Conference poster design with LaTeX/PowerPoint/Figma |
| `literature-review` | Systematic literature review methodology and tools |
| `huggingface-hub` | Upload models/datasets/Spaces, manage HF repositories |
| `experiment-reproducibility` | Seeds, configs, environments, checkpoints, data versioning |
| `collaborative-research` | Multi-author papers, supervisor communication, project management |
| `blackwell-fp4-fp8-block-scaling-ptx-gb10` | FP8 and block-scaled FP4 (NVFP4) PTX MMA with scale factors on SM121 |
| `blackwell-sm121-targeting-gb10` | Correctly compile for GB10 (sm_121/121f/121a), PTX 9.1, and Triton ptxas setup |
| `cp-async-pipeline-gb10` | Multi-stage cp.async copy pipelines for GB10 GMEM->SMEM staging |
| `cuda-occupancy-register-pressure-gb10` | Occupancy, register pressure, launch bounds, and SMEM tradeoffs on GB10 |
| `nsight-compute-tensor-cores-gb10` | Profile Tensor Core utilization and memory bottlenecks with Nsight Compute on GB10 |
| `shared-memory-swizzling-gb10` | Bank-conflict-free shared memory layouts with XOR swizzling and padding tradeoffs on GB10 |
| `tensor-core-fragment-layouts-gb10` | PTX mma.sync fragment layouts and lane-to-element mapping for GB10 Tensor Cores |
| `ada-l40s-optimization` | L40S-specific tuning: FP8, TensorRT-LLM/Triton, multi-GPU PCIe scaling, and media engines. |
| `blackwell-dc-fp4-quantization` | Block-scaled 4-bit formats for training and inference on datacenter Blackwell. |
| `blackwell-dc-moepart-green-contexts` | Resource partitioning (MLOPart, Green Contexts, MPS) and disaggregated prefill/decode serving for datacenter Blackwell. |
| `blackwell-dc-tcgen05-tmem` | Programming datacenter Blackwell (sm_100/sm_103) with tcgen05.mma, TMEM, TMA multicast, and CTA-pair operations. |
| `climate-weather-ml` | FourCastNet, GraphCast, Pangu-Weather, ClimaX, and ECMWF ai-models on GPU clusters. |
| `cuda-q-hybrid-quantum` | CUDA-Q kernels, simulators, VQE/QAOA, PyTorch/JAX integration, and multi-GPU quantum workflows. |
| `cuquantum-tensornet` | GPU-accelerated quantum simulation: state vector, tensor network, expectation values, and gradients. |
| `distributed-launch-slurm-mpi` | Launching multi-node PyTorch/JAX training with SLURM, torchrun, MPI, CUDA-aware MPI, and UCX. |
| `hopper-flashattention-3` | FlashAttention-3 warp specialization, WGMMA/TMA pipelining, and FP8 block quantization on H100/H200. |
| `hopper-fp8-transformer-engine` | FP8 recipes (E4M3/E5M2, current, delayed, and blockwise scaling) with Transformer Engine for LLM training. |
| `hopper-megatron-deepspeed` | Large-model training with Megatron-Core, Megatron-FSDP, DeepSpeed ZeRO, and NVLink4 on H100/H200. |
| `hopper-wgmma-tma` | Low-level Hopper programming with `wgmma.mma_async`, `cp.async.bulk.tensor`, tensor maps, and mbarriers. |
| `jax-gpu-scientific` | JAX `jit`, `vmap`, `shard_map`, device meshes, and XLA memory tuning on H100/H200/Blackwell/L40S. |
| `jax-pde-sciml` | JAX-based SciML: Diffrax, Exponax, JAX-MD, neural operators, and differentiable simulations. |
| `mamba-ssm-kernels` | Mamba-2/3 SSD kernels, fused selective scan, CuTe/Triton/TileLang backends, and chunk scheduling. |
| `materials-discovery-ml` | MatterGen, GNoME, DiffCSP, CDVAE, and crystal structure generation on GPU. |
| `moe-grouped-gemm` | Grouped GEMM, MoE routing, cuBLAS/cuDNN/TransformerEngine/FlashInfer/vLLM backends. |
| `molecular-ml-drug-discovery` | Equivariant GNNs, ML potentials, molecular docking (DiffDock), and generative molecule design on GPU. |
| `multigpu-nccl-topology` | NCCL, NVLink/NVSwitch, PCIe, InfiniBand/RoCE, GPUDirect, and common topology hang fixes. |
| `neural-operators-pinns` | Fourier Neural Operator, DeepONet, PINNs, and JAX/Diffrax/Exponax for PDEs on GPU. |
| `protein-folding-gpu` | AlphaFold 3, ESM3, Boltz, BioNeMo Fold-CP, OpenFold, and high-throughput protein folding pipelines. |
| `scientific-data-formats` | Zarr, TensorStore, WebDataset, HDF5/NetCDF, KvikIO, and direct-to-GPU I/O pipelines. |
| `torch-compile-inductor` | PyTorch 2.7+ `torch.compile`, Inductor autotune, custom operators, CuTeDSL/Gluon backends, and debug. |
| `triton-cross-arch` | Writing and deploying Triton kernels across sm_80, sm_89, sm_90, sm_100, sm_120, and sm_121. |
| `ampere-a100-scientific` | A100 architecture, TF32, structured sparsity, MIG, FP64, and cuBLAS/cuDNN paths for scientific workloads. |
| `bioinformatics-genomics-ml` | DNABERT, Enformer, single-cell analysis with scVI/scGPT, and RAPIDS cuDF for genomics pipelines. |
| `cuda-tile-advanced-gb10` | cuTile Python/C++ advanced features: block-scaled `ct.mma_scaled`, Tile IR, persistent kernels, and Nsight Tile profiling. |
| `cutlass-persistent-kernels` | CUTLASS 3.x persistent kernels, cooperative vs ping-pong schedule, warp specialization, and CollectiveBuilder for FP8/FP4. |
| `dgx-spark-multinode-roce` | Connect 2-3 DGX Sparks over QSFP RoCE, NCCL configuration, Docker host networking, and no GPUDirect RDMA. |
| `dgx-spark-uma-tuning` | Tuning DGX Spark's 128 GB unified LPDDR5X memory, page cache competition, thermal throttling, EC firmware, and CPU compilation flags. |
| `flashattention-4-sm121` | FlashAttention-4 consumer Blackwell support on sm_120/sm_121: paged KV, head_dim limits, FP8, and the CuTe DSL dispatch path. |
| `geospatial-remote-sensing-ml` | Prithvi, SatMAE, TorchGeo, TerraTorch, segment-anything for Earth observation, and NVIDIA cuOpt. |
| `llm-inference-gb10` | vLLM and TensorRT-LLM inference on GB10: FP8 KV, Marlin, MTP, MoE backend selection, and driver 580.x. |
| `mixed-precision-training-gpu` | BF16, FP16, FP8, TF32, FP32 master weights, loss scaling, and when to use each on Ampere/Hopper/Blackwell. |
| `molecular-dynamics-gpu` | MACE, CHGNet, DeePMD-kit, LAMMPS/GROMACS integration, and multi-GPU spatial decomposition for ML potentials. |
| `nsight-profiling-gpu` | Nsight Compute sections/metrics, Nsight Systems gap analysis, hardware CUDA trace, and Tile profiling for cuTile. |
| `pytorch-blackwell-deployment` | PyTorch nightly wheels, sm_100/sm_120 support, architecture detection, and common Blackwell-specific errors. |
| `quantization-backends-gpu` | AWQ, GPTQ, AutoRound, Marlin, FP8, NVFP4, MXFP4, and backend selection for A100/H100/L40S/RTX50/GB10. |
| `astrophysics-cosmology-ml` | Gravitational lensing, galaxy classification, N-body simulations, dark matter mapping, and cosmological parameter inference. |
| `bayesian-inference-gpu` | MCMC, NUTS, variational inference, NumPyro, BlackJAX, and GPyTorch on NVIDIA GPUs. |
| `causal-inference-science` | Do-calculus, causal discovery, structural causal models, transportability, and mediation for observational and experimental data. |
| `differential-equations-gpu` | ODE/PDE/SDE solvers, spectral and finite element methods, Diffrax, FEniCSx, PETSc, and NekRS on GPU. |
| `equivariant-neural-networks-science` | E(3)/SE(3)-equivariant networks (E3NN, Equiformer, MACE, NequIP, steerable CNNs) for atomic and molecular systems. |
| `experiment-tracking-optimization` | W&B, MLflow, Neptune, Aim, Optuna, Ray Tune, and reproducible hyperparameter search on HPC. |
| `fluid-dynamics-cfd-ml` | Neural operators, PhysicsNeMo (Modulus), JAX-Fluids, PhiFlow, and surrogate CFD on GPU. |
| `generative-models-science` | Diffusion, flow matching, score-based models, and normalizing flows for molecules, materials, and inverse design. |
| `gnn-science` | GNNs for molecules, materials, weather, neural operators, and large-scale graph training on GPU. |
| `neuroscience-ml-gpu` | fMRI, calcium imaging, connectomics, and neural decoding with cuBNM, DeepWonder, scGPT, and RAPIDS. |
| `optimization-gpu` | First- and second-order optimization, Optax/JAXopt, L-BFGS, trust-region, constrained, and Newton-Krylov methods on GPU. |
| `quantum-chemistry-gpu` | GPU-accelerated DFT, Hartree-Fock, coupled cluster with PySCF/GPU4PySCF, and hybrid quantum-classical ML. |
| `reinforcement-learning-science` | RL for tokamak plasma control, drug design, experiment design, and autonomous scientific systems. |
| `scientific-linear-algebra-gpu` | Dense and sparse linear algebra with cuBLAS, cuSOLVER, cuSPARSE, cuDSS, MAGMA, and device-side cuSolverDx. |
| `scientific-workflows-hpc` | Workflow engines (Snakemake, Nextflow, CWL), containers, DVC, SLURM job arrays, checkpointing, and cloud HPC. |
| `signal-image-processing-gpu` | FFT, wavelets, filtering, compressed sensing, and tomography with cuFFT, RAPIDS, and GPU pipelines. |
| `transformers-for-science` | Transformers for protein, genomics, weather, chemistry, math, and symbolic regression; ESM, AlphaFold, Prithvi, DNABERT, AI-Descartes. |
| `uncertainty-quantification-science` | Conformal prediction, evidential learning, Bayesian neural nets, ensembles, Fortuna, and UQ for PDE surrogates. |
| `cicd-ml-pipelines` | GitHub Actions, GitLab CI, pre-commit, artifact registries, and model promotion gates for ML pipelines. |
| `containers-reproducibility` | Docker, Apptainer/Singularity, Podman, conda-lock, Nix, and reproducible scientific environments. |
| `data-engineering-science` | ETL pipelines, feature stores, vector databases, RAG, and embeddings for scientific data. |
| `distributed-storage-hpc` | Lustre, BeeGFS, GPFS, WekaFS, Ceph, Zarr, and TensorStore for high-throughput scientific data. |
| `fault-tolerance-checkpointing` | PyTorch DCP, DeepSpeed elastic training, asynchronous checkpointing, and multi-tier checkpoint storage. |
| `gpu-cluster-management` | SLURM, PBS, LSF, cloud bursting, hybrid clusters, and AWS ParallelCluster for GPU HPC. |
| `kubernetes-gpu-orchestration` | NVIDIA GPU Operator, MIG, MPS, Kueue, Volcano, gang scheduling, and DRA for ML workloads on Kubernetes. |
| `ml-security-supply-chain` | Model signing, AIBOM/ML-BOM, container scanning, malicious pickle detection, and provenance for ML artifacts. |
| `model-serving-gpu` | Triton Inference Server, TensorRT-LLM, vLLM, TorchServe, FastAPI, and BentoML for production inference. |
| `monitoring-observability-ml` | Prometheus, Grafana, Weights & Biases, MLflow, Evidently, and drift detection for production ML. |
| `networking-distributed-training` | InfiniBand, RoCE, NCCL tuning, AWS EFA, and diagnosing multi-node network issues. |
| `ray-ml-distributed` | Ray Train, Ray Tune, Ray Serve, Ray Data, and Ray clusters for scaling training, tuning, serving, and data processing. |
| `agritech-phenotyping` | UAV/drone imaging, vision-language models, yield estimation, disease detection, and crop monitoring on GPU. |
| `battery-materials-ml` | GNNs, Gaussian processes, and high-throughput screening for battery materials, redox flow batteries, and carbon capture solvents. |
| `biodiversity-edna-ml` | Environmental DNA, species distribution modeling, zero-shot taxonomic assignment, and biodiversity monitoring on GPU. |
| `epidemiology-disease-surveillance` | SIR/SEIR models, GNNs, Gaussian processes, and transfer learning for outbreak prediction and disease dynamics. |
| `high-energy-physics-ml` | Jet tagging, event reconstruction, Particle Transformer, Hypergraph, and ROOT/Geant4 integration on GPU. |
| `industry-4-predictive-maintenance` | RAPIDS, NVIDIA Omniverse, XGBoost, anomaly detection, and digital twins for manufacturing. |
| `lab-robotics-digital-twins` | MATTERIX, LucidGrasp, 6D pose, sim-to-real, and digital twins for autonomous science labs. |
| `proteomics-metabolomics-ml` | Mass spectrometry, peptide identification, DelPi, DIA-BERT, GiCOPS, ANN-SoLo, and metabolite annotation on GPU. |
| `renewable-energy-forecasting` | Spatio-temporal diffusion, FNO, attention, and RL for solar/wind forecasting and energy dispatch. |
| `social-simulation-ml` | AgentTorch, LLM-based agents, differentiable ABM, and causal discovery for social and economic systems. |
| `spatial-transcriptomics-gpu` | Cell segmentation, transcript assignment, BIDCell, segger, PanoSpace, and foundation models for spatial omics. |
| `sports-biomechanics-ml` | Wearable sensors, ST-GNNs, federated learning, and multimodal fusion for athlete performance and injury risk. |
| `category-theory-ml` | Functorial data modeling, categorical deep learning, structured cospans, string diagrams, and topos theory for ML. |
| `differential-geometry-ml` | Riemannian manifolds, geodesics, natural gradients, hyperbolic ML, and optimization on curved spaces. |
| `game-theory-multiagent-ml` | Nash equilibria, mean-field games, mechanism design, and deep multi-agent reinforcement learning. |
| `high-dimensional-statistics` | Sparsity, LASSO, compressed sensing, concentration inequalities, and covariance estimation. |
| `information-geometry-ml` | Fisher information metric, natural gradient, alpha-connections, and geometry of probability distributions. |
| `kernel-methods-science` | RKHS, Gaussian processes, MMD, kernel mean embeddings, and kernel methods for PDEs. |
| `optimal-transport-ml` | Wasserstein distance, Sinkhorn algorithm, sliced Wasserstein, and applications to generative modeling and domain adaptation. |
| `optimization-under-uncertainty` | Robust optimization, stochastic programming, distributionally robust optimization, and Wasserstein DRO. |
| `random-matrix-theory-ml` | Marchenko-Pastur, semicircle law, free probability, and spectral analysis of neural networks. |
| `spectral-graph-ml` | Graph Laplacian, spectral clustering, spectral GNNs, graph partitioning, and spectral sparsification. |
| `stochastic-processes-ml` | Itô calculus, score-based generative models, neural SDEs, rough paths, and continuous-time generative modeling. |
| `topological-data-analysis` | Persistent homology, Ripser, GUDHI, Mapper, and topological deep learning for shape-aware scientific ML. |
| `agent-evaluation-benchmarks` | Measure agent capability on coding, web, tool use, and open-ended reasoning benchmarks. |
| `agent-memory` | Short-term and long-term memory for agents: vector stores, summaries, entity tracking, and memory hierarchies. |
| `llm-judge-evaluation` | Use strong language models to evaluate, score, and compare outputs from other models or pipelines. |
| `llm-reasoning` | Chain-of-thought, self-consistency, tree-of-thoughts, and reasoning-optimized prompting for large language models. |
| `llm-redteaming` | Systematically probe LLMs for harmful outputs, jailbreaks, privacy leaks, and misalignment. |
| `long-context-llm` | Architectures, position interpolation, and evaluation for language models with very long contexts. |
| `mcp-integration` | Connect agents to external tools, databases, and services using the Model Context Protocol (MCP). |
| `multi-agent-orchestration` | Coordinate multiple specialist agents to decompose tasks, debate, and synthesize solutions. |
| `prompt-engineering-advanced` | Structured prompting, few-shot, chain-of-thought, role prompts, and prompt optimization for LLMs. |
| `rag-retrieval-evaluation` | Evaluate retrieval quality, answer relevance, and end-to-end RAG pipeline performance. |
| `test-time-compute` | Improve LLM output quality by increasing inference-time computation: search, verification, and reward models. |
| `tool-use-agents` | Design LLM agents that call functions, APIs, and utilities to gather facts and take actions. |
| `ai-for-arts-humanities` | Digital humanities, text analysis, image restoration, and creative AI for cultural heritage. |
| `ai-for-autonomous-vehicles` | Perception, prediction, planning, and simulation for self-driving cars and mobile robots. |
| `ai-for-biology` | Deep learning for genomics, transcriptomics, proteomics, cell imaging, and biological sequence modeling. |
| `ai-for-chemistry` | Molecular property prediction, generative chemistry, reaction prediction, and cheminformatics with deep learning. |
| `ai-for-education` | Personalized learning, knowledge tracing, automated assessment, and intelligent tutoring systems. |
| `ai-for-finance` | Machine learning for time-series forecasting, risk modeling, algorithmic trading, and financial NLP. |
| `ai-for-law` | Legal document analysis, case law retrieval, contract review, and legal reasoning benchmarks. |
| `ai-for-music` | Music generation, transcription, recommendation, and audio processing with deep learning. |
| `ai-for-physics-simulation` | Neural operators, surrogate models, and learned emulators for partial differential equations and physical systems. |
| `ai-for-psychiatry-mental-health` | Machine learning for digital phenotyping, diagnostic support, treatment prediction, and crisis detection. |
| `ai-for-quantum-computing` | Machine learning for quantum state tomography, variational quantum algorithms, quantum control, and error mitigation. |
| `ai-for-robotics` | Imitation learning, reinforcement learning, sim-to-real, and foundation models for robot manipulation and navigation. |
| `ai-for-agriculture` | Crop monitoring, yield prediction, pest detection, and precision agriculture with ML and remote sensing. |
| `ai-for-archaeology` | Remote sensing, LiDAR, and computer vision for site detection, artifact analysis, and heritage preservation. |
| `ai-for-carbon-capture` | Machine learning for adsorbent and solvent screening, process optimization, and carbon capture materials design. |
| `ai-for-forensics` | ML for image authentication, deepfake detection, authorship attribution, and anomaly detection in forensic evidence. |
| `ai-for-gravitational-waves` | Deep learning for compact binary coalescence search, parameter estimation, and glitch classification. |
| `ai-for-materials-synthesis` | Machine learning for synthesis route prediction, process optimization, and inverse design of materials. |
| `ai-for-nuclear-engineering` | Machine learning for reactor design, plasma control, material degradation, and fusion ignition prediction. |
| `ai-for-oceanography` | Data-driven ocean forecasting, current reconstruction, eddy detection, and marine ecosystem modeling. |
| `ai-for-satellite-imaging` | Earth observation foundation models, land-use classification, change detection, and disaster mapping. |
| `ai-for-seismology` | Machine learning for earthquake detection, phase picking, denoising, and seismic signal classification. |
| `ai-for-volcanology` | Machine learning for eruption forecasting, volcanic seismicity classification, and hazard assessment. |
| `ai-for-water-security` | ML for water quality prediction, leak detection, flood forecasting, and hydrological modeling. |
| `active-learning` | Iteratively select the most informative unlabeled data points for efficient annotation and model improvement. |
| `ai-fairness` | Detect, measure, and mitigate bias across demographic groups in classification, ranking, and regression. |
| `curriculum-learning` | Order training examples from easy to hard to improve convergence and generalization. |
| `domain-adaptation` | Transfer knowledge from a labeled source domain to an unlabeled or partially labeled target domain. |
| `explainable-ai` | Feature attribution, concept-based explanations, saliency maps, and interpretability for black-box models. |
| `federated-learning` | Decentralized model training across clients, handling non-IID data, aggregation, and personalization. |
| `few-shot-learning` | Learning from a handful of labeled examples through meta-learning, prompt tuning, and data augmentation. |
| `meta-learning` | Learn-to-learn methods such as MAML, metric learning, and neural processes for fast adaptation. |
| `model-interpretability` | Intrinsic and post-hoc methods for understanding model behavior, features, and decision boundaries. |
| `privacy-preserving-ml` | Differential privacy, federated learning, homomorphic encryption, and secure multi-party computation for ML. |
| `robust-ml` | Adversarial robustness, distribution shift, out-of-distribution detection, and reliable model performance. |
| `uncertainty-quantification-ml` | Predictive uncertainty, calibration, conformal prediction, and Bayesian methods for reliable ML. |
| `agent-monitoring-guardrails` | Runtime monitoring, safety policy enforcement, tool-call validation, probabilistic risk prediction, and guardrail frameworks for LLM agents. |
| `ai-for-cad` | Deep generative models for parametric CAD sketches, B-rep synthesis, sketch-and-extrude sequences, and vision-language conditional CAD generation. |
| `cost-optimization-cloud` | FinOps practices, spot/preemptible instances, right-sizing, reserved capacity, autoscaling, and cost-aware scheduling for ML workloads. |
| `data-stream-processing` | Apache Kafka and Flink pipelines, event-time semantics, exactly-once delivery, online feature engineering, and real-time model updates. |
| `edge-ai` | Quantization, pruning, knowledge distillation, neural architecture search, and deployment of ML models on mobile, embedded, and edge accelerators. |
| `generative-design` | Deep generative models (VAEs, GANs, diffusion) for engineering design synthesis, constraint-aware generation, Pareto-front exploration, and design automation. |
| `graph-databases` | Property graph models, Cypher/Gremlin querying, graph embeddings, GNNs on graph DBs, and knowledge graph completion for connected data. |
| `industrial-digital-twins` | Real-time virtual replicas of physical systems for monitoring, predictive maintenance, process optimization, and hybrid physics-ML modeling. |
| `ml-infrastructure-as-code` | Terraform, Pulumi, and GitOps for reproducible ML platforms, modular MLOps stacks, and CI/CD-managed infrastructure. |
| `real-time-ml` | Streaming inference, online learning, low-latency GPU serving, event-time semantics, and service-level objectives for real-time ML systems. |
| `topology-optimization` | SIMP, neural reparameterization, generative topology optimization, physics-informed neural networks, and learned resolution-free solvers for structural design. |
| `vector-databases` | Approximate nearest neighbor search, dense-embedding storage, metadata filtering, hybrid search, and vector indexing for RAG and recommendation. |
| `ai-peer-review` | Use AI tools and structured checklists to write constructive, ethical peer reviews for manuscripts and proposals. |
| `citation-management` | Organize references, manage PDFs, format bibliographies, and share libraries with Zotero, Mendeley, or BibTeX. |
| `collaboration-and-team-science` | Build, lead, and sustain productive interdisciplinary research teams with clear roles, communication, and shared tools. |
| `competitive-analysis` | Map industry structure, benchmark competitors, and identify strategic positioning using Porter's Five Forces, SWOT, and data. |
| `grant-proposal-writing` | Structure Specific Aims, research strategy, budget, and broader impact sections for NIH/NSF/ERC-style proposals with AI drafting support. |
| `market-research-ai` | Design surveys, segment customers, analyze open-ended responses, and forecast market trends with AI-driven tools. |
| `product-requirements-ai` | Draft, validate, and track product requirements documents (PRDs) with user stories, assumptions, and success metrics. |
| `research-data-storytelling` | Turn complex scientific results into narrative visualizations and stories that resonate with specialists and the public. |
| `research-paper-ideation` | Use LLMs, citation networks, and structured brainstorming to generate and refine research questions, hypotheses, and project outlines. |
| `research-presentation-design` | Build clear, compelling slides and posters for seminars, conferences, and outreach using narrative structure and visual hierarchy. |
| `scientific-writing` | Improve clarity, structure, and style for manuscripts, theses, and reports using AI drafting and editing tools. |
| `user-interviews-synthesis` | Turn interview transcripts into themes, insights, and personas using thematic analysis, affinity mapping, and AI coding. |
| `ai-for-biofoundries` | AI/ML-driven lab automation, robotic liquid handling, closed-loop DBTL, and self-driving laboratories for synthetic biology. |
| `ai-for-digital-organism` | Computational models, simulations, and multiscale foundation models of living systems as AI-driven digital organisms. |
| `ai-for-drug-repurposing` | Graph ML, knowledge graphs, LLMs, and transcriptomics for identifying new indications for existing drugs. |
| `ai-for-immunology` | Machine learning for adaptive immune receptor repertoires, epitope-MHC binding, immune cell phenotyping, and vaccine/immunotherapy design. |
| `ai-for-longevity` | Biological aging clocks, biomarkers of aging, longevity intervention mining, and integrative multi-omic models of aging. |
| `ai-for-neuroscience` | Deep learning for neural recordings, brain decoding, neuroimaging analysis, connectomics, and NeuroAI foundation models. |
| `ai-for-nutrition` | Machine learning and generative AI for personalized nutrition, dietary assessment, meal planning, food recognition, and nutrition-health modeling. |
| `ai-for-precision-medicine` | Multimodal machine learning for personalized diagnosis, treatment selection, risk prediction, and integration of genomics, EHRs, imaging, and wearables. |
| `ai-for-protein-design` | Inverse folding, generative backbone design, and binder engineering with ProteinMPNN, RFdiffusion, structure predictors, and Rosetta validation. |
| `ai-for-rare-disease` | AI for rare disease diagnosis, target prioritization, drug repurposing, natural history modeling, and diagnostic-odyssey support. |
| `ai-for-sleep` | Machine learning for sleep staging, sleep disorder detection, wearable PSG analysis, and sleep health monitoring. |
| `ai-for-synthetic-biology` | Machine learning for genetic circuit design, promoter and RBS optimization, metabolic pathway engineering, and closed-loop Design-Build-Test-Learn biofoundry pipelines. |
| `analog-computing` | Reconfigurable analog accelerators, in-memory analog computing, and mixed-signal AI hardware. |
| `dask-ml` | Distributed and out-of-core machine learning with Dask and scikit-learn, XGBoost, and hyperparameter search. |
| `data-versioning` | DVC, lakeFS, and Delta Lake for versioning datasets, models, and pipelines alongside code. |
| `feature-stores` | Feast, Tecton, and Hopsworks for centralized feature definition, versioning, and online/offline serving. |
| `high-performance-python` | Numba, Cython, pybind11, vectorization, and profiling for Python code that rivals C/Fortran speed. |
| `in-memory-computing` | Compute-in-memory, processing-in-memory, and emerging NVM technologies (PCM, RRAM, MRAM) for AI. |
| `ml-metadata-lineage` | ML Metadata (MLMD), MLflow, and Kubeflow lineage for tracking artifacts, executions, and provenance. |
| `modin-pandas` | Drop-in distributed, parallel pandas replacement using Modin with Ray or Dask backends. |
| `neuromorphic-computing` | Spiking neural networks (SNNs), event-based processing, and brain-inspired low-power accelerators like Intel Loihi and BrainChip. |
| `photonic-computing` | Silicon photonics, optical processing units, and photonic interconnects for energy-efficient AI and HPC. |
| `quantum-machine-learning` | Hybrid quantum-classical ML with variational quantum circuits, PennyLane, TensorFlow Quantum, and Qiskit. |
| `wafer-scale-ai` | Cerebras Wafer Scale Engine, wafer-scale training and inference, and massive on-chip compute fabric. |
| `contrastive-learning` | Instance discrimination, InfoNCE, SimCLR, MoCo, CLIP, and deep metric learning for vision, language, and retrieval. |
| `curriculum-rl` | Task sequencing, automatic curriculum generation, and progressive difficulty for sample-efficient RL. |
| `hierarchical-rl` | Options, feudal networks, and goal-conditioned hierarchies for long-horizon, sparse-reward tasks. |
| `imitation-learning` | Behavioral cloning, DAgger, GAIL, and learning policies from expert demonstrations with or without a reward function. |
| `inverse-rl` | Recover reward functions from expert demonstrations using MaxEnt IRL, apprenticeship learning, and adversarial IRL. |
| `masked-autoencoders` | BERT-style masked prediction for vision, BEVT, data2vec, and generative masked image and language modeling. |
| `model-based-rl` | Learn environment dynamics for sample-efficient planning and policy optimization with PETS, MBPO, PlaNet, and MuZero. |
| `multi-task-learning` | Shared representations, hard and soft parameter sharing, MTL architectures (MMoE, PLE, MTAN), and gradient balancing. |
| `offline-rl` | Learn from static logged datasets with CQL, IQL, TD3+BC, D4RL, and conservative/batch RL methods. |
| `safe-rl` | Constrained Markov Decision Processes, CPO, P3O, Lagrangian methods, and safety-gym benchmarks for constrained RL. |
| `self-supervised-learning` | Pretext tasks, contrastive and non-contrastive SSL, masked prediction, and unsupervised representation learning for vision, language, and graphs. |
| `world-models` | Latent dynamics models, recurrent state-space models, Dreamer, PlaNet, and agents that plan in imagination. |
| `ai-for-climate-policy` | Natural-language analysis of climate laws, NDCs, and policies; target extraction, alignment scoring, and climate-finance tracking. |
| `ai-for-disaster-response` | Situational awareness, damage assessment, evacuation planning, supply pre-positioning, and multi-modal disaster imagery analysis. |
| `ai-for-energy-grid` | Power-flow surrogates, renewable and load forecasting, grid stability, optimal power flow, and AI-assisted grid operations. |
| `ai-for-governance` | Public-service delivery, regulatory compliance, algorithmic accountability, participatory policy tools, and fair decision-support systems. |
| `ai-for-logistics` | Vehicle routing, last-mile delivery, warehouse automation, fleet scheduling, and dynamic logistics optimization. |
| `ai-for-manufacturing` | Predictive maintenance, quality control, process optimization, digital twins, and human-interpretable factory AI. |
| `ai-for-public-health` | Disease surveillance, outbreak prediction, resource allocation, geospatial health modeling, and health-equity analytics. |
| `ai-for-smart-cities` | Urban computing, IoT analytics, spatio-temporal forecasting, mobility, public safety, and citizen-centric services. |
| `ai-for-social-good` | Education, poverty alleviation, agriculture, humanitarian response, accessibility, and community-driven AI for underserved populations. |
| `ai-for-space-exploration` | Onboard autonomy, science target selection, anomaly detection, mission planning, and analysis of space and Earth-observation data. |
| `ai-for-supply-chain` | Demand forecasting, inventory optimization, risk and resilience, supplier analytics, and end-to-end supply chain visibility. |
| `ai-for-transportation` | Traffic prediction, route optimization, public transit planning, autonomous driving, and multi-modal mobility. |
| `ai-for-battery-materials` | Machine learning for cathode, anode, electrolyte, and separator discovery, as well as battery lifetime and charging protocol optimization. |
| `ai-for-catalysis` | Machine learning for catalyst discovery, reaction mechanism elucidation, activity and selectivity prediction, and catalytic process optimization. |
| `ai-for-ceramics` | Data-driven design, processing optimization, and microstructure-property prediction for ceramic and refractory materials. |
| `ai-for-composites` | Machine learning for composite material design, manufacturing process optimization, defect detection, and multiscale property prediction. |
| `ai-for-corrosion` | Machine learning for corrosion rate prediction, corrosion-resistant alloy design, protective coating optimization, and infrastructure degradation monitoring. |
| `ai-for-materials-characterization` | Machine learning for automated interpretation of microscopy, spectroscopy, diffraction, and tomography data in materials science. |
| `ai-for-membranes` | Machine learning for membrane material design, permeability and selectivity prediction, fouling control, and separation process optimization. |
| `ai-for-metals` | Machine learning for alloy design, phase stability, mechanical properties, process optimization, and microstructure-property mapping. |
| `ai-for-photovoltaics` | Machine learning for solar-cell materials discovery, perovskite and organic PV optimization, device engineering, and stability prediction. |
| `ai-for-polymers` | Machine learning for polymer property prediction, generative design, process optimization, and structure representation. |
| `ai-for-semiconductors` | Machine learning for semiconductor materials discovery, bandgap engineering, defect analysis, and fabrication process optimization. |
| `ai-for-superconductors` | Machine learning for superconductor discovery, critical temperature prediction, electron-phonon modeling, and materials screening. |
| `ai-for-ecology` | Species distribution modeling, habitat suitability, biodiversity monitoring, and ecological forecasting using ML and remote sensing. |
| `ai-for-environmental-science` | Remote sensing, land-cover mapping, ecosystem service assessment, and integrated modeling for environmental monitoring and analysis. |
| `ai-for-fisheries` | Fish stock assessment, catch forecasting, aquaculture monitoring, eDNA, and IUU fishing detection with ML. |
| `ai-for-forestry` | Forest inventory, tree segmentation, biomass estimation, and species mapping from remote sensing and LiDAR. |
| `ai-for-geology` | Geologic mapping, mineral prospectivity, geophysical inversion, drill-core imagery, and remote sensing with ML and deep learning. |
| `ai-for-hydrology` | Rainfall-runoff modeling, streamflow forecasting, flood prediction, and physics-informed deep learning for water systems. |
| `ai-for-meteorology` | Numerical weather prediction emulators, precipitation nowcasting, extreme-weather detection, and weather foundation models. |
| `ai-for-mineralogy` | XRD, SEM-EDS, Raman, and hyperspectral imaging for automated mineral identification, classification, and segmentation. |
| `ai-for-paleontology` | Automated fossil identification, morphometric analysis, 3D segmentation, and taxonomic classification from images and point clouds. |
| `ai-for-pollution` | Air, water, and soil pollution monitoring, source apportionment, forecasting, and regulatory compliance with ML. |
| `ai-for-soil-science` | Digital soil mapping, pedotransfer functions, spectroscopic prediction, and soil health assessment with ML. |
| `ai-for-wildlife-conservation` | Camera-trap image classification, acoustic monitoring, animal re-identification, and anti-poaching analytics. |
| `ai-for-customer-service` | Conversational AI, intent classification, sentiment and satisfaction analysis, ticket routing, and agent-assist systems. |
| `ai-for-demand-forecasting` | Time-series forecasting, hierarchical and intermittent demand, probabilistic forecasts, and promotion/event effects. |
| `ai-for-economics` | Causal inference, policy evaluation, nowcasting, heterogeneous treatment effects, and demand estimation for economic and policy analysis. |
| `ai-for-fraud-detection` | Transaction fraud, anti-money laundering, anomaly detection, graph-based fraud networks, and concept-drift monitoring. |
| `ai-for-hr` | Talent analytics, recruitment matching, attrition prediction, workforce planning, and compensation and equity analysis. |
| `ai-for-marketing` | Customer segmentation, personalization, propensity modeling, marketing-mix attribution, and generative AI for content and campaigns. |
| `ai-for-operations-research` | Optimization, MILP/CP, vehicle routing and scheduling, decision-focused learning, and learning-augmented heuristics. |
| `ai-for-pricing` | Price elasticity, dynamic and personalized pricing, revenue management, promotion optimization, and causal demand forecasting for pricing. |
| `ai-for-recommendation-systems` | Collaborative filtering, content-based and hybrid recommendation, sequence models, and multi-objective ranking for commerce and content. |
| `ai-for-retail` | Demand forecasting, inventory placement, personalized recommendations, dynamic pricing, and omnichannel fulfillment for retail. |
| `ai-for-sales` | Predictive lead scoring, sales forecasting, opportunity win probability, next-best action, and pipeline analytics. |
| `ai-for-supply-chain-optimization` | Multi-echelon inventory, distribution network design, demand-supply synchronization, and resilient supply chain planning. |
| `ai-for-cardiology` | ECG interpretation, arrhythmia detection, heart failure screening, echocardiography analysis, and cardiovascular risk stratification with deep learning. |
| `ai-for-clinical-nlp` | Natural language processing for electronic health records, clinical entity extraction, term normalization, de-identification, and question answering. |
| `ai-for-dermatology` | Skin lesion classification, dermoscopy analysis, melanoma detection, teledermatology, and fairness across skin tones with deep learning. |
| `ai-for-digital-therapeutics` | Software-as-a-medical-device interventions for mental health, substance use, sleep, ADHD, and chronic disease delivered through apps and wearables. |
| `ai-for-gastroenterology` | AI-assisted endoscopy, real-time polyp detection and characterization, colonoscopy quality, and colorectal cancer screening. |
| `ai-for-medical-imaging` | General medical image preprocessing, segmentation, classification, and deployment with DICOM, MONAI, nnU-Net, and clinical AI pipelines. |
| `ai-for-neurology` | Neuroimaging and EEG analysis for stroke, brain tumors, epilepsy, and neurodegeneration, including lesion segmentation and outcome prediction. |
| `ai-for-oncology` | AI for cancer detection, subtyping, treatment response, prognosis, radiomics, pathology, and clinical trial matching. |
| `ai-for-ophthalmology` | Diabetic retinopathy screening, OCT analysis, glaucoma detection, and AI for retinal disease diagnosis from fundus photography. |
| `ai-for-pathology` | Computational pathology, whole-slide image analysis, cancer subtyping, biomarker discovery, and vision-language models for histopathology. |
| `ai-for-pulmonology` | Chest X-ray and CT interpretation, COPD and asthma assessment, respiratory sound analysis, and pulmonary disease risk prediction. |
| `ai-for-radiology` | Deep learning for X-ray, CT, MRI, and mammography interpretation, including lesion detection, segmentation, report generation, and radiology foundation models. |
| `ai-for-architecture` | AI for generative spatial layouts, floorplan synthesis, style exploration, and text/sketch-driven conceptual design. |
| `ai-for-building-design` | AI for energy, daylight, HVAC, envelope, and MEP performance optimization in the built environment. |
| `ai-for-construction` | AI for construction site safety, progress monitoring, schedule and cost risk, robotics, and digital-twin-enabled project delivery. |
| `ai-for-cosmetics` | AI for personalized skincare, formulation optimization, shade matching, safety/toxicity prediction, and consumer insight. |
| `ai-for-fashion` | AI for trend forecasting, outfit recommendation, virtual try-on, generative design, and personalized shopping. |
| `ai-for-food-and-beverage` | AI for food safety, quality control, recipe and product development, shelf-life prediction, and supply chain optimization. |
| `ai-for-hospitality` | AI for guest personalization, revenue management, dynamic pricing, operations, and conversational service. |
| `ai-for-media-and-entertainment` | AI for content recommendation, personalization, generative media, audience analytics, and rights/compliance workflows. |
| `ai-for-mining` | AI for mineral exploration, ore grade estimation, predictive maintenance, autonomous haulage, and mine safety. |
| `ai-for-oil-and-gas` | AI for seismic interpretation, reservoir characterization, production forecasting, and predictive maintenance in energy operations. |
| `ai-for-sports` | AI for athlete tracking, match analytics, performance prediction, injury risk, and tactical decision support. |
| `ai-for-textiles` | AI for fabric defect detection, pattern and color design, sorting, and textile supply chain optimization. |
| `api-development` | REST, gRPC, and GraphQL API design, implementation, documentation, and versioning for ML services. |
| `backend-engineering` | Server-side development, async task queues, databases, caching, and resilience patterns for ML products. |
| `data-engineering-best-practices` | Data lifecycle management, data quality, observability, lineage, testing, version control, and infrastructure-as-code for robust data systems. |
| `data-lakes` | Object storage, open table formats, lakehouse architecture, and batch/stream unification for ML and analytics. |
| `data-pipelines-ml` | Orchestrating end-to-end ML workflows with task dependencies, artifact tracking, retries, and reproducibility. |
| `data-warehousing` | Cloud data warehouses, dimensional modeling, indexing, partitioning, and workload optimization. |
| `etl-and-elt` | Extract, transform, load patterns and the modern extract, load, transform paradigm with tooling and trade-offs. |
| `event-driven-architecture` | Events, event brokers, event sourcing, CQRS, and event-driven microservices for scalable, decoupled systems. |
| `frontend-engineering` | Building user interfaces for ML-powered applications with modern frameworks, state management, and data visualization. |
| `full-stack-ml` | End-to-end ML applications spanning data, model, API, frontend, deployment, and monitoring. |
| `microservices` | Small, independently deployable services, inter-service communication, containers, and service discovery. |
| `streaming-data` | Real-time data ingestion and processing with stream processors, message brokers, and event-time semantics. |
| `ai-for-anthropology` | Computational ethnography, NLP for field notes and interviews, multimodal cultural analysis, and AI-assisted thick description and reflexivity. |
| `ai-for-communication` | Computational communication science: content analysis, information diffusion, agenda setting, and audience effects across digital platforms. |
| `ai-for-criminology` | Predictive policing, recidivism risk assessment, crime forecasting, criminal network analysis, and fairness-aware public safety research. |
| `ai-for-history` | HTR and OCR for historical documents, event extraction, temporal reasoning, geospatial and network analysis, and distant reading for historical research. |
| `ai-for-international-relations` | Conflict forecasting, event data analysis, crisis early warning, treaty and negotiation text mining, and geopolitical risk modeling. |
| `ai-for-journalism` | Algorithmic journalism, automated reporting, fact-checking, news recommendation, and AI-assisted investigative data reporting. |
| `ai-for-linguistics` | Computational linguistics, corpus analysis, morphosyntactic annotation, syntactic parsing, language modeling, and NLP tools for linguistic research. |
| `ai-for-media-literacy` | AI for detecting disinformation, prebunking, source credibility, and teaching critical thinking and digital literacy. |
| `ai-for-philosophy` | Computational philosophy, argument mining, automated reasoning, text analysis of philosophical corpora, and LLM-assisted conceptual analysis. |
| `ai-for-political-science` | Text-as-data for politics: manifesto scaling, sentiment and stance detection, legislative and voting analysis, and causal inference for political institutions. |
| `ai-for-public-policy` | Causal and predictive policy evaluation, program impact assessment, regulatory text analysis, and equitable resource allocation for government and public administration. |
| `ai-for-sociology` | Computational social science for sociology: text and image classification, survey augmentation, social network analysis, and modeling social inequalities. |
| `ai-for-3d-vision` | 3D reconstruction, point cloud processing, NeRF and Gaussian splatting, depth estimation, 3D detection, and scene understanding. |
| `ai-for-animation` | Motion synthesis, inbetweening, character retargeting, physics-based animation, and style transfer for animated content. |
| `ai-for-audio` | Audio enhancement, source separation, music generation, audio event detection, and speech enhancement. |
| `ai-for-augmented-reality` | SLAM, scene understanding, depth completion, registration, occlusion handling, and semantic AR with deep learning. |
| `ai-for-computer-graphics` | Neural rendering, differentiable rendering, inverse rendering, geometry and material estimation, and generative image synthesis for photorealistic graphics. |
| `ai-for-computer-vision` | Image classification, detection, segmentation, vision-language models, generative vision, and efficient deep learning deployment. |
| `ai-for-games` | Procedural content generation, game-playing agents via reinforcement learning, NPC behavior, and generative AI for game assets and narratives. |
| `ai-for-human-robot-interaction` | Multimodal interfaces, natural language instructions, shared autonomy, social robotics, and embodied AI for human-robot collaboration. |
| `ai-for-nlp` | Large language models, text classification, machine translation, question answering, information extraction, and prompt engineering. |
| `ai-for-speech` | Automatic speech recognition, text-to-speech, speaker verification, speech synthesis, and self-supervised speech models. |
| `ai-for-video` | Video understanding, action recognition, video generation, temporal modeling, video captioning, and multimodal video models. |
| `ai-for-virtual-reality` | Natural interaction, intent recognition, multimodal input, foveated rendering, virtual agents, and AI-driven content creation for VR. |
| `ai-for-acoustics` | Machine learning for source localization, room acoustics, bioacoustics, structural health monitoring, and spatial audio. |
| `ai-for-astrobiology` | ML for biosignature detection, life-detection mass spectrometry, extremophile habitats, and mission autonomy in alien environments. |
| `ai-for-astronomy` | Machine learning for survey-scale classification, transient detection, galaxy morphology, light-curve analysis, and telescope scheduling. |
| `ai-for-biophysics` | Machine learning for molecular dynamics, free-energy landscapes, protein-ligand kinetics, single-molecule analysis, and membrane systems. |
| `ai-for-condensed-matter` | Machine learning for phase classification, topological order, Hamiltonian learning, density functional surrogates, and quantum many-body systems. |
| `ai-for-cosmology` | ML for large-scale structure, weak lensing, CMB analysis, 21-cm cosmology, and cosmological parameter inference. |
| `ai-for-microfluidics` | Machine learning for droplet generation, lab-on-a-chip control, cell sorting, reaction optimization, and high-throughput screening. |
| `ai-for-nanotechnology` | ML for nanoparticle design, nanomaterial discovery, nano-architectonics, nanoscale imaging, and nanomanufacturing optimization. |
| `ai-for-optics` | Computational imaging, lens design, wavefront shaping, optical metrology, and inverse scattering with deep learning. |
| `ai-for-particle-physics` | ML for collider event classification, jet tagging, fast detector simulation, neutrino event reconstruction, and new-physics searches. |
| `ai-for-photonics` | Deep learning for photonic device inverse design, metasurfaces, optical communications, and nanophotonic simulation surrogates. |
| `ai-for-planetary-science` | Machine learning for mission data analysis, terrain classification, crater detection, atmospheric retrievals, and exoplanet characterization. |
| `ai-for-aerospace` | Machine learning for aircraft and spacecraft design, aerodynamic optimization, structural health monitoring, satellite operations, and certification of safety-critical aerospace systems. |
| `ai-for-automotive` | AI for automotive design, manufacturing, battery management, ADAS, quality control, and supply-chain optimization across the vehicle lifecycle. |
| `ai-for-aviation` | AI for airline and airport operations, including predictive maintenance, crew and fleet scheduling, disruption recovery, fuel optimization, and safety analytics. |
| `ai-for-drones` | AI for UAV perception, navigation, obstacle avoidance, mission planning, multi-drone coordination, and vision-language drone control. |
| `ai-for-exoskeletons` | AI for wearable exoskeleton and exosuit control, gait and intention recognition, human-robot interaction, rehabilitation, and assistive augmentation. |
| `ai-for-field-robotics` | AI for robots operating in outdoor, unstructured environments such as agriculture, construction, mining, environmental monitoring, and disaster response. |
| `ai-for-industrial-robotics` | Machine learning for factory manipulation, assembly, pick-and-place, force control, sim-to-real, and vision-language-action models in industrial settings. |
| `ai-for-maritime` | AI for maritime autonomous surface ships, route and weather routing optimization, collision avoidance, port logistics, and vessel situational awareness. |
| `ai-for-quality-control` | Machine learning and computer vision for automated inspection, defect detection, statistical process control, and zero-defect manufacturing. |
| `ai-for-rail` | AI for railway infrastructure health, predictive maintenance, train scheduling, energy optimization, and real-time disruption management. |
| `ai-for-smart-manufacturing` | AI for cyber-physical manufacturing, digital twins, real-time process optimization, predictive maintenance, and sustainable Industry 4.0/5.0 systems. |
| `ai-for-warehouse-robotics` | AI for autonomous mobile robots, goods-to-person systems, picking, multi-agent path finding, task allocation, and warehouse traffic management. |
| `ai-for-cooking` | Recipe generation, meal planning, ingredient substitution, food image recognition, and personalized nutrition-aware cooking assistance. |
| `ai-for-event-planning` | Venue and vendor recommendation, guest-list management, scheduling, budget optimization, and group preference aggregation for personal and small events. |
| `ai-for-fitness` | Personalized workout plans, exercise form analysis, pose estimation, wearables, and adaptive recovery for individual fitness. |
| `ai-for-home-automation` | Smart home control, energy management, occupancy prediction, device scheduling, and comfort optimization with reinforcement learning and IoT. |
| `ai-for-legal-assistance` | Legal intake, contract review, plain-language document summarization, form filling, and accessible legal triage for non-experts. |
| `ai-for-lifestyle` | Habit formation, hobby and style recommendations, personal goal coaching, and holistic life-planning agents for everyday decisions. |
| `ai-for-mental-health` | CBT-based chatbots, mood tracking, crisis triage, digital therapeutics, and scalable psychological support for consumers. |
| `ai-for-personal-finance` | Budget optimization, cash-flow forecasting, robo-advisory, credit scoring, and personalized savings and investment guidance for household financial decisions. |
| `ai-for-personal-productivity` | Time management, task prioritization, calendar scheduling, meeting optimization, and personal workflow automation. |
| `ai-for-shopping` | Product discovery, personalized recommendations, price comparison, review summarization, and AI buyer guides for consumer purchases. |
| `ai-for-travel` | Itinerary planning, point-of-interest recommendation, flight and hotel personalization, trip optimization, and conversational travel agents. |
| `ai-for-wellness` | Holistic wellness, sleep, stress, mindfulness, HRV biofeedback, and personalized lifestyle recommendations for everyday well-being. |
| `ai-for-border-security` | Biometric identity verification, contraband and anomaly detection, and multi-sensor fusion at ports of entry. |
| `ai-for-crisis-communication` | Automated situational awareness, rumor detection, multilingual crisis summarization, and public information chatbots. |
| `ai-for-cyber-physical-security` | Securing industrial control systems, SCADA anomaly detection, physical invariants, and cross-layer intrusion detection. |
| `ai-for-cybersecurity` | Network intrusion detection, malware and phishing classification, vulnerability discovery, adversarial ML, and SOC automation. |
| `ai-for-disaster-preparedness` | Hazard risk assessment, early warning systems, scenario simulation, and mitigation planning with AI. |
| `ai-for-emergency-management` | Incident prediction, resource allocation, damage assessment, and generative AI for emergency operations. |
| `ai-for-physical-security` | Perimeter intrusion detection, access control analytics, video anomaly detection, and AI-augmented guard operations. |
| `ai-for-public-safety` | Emergency call dispatch, response-time optimization, situational awareness, and fairness-aware public safety analytics. |
| `ai-for-resilience` | Critical infrastructure resilience, disaster recovery planning, stress testing, and learning-based restoration optimization. |
| `ai-for-search-and-rescue` | UAV and robot search planning, victim detection from imagery and sensors, and SAR mission coordination with AI. |
| `ai-for-surveillance-ethics` | Fairness, privacy, proportionality, and algorithmic accountability for AI surveillance and facial recognition. |
| `ai-for-threat-intelligence` | Cyber threat intelligence extraction, attribution, knowledge graphs, and automated indicator analysis with ML and LLMs. |
| `ai-for-advertising` | Ad creative generation, media buying optimization, dynamic creative optimization, and predictive performance modeling. |
| `ai-for-branding` | Brand strategy, visual identity, brand voice, naming, and AI-assisted brand co-creation with human curation. |
| `ai-for-content-strategy` | Planning, auditing, and orchestrating content portfolios with AI, including generative-engine optimization and cross-platform adaptation. |
| `ai-for-copywriting` | Marketing and advertising copy, email and landing-page text, conversion frameworks, and brand-voice calibration with LLMs. |
| `ai-for-creative-writing` | Co-writing novels, screenplays, and long-form fiction with LLMs, prompt engineering for voice and style, and human-AI revision workflows. |
| `ai-for-digital-marketing` | SEO, SEM, social media, email automation, marketing analytics, and AI-driven personalization across digital channels. |
| `ai-for-influencer-marketing` | Creator discovery, campaign matching, content co-creation, performance prediction, and authenticity measurement for influencer marketing. |
| `ai-for-podcasting` | AI-generated and AI-assisted podcast production, including scriptwriting, voice synthesis, editing, transcription, and show notes. |
| `ai-for-poetry` | Meter, rhyme, and stylistic constraints for AI-generated poetry, with evaluation and human-AI curation. |
| `ai-for-product-design` | Concept generation, design space exploration, prototyping, and engineering handoff with generative AI in product development. |
| `ai-for-storytelling` | Narrative generation, plot planning, character arcs, and worldbuilding with structured LLM workflows. |
| `ai-for-ux-design` | Interaction design, user research, prototyping, and AI UX patterns for human-centered AI products. |
| `ai-for-competency-development` | Competency-based education, skill gap analysis, adaptive credentialing, and AI-driven mastery and portfolio assessment. |
| `ai-for-curriculum-design` | Goal-aligned course sequencing, personalized learning paths, content alignment, adaptive curricula, and standards mapping. |
| `ai-for-educational-assessment` | Automated essay scoring, conversational assessment, LLM rubric grading, feedback generation, and validity and fairness of AI-driven evaluation. |
| `ai-for-educational-games` | Game-based learning, adaptive difficulty, intelligent NPCs, scaffolding, and learning analytics embedded in playful environments. |
| `ai-for-higher-education` | Admissions analytics, retention and completion modeling, student success advising, enrollment planning, and institutional research. |
| `ai-for-language-learning` | AI chatbots for conversation practice, automated writing and pronunciation feedback, CEFR-level adaptation, and second-language acquisition support. |
| `ai-for-learning-analytics` | Learning management system analysis, learner trajectory modeling, early warning systems, engagement dashboards, and educational data mining. |
| `ai-for-lifelong-learning` | Continuous skill development, career-aligned learning pathways, micro-credentials, and AI support for adult and professional learners. |
| `ai-for-pedagogy` | Teacher-AI collaboration, lesson planning, instructional design, feedback generation, and evidence-based teaching practice augmentation. |
| `ai-for-special-education` | Assistive technologies, personalized interventions, augmentative and alternative communication, accessibility, and inclusive learning for learners with disabilities. |
| `ai-for-student-engagement` | Engagement prediction, behavioral analytics, early warning systems, intervention targeting, and motivational feedback. |
| `ai-for-tutoring` | Intelligent tutoring systems, dialogue-based tutoring, error diagnosis, Socratic scaffolding, and personalized next-step hints. |
| `ai-for-air-quality` | Pollutant forecasting, spatiotemporal PM modeling, emission source apportionment, and early warning for air quality. |
| `ai-for-biodiversity` | Automated species detection, acoustic and eDNA monitoring, habitat suitability modeling, and biodiversity trend analysis for conservation. |
| `ai-for-circular-economy` | Material flow optimization, predictive recycling, product lifecycle extension, and circular supply-chain design with AI. |
| `ai-for-conservation-planning` | Spatial prioritization, protected-area design, systematic conservation planning, and trade-off analysis using optimization and ML. |
| `ai-for-coral-reefs` | Coral reef monitoring, bleaching detection, benthic classification, and reef-health assessment from underwater and drone imagery. |
| `ai-for-desertification` | Land degradation and desertification risk mapping, sensitivity assessment, and early warning from remote sensing and ML. |
| `ai-for-ecosystem-restoration` | Monitoring rewilding, forest recovery, wetland restoration, and habitat reconstruction using remote sensing and biodiversity indicators. |
| `ai-for-glaciology` | Glacier mapping, surface mass balance estimation, snow/ice classification, and climate-change impact assessment. |
| `ai-for-natural-hazards` | Multi-hazard susceptibility mapping and early warning for landslides, floods, wildfires, and land subsidence with ML and remote sensing. |
| `ai-for-ocean-conservation` | Marine protected area monitoring, illegal fishing detection, species tracking, and ocean health assessment from satellite and vessel data. |
| `ai-for-waste-management` | Waste classification, automated sorting, route optimization, recycling quality, and lifecycle assessment with ML and robotics. |
| `ai-for-wetlands` | Wetland mapping, inundation dynamics, cover-type classification, and hydrological trend monitoring from satellite time series. |
| `ai-for-change-management` | Stakeholder sentiment monitoring, adoption analytics, training personalization, and AI-assisted transformation communications. |
| `ai-for-compliance` | Regulatory mapping, policy gap analysis, automated control testing, and AI-assisted compliance monitoring. |
| `ai-for-innovation-management` | Idea generation, R&D portfolio prioritization, trend forecasting, and AI-enabled new product development. |
| `ai-for-insurance` | Underwriting triage, claims automation, fraud detection, and AI-assisted pricing and reserving. |
| `ai-for-knowledge-management` | Semantic knowledge search, enterprise RAG, expertise mining, and AI-assisted capture of institutional tacit knowledge. |
| `ai-for-legal-operations` | Contract review, clause extraction, matter intake, and AI-assisted legal workflow automation. |
| `ai-for-management-consulting` | Accelerate diagnostic research, market sizing, client synthesis, and GenAI-assisted advisory workflows while managing epistemic risk. |
| `ai-for-operations-management` | Process mining, service-level optimization, quality control, and AI-driven operational decision support. |
| `ai-for-project-management` | Schedule and cost forecasting, risk triage, resource optimization, and AI-driven project health monitoring. |
| `ai-for-real-estate` | Automated valuation, market analysis, lead matching, and AI-assisted property due diligence. |
| `ai-for-risk-management` | Credit, market, operational, and emerging risk modeling with ML and scenario analysis. |
| `ai-for-strategy` | Data-driven strategy formulation, competitive scenario modeling, market sensing, and AI-augmented strategic decision-making. |
| `ai-for-behavioral-science` | Computational modeling of human behavior, n-of-1 and ecological momentary assessment, digital interventions, and experimentally validated behavior change. |
| `ai-for-cancer-bioinformatics` | Multi-omics integration, tumor subtyping, biomarker discovery, and precision oncology using AI. |
| `ai-for-clinical-informatics` | AI-enabled clinical decision support, EHR integration, workflow optimization, and evaluation in real-world care settings. |
| `ai-for-cognitive-science` | Computational models of perception, memory, language, reasoning, and human-like cognition, bridging AI and psychological theory. |
| `ai-for-digital-health` | Consumer-facing health apps, wearable biosensors, remote monitoring, patient portals, and data-driven digital wellness interventions. |
| `ai-for-global-health` | AI for disease burden, healthcare systems, and health equity in low- and middle-income countries and resource-limited settings. |
| `ai-for-health-economics` | Cost-effectiveness, health technology assessment, demand and pricing models, and machine learning for health outcomes research. |
| `ai-for-health-informatics` | Electronic health records, clinical data standards, interoperability, and AI-enabled analytics for healthcare delivery and research. |
| `ai-for-health-services-research` | AI for healthcare access, quality, utilization, policy, workforce, and health-system performance. |
| `ai-for-immunoinformatics` | Machine learning for immune repertoire analysis, epitope prediction, vaccine design, and immunotherapy optimization. |
| `ai-for-neuroinformatics` | Data science for brain imaging, neural signals, connectomics, and computational neuroscience workflows. |
| `ai-for-precision-public-health` | Subpopulation-targeted prevention, genomics-guided public health, geospatial risk modeling, and equitable intervention targeting. |
| `ai-for-art-history` | Computer vision, deep learning, and vision-language models for style classification, iconography, provenance, and quantitative art history. |
| `ai-for-cultural-heritage` | Machine learning and deep learning for the digitization, documentation, analysis, and sustainable management of tangible and intangible cultural heritage. |
| `ai-for-digital-humanities` | Machine learning, NLP, and network analysis for historical texts, archives, languages, and multimodal humanities collections. |
| `ai-for-ethnomusicology` | Computational analysis of field recordings, oral musical traditions, tuning systems, and cross-cultural musical patterns using MIR and machine learning. |
| `ai-for-folklore` | Computational folkloristics, motif and tale-type detection, and large-scale narrative analysis of folk tales, legends, and oral traditions. |
| `ai-for-heritage-tourism` | Recommender systems, itinerary planning, visitor behavior modeling, and personalized cultural heritage experiences for sustainable tourism. |
| `ai-for-literary-studies` | Computational stylistics, authorship attribution, genre and style analysis, and interpretive NLP for literary texts and corpora. |
| `ai-for-museum-collections` | Computer vision, natural language processing, and metadata enrichment for cataloging, searching, and interpreting museum and archive collections. |
| `ai-for-mythology` | Computational mythography, knowledge graphs of mythological figures, structural analysis of myths, and cross-cultural narrative comparison. |
| `ai-for-oral-history` | Speech recognition, diarization, natural language processing, and generative AI for transcribing, indexing, and exploring oral history archives. |
| `ai-for-preservation` | Predictive monitoring, environmental risk assessment, digital twins, and preventive conservation for built heritage and cultural collections. |
| `ai-for-restoration` | Digital inpainting, virtual restoration, style-aware reconstruction, and diffusion models for repairing artworks, murals, and manuscripts. |
| `ai-for-algorithms` | Learning-augmented algorithms, learned data structures, and ML-guided design for search, routing, scheduling, and data-intensive pipelines. |
| `ai-for-approximation-algorithms` | Learning-augmented approximation, learned heuristics for NP-hard maximization and CSPs, and data-driven rounding. |
| `ai-for-automated-reasoning` | Learning to guide proof search, premise selection, tactic prediction, and combining LLMs with symbolic reasoners. |
| `ai-for-computational-complexity` | Using machine learning to predict, characterize, and understand the complexity of computational problems, reductions, and hardness proxies. |
| `ai-for-constraint-programming` | ML for constraint learning, search heuristics, model acquisition, and combining CP solvers with neural predictors. |
| `ai-for-discrete-optimization` | Learning-augmented branch-and-bound, primal heuristics, GNNs for combinatorial optimization, and data-driven algorithm configuration. |
| `ai-for-formal-methods` | Neuro-symbolic verification, LLM-assisted autoformalization, and learned heuristics for theorem provers and model checkers. |
| `ai-for-logic` | Neuro-symbolic reasoning, learning logical rules and constraints, probabilistic logics, and SAT/SMT/ASP guided by ML. |
| `ai-for-program-synthesis` | Neural and symbolic program synthesis from examples, sketches, and natural language, including neurosymbolic and LLM-based code generation. |
| `ai-for-satisfiability` | ML-enhanced SAT/SMT/QSAT solvers, end-to-end neural solvers like NeuroSAT, and learned branching and restart heuristics. |
| `ai-for-software-verification` | ML for test generation, coverage closure, bug localization, static analysis, and verifying code produced by LLMs. |
| `ai-for-type-theory` | ML-guided tactic prediction, premise selection, and synthesis in dependent type theories and proof assistants. |
| `ai-for-advanced-packaging` | Co-design of 2.5D/3D chiplets, interconnect routing, signal-integrity-aware placement, and package-thermal optimization. |
| `ai-for-chip-design` | ML for RTL generation, EDA scripting, floorplanning, placement, routing, timing optimization, and analog/mixed-signal design. |
| `ai-for-edge-accelerators` | NPU/TPU/FPGA edge accelerator design, benchmarking, mapping, and optimization for low-latency, energy-efficient inference. |
| `ai-for-embedded-ai` | TinyML, on-device inference, quantization, neural architecture search, and co-optimization for microcontrollers and DSPs. |
| `ai-for-hardware-security` | ML for side-channel analysis, hardware Trojan and PUF detection, supply-chain assurance, and secure accelerator design. |
| `ai-for-integrated-photonics` | Inverse design, layout generation, and fabrication-aware optimization of silicon-photonic and photonic-integrated-circuit components. |
| `ai-for-memristors` | Crossbar array modeling, compute-in-memory mapping, device variability learning, and memristor-based AI accelerator co-design. |
| `ai-for-neuromorphic-hardware` | Spiking neural network training, SNN-to-chip mapping, event-based processing, and co-design with analog/mixed-signal neuromorphic platforms. |
| `ai-for-photonic-hardware` | Photonic AI accelerators, optical neural networks, optoelectronic co-design, and programming of photonic tensor cores. |
| `ai-for-quantum-hardware` | ML-driven qubit control, calibration, error decoding, and quantum processor design for superconducting, trapped-ion, and neutral-atom systems. |
| `ai-for-spintronics` | ML for magnetic material discovery, skyrmion and MRAM device modeling, spin-orbit torque optimization, and spin-wave logic. |
| `ai-for-thermal-design` | ML surrogates for electronics cooling, data-center thermal control, heat-sink and package thermal co-design, and CFD emulation. |
| `ai-for-allergy-immunology` | Machine learning for asthma phenotyping and exacerbation prediction, allergic rhinitis and food/drug allergy risk, anaphylaxis, and primary immunodeficiency screening. |
| `ai-for-anesthesiology` | Machine learning for preoperative risk stratification, intraoperative hemodynamic monitoring, anesthetic depth, postoperative nausea and pain, and closed-loop anesthesia. |
| `ai-for-endocrinology` | Machine learning for diabetes prediction and glucose forecasting, thyroid nodule risk stratification, adrenal and pituitary disorders, and bone mineral metabolism. |
| `ai-for-hematology` | Machine learning for blood cell morphology, leukemia and lymphoma classification, thrombosis and bleeding risk, transfusion optimization, and stem-cell transplant outcomes. |
| `ai-for-infectious-disease` | Machine learning for pathogen identification, antimicrobial resistance prediction, sepsis early warning, and infectious disease outbreak surveillance. |
| `ai-for-nephrology` | Machine learning for chronic kidney disease progression, acute kidney injury prediction, dialysis adequacy, kidney transplant outcomes, and renal pathology image analysis. |
| `ai-for-orthopedics` | Machine learning for fracture detection and classification, osteoarthritis grading, joint replacement outcomes, spine analysis, and sports injury risk. |
| `ai-for-pain-management` | Machine learning for chronic pain phenotyping, opioid and analgesic response prediction, procedural guidance, and patient self-management and monitoring. |
| `ai-for-physical-medicine` | Machine learning for electrodiagnostic studies, musculoskeletal ultrasound, gait and motion analysis, prosthetics/orthotics, and functional assessment in physiatry. |
| `ai-for-plastic-surgery` | Machine learning for aesthetic and reconstructive surgical planning, facial analysis, flap monitoring, wound assessment, and patient-reported outcomes. |
| `ai-for-rehabilitation` | Machine learning for stroke, spinal cord, and traumatic brain injury rehabilitation, robotic and virtual-reality therapy, telerehabilitation, and wearable sensor monitoring. |
| `ai-for-rheumatology` | Machine learning for autoimmune disease diagnosis and phenotyping, flare prediction, treatment response in RA and SLE, and imaging-based joint inflammation scoring. |
| `ai-for-ai-ethics` | Fairness, accountability, transparency, privacy, and value alignment in AI systems, including bias auditing, model cards, and stakeholder deliberation. |
| `ai-for-ai-governance` | Risk management, accountability, lifecycle governance, standards, and multi-stakeholder oversight for trustworthy and responsible AI organizations. |
| `ai-for-ai-policy` | Regulatory analysis, risk classification, standards mapping, policy evaluation, and evidence synthesis for national and international AI governance. |
| `ai-for-ai-safety` | Alignment, robustness, interpretability, red teaming, monitoring, and safe deployment of AI systems, especially large language and agentic models. |
| `ai-for-computational-design` | Differentiable simulation, topology optimization, CAD-aware generative models, and solver-in-the-loop co-design for architecture, products, and structures. |
| `ai-for-digital-twin-simulation` | High-fidelity virtual replicas, real-time synchronization, physics-informed and data-driven simulation, and AI training environments for cyber-physical systems. |
| `ai-for-future-of-work` | Automation and augmentation analysis, skill demand forecasting, workforce transitions, algorithmic management, and human-centered labor market policy. |
| `ai-for-generative-engineering` | Diffusion, VAE, and generative inverse design for engineering concepts, constraint-aware generation, and performance-conditioned shape and material synthesis. |
| `ai-for-human-centered-ai` | Human-AI interaction, explainability, trust, feedback loops, participatory design, and human-in-the-loop ML to keep people at the center of AI systems. |
| `ai-for-responsible-innovation` | Anticipatory governance, ethical deliberation, stakeholder engagement, regulatory foresight, and impact assessment for emerging AI technologies. |
| `ai-for-synthetic-data` | Generative models, differential privacy, tabular/image/text synthesis, and utility-privacy evaluation for creating realistic synthetic datasets. |
| `ai-for-tech-forecasting` | Patent and publication analysis, trend extrapolation, expert elicitation, and ML models for predicting technological progress and emerging AI capabilities. |
| `ai-for-aging` | Machine learning for geriatric health monitoring, aging-in-place, fall prevention, cognitive and social support, and age-friendly AI design. |
| `ai-for-child-health` | Machine learning for pediatric diagnostics, developmental surveillance, pediatric AI readiness, and risk stratification for children. |
| `ai-for-dementia-care` | Machine learning for cognitive impairment screening, dementia risk stratification, voice and EHR analytics, and caregiver support. |
| `ai-for-disability-inclusion` | Accessible AI, disability-aware bias evaluation, inclusive design, and assistive technologies that respect the rights and agency of people with disabilities. |
| `ai-for-humanitarian-aid` | AI across the crisis management cycle: needs assessment, resource allocation, routing, damage assessment, and early warning for disaster response. |
| `ai-for-hunger-relief` | AI/ML for food-security early warning, acute food-insecurity forecasting, remote-sensing crop monitoring, and targeted food assistance. |
| `ai-for-maternal-health` | Machine learning for maternal risk stratification, preterm birth prediction, obstetric decision support, and neonatal outcome forecasting. |
| `ai-for-mental-health-services` | LLM and multimodal mental health screening, CBT chatbots, psychosocial risk assessment, and clinical interview support. |
| `ai-for-palliative-care` | Machine learning for prognostication, symptom management, hospice suitability, advance care planning, and ethical decision support in end-of-life care. |
| `ai-for-poverty-alleviation` | Machine learning for poverty mapping, consumption estimation, proxy means testing, and targeted social protection in low-resource settings. |
| `ai-for-refugees` | Machine learning for forced-displacement forecasting, refugee camp mapping, asylum-flow prediction, and humanitarian response planning. |
| `ai-for-rural-health` | AI-driven diagnostics, telemedicine, rural health equity, and resource allocation for underserved and remote populations. |
| `ai-for-data-journalism` | Using AI to find stories in datasets, fact-check claims, generate visualizations, and produce data-driven reporting. |
| `ai-for-document-design` | Automating layout, typography, templates, and multi-format rendering of reports, certificates, and proposals. |
| `ai-for-infographics` | Generating data-rich infographics and visual stories from documents, tables, and natural-language prompts. |
| `ai-for-knowledge-design` | Designing knowledge architectures, taxonomies, ontologies, and agent-facing knowledge layers for organizations. |
| `ai-for-open-science` | Reproducible research agents, open-source workbenches, provenance tracking, and computational reproducibility with AI. |
| `ai-for-policy-briefs` | Converting scientific evidence and legislative text into concise, actionable policy briefs and impact analyses. |
| `ai-for-public-engagement` | Conversational agents, citizen science, public consultations, and participatory science supported by LLMs and interactive AI. |
| `ai-for-research-communication` | Drafting manuscripts, abstracts, cover letters, response-to-reviewers, and translating findings across disciplines with LLMs. |
| `ai-for-science-communication` | Plain-language summaries, research storytelling, audience adaptation, and ethical, evidence-based use of generative AI for public-facing science. |
| `ai-for-technical-blogs` | Planning, drafting, SEO-optimizing, and reviewing technical blog posts and tutorials with LLMs. |
| `ai-for-visual-communication` | Generating and refining posters, slides, brand assets, and visual narratives with diffusion models and design tools. |
| `ai-for-white-papers` | Authoring long-form, evidence-based white papers and thought-leadership documents grounded in verified sources. |
| `ai-for-comparative-genomics` | Cross-species and population genome comparison, orthology inference, phylogenomics, selection scans, and pan-genome analysis. |
| `ai-for-epigenomics` | DNA methylation, histone modifications, chromatin accessibility, enhancer-promoter interactions, and deep learning models of gene regulation. |
| `ai-for-functional-genomics` | Predicting gene regulatory function from sequence and epigenomic data, mapping cis-regulatory elements, and interpreting non-coding variants. |
| `ai-for-immunogenomics` | MHC and peptide binding prediction, TCR/BCR repertoire analysis, epitope and neoantigen prediction, and immunoinformatics. |
| `ai-for-lipidomics` | LC-MS/MS lipid species quantification, structural isomer resolution, lipid class normalization, and predictive modeling of lipid phenotypes. |
| `ai-for-metabolomics` | Mass spectrometry and NMR metabolite profiling, annotation, pathway analysis, normalization, and machine learning for biomarker discovery. |
| `ai-for-metagenomics` | 16S rRNA and shotgun microbial community profiling, taxonomic and functional prediction, MAG binning, and microbiome-host association modeling. |
| `ai-for-proteomics` | Mass spectrometry protein identification and quantification, DDA/DIA workflows, post-translational modifications, and AI-driven peptide property prediction. |
| `ai-for-single-cell` | Single-cell transcriptomics, epigenomics, proteomics, and multi-omics integration, cell type annotation, trajectory inference, and foundation models. |
| `ai-for-spatial-omics` | Spatially resolved transcriptomics and proteomics, cell segmentation, neighborhood analysis, and integration with imaging data. |
| `ai-for-structural-genomics` | 3D genome organization, Hi-C analysis, protein structure prediction with deep learning, and multiscale structural modeling. |
| `ai-for-transcriptomics` | Bulk and single-cell RNA-seq analysis, normalization, clustering, differential expression, splicing, and foundation models for gene expression. |
| `ai-for-aerospace-engineering` | AI for aerodynamic design, propulsion, structural analysis, flight dynamics, GNC, and certification of aerospace vehicles. |
| `ai-for-biomedical-engineering` | AI for medical devices, wearable biosensors, biomechanics, neural engineering, tissue engineering, and clinical diagnostics. |
| `ai-for-chemical-engineering` | AI for process design, optimization, control, reaction engineering, materials discovery, and digital chemical plants. |
| `ai-for-civil-engineering` | Machine learning for structural health monitoring, geotechnical prediction, transportation systems, water resources, and resilient infrastructure. |
| `ai-for-electrical-engineering` | AI for power systems, smart grids, renewable integration, power electronics, fault diagnosis, and energy management. |
| `ai-for-environmental-engineering` | AI for water and wastewater treatment, air quality, climate modeling, waste management, and environmental monitoring. |
| `ai-for-industrial-engineering` | AI for production planning, scheduling, quality control, ergonomics, operations research, and process improvement. |
| `ai-for-mechanical-engineering` | AI for mechanical design, predictive maintenance, digital twins, dynamic systems, and manufacturing process optimization. |
| `ai-for-petroleum-engineering` | AI for reservoir characterization, production optimization, well placement, drilling, and digital oilfield twins. |
| `ai-for-software-engineering` | AI for code generation, testing, debugging, program repair, code review, and design assistance. |
| `ai-for-systems-engineering` | AI for architecting complex systems, model-based systems engineering (MBSE), requirements analysis, trade studies, and verification. |
| `ai-for-telecommunications` | AI for wireless networks, 5G/6G, network optimization, traffic forecasting, security, and edge intelligence. |
| `ai-for-biomarkers` | Machine learning for omics-based biomarker discovery, sparse signature selection, multi-modal integration, and clinical validation. |
| `ai-for-clinical-trials` | Machine learning for clinical-trial design, patient eligibility, cohort selection, outcome prediction, and operational monitoring across the trial lifecycle. |
| `ai-for-cohort-studies` | Machine learning for risk prediction, confounding control, survival analysis, and biomarker discovery in prospective and retrospective cohort studies. |
| `ai-for-evidence-synthesis` | AI and LLMs for systematic review automation, risk-of-bias assessment, evidence mapping, and trustworthy synthesis of research findings. |
| `ai-for-longitudinal-studies` | Machine learning and deep learning for repeated measurements, time-varying covariates, missing data, trajectories, and outcomes in longitudinal cohorts and EHR data. |
| `ai-for-meta-analysis` | Machine learning and LLMs for automating literature search, screening, data extraction, effect-size estimation, and heterogeneity assessment in meta-analyses. |
| `ai-for-observational-studies` | Causal machine learning for treatment-effect estimation, propensity scoring, confounding adjustment, and sensitivity analysis in observational data. |
| `ai-for-patient-reported-outcomes` | Machine learning for predicting, personalizing, and reducing the burden of patient-reported outcome measures and PRO-based treatment decisions. |
| `ai-for-randomized-trials` | Machine learning for heterogeneous treatment effects, covariate adjustment, adaptive randomization, and efficient inference in randomized controlled trials. |
| `ai-for-real-world-evidence` | Machine learning for extracting, validating, and synthesizing real-world evidence from EHRs, claims, registries, and wearables for regulatory and clinical decisions. |
| `ai-for-registry-studies` | Machine learning for patient registries, disease surveillance, regulatory-grade real-world evidence, and longitudinal outcome tracking. |
| `ai-for-synthetic-controls` | Machine learning for constructing, validating, and extending synthetic and virtual control arms from observational data to augment clinical and policy evaluation. |
| `ai-for-data-curation` | Automated selection, cleaning, labeling, augmentation, and documentation of datasets to produce high-quality, FAIR, and reusable ML data assets. |
| `ai-for-data-discovery` | Intelligent dataset search, metadata enrichment, schema inference, and conversational data catalog exploration to find the right data quickly. |
| `ai-for-data-ethics` | Fairness, accountability, transparency, data dignity, consent, and responsible data use in ML pipelines and AI systems. |
| `ai-for-data-governance` | Automated policy enforcement, metadata management, data lineage, stewardship, and AI-driven regulatory compliance for enterprise data governance. |
| `ai-for-data-marketplaces` | AI for data and model discovery, pricing, valuation, matching, trust, and governance in data-sharing marketplaces and AI model markets. |
| `ai-for-data-monetization` | Data valuation, pricing, data products, marketplaces, and revenue allocation for turning data assets into measurable business value. |
| `ai-for-data-observability` | ML-driven monitoring of data freshness, schema drift, volume anomalies, lineage breaks, and pipeline health to ensure reliable data operations. |
| `ai-for-data-privacy` | Differential privacy, federated learning, homomorphic encryption, PETs, and privacy-preserving ML for sensitive data. |
| `ai-for-data-provenance` | Lineage tracking, W3C PROV, reproducible ML pipelines, experiment tracking, and provenance for explainable and trustworthy AI. |
| `ai-for-data-quality` | Automated profiling, anomaly detection, data cleaning, imputation, validation, and continuous data quality monitoring for ML and analytics. |
| `ai-for-data-security` | Adversarial robustness, data poisoning detection, access control, threat detection, and AI-driven security for ML training and inference data. |
| `ai-for-data-sharing` | Federated learning, data sharing incentives, interoperability, trust, and privacy-preserving collaboration for shared data ecosystems. |
| `ai-for-5g` | AI/ML for 5G RAN optimization, network slicing, beam management, mobility, and core automation. |
| `ai-for-6g` | AI-native 6G architectures, semantic communications, integrated sensing and communication, reconfigurable intelligent surfaces, and distributed learning. |
| `ai-for-edge-computing` | Model compression, inference offloading, task placement, federated learning, and MLOps at the network edge. |
| `ai-for-fog-computing` | AI for hierarchical fog resource management, task scheduling, load balancing, latency optimization, and IoT-fog-cloud orchestration. |
| `ai-for-iot` | TinyML, edge AI, anomaly detection, device fingerprinting, and predictive maintenance for IoT systems. |
| `ai-for-network-management` | AIOps for network monitoring, anomaly detection, root-cause analysis, configuration management, and predictive maintenance. |
| `ai-for-network-optimization` | Graph neural networks, deep reinforcement learning, traffic engineering, resource allocation, and learning-augmented optimization for routing, load balancing, and network design. |
| `ai-for-network-security` | Intrusion detection, malware classification, anomaly detection, adversarial defenses, and threat intelligence using ML and LLMs. |
| `ai-for-optical-networks` | ML for optical performance monitoring, QoT estimation, traffic prediction, nonlinearity compensation, and optical layer provisioning. |
| `ai-for-satellite-communications` | ML for satellite link prediction, beam hopping, resource allocation, non-terrestrial networks, and onboard edge AI. |
| `ai-for-software-defined-networks` | ML-driven traffic classification, routing, QoS/QoE prediction, resource management, and security in SDN control and data planes. |
| `ai-for-wireless-communications` | ML for channel estimation, modulation recognition, MIMO, spectrum sensing, and end-to-end physical-layer design. |
| `ai-for-agricultural-economics` | Machine learning and econometric ML for farm decision support, risk, policy, market analysis, adoption, and the economics of digital agriculture. |
| `ai-for-agricultural-robots` | Perception, motion planning, and control for autonomous robots that weed, spray, scout, and harvest in field and greenhouse environments. |
| `ai-for-aquaculture` | Machine learning for water quality, feeding, disease, and stock management in fish, shrimp, and shellfish farming. |
| `ai-for-crop-protection` | Machine and deep learning for detecting crop diseases, pests, weeds, and abiotic stresses and for supporting timely, targeted protection decisions. |
| `ai-for-dairy` | Machine learning for health, fertility, behaviour, and production monitoring in dairy cattle and dairy farm decision support. |
| `ai-for-irrigation` | Machine learning for predicting crop water demand, scheduling irrigation, and optimising water use through IoT and weather data integration. |
| `ai-for-livestock` | Machine learning for health, behaviour, welfare, grazing, and reproduction across cattle, pigs, sheep, goats, and other farm animals. |
| `ai-for-pest-management` | Machine and deep learning for pest detection, identification, population monitoring, and integrated pest management decision support. |
| `ai-for-plant-breeding` | Genomic selection, phenotype prediction, multi-environment trial analysis, and marker-assisted breeding with machine and deep learning. |
| `ai-for-poultry` | AI for flock health, welfare, behaviour, environmental control, and productivity in broiler, layer, and turkey production. |
| `ai-for-soil-health` | Machine learning for predicting soil carbon, nutrients, biology, compaction, erosion risk, and overall soil health from sensors and remote sensing. |
| `ai-for-viticulture` | AI for vineyard monitoring, grape and canopy sensing, disease detection, yield and quality prediction, and harvest decision support. |
| `ai-for-budgeting` | Public expenditure forecasting, budget allocation optimization, fiscal scenario analysis, program-cost modeling, and spending anomaly detection. |
| `ai-for-civic-tech` | Digital participation, deliberation, civic engagement, public comment analysis, and participatory budgeting tools powered by AI. |
| `ai-for-e-government` | Chatbots and virtual assistants, proactive public services, document automation, eligibility screening, and responsible AI in digital government. |
| `ai-for-permitting` | Automated permit intake, plan review, code compliance checks, application completeness screening, and permit workflow optimization. |
| `ai-for-public-records` | Automated records classification, sensitivity review, metadata enrichment, archival appraisal, and access to digital government archives. |
| `ai-for-public-transport` | Ridership prediction, service scheduling, bus and rail dispatch optimization, disruption recovery, and multi-modal transit analytics. |
| `ai-for-public-utilities` | Smart grid load forecasting, water and energy demand prediction, asset maintenance, leak and outage detection, and resource allocation. |
| `ai-for-social-services` | Eligibility screening, benefits triage, case management support, risk stratification, and resource matching for social care and public assistance. |
| `ai-for-taxation` | Tax compliance risk scoring, fraud and evasion detection, audit selection, taxpayer assistance, and revenue forecasting. |
| `ai-for-urban-planning` | Spatial plan generation, land-use optimization, urban digital twins, scenario simulation, and participatory planning analytics. |
| `ai-for-veterans-services` | Claims processing, benefits eligibility, health risk identification, veteran-centered care coordination, and administrative automation at VA and related agencies. |
| `ai-for-zoning` | Zoning code interpretation, compliance checking, variance analysis, automated answers to zoning questions, and land-use regulation analytics. |
| `ai-for-charging-infrastructure` | Machine learning for EV charging demand forecasting, station scheduling, load balancing, and grid-integrated charging control. |
| `ai-for-demand-response` | Machine learning for load flexibility estimation, demand response program design, virtual power plant dispatch, and dynamic pricing. |
| `ai-for-distributed-energy` | Machine learning and multi-agent methods for DER forecasting, microgrid optimization, peer-to-peer trading, and prosumer coordination. |
| `ai-for-electric-vehicles` | Machine learning for battery management, range and energy consumption prediction, predictive maintenance, and EV powertrain optimization. |
| `ai-for-energy-storage` | Machine learning for battery state estimation, degradation modeling, storage dispatch, and energy storage asset optimization. |
| `ai-for-energy-trading` | Machine learning for electricity price forecasting, algorithmic trading, arbitrage, and bidding in day-ahead, intraday, and balancing markets. |
| `ai-for-gas-utilities` | Machine learning for natural gas demand forecasting, pipeline leak detection, compressor optimization, and asset integrity. |
| `ai-for-grid-resilience` | Machine learning for outage prediction, storm hardening, restoration planning, and cyber-physical resilience of power systems. |
| `ai-for-renewable-energy` | Machine learning for solar, wind, and other renewable energy forecasting, resource assessment, yield optimization, and predictive O&M. |
| `ai-for-smart-grid` | AI and machine learning for load and renewable forecasting, grid state estimation, optimal power flow, and smart-grid control. |
| `ai-for-wastewater` | Machine learning for process monitoring, anomaly detection, influent forecasting, and control in wastewater treatment plants. |
| `ai-for-water-utilities` | Machine learning for water demand forecasting, leak detection, quality monitoring, pump scheduling, and smart water distribution. |
| `ai-for-building-operations` | Smart building control, energy optimization, occupant-centric HVAC and lighting, and IoT-BMS integration for operational performance. |
| `ai-for-city-modeling` | Urban digital twins, 3D city reconstruction, generative city models, and AI-driven urban simulation for planning and operations. |
| `ai-for-construction-management` | BIM-NLP integration, 4D/5D digital twins, computer-vision progress monitoring, and AI-driven scheduling and cost control for construction. |
| `ai-for-facilities-management` | Predictive maintenance, fault detection, digital twins, and AI-enabled asset lifecycle management for built facilities. |
| `ai-for-land-use` | Remote sensing, multi-source data fusion, functional-zone mapping, and neural-symbolic planning for land-use analysis and policy. |
| `ai-for-lease-management` | NLP-based lease abstraction, clause extraction, compliance tracking, and predictive analytics for commercial and residential lease portfolios. |
| `ai-for-portfolio-optimization` | Diversification, risk-return balancing, rebalancing strategies, and generative-AI analytics for real estate and mixed-asset portfolios. |
| `ai-for-property-valuation` | Automated valuation models, hedonic pricing, spatial machine learning, and deep learning for residential and commercial property appraisal. |
| `ai-for-real-estate-investment` | Predictive analytics, investment screening, REIT return forecasting, and risk-adjusted underwriting for real estate investment decisions. |
| `ai-for-site-selection` | Geospatial ML, graph neural networks, urban knowledge graphs, and location analytics for retail, logistics, and facility siting. |
| `ai-for-tenant-experience` | Personalization, occupancy analytics, indoor environmental quality, and tenant engagement for workplace and residential environments. |
| `ai-for-urban-development` | GeoAI, spatial modeling, generative urban design, and scenario simulation for sustainable, equitable, and data-driven urban development. |
| `ai-for-defect-detection` | Computer vision, anomaly detection, and segmentation for automated inspection of surface, PCB, casting, and assembly defects in manufacturing quality control. |
| `ai-for-digital-manufacturing` | AI-driven digital twins, virtual commissioning, real-time simulation, and lifecycle data integration for smart, connected factories. |
| `ai-for-discrete-manufacturing` | Machine learning for assembly, machining, electronics, and automotive part production: process planning, scheduling, robotic assembly, and work-in-progress tracking. |
| `ai-for-factory-automation` | ML-integrated PLCs, edge controllers, motion control, robot programming, and real-time AI inference on the shop floor. |
| `ai-for-industrial-iot` | Industrial Internet of Things, edge-fog-cloud architectures, and AI for real-time monitoring, predictive maintenance, and secure shop-floor connectivity. |
| `ai-for-lean-manufacturing` | Data-driven waste elimination, value stream mapping, bottleneck detection, and Kaizen prioritization for flow, pull, and just-in-time systems. |
| `ai-for-manufacturing-analytics` | KPI dashboards, OEE analysis, descriptive-to-prescriptive analytics, and association mining for manufacturing performance management. |
| `ai-for-predictive-quality` | In-process quality forecasting, virtual metrology, and causal quality models that predict final part quality from machine and sensor data before completion. |
| `ai-for-process-manufacturing` | Machine learning for continuous and batch chemical, pharmaceutical, food, and materials processes: recipe optimization, soft sensors, advanced process control, and real-time quality prediction. |
| `ai-for-root-cause-analysis` | Knowledge graphs, causal discovery, graph neural networks, and SHAP-based diagnostics for identifying fault origins and propagations in complex systems. |
| `ai-for-six-sigma` | ML-augmented DMAIC for defect reduction, statistical process control, capability analysis, and automated root-cause prioritization in quality improvement. |
| `ai-for-total-productive-maintenance` | AI and IIoT for autonomous maintenance, OEE improvement, zero-breakdown programs, and condition-based monitoring across the eight TPM pillars. |
| `ai-for-additive-manufacturing` | Machine learning for powder-bed fusion, directed energy deposition, in-situ monitoring, defect detection, build simulation, and process parameter optimization in additive manufacturing. |
| `ai-for-casting` | Machine learning for sand, investment, die, and continuous casting: defect prediction, mold filling, solidification, microstructure, and process optimization. |
| `ai-for-coatings` | Machine learning for coating formulation, deposition, thickness, microstructure, adhesion, corrosion protection, and service-life prediction. |
| `ai-for-composites-manufacturing` | Machine learning for automated fiber placement, tape laying, resin infusion, cure monitoring, defect detection, and process optimization in composite part manufacturing. |
| `ai-for-corrosion-engineering` | Machine learning for corrosion rate prediction, risk-based inspection, cathodic protection, coating lifetime, EIS interpretation, and materials selection. |
| `ai-for-metal-forming` | Machine learning for sheet-metal stamping, deep drawing, forging, rolling, extrusion, springback prediction, die design, and forming-limit prediction. |
| `ai-for-nanomanufacturing` | Machine learning for nanoscale fabrication, roll-to-roll processing, nanoimprint lithography, self-assembly, nanoscale metrology, and process control. |
| `ai-for-polymer-processing` | Machine learning for extrusion, injection molding, blow molding, compounding, mixing, and polymer recycling process optimization and quality control. |
| `ai-for-semiconductor-manufacturing` | Machine learning for semiconductor fabrication yield enhancement, wafer defect detection, equipment fault classification, process control, and advanced lithography/etch modeling. |
| `ai-for-surface-engineering` | Machine learning for surface modification processes: thermal spray, laser cladding/peening, shot peening, plasma electrolytic oxidation, surface texturing, and residual stress optimization. |
| `ai-for-textile-manufacturing` | Machine learning for yarn, fabric, and garment manufacturing: spinning, weaving, knitting, dyeing, finishing, quality inspection, and production optimization. |
| `ai-for-welding` | Machine learning for arc, laser, and resistance welding: penetration prediction, defect detection, bead geometry, process monitoring, and parameter optimization. |

## Workflows (786)

### Research Workflows (15)

| Workflow | Description |
|----------|-------------|
| `/reproducibility` | Set up seeds, config logging, environment capture |
| `/reproducibility-checklist` | Audit project for reproducibility gaps |
| `/experiment-tracking` | Set up structured experiment tracking |
| `/data-management` | Set up dataset versioning and leak-free splits |
| `/paper-code-release` | Prepare code for public release |
| `/paper-submission-prep` | Finalize repo for paper submission |
| `/ablation-study` | Design and run systematic ablation study |
| `/tdv-pretrain` | Run TDV pretraining on surgical video |
| `/surgical-mot-eval` | Evaluate MOT models on CholecTrack20 |
| `/lora-finetune` | Configure and run LoRA fine-tuning |
| `/pretrain-and-evaluate` | Full pretrain → detect → eval pipeline |
| `/continual-learning` | Session start/end handoff protocol |
| `/deep-research` | Systematic web research and deep reasoning workflow |
| `/wandb-experiment` | Set up WandB tracking |

### SWE Workflows (8)

| Workflow | Description |
|----------|-------------|
| `/code-quality` | Set up formatting, linting, type checking |
| `/code-review` | Systematic ML code review |
| `/testing-strategy` | Design and implement test suite |
| `/dependency-management` | Manage Python dependencies and lock files |
| `/ci-cd-setup` | Set up GitHub Actions CI/CD |
| `/pre-commit-setup` | Install pre-commit hooks with ruff |
| `/release-checklist` | Create a versioned release |
| `/refactor-extract-module` | Extract code into separate module |

### Infrastructure Workflows (5)

| Workflow | Description |
|----------|-------------|
| `/aire-slurm-submit` | Submit and monitor Slurm jobs on AIRE |
| `/submit-gpu-job` | Submit GPU job with smoke test verification |
| `/conda-env-setup` | Create conda environment with CUDA |
| `/debug-pytorch-gpu` | Diagnose PyTorch GPU issues |
| `/debug-training` | Debug training failures by symptom |

### PCOS Workflows (4)

| Workflow | Description |
|----------|-------------|
| `/pcos-setup` | Set up PCOS broker for local development |
| `/pcos-test` | Run PCOS test suite and fix failures |
| `/pcos-add-chrome-api` | Add a new Chrome Built-in AI API to routing pipeline |
| `/pcos-debug-routing` | Debug why a task routes to the wrong surface |

### MCP Server Workflows (7)

| Workflow | Description |
|----------|-------------|
| `/dgx-monitor` | Check DGX Spark GPU, memory, Docker, conda, CUDA status |
| `/cuda-profiling` | Profile CUDA kernels with nsys, ncu, compute-sanitizer |
| `/distributed-training` | Multi-GPU discovery, NCCL diagnostics, DDP/FSDP setup |
| `/cloud-gpu-ssh` | Manage remote GPU machines via SSH, run remote commands |
| `/tpu-jax` | JAX/TPU device discovery, gcloud TPU management, profiling |
| `/endosight-pipeline` | Monitor Endosight 3D reconstruction pipeline status |
| `/research-workflow` | Search ArXiv, manage BibTeX, track experiments |

### Custom Research Workflows (663)

| Workflow | Description |
|----------|-------------|
| `/surgical-video-analysis` | Analyze surgical video for MOT, detection, scene understanding |
| `/cuda-kernel-optimization` | Optimize CUDA kernels for GB10 DGX Spark (SM121) |
| `/cutile-python-gb10` | Tile-based programming with NVIDIA cuTile Python on GB10 |
| `/cutile-persistent-matmul-gb10` | Persistent cuTile FP16/FP32 GEMM with ~2-wave launch on GB10 |
| `/cutile-fmha-attention-gb10` | Fused multi-head attention with cuTile and online softmax on GB10 |
| `/cooperative-groups-gb10` | Cooperative Groups and `cudaLaunchCooperativeKernel` on GB10 |
| `/cooperative-groups-warp-tile-gb10` | Warp-level `tiled_partition` reduce/scan/shfl on GB10 |
| `/cub-device-algorithms-gb10` | CUB device-wide reduce/scan/sort on GB10 |
| `/cub-reduce-by-key-gb10` | CUB `DeviceReduce::ReduceByKey` on GB10 |
| `/cub-segmented-sort-gb10` | CUB `DeviceSegmentedSort::SortKeys` on GB10 |
| `/cuda-dynamic-parallelism-gb10` | CUDA Dynamic Parallelism (parent/child kernels) on GB10 |
| `/cuda-dynamic-parallelism-quicksort-gb10` | Recursive CDP quicksort with `-rdc=true` on GB10 |
| `/cuda-graphs-inference-gb10` | Capture/replay CUDA graphs for low-latency inference on GB10 |
| `/fused-attention-inference-gb10` | FlashAttention-style fused attention for inference on GB10 |
| `/fp8-fp4-quantization-inference-gb10` | FP8/FP4 post-training quantization for Blackwell inference |
| `/fast-gemm-inference-gb10` | cuBLASLt and cuTile GEMM for low-latency inference on GB10 |
| `/model-evaluation` | Systematic model evaluation and benchmarking |
| `/video-processing-pipeline` | Build GPU-accelerated video processing pipelines |
| `/thesis-writing` | Write and structure PhD thesis chapters with LaTeX |
| `/academic-poster` | Create academic conference posters |
| `/literature-review` | Conduct systematic literature reviews |
| `/huggingface-hub` | Upload models, datasets, and Spaces to Hugging Face Hub |
| `/experiment-reproducibility` | Ensure experiments are fully reproducible |
| `/collaborative-research` | Manage collaborative research projects |
| `/blackwell-fp4-fp8-block-scaling-ptx-gb10` | FP8 and block-scaled FP4 (NVFP4) PTX MMA with scale factors on SM121 |
| `/blackwell-sm121-targeting-gb10` | Correctly compile for GB10 (sm_121/121f/121a), PTX 9.1, and Triton ptxas setup |
| `/cp-async-pipeline-gb10` | Multi-stage cp.async copy pipelines for GB10 GMEM->SMEM staging |
| `/cuda-occupancy-register-pressure-gb10` | Occupancy, register pressure, launch bounds, and SMEM tradeoffs on GB10 |
| `/nsight-compute-tensor-cores-gb10` | Profile Tensor Core utilization and memory bottlenecks with Nsight Compute on GB10 |
| `/shared-memory-swizzling-gb10` | Bank-conflict-free shared memory layouts with XOR swizzling and padding tradeoffs on GB10 |
| `/tensor-core-fragment-layouts-gb10` | PTX mma.sync fragment layouts and lane-to-element mapping for GB10 Tensor Cores |
| `/ada-l40s-optimization` | L40S-specific tuning: FP8, TensorRT-LLM/Triton, multi-GPU PCIe scaling, and media engines. |
| `/blackwell-dc-fp4-quantization` | Block-scaled 4-bit formats for training and inference on datacenter Blackwell. |
| `/blackwell-dc-moepart-green-contexts` | Resource partitioning (MLOPart, Green Contexts, MPS) and disaggregated prefill/decode serving for datacenter Blackwell. |
| `/blackwell-dc-tcgen05-tmem` | Programming datacenter Blackwell (sm_100/sm_103) with tcgen05.mma, TMEM, TMA multicast, and CTA-pair operations. |
| `/climate-weather-ml` | FourCastNet, GraphCast, Pangu-Weather, ClimaX, and ECMWF ai-models on GPU clusters. |
| `/cuda-q-hybrid-quantum` | CUDA-Q kernels, simulators, VQE/QAOA, PyTorch/JAX integration, and multi-GPU quantum workflows. |
| `/cuquantum-tensornet` | GPU-accelerated quantum simulation: state vector, tensor network, expectation values, and gradients. |
| `/distributed-launch-slurm-mpi` | Launching multi-node PyTorch/JAX training with SLURM, torchrun, MPI, CUDA-aware MPI, and UCX. |
| `/hopper-flashattention-3` | FlashAttention-3 warp specialization, WGMMA/TMA pipelining, and FP8 block quantization on H100/H200. |
| `/hopper-fp8-transformer-engine` | FP8 recipes (E4M3/E5M2, current, delayed, and blockwise scaling) with Transformer Engine for LLM training. |
| `/hopper-megatron-deepspeed` | Large-model training with Megatron-Core, Megatron-FSDP, DeepSpeed ZeRO, and NVLink4 on H100/H200. |
| `/hopper-wgmma-tma` | Low-level Hopper programming with `wgmma.mma_async`, `cp.async.bulk.tensor`, tensor maps, and mbarriers. |
| `/jax-gpu-scientific` | JAX `jit`, `vmap`, `shard_map`, device meshes, and XLA memory tuning on H100/H200/Blackwell/L40S. |
| `/jax-pde-sciml` | JAX-based SciML: Diffrax, Exponax, JAX-MD, neural operators, and differentiable simulations. |
| `/mamba-ssm-kernels` | Mamba-2/3 SSD kernels, fused selective scan, CuTe/Triton/TileLang backends, and chunk scheduling. |
| `/materials-discovery-ml` | MatterGen, GNoME, DiffCSP, CDVAE, and crystal structure generation on GPU. |
| `/moe-grouped-gemm` | Grouped GEMM, MoE routing, cuBLAS/cuDNN/TransformerEngine/FlashInfer/vLLM backends. |
| `/molecular-ml-drug-discovery` | Equivariant GNNs, ML potentials, molecular docking (DiffDock), and generative molecule design on GPU. |
| `/multigpu-nccl-topology` | NCCL, NVLink/NVSwitch, PCIe, InfiniBand/RoCE, GPUDirect, and common topology hang fixes. |
| `/neural-operators-pinns` | Fourier Neural Operator, DeepONet, PINNs, and JAX/Diffrax/Exponax for PDEs on GPU. |
| `/protein-folding-gpu` | AlphaFold 3, ESM3, Boltz, BioNeMo Fold-CP, OpenFold, and high-throughput protein folding pipelines. |
| `/scientific-data-formats` | Zarr, TensorStore, WebDataset, HDF5/NetCDF, KvikIO, and direct-to-GPU I/O pipelines. |
| `/torch-compile-inductor` | PyTorch 2.7+ `torch.compile`, Inductor autotune, custom operators, CuTeDSL/Gluon backends, and debug. |
| `/triton-cross-arch` | Writing and deploying Triton kernels across sm_80, sm_89, sm_90, sm_100, sm_120, and sm_121. |
| `/ampere-a100-scientific` | A100 architecture, TF32, structured sparsity, MIG, FP64, and cuBLAS/cuDNN paths for scientific workloads. |
| `/bioinformatics-genomics-ml` | DNABERT, Enformer, single-cell analysis with scVI/scGPT, and RAPIDS cuDF for genomics pipelines. |
| `/cuda-tile-advanced-gb10` | cuTile Python/C++ advanced features: block-scaled `ct.mma_scaled`, Tile IR, persistent kernels, and Nsight Tile profiling. |
| `/cutlass-persistent-kernels` | CUTLASS 3.x persistent kernels, cooperative vs ping-pong schedule, warp specialization, and CollectiveBuilder for FP8/FP4. |
| `/dgx-spark-multinode-roce` | Connect 2-3 DGX Sparks over QSFP RoCE, NCCL configuration, Docker host networking, and no GPUDirect RDMA. |
| `/dgx-spark-uma-tuning` | Tuning DGX Spark's 128 GB unified LPDDR5X memory, page cache competition, thermal throttling, EC firmware, and CPU compilation flags. |
| `/flashattention-4-sm121` | FlashAttention-4 consumer Blackwell support on sm_120/sm_121: paged KV, head_dim limits, FP8, and the CuTe DSL dispatch path. |
| `/geospatial-remote-sensing-ml` | Prithvi, SatMAE, TorchGeo, TerraTorch, segment-anything for Earth observation, and NVIDIA cuOpt. |
| `/llm-inference-gb10` | vLLM and TensorRT-LLM inference on GB10: FP8 KV, Marlin, MTP, MoE backend selection, and driver 580.x. |
| `/mixed-precision-training-gpu` | BF16, FP16, FP8, TF32, FP32 master weights, loss scaling, and when to use each on Ampere/Hopper/Blackwell. |
| `/molecular-dynamics-gpu` | MACE, CHGNet, DeePMD-kit, LAMMPS/GROMACS integration, and multi-GPU spatial decomposition for ML potentials. |
| `/nsight-profiling-gpu` | Nsight Compute sections/metrics, Nsight Systems gap analysis, hardware CUDA trace, and Tile profiling for cuTile. |
| `/pytorch-blackwell-deployment` | PyTorch nightly wheels, sm_100/sm_120 support, architecture detection, and common Blackwell-specific errors. |
| `/quantization-backends-gpu` | AWQ, GPTQ, AutoRound, Marlin, FP8, NVFP4, MXFP4, and backend selection for A100/H100/L40S/RTX50/GB10. |
| `/astrophysics-cosmology-ml` | Gravitational lensing, galaxy classification, N-body simulations, dark matter mapping, and cosmological parameter inference. |
| `/bayesian-inference-gpu` | MCMC, NUTS, variational inference, NumPyro, BlackJAX, and GPyTorch on NVIDIA GPUs. |
| `/causal-inference-science` | Do-calculus, causal discovery, structural causal models, transportability, and mediation for observational and experimental data. |
| `/differential-equations-gpu` | ODE/PDE/SDE solvers, spectral and finite element methods, Diffrax, FEniCSx, PETSc, and NekRS on GPU. |
| `/equivariant-neural-networks-science` | E(3)/SE(3)-equivariant networks (E3NN, Equiformer, MACE, NequIP, steerable CNNs) for atomic and molecular systems. |
| `/experiment-tracking-optimization` | W&B, MLflow, Neptune, Aim, Optuna, Ray Tune, and reproducible hyperparameter search on HPC. |
| `/fluid-dynamics-cfd-ml` | Neural operators, PhysicsNeMo (Modulus), JAX-Fluids, PhiFlow, and surrogate CFD on GPU. |
| `/generative-models-science` | Diffusion, flow matching, score-based models, and normalizing flows for molecules, materials, and inverse design. |
| `/gnn-science` | GNNs for molecules, materials, weather, neural operators, and large-scale graph training on GPU. |
| `/neuroscience-ml-gpu` | fMRI, calcium imaging, connectomics, and neural decoding with cuBNM, DeepWonder, scGPT, and RAPIDS. |
| `/optimization-gpu` | First- and second-order optimization, Optax/JAXopt, L-BFGS, trust-region, constrained, and Newton-Krylov methods on GPU. |
| `/quantum-chemistry-gpu` | GPU-accelerated DFT, Hartree-Fock, coupled cluster with PySCF/GPU4PySCF, and hybrid quantum-classical ML. |
| `/reinforcement-learning-science` | RL for tokamak plasma control, drug design, experiment design, and autonomous scientific systems. |
| `/scientific-linear-algebra-gpu` | Dense and sparse linear algebra with cuBLAS, cuSOLVER, cuSPARSE, cuDSS, MAGMA, and device-side cuSolverDx. |
| `/scientific-workflows-hpc` | Workflow engines (Snakemake, Nextflow, CWL), containers, DVC, SLURM job arrays, checkpointing, and cloud HPC. |
| `/signal-image-processing-gpu` | FFT, wavelets, filtering, compressed sensing, and tomography with cuFFT, RAPIDS, and GPU pipelines. |
| `/transformers-for-science` | Transformers for protein, genomics, weather, chemistry, math, and symbolic regression; ESM, AlphaFold, Prithvi, DNABERT, AI-Descartes. |
| `/uncertainty-quantification-science` | Conformal prediction, evidential learning, Bayesian neural nets, ensembles, Fortuna, and UQ for PDE surrogates. |
| `/cicd-ml-pipelines` | GitHub Actions, GitLab CI, pre-commit, artifact registries, and model promotion gates for ML pipelines. |
| `/containers-reproducibility` | Docker, Apptainer/Singularity, Podman, conda-lock, Nix, and reproducible scientific environments. |
| `/data-engineering-science` | ETL pipelines, feature stores, vector databases, RAG, and embeddings for scientific data. |
| `/distributed-storage-hpc` | Lustre, BeeGFS, GPFS, WekaFS, Ceph, Zarr, and TensorStore for high-throughput scientific data. |
| `/fault-tolerance-checkpointing` | PyTorch DCP, DeepSpeed elastic training, asynchronous checkpointing, and multi-tier checkpoint storage. |
| `/gpu-cluster-management` | SLURM, PBS, LSF, cloud bursting, hybrid clusters, and AWS ParallelCluster for GPU HPC. |
| `/kubernetes-gpu-orchestration` | NVIDIA GPU Operator, MIG, MPS, Kueue, Volcano, gang scheduling, and DRA for ML workloads on Kubernetes. |
| `/ml-security-supply-chain` | Model signing, AIBOM/ML-BOM, container scanning, malicious pickle detection, and provenance for ML artifacts. |
| `/model-serving-gpu` | Triton Inference Server, TensorRT-LLM, vLLM, TorchServe, FastAPI, and BentoML for production inference. |
| `/monitoring-observability-ml` | Prometheus, Grafana, Weights & Biases, MLflow, Evidently, and drift detection for production ML. |
| `/networking-distributed-training` | InfiniBand, RoCE, NCCL tuning, AWS EFA, and diagnosing multi-node network issues. |
| `/ray-ml-distributed` | Ray Train, Ray Tune, Ray Serve, Ray Data, and Ray clusters for scaling training, tuning, serving, and data processing. |
| `/agritech-phenotyping` | UAV/drone imaging, vision-language models, yield estimation, disease detection, and crop monitoring on GPU. |
| `/battery-materials-ml` | GNNs, Gaussian processes, and high-throughput screening for battery materials, redox flow batteries, and carbon capture solvents. |
| `/biodiversity-edna-ml` | Environmental DNA, species distribution modeling, zero-shot taxonomic assignment, and biodiversity monitoring on GPU. |
| `/epidemiology-disease-surveillance` | SIR/SEIR models, GNNs, Gaussian processes, and transfer learning for outbreak prediction and disease dynamics. |
| `/high-energy-physics-ml` | Jet tagging, event reconstruction, Particle Transformer, Hypergraph, and ROOT/Geant4 integration on GPU. |
| `/industry-4-predictive-maintenance` | RAPIDS, NVIDIA Omniverse, XGBoost, anomaly detection, and digital twins for manufacturing. |
| `/lab-robotics-digital-twins` | MATTERIX, LucidGrasp, 6D pose, sim-to-real, and digital twins for autonomous science labs. |
| `/proteomics-metabolomics-ml` | Mass spectrometry, peptide identification, DelPi, DIA-BERT, GiCOPS, ANN-SoLo, and metabolite annotation on GPU. |
| `/renewable-energy-forecasting` | Spatio-temporal diffusion, FNO, attention, and RL for solar/wind forecasting and energy dispatch. |
| `/social-simulation-ml` | AgentTorch, LLM-based agents, differentiable ABM, and causal discovery for social and economic systems. |
| `/spatial-transcriptomics-gpu` | Cell segmentation, transcript assignment, BIDCell, segger, PanoSpace, and foundation models for spatial omics. |
| `/sports-biomechanics-ml` | Wearable sensors, ST-GNNs, federated learning, and multimodal fusion for athlete performance and injury risk. |
| `/category-theory-ml` | Functorial data modeling, categorical deep learning, structured cospans, string diagrams, and topos theory for ML. |
| `/differential-geometry-ml` | Riemannian manifolds, geodesics, natural gradients, hyperbolic ML, and optimization on curved spaces. |
| `/game-theory-multiagent-ml` | Nash equilibria, mean-field games, mechanism design, and deep multi-agent reinforcement learning. |
| `/high-dimensional-statistics` | Sparsity, LASSO, compressed sensing, concentration inequalities, and covariance estimation. |
| `/information-geometry-ml` | Fisher information metric, natural gradient, alpha-connections, and geometry of probability distributions. |
| `/kernel-methods-science` | RKHS, Gaussian processes, MMD, kernel mean embeddings, and kernel methods for PDEs. |
| `/optimal-transport-ml` | Wasserstein distance, Sinkhorn algorithm, sliced Wasserstein, and applications to generative modeling and domain adaptation. |
| `/optimization-under-uncertainty` | Robust optimization, stochastic programming, distributionally robust optimization, and Wasserstein DRO. |
| `/random-matrix-theory-ml` | Marchenko-Pastur, semicircle law, free probability, and spectral analysis of neural networks. |
| `/spectral-graph-ml` | Graph Laplacian, spectral clustering, spectral GNNs, graph partitioning, and spectral sparsification. |
| `/stochastic-processes-ml` | Itô calculus, score-based generative models, neural SDEs, rough paths, and continuous-time generative modeling. |
| `/topological-data-analysis` | Persistent homology, Ripser, GUDHI, Mapper, and topological deep learning for shape-aware scientific ML. |
| `/agent-evaluation-benchmarks` | Measure agent capability on coding, web, tool use, and open-ended reasoning benchmarks. |
| `/agent-memory` | Short-term and long-term memory for agents: vector stores, summaries, entity tracking, and memory hierarchies. |
| `/llm-judge-evaluation` | Use strong language models to evaluate, score, and compare outputs from other models or pipelines. |
| `/llm-reasoning` | Chain-of-thought, self-consistency, tree-of-thoughts, and reasoning-optimized prompting for large language models. |
| `/llm-redteaming` | Systematically probe LLMs for harmful outputs, jailbreaks, privacy leaks, and misalignment. |
| `/long-context-llm` | Architectures, position interpolation, and evaluation for language models with very long contexts. |
| `/mcp-integration` | Connect agents to external tools, databases, and services using the Model Context Protocol (MCP). |
| `/multi-agent-orchestration` | Coordinate multiple specialist agents to decompose tasks, debate, and synthesize solutions. |
| `/prompt-engineering-advanced` | Structured prompting, few-shot, chain-of-thought, role prompts, and prompt optimization for LLMs. |
| `/rag-retrieval-evaluation` | Evaluate retrieval quality, answer relevance, and end-to-end RAG pipeline performance. |
| `/test-time-compute` | Improve LLM output quality by increasing inference-time computation: search, verification, and reward models. |
| `/tool-use-agents` | Design LLM agents that call functions, APIs, and utilities to gather facts and take actions. |
| `/ai-for-arts-humanities` | Digital humanities, text analysis, image restoration, and creative AI for cultural heritage. |
| `/ai-for-autonomous-vehicles` | Perception, prediction, planning, and simulation for self-driving cars and mobile robots. |
| `/ai-for-biology` | Deep learning for genomics, transcriptomics, proteomics, cell imaging, and biological sequence modeling. |
| `/ai-for-chemistry` | Molecular property prediction, generative chemistry, reaction prediction, and cheminformatics with deep learning. |
| `/ai-for-education` | Personalized learning, knowledge tracing, automated assessment, and intelligent tutoring systems. |
| `/ai-for-finance` | Machine learning for time-series forecasting, risk modeling, algorithmic trading, and financial NLP. |
| `/ai-for-law` | Legal document analysis, case law retrieval, contract review, and legal reasoning benchmarks. |
| `/ai-for-music` | Music generation, transcription, recommendation, and audio processing with deep learning. |
| `/ai-for-physics-simulation` | Neural operators, surrogate models, and learned emulators for partial differential equations and physical systems. |
| `/ai-for-psychiatry-mental-health` | Machine learning for digital phenotyping, diagnostic support, treatment prediction, and crisis detection. |
| `/ai-for-quantum-computing` | Machine learning for quantum state tomography, variational quantum algorithms, quantum control, and error mitigation. |
| `/ai-for-robotics` | Imitation learning, reinforcement learning, sim-to-real, and foundation models for robot manipulation and navigation. |
| `/ai-for-agriculture` | Crop monitoring, yield prediction, pest detection, and precision agriculture with ML and remote sensing. |
| `/ai-for-archaeology` | Remote sensing, LiDAR, and computer vision for site detection, artifact analysis, and heritage preservation. |
| `/ai-for-carbon-capture` | Machine learning for adsorbent and solvent screening, process optimization, and carbon capture materials design. |
| `/ai-for-forensics` | ML for image authentication, deepfake detection, authorship attribution, and anomaly detection in forensic evidence. |
| `/ai-for-gravitational-waves` | Deep learning for compact binary coalescence search, parameter estimation, and glitch classification. |
| `/ai-for-materials-synthesis` | Machine learning for synthesis route prediction, process optimization, and inverse design of materials. |
| `/ai-for-nuclear-engineering` | Machine learning for reactor design, plasma control, material degradation, and fusion ignition prediction. |
| `/ai-for-oceanography` | Data-driven ocean forecasting, current reconstruction, eddy detection, and marine ecosystem modeling. |
| `/ai-for-satellite-imaging` | Earth observation foundation models, land-use classification, change detection, and disaster mapping. |
| `/ai-for-seismology` | Machine learning for earthquake detection, phase picking, denoising, and seismic signal classification. |
| `/ai-for-volcanology` | Machine learning for eruption forecasting, volcanic seismicity classification, and hazard assessment. |
| `/ai-for-water-security` | ML for water quality prediction, leak detection, flood forecasting, and hydrological modeling. |
| `/active-learning` | Iteratively select the most informative unlabeled data points for efficient annotation and model improvement. |
| `/ai-fairness` | Detect, measure, and mitigate bias across demographic groups in classification, ranking, and regression. |
| `/curriculum-learning` | Order training examples from easy to hard to improve convergence and generalization. |
| `/domain-adaptation` | Transfer knowledge from a labeled source domain to an unlabeled or partially labeled target domain. |
| `/explainable-ai` | Feature attribution, concept-based explanations, saliency maps, and interpretability for black-box models. |
| `/federated-learning` | Decentralized model training across clients, handling non-IID data, aggregation, and personalization. |
| `/few-shot-learning` | Learning from a handful of labeled examples through meta-learning, prompt tuning, and data augmentation. |
| `/meta-learning` | Learn-to-learn methods such as MAML, metric learning, and neural processes for fast adaptation. |
| `/model-interpretability` | Intrinsic and post-hoc methods for understanding model behavior, features, and decision boundaries. |
| `/privacy-preserving-ml` | Differential privacy, federated learning, homomorphic encryption, and secure multi-party computation for ML. |
| `/robust-ml` | Adversarial robustness, distribution shift, out-of-distribution detection, and reliable model performance. |
| `/uncertainty-quantification-ml` | Predictive uncertainty, calibration, conformal prediction, and Bayesian methods for reliable ML. |
| `/agent-monitoring-guardrails` | Runtime monitoring, safety policy enforcement, tool-call validation, probabilistic risk prediction, and guardrail frameworks for LLM agents. |
| `/ai-for-cad` | Deep generative models for parametric CAD sketches, B-rep synthesis, sketch-and-extrude sequences, and vision-language conditional CAD generation. |
| `/cost-optimization-cloud` | FinOps practices, spot/preemptible instances, right-sizing, reserved capacity, autoscaling, and cost-aware scheduling for ML workloads. |
| `/data-stream-processing` | Apache Kafka and Flink pipelines, event-time semantics, exactly-once delivery, online feature engineering, and real-time model updates. |
| `/edge-ai` | Quantization, pruning, knowledge distillation, neural architecture search, and deployment of ML models on mobile, embedded, and edge accelerators. |
| `/generative-design` | Deep generative models (VAEs, GANs, diffusion) for engineering design synthesis, constraint-aware generation, Pareto-front exploration, and design automation. |
| `/graph-databases` | Property graph models, Cypher/Gremlin querying, graph embeddings, GNNs on graph DBs, and knowledge graph completion for connected data. |
| `/industrial-digital-twins` | Real-time virtual replicas of physical systems for monitoring, predictive maintenance, process optimization, and hybrid physics-ML modeling. |
| `/ml-infrastructure-as-code` | Terraform, Pulumi, and GitOps for reproducible ML platforms, modular MLOps stacks, and CI/CD-managed infrastructure. |
| `/real-time-ml` | Streaming inference, online learning, low-latency GPU serving, event-time semantics, and service-level objectives for real-time ML systems. |
| `/topology-optimization` | SIMP, neural reparameterization, generative topology optimization, physics-informed neural networks, and learned resolution-free solvers for structural design. |
| `/vector-databases` | Approximate nearest neighbor search, dense-embedding storage, metadata filtering, hybrid search, and vector indexing for RAG and recommendation. |
| `/ai-peer-review` | Use AI tools and structured checklists to write constructive, ethical peer reviews for manuscripts and proposals. |
| `/citation-management` | Organize references, manage PDFs, format bibliographies, and share libraries with Zotero, Mendeley, or BibTeX. |
| `/collaboration-and-team-science` | Build, lead, and sustain productive interdisciplinary research teams with clear roles, communication, and shared tools. |
| `/competitive-analysis` | Map industry structure, benchmark competitors, and identify strategic positioning using Porter's Five Forces, SWOT, and data. |
| `/grant-proposal-writing` | Structure Specific Aims, research strategy, budget, and broader impact sections for NIH/NSF/ERC-style proposals with AI drafting support. |
| `/market-research-ai` | Design surveys, segment customers, analyze open-ended responses, and forecast market trends with AI-driven tools. |
| `/product-requirements-ai` | Draft, validate, and track product requirements documents (PRDs) with user stories, assumptions, and success metrics. |
| `/research-data-storytelling` | Turn complex scientific results into narrative visualizations and stories that resonate with specialists and the public. |
| `/research-paper-ideation` | Use LLMs, citation networks, and structured brainstorming to generate and refine research questions, hypotheses, and project outlines. |
| `/research-presentation-design` | Build clear, compelling slides and posters for seminars, conferences, and outreach using narrative structure and visual hierarchy. |
| `/scientific-writing` | Improve clarity, structure, and style for manuscripts, theses, and reports using AI drafting and editing tools. |
| `/user-interviews-synthesis` | Turn interview transcripts into themes, insights, and personas using thematic analysis, affinity mapping, and AI coding. |
| `/ai-for-biofoundries` | AI/ML-driven lab automation, robotic liquid handling, closed-loop DBTL, and self-driving laboratories for synthetic biology. |
| `/ai-for-digital-organism` | Computational models, simulations, and multiscale foundation models of living systems as AI-driven digital organisms. |
| `/ai-for-drug-repurposing` | Graph ML, knowledge graphs, LLMs, and transcriptomics for identifying new indications for existing drugs. |
| `/ai-for-immunology` | Machine learning for adaptive immune receptor repertoires, epitope-MHC binding, immune cell phenotyping, and vaccine/immunotherapy design. |
| `/ai-for-longevity` | Biological aging clocks, biomarkers of aging, longevity intervention mining, and integrative multi-omic models of aging. |
| `/ai-for-neuroscience` | Deep learning for neural recordings, brain decoding, neuroimaging analysis, connectomics, and NeuroAI foundation models. |
| `/ai-for-nutrition` | Machine learning and generative AI for personalized nutrition, dietary assessment, meal planning, food recognition, and nutrition-health modeling. |
| `/ai-for-precision-medicine` | Multimodal machine learning for personalized diagnosis, treatment selection, risk prediction, and integration of genomics, EHRs, imaging, and wearables. |
| `/ai-for-protein-design` | Inverse folding, generative backbone design, and binder engineering with ProteinMPNN, RFdiffusion, structure predictors, and Rosetta validation. |
| `/ai-for-rare-disease` | AI for rare disease diagnosis, target prioritization, drug repurposing, natural history modeling, and diagnostic-odyssey support. |
| `/ai-for-sleep` | Machine learning for sleep staging, sleep disorder detection, wearable PSG analysis, and sleep health monitoring. |
| `/ai-for-synthetic-biology` | Machine learning for genetic circuit design, promoter and RBS optimization, metabolic pathway engineering, and closed-loop Design-Build-Test-Learn biofoundry pipelines. |
| `/analog-computing` | Reconfigurable analog accelerators, in-memory analog computing, and mixed-signal AI hardware. |
| `/dask-ml` | Distributed and out-of-core machine learning with Dask and scikit-learn, XGBoost, and hyperparameter search. |
| `/data-versioning` | DVC, lakeFS, and Delta Lake for versioning datasets, models, and pipelines alongside code. |
| `/feature-stores` | Feast, Tecton, and Hopsworks for centralized feature definition, versioning, and online/offline serving. |
| `/high-performance-python` | Numba, Cython, pybind11, vectorization, and profiling for Python code that rivals C/Fortran speed. |
| `/in-memory-computing` | Compute-in-memory, processing-in-memory, and emerging NVM technologies (PCM, RRAM, MRAM) for AI. |
| `/ml-metadata-lineage` | ML Metadata (MLMD), MLflow, and Kubeflow lineage for tracking artifacts, executions, and provenance. |
| `/modin-pandas` | Drop-in distributed, parallel pandas replacement using Modin with Ray or Dask backends. |
| `/neuromorphic-computing` | Spiking neural networks (SNNs), event-based processing, and brain-inspired low-power accelerators like Intel Loihi and BrainChip. |
| `/photonic-computing` | Silicon photonics, optical processing units, and photonic interconnects for energy-efficient AI and HPC. |
| `/quantum-machine-learning` | Hybrid quantum-classical ML with variational quantum circuits, PennyLane, TensorFlow Quantum, and Qiskit. |
| `/wafer-scale-ai` | Cerebras Wafer Scale Engine, wafer-scale training and inference, and massive on-chip compute fabric. |
| `/contrastive-learning` | Instance discrimination, InfoNCE, SimCLR, MoCo, CLIP, and deep metric learning for vision, language, and retrieval. |
| `/curriculum-rl` | Task sequencing, automatic curriculum generation, and progressive difficulty for sample-efficient RL. |
| `/hierarchical-rl` | Options, feudal networks, and goal-conditioned hierarchies for long-horizon, sparse-reward tasks. |
| `/imitation-learning` | Behavioral cloning, DAgger, GAIL, and learning policies from expert demonstrations with or without a reward function. |
| `/inverse-rl` | Recover reward functions from expert demonstrations using MaxEnt IRL, apprenticeship learning, and adversarial IRL. |
| `/masked-autoencoders` | BERT-style masked prediction for vision, BEVT, data2vec, and generative masked image and language modeling. |
| `/model-based-rl` | Learn environment dynamics for sample-efficient planning and policy optimization with PETS, MBPO, PlaNet, and MuZero. |
| `/multi-task-learning` | Shared representations, hard and soft parameter sharing, MTL architectures (MMoE, PLE, MTAN), and gradient balancing. |
| `/offline-rl` | Learn from static logged datasets with CQL, IQL, TD3+BC, D4RL, and conservative/batch RL methods. |
| `/safe-rl` | Constrained Markov Decision Processes, CPO, P3O, Lagrangian methods, and safety-gym benchmarks for constrained RL. |
| `/self-supervised-learning` | Pretext tasks, contrastive and non-contrastive SSL, masked prediction, and unsupervised representation learning for vision, language, and graphs. |
| `/world-models` | Latent dynamics models, recurrent state-space models, Dreamer, PlaNet, and agents that plan in imagination. |
| `/ai-for-climate-policy` | Natural-language analysis of climate laws, NDCs, and policies; target extraction, alignment scoring, and climate-finance tracking. |
| `/ai-for-disaster-response` | Situational awareness, damage assessment, evacuation planning, supply pre-positioning, and multi-modal disaster imagery analysis. |
| `/ai-for-energy-grid` | Power-flow surrogates, renewable and load forecasting, grid stability, optimal power flow, and AI-assisted grid operations. |
| `/ai-for-governance` | Public-service delivery, regulatory compliance, algorithmic accountability, participatory policy tools, and fair decision-support systems. |
| `/ai-for-logistics` | Vehicle routing, last-mile delivery, warehouse automation, fleet scheduling, and dynamic logistics optimization. |
| `/ai-for-manufacturing` | Predictive maintenance, quality control, process optimization, digital twins, and human-interpretable factory AI. |
| `/ai-for-public-health` | Disease surveillance, outbreak prediction, resource allocation, geospatial health modeling, and health-equity analytics. |
| `/ai-for-smart-cities` | Urban computing, IoT analytics, spatio-temporal forecasting, mobility, public safety, and citizen-centric services. |
| `/ai-for-social-good` | Education, poverty alleviation, agriculture, humanitarian response, accessibility, and community-driven AI for underserved populations. |
| `/ai-for-space-exploration` | Onboard autonomy, science target selection, anomaly detection, mission planning, and analysis of space and Earth-observation data. |
| `/ai-for-supply-chain` | Demand forecasting, inventory optimization, risk and resilience, supplier analytics, and end-to-end supply chain visibility. |
| `/ai-for-transportation` | Traffic prediction, route optimization, public transit planning, autonomous driving, and multi-modal mobility. |
| `/ai-for-battery-materials` | Machine learning for cathode, anode, electrolyte, and separator discovery, as well as battery lifetime and charging protocol optimization. |
| `/ai-for-catalysis` | Machine learning for catalyst discovery, reaction mechanism elucidation, activity and selectivity prediction, and catalytic process optimization. |
| `/ai-for-ceramics` | Data-driven design, processing optimization, and microstructure-property prediction for ceramic and refractory materials. |
| `/ai-for-composites` | Machine learning for composite material design, manufacturing process optimization, defect detection, and multiscale property prediction. |
| `/ai-for-corrosion` | Machine learning for corrosion rate prediction, corrosion-resistant alloy design, protective coating optimization, and infrastructure degradation monitoring. |
| `/ai-for-materials-characterization` | Machine learning for automated interpretation of microscopy, spectroscopy, diffraction, and tomography data in materials science. |
| `/ai-for-membranes` | Machine learning for membrane material design, permeability and selectivity prediction, fouling control, and separation process optimization. |
| `/ai-for-metals` | Machine learning for alloy design, phase stability, mechanical properties, process optimization, and microstructure-property mapping. |
| `/ai-for-photovoltaics` | Machine learning for solar-cell materials discovery, perovskite and organic PV optimization, device engineering, and stability prediction. |
| `/ai-for-polymers` | Machine learning for polymer property prediction, generative design, process optimization, and structure representation. |
| `/ai-for-semiconductors` | Machine learning for semiconductor materials discovery, bandgap engineering, defect analysis, and fabrication process optimization. |
| `/ai-for-superconductors` | Machine learning for superconductor discovery, critical temperature prediction, electron-phonon modeling, and materials screening. |
| `/ai-for-ecology` | Species distribution modeling, habitat suitability, biodiversity monitoring, and ecological forecasting using ML and remote sensing. |
| `/ai-for-environmental-science` | Remote sensing, land-cover mapping, ecosystem service assessment, and integrated modeling for environmental monitoring and analysis. |
| `/ai-for-fisheries` | Fish stock assessment, catch forecasting, aquaculture monitoring, eDNA, and IUU fishing detection with ML. |
| `/ai-for-forestry` | Forest inventory, tree segmentation, biomass estimation, and species mapping from remote sensing and LiDAR. |
| `/ai-for-geology` | Geologic mapping, mineral prospectivity, geophysical inversion, drill-core imagery, and remote sensing with ML and deep learning. |
| `/ai-for-hydrology` | Rainfall-runoff modeling, streamflow forecasting, flood prediction, and physics-informed deep learning for water systems. |
| `/ai-for-meteorology` | Numerical weather prediction emulators, precipitation nowcasting, extreme-weather detection, and weather foundation models. |
| `/ai-for-mineralogy` | XRD, SEM-EDS, Raman, and hyperspectral imaging for automated mineral identification, classification, and segmentation. |
| `/ai-for-paleontology` | Automated fossil identification, morphometric analysis, 3D segmentation, and taxonomic classification from images and point clouds. |
| `/ai-for-pollution` | Air, water, and soil pollution monitoring, source apportionment, forecasting, and regulatory compliance with ML. |
| `/ai-for-soil-science` | Digital soil mapping, pedotransfer functions, spectroscopic prediction, and soil health assessment with ML. |
| `/ai-for-wildlife-conservation` | Camera-trap image classification, acoustic monitoring, animal re-identification, and anti-poaching analytics. |
| `/ai-for-customer-service` | Conversational AI, intent classification, sentiment and satisfaction analysis, ticket routing, and agent-assist systems. |
| `/ai-for-demand-forecasting` | Time-series forecasting, hierarchical and intermittent demand, probabilistic forecasts, and promotion/event effects. |
| `/ai-for-economics` | Causal inference, policy evaluation, nowcasting, heterogeneous treatment effects, and demand estimation for economic and policy analysis. |
| `/ai-for-fraud-detection` | Transaction fraud, anti-money laundering, anomaly detection, graph-based fraud networks, and concept-drift monitoring. |
| `/ai-for-hr` | Talent analytics, recruitment matching, attrition prediction, workforce planning, and compensation and equity analysis. |
| `/ai-for-marketing` | Customer segmentation, personalization, propensity modeling, marketing-mix attribution, and generative AI for content and campaigns. |
| `/ai-for-operations-research` | Optimization, MILP/CP, vehicle routing and scheduling, decision-focused learning, and learning-augmented heuristics. |
| `/ai-for-pricing` | Price elasticity, dynamic and personalized pricing, revenue management, promotion optimization, and causal demand forecasting for pricing. |
| `/ai-for-recommendation-systems` | Collaborative filtering, content-based and hybrid recommendation, sequence models, and multi-objective ranking for commerce and content. |
| `/ai-for-retail` | Demand forecasting, inventory placement, personalized recommendations, dynamic pricing, and omnichannel fulfillment for retail. |
| `/ai-for-sales` | Predictive lead scoring, sales forecasting, opportunity win probability, next-best action, and pipeline analytics. |
| `/ai-for-supply-chain-optimization` | Multi-echelon inventory, distribution network design, demand-supply synchronization, and resilient supply chain planning. |
| `/ai-for-cardiology` | ECG interpretation, arrhythmia detection, heart failure screening, echocardiography analysis, and cardiovascular risk stratification with deep learning. |
| `/ai-for-clinical-nlp` | Natural language processing for electronic health records, clinical entity extraction, term normalization, de-identification, and question answering. |
| `/ai-for-dermatology` | Skin lesion classification, dermoscopy analysis, melanoma detection, teledermatology, and fairness across skin tones with deep learning. |
| `/ai-for-digital-therapeutics` | Software-as-a-medical-device interventions for mental health, substance use, sleep, ADHD, and chronic disease delivered through apps and wearables. |
| `/ai-for-gastroenterology` | AI-assisted endoscopy, real-time polyp detection and characterization, colonoscopy quality, and colorectal cancer screening. |
| `/ai-for-medical-imaging` | General medical image preprocessing, segmentation, classification, and deployment with DICOM, MONAI, nnU-Net, and clinical AI pipelines. |
| `/ai-for-neurology` | Neuroimaging and EEG analysis for stroke, brain tumors, epilepsy, and neurodegeneration, including lesion segmentation and outcome prediction. |
| `/ai-for-oncology` | AI for cancer detection, subtyping, treatment response, prognosis, radiomics, pathology, and clinical trial matching. |
| `/ai-for-ophthalmology` | Diabetic retinopathy screening, OCT analysis, glaucoma detection, and AI for retinal disease diagnosis from fundus photography. |
| `/ai-for-pathology` | Computational pathology, whole-slide image analysis, cancer subtyping, biomarker discovery, and vision-language models for histopathology. |
| `/ai-for-pulmonology` | Chest X-ray and CT interpretation, COPD and asthma assessment, respiratory sound analysis, and pulmonary disease risk prediction. |
| `/ai-for-radiology` | Deep learning for X-ray, CT, MRI, and mammography interpretation, including lesion detection, segmentation, report generation, and radiology foundation models. |
| `/ai-for-architecture` | AI for generative spatial layouts, floorplan synthesis, style exploration, and text/sketch-driven conceptual design. |
| `/ai-for-building-design` | AI for energy, daylight, HVAC, envelope, and MEP performance optimization in the built environment. |
| `/ai-for-construction` | AI for construction site safety, progress monitoring, schedule and cost risk, robotics, and digital-twin-enabled project delivery. |
| `/ai-for-cosmetics` | AI for personalized skincare, formulation optimization, shade matching, safety/toxicity prediction, and consumer insight. |
| `/ai-for-fashion` | AI for trend forecasting, outfit recommendation, virtual try-on, generative design, and personalized shopping. |
| `/ai-for-food-and-beverage` | AI for food safety, quality control, recipe and product development, shelf-life prediction, and supply chain optimization. |
| `/ai-for-hospitality` | AI for guest personalization, revenue management, dynamic pricing, operations, and conversational service. |
| `/ai-for-media-and-entertainment` | AI for content recommendation, personalization, generative media, audience analytics, and rights/compliance workflows. |
| `/ai-for-mining` | AI for mineral exploration, ore grade estimation, predictive maintenance, autonomous haulage, and mine safety. |
| `/ai-for-oil-and-gas` | AI for seismic interpretation, reservoir characterization, production forecasting, and predictive maintenance in energy operations. |
| `/ai-for-sports` | AI for athlete tracking, match analytics, performance prediction, injury risk, and tactical decision support. |
| `/ai-for-textiles` | AI for fabric defect detection, pattern and color design, sorting, and textile supply chain optimization. |
| `/api-development` | REST, gRPC, and GraphQL API design, implementation, documentation, and versioning for ML services. |
| `/backend-engineering` | Server-side development, async task queues, databases, caching, and resilience patterns for ML products. |
| `/data-engineering-best-practices` | Data lifecycle management, data quality, observability, lineage, testing, version control, and infrastructure-as-code for robust data systems. |
| `/data-lakes` | Object storage, open table formats, lakehouse architecture, and batch/stream unification for ML and analytics. |
| `/data-pipelines-ml` | Orchestrating end-to-end ML workflows with task dependencies, artifact tracking, retries, and reproducibility. |
| `/data-warehousing` | Cloud data warehouses, dimensional modeling, indexing, partitioning, and workload optimization. |
| `/etl-and-elt` | Extract, transform, load patterns and the modern extract, load, transform paradigm with tooling and trade-offs. |
| `/event-driven-architecture` | Events, event brokers, event sourcing, CQRS, and event-driven microservices for scalable, decoupled systems. |
| `/frontend-engineering` | Building user interfaces for ML-powered applications with modern frameworks, state management, and data visualization. |
| `/full-stack-ml` | End-to-end ML applications spanning data, model, API, frontend, deployment, and monitoring. |
| `/microservices` | Small, independently deployable services, inter-service communication, containers, and service discovery. |
| `/streaming-data` | Real-time data ingestion and processing with stream processors, message brokers, and event-time semantics. |
| `/ai-for-anthropology` | Computational ethnography, NLP for field notes and interviews, multimodal cultural analysis, and AI-assisted thick description and reflexivity. |
| `/ai-for-communication` | Computational communication science: content analysis, information diffusion, agenda setting, and audience effects across digital platforms. |
| `/ai-for-criminology` | Predictive policing, recidivism risk assessment, crime forecasting, criminal network analysis, and fairness-aware public safety research. |
| `/ai-for-history` | HTR and OCR for historical documents, event extraction, temporal reasoning, geospatial and network analysis, and distant reading for historical research. |
| `/ai-for-international-relations` | Conflict forecasting, event data analysis, crisis early warning, treaty and negotiation text mining, and geopolitical risk modeling. |
| `/ai-for-journalism` | Algorithmic journalism, automated reporting, fact-checking, news recommendation, and AI-assisted investigative data reporting. |
| `/ai-for-linguistics` | Computational linguistics, corpus analysis, morphosyntactic annotation, syntactic parsing, language modeling, and NLP tools for linguistic research. |
| `/ai-for-media-literacy` | AI for detecting disinformation, prebunking, source credibility, and teaching critical thinking and digital literacy. |
| `/ai-for-philosophy` | Computational philosophy, argument mining, automated reasoning, text analysis of philosophical corpora, and LLM-assisted conceptual analysis. |
| `/ai-for-political-science` | Text-as-data for politics: manifesto scaling, sentiment and stance detection, legislative and voting analysis, and causal inference for political institutions. |
| `/ai-for-public-policy` | Causal and predictive policy evaluation, program impact assessment, regulatory text analysis, and equitable resource allocation for government and public administration. |
| `/ai-for-sociology` | Computational social science for sociology: text and image classification, survey augmentation, social network analysis, and modeling social inequalities. |
| `/ai-for-3d-vision` | 3D reconstruction, point cloud processing, NeRF and Gaussian splatting, depth estimation, 3D detection, and scene understanding. |
| `/ai-for-animation` | Motion synthesis, inbetweening, character retargeting, physics-based animation, and style transfer for animated content. |
| `/ai-for-audio` | Audio enhancement, source separation, music generation, audio event detection, and speech enhancement. |
| `/ai-for-augmented-reality` | SLAM, scene understanding, depth completion, registration, occlusion handling, and semantic AR with deep learning. |
| `/ai-for-computer-graphics` | Neural rendering, differentiable rendering, inverse rendering, geometry and material estimation, and generative image synthesis for photorealistic graphics. |
| `/ai-for-computer-vision` | Image classification, detection, segmentation, vision-language models, generative vision, and efficient deep learning deployment. |
| `/ai-for-games` | Procedural content generation, game-playing agents via reinforcement learning, NPC behavior, and generative AI for game assets and narratives. |
| `/ai-for-human-robot-interaction` | Multimodal interfaces, natural language instructions, shared autonomy, social robotics, and embodied AI for human-robot collaboration. |
| `/ai-for-nlp` | Large language models, text classification, machine translation, question answering, information extraction, and prompt engineering. |
| `/ai-for-speech` | Automatic speech recognition, text-to-speech, speaker verification, speech synthesis, and self-supervised speech models. |
| `/ai-for-video` | Video understanding, action recognition, video generation, temporal modeling, video captioning, and multimodal video models. |
| `/ai-for-virtual-reality` | Natural interaction, intent recognition, multimodal input, foveated rendering, virtual agents, and AI-driven content creation for VR. |
| `/ai-for-acoustics` | Machine learning for source localization, room acoustics, bioacoustics, structural health monitoring, and spatial audio. |
| `/ai-for-astrobiology` | ML for biosignature detection, life-detection mass spectrometry, extremophile habitats, and mission autonomy in alien environments. |
| `/ai-for-astronomy` | Machine learning for survey-scale classification, transient detection, galaxy morphology, light-curve analysis, and telescope scheduling. |
| `/ai-for-biophysics` | Machine learning for molecular dynamics, free-energy landscapes, protein-ligand kinetics, single-molecule analysis, and membrane systems. |
| `/ai-for-condensed-matter` | Machine learning for phase classification, topological order, Hamiltonian learning, density functional surrogates, and quantum many-body systems. |
| `/ai-for-cosmology` | ML for large-scale structure, weak lensing, CMB analysis, 21-cm cosmology, and cosmological parameter inference. |
| `/ai-for-microfluidics` | Machine learning for droplet generation, lab-on-a-chip control, cell sorting, reaction optimization, and high-throughput screening. |
| `/ai-for-nanotechnology` | ML for nanoparticle design, nanomaterial discovery, nano-architectonics, nanoscale imaging, and nanomanufacturing optimization. |
| `/ai-for-optics` | Computational imaging, lens design, wavefront shaping, optical metrology, and inverse scattering with deep learning. |
| `/ai-for-particle-physics` | ML for collider event classification, jet tagging, fast detector simulation, neutrino event reconstruction, and new-physics searches. |
| `/ai-for-photonics` | Deep learning for photonic device inverse design, metasurfaces, optical communications, and nanophotonic simulation surrogates. |
| `/ai-for-planetary-science` | Machine learning for mission data analysis, terrain classification, crater detection, atmospheric retrievals, and exoplanet characterization. |
| `/ai-for-aerospace` | Machine learning for aircraft and spacecraft design, aerodynamic optimization, structural health monitoring, satellite operations, and certification of safety-critical aerospace systems. |
| `/ai-for-automotive` | AI for automotive design, manufacturing, battery management, ADAS, quality control, and supply-chain optimization across the vehicle lifecycle. |
| `/ai-for-aviation` | AI for airline and airport operations, including predictive maintenance, crew and fleet scheduling, disruption recovery, fuel optimization, and safety analytics. |
| `/ai-for-drones` | AI for UAV perception, navigation, obstacle avoidance, mission planning, multi-drone coordination, and vision-language drone control. |
| `/ai-for-exoskeletons` | AI for wearable exoskeleton and exosuit control, gait and intention recognition, human-robot interaction, rehabilitation, and assistive augmentation. |
| `/ai-for-field-robotics` | AI for robots operating in outdoor, unstructured environments such as agriculture, construction, mining, environmental monitoring, and disaster response. |
| `/ai-for-industrial-robotics` | Machine learning for factory manipulation, assembly, pick-and-place, force control, sim-to-real, and vision-language-action models in industrial settings. |
| `/ai-for-maritime` | AI for maritime autonomous surface ships, route and weather routing optimization, collision avoidance, port logistics, and vessel situational awareness. |
| `/ai-for-quality-control` | Machine learning and computer vision for automated inspection, defect detection, statistical process control, and zero-defect manufacturing. |
| `/ai-for-rail` | AI for railway infrastructure health, predictive maintenance, train scheduling, energy optimization, and real-time disruption management. |
| `/ai-for-smart-manufacturing` | AI for cyber-physical manufacturing, digital twins, real-time process optimization, predictive maintenance, and sustainable Industry 4.0/5.0 systems. |
| `/ai-for-warehouse-robotics` | AI for autonomous mobile robots, goods-to-person systems, picking, multi-agent path finding, task allocation, and warehouse traffic management. |
| `/ai-for-cooking` | Recipe generation, meal planning, ingredient substitution, food image recognition, and personalized nutrition-aware cooking assistance. |
| `/ai-for-event-planning` | Venue and vendor recommendation, guest-list management, scheduling, budget optimization, and group preference aggregation for personal and small events. |
| `/ai-for-fitness` | Personalized workout plans, exercise form analysis, pose estimation, wearables, and adaptive recovery for individual fitness. |
| `/ai-for-home-automation` | Smart home control, energy management, occupancy prediction, device scheduling, and comfort optimization with reinforcement learning and IoT. |
| `/ai-for-legal-assistance` | Legal intake, contract review, plain-language document summarization, form filling, and accessible legal triage for non-experts. |
| `/ai-for-lifestyle` | Habit formation, hobby and style recommendations, personal goal coaching, and holistic life-planning agents for everyday decisions. |
| `/ai-for-mental-health` | CBT-based chatbots, mood tracking, crisis triage, digital therapeutics, and scalable psychological support for consumers. |
| `/ai-for-personal-finance` | Budget optimization, cash-flow forecasting, robo-advisory, credit scoring, and personalized savings and investment guidance for household financial decisions. |
| `/ai-for-personal-productivity` | Time management, task prioritization, calendar scheduling, meeting optimization, and personal workflow automation. |
| `/ai-for-shopping` | Product discovery, personalized recommendations, price comparison, review summarization, and AI buyer guides for consumer purchases. |
| `/ai-for-travel` | Itinerary planning, point-of-interest recommendation, flight and hotel personalization, trip optimization, and conversational travel agents. |
| `/ai-for-wellness` | Holistic wellness, sleep, stress, mindfulness, HRV biofeedback, and personalized lifestyle recommendations for everyday well-being. |
| `/ai-for-border-security` | Biometric identity verification, contraband and anomaly detection, and multi-sensor fusion at ports of entry. |
| `/ai-for-crisis-communication` | Automated situational awareness, rumor detection, multilingual crisis summarization, and public information chatbots. |
| `/ai-for-cyber-physical-security` | Securing industrial control systems, SCADA anomaly detection, physical invariants, and cross-layer intrusion detection. |
| `/ai-for-cybersecurity` | Network intrusion detection, malware and phishing classification, vulnerability discovery, adversarial ML, and SOC automation. |
| `/ai-for-disaster-preparedness` | Hazard risk assessment, early warning systems, scenario simulation, and mitigation planning with AI. |
| `/ai-for-emergency-management` | Incident prediction, resource allocation, damage assessment, and generative AI for emergency operations. |
| `/ai-for-physical-security` | Perimeter intrusion detection, access control analytics, video anomaly detection, and AI-augmented guard operations. |
| `/ai-for-public-safety` | Emergency call dispatch, response-time optimization, situational awareness, and fairness-aware public safety analytics. |
| `/ai-for-resilience` | Critical infrastructure resilience, disaster recovery planning, stress testing, and learning-based restoration optimization. |
| `/ai-for-search-and-rescue` | UAV and robot search planning, victim detection from imagery and sensors, and SAR mission coordination with AI. |
| `/ai-for-surveillance-ethics` | Fairness, privacy, proportionality, and algorithmic accountability for AI surveillance and facial recognition. |
| `/ai-for-threat-intelligence` | Cyber threat intelligence extraction, attribution, knowledge graphs, and automated indicator analysis with ML and LLMs. |
| `/ai-for-advertising` | Ad creative generation, media buying optimization, dynamic creative optimization, and predictive performance modeling. |
| `/ai-for-branding` | Brand strategy, visual identity, brand voice, naming, and AI-assisted brand co-creation with human curation. |
| `/ai-for-content-strategy` | Planning, auditing, and orchestrating content portfolios with AI, including generative-engine optimization and cross-platform adaptation. |
| `/ai-for-copywriting` | Marketing and advertising copy, email and landing-page text, conversion frameworks, and brand-voice calibration with LLMs. |
| `/ai-for-creative-writing` | Co-writing novels, screenplays, and long-form fiction with LLMs, prompt engineering for voice and style, and human-AI revision workflows. |
| `/ai-for-digital-marketing` | SEO, SEM, social media, email automation, marketing analytics, and AI-driven personalization across digital channels. |
| `/ai-for-influencer-marketing` | Creator discovery, campaign matching, content co-creation, performance prediction, and authenticity measurement for influencer marketing. |
| `/ai-for-podcasting` | AI-generated and AI-assisted podcast production, including scriptwriting, voice synthesis, editing, transcription, and show notes. |
| `/ai-for-poetry` | Meter, rhyme, and stylistic constraints for AI-generated poetry, with evaluation and human-AI curation. |
| `/ai-for-product-design` | Concept generation, design space exploration, prototyping, and engineering handoff with generative AI in product development. |
| `/ai-for-storytelling` | Narrative generation, plot planning, character arcs, and worldbuilding with structured LLM workflows. |
| `/ai-for-ux-design` | Interaction design, user research, prototyping, and AI UX patterns for human-centered AI products. |
| `/ai-for-competency-development` | Competency-based education, skill gap analysis, adaptive credentialing, and AI-driven mastery and portfolio assessment. |
| `/ai-for-curriculum-design` | Goal-aligned course sequencing, personalized learning paths, content alignment, adaptive curricula, and standards mapping. |
| `/ai-for-educational-assessment` | Automated essay scoring, conversational assessment, LLM rubric grading, feedback generation, and validity and fairness of AI-driven evaluation. |
| `/ai-for-educational-games` | Game-based learning, adaptive difficulty, intelligent NPCs, scaffolding, and learning analytics embedded in playful environments. |
| `/ai-for-higher-education` | Admissions analytics, retention and completion modeling, student success advising, enrollment planning, and institutional research. |
| `/ai-for-language-learning` | AI chatbots for conversation practice, automated writing and pronunciation feedback, CEFR-level adaptation, and second-language acquisition support. |
| `/ai-for-learning-analytics` | Learning management system analysis, learner trajectory modeling, early warning systems, engagement dashboards, and educational data mining. |
| `/ai-for-lifelong-learning` | Continuous skill development, career-aligned learning pathways, micro-credentials, and AI support for adult and professional learners. |
| `/ai-for-pedagogy` | Teacher-AI collaboration, lesson planning, instructional design, feedback generation, and evidence-based teaching practice augmentation. |
| `/ai-for-special-education` | Assistive technologies, personalized interventions, augmentative and alternative communication, accessibility, and inclusive learning for learners with disabilities. |
| `/ai-for-student-engagement` | Engagement prediction, behavioral analytics, early warning systems, intervention targeting, and motivational feedback. |
| `/ai-for-tutoring` | Intelligent tutoring systems, dialogue-based tutoring, error diagnosis, Socratic scaffolding, and personalized next-step hints. |
| `/ai-for-air-quality` | Pollutant forecasting, spatiotemporal PM modeling, emission source apportionment, and early warning for air quality. |
| `/ai-for-biodiversity` | Automated species detection, acoustic and eDNA monitoring, habitat suitability modeling, and biodiversity trend analysis for conservation. |
| `/ai-for-circular-economy` | Material flow optimization, predictive recycling, product lifecycle extension, and circular supply-chain design with AI. |
| `/ai-for-conservation-planning` | Spatial prioritization, protected-area design, systematic conservation planning, and trade-off analysis using optimization and ML. |
| `/ai-for-coral-reefs` | Coral reef monitoring, bleaching detection, benthic classification, and reef-health assessment from underwater and drone imagery. |
| `/ai-for-desertification` | Land degradation and desertification risk mapping, sensitivity assessment, and early warning from remote sensing and ML. |
| `/ai-for-ecosystem-restoration` | Monitoring rewilding, forest recovery, wetland restoration, and habitat reconstruction using remote sensing and biodiversity indicators. |
| `/ai-for-glaciology` | Glacier mapping, surface mass balance estimation, snow/ice classification, and climate-change impact assessment. |
| `/ai-for-natural-hazards` | Multi-hazard susceptibility mapping and early warning for landslides, floods, wildfires, and land subsidence with ML and remote sensing. |
| `/ai-for-ocean-conservation` | Marine protected area monitoring, illegal fishing detection, species tracking, and ocean health assessment from satellite and vessel data. |
| `/ai-for-waste-management` | Waste classification, automated sorting, route optimization, recycling quality, and lifecycle assessment with ML and robotics. |
| `/ai-for-wetlands` | Wetland mapping, inundation dynamics, cover-type classification, and hydrological trend monitoring from satellite time series. |
| `/ai-for-change-management` | Stakeholder sentiment monitoring, adoption analytics, training personalization, and AI-assisted transformation communications. |
| `/ai-for-compliance` | Regulatory mapping, policy gap analysis, automated control testing, and AI-assisted compliance monitoring. |
| `/ai-for-innovation-management` | Idea generation, R&D portfolio prioritization, trend forecasting, and AI-enabled new product development. |
| `/ai-for-insurance` | Underwriting triage, claims automation, fraud detection, and AI-assisted pricing and reserving. |
| `/ai-for-knowledge-management` | Semantic knowledge search, enterprise RAG, expertise mining, and AI-assisted capture of institutional tacit knowledge. |
| `/ai-for-legal-operations` | Contract review, clause extraction, matter intake, and AI-assisted legal workflow automation. |
| `/ai-for-management-consulting` | Accelerate diagnostic research, market sizing, client synthesis, and GenAI-assisted advisory workflows while managing epistemic risk. |
| `/ai-for-operations-management` | Process mining, service-level optimization, quality control, and AI-driven operational decision support. |
| `/ai-for-project-management` | Schedule and cost forecasting, risk triage, resource optimization, and AI-driven project health monitoring. |
| `/ai-for-real-estate` | Automated valuation, market analysis, lead matching, and AI-assisted property due diligence. |
| `/ai-for-risk-management` | Credit, market, operational, and emerging risk modeling with ML and scenario analysis. |
| `/ai-for-strategy` | Data-driven strategy formulation, competitive scenario modeling, market sensing, and AI-augmented strategic decision-making. |
| `/ai-for-behavioral-science` | Computational modeling of human behavior, n-of-1 and ecological momentary assessment, digital interventions, and experimentally validated behavior change. |
| `/ai-for-cancer-bioinformatics` | Multi-omics integration, tumor subtyping, biomarker discovery, and precision oncology using AI. |
| `/ai-for-clinical-informatics` | AI-enabled clinical decision support, EHR integration, workflow optimization, and evaluation in real-world care settings. |
| `/ai-for-cognitive-science` | Computational models of perception, memory, language, reasoning, and human-like cognition, bridging AI and psychological theory. |
| `/ai-for-digital-health` | Consumer-facing health apps, wearable biosensors, remote monitoring, patient portals, and data-driven digital wellness interventions. |
| `/ai-for-global-health` | AI for disease burden, healthcare systems, and health equity in low- and middle-income countries and resource-limited settings. |
| `/ai-for-health-economics` | Cost-effectiveness, health technology assessment, demand and pricing models, and machine learning for health outcomes research. |
| `/ai-for-health-informatics` | Electronic health records, clinical data standards, interoperability, and AI-enabled analytics for healthcare delivery and research. |
| `/ai-for-health-services-research` | AI for healthcare access, quality, utilization, policy, workforce, and health-system performance. |
| `/ai-for-immunoinformatics` | Machine learning for immune repertoire analysis, epitope prediction, vaccine design, and immunotherapy optimization. |
| `/ai-for-neuroinformatics` | Data science for brain imaging, neural signals, connectomics, and computational neuroscience workflows. |
| `/ai-for-precision-public-health` | Subpopulation-targeted prevention, genomics-guided public health, geospatial risk modeling, and equitable intervention targeting. |
| `/ai-for-art-history` | Computer vision, deep learning, and vision-language models for style classification, iconography, provenance, and quantitative art history. |
| `/ai-for-cultural-heritage` | Machine learning and deep learning for the digitization, documentation, analysis, and sustainable management of tangible and intangible cultural heritage. |
| `/ai-for-digital-humanities` | Machine learning, NLP, and network analysis for historical texts, archives, languages, and multimodal humanities collections. |
| `/ai-for-ethnomusicology` | Computational analysis of field recordings, oral musical traditions, tuning systems, and cross-cultural musical patterns using MIR and machine learning. |
| `/ai-for-folklore` | Computational folkloristics, motif and tale-type detection, and large-scale narrative analysis of folk tales, legends, and oral traditions. |
| `/ai-for-heritage-tourism` | Recommender systems, itinerary planning, visitor behavior modeling, and personalized cultural heritage experiences for sustainable tourism. |
| `/ai-for-literary-studies` | Computational stylistics, authorship attribution, genre and style analysis, and interpretive NLP for literary texts and corpora. |
| `/ai-for-museum-collections` | Computer vision, natural language processing, and metadata enrichment for cataloging, searching, and interpreting museum and archive collections. |
| `/ai-for-mythology` | Computational mythography, knowledge graphs of mythological figures, structural analysis of myths, and cross-cultural narrative comparison. |
| `/ai-for-oral-history` | Speech recognition, diarization, natural language processing, and generative AI for transcribing, indexing, and exploring oral history archives. |
| `/ai-for-preservation` | Predictive monitoring, environmental risk assessment, digital twins, and preventive conservation for built heritage and cultural collections. |
| `/ai-for-restoration` | Digital inpainting, virtual restoration, style-aware reconstruction, and diffusion models for repairing artworks, murals, and manuscripts. |
| `/ai-for-algorithms` | Learning-augmented algorithms, learned data structures, and ML-guided design for search, routing, scheduling, and data-intensive pipelines. |
| `/ai-for-approximation-algorithms` | Learning-augmented approximation, learned heuristics for NP-hard maximization and CSPs, and data-driven rounding. |
| `/ai-for-automated-reasoning` | Learning to guide proof search, premise selection, tactic prediction, and combining LLMs with symbolic reasoners. |
| `/ai-for-computational-complexity` | Using machine learning to predict, characterize, and understand the complexity of computational problems, reductions, and hardness proxies. |
| `/ai-for-constraint-programming` | ML for constraint learning, search heuristics, model acquisition, and combining CP solvers with neural predictors. |
| `/ai-for-discrete-optimization` | Learning-augmented branch-and-bound, primal heuristics, GNNs for combinatorial optimization, and data-driven algorithm configuration. |
| `/ai-for-formal-methods` | Neuro-symbolic verification, LLM-assisted autoformalization, and learned heuristics for theorem provers and model checkers. |
| `/ai-for-logic` | Neuro-symbolic reasoning, learning logical rules and constraints, probabilistic logics, and SAT/SMT/ASP guided by ML. |
| `/ai-for-program-synthesis` | Neural and symbolic program synthesis from examples, sketches, and natural language, including neurosymbolic and LLM-based code generation. |
| `/ai-for-satisfiability` | ML-enhanced SAT/SMT/QSAT solvers, end-to-end neural solvers like NeuroSAT, and learned branching and restart heuristics. |
| `/ai-for-software-verification` | ML for test generation, coverage closure, bug localization, static analysis, and verifying code produced by LLMs. |
| `/ai-for-type-theory` | ML-guided tactic prediction, premise selection, and synthesis in dependent type theories and proof assistants. |
| `/ai-for-advanced-packaging` | Co-design of 2.5D/3D chiplets, interconnect routing, signal-integrity-aware placement, and package-thermal optimization. |
| `/ai-for-chip-design` | ML for RTL generation, EDA scripting, floorplanning, placement, routing, timing optimization, and analog/mixed-signal design. |
| `/ai-for-edge-accelerators` | NPU/TPU/FPGA edge accelerator design, benchmarking, mapping, and optimization for low-latency, energy-efficient inference. |
| `/ai-for-embedded-ai` | TinyML, on-device inference, quantization, neural architecture search, and co-optimization for microcontrollers and DSPs. |
| `/ai-for-hardware-security` | ML for side-channel analysis, hardware Trojan and PUF detection, supply-chain assurance, and secure accelerator design. |
| `/ai-for-integrated-photonics` | Inverse design, layout generation, and fabrication-aware optimization of silicon-photonic and photonic-integrated-circuit components. |
| `/ai-for-memristors` | Crossbar array modeling, compute-in-memory mapping, device variability learning, and memristor-based AI accelerator co-design. |
| `/ai-for-neuromorphic-hardware` | Spiking neural network training, SNN-to-chip mapping, event-based processing, and co-design with analog/mixed-signal neuromorphic platforms. |
| `/ai-for-photonic-hardware` | Photonic AI accelerators, optical neural networks, optoelectronic co-design, and programming of photonic tensor cores. |
| `/ai-for-quantum-hardware` | ML-driven qubit control, calibration, error decoding, and quantum processor design for superconducting, trapped-ion, and neutral-atom systems. |
| `/ai-for-spintronics` | ML for magnetic material discovery, skyrmion and MRAM device modeling, spin-orbit torque optimization, and spin-wave logic. |
| `/ai-for-thermal-design` | ML surrogates for electronics cooling, data-center thermal control, heat-sink and package thermal co-design, and CFD emulation. |
| `/ai-for-allergy-immunology` | Machine learning for asthma phenotyping and exacerbation prediction, allergic rhinitis and food/drug allergy risk, anaphylaxis, and primary immunodeficiency screening. |
| `/ai-for-anesthesiology` | Machine learning for preoperative risk stratification, intraoperative hemodynamic monitoring, anesthetic depth, postoperative nausea and pain, and closed-loop anesthesia. |
| `/ai-for-endocrinology` | Machine learning for diabetes prediction and glucose forecasting, thyroid nodule risk stratification, adrenal and pituitary disorders, and bone mineral metabolism. |
| `/ai-for-hematology` | Machine learning for blood cell morphology, leukemia and lymphoma classification, thrombosis and bleeding risk, transfusion optimization, and stem-cell transplant outcomes. |
| `/ai-for-infectious-disease` | Machine learning for pathogen identification, antimicrobial resistance prediction, sepsis early warning, and infectious disease outbreak surveillance. |
| `/ai-for-nephrology` | Machine learning for chronic kidney disease progression, acute kidney injury prediction, dialysis adequacy, kidney transplant outcomes, and renal pathology image analysis. |
| `/ai-for-orthopedics` | Machine learning for fracture detection and classification, osteoarthritis grading, joint replacement outcomes, spine analysis, and sports injury risk. |
| `/ai-for-pain-management` | Machine learning for chronic pain phenotyping, opioid and analgesic response prediction, procedural guidance, and patient self-management and monitoring. |
| `/ai-for-physical-medicine` | Machine learning for electrodiagnostic studies, musculoskeletal ultrasound, gait and motion analysis, prosthetics/orthotics, and functional assessment in physiatry. |
| `/ai-for-plastic-surgery` | Machine learning for aesthetic and reconstructive surgical planning, facial analysis, flap monitoring, wound assessment, and patient-reported outcomes. |
| `/ai-for-rehabilitation` | Machine learning for stroke, spinal cord, and traumatic brain injury rehabilitation, robotic and virtual-reality therapy, telerehabilitation, and wearable sensor monitoring. |
| `/ai-for-rheumatology` | Machine learning for autoimmune disease diagnosis and phenotyping, flare prediction, treatment response in RA and SLE, and imaging-based joint inflammation scoring. |
| `/ai-for-ai-ethics` | Fairness, accountability, transparency, privacy, and value alignment in AI systems, including bias auditing, model cards, and stakeholder deliberation. |
| `/ai-for-ai-governance` | Risk management, accountability, lifecycle governance, standards, and multi-stakeholder oversight for trustworthy and responsible AI organizations. |
| `/ai-for-ai-policy` | Regulatory analysis, risk classification, standards mapping, policy evaluation, and evidence synthesis for national and international AI governance. |
| `/ai-for-ai-safety` | Alignment, robustness, interpretability, red teaming, monitoring, and safe deployment of AI systems, especially large language and agentic models. |
| `/ai-for-computational-design` | Differentiable simulation, topology optimization, CAD-aware generative models, and solver-in-the-loop co-design for architecture, products, and structures. |
| `/ai-for-digital-twin-simulation` | High-fidelity virtual replicas, real-time synchronization, physics-informed and data-driven simulation, and AI training environments for cyber-physical systems. |
| `/ai-for-future-of-work` | Automation and augmentation analysis, skill demand forecasting, workforce transitions, algorithmic management, and human-centered labor market policy. |
| `/ai-for-generative-engineering` | Diffusion, VAE, and generative inverse design for engineering concepts, constraint-aware generation, and performance-conditioned shape and material synthesis. |
| `/ai-for-human-centered-ai` | Human-AI interaction, explainability, trust, feedback loops, participatory design, and human-in-the-loop ML to keep people at the center of AI systems. |
| `/ai-for-responsible-innovation` | Anticipatory governance, ethical deliberation, stakeholder engagement, regulatory foresight, and impact assessment for emerging AI technologies. |
| `/ai-for-synthetic-data` | Generative models, differential privacy, tabular/image/text synthesis, and utility-privacy evaluation for creating realistic synthetic datasets. |
| `/ai-for-tech-forecasting` | Patent and publication analysis, trend extrapolation, expert elicitation, and ML models for predicting technological progress and emerging AI capabilities. |
| `/ai-for-aging` | Machine learning for geriatric health monitoring, aging-in-place, fall prevention, cognitive and social support, and age-friendly AI design. |
| `/ai-for-child-health` | Machine learning for pediatric diagnostics, developmental surveillance, pediatric AI readiness, and risk stratification for children. |
| `/ai-for-dementia-care` | Machine learning for cognitive impairment screening, dementia risk stratification, voice and EHR analytics, and caregiver support. |
| `/ai-for-disability-inclusion` | Accessible AI, disability-aware bias evaluation, inclusive design, and assistive technologies that respect the rights and agency of people with disabilities. |
| `/ai-for-humanitarian-aid` | AI across the crisis management cycle: needs assessment, resource allocation, routing, damage assessment, and early warning for disaster response. |
| `/ai-for-hunger-relief` | AI/ML for food-security early warning, acute food-insecurity forecasting, remote-sensing crop monitoring, and targeted food assistance. |
| `/ai-for-maternal-health` | Machine learning for maternal risk stratification, preterm birth prediction, obstetric decision support, and neonatal outcome forecasting. |
| `/ai-for-mental-health-services` | LLM and multimodal mental health screening, CBT chatbots, psychosocial risk assessment, and clinical interview support. |
| `/ai-for-palliative-care` | Machine learning for prognostication, symptom management, hospice suitability, advance care planning, and ethical decision support in end-of-life care. |
| `/ai-for-poverty-alleviation` | Machine learning for poverty mapping, consumption estimation, proxy means testing, and targeted social protection in low-resource settings. |
| `/ai-for-refugees` | Machine learning for forced-displacement forecasting, refugee camp mapping, asylum-flow prediction, and humanitarian response planning. |
| `/ai-for-rural-health` | AI-driven diagnostics, telemedicine, rural health equity, and resource allocation for underserved and remote populations. |
| `/ai-for-data-journalism` | Using AI to find stories in datasets, fact-check claims, generate visualizations, and produce data-driven reporting. |
| `/ai-for-document-design` | Automating layout, typography, templates, and multi-format rendering of reports, certificates, and proposals. |
| `/ai-for-infographics` | Generating data-rich infographics and visual stories from documents, tables, and natural-language prompts. |
| `/ai-for-knowledge-design` | Designing knowledge architectures, taxonomies, ontologies, and agent-facing knowledge layers for organizations. |
| `/ai-for-open-science` | Reproducible research agents, open-source workbenches, provenance tracking, and computational reproducibility with AI. |
| `/ai-for-policy-briefs` | Converting scientific evidence and legislative text into concise, actionable policy briefs and impact analyses. |
| `/ai-for-public-engagement` | Conversational agents, citizen science, public consultations, and participatory science supported by LLMs and interactive AI. |
| `/ai-for-research-communication` | Drafting manuscripts, abstracts, cover letters, response-to-reviewers, and translating findings across disciplines with LLMs. |
| `/ai-for-science-communication` | Plain-language summaries, research storytelling, audience adaptation, and ethical, evidence-based use of generative AI for public-facing science. |
| `/ai-for-technical-blogs` | Planning, drafting, SEO-optimizing, and reviewing technical blog posts and tutorials with LLMs. |
| `/ai-for-visual-communication` | Generating and refining posters, slides, brand assets, and visual narratives with diffusion models and design tools. |
| `/ai-for-white-papers` | Authoring long-form, evidence-based white papers and thought-leadership documents grounded in verified sources. |
| `/ai-for-comparative-genomics` | Cross-species and population genome comparison, orthology inference, phylogenomics, selection scans, and pan-genome analysis. |
| `/ai-for-epigenomics` | DNA methylation, histone modifications, chromatin accessibility, enhancer-promoter interactions, and deep learning models of gene regulation. |
| `/ai-for-functional-genomics` | Predicting gene regulatory function from sequence and epigenomic data, mapping cis-regulatory elements, and interpreting non-coding variants. |
| `/ai-for-immunogenomics` | MHC and peptide binding prediction, TCR/BCR repertoire analysis, epitope and neoantigen prediction, and immunoinformatics. |
| `/ai-for-lipidomics` | LC-MS/MS lipid species quantification, structural isomer resolution, lipid class normalization, and predictive modeling of lipid phenotypes. |
| `/ai-for-metabolomics` | Mass spectrometry and NMR metabolite profiling, annotation, pathway analysis, normalization, and machine learning for biomarker discovery. |
| `/ai-for-metagenomics` | 16S rRNA and shotgun microbial community profiling, taxonomic and functional prediction, MAG binning, and microbiome-host association modeling. |
| `/ai-for-proteomics` | Mass spectrometry protein identification and quantification, DDA/DIA workflows, post-translational modifications, and AI-driven peptide property prediction. |
| `/ai-for-single-cell` | Single-cell transcriptomics, epigenomics, proteomics, and multi-omics integration, cell type annotation, trajectory inference, and foundation models. |
| `/ai-for-spatial-omics` | Spatially resolved transcriptomics and proteomics, cell segmentation, neighborhood analysis, and integration with imaging data. |
| `/ai-for-structural-genomics` | 3D genome organization, Hi-C analysis, protein structure prediction with deep learning, and multiscale structural modeling. |
| `/ai-for-transcriptomics` | Bulk and single-cell RNA-seq analysis, normalization, clustering, differential expression, splicing, and foundation models for gene expression. |
| `/ai-for-aerospace-engineering` | AI for aerodynamic design, propulsion, structural analysis, flight dynamics, GNC, and certification of aerospace vehicles. |
| `/ai-for-biomedical-engineering` | AI for medical devices, wearable biosensors, biomechanics, neural engineering, tissue engineering, and clinical diagnostics. |
| `/ai-for-chemical-engineering` | AI for process design, optimization, control, reaction engineering, materials discovery, and digital chemical plants. |
| `/ai-for-civil-engineering` | Machine learning for structural health monitoring, geotechnical prediction, transportation systems, water resources, and resilient infrastructure. |
| `/ai-for-electrical-engineering` | AI for power systems, smart grids, renewable integration, power electronics, fault diagnosis, and energy management. |
| `/ai-for-environmental-engineering` | AI for water and wastewater treatment, air quality, climate modeling, waste management, and environmental monitoring. |
| `/ai-for-industrial-engineering` | AI for production planning, scheduling, quality control, ergonomics, operations research, and process improvement. |
| `/ai-for-mechanical-engineering` | AI for mechanical design, predictive maintenance, digital twins, dynamic systems, and manufacturing process optimization. |
| `/ai-for-petroleum-engineering` | AI for reservoir characterization, production optimization, well placement, drilling, and digital oilfield twins. |
| `/ai-for-software-engineering` | AI for code generation, testing, debugging, program repair, code review, and design assistance. |
| `/ai-for-systems-engineering` | AI for architecting complex systems, model-based systems engineering (MBSE), requirements analysis, trade studies, and verification. |
| `/ai-for-telecommunications` | AI for wireless networks, 5G/6G, network optimization, traffic forecasting, security, and edge intelligence. |
| `/ai-for-biomarkers` | Machine learning for omics-based biomarker discovery, sparse signature selection, multi-modal integration, and clinical validation. |
| `/ai-for-clinical-trials` | Machine learning for clinical-trial design, patient eligibility, cohort selection, outcome prediction, and operational monitoring across the trial lifecycle. |
| `/ai-for-cohort-studies` | Machine learning for risk prediction, confounding control, survival analysis, and biomarker discovery in prospective and retrospective cohort studies. |
| `/ai-for-evidence-synthesis` | AI and LLMs for systematic review automation, risk-of-bias assessment, evidence mapping, and trustworthy synthesis of research findings. |
| `/ai-for-longitudinal-studies` | Machine learning and deep learning for repeated measurements, time-varying covariates, missing data, trajectories, and outcomes in longitudinal cohorts and EHR data. |
| `/ai-for-meta-analysis` | Machine learning and LLMs for automating literature search, screening, data extraction, effect-size estimation, and heterogeneity assessment in meta-analyses. |
| `/ai-for-observational-studies` | Causal machine learning for treatment-effect estimation, propensity scoring, confounding adjustment, and sensitivity analysis in observational data. |
| `/ai-for-patient-reported-outcomes` | Machine learning for predicting, personalizing, and reducing the burden of patient-reported outcome measures and PRO-based treatment decisions. |
| `/ai-for-randomized-trials` | Machine learning for heterogeneous treatment effects, covariate adjustment, adaptive randomization, and efficient inference in randomized controlled trials. |
| `/ai-for-real-world-evidence` | Machine learning for extracting, validating, and synthesizing real-world evidence from EHRs, claims, registries, and wearables for regulatory and clinical decisions. |
| `/ai-for-registry-studies` | Machine learning for patient registries, disease surveillance, regulatory-grade real-world evidence, and longitudinal outcome tracking. |
| `/ai-for-synthetic-controls` | Machine learning for constructing, validating, and extending synthetic and virtual control arms from observational data to augment clinical and policy evaluation. |
| `/ai-for-data-curation` | Automated selection, cleaning, labeling, augmentation, and documentation of datasets to produce high-quality, FAIR, and reusable ML data assets. |
| `/ai-for-data-discovery` | Intelligent dataset search, metadata enrichment, schema inference, and conversational data catalog exploration to find the right data quickly. |
| `/ai-for-data-ethics` | Fairness, accountability, transparency, data dignity, consent, and responsible data use in ML pipelines and AI systems. |
| `/ai-for-data-governance` | Automated policy enforcement, metadata management, data lineage, stewardship, and AI-driven regulatory compliance for enterprise data governance. |
| `/ai-for-data-marketplaces` | AI for data and model discovery, pricing, valuation, matching, trust, and governance in data-sharing marketplaces and AI model markets. |
| `/ai-for-data-monetization` | Data valuation, pricing, data products, marketplaces, and revenue allocation for turning data assets into measurable business value. |
| `/ai-for-data-observability` | ML-driven monitoring of data freshness, schema drift, volume anomalies, lineage breaks, and pipeline health to ensure reliable data operations. |
| `/ai-for-data-privacy` | Differential privacy, federated learning, homomorphic encryption, PETs, and privacy-preserving ML for sensitive data. |
| `/ai-for-data-provenance` | Lineage tracking, W3C PROV, reproducible ML pipelines, experiment tracking, and provenance for explainable and trustworthy AI. |
| `/ai-for-data-quality` | Automated profiling, anomaly detection, data cleaning, imputation, validation, and continuous data quality monitoring for ML and analytics. |
| `/ai-for-data-security` | Adversarial robustness, data poisoning detection, access control, threat detection, and AI-driven security for ML training and inference data. |
| `/ai-for-data-sharing` | Federated learning, data sharing incentives, interoperability, trust, and privacy-preserving collaboration for shared data ecosystems. |
| `/ai-for-5g` | AI/ML for 5G RAN optimization, network slicing, beam management, mobility, and core automation. |
| `/ai-for-6g` | AI-native 6G architectures, semantic communications, integrated sensing and communication, reconfigurable intelligent surfaces, and distributed learning. |
| `/ai-for-edge-computing` | Model compression, inference offloading, task placement, federated learning, and MLOps at the network edge. |
| `/ai-for-fog-computing` | AI for hierarchical fog resource management, task scheduling, load balancing, latency optimization, and IoT-fog-cloud orchestration. |
| `/ai-for-iot` | TinyML, edge AI, anomaly detection, device fingerprinting, and predictive maintenance for IoT systems. |
| `/ai-for-network-management` | AIOps for network monitoring, anomaly detection, root-cause analysis, configuration management, and predictive maintenance. |
| `/ai-for-network-optimization` | Graph neural networks, deep reinforcement learning, traffic engineering, resource allocation, and learning-augmented optimization for routing, load balancing, and network design. |
| `/ai-for-network-security` | Intrusion detection, malware classification, anomaly detection, adversarial defenses, and threat intelligence using ML and LLMs. |
| `/ai-for-optical-networks` | ML for optical performance monitoring, QoT estimation, traffic prediction, nonlinearity compensation, and optical layer provisioning. |
| `/ai-for-satellite-communications` | ML for satellite link prediction, beam hopping, resource allocation, non-terrestrial networks, and onboard edge AI. |
| `/ai-for-software-defined-networks` | ML-driven traffic classification, routing, QoS/QoE prediction, resource management, and security in SDN control and data planes. |
| `/ai-for-wireless-communications` | ML for channel estimation, modulation recognition, MIMO, spectrum sensing, and end-to-end physical-layer design. |
| `/ai-for-agricultural-economics` | Machine learning and econometric ML for farm decision support, risk, policy, market analysis, adoption, and the economics of digital agriculture. |
| `/ai-for-agricultural-robots` | Perception, motion planning, and control for autonomous robots that weed, spray, scout, and harvest in field and greenhouse environments. |
| `/ai-for-aquaculture` | Machine learning for water quality, feeding, disease, and stock management in fish, shrimp, and shellfish farming. |
| `/ai-for-crop-protection` | Machine and deep learning for detecting crop diseases, pests, weeds, and abiotic stresses and for supporting timely, targeted protection decisions. |
| `/ai-for-dairy` | Machine learning for health, fertility, behaviour, and production monitoring in dairy cattle and dairy farm decision support. |
| `/ai-for-irrigation` | Machine learning for predicting crop water demand, scheduling irrigation, and optimising water use through IoT and weather data integration. |
| `/ai-for-livestock` | Machine learning for health, behaviour, welfare, grazing, and reproduction across cattle, pigs, sheep, goats, and other farm animals. |
| `/ai-for-pest-management` | Machine and deep learning for pest detection, identification, population monitoring, and integrated pest management decision support. |
| `/ai-for-plant-breeding` | Genomic selection, phenotype prediction, multi-environment trial analysis, and marker-assisted breeding with machine and deep learning. |
| `/ai-for-poultry` | AI for flock health, welfare, behaviour, environmental control, and productivity in broiler, layer, and turkey production. |
| `/ai-for-soil-health` | Machine learning for predicting soil carbon, nutrients, biology, compaction, erosion risk, and overall soil health from sensors and remote sensing. |
| `/ai-for-viticulture` | AI for vineyard monitoring, grape and canopy sensing, disease detection, yield and quality prediction, and harvest decision support. |
| `/ai-for-budgeting` | Public expenditure forecasting, budget allocation optimization, fiscal scenario analysis, program-cost modeling, and spending anomaly detection. |
| `/ai-for-civic-tech` | Digital participation, deliberation, civic engagement, public comment analysis, and participatory budgeting tools powered by AI. |
| `/ai-for-e-government` | Chatbots and virtual assistants, proactive public services, document automation, eligibility screening, and responsible AI in digital government. |
| `/ai-for-permitting` | Automated permit intake, plan review, code compliance checks, application completeness screening, and permit workflow optimization. |
| `/ai-for-public-records` | Automated records classification, sensitivity review, metadata enrichment, archival appraisal, and access to digital government archives. |
| `/ai-for-public-transport` | Ridership prediction, service scheduling, bus and rail dispatch optimization, disruption recovery, and multi-modal transit analytics. |
| `/ai-for-public-utilities` | Smart grid load forecasting, water and energy demand prediction, asset maintenance, leak and outage detection, and resource allocation. |
| `/ai-for-social-services` | Eligibility screening, benefits triage, case management support, risk stratification, and resource matching for social care and public assistance. |
| `/ai-for-taxation` | Tax compliance risk scoring, fraud and evasion detection, audit selection, taxpayer assistance, and revenue forecasting. |
| `/ai-for-urban-planning` | Spatial plan generation, land-use optimization, urban digital twins, scenario simulation, and participatory planning analytics. |
| `/ai-for-veterans-services` | Claims processing, benefits eligibility, health risk identification, veteran-centered care coordination, and administrative automation at VA and related agencies. |
| `/ai-for-zoning` | Zoning code interpretation, compliance checking, variance analysis, automated answers to zoning questions, and land-use regulation analytics. |
| `/ai-for-charging-infrastructure` | Machine learning for EV charging demand forecasting, station scheduling, load balancing, and grid-integrated charging control. |
| `/ai-for-demand-response` | Machine learning for load flexibility estimation, demand response program design, virtual power plant dispatch, and dynamic pricing. |
| `/ai-for-distributed-energy` | Machine learning and multi-agent methods for DER forecasting, microgrid optimization, peer-to-peer trading, and prosumer coordination. |
| `/ai-for-electric-vehicles` | Machine learning for battery management, range and energy consumption prediction, predictive maintenance, and EV powertrain optimization. |
| `/ai-for-energy-storage` | Machine learning for battery state estimation, degradation modeling, storage dispatch, and energy storage asset optimization. |
| `/ai-for-energy-trading` | Machine learning for electricity price forecasting, algorithmic trading, arbitrage, and bidding in day-ahead, intraday, and balancing markets. |
| `/ai-for-gas-utilities` | Machine learning for natural gas demand forecasting, pipeline leak detection, compressor optimization, and asset integrity. |
| `/ai-for-grid-resilience` | Machine learning for outage prediction, storm hardening, restoration planning, and cyber-physical resilience of power systems. |
| `/ai-for-renewable-energy` | Machine learning for solar, wind, and other renewable energy forecasting, resource assessment, yield optimization, and predictive O&M. |
| `/ai-for-smart-grid` | AI and machine learning for load and renewable forecasting, grid state estimation, optimal power flow, and smart-grid control. |
| `/ai-for-wastewater` | Machine learning for process monitoring, anomaly detection, influent forecasting, and control in wastewater treatment plants. |
| `/ai-for-water-utilities` | Machine learning for water demand forecasting, leak detection, quality monitoring, pump scheduling, and smart water distribution. |
| `/ai-for-building-operations` | Smart building control, energy optimization, occupant-centric HVAC and lighting, and IoT-BMS integration for operational performance. |
| `/ai-for-city-modeling` | Urban digital twins, 3D city reconstruction, generative city models, and AI-driven urban simulation for planning and operations. |
| `/ai-for-construction-management` | BIM-NLP integration, 4D/5D digital twins, computer-vision progress monitoring, and AI-driven scheduling and cost control for construction. |
| `/ai-for-facilities-management` | Predictive maintenance, fault detection, digital twins, and AI-enabled asset lifecycle management for built facilities. |
| `/ai-for-land-use` | Remote sensing, multi-source data fusion, functional-zone mapping, and neural-symbolic planning for land-use analysis and policy. |
| `/ai-for-lease-management` | NLP-based lease abstraction, clause extraction, compliance tracking, and predictive analytics for commercial and residential lease portfolios. |
| `/ai-for-portfolio-optimization` | Diversification, risk-return balancing, rebalancing strategies, and generative-AI analytics for real estate and mixed-asset portfolios. |
| `/ai-for-property-valuation` | Automated valuation models, hedonic pricing, spatial machine learning, and deep learning for residential and commercial property appraisal. |
| `/ai-for-real-estate-investment` | Predictive analytics, investment screening, REIT return forecasting, and risk-adjusted underwriting for real estate investment decisions. |
| `/ai-for-site-selection` | Geospatial ML, graph neural networks, urban knowledge graphs, and location analytics for retail, logistics, and facility siting. |
| `/ai-for-tenant-experience` | Personalization, occupancy analytics, indoor environmental quality, and tenant engagement for workplace and residential environments. |
| `/ai-for-urban-development` | GeoAI, spatial modeling, generative urban design, and scenario simulation for sustainable, equitable, and data-driven urban development. |
| `/ai-for-defect-detection` | Computer vision, anomaly detection, and segmentation for automated inspection of surface, PCB, casting, and assembly defects in manufacturing quality control. |
| `/ai-for-digital-manufacturing` | AI-driven digital twins, virtual commissioning, real-time simulation, and lifecycle data integration for smart, connected factories. |
| `/ai-for-discrete-manufacturing` | Machine learning for assembly, machining, electronics, and automotive part production: process planning, scheduling, robotic assembly, and work-in-progress tracking. |
| `/ai-for-factory-automation` | ML-integrated PLCs, edge controllers, motion control, robot programming, and real-time AI inference on the shop floor. |
| `/ai-for-industrial-iot` | Industrial Internet of Things, edge-fog-cloud architectures, and AI for real-time monitoring, predictive maintenance, and secure shop-floor connectivity. |
| `/ai-for-lean-manufacturing` | Data-driven waste elimination, value stream mapping, bottleneck detection, and Kaizen prioritization for flow, pull, and just-in-time systems. |
| `/ai-for-manufacturing-analytics` | KPI dashboards, OEE analysis, descriptive-to-prescriptive analytics, and association mining for manufacturing performance management. |
| `/ai-for-predictive-quality` | In-process quality forecasting, virtual metrology, and causal quality models that predict final part quality from machine and sensor data before completion. |
| `/ai-for-process-manufacturing` | Machine learning for continuous and batch chemical, pharmaceutical, food, and materials processes: recipe optimization, soft sensors, advanced process control, and real-time quality prediction. |
| `/ai-for-root-cause-analysis` | Knowledge graphs, causal discovery, graph neural networks, and SHAP-based diagnostics for identifying fault origins and propagations in complex systems. |
| `/ai-for-six-sigma` | ML-augmented DMAIC for defect reduction, statistical process control, capability analysis, and automated root-cause prioritization in quality improvement. |
| `/ai-for-total-productive-maintenance` | AI and IIoT for autonomous maintenance, OEE improvement, zero-breakdown programs, and condition-based monitoring across the eight TPM pillars. |
| `/ai-for-additive-manufacturing` | Machine learning for powder-bed fusion, directed energy deposition, in-situ monitoring, defect detection, build simulation, and process parameter optimization in additive manufacturing. |
| `/ai-for-casting` | Machine learning for sand, investment, die, and continuous casting: defect prediction, mold filling, solidification, microstructure, and process optimization. |
| `/ai-for-coatings` | Machine learning for coating formulation, deposition, thickness, microstructure, adhesion, corrosion protection, and service-life prediction. |
| `/ai-for-composites-manufacturing` | Machine learning for automated fiber placement, tape laying, resin infusion, cure monitoring, defect detection, and process optimization in composite part manufacturing. |
| `/ai-for-corrosion-engineering` | Machine learning for corrosion rate prediction, risk-based inspection, cathodic protection, coating lifetime, EIS interpretation, and materials selection. |
| `/ai-for-metal-forming` | Machine learning for sheet-metal stamping, deep drawing, forging, rolling, extrusion, springback prediction, die design, and forming-limit prediction. |
| `/ai-for-nanomanufacturing` | Machine learning for nanoscale fabrication, roll-to-roll processing, nanoimprint lithography, self-assembly, nanoscale metrology, and process control. |
| `/ai-for-polymer-processing` | Machine learning for extrusion, injection molding, blow molding, compounding, mixing, and polymer recycling process optimization and quality control. |
| `/ai-for-semiconductor-manufacturing` | Machine learning for semiconductor fabrication yield enhancement, wafer defect detection, equipment fault classification, process control, and advanced lithography/etch modeling. |
| `/ai-for-surface-engineering` | Machine learning for surface modification processes: thermal spray, laser cladding/peening, shot peening, plasma electrolytic oxidation, surface texturing, and residual stress optimization. |
| `/ai-for-textile-manufacturing` | Machine learning for yarn, fabric, and garment manufacturing: spinning, weaving, knitting, dyeing, finishing, quality inspection, and production optimization. |
| `/ai-for-welding` | Machine learning for arc, laser, and resistance welding: penetration prediction, defect detection, bead geometry, process monitoring, and parameter optimization. |

## Usage

### In Devin
1. Copy the `.devin/` directory into your project root (or symlink it).
2. Skills are automatically discovered and invoked by the agent based on task relevance.
3. Workflows are invoked via `/workflow-name` slash commands.

### In Cursor
1. Copy the `.cursor/` directory into your project root (or symlink `skills/` and `commands/`).
2. **Skills** live in `.cursor/skills/<name>/SKILL.md` — auto-suggested by the agent when relevant.
3. **Commands** live in `.cursor/commands/<name>.md` — invoked via `/name` in chat or referenced explicitly.
4. See `.cursor/README.md` for the full inventory and bootstrap guide.

**Cursor-only extras** (beyond the shared Devin set):
- Domain: `dgx-spark-cosmos3`, `nemotron-agent-loop`, `endosight-3d-pipeline`, `3d-reconstruction-best-practices`, `agentic-loop-design`, `spark-hardware-optim`, `surgical-video-data-pipeline`
- MOT: `mot-training-workflow`, `mot-repo-orientation`, `mot-browser-research`
- Cosmos/Spark commands: `/cosmos-verify`, `/esd-forward-dynamics`, `/esd-t2v`, `/lap-t2v`, `/cosmos-spark-kernels`
- Cursor workflow skills: `/review-bugbot`, `/ship-pr`, `/babysit-pr`, `/impact-aware-testing`, `/iterative-test-loop`, `/explore-sota`, `/fix-ci`, `/split-to-prs`

### Skill vs Workflow: When to use which

- **Skills** are auto-invoked by the Devin agent when it detects a relevant task. Use for
  knowledge that should be available on-demand (e.g., debugging guides, hyperparameter tables).
- **Workflows** are manually triggered via `/name` when you want to follow a specific
  step-by-step procedure (e.g., `/pretrain-and-evaluate`, `/code-review`).
- This repo provides both for every topic — use the skill for reference, the workflow for execution.

## Structure

```
mcp_servers/                   # 7 MCP servers, 72 tools (dual CLI + MCP)
├── dgx_monitor/server.py      # GPU/memory/Docker/conda/CUDA monitoring
├── cuda_profiling/server.py   # nsys/ncu/compute-sanitizer/SASS/PTX
├── distributed_training/server.py  # Multi-GPU/NCCL/DDP/FSDP
├── cloud_gpu_ssh/server.py    # Remote GPU SSH (Lambda/RunPod/Vast)
├── tpu_jax/server.py          # JAX/TPU/gcloud TPU management
├── endosight_pipeline/server.py   # Endosight 3D pipeline monitoring
├── research_workflow/server.py    # ArXiv/BibTeX/experiments/Semantic Scholar
├── install_all.sh             # Install all servers into all agents
├── README.md                  # Full MCP server documentation
└── MASTERPLAN.md              # Design rationale and architecture

.devin/
├── skills/                    # 168 SKILL.md files (auto-invoked)
│   ├── ablation-study/
│   ├── address-pr-comments/
│   ├── aire-slurm-submit/
│   ├── checkpoint-to-deployment/
│   ├── ci-cd-setup/
│   ├── code-quality/
│   ├── code-review/
│   ├── conda-env-setup/
│   ├── continual-learning/
│   ├── data-management/
│   ├── debug-pytorch-gpu/
│   ├── deep-research/
│   ├── debug-training/
│   ├── dependency-management/
│   ├── experiment-tracking/
│   ├── git-branch-workflow/
│   ├── lora-finetune/
│   ├── paper-code-release/
│   ├── paper-submission-prep/
│   ├── pcos-routing/
│   ├── pcos-chrome-ai/
│   ├── pcos-android-litert/
│   ├── pcos-bridge/
│   ├── pcos-privacy/
│   ├── pcos-deploy/
│   ├── pre-commit-setup/
│   ├── pretrain-and-evaluate/
│   ├── refactor-extract-module/
│   ├── release-checklist/
│   ├── reproducibility/
│   ├── reproducibility-checklist/
│   ├── setup-ml-project/
│   ├── submit-gpu-job/
│   ├── surgical-mot-eval/
│   ├── tdv-pretrain/
│   ├── testing-strategy/
│   └── wandb-experiment/
└── workflows/                 # 154 workflow .md files (slash commands)
    ├── ablation-study.md
    ├── address-pr-comments.md
    ├── aire-slurm-submit.md
    ├── checkpoint-to-deployment.md
    ├── ci-cd-setup.md
    ├── code-quality.md
    ├── code-review.md
    ├── conda-env-setup.md
    ├── continual-learning.md
    ├── data-management.md
    ├── debug-pytorch-gpu.md
    ├── debug-training.md
    ├── deep-research.md
    ├── dependency-management.md
    ├── experiment-tracking.md
    ├── git-branch-workflow.md
    ├── lora-finetune.md
    ├── paper-code-release.md
    ├── paper-submission-prep.md
    ├── pre-commit-setup.md
    ├── pretrain-and-evaluate.md
    ├── refactor-extract-module.md
    ├── release-checklist.md
    ├── reproducibility-checklist.md
    ├── pcos-add-chrome-api.md
    ├── pcos-debug-routing.md
    ├── pcos-setup.md
    ├── pcos-test.md
    ├── reproducibility.md
    ├── setup-ml-project.md
    ├── submit-gpu-job.md
    ├── surgical-mot-eval.md
    ├── tdv-pretrain.md
    ├── testing-strategy.md
    └── wandb-experiment.md

.cursor/
├── skills/                    # 181 SKILL.md files (auto-suggested)
│   ├── 3d-reconstruction-best-practices/
│   ├── ablation-study/
│   ├── agentic-loop-design/
│   ├── dgx-spark-cosmos3/
│   ├── endosight-3d-pipeline/
│   ├── mot-training-workflow/
│   ├── nemotron-agent-loop/
│   ├── reproducibility/
│   ├── tdv-pretrain/
│   └── ... (see .cursor/README.md)
├── commands/                  # 164 command .md files (/name)
│   ├── pretrain-and-evaluate.md
│   ├── code-review.md
│   ├── cosmos-verify.md
│   ├── esd-forward-dynamics.md
│   └── ...
└── README.md
```

## License

MIT
