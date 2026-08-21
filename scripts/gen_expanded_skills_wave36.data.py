SKILLS = [
    {
        "name": "ai-for-quantum-hardware",
        "title": "AI for Quantum Hardware",
        "description": "Use machine learning to calibrate qubits, decode errors, optimize control pulses, and design quantum processor components.",
        "devin_body": r'''
## When to use

You are designing, calibrating, or controlling qubits and quantum processors and need to automate gate design, real-time feedback, or error decoding.

## Usage

- Calibrate qubits and optimize pulse shapes, gate sets, and real-time feedback from measurement data.
- Decode quantum errors with neural decoders such as transformer-based syndrome-to-correction models.
- Apply reinforcement learning to design error-robust gates without a detailed Hamiltonian.
- Build fast surrogate models to replace expensive quantum device simulations.

## Steps

1. Collect qubit characterization, gate, and noise data from the target quantum platform.
2. Train an ML model for calibration, control, or error decoding.
3. Use the model to optimize pulses, gate parameters, or decoder thresholds.
4. Validate the optimized gates or decoder on realistic noise models and real device data.
5. Integrate the model into the control stack for real-time feedback.
6. Retrain as device drift and noise characteristics change.

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
        "description": "Use machine learning to discover magnetic materials, model skyrmions, and optimize spintronic devices such as MRAM.",
        "devin_body": r'''
## When to use

You are discovering spintronic materials, modeling magnetic textures such as skyrmions, or optimizing spin-orbit-torque MRAM devices.

## Usage

- Screen heavy-metal/ferromagnet stacks for high spin-orbit and spin-transfer torque efficiency.
- Predict stable skyrmion-host compounds and Dzyaloshinskii-Moriya interaction strength.
- Build surrogate models that map MRAM stack parameters to switching current, retention, and margins.
- Propose novel magnetic compounds with generative models for spintronic applications.

## Steps

1. Curate DFT, micromagnetic, and experimental data for candidate spintronic materials.
2. Train predictors for spin Hall conductivity, skyrmion stability, or MRAM switching.
3. Screen new materials or stack designs against fabrication and stability criteria.
4. Validate magnetic texture predictions with micromagnetic simulations.
5. Optimize an SOT-MRAM or skyrmion device and compare switching energy to a baseline.
6. Iterate with foundry constraints and experimental feedback.

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
        "description": "Use machine learning to model memristor devices, simulate crossbar arrays, and co-design compute-in-memory accelerators.",
        "devin_body": r'''
## When to use

You are building or simulating memristor crossbars, compute-in-memory tiles, or analog AI accelerators based on resistive switching.

## Usage

- Learn compact device models from I-V and pulse data.
- Simulate analog matrix-vector multiplication on crossbars with device nonidealities.
- Predict device-to-device and cycle-to-cycle variation effects on inference accuracy.
- Co-design mixed-precision memristor and SRAM compute-in-memory tiles.

## Steps

1. Collect memristor I-V, pulse, and endurance data from the target device technology.
2. Fit a neural or physics-informed surrogate to the device behavior.
3. Build a crossbar simulator that models conductance, line resistance, and noise.
4. Run an MLP or kernel layer on the crossbar and measure accuracy under variation.
5. Co-design with digital tiles and quantization to meet accuracy and energy targets.
6. Verify the design against SPICE or measured data and compare energy-delay to a digital baseline.

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
        "description": "Use machine learning to inversely design photonic components, train fast surrogates, and automate PIC layout.",
        "devin_body": r'''
## When to use

You are designing photonic integrated circuits (PICs), waveguides, couplers, modulators, or foundry-ready silicon photonics components.

## Usage

- Optimize waveguide, coupler, modulator, and PIC geometries with adjoint, gradient, or surrogate methods.
- Replace FDTD/EME simulations with fast neural-network surrogates in design loops.
- Embed foundry DRC, variability, and process windows into the design objective.
- Generate GDS layouts and compact cells for large-scale photonic integrated circuits.

## Steps

1. Define the target optical response and parameterize the photonic component geometry.
2. Run a coarse-to-fine FDTD or EME simulation to create training data.
3. Train a surrogate or use an adjoint/inverse-design optimizer to meet the response target.
4. Add foundry constraints and process-window penalties to ensure manufacturability.
5. Generate a GDS layout and run DRC and full-wave verification.
6. Iterate on geometry and fabrication tolerances.

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
        "description": "Use machine learning to co-design 2.5D/3D chiplet packages, route interconnects, and optimize thermal and signal integrity.",
        "devin_body": r'''
## When to use

You are architecting heterogeneous chiplet systems, interposers, 2.5D/3D packages, or package-level power/thermal/signal-integrity co-design.

## Usage

- Optimize chiplet partitioning, die disaggregation, and package-level floorplanning.
- Route UCIe die-to-die links while respecting signal-integrity constraints.
- Co-design for thermal, mechanical stress, and CTE-mismatch reliability.
- Trade off power, performance, area, and cost across architecture and packaging.

## Steps

1. Build a package-level netlist with die sizes, bump maps, and thermal/power constraints.
2. Use ML or optimization to place chiplets and assign UCIe links.
3. Route signals and verify eye masks, crosstalk, and timing budgets.
4. Run FEM thermal and stress simulations and feed results back into placement.
5. Co-optimize with architecture for memory bandwidth and compute throughput.
6. Verify the final floorplan with signoff DRC, signal integrity, and thermal tests.

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
        "description": "Use machine learning to generate RTL, floorplan chips, optimize placement, and assist analog and mixed-signal design.",
        "devin_body": r'''
## When to use

You are automating digital or analog IC design tasks, including floorplanning, placement, standard-cell routing, or EDA-tool scripting.

## Usage

- Optimize macro and standard-cell placement for power, performance, and area with deep RL.
- Generate Verilog, Tcl, and Python EDA flows with domain-adapted code LLMs.
- Size transistors and layout analog cells with Bayesian optimization and surrogates.
- Explore design trade-offs across architecture, PPA, and manufacturability.

## Steps

1. Prepare netlist, constraints, and floorplan input for the target IC block.
2. Train an RL placement agent or a surrogate for analog sizing.
3. Legalize and sign off the placement with commercial EDA tools.
4. Use a code LLM to generate or review synthesis and STA scripts.
5. Verify timing, congestion, DRC, and power-grid constraints.
6. Compare the optimized design to a manual or baseline flow.

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
        "description": "Use machine learning to detect Trojans, analyze side-channel leakage, evaluate PUFs, and secure accelerators.",
        "devin_body": r'''
## When to use

You are assessing the security of ASICs, FPGAs, or AI accelerators; detecting Trojans, side-channel leakage, or PUF vulnerabilities; or designing trusted hardware.

## Usage

- Classify power and electromagnetic traces to recover keys or detect side-channel leakage.
- Detect anomalous circuit behavior and layout features of hardware Trojans.
- Assess PUF entropy, attack robustness, and anti-counterfeiting properties.
- Monitor neural accelerators at run time for fault and Trojan attacks.

## Steps

1. Collect side-channel, layout, or run-time traces under varying conditions.
2. Train a classifier or anomaly detector for the target threat (Trojan, leakage, fault).
3. Validate the model on unseen attack scenarios and device corners.
4. Integrate detection into a test, supply-chain, or run-time monitoring flow.
5. Evaluate security overhead in area, power, and latency against performance.
6. Update the model as new Trojan designs or attack strategies emerge.

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
        "description": "Use machine learning and co-optimization to deploy tiny models on microcontrollers, DSPs, and low-power SoCs.",
        "devin_body": r'''
## When to use

You are deploying ML on microcontrollers, DSPs, or low-power SoCs and need to meet latency, memory, and energy budgets.

## Usage

- Run sub-milliwatt inference on Cortex-M, RISC-V, or custom DSP cores.
- Quantize and prune models to int8/int16 with mixed precision.
- Co-design neural architectures and inference engines for a target MCU.
- Match operators, memory hierarchy, and on-device training to the hardware.

## Steps

1. Profile the target MCU for SRAM, Flash, and MAC limits.
2. Select or search a TinyML network with NAS and quantization.
3. Convert to TFLite Micro or CMSIS-NN with per-layer quantization.
4. Validate on the actual device, not just the simulator.
5. Measure latency and energy with MLPerf Tiny or board-level benchmarks.
6. Iterate on the network, operator support, and memory allocation.

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
        "description": "Compile and deploy tiny language models and vision detectors onto RISC-V microcontrollers and NPUs for milliwatt inference.",
        "devin_body": r'''
## When to use

You are selecting, programming, or designing an edge AI accelerator (NPU, TPU, GPU, FPGA) and need to optimize inference throughput and energy.

## Usage

- Architect dataflow, systolic, and in-memory arrays for low-power inference.
- Map and tile operators to maximize MAC utilization and minimize off-chip traffic.
- Benchmark accuracy, latency, and energy on MLPerf Tiny and Edge suites.
- Exploit int4/int8, block sparsity, and structured pruning on the target NPU.

## Steps

1. Profile the target accelerator's op set, tensor formats, and memory bandwidth.
2. Quantize and optimize the model for the supported bit width and sparsity.
3. Map operators to the accelerator and tile tensors to reduce memory traffic.
4. Run end-to-end inference on the target board and measure accuracy and latency.
5. Compare the quantized model to a floating-point baseline on energy-delay product.
6. Fall back unsupported operators to the CPU and profile the overhead.

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
        "description": "Use machine learning to predict electronics cooling, control data-center thermal systems, and co-design heat sinks and packages.",
        "devin_body": r'''
## When to use

You are designing heat sinks, cold plates, 3D/2.5D packages, or data-center cooling and need fast thermal predictions for optimization.

## Usage

- Replace CFD simulations with neural networks and Fourier neural operator surrogates.
- Control data-center cooling with reinforcement learning and MPC.
- Predict junction temperature and hot spots from package and heat-sink geometry.
- Embed heat-equation constraints with physics-informed neural networks.

## Steps

1. Define the thermal scenario (package, heat sink, or data center) and collect CFD/FEM data.
2. Train a surrogate thermal model with high-fidelity training and validation splits.
3. Use the surrogate in an optimization loop for geometry or set points.
4. Enforce boundary conditions and conservation laws with PINNs or hybrid loss terms.
5. Validate predictions against CFD/FEM under unseen operating conditions.
6. Co-optimize with mechanical stress and reliability constraints.

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
        "description": "Use machine learning to train spiking neural networks and map them to neuromorphic chips such as Loihi and SpiNNaker.",
        "devin_body": r'''
## When to use

You are programming or designing neuromorphic chips (e.g., Loihi, TrueNorth, BrainScaleS, SpiNNaker) and need to train and deploy SNNs.

## Usage

- Train event-driven SNNs with surrogate gradients, ANN-to-SNN conversion, or direct time-to-first-spike coding.
- Map neurons and synapses to cores while respecting on-chip learning and routing constraints.
- Pair DVS cameras and silicon cochleas with neuromorphic processors for event-based sensing.
- Balance accuracy with spike sparsity for energy-efficient inference.

## Steps

1. Choose a neuromorphic chip or simulator (Loihi, TrueNorth, BrainScaleS, SpiNNaker).
2. Prepare an event-based dataset (N-MNIST, DVS Gesture) and preprocess spikes.
3. Train the SNN with surrogate gradients or conversion and tune time constants.
4. Map the SNN to cores and verify spike routing feasibility.
5. Validate accuracy and event count on the target simulator or hardware.
6. Measure energy per spike and latency for the target workload.

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
            "https://arxiv.org/abs/1901.03690",
            "https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.795876/full",
            "https://impact.ornl.gov/en/publications/a-review-of-spiking-neuromorphic-hardware-communication-systems/",
            "https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.667011/full",
        ],
    },
    {
        "name": "ai-for-photonic-hardware",
        "title": "AI for Photonic Hardware",
        "description": "Use machine learning to design, calibrate, and program photonic AI accelerators and optical neural networks.",
        "devin_body": r'''
## When to use

You are building or programming photonic AI accelerators, optical neural networks, or photonic tensor cores for matrix/vector and tensor operations.

## Usage

- Implement matrix-vector multiplication with Mach-Zehnder meshes, microring resonators, and coherent crossbars.
- Combine photonic linear layers with electronic nonlinearities and memory in hybrid compute.
- Co-design the algorithm, photonic device, and control electronics.
- Calibrate and mitigate phase drift, crosstalk, and optical loss.

## Steps

1. Define the photonic accelerator architecture and the target AI workload.
2. Construct a simulation of MVM, phase shifters, photodetectors, and ADC/DAC.
3. Train an optical neural network or calibration model in the photonic simulator.
4. Calibrate phase shifters and photodiode gains with on-chip feedback loops.
5. Implement error mitigation for phase drift, crosstalk, and optical loss.
6. Verify a small network on the photonic chip or test bench and compare to a digital baseline.

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