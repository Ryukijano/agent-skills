SKILLS = [
    {
        "name": "neuromorphic-computing",
        "title": "Neuromorphic Computing",
        "description": "Spiking neural networks (SNNs), event-based processing, and brain-inspired low-power accelerators like Intel Loihi and BrainChip.",
        "devin_body": r'''
## When to use

You need ultra-low-power inference, event-based sensing, or brain-inspired temporal computation for edge or robotics workloads.

## Key concepts

- **Spiking Neural Networks (SNNs)**: neurons communicate via discrete spikes over time.
- **Event-based processing**: react to changes rather than frame-based sampling.
- **Neuromorphic hardware**: analog/digital chips (Intel Loihi, BrainChip Akida) that emulate neural dynamics.
- **Surrogate gradients**: train SNNs with backpropagation through time.
- **Neuromorphic sensors**: event cameras (DAVIS, Dynamic Vision Sensor) output spike streams.

## Code pattern

```python
import snntorch as snn
import torch

# Leaky integrate-and-fire neuron
lif = snn.Leaky(beta=0.8)
spk, mem = lif(x, mem)
```

## Tuning notes

- Time constants and spike thresholds strongly affect accuracy and sparsity.
- Use surrogate gradients (e.g., fast sigmoid) for BPTT training.
- Quantize weights and biases for deployment on neuromorphic edge chips.

## Verification

1. Train an SNN classifier on a small spiking dataset (e.g., N-MNIST, DVSGesture).
2. Compare energy and latency to an equivalent ANN on edge hardware.
3. Visualize spike raster and measure mean firing rate.
''',
        "references": [
            "https://redwood.berkeley.edu/wp-content/uploads/2021/08/Davies2018.pdf",
            "https://www.intel.com/content/dam/www/central-libraries/us/en/documents/neuromorphic-computing-loihi-2-brief.pdf",
            "https://www.nature.com/articles/s41467-024-53827-9",
            "https://proceedingsoftheieee.ieee.org/advancing-neuromorphic-computing-with-loihi-a-survey-of-results-and-outlook/",
        ],
    },
    {
        "name": "photonic-computing",
        "title": "Photonic Computing",
        "description": "Silicon photonics, optical processing units, and photonic interconnects for energy-efficient AI and HPC.",
        "devin_body": r'''
## When to use

You want to accelerate matrix-vector multiplications or interconnects using light, reducing energy and increasing bandwidth for AI/HPC.

## Key concepts

- **Silicon photonics**: integrate optical components on CMOS chips.
- **Optical Processing Unit (OPU)**: perform random projections in the analog optical domain.
- **Photonic interconnects**: replace electrical I/O with optical links for high bandwidth density.
- **Coherent and incoherent photonic accelerators**: MZIs, MRRs, and free-space optics.
- **Thermal/crosstalk calibration**: photonic devices are sensitive to temperature and phase drift.

## Code pattern

```python
# Example: LightOn OPU random projection via Python API
from lightonopu.opu import OPU
import numpy as np

opu = OPU()
X = np.random.randn(1000, 784).astype(np.float32)
Y = opu.transform(X)  # random feature map
```

## Tuning notes

- Photonic accelerators excel at large, high-dimensional linear transforms.
- Account for analog noise, drift, and finite precision when building models.
- Hybrid CPU/GPU/OPU pipelines are common; place OPU at the bottleneck layer.

## Verification

1. Run a random projection benchmark on an OPU and compare throughput to CPU/GPU.
2. Train a kernel/Ridge classifier on OPU features.
3. Measure energy per MAC and bit accuracy of optical outputs.
''',
        "references": [
            "https://lightmatter.co/products/envise/",
            "https://arxiv.org/abs/2107.11814",
            "https://lightmatter.co/products/m1000/",
            "https://lightmatter.co/press-release/lightmatter-unveils-passage-m1000-photonic-superchip-worlds-fastest-ai-interconnect/",
        ],
    },
    {
        "name": "quantum-machine-learning",
        "title": "Quantum Machine Learning",
        "description": "Hybrid quantum-classical ML with variational quantum circuits, PennyLane, TensorFlow Quantum, and Qiskit.",
        "devin_body": r'''
## When to use

You are exploring whether parameterized quantum circuits can improve expressivity or efficiency for small, structured ML problems.

## Key concepts

- **Variational Quantum Circuits (VQCs)**: parameterized gates optimized classically.
- **Quantum embeddings**: amplitude/angle encoding of classical data.
- **Hybrid quantum-classical models**: combine a small quantum co-processor with a neural network.
- **PennyLane / TFQ / Qiskit**: frameworks for differentiable quantum circuits.
- **Barren plateaus**: watch for vanishing gradients in deep unstructured circuits.

## Code pattern

```python
import pennylane as qml
import torch

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev, interface="torch")
def qnode(inputs, weights):
    qml.AngleEmbedding(inputs, wires=range(2))
    qml.BasicEntanglerLayers(weights, wires=range(2))
    return qml.expval(qml.PauliZ(0))
```

## Tuning notes

- Use data re-uploading or feature maps carefully to avoid exponential qubit needs.
- Start with small circuits and simulators; real hardware is noisy and expensive.
- Regularize to avoid overfitting on tiny quantum datasets.

## Verification

1. Train a VQC binary classifier on a 2D toy dataset.
2. Compare test accuracy to a classical MLP on the same data.
3. Analyze gradient variance across circuit depth (barren-plateau check).
''',
        "references": [
            "https://pennylane.ai",
            "https://www.tensorflow.org/quantum",
            "https://github.com/tensorflow/quantum",
            "https://github.com/PennyLaneAI/pennylane-qiskit",
        ],
    },
    {
        "name": "high-performance-python",
        "title": "High-Performance Python",
        "description": "Numba, Cython, pybind11, vectorization, and profiling for Python code that rivals C/Fortran speed.",
        "devin_body": r'''
## When to use

Your Python ML/scientific code is too slow and you want to keep (most of) the Python ecosystem while approaching compiled-language speed.

## Key concepts

- **Numba**: JIT compilation of NumPy-aware Python functions via LLVM.
- **Cython**: static compilation with optional type annotations and C/C++ interop.
- **pybind11**: lightweight header-only bindings for C++ extensions.
- **Vectorization and memory layout**: contiguous arrays, row/column-major order.
- **Profiling**: cProfile, line_profiler, py-spy, and profilers to find hotspots.

## Code pattern

```python
from numba import njit, prange
import numpy as np

@njit(parallel=True)
def sum_rows(a):
    m, n = a.shape
    out = np.empty(m)
    for i in prange(m):
        out[i] = a[i, :].sum()
    return out
```

## Tuning notes

- Numba works best with numerical NumPy/loops; avoid object types and unsupported Python features.
- Cython pays off when you need C-level structs, typed memoryviews, or static binding.
- Cache Numba-compiled functions with `cache=True` and profile before optimizing.

## Verification

1. Benchmark a hotspot before and after Numba/Cython/pypbind11.
2. Verify numerical output matches the pure-Python reference implementation.
3. Profile memory and cache behavior; ensure array layout is contiguous.
''',
        "references": [
            "https://numba.pydata.org/",
            "https://cython.org/",
            "https://www.github.com/pybind/pybind11",
            "https://github.com/numba/numba",
        ],
    },
    {
        "name": "dask-ml",
        "title": "Dask-ML",
        "description": "Distributed and out-of-core machine learning with Dask and scikit-learn, XGBoost, and hyperparameter search.",
        "devin_body": r'''
## When to use

You want to scale scikit-learn-style ML workloads across multiple cores or machines without rewriting to a new framework.

## Key concepts

- **Dask collections**: Dask Array, DataFrame, and Bag for partitioned, lazy data.
- **Dask-ML estimators**: distributed preprocessing, clustering, and regression.
- **Joblib backend**: parallelize scikit-learn with Dask clusters.
- **Parallel meta-estimators**: `ParallelPostFit`, `Incremental` for larger-than-memory prediction.
- **XGBoost/Dask integration**: train distributed XGBoost on Dask arrays/DataFrames.

## Code pattern

```python
from dask_ml.cluster import KMeans
from dask_ml.datasets import make_blobs

X, y = make_blobs(n_samples=1_000_000, chunks=100_000)
clf = KMeans(n_clusters=10)
clf.fit(X)
```

## Tuning notes

- Chunk size affects overhead; aim for ~100 MB chunks for in-memory workloads.
- Use Dask's dashboard to diagnose stragglers and data transfer.
- Prefer `Incremental` and partial_fit for streaming/online models.

## Verification

1. Run a Dask-ML estimator on a dataset that does not fit in local RAM.
2. Compare results to the equivalent scikit-learn single-machine run.
3. Inspect the Dask dashboard for task scheduling and memory usage.
''',
        "references": [
            "https://ml.dask.org/",
            "https://ml.dask.org/joblib",
            "https://examples.dask.org/machine-learning.html",
            "https://ml.dask.org/meta-estimators.html",
        ],
    },
    {
        "name": "modin-pandas",
        "title": "Modin Pandas",
        "description": "Drop-in distributed, parallel pandas replacement using Modin with Ray or Dask backends.",
        "devin_body": r'''
## When to use

You have pandas code that is slow or runs out of memory on large DataFrames and want a near-drop-in parallel replacement.

## Key concepts

- **Modin**: parallel DataFrame library exposing the pandas API.
- **Execution engines**: Ray, Dask, HDK, or Python unidist.
- **Lazy vs eager**: operations are distributed and parallelized under the hood.
- **Out-of-core**: process DataFrames larger than memory on a single machine.
- **API compatibility**: most pandas methods work; unsupported ones fall back or warn.

## Code pattern

```python
# import modin.pandas as pd
import modin.pandas as pd

df = pd.read_csv("large_dataset.csv")
df.groupby("category").agg({"value": "mean"}).compute()  # modin exposes .compute()
```

## Tuning notes

- Use the Ray or Dask backend depending on your cluster setup.
- Some pandas operations are not yet fully optimized; check Modin docs for coverage.
- For very small dataframes, native pandas may be faster due to lower overhead.

## Verification

1. Run a representative pandas notebook with `import modin.pandas as pd`.
2. Compare wall-clock time and peak RAM against the original pandas run.
3. Validate that output matches pandas exactly on a sample dataset.
''',
        "references": [
            "https://modin.org/",
            "https://github.com/modin-project/modin/",
            "https://modin.readthedocs.io/en/latest/getting_started/quickstart.html",
            "https://modin.readthedocs.io/en/latest/getting_started/why_modin/pandas.html",
        ],
    },
    {
        "name": "feature-stores",
        "title": "Feature Stores",
        "description": "Feast, Tecton, and Hopsworks for centralized feature definition, versioning, and online/offline serving.",
        "devin_body": r'''
## When to use

You need consistent, low-latency features shared across training and inference, with point-in-time correctness and versioning.

## Key concepts

- **Offline store**: historical feature data for training (data warehouse / lakehouse).
- **Online store**: low-latency key-value store for inference (Redis, DynamoDB, Bigtable).
- **Feature view**: a declarative group of features computed from data sources.
- **Point-in-time joins**: retrieve feature values as of each training example's timestamp.
- **Feast / Tecton / Hopsworks**: open-source and managed feature store platforms.

## Code pattern

```python
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo")

training_df = store.get_historical_features(
    entity_df=entities,
    features=["user_stats:daily_transactions", "user_stats:ltv"]
).to_df()
```

## Tuning notes

- Define clear entities, feature views, and feature services.
- Materialize features to the online store before serving.
- Monitor train/serve skew with freshness and distribution checks.

## Verification

1. Set up a feature repo with an offline and online store.
2. Materialize features and serve a sample online request.
3. Compare training-serving feature values for the same entity and timestamp.
''',
        "references": [
            "https://feast.dev/",
            "https://docs.feast.dev/",
            "https://resources.tecton.ai/hubfs/Choosing-Feature-Solution-Feast-or-Tecton.pdf",
            "https://mlopsplatforms.com/posts/feature-store-comparison-2026/",
        ],
    },
    {
        "name": "data-versioning",
        "title": "Data Versioning",
        "description": "DVC, lakeFS, and Delta Lake for versioning datasets, models, and pipelines alongside code.",
        "devin_body": r'''
## When to use

You need to reproduce ML experiments, track dataset changes, and manage large artifacts beyond what Git can handle.

## Key concepts

- **DVC**: Git-like data version control with storage remotes (S3, GCS, Azure).
- **lakeFS**: Git-like branching/merging over object storage data lakes.
- **Delta Lake**: ACID transactions and time travel for Parquet tables.
- **Data registries**: central repositories of versioned datasets and models.
- **Reproducibility**: tie code, data, and pipeline versions together.

## Code pattern

```bash
# DVC workflow
dvc add data/raw
git add data/raw.dvc .gitignore
dvc push
```

```python
# Delta Lake time travel
from deltalake import DeltaTable

dt = DeltaTable("s3://bucket/training_data")
df = dt.load_as_version(5).to_pandas()
```

## Tuning notes

- Use `.dvc` files for large artifacts and keep metadata in Git.
- LakeFS is great for multi-table data lake versioning; DVC is project/ML focused.
- Delta Lake adds schema enforcement but requires a Spark/Delta Lake engine.

## Verification

1. Version a dataset, train a model, and reproduce the exact run later.
2. Roll back to a previous dataset version and rerun validation.
3. Compare DVC, lakeFS, and Delta Lake for your storage architecture.
''',
        "references": [
            "https://dvc.org/",
            "https://doc.dvc.org/example-scenarios/versioning-data-and-models/tutorial",
            "https://lakefs.io/blog/dvc-vs-git-vs-dolt-vs-lakefs/",
            "https://devidevs.com/blog/data-versioning-ml-dvc-lakefs-delta-lake",
        ],
    },
    {
        "name": "ml-metadata-lineage",
        "title": "ML Metadata and Lineage",
        "description": "ML Metadata (MLMD), MLflow, and Kubeflow lineage for tracking artifacts, executions, and provenance.",
        "devin_body": r'''
## When to use

You need to trace which data, code, and model versions produced a given artifact or prediction in an ML pipeline.

## Key concepts

- **ML Metadata (MLMD)**: store artifacts, executions, and contexts.
- **Lineage graph**: directed graph linking artifacts to executions and downstream artifacts.
- **MLflow Tracking**: log parameters, metrics, artifacts, and models.
- **Kubeflow Pipelines**: capture lineage across pipeline runs.
- **OpenLineage**: open standard for lineage metadata collection.

## Code pattern

```python
import mlflow

mlflow.set_experiment("forecasting")
with mlflow.start_run():
    mlflow.log_param("lr", 0.01)
    mlflow.log_metric("rmse", 3.4)
    mlflow.log_artifact("model.pkl")
    mlflow.sklearn.log_model(model, "model")
```

## Tuning notes

- Log everything deterministic (seeds, code commit, data version) for reproducibility.
- Use artifact stores and model registries for long-lived lineage.
- Link lineage across tools via consistent run IDs and artifact URIs.

## Verification

1. Log a model training run with parameters, metrics, and artifacts.
2. Query the lineage from raw data → features → model → predictions.
3. Demonstrate reproducibility by checking out a run and re-running it.
''',
        "references": [
            "https://github.com/google/ml-metadata/",
            "https://www.kubeflow.org/docs/components/pipelines/concepts/metadata/",
            "https://mlflow.org/docs/latest/ml/tracking/",
            "https://github.com/mlflow/mlflow/",
        ],
    },
    {
        "name": "in-memory-computing",
        "title": "In-Memory Computing",
        "description": "Compute-in-memory, processing-in-memory, and emerging NVM technologies (PCM, RRAM, MRAM) for AI.",
        "devin_body": r'''
## When to use

You are designing hardware or algorithms that reduce data movement by placing computation inside or near memory arrays.

## Key concepts

- **Compute-in-memory (CIM) / processing-in-memory (PIM)**: perform MACs inside memory arrays.
- **Analog CIM**: use Ohm's law and Kirchhoff's laws for vector-matrix multiplication.
- **Emerging NVMs**: RRAM, PCM, MRAM, FeFET as compute/storage elements.
- **Memory wall**: von Neumann bottleneck driving CIM research.
- **Noise and precision**: analog CIM introduces device and readout noise.

## Code pattern

```python
import numpy as np

# Idealized analog CIM: G stores weights, V is input vector, I is output
G = np.array([[1.0, 0.5], [0.2, 0.9]])  # conductance matrix
V = np.array([0.5, 0.3])                # input voltages
I = G @ V                               # Kirchhoff current summation
```

## Tuning notes

- ADC/DAC and readout circuits often dominate energy and area in analog CIM.
- Weight programming and drift compensation are critical for accuracy.
- Start with behavioral models before taping out analog macros.

## Verification

1. Simulate an ideal conductance-based MAC and compare to digital golden reference.
2. Add conductance noise / quantization and measure accuracy drop on a DNN layer.
3. Compare throughput, energy, and area estimates to a digital baseline.
''',
        "references": [
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12164277/",
            "https://www.mdpi.com/1424-8220/25/12/3618",
            "https://link.springer.com/article/10.1007/s11432-023-3789-7",
            "https://par.nsf.gov/biblio/10649488",
        ],
    },
    {
        "name": "analog-computing",
        "title": "Analog Computing",
        "description": "Reconfigurable analog accelerators, in-memory analog computing, and mixed-signal AI hardware.",
        "devin_body": r'''
## When to use

You are building or using analog/mixed-signal accelerators where continuous physical quantities directly implement mathematical operations.

## Key concepts

- **Analog computing**: continuous voltages/currents represent variables.
- **Analog in-memory computing (AIMC)**: resistive arrays compute dot products in the analog domain.
- **Reconfigurable analog engines**: switch capacitor/resistor networks to map different kernels.
- **ADC/DAC precision and noise**: analog results must be digitized; converter resolution matters.
- **HW/SW co-design**: algorithm choices must match analog noise and dynamic range.

## Code pattern

```python
import numpy as np

# Idealized analog MAC with finite ADC precision
G = np.random.randn(64, 64)
x = np.random.randn(64)
y_analog = G @ x
# quantize to e.g. 8-bit ADC
y_digital = np.round(y_analog / np.max(np.abs(y_analog)) * 127).astype(np.int8)
```

## Tuning notes

- Quantize weights and activations to match the analog accelerator's bit precision.
- Retrain with noise injection to improve robustness to analog non-idealities.
- Evaluate end-to-end accuracy with a calibrated behavioral model.

## Verification

1. Build a behavioral analog accelerator model in Python.
2. Run a small DNN layer through the model and compare to a digital reference.
3. Sweep noise, ADC bits, and weight drift to find an accuracy operating point.
''',
        "references": [
            "https://www.nature.com/articles/s41928-025-01537-5",
            "https://research.ibm.com/publications/eagle-a-flexible-heterogeneous-analog-compute-in-memory-architecture-with-risc-v-programmable-multi-core-accelerators",
            "https://doi.org/10.1109/iccd65941.2025.00021",
            "https://doi.org/10.1109/iedm45741.2023.10413724",
        ],
    },
    {
        "name": "wafer-scale-ai",
        "title": "Wafer-Scale AI",
        "description": "Cerebras Wafer Scale Engine, wafer-scale training and inference, and massive on-chip compute fabric.",
        "devin_body": r'''
## When to use

You need to train or serve massive AI models with massive on-chip memory and near-linear scaling by avoiding multi-GPU communication overhead.

## Key concepts

- **Wafer Scale Engine (WSE)**: a chip the size of an entire wafer (e.g., Cerebras WSE-3).
- **Giant on-chip memory and compute fabric**: hundreds of thousands of cores on one die.
- **Weight streaming / appliance mode**: scale out with external MemoryX and SwarmX nodes.
- **CSoft / Cerebras SDK**: PyTorch/XLA interface and C-like kernel language (CSL).
- **Fail-in-place architecture**: redundant cores and routing tolerate manufacturing defects.

## Code pattern

```python
import torch
import cerebras.pytorch as cbtorch

# Run a standard PyTorch model on a CS-3 with Cerebras XLA backend
model = MyModel()
# compile and run through cbtorch; exact API is hardware-dependent
```

## Tuning notes

- Wafer-scale systems excel at large-model training/inference on a single device.
- Use the Cerebras Weight Streaming cluster for multi-system scaling.
- Optimize data loading and compilation time for your model shapes.

## Verification

1. Profile a model on a wafer-scale system and compare throughput to a GPU baseline.
2. Measure scaling efficiency from one to multiple CS nodes.
3. Verify weight streaming and gradient accumulation produce identical convergence.
''',
        "references": [
            "https://www.cerebras.ai/chip",
            "https://www.cerebras.ai/inference",
            "https://www.cerebras.ai/product-software",
            "https://www.cerebras.ai/blog/the-complete-guide-to-scale-out-on-cerebras-wafer-scale-clusters",
        ],
    },
]
