# MCP Servers and Tools

Custom MCP servers for the DGX Spark that work both as direct CLI tools AND as MCP tools for AI coding agents (Cursor, Devin, Claude, Windsurf, Gemini). Covers GPU monitoring, CUDA profiling, distributed training, cloud GPU management, TPU/JAX, endosight pipeline, and research workflows.

## Quick Start

```bash
# 1. Install all MCP servers into all agents
bash install_all.sh

# 2. Test a server in CLI mode
python3 servers/dgx_monitor/server.py --cli gpu_status
python3 servers/distributed_training/server.py --cli list_gpus

# 3. Test with MCP Inspector (web UI)
npx @modelcontextprotocol/inspector python3 servers/dgx_monitor/server.py

# 4. Restart your AI agents to pick up the new servers
```

## What's Included

### 7 Custom MCP Servers

| Server | Tools | Purpose |
|--------|-------|---------|
| **dgx-monitor** | 15 | GPU status, memory, Docker, conda, CUDA info, kernel compilation, NVDEC/NVENC, bandwidth tests |
| **cuda-profiling** | 13 | nsys/ncu profiling, compute-sanitizer, SASS/PTX dump, benchmarking, GPU info, kernel compilation |
| **distributed-training** | 12 | Multi-GPU discovery, NCCL diagnostics, DDP/FSDP setup, training job management, checkpoints |
| **cloud-gpu-ssh** | 16 | Remote GPU machine management (Lambda/RunPod/Vast/SSH), remote commands, file sync |
| **tpu-jax** | 10 | JAX device discovery, TPU info, gcloud TPU management, JAX profiling, memory info |
| **endosight-pipeline** | 13 | Pipeline status, clip listing, reconstruction stats, verification, crop/QA/video export, logs |
| **research-workflow** | 11 | ArXiv search, paper download, BibTeX, experiment tracking, repro bundles, Semantic Scholar, citations |

### NVIDIA & Community MCP Servers (Installed)

| Server | Type | Purpose |
|--------|------|---------|
| **nvidia-cuda-docs** | NVIDIA hosted | Up-to-date CUDA documentation for agents |
| **wandb** | Hosted | Weights & Biases experiment tracking (needs `WANDB_API_KEY`) |
| **mlflow** | Local | MLflow trace management (needs `pip install mlflow[mcp]`) |

### 22 NVIDIA Agent Skills (Installed via `npx skills add`)

| Category | Skills |
|----------|--------|
| **Distributed Training** | nemo-automodel-distributed-training, nemo-automodel-launcher-config, nemo-automodel-model-onboarding, nemo-automodel-recipe-development |
| **Megatron-Core** | mcore-run-on-slurm |
| **NeMo MBridge** | nemo-mbridge-multi-node-slurm, nemo-mbridge-perf-parallelism-strategies, nemo-mbridge-perf-megatron-fsdp, nemo-mbridge-perf-memory-tuning, nemo-mbridge-perf-cuda-graphs, nemo-mbridge-perf-activation-recompute, nemo-mbridge-perf-cpu-offloading, nemo-mbridge-perf-sequence-packing, nemo-mbridge-perf-moe-optimization-workflow, nemo-mbridge-recipe-recommender, nemo-mbridge-resiliency |
| **NeMo RL** | launch-nemo-rl |
| **NeMo Other** | nemo-retriever |
| **Data Loading** | dali-dynamic-mode |
| **Quantum** | cudaq-guide |
| **Video Analytics** | deepstream-dev, deepstream-profile-pipeline |

## Dual CLI + MCP Interface

Every server has two modes:

```bash
# CLI mode — you use it directly
python3 servers/dgx_monitor/server.py --cli gpu_status
python3 servers/distributed_training/server.py --cli torch_distributed_info
python3 servers/cloud_gpu_ssh/server.py --cli list_machines
python3 servers/tpu_jax/server.py --cli jax_devices

# MCP mode — agents call it via stdio
# (configured automatically by install_all.sh)
```

## Available Tools by Server

### DGX Monitor (`dgx-monitor`)

| Tool | What it does |
|------|-------------|
| `gpu_status` | GPU utilization, memory (with GB10 unified memory fallback) |
| `gpu_processes` | Processes using GPU memory |
| `kill_gpu_process` | Kill a GPU process by PID |
| `system_memory` | System RAM usage (critical for unified memory) |
| `disk_usage` | Disk space check |
| `docker_ps` | Running containers |
| `docker_logs` | Container logs |
| `docker_gpu_stats` | Which containers are using GPU |
| `conda_envs` | List conda environments |
| `conda_packages` | List packages in an environment |
| `cuda_info` | CUDA/nvcc/driver versions |
| `compile_cuda` | Compile .cu with correct SM121 flags |
| `nvdec_status` | NVDEC/NVENC encoder session stats |
| `top_gpu_processes` | Top GPU memory-consuming processes by used memory |
| `bandwidth_test` | Tiny CUDA memcpy bandwidth benchmark (D2D, H2D, D2H) |

