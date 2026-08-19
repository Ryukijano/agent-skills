SKILLS = [
    {
        "name": "kubernetes-gpu-orchestration",
        "title": "Kubernetes and GPU Orchestration",
        "description": "NVIDIA GPU Operator, MIG, MPS, Kueue, Volcano, gang scheduling, and DRA for ML workloads on Kubernetes.",
        "devin_body": '''
## When to use

You are running ML training or inference on Kubernetes and need to schedule, share, or partition GPUs.

## Key concepts

- **NVIDIA GPU Operator**: automates driver, container runtime, device plugin, DCGM, and MIG manager deployment.
- **MIG on Kubernetes**: `mig.strategy=single/mixed`; node labels like `nvidia.com/mig-1g.5gb`.
- **MPS**: multi-process service for sharing a GPU across containers; controlled via DRA driver feature gate.
- **Kueue**: Kubernetes native queueing with quotas, fair sharing, and preemption.
- **Volcano**: alternative scheduler with gang scheduling, hierarchical queues, and job-level co-scheduling.
- **DRA (Dynamic Resource Allocation)**: new device API in K8s; used by Kueue for fine-grained GPU allocation.

## Code pattern

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: gpu-job
spec:
  containers:
  - name: train
    image: nvcr.io/nvidia/pytorch:25.06-py3
    resources:
      limits:
        nvidia.com/gpu: 1
```

For Kueue:

```bash
kubectl label queue default-queue
kubectl apply -f job.yaml
```

## Tuning notes

- MIG and MPS are mutually exclusive in the DRA driver; choose one per node.
- Gang scheduling prevents partial-allocation deadlock for multi-pod jobs.
- Use `nvidia.com/gpu: 1` for whole GPU, `nvidia.com/mig-...` for slices.

## Verification

1. Check `kubectl get nodes` shows `nvidia.com/gpu` allocatable resources.
2. Run a small GPU pod and `nvidia-smi` inside the container.
3. With Kueue, verify the job is admitted and scheduled.
''',
        "references": [
            "https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/26.3/gpu-operator-mig.html",
            "https://kueue.sigs.k8s.io/",
            "https://volcano.sh/",
            "https://dra-driver-nvidia-gpu.sigs.k8s.io/"
        ],
    },
    {
        "name": "ray-ml-distributed",
        "title": "Ray for Distributed ML",
        "description": "Ray Train, Ray Tune, Ray Serve, Ray Data, and Ray clusters for scaling training, tuning, serving, and data processing.",
        "devin_body": '''
## When to use

You want to scale PyTorch/TensorFlow/HF training, hyperparameter search, or serving across a Ray cluster.

## Key concepts

- **Ray Train**: `TorchTrainer`, `ScalingConfig`, distributed data-parallel training.
- **Ray Tune**: distributed HPO with ASHA/Hyperband, integrates with Ray Train.
- **Ray Serve**: model composition, dynamic batching, multi-GPU inference.
- **Ray Data**: scalable data loading and preprocessing with GPU actors.
- **Ray Clusters**: `ray start --head`, `ray submit`, autoscaling.

## Code pattern

```python
import ray
from ray.train.torch import TorchTrainer
from ray.train import ScalingConfig

ray.init()

def train_func(config):
    # training loop
    pass

trainer = TorchTrainer(
    train_loop_per_worker=train_func,
    scaling_config=ScalingConfig(num_workers=4, use_gpu=True)
)
result = trainer.fit()
```

## Tuning notes

- Use `RAY_TRAIN_V2_ENABLED=1` for the new Ray Train V2 API.
- Tune with `ASHAScheduler` for early stopping.
- `ray.init(address="auto")` on a cluster; `ray.init()` for local testing.

## Verification

1. Start a local Ray cluster and run a `TorchTrainer` with 2 workers.
2. Run a small Tune search and confirm multiple trials execute in parallel.
3. Check `ray status` shows expected GPU usage.
''',
        "references": [
            "https://docs.ray.io/en/latest/train/train.html",
            "https://docs.ray.io/en/latest/tune/index.html",
            "https://docs.ray.io/en/latest/serve/index.html",
            "https://docs.ray.io/en/latest/data/data.html"
        ],
    },
    {
        "name": "model-serving-gpu",
        "title": "Model Serving on GPU",
        "description": "Triton Inference Server, TensorRT-LLM, vLLM, TorchServe, FastAPI, and BentoML for production inference.",
        "devin_body": '''
## When to use

You need to deploy a trained model for low-latency, high-throughput inference on GPU.

## Key concepts

- **Triton Inference Server**: multi-backend, batched, multi-GPU. Supports vLLM and TensorRT-LLM backends.
- **TensorRT-LLM**: compile and serve LLMs with inflight batching, paged attention, FP8/FP4.
- **vLLM**: PagedAttention, continuous batching, easy OpenAI-compatible API.
- **TorchServe**: PyTorch-native serving with model archiving and A/B testing.
- **BentoML**: full ML serving platform with packaging and monitoring.

## Code pattern

```bash
# vLLM serve
vllm serve meta-llama/Llama-2-7b --tensor-parallel-size 1

# Triton with TensorRT-LLM backend
python TensorRT-LLM/triton_backend/scripts/launch_triton_server.py \
  --model_repo=TensorRT-LLM/triton_backend/all_models/llmapi/
```

## Tuning notes

- TensorRT-LLM gives 20-40% higher throughput after compile time; vLLM is faster to deploy.
- Use `--gpu-memory-utilization` carefully on UMA systems.
- For mixed model serving, Triton can host multiple backends in one server.

## Verification

1. Send a sample request to the server and measure latency at batch 1 and 16.
2. Verify throughput (tokens/s) matches expected for the GPU.
3. Check `nvidia-smi` for GPU utilization and memory.
''',
        "references": [
            "https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/vllm_backend/README.html",
            "https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrtllm_backend/README.html",
            "https://docs.vllm.ai/",
            "https://pytorch.org/serve/"
        ],
    },
    {
        "name": "cicd-ml-pipelines",
        "title": "CI/CD for Machine Learning",
        "description": "GitHub Actions, GitLab CI, pre-commit, artifact registries, and model promotion gates for ML pipelines.",
        "devin_body": '''
## When to use

You want to automate testing, training, and deployment of ML models with proper gates.

## Key concepts

- **Code CI**: lint, unit tests, type checks, sample inference on every PR.
- **Model CD**: retrain on schedule, validate metrics, promote to staging/prod.
- **Self-hosted runners**: GPU runners for training jobs on GH Actions / GitLab CI.
- **Artifact registries**: Docker Hub, GHCR, GitLab Container Registry for images; DVC or model registry for weights.
- **Pre-commit**: `black`, `ruff`, `mypy`, `pytest`.

## Code pattern

```yaml
# .github/workflows/ml.yml
name: ML CI
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install -r requirements.txt
      - run: pytest tests/
```

## Tuning notes

- Cache dependencies and DVC-tracked data in CI.
- Use parent-child pipelines for multi-stage ML workflows.
- Add a gate: block promotion if validation metric regresses vs baseline.

## Verification

1. Open a PR and confirm CI runs lint, tests, and sample inference.
2. Verify model retraining triggers on schedule and metrics are logged.
3. Confirm rollback to previous model artifact works.
''',
        "references": [
            "https://github.com/mlrepa/cicd-for-modern-ai",
            "https://docs.github.com/en/actions",
            "https://dvc.org/doc/use-cases/versioning-data-and-models",
            "https://pre-commit.com/"
        ],
    },
    {
        "name": "monitoring-observability-ml",
        "title": "Monitoring and Observability for ML",
        "description": "Prometheus, Grafana, Weights & Biases, MLflow, Evidently, and drift detection for production ML.",
        "devin_body": '''
## When to use

You have models in production and need to monitor infrastructure, model performance, and data drift.

## Key concepts

- **Infrastructure**: Prometheus + Grafana for GPU utilization, latency, throughput.
- **Experiment tracking**: W&B, MLflow, Neptune, Aim.
- **Model observability**: Evidently for drift, data quality, performance degradation.
- **Alerting**: Grafana alerts on metrics, Evidently triggers retraining.

## Code pattern

```python
import wandb
wandb.init(project="science-ml", config=config)
wandb.log({"loss": loss, "val_acc": acc})
```

Prometheus scrape:

```yaml
scrape_configs:
  - job_name: 'triton'
    static_configs:
      - targets: ['triton:8002']
```

## Tuning notes

- Combine infra monitoring (Prometheus) with model monitoring (Evidently/W&B).
- Track data distribution drift as early as possible.
- Use champion/challenger pattern for model promotion.

## Verification

1. Set up a Grafana dashboard showing GPU utilization and request latency.
2. Log a training run to W&B or MLflow and compare to previous runs.
3. Run Evidently on a dataset shift and confirm it flags drift.
''',
        "references": [
            "https://prometheus.io/docs/introduction/overview/",
            "https://www.evidentlyai.com/",
            "https://mlflow.org/",
            "https://docs.wandb.ai/"
        ],
    },
    {
        "name": "ml-security-supply-chain",
        "title": "ML Security and Supply Chain",
        "description": "Model signing, AIBOM/ML-BOM, container scanning, malicious pickle detection, and provenance for ML artifacts.",
        "devin_body": '''
## When to use

You need to secure the ML supply chain: models, datasets, containers, and dependencies.

## Key concepts

- **Model signing**: OpenSSF Model Signing (OMS), Sigstore keyless signing.
- **SBOM/AIBOM/ML-BOM**: CycloneDX, SPDX for AI models and dependencies.
- **Container scanning**: Trivy, Grype for CVEs in ML images.
- **Artifact scanning**: ML Guard for malicious pickles, leaked secrets, vulnerable dependencies.
- **Provenance**: in-toto attestations, signed hashes, lineage.

## Code pattern

```bash
# Sign a model with Sigstore/OMS
oms sign --model-dir ./model --identity user@example.com

# Scan container
trivy image my-ml-image:latest

# Generate CycloneDX SBOM
sbom-tool generate -b . -bc . -o sbom.json
```

## Tuning notes

- Treat models and datasets as code artifacts with version, hash, and signature.
- Use `safetensors` instead of `pickle` for model weights when possible.
- Quarantine external models/datasets before promoting to production.

## Verification

1. Sign a model artifact and verify the signature.
2. Run Trivy on a serving container and review CVEs.
3. Generate an AIBOM for a trained model and confirm it captures datasets, hyperparameters, and dependencies.
''',
        "references": [
            "https://github.com/ossf/model-signing-spec",
            "https://cyclonedx.org/specification/",
            "https://trivy.dev/",
            "https://github.com/ml-guard/ml-guard"
        ],
    },
    {
        "name": "data-engineering-science",
        "title": "Data Engineering for Scientific ML",
        "description": "ETL pipelines, feature stores, vector databases, RAG, and embeddings for scientific data.",
        "devin_body": '''
## When to use

You are building data pipelines, feature stores, or retrieval systems for scientific ML.

## Key concepts

- **ETL**: Apache Spark, DuckDB, Polars, RAPIDS cuDF, dask-cuda.
- **Feature stores**: Feast for online/offline features; vector DB support.
- **Vector DBs**: FAISS, Milvus, Qdrant, pgvector, Pinecone.
- **RAG**: chunk, embed, retrieve, generate.
- **Embeddings**: sentence-transformers, ESM, Prithvi, CLIP for science.

## Code pattern

```python
import polars as pl

df = pl.read_parquet("s3://bucket/data/*.parquet")
df = df.with_columns(pl.col("x").log().alias("log_x"))
```

RAG:

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(docs)
```

## Tuning notes

- Use Parquet/Zarr/TensorStore for large scientific arrays.
- For RAG, chunk size should match the embedding model's context window.
- Feature stores decouple training and serving features to avoid skew.

## Verification

1. Ingest 1M scientific records and measure ETL throughput.
2. Build a small FAISS index and run nearest-neighbor queries.
3. Verify RAG retrieval improves LLM answer quality on a scientific Q&A task.
''',
        "references": [
            "https://docs.feast.dev/",
            "https://milvus.io/",
            "https://docs.pola.rs/",
            "https://rapids.ai/"
        ],
    },
    {
        "name": "distributed-storage-hpc",
        "title": "Distributed Storage for HPC and ML",
        "description": "Lustre, BeeGFS, GPFS, WekaFS, Ceph, Zarr, and TensorStore for high-throughput scientific data.",
        "devin_body": '''
## When to use

You need high-throughput, parallel storage for large scientific datasets or model checkpoints.

## Key concepts

- **Lustre**: high-bandwidth parallel POSIX filesystem; MDS + OSS.
- **BeeGFS**: easy admin, distributed metadata, RDMA.
- **GPFS/Storage Scale**: enterprise HPC filesystem.
- **WekaFS**: NVMe-only, high IOPS for metadata-heavy AI.
- **Ceph**: unified object, block, file storage.
- **Zarr/TensorStore**: chunked, cloud-native array formats.

## Code pattern

```python
import zarr
z = zarr.open("s3://bucket/data.zarr", mode="r")
chunk = z[0:1024, 0:1024]
```

For Lustre striping:

```bash
lfs setstripe -c 4 -S 1M /path/to/dir
```

## Tuning notes

- Match file/chunk size to storage stripe size.
- Use object storage for archival; parallel filesystem for hot training data.
- TensorStore gives ACID-like multi-process access to Zarr.

## Verification

1. Run `fio` or `IOR` on the filesystem and compare bandwidth to expected.
2. Benchmark `zarr` reads against `h5py`/`netcdf`.
3. Check Lustre stripe settings with `lfs getstripe`.
''',
        "references": [
            "https://www.beegfs.io/",
            "https://www.weka.io/",
            "https://google.github.io/tensorstore/",
            "https://zarr.dev/"
        ],
    },
    {
        "name": "gpu-cluster-management",
        "title": "GPU Cluster Management and Cloud Bursting",
        "description": "SLURM, PBS, LSF, cloud bursting, hybrid clusters, and AWS ParallelCluster for GPU HPC.",
        "devin_body": '''
## When to use

You are managing an on-prem or hybrid GPU cluster for training/inference.

## Key concepts

- **SLURM**: `sbatch`, `srun`, job arrays, partitions, fairshare.
- **PBS/LSF**: alternative schedulers with enterprise features.
- **Cloud bursting**: on-prem SLURM + AWS/Azure/GCP spot instances.
- **ParallelCluster**: AWS open-source HPC cluster management.
- **MIG/MPS in HPC**: partition or share GPUs across users.

## Code pattern

```bash
# Submit to SLURM
sbatch --gpus=8 --nodes=2 --ntasks-per-node=8 train.sh

# Cloud bursting config in slurm.conf
ResumeProgram=/usr/local/bin/slurm_resume
SuspendProgram=/usr/local/bin/slurm_suspend
```

## Tuning notes

- Use job arrays for hyperparameter sweeps.
- Cloud bursting needs low-latency network (Direct Connect/ExpressRoute).
- Pre-bake AMIs to meet boot-time requirements.

## Verification

1. Submit a 2-node 8-GPU job and check `squeue`/`sinfo`.
2. Verify NCCL all-reduce across on-prem and cloud nodes.
3. Test cloud burst with a small job and confirm auto-suspend after idle time.
''',
        "references": [
            "https://slurm.schedmd.com/",
            "https://aws.amazon.com/hpc/parallelcluster/",
            "https://learn.microsoft.com/en-us/azure/cyclecloud/",
            "https://www.ibm.com/products/lsf"
        ],
    },
    {
        "name": "fault-tolerance-checkpointing",
        "title": "Fault Tolerance and Checkpointing at Scale",
        "description": "PyTorch DCP, DeepSpeed elastic training, asynchronous checkpointing, and multi-tier checkpoint storage.",
        "devin_body": '''
## When to use

You are running long or large-scale distributed training and need to recover from failures.

## Key concepts

- **PyTorch DCP**: Distributed Checkpoint, `torch.distributed.checkpoint`, async checkpointing.
- **Elastic training**: `torchrun` with `--rdzv_id`, `--max_restarts`.
- **DeepSpeed**: DSElasticAgent, universal checkpoints, ZeRO optimizer state.
- **Checkpoint content**: model, optimizer, scheduler, RNG, step.
- **Storage tiers**: local NVMe/PMEM → `$SCRATCH` → permanent object storage.

## Code pattern

```python
import torch.distributed.checkpoint as dcp

dcp.save(state_dict, checkpoint_id=f"checkpoint/{step}")
```

DeepSpeed:

```bash
deepspeed --num_gpus 8 train.py --deepspeed ds_config.json
```

## Tuning notes

- Checkpoint frequency balances lost work vs overhead.
- Use async checkpointing to avoid blocking training.
- Store RNG state for exact reproducibility.

## Verification

1. Kill a training job mid-run and resume; confirm loss matches no-interruption curve.
2. Measure checkpoint write bandwidth to `$SCRATCH` vs object storage.
3. Run an elastic training job and simulate a worker failure.
''',
        "references": [
            "https://pytorch.org/docs/stable/distributed.checkpoint.html",
            "https://www.deepspeed.ai/tutorials/elastic-training/",
            "https://pytorch.org/docs/stable/elastic/run.html",
            "https://docs.mila.quebec/examples/good_practices/checkpointing/"
        ],
    },
    {
        "name": "containers-reproducibility",
        "title": "Containers and Reproducibility for HPC",
        "description": "Docker, Apptainer/Singularity, Podman, conda-lock, Nix, and reproducible scientific environments.",
        "devin_body": '''
## When to use

You want to ensure your scientific ML environment is reproducible across laptop, cluster, and cloud.

## Key concepts

- **Docker**: standard containers, root required for build.
- **Apptainer (Singularity)**: user-space, HPC-friendly, can run Docker images.
- **Podman**: daemonless, rootless alternative.
- **Conda-lock**: deterministic cross-platform lockfiles.
- **Nix**: purely functional, bit-for-bit reproducible builds.

## Code pattern

```bash
# Build Apptainer from Docker
apptainer build my.sif docker://my-image:latest

# Conda lock
conda-lock -f environment.yml -p linux-64 -p osx-64

# Run
apptainer run --nv my.sif python train.py
```

## Tuning notes

- Use multi-stage builds to reduce image size and attack surface.
- Bind host filesystems (`--bind /scratch`) in Apptainer.
- Pin CUDA/cuDNN versions in environment.

## Verification

1. Build a container and run the same script on two different hosts.
2. Verify `conda-lock install -n env conda-lock.yml` reproduces the exact packages.
3. Confirm the container can use the GPU with `nvidia-smi`.
''',
        "references": [
            "https://apptainer.org/",
            "https://conda.github.io/conda-lock/",
            "https://nixos.org/",
            "https://docs.podman.io/"
        ],
    },
    {
        "name": "networking-distributed-training",
        "title": "Networking for Distributed Training",
        "description": "InfiniBand, RoCE, NCCL tuning, AWS EFA, and diagnosing multi-node network issues.",
        "devin_body": '''
## When to use

You are running multi-node distributed training and need to optimize the interconnect.

## Key concepts

- **InfiniBand**: lowest latency, highest bandwidth, RDMA; needs Subnet Manager.
- **RoCEv2**: RDMA over Ethernet; needs PFC/ECN for lossless.
- **NCCL tuning**: `NCCL_IB_HCA`, `NCCL_SOCKET_IFNAME`, `NCCL_BUFFSIZE`.
- **AWS EFA**: `aws-ofi-nccl` plugin, `FI_EFA_USE_DEVICE_RDMA=1`.
- **Diagnostics**: `ibstat`, `ibstatus`, `ethtool`, `nccl-tests`.

## Code pattern

```bash
# NCCL with IB
export NCCL_IB_HCA=mlx5_0,mlx5_1
export NCCL_IB_GID_INDEX=3
export NCCL_SOCKET_IFNAME=eth0
mpirun -np 8 python train.py
```

## Tuning notes

- Use `NCCL_DEBUG=INFO` to verify transport.
- For AWS EFA, use the `aws-ofi-nccl` plugin.
- MTU 9000 for RoCE; check with `ping -M do -s 8972`.

## Verification

1. Run `nccl-tests/all_reduce_perf` and confirm bandwidth.
2. `NCCL_DEBUG=INFO` shows `IB` or `NET/IB` being used.
3. `ibstat` or `rdma link` shows link up.
''',
        "references": [
            "https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/networking_troubleshooting.html",
            "https://github.com/aws/aws-ofi-nccl",
            "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start-nccl.html",
            "https://github.com/NVIDIA/nccl-tests"
        ],
    },
]
