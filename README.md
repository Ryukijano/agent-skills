# agent-skills

Reusable **Devin** and **Cursor** skills and workflows for cross-project AI-assisted development.
Designed for research scientists and software engineers working on ML projects (surgical video MOT, HPC, DGX Spark, 3D recon, agentic loops) and **PCOS edge agent** development.

## Overview

| Platform | Skills | Workflows / Commands |
|----------|--------|----------------------|
| **Devin** (`.devin/`) | 248 | 234 workflows (`/name`) |
| **Cursor** (`.cursor/`) | 261 | 244 commands (`/name`) |
| **MCP Servers** (`mcp_servers/`) | 7 servers | 72 tools (dual CLI + MCP) |
| **Hugging Face Skills** | 12 | Hub, datasets, training, eval, papers, Gradio |
| **NVIDIA Skills** | 22 | NeMo, Megatron-Core, DALI, CUDA-Q, DeepStream |

- Every major topic has both a **skill** and a **workflow/command**.
- **MCP servers** provide live tools that agents call at runtime — GPU monitoring, CUDA profiling, distributed training, cloud GPU SSH, TPU/JAX, endosight pipeline, and research workflows.
- **Hugging Face skills** (installed via `npx skills add huggingface/skills`) give agents access to the HF Hub: model search, dataset exploration, LLM/vision training, evaluation, paper lookup, and Gradio demos.
- **NVIDIA skills** (installed via `npx skills add nvidia/skills`) provide NeMo distributed training, Megatron-Core, DALI, CUDA-Q, and DeepStream expertise.

Every major topic has both a **skill** (reference knowledge, auto-suggested) and a **workflow/command** (step-by-step procedure).

Skills use **progressive disclosure**: only `name` and `description` are loaded until the agent invokes them, keeping context lean.

## Skills (248)

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

### Custom Research Skills (111)

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

## Workflows (234)

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

### Custom Research Workflows (111)

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