### CUDA Profiling (`cuda-profiling`)

| Tool | What it does |
|------|-------------|
| `profile_nsys` | Nsight Systems timeline profiling |
| `parse_nsys_stats` | Parse nsys report stats |
| `parse_nsys_report` | Alias for parse_nsys_stats |
| `profile_ncu` | Nsight Compute kernel profiling |
| `parse_ncu_report` | Parse ncu report metrics |
| `gpu_info` | Query GPU name, compute cap, PCI bus, driver |
| `compile_kernel` | Compile a .cu file with nvcc |
| `memcheck` | compute-sanitizer memory error detection |
| `racecheck` | compute-sanitizer data race detection |
| `initcheck` | compute-sanitizer uninitialized memory detection |
| `dump_sass` | Dump SASS instructions |
| `dump_ptx` | Dump PTX intermediate representation |
| `benchmark_kernel` | Multi-run timing benchmark |

### Distributed Training (`distributed-training`)

| Tool | What it does |
|------|-------------|
| `list_gpus` | List all GPUs with topology (NVLink/PCIe) |
| `gpu_interconnect` | Check interconnect type and bandwidth |
| `cuda_visible_devices` | Show CUDA_VISIBLE_DEVICES and PyTorch GPU count |
| `nccl_test_all_reduce` | Run NCCL all-reduce bandwidth test |
| `check_nccl_env` | Check NCCL environment variables |
| `torch_distributed_info` | Check PyTorch distributed setup (DDP/FSDP/NCCL) |
| `check_ddp_setup` | Verify DDP can be initialized |
| `check_fsdp_setup` | Check FSDP can wrap a small model |
| `training_jobs` | List running training processes |
| `kill_training_job` | Kill a training process |
| `list_checkpoints` | Find checkpoint files by size |
| `hostfile_info` | Hostname, IP, SSH, distributed tools available |

### Cloud GPU & SSH (`cloud-gpu-ssh`)

| Tool | What it does |
|------|-------------|
| `register_machine` | Register a remote GPU machine for SSH access |
| `list_machines` | List all registered machines |
| `unregister_machine` | Remove a registered machine |
| `remote_command` | Run a command on a remote machine via SSH |
| `remote_gpu_status` | Get nvidia-smi on a remote machine |
| `remote_training_status` | Check training processes on a remote machine |
| `remote_disk_usage` | Check disk space on a remote machine |
| `remote_tail_log` | Tail a log file on a remote machine |
| `upload_file` | Upload a file to a remote machine via SFTP |
| `download_file` | Download a file from a remote machine via SFTP |
| `remote_sftp_list` | List remote directory contents via SFTP |
| `lambda_gpu_pricing` | Get Lambda Labs GPU pricing (needs `LAMBDA_API_KEY`) |
| `runpod_pricing` | Get RunPod GPU pricing (needs `RUNPOD_API_KEY`) |
| `runpod_machines` | List RunPod pods (needs `RUNPOD_API_KEY`) |
| `vast_pricing` | Get public Vast.ai GPU pricing |
| `vast_machines` | List public Vast.ai machine offers |

### TPU & JAX (`tpu-jax`)

| Tool | What it does |
|------|-------------|
| `jax_devices` | List all JAX-visible devices (TPU/GPU/CPU) |
| `jax_tpu_info` | Detailed TPU info (topology, memory, mesh) |
| `jax_distributed_setup` | Check multi-host JAX distributed setup |
| `gcloud_tpu_list` | List TPU nodes in Google Cloud |
| `gcloud_tpu_create` | Create a TPU VM (billable!) |
| `gcloud_tpu_delete` | Delete a TPU VM |
| `gcloud_tpu_ssh` | SSH into a TPU VM |
| `jax_profile` | Profile a JAX script with TensorBoard trace |
| `jax_memory_info` | Get JAX memory usage per device |
| `jax_compilation_check` | Check if a JAX function compiles (XLA HLO) |

### Endosight Pipeline (`endosight-pipeline`)

| Tool | What it does |
|------|-------------|
| `list_clips` | List available endoscopy clips |
| `list_reconstructions` | List completed reconstructions |
| `get_reconstruction_stats` | Point count, mesh info, file sizes |
| `pipeline_status` | Check BFF/Node/Vite/Postgres status |
| `start_pipeline` | Start the pipeline in the background |
| `verify_pipeline` | Run verify.sh |
| `sweep_clinical_clips` | Run clinical clip sweep |
| `run_reconstruction` | Trigger reconstruction via BFF upload |
| `run_crop` | Trigger frame/clip cropping for a batch |
| `run_qa` | Run QA checks for a batch |
| `run_video_export` | Trigger video export for a batch |
| `pipeline_logs` | Fetch recent Docker logs for a service |
| `validate_reconstruction` | Check Demo-shaped artifacts exist for a batch |

