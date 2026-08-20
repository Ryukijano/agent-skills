SKILLS = [
    {
        "name": "generative-design",
        "title": "AI-Driven Generative Design",
        "description": "Deep generative models (VAEs, GANs, diffusion) for engineering design synthesis, constraint-aware generation, Pareto-front exploration, and design automation.",
        "devin_body": r'''
## When to use

You want to automatically explore, synthesize, or optimize mechanical/product designs subject to performance, manufacturing, and aesthetic constraints.

## Key concepts

- **Generative design**: algorithms that generate candidate designs from requirements and constraints.
- **Conditional generative models**: VAEs, GANs, diffusion models conditioned on design specs.
- **Pareto-front exploration**: sampling the trade-off between competing objectives (weight, stiffness, cost).
- **Constraint handling**: geometry, physics, and manufacturability constraints embedded in generation or filtering.
- **Design representations**: voxels, B-reps, parametric CAD, point clouds, and latent fields.

## Code pattern

```python
import torch
import torch.nn as nn

# Conditional VAE for a simple design latent space
class CVAE(nn.Module):
    def __init__(self, input_dim, cond_dim, latent_dim):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(input_dim + cond_dim, 256), nn.ReLU())
        self.fc_mu = nn.Linear(256, latent_dim)
        self.fc_logvar = nn.Linear(256, latent_dim)
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim + cond_dim, 256), nn.ReLU(),
            nn.Linear(256, input_dim)
        )

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x, c):
        h = self.encoder(torch.cat([x, c], dim=-1))
        z = self.reparameterize(self.fc_mu(h), self.fc_logvar(h))
        return self.decoder(torch.cat([z, c], dim=-1))

# Generate new design candidates conditioned on stiffness target
cvae = CVAE(input_dim=128, cond_dim=8, latent_dim=16)
condition = torch.randn(10, 8)          # e.g. target stiffness, volume fraction
latent = torch.randn(10, 16)
designs = cvae.decoder(torch.cat([latent, condition], dim=-1))
```

## Tuning notes

- Condition vectors should encode meaningful physical or semantic design requirements.
- Use simulation-in-the-loop oracles to filter physically invalid generations.
- Balance diversity and quality with temperature, truncation, or latent-space interpolation.
- Validate generated designs with FEA/CFD or a learned surrogate before fabrication.

## Verification

1. Train a conditional generative model on a small design dataset and sample 100 candidates.
2. Evaluate constraint satisfaction and performance of generated designs against a simulator.
3. Produce a Pareto-front plot of two competing objectives (e.g., weight vs. stiffness).
''',
        "references": [
            "https://arxiv.org/abs/2110.10863",
            "https://doi.org/10.1115/1.4053859",
            "https://doi.org/10.48550/arxiv.2502.02628",
            "https://arxiv.org/abs/2302.02913",
            "https://www.autodesk.com/solutions/generative-design"
        ],
    },
    {
        "name": "ai-for-cad",
        "title": "AI for Computer-Aided Design (CAD)",
        "description": "Deep generative models for parametric CAD sketches, B-rep synthesis, sketch-and-extrude sequences, and vision-language conditional CAD generation.",
        "devin_body": r'''
## When to use

You need to generate, complete, edit, or retrieve 3D parametric CAD models from sketches, images, text, or partial command sequences.

## Key concepts

- **Parametric CAD sequences**: sketch-and-extrude, boolean, fillet, chamfer operations.
- **B-rep and CSG representations**: boundary representation vs. constructive solid geometry.
- **CAD generative models**: Transformers, VQ-VAEs, and autoregressive models over CAD tokens.
- **Conditional CAD generation**: completion from partial inputs, image-to-CAD, text-to-CAD.
- **Design constraints**: symmetry, parallelism, perpendicularity, and manufacturability.

## Code pattern

```python
import torch
import torch.nn as nn

# Simplified autoregressive CAD command sequence model
class CADSequenceModel(nn.Module):
    def __init__(self, vocab_size, d_model=128, nhead=4, num_layers=4):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, d_model)
        self.pos = nn.Parameter(torch.randn(1, 512, d_model))
        decoder_layer = nn.TransformerDecoderLayer(d_model=d_model, nhead=nhead, batch_first=True)
        self.decoder = nn.TransformerDecoder(decoder_layer, num_layers=num_layers)
        self.head = nn.Linear(d_model, vocab_size)

    def forward(self, seq, condition):
        x = self.embed(seq) + self.pos[:, :seq.size(1), :]
        x = self.decoder(x, condition.unsqueeze(1))
        return self.head(x)

vocab_size = 128  # operation + parameter tokens
model = CADSequenceModel(vocab_size)
commands = torch.randint(0, vocab_size, (4, 32))
logits = model(commands, condition=torch.randn(4, 128))
```

## Tuning notes

- Tokenize CAD operations and parameters separately or jointly depending on the model.
- Use a robust CAD kernel (e.g., Open CASCADE, FreeCAD) to validate generated sequences.
- Data augmentation by random command orderings and parameter perturbations can help.
- Evaluate with geometry-based and sequence-based metrics.

## Verification

1. Train a model to auto-complete partial CAD command sequences.
2. Generate 50 CAD models and check valid B-rep conversion rate.
3. Compare generated designs to ground-truth on Chamfer distance and command accuracy.
''',
        "references": [
            "https://openaccess.thecvf.com/content/ICCV2021/papers/Wu_DeepCAD_A_Deep_Generative_Network_for_Computer-Aided_Design_Models_ICCV_2021_paper.pdf",
            "https://proceedings.mlr.press/v202/xu23f.html",
            "https://arxiv.org/abs/2409.17457",
            "https://proceedings.mlr.press/v162/xu22k.html",
            "https://ojs.aaai.org/index.php/AAAI/article/view/32531"
        ],
    },
    {
        "name": "topology-optimization",
        "title": "Machine Learning for Topology Optimization",
        "description": "SIMP, neural reparameterization, generative topology optimization, physics-informed neural networks, and learned resolution-free solvers for structural design.",
        "devin_body": r'''
## When to use

You need to distribute material inside a design domain to minimize compliance (or another objective) under load, boundary, and volume constraints.

## Key concepts

- **SIMP**: Solid Isotropic Material with Penalization for density-based topology optimization.
- **Neural reparameterization**: using an NN (e.g., CNN, implicit field) to represent density or signed distance.
- **Solver-in-the-loop**: training a generative model with an FE/physics oracle.
- **Physics-informed neural networks (PINNs)**: embedding PDE constraints directly in the loss.
- **Resolution-free models**: predict topologies at arbitrary grid sizes and aspect ratios.

## Code pattern

```python
import torch

# Learned topology generator conditioned on boundary conditions
class TopologyNet(torch.nn.Module):
    def __init__(self, cond_dim, grid_size):
        super().__init__()
        self.mlp = torch.nn.Sequential(
            torch.nn.Linear(cond_dim, 256), torch.nn.ReLU(),
            torch.nn.Linear(256, grid_size * grid_size), torch.nn.Sigmoid()
        )

    def forward(self, cond):
        return self.mlp(cond).view(-1, 1, grid_size, grid_size)

cond = torch.tensor([[load_x, load_y, fix_x, fix_y, volfrac]])
model = TopologyNet(cond_dim=5, grid_size=64)
rho = model(cond)  # density field (0 = void, 1 = solid)
```

## Tuning notes

- Penalization power $p$ in SIMP typically starts around 3 and is gradually increased.
- Filter densities to avoid checkerboarding and ensure mesh independence.
- For learned methods, ground-truth data from conventional TO is often required.
- Validate compliance and volume fraction error against FE analysis.

## Verification

1. Run SIMP on a cantilever beam and visualize the optimized density field.
2. Train a neural surrogate and compare its compliance prediction to FEA.
3. Evaluate a generative topology model on out-of-distribution loads and aspect ratios.
''',
        "references": [
            "https://arxiv.org/abs/2210.10782",
            "https://arxiv.org/abs/2407.13954",
            "https://arxiv.org/abs/2510.23667",
            "https://arxiv.org/abs/2502.13174",
            "https://arxiv.org/abs/2209.05098"
        ],
    },
    {
        "name": "industrial-digital-twins",
        "title": "Industrial Digital Twins",
        "description": "Real-time virtual replicas of physical systems for monitoring, predictive maintenance, process optimization, and hybrid physics-ML modeling.",
        "devin_body": r'''
## When to use

You want to mirror, simulate, predict, and optimize a physical asset or process using live sensor data and computational models.

## Key concepts

- **Digital twin (DT)**: dynamic virtual representation synchronized with a physical counterpart.
- **Physics-informed and data-driven models**: combine first-principles and ML surrogates.
- **Predictive maintenance**: forecast failures from vibration, temperature, pressure, etc.
- **Real-time synchronization**: IoT/edge ingestion, time-series databases, and state estimation.
- **What-if simulation**: test control actions in the twin before applying them physically.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import IsolationForest

# Train an anomaly detector for predictive maintenance
sensors = pd.read_parquet('industrial_sensor_stream.parquet')
features = sensors[['vibration', 'temperature', 'pressure', 'current']]
model = IsolationForest(contamination=0.02, random_state=42)
model.fit(features)
sensors['anomaly_score'] = model.decision_function(features)

# Flag assets with anomalous readings
alerts = sensors[sensors['anomaly_score'] < -0.4]
print(alerts[['asset_id', 'anomaly_score']].head())
```

## Tuning notes

- Keep the digital model synchronized with real-time telemetry and calibration data.
- Use time-aware validation (rolling origin) when training on sequential data.
- Balance model fidelity with computational cost, especially for control loops.
- Integrate domain knowledge to avoid spurious anomaly alerts.

## Verification

1. Build a digital twin of a simple pump/heat-exchanger and compare predicted vs. measured state.
2. Simulate a fault condition and verify the twin detects it before it reaches a threshold.
3. Use the twin to evaluate two control policies and measure simulated improvement.
''',
        "references": [
            "https://arxiv.org/abs/2108.04465",
            "https://arxiv.org/abs/2507.12468",
            "https://arxiv.org/abs/2505.02076",
            "https://arxiv.org/abs/2405.11895",
            "https://arxiv.org/abs/2501.18016"
        ],
    },
    {
        "name": "edge-ai",
        "title": "Edge AI and On-Device Machine Learning",
        "description": "Quantization, pruning, knowledge distillation, neural architecture search, and deployment of ML models on mobile, embedded, and edge accelerators.",
        "devin_body": r'''
## When to use

You need to run ML inference (or training) on constrained devices where latency, privacy, or connectivity limit cloud offloading.

## Key concepts

- **Model compression**: quantization, pruning, knowledge distillation, low-rank factorization.
- **Edge tiers**: mobile, embedded SoC, edge gateway, near-edge server.
- **Hardware accelerators**: NPU, GPU, DSP, TPU, and custom inference chips.
- **Deployment runtimes**: TensorRT, ONNX Runtime, OpenVINO, TensorFlow Lite, Core ML.
- **Accuracy-latency trade-off**: choose quantization bits and model size to meet SLOs.

## Code pattern

```python
import torch
import torch.quantization

# Dynamic post-training quantization of a PyTorch model
model = torch.load('model.pt', map_location='cpu')
model.eval()
quantized_model = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)

# Export to ONNX for an edge runtime
x = torch.randn(1, 3, 224, 224)
torch.onnx.export(quantized_model, x, 'model_quantized.onnx', opset_version=13)
```

## Tuning notes

- Quantize-aware training (QAT) usually preserves accuracy better than post-training quantization.
- Profile latency on the target device, not just the development workstation.
- Beware of operator support differences across runtimes (e.g., ONNX opset).
- Use batching, parallel execution, and memory planning to maximize throughput.

## Verification

1. Quantize a model and compare top-1 accuracy on a validation set before and after.
2. Benchmark end-to-end latency on the target edge device.
3. Run an operator coverage check for the chosen runtime.
''',
        "references": [
            "https://arxiv.org/abs/2403.17154",
            "https://arxiv.org/abs/2411.00907",
            "https://arxiv.org/abs/1806.07846",
            "https://arxiv.org/abs/2605.26119",
            "https://arxiv.org/abs/2604.14661"
        ],
    },
    {
        "name": "real-time-ml",
        "title": "Real-Time Machine Learning and Low-Latency Inference",
        "description": "Streaming inference, online learning, low-latency GPU serving, event-time semantics, and service-level objectives for real-time ML systems.",
        "devin_body": r'''
## When to use

You must serve predictions or update models on continuously arriving data with strict latency and freshness requirements.

## Key concepts

- **Stream processing**: Kafka, Flink, ksqlDB, and cloud-managed streaming services.
- **Online learning**: incremental model updates from data streams.
- **Exactly-once / at-least-once**: delivery guarantees and idempotent consumers.
- **Event time vs. processing time**: handling out-of-order and late-arriving events.
- **SLOs and tail latency**: p50, p99 latency, throughput, and freshness windows.

## Code pattern

```python
from kafka import KafkaConsumer
import onnxruntime as ort
import json

consumer = KafkaConsumer(
    'events',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

session = ort.InferenceSession('model.onnx', providers=['CUDAExecutionProvider'])
input_name = session.get_inputs()[0].name

for msg in consumer:
    features = preprocess(msg.value)
    pred = session.run(None, {input_name: features})[0]
    emit(pred)
```

## Tuning notes

- Precompute and cache features to avoid repeated transformations at inference time.
- Use hardware-specific runtimes (TensorRT, ONNX Runtime) and batching for throughput.
- Set autoscaling based on queue depth and p99 latency, not just CPU.
- Monitor data drift continuously; stale models hurt real-time accuracy.

## Verification

1. Build a streaming inference pipeline and measure p50/p99 latency over 1M events.
2. Compare batch and online learning performance on a concept-drift benchmark.
3. Validate exactly-once semantics by replaying a small event log and checking outputs.
''',
        "references": [
            "https://arxiv.org/abs/2410.15533",
            "https://arxiv.org/abs/2211.10280",
            "https://proceedings.neurips.cc/paper_files/paper/2023/file/7526508f11bbe0a123af62b9dab1fbe1-Paper-Conference.pdf",
            "https://developer.nvidia.com/blog/achieving-single-digit-microsecond-latency-inference-for-capital-markets/",
            "https://www.usenix.org/system/files/atc25-yu.pdf"
        ],
    },
    {
        "name": "vector-databases",
        "title": "Vector Databases for Machine Learning",
        "description": "Approximate nearest neighbor search, dense-embedding storage, metadata filtering, hybrid search, and vector indexing for RAG and recommendation.",
        "devin_body": r'''
## When to use

You need to store, search, and retrieve high-dimensional embeddings at scale, often with metadata constraints and low latency.

## Key concepts

- **Vector embeddings**: dense representations from encoders, LLMs, or multimodal models.
- **Approximate nearest neighbor (ANN)**: HNSW, IVF, PQ, LSH for fast search.
- **Metadata filtering**: combine vector similarity with attribute constraints.
- **Hybrid search**: combine dense vector and sparse/keyword retrieval.
- **Operational features**: replication, sharding, persistence, and multi-tenancy.

## Code pattern

```python
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

client = QdrantClient(":memory:")
client.create_collection(
    collection_name="docs",
    vectors_config=VectorParams(size=128, distance=Distance.COSINE),
)

client.upsert(
    collection_name="docs",
    points=[
        PointStruct(id=1, vector=[0.1] * 128, payload={"doc_id": "A1"}),
        PointStruct(id=2, vector=[0.9] * 128, payload={"doc_id": "B2"}),
    ],
)

results = client.search(
    collection_name="docs",
    query_vector=[0.1] * 128,
    limit=5,
    query_filter={"must": [{"key": "doc_id", "match": {"value": "A1"}}]}
)
```

## Tuning notes

- Choose the distance metric and indexing algorithm that match your embedding model.
- Tune HNSW `ef_construct`, `ef_search`, and `M` for recall vs. latency trade-offs.
- Pre-filtering reduces recall if the vector index is not built on the filtered subset.
- Monitor index build time and memory as dimensionality and cardinality grow.

## Verification

1. Index 10k vectors and measure Recall@10 against exact brute-force search.
2. Run hybrid queries combining vector and metadata filters; verify result relevance.
3. Benchmark latency and throughput under a representative query load.
''',
        "references": [
            "https://arxiv.org/abs/2608.12812",
            "https://arxiv.org/abs/2310.11703",
            "https://arxiv.org/abs/2602.11443",
            "https://www.pinecone.io/research/ICML_2025.pdf",
            "https://arxiv.org/abs/2502.16931"
        ],
    },
    {
        "name": "graph-databases",
        "title": "Graph Databases and Knowledge Graphs for ML",
        "description": "Property graph models, Cypher/Gremlin querying, graph embeddings, GNNs on graph DBs, and knowledge graph completion for connected data.",
        "devin_body": r'''
## When to use

Your data is naturally connected (knowledge, supply chains, social/transactional networks) and you need traversal, reasoning, or graph ML.

## Key concepts

- **Property graph model**: nodes and edges with labels and key-value properties.
- **Cypher / Gremlin**: declarative and traversal graph query languages.
- **Knowledge graphs (KGs)**: semantic triples and ontologies for reasoning.
- **Graph databases**: Neo4j, TigerGraph, Amazon Neptune, ArangoDB, JanusGraph.
- **GNNs on graph DBs**: train graph neural networks by sampling from a graph DB query engine.

## Code pattern

```python
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

with driver.session() as session:
    session.run("""
        CREATE (a:Asset {id: $id})
        CREATE (s:Sensor {name: 'temp'})
        CREATE (a)-[:HAS_SENSOR]->(s)
    """, id="pump-01")

    result = session.run("""
        MATCH (a:Asset {id: 'pump-01'})-[:HAS_SENSOR]->(s:Sensor)
        RETURN s.name AS sensor
    """)
    for record in result:
        print(record["sensor"])
```

## Tuning notes

- Design the graph schema around query patterns, not just the source schema.
- Use indexes and constraints on high-cardinality properties.
- For GNN training, use graph DB sampling to avoid materializing the entire graph in memory.
- Choose between property graphs and RDF/KGs based on reasoning and inference needs.

## Verification

1. Model a small domain as a property graph and run multi-hop Cypher queries.
2. Train a GNN by sampling from a graph DB and evaluate node classification accuracy.
3. Perform knowledge graph completion and check hits@10 on a held-out test set.
''',
        "references": [
            "https://arxiv.org/abs/2209.09732",
            "https://arxiv.org/abs/2411.11375",
            "https://arxiv.org/abs/2511.11399",
            "https://arxiv.org/abs/2504.05478",
            "https://arxiv.org/abs/2607.09666"
        ],
    },
    {
        "name": "data-stream-processing",
        "title": "Data Stream Processing for Machine Learning",
        "description": "Apache Kafka and Flink pipelines, event-time semantics, exactly-once delivery, online feature engineering, and real-time model updates.",
        "devin_body": r'''
## When to use

You need to ingest, transform, and act on high-velocity event data rather than processing everything in static batches.

## Key concepts

- **Data streams**: unbounded, time-ordered sequences of events.
- **Stream processing engines**: Apache Flink, Kafka Streams, Spark Structured Streaming, ksqlDB.
- **Event time vs. processing time**: windows and watermarks for out-of-order data.
- **Delivery guarantees**: at-most-once, at-least-once, exactly-once.
- **Online feature engineering**: real-time aggregations, joins, and point-in-time lookups.

## Code pattern

```python
from kafka import KafkaProducer, KafkaConsumer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Produce events
for record in event_source:
    producer.send('user-events', record)

# Consume and score events in real time
consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for msg in consumer:
    features = extract_online_features(msg.value)
    score = online_model.predict(features)
    if score > threshold:
        trigger_action(msg.value)
```

## Tuning notes

- Use keyed partitioning to keep related events on the same stream partition.
- Tune checkpointing, watermarks, and state backend for Flink jobs.
- Avoid training-inference skew by using the same feature transformation logic in both paths.
- Back-pressure and autoscaling are critical during traffic spikes.

## Verification

1. Deploy a Flink or Kafka Streams job and verify exactly-once output under failures.
2. Compare event-time windows to processing-time windows on out-of-order data.
3. Build a real-time feature pipeline and validate features against batch equivalents.
''',
        "references": [
            "https://arxiv.org/abs/2410.15533",
            "https://arxiv.org/abs/1802.05872",
            "https://arxiv.org/abs/2211.10280",
            "https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/kafka/",
            "https://www.kai-waehner.de/blog/2024/10/01/real-time-model-inference-with-apache-kafka-and-flink-for-predictive-ai-and-genai/"
        ],
    },
    {
        "name": "cost-optimization-cloud",
        "title": "Cloud Cost Optimization for MLOps",
        "description": "FinOps practices, spot/preemptible instances, right-sizing, reserved capacity, autoscaling, and cost-aware scheduling for ML workloads.",
        "devin_body": r'''
## When to use

You need to control cloud spend for data, training, or inference workloads without sacrificing reliability or performance.

## Key concepts

- **FinOps**: collaborative cloud financial management (inform, optimize, operate).
- **Spot/preemptible instances**: unused capacity at deep discounts with interruption risk.
- **Reserved capacity / savings plans**: commit to usage for lower rates.
- **Right-sizing and autoscaling**: match resources to actual demand.
- **Cost allocation and tagging**: attribute spend to teams, projects, and experiments.

## Code pattern

```python
import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')
prices = ec2.describe_spot_price_history(
    InstanceTypes=['g5.xlarge'],
    ProductDescriptions=['Linux/UNIX'],
    StartTime=datetime.utcnow() - timedelta(hours=1)
)

if prices['SpotPriceHistory']:
    avg = sum(float(p['SpotPrice']) for p in prices['SpotPriceHistory']) / len(prices['SpotPriceHistory'])
    print(f"Average g5.xlarge spot price (1h): ${avg:.4f}")
else:
    print("No spot price history available")
```

## Tuning notes

- Use spot for interruptible training and batch jobs; use on-demand/reserved for serving.
- Set autoscaling min/max and scale-down delays to avoid idle nodes.
- Tier storage and archive old artifacts; storage costs compound quickly.
- Track cost per prediction and per experiment, not just total cloud bill.

## Verification

1. Implement a spot-instance training job with checkpointing and measure savings.
2. Compare cost and wall-clock time of spot vs. on-demand for the same workload.
3. Create a cost dashboard with tags and identify the top-3 spend drivers.
''',
        "references": [
            "https://arxiv.org/abs/2307.12479",
            "https://aws.amazon.com/blogs/compute/introducing-price-capacity-optimized-allocation-strategy-for-ec2-spot-instances/",
            "https://www.finops.org/wg/scaling-kubernetes-for-ai-ml-workloads-with-finops/",
            "https://learn.microsoft.com/en-us/cloud-computing/finops/",
            "https://azure.microsoft.com/en-us/blog/cloud-cost-optimization-how-to-maximize-roi-from-ai-manage-costs-and-unlock-real-business-value/"
        ],
    },
    {
        "name": "ml-infrastructure-as-code",
        "title": "ML Infrastructure as Code (MLOps IaC)",
        "description": "Terraform, Pulumi, and GitOps for reproducible ML platforms, modular MLOps stacks, and CI/CD-managed infrastructure.",
        "devin_body": r'''
## When to use

You want to provision, version, and reproduce ML environments, pipelines, and serving infrastructure through code rather than manual setup.

## Key concepts

- **Infrastructure as Code (IaC)**: Terraform, Pulumi, AWS CDK, Azure Bicep.
- **GitOps**: infrastructure changes via Git pull requests and automated reconciliation.
- **MLOps platforms**: training, registry, serving, feature store, experiment tracking.
- **Modular stacks**: reusable components for data, compute, model registry, and monitoring.
- **State management and secrets**: remote state, locking, and secret injection.

## Code pattern

```hcl
# main.tf - Terraform snippet for MLOps base infrastructure
terraform {
  required_providers { aws = { source = "hashicorp/aws" } }
}

resource "aws_s3_bucket" "ml_artifacts" {
  bucket = "my-ml-artifacts-bucket"
}

resource "aws_sagemaker_notebook_instance" "nb" {
  name          = "mlops-notebook"
  role_arn      = aws_iam_role.sagemaker.arn
  instance_type = "ml.t3.medium"
  lifecycle_config_name = aws_sagemaker_notebook_lifecycle_configuration.setup.name
}
```

## Tuning notes

- Keep modules small, composable, and environment-agnostic.
- Use remote state with locking (e.g., S3 + DynamoDB) for team workflows.
- Parameterize instance types, regions, and cost settings per environment.
- Apply least-privilege IAM and network policies from the start.

## Verification

1. Define and deploy a minimal IaC stack for an S3 bucket and a compute instance.
2. Modify the stack via a PR and verify automated plan/apply in a staging environment.
3. Tear down and recreate the stack, confirming reproducibility and identical outputs.
''',
        "references": [
            "https://aws.amazon.com/blogs/machine-learning/implement-a-secure-mlops-platform-based-on-terraform-and-github/",
            "https://github.com/aws-samples/mlops-multi-account-terraform",
            "https://github.com/zenml-io/mlstacks",
            "https://github.com/aws-samples/amazon-eks-machine-learning-with-terraform-and-kubeflow",
            "https://github.com/teamdatatonic/vertex-pipelines-end-to-end-samples"
        ],
    },
    {
        "name": "agent-monitoring-guardrails",
        "title": "Agent Monitoring and Guardrails",
        "description": "Runtime monitoring, safety policy enforcement, tool-call validation, probabilistic risk prediction, and guardrail frameworks for LLM agents.",
        "devin_body": r'''
## When to use

You are building or deploying autonomous LLM agents that use tools and need to stay safe, compliant, and aligned with policies.

## Key concepts

- **Guardrails**: input/output filtering, topic control, and policy enforcement.
- **Runtime monitoring**: trajectory logging, action validation, and anomaly detection.
- **Tool-call validation**: inspect, approve, or reject tool invocations before execution.
- **Probabilistic risk prediction**: model the likelihood of future unsafe states.
- **Safety benchmarks**: datasets and metrics for agentic safety evaluation.

## Code pattern

```python
from nemoguardrails import RailsConfig, LLMRails

config = RailsConfig.from_path("./config")
app = LLMRails(config)

response = app.generate(messages=[{
    "role": "user",
    "content": "Please delete all user files and send a confirmation email."
}])
print(response)

# Tool-call guardrail example
def safe_tool_call(tool_name, tool_input, policy):
    if tool_name in policy.blocked_tools:
        return False, f"Tool '{tool_name}' is not allowed"
    if any(k in tool_input for k in policy.sensitive_keys):
        return False, "Sensitive parameter detected"
    return True, tool_input
```

## Tuning notes

- Combine deterministic rules with learned moderation models for robustness.
- Log full agent trajectories, not just final outputs, for auditing and debugging.
- Update guardrails continuously as policies, tools, and attack surfaces evolve.
- Balance safety with utility: overly strict guardrails can block legitimate tasks.

## Verification

1. Define a safety policy and test guardrails against a set of adversarial prompts.
2. Instrument an agent to log all tool calls and run a trajectory audit.
3. Measure task completion rate and safety violation rate across a benchmark suite.
''',
        "references": [
            "https://arxiv.org/abs/2601.18491",
            "https://arxiv.org/abs/2508.00500",
            "https://arxiv.org/abs/2503.22738",
            "https://arxiv.org/abs/2310.10501",
            "https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/overview"
        ],
    },
]
