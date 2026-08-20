SKILLS = [
    {
        "name": "ai-for-quantum-hardware",
        "title": "AI for Quantum Hardware",
        "description": "ML-driven qubit control, calibration, error decoding, and quantum processor design for superconducting, trapped-ion, and neutral-atom systems.",
        "devin_body": r'''
## When to use

You are designing, calibrating, or controlling qubits and quantum processors and need to automate gate design, real-time feedback, or error decoding.

## Key concepts

- **Qubit calibration and control**: ML optimizes pulse shapes, gate sets, and real-time feedback using measurement data.
- **Quantum error decoding**: neural decoders (e.g., transformer-based AlphaQubit) map syndromes to corrections.
- **Reinforcement learning for control**: model-free DRL designs error-robust gates and stabilizes qubits without a detailed Hamiltonian.
- **Surrogate modeling**: fast ML surrogates replace expensive quantum device simulations for design-space exploration.

## Code pattern

```python
import numpy as np
from stable_baselines3 import PPO

# Example: pulse-amplitude optimization via a custom RL environment
amplitudes = np.linspace(0.0, 1.0, 64)
best = amplitudes[np.argmax(rewards)]
```

## Tuning notes

- Match the control bandwidth and latency to the qubit coherence time.
- Use physics-informed reward shaping to avoid local optima in RL.
- Validate learned decoders on realistic noise models and real device data.

## Verification

1. Train a neural decoder on simulated surface-code syndromes and compare the logical error rate to a minimum-weight perfect-matching baseline.
2. Use DRL to optimize a single-qubit gate and measure gate-fidelity improvement.
3. Build a surrogate that predicts a qubit figure of merit from design parameters and validate it against full simulations.
''',
        "references": [
            "https://doi.org/10.1038/s41586-024-08148-8",
            "https://doi.org/10.1038/s41467-023-42901-3",
            "https://doi.org/10.1103/prxquantum.2.040324",
            "https://doi.org/10.1109/tai.2023.3243187",
        ],
    },
    {
        "name": "ai-for-spintronics",
        "title": "AI for Spintronics",
        "description": "ML for magnetic material discovery, skyrmion and MRAM device modeling, spin-orbit torque optimization, and spin-wave logic.",
        "devin_body": r'''
## When to use

You are discovering spintronic materials, modeling magnetic textures such as skyrmions, or optimizing spin-orbit-torque MRAM devices.

## Key concepts

- **Spin-orbit torque (SOT) and spin-transfer torque (STT)**: ML screens heavy-metal/ferromagnet stacks for high charge-to-spin conversion.
- **Skyrmion materials**: classifiers predict stable skyrmion-host compounds and Dzyaloshinskii-Moriya interaction strength.
- **MRAM device modeling**: surrogate models map stack parameters to switching current, retention, and read/write margins.
- **Generative materials design**: GANs and diffusion models propose novel magnetic compounds for spintronic applications.

## Code pattern

```python
from pymatgen.core import Composition
from sklearn.ensemble import GradientBoostingRegressor

# Train a surrogate for SOT efficiency from compositional descriptors
X = featurize_compositions(compositions)
model = GradientBoostingRegressor().fit(X, sot_efficiency)
```

## Tuning notes

- Include fabrication constraints and stability criteria (energy above hull) in screening.
- Use high-throughput DFT data as labels; augment with experimental measurements when available.
- Validate magnetic texture predictions with micromagnetic simulations (e.g., MuMax3).

## Verification

1. Train an ML model to predict spin Hall conductivity and rank candidate materials.
2. Predict stable skyrmion formation in a new compound and verify it with DFT/micromagnetic simulation.
3. Optimize an SOT-MRAM stack and compare switching energy to a baseline design.
''',
        "references": [
            "https://doi.org/10.1038/s41524-025-01626-1",
            "https://www.nature.com/articles/s44306-024-00044-1",
            "https://pubs.rsc.org/en/content/articlelanding/2023/ce/d3ce00765k",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC10019916/",
        ],
    },
    {
        "name": "ai-for-memristors",
        "title": "AI for Memristors",
        "description": "Crossbar array modeling, compute-in-memory mapping, device variability learning, and memristor-based AI accelerator co-design.",
        "devin_body": r'''
## When to use

You are building or simulating memristor crossbars, compute-in-memory tiles, or analog AI accelerators based on resistive switching.

## Key concepts

- **Memristor device models**: learning compact models (e.g., ODE-based, physics-informed) from I-V and pulse data.
- **Crossbar MVM**: mapping weights to conductance states and simulating analog matrix-vector multiplication with nonidealities.
- **Variability and yield**: ML predicts device-to-device and cycle-to-cycle variation effects on inference accuracy.
- **Hardware-software co-design**: mixed-precision memristor + SRAM CIM partitioning for accuracy and energy.

## Code pattern

```python
import numpy as np

# Analog MVM on a memristor crossbar with device variation
G = np.random.lognormal(mean=0.0, sigma=0.1, size=(m, n)) * G_target
I = G @ x
y = adc_quantize(I, bits=4)
```

## Tuning notes

- Calibrate conductance programming with closed-loop write-and-verify schemes.
- Model nonidealities (line resistance, sneak paths, noise, retention) at the circuit level.
- Use bit-slicing and hybrid digital/analog tiles to mitigate variability for precision-sensitive layers.

## Verification

1. Fit a neural or physics-informed surrogate to measured memristor I-V curves.
2. Simulate an MLP layer on a crossbar and measure accuracy degradation under device variation.
3. Compare the energy-delay product of a memristor CIM tile to a digital baseline for the same workload.
''',
        "references": [
            "https://www.nature.com/articles/s41928-025-01537-5",
            "https://www.nature.com/articles/s41586-025-08639-2",
            "https://www.nature.com/articles/s41467-025-61025-4",
            "https://www.nature.com/articles/s44172-025-00461-y",
        ],
    },
    {
        "name": "ai-for-integrated-photonics",
        "title": "AI for Integrated Photonics",
        "description": "Inverse design, layout generation, and fabrication-aware optimization of silicon-photonic and photonic-integrated-circuit components.",
        "devin_body": r'''
## When to use

You are designing photonic integrated circuits (PICs), waveguides, couplers, modulators, or foundry-ready silicon photonics components.

## Key concepts

- **Inverse design**: adjoint/gradient and neural-surrogate methods optimize geometry for target spectral or field response.
- **Surrogate modeling**: fast neural-network surrogates replace FDTD/EME simulations in design loops.
- **Foundry constraints**: DRC, fabrication variability, and process windows must be embedded in the objective.
- **Layout automation**: ML generates GDS layouts and compact cells for large-scale PICs.

## Code pattern

```python
import gdsfactory as gf
import tidy3d as td

# Define a parameterized photonic component and simulation
c = gf.components.mmi1x2()
sim = td.Simulation(size=(10, 10, 0.22), grid_spec=td.GridSpec.auto(wavelength=1.55))
```

## Tuning notes

- Use a coarse-to-fine mesh and geometry parameterization to reduce simulation cost.
- Penalize small feature sizes to ensure manufacturability in the target foundry process.
- Train surrogates on diverse wavelength, polarization, and geometry samples for robustness.

## Verification

1. Inverse-design a wavelength demultiplexer and validate S-parameters with FDTD.
2. Train a surrogate to predict transmission and compare prediction time and error to a full-wave solver.
3. Generate a PIC layout and verify that it passes foundry DRC.
''',
        "references": [
            "https://doi.org/10.1021/acsphotonics.9b01540",
            "https://www.nature.com/articles/s41566-018-0246-9",
            "https://www.nature.com/articles/s41578-026-00915-5",
            "https://www.mdpi.com/2076-3417/11/9/3822",
        ],
    },
    {
        "name": "ai-for-advanced-packaging",
        "title": "AI for Advanced Packaging",
        "description": "Co-design of 2.5D/3D chiplets, interconnect routing, signal-integrity-aware placement, and package-thermal optimization.",
        "devin_body": r'''
## When to use

You are architecting heterogeneous chiplet systems, interposers, 2.5D/3D packages, or package-level power/thermal/signal-integrity co-design.

## Key concepts

- **Chiplet partitioning and placement**: ML/RL optimizes die disaggregation and package-level floorplanning.
- **Interconnect and routing**: UCIe-based die-to-die links, signal-integrity constraints, and place-to-route algorithms.
- **Thermal-mechanical co-design**: stress, warpage, and CTE-mismatch aware placement for reliability.
- **PPAC optimization**: power, performance, area, and cost trade-offs across architecture and packaging.

## Code pattern

```python
import networkx as nx
from ortools.constraint_solver import routing_enums_pb2

# Build a chiplet network and solve a routing/assignment problem
G = nx.grid_graph(dim=(4, 4))
# Use an RL or OR solver to place chiplets and route signals
```

## Tuning notes

- Co-optimize with architecture (memory bandwidth, compute throughput) and thermal constraints.
- Include package-level parasitics and UCIe eye-mask specifications.
- Use digital-twin or FEM-based thermal/stress models for validation, not just analytical estimates.

## Verification

1. Run a chiplet placement optimization and compare wirelength and thermal profile to a manual floorplan.
2. Verify signal-integrity compliance (eye diagram) for a routed chiplet interconnect.
3. Stress-test a 3D package stack under power and thermal cycling using FEM.
''',
        "references": [
            "https://doi.org/10.1109/TC.2024.3457740",
            "https://doi.org/10.1109/iccd65941.2025.00029",
            "https://ieeexplore.ieee.org/document/10965735",
            "https://www.uciexpress.org/",
        ],
    },
    {
        "name": "ai-for-chip-design",
        "title": "AI for Chip Design",
        "description": "ML for RTL generation, EDA scripting, floorplanning, placement, routing, timing optimization, and analog/mixed-signal design.",
        "devin_body": r'''
## When to use

You are automating digital or analog IC design tasks, including floorplanning, placement, standard-cell routing, or EDA-tool scripting.

## Key concepts

- **Floorplanning and placement**: deep RL (e.g., AlphaChip) optimizes macro and standard-cell placement for PPA.
- **RTL and EDA scripting**: domain-adapted LLMs (e.g., ChipNeMo) generate Verilog, Tcl, and Python EDA flows.
- **Analog design**: ML surrogate models and Bayesian optimization size transistors and layout cells.
- **Design-space exploration**: multi-objective optimization over architecture, PPA, and manufacturability.

## Code pattern

```python
import tensorflow as tf
from circuit_training.learning import ppo_lib

# Policy network inputs a graph netlist and outputs placement coordinates
policy = ppo_lib.PolicyNet(num_actions=128)
```

## Tuning notes

- Use realistic constraints (timing, congestion, DRC, power grid) as reward or loss terms.
- Combine learned placement with commercial EDA legalizers and signoff tools.
- Fine-tune code LLMs on internal EDA scripts and design documentation for safe deployment.

## Verification

1. Generate a chip floorplan with an RL agent and compare wirelength/congestion to a human baseline.
2. Use a domain LLM to write a synthesis/STA Tcl script and run it in a commercial tool.
3. Optimize an analog cell with a learned surrogate and verify performance with SPICE.
''',
        "references": [
            "https://doi.org/10.1038/s41586-021-03544-w",
            "https://github.com/google-research/circuit_training",
            "https://doi.org/10.48550/arxiv.2311.00176",
            "https://openroad.readthedocs.io/en/latest/",
        ],
    },
    {
        "name": "ai-for-hardware-security",
        "title": "AI for Hardware Security",
        "description": "ML for side-channel analysis, hardware Trojan and PUF detection, supply-chain assurance, and secure accelerator design.",
        "devin_body": r'''
## When to use

You are assessing the security of ASICs, FPGAs, or AI accelerators; detecting Trojans, side-channel leakage, or PUF vulnerabilities; or designing trusted hardware.

## Key concepts

- **Side-channel analysis**: deep learning classifies power/electromagnetic traces to recover keys or detect leakage.
- **Hardware Trojan detection**: supervised and unsupervised ML identify anomalous circuit behavior or layout features.
- **PUFs and anti-counterfeiting**: ML models assess PUF entropy and attack robustness, or assist in PUF design.
- **Secure AI accelerators**: run-time monitoring and anomaly detection protect neural accelerators against fault/Trojan attacks.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import IsolationForest

# Detect anomalous side-channel traces from a Trojan-infected IC
clf = IsolationForest(contamination=0.02).fit(traces)
anomaly_scores = clf.decision_function(test_traces)
```

## Tuning notes

- Collect traces under varying temperature, voltage, and process corners for robust models.
- Avoid overfitting to specific attack scenarios; validate against unseen Trojan designs.
- Balance security overhead (area, power, latency) with system performance.

## Verification

1. Train a CNN side-channel classifier and report key-recovery success on an open AES dataset.
2. Detect a set of unknown hardware Trojans using an unsupervised anomaly detector.
3. Evaluate a PUF's unpredictability and resistance to modeling attacks.
''',
        "references": [
            "https://link.springer.com/article/10.1007/s41635-026-00182-4",
            "https://doi.org/10.3390/mi15010149",
            "https://doi.org/10.1109/satc65530.2025.11137155",
            "https://doi.org/10.3390/cryptography9010005",
        ],
    },
    {
        "name": "ai-for-embedded-ai",
        "title": "AI for Embedded AI",
        "description": "TinyML, on-device inference, quantization, neural architecture search, and co-optimization for microcontrollers and DSPs.",
        "devin_body": r'''
## When to use

You are deploying ML on microcontrollers, DSPs, or low-power SoCs and need to meet latency, memory, and energy budgets.

## Key concepts

- **TinyML**: sub-1 mW inference on Cortex-M, RISC-V, or custom DSP cores.
- **Quantization and pruning**: int8/int16, unstructured/structured pruning, and mixed-precision search.
- **Neural architecture search (NAS)**: TinyNAS co-designs networks and inference engines for a target MCU.
- **Hardware-software co-design**: matching operator support, memory hierarchy, and on-device training.

## Code pattern

```python
import tensorflow as tf

# Convert a trained model to a quantized TFLite Micro model
converter = tf.lite.TFLiteConverter.from_saved_model("model")
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()
```

## Tuning notes

- Profile peak SRAM and Flash usage against the target device limits.
- Use per-layer quantization to preserve accuracy for sensitive layers.
- Validate on the actual embedded target, not just the host simulator, to catch timing and cache effects.

## Verification

1. Deploy a keyword-spotting model on a Cortex-M4 and measure latency/energy with MLPerf Tiny.
2. Run a TinyNAS search for an MCU and compare accuracy to a hand-tuned MobileNet.
3. Perform on-device inference on a held-out test set and confirm bit-exact outputs with the reference.
''',
        "references": [
            "https://hanlab.mit.edu/projects/mcunet",
            "https://github.com/ARM-software/CMSIS-NN",
            "https://github.com/tensorflow/tflite-micro",
            "https://www.arm.com/resources/guide/machine-learning-on-cortex-m",
        ],
    },
    {
        "name": "ai-for-edge-accelerators",
        "title": "AI for Edge Accelerators",
        "description": "NPU/TPU/FPGA edge accelerator design, benchmarking, mapping, and optimization for low-latency, energy-efficient inference.",
        "devin_body": r'''
## When to use

You are selecting, programming, or designing an edge AI accelerator (NPU, TPU, GPU, FPGA) and need to optimize inference throughput and energy.

## Key concepts

- **Edge NPU/TPU architectures**: dataflow, systolic arrays, and in-memory computing for low-power inference.
- **Model mapping and tiling**: schedule operators to maximize MAC utilization and minimize off-chip traffic.
- **Benchmarking**: MLPerf Tiny and MLPerf Edge provide fair accuracy/latency/energy metrics.
- **Hybrid precision and sparsity**: exploit int4/int8, block sparsity, and structured pruning on accelerator hardware.

## Code pattern

```python
import onnxruntime as ort
import numpy as np

# Run a quantized model on an edge NPU with ONNX Runtime
session = ort.InferenceSession("model.onnx", providers=["NPUExecutionProvider"])
out = session.run(None, {"input": np.zeros((1, 3, 224, 224), dtype=np.float32)})
```

## Tuning notes

- Align model operators with the accelerator's supported op set and tensor formats.
- Quantize activations and weights to the supported bit width; fall back to CPU for unsupported ops.
- Measure end-to-end latency and energy on the target board, not just layer-wise roofline.

## Verification

1. Benchmark an image-classification model on an edge NPU and report top-1 accuracy vs. latency.
2. Profile operator placement and memory movement for a transformer on a Jetson/Coral board.
3. Compare an int8-quantized model to a floating-point baseline on energy-delay product.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2106.07597",
            "https://mlcommons.org/working-groups/benchmarks/tiny/",
            "https://www.mdpi.com/1999-4893/15/11/419",
            "https://doi.org/10.3390/electronics14244877",
        ],
    },
    {
        "name": "ai-for-thermal-design",
        "title": "AI for Thermal Design",
        "description": "ML surrogates for electronics cooling, data-center thermal control, heat-sink and package thermal co-design, and CFD emulation.",
        "devin_body": r'''
## When to use

You are designing heat sinks, cold plates, 3D/2.5D packages, or data-center cooling and need fast thermal predictions for optimization.

## Key concepts

- **Surrogate thermal modeling**: neural networks and Fourier neural operators replace expensive CFD simulations.
- **Data-center cooling control**: reinforcement learning and MPC optimize fan speed, set points, and workload placement.
- **Package and heat-sink design**: ML predicts junction temperature, hot spots, and thermal resistance from geometry.
- **Physics-informed neural networks (PINNs)**: embed heat-equation constraints for reliable extrapolation.

## Code pattern

```python
import torch
import torch.nn as nn

# Simple surrogate mapping package geometry to maximum temperature
model = nn.Sequential(nn.Linear(64, 128), nn.ReLU(), nn.Linear(128, 1))
T_max = model(geometry_features)
```

## Tuning notes

- Use high-fidelity CFD/FEM data for training and validate on unseen operating conditions.
- Enforce boundary conditions and conservation laws with PINNs or hybrid loss terms.
- Co-optimize with mechanical stress and reliability constraints for 3D packages.

## Verification

1. Train a surrogate to predict a heat-sink or cold-plate temperature field and compare to CFD with less than 5% error.
2. Run an RL cooling controller in a data-center simulator and show energy reduction.
3. Optimize a chip-package thermal design and verify junction temperature with FEM.
''',
        "references": [
            "https://doi.org/10.1063/5.0206287",
            "https://doi.org/10.1145/3708890",
            "https://doi.org/10.1109/eptc62800.2024.10909871",
            "https://arxiv.org/abs/2103.11177",
        ],
    },
    {
        "name": "ai-for-neuromorphic-hardware",
        "title": "AI for Neuromorphic Hardware",
        "description": "Spiking neural network training, SNN-to-chip mapping, event-based processing, and co-design with analog/mixed-signal neuromorphic platforms.",
        "devin_body": r'''
## When to use

You are programming or designing neuromorphic chips (e.g., Loihi, TrueNorth, BrainScaleS, SpiNNaker) and need to train and deploy SNNs.

## Key concepts

- **Spiking neural networks (SNNs)**: event-driven, sparse computation with temporal dynamics.
- **Training methods**: surrogate gradients, ANN-to-SNN conversion, and direct SNN training with time-to-first-spike coding.
- **Chip mapping**: mapping neurons/synapses to cores, on-chip learning, and spike routing constraints.
- **Event-based sensing**: pairing DVS cameras and silicon cochleas with neuromorphic processors.

## Code pattern

```python
import snntorch as snn
import torch

# Leaky integrate-and-fire neuron
lif = snn.Leaky(beta=0.9)
spk, mem = lif(cur_in, mem_prev)
```

## Tuning notes

- Choose time constants and thresholds that match the target neuromorphic hardware.
- Balance accuracy with spike sparsity to maximize energy efficiency.
- Validate on the target chip or a cycle-accurate simulator, not just a software backend.

## Verification

1. Train an SNN classifier on a neuromorphic dataset (e.g., N-MNIST, DVS Gesture) and report accuracy vs. event count.
2. Map an SNN to a Loihi/SpiNNaker core graph and verify spike routing feasibility.
3. Measure energy per spike on the target neuromorphic hardware for a keyword-spotting task.
''',
        "references": [
            "https://arxiv.org/html/1901.03690",
            "https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.795876/full",
            "https://impact.ornl.gov/en/publications/a-review-of-spiking-neuromorphic-hardware-communication-systems/",
            "https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.667011/full",
        ],
    },
    {
        "name": "ai-for-photonic-hardware",
        "title": "AI for Photonic Hardware",
        "description": "Photonic AI accelerators, optical neural networks, optoelectronic co-design, and programming of photonic tensor cores.",
        "devin_body": r'''
## When to use

You are building or programming photonic AI accelerators, optical neural networks, or photonic tensor cores for matrix/vector and tensor operations.

## Key concepts

- **Photonic matrix-vector multiplication (MVM)**: Mach-Zehnder meshes, microring resonators, and coherent crossbars for analog linear transforms.
- **Optical nonlinearities and hybrid compute**: combining photonic linear layers with electronic nonlinearities and memory.
- **Photonic accelerator co-design**: algorithm, photonic device, and control/electronics co-optimization.
- **Calibration and error mitigation**: phase drift, crosstalk, and loss-aware training.

## Code pattern

```python
import numpy as np

# Coherent MVM using a unitary mesh (simplified)
theta = np.random.rand(n, n)
U = construct_unitary_mesh(theta)
y = np.abs(U @ x) ** 2
```

## Tuning notes

- Calibrate phase shifters and photodiode gains with on-chip feedback loops.
- Account for optical losses, crosstalk, and ADC/DAC precision in the training graph.
- Use digital pre-emphasis and error correction for high-precision AI workloads.

## Verification

1. Implement a photonic MVM accelerator in simulation and compare matrix-vector output to a digital baseline.
2. Run a small neural network (e.g., MNIST) on a photonic tensor core and report accuracy.
3. Characterize and compensate phase drift over time in a programmable photonic chip.
''',
        "references": [
            "https://www.nature.com/articles/s41586-025-08854-x",
            "https://www.nature.com/articles/s41566-025-01799-7",
            "https://www.nature.com/articles/s41467-026-71599-2",
            "https://lightmatter.co/products/envise/",
        ],
    },
]