### Research Workflow (`research-workflow`)

| Tool | What it does |
|------|-------------|
| `search_arxiv` | Search arXiv by keywords |
| `get_arxiv_paper` | Get paper metadata, optionally download PDF |
| `get_paper` | Alias for get_arxiv_paper |
| `add_to_bibtex` | Add paper to BibTeX file |
| `search_bibtex` | Search BibTeX database |
| `list_experiments` | List experiment directories |
| `create_experiment` | Create new experiment with metadata |
| `log_experiment` | Append to experiment log |
| `create_repro_bundle` | Zip source dir with manifest and env snapshot |
| `search_semantic_scholar` | Search Semantic Scholar API |
| `get_citations` | Get citations for an arXiv paper |

## NVIDIA Skills Installation

The following NVIDIA skills were installed via `npx skills add nvidia/skills`:

```bash
# Distributed training
npx skills add nvidia/skills --skill nemo-automodel-distributed-training --agent cursor --yes
npx skills add nvidia/skills --skill nemo-automodel-launcher-config --agent cursor --yes
npx skills add nvidia/skills --skill mcore-run-on-slurm --agent cursor --yes
npx skills add nvidia/skills --skill nemo-mbridge-multi-node-slurm --agent cursor --yes

# Performance tuning
npx skills add nvidia/skills --skill nemo-mbridge-perf-parallelism-strategies --agent cursor --yes
npx skills add nvidia/skills --skill nemo-mbridge-perf-megatron-fsdp --agent cursor --yes
npx skills add nvidia/skills --skill nemo-mbridge-perf-memory-tuning --agent cursor --yes
npx skills add nvidia/skills --skill nemo-mbridge-perf-cuda-graphs --agent cursor --yes

# Other
npx skills add nvidia/skills --skill dali-dynamic-mode --agent cursor --yes
npx skills add nvidia/skills --skill cudaq-guide --agent cursor --yes
npx skills add nvidia/skills --skill deepstream-dev --agent cursor --yes
npx skills add nvidia/skills --skill deepstream-profile-pipeline --agent cursor --yes
```

Browse all 330+ skills: `npx skills add nvidia/skills --list`

## Community MCP Servers (Optional)

### W&B (Weights & Biases)
```json
{"mcpServers": {"wandb": {"url": "https://mcp.withwandb.com/mcp", "headers": {"Authorization": "Bearer ${WANDB_API_KEY}"}}}}
```
Get API key at [wandb.ai/authorize](https://wandb.ai/authorize). Tools: query runs, analyze traces, create reports, search docs.

### MLflow
```json
{"mcpServers": {"mlflow": {"command": "uv", "args": ["run", "--with", "mlflow[mcp]>=3.5.1", "mlflow", "mcp", "run"], "env": {"MLFLOW_TRACKING_URI": "file:///home/mlruns"}}}}
```
Install: `pip install mlflow[mcp]`. Tools: search traces, analyze runs, log feedback, manage model registry.

### Slurm (for HPC clusters)
- [slurm-mcp](https://github.com/dongwookim-ml/slurm-mcp) — submit jobs, monitor GPUs, tail output
- [secure-cluster-mcp](https://github.com/FlorianSp2000/secure-cluster-mcp) — safe SSH + Slurm with guardrails
- [clausius](https://github.com/tamohannes/clausius) — multi-cluster dashboard with MCP

### Kubeflow Training
- [kubeflow/mcp-server](https://github.com/kubeflow/mcp-server) — submit/monitor training jobs on K8s via natural language

### Cloud GPU Provisioning
- [lambda-cloud-cli](https://registry.npmjs.org/lambda-cloud-cli) — Lambda Labs GPU instances with MCP
- [vastai-mcp](https://github.com/crydevok/vastai-mcp) — Vast.ai GPU instances
- [ml-mcp](https://github.com/PushPullCommitPush/ml-mcp) — Multi-provider (Lambda + RunPod + Together AI)

## Agent Configuration

Servers are registered in these config files:

| Agent | Config file |
|-------|------------|
| Cursor | `~/.cursor/mcp.json` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` |
| Claude Code | `~/.claude/mcp.json` |
| Devin | `~/.config/devin/mcp_config.json` |
| Gemini | `~/.gemini/config/mcp_config.json` |

## Adding More Tools

To add a new tool to any server, edit the `server.py` file and add a function with the `@server.tool()` decorator:

```python
@server.tool()
def my_new_tool(
    arg1: Annotated[str, "Description of arg1"],
    arg2: Annotated[int, "Description of arg2"] = 10,
) -> str:
    """What this tool does (this becomes the tool description for agents)."""
    # Your logic here
    return "result"
```

Then add it to the `TOOLS` dict at the bottom of the file for CLI mode.
