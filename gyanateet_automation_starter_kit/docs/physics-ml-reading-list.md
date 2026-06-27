# Physics-Based ML Papers Reading List for Gyanateet Dutta

> Curated for someone who has completed the [UvA DL Course notebooks](https://uvadlc-notebooks.readthedocs.io/en/latest/index.html) 
> and [Physics-Based Deep Learning](https://www.physicsbaseddeeplearning.org/intro.html) materials, 
> and understands the progression from UNet-based CFD surrogate models → Fourier Neural Operators → 
> PINNs → graph-based weather/climate simulators. This list goes deeper into the seminal papers 
> behind each of these paradigms and connects them to your work in quantum ML, computer vision, 
> and representation learning.

---

## Tier 0: The Encoder-Decoder Foundation (You Know This, But Read the Papers)

### 1. U-Net: Convolutional Networks for Biomedical Image Segmentation
- **Venue**: MICCAI 2015
- **Link**: [arXiv:1505.04597](https://arxiv.org/abs/1505.04597)
- **Authors**: Ronneberger, Fischer, Brox
- **Why**: The architecture that started physics-based ML surrogate modeling. People were 
  using U-Nets for airfoil aerodynamics, CFD fields, and flow prediction before neural 
  operators came along. The skip connections that preserve spatial detail are the same 
  concept you use in your surgical AI work (DINOv2 + decoder).
- **Key idea**: Symmetric encoder-decoder with skip connections. The contracting path 
  captures context; the expanding path enables precise localization. Trained end-to-end 
  from very few images with aggressive data augmentation.
- **Your angle**: You know U-Net from medical imaging (your Endo-FM / surgical phase 
  recognition work). The same architecture was repurposed for PDE surrogate modeling — 
  instead of segmenting tissue, it predicts velocity/pressure fields. The progression 
  from U-Net → FNO is about going from fixed-grid to resolution-invariant operators.

### 2. Neural Message Passing for Quantum Chemistry (MPNN)
- **Venue**: ICML 2017
- **Link**: [arXiv:1704.01212](https://arxiv.org/abs/1704.01212)
- **Authors**: Gilmer, Schoenholz, Riley, Vinyals, Dahl (Google)
- **Why**: Unifies GNNs for molecular property prediction into a single framework. This 
  is the bridge between your quantum chemistry work and graph-based ML. The MPNN 
  framework subsumes Gilmer et al.'s directed message passing, which is the basis for 
  most modern molecular GNNs (SchNet, DimeNet, GemNet, etc.).
- **Key idea**: Message passing phase (aggregate neighbor information) + readout phase 
  (produce graph-level output). All molecular GNNs are variations on this theme — 
  different message functions, different aggregation operators.
- **Your angle**: Your `chemistry_encoder.py` in Conditional-GQE uses graph-level 
  features from molecular Hamiltonians. MPNN is the theoretical framework behind this. 
  The connection to physics-based ML: molecular properties are determined by physics 
  (Schrödinger equation), and GNNs learn to approximate this mapping efficiently.

---

## Tier 1: Neural Operators (The Resolution-Invariant Revolution)

### 3. Fourier Neural Operator (FNO)
- **Venue**: ICLR 2021
- **Link**: [arXiv:2010.08895](https://arxiv.org/abs/2010.08895)
- **Authors**: Li, Kovachki, Azizzadenesheli, et al. (Caltech/NVIDIA)
- **Why**: The paper that changed physics-based ML. Instead of learning a mapping 
  between fixed-resolution grids (like U-Net), FNO learns a mapping between function 
  spaces directly in Fourier space. This makes it **discretization-invariant** — train 
  on one grid, evaluate on another. Quasi-linear time complexity.
- **Key idea**: Replace spatial convolutions with global spectral convolutions. The 
  Fourier transform captures global patterns (low frequencies = large-scale structure, 
  high frequencies = fine details). Truncating high modes acts as a natural regularizer.
- **Your angle**: The spectral perspective connects to your quantum computing knowledge 
  — Fourier transforms are unitary transformations, and the FNO is essentially learning 
  in a rotated basis. The "resolution invariance" property is like the unitarity of 
  quantum operations — the operator acts on the function space, not its discretization.

### 4. DeepONet: Learning Nonlinear Operators
- **Venue**: Nature Machine Intelligence 2021
- **Link**: [arXiv:1910.03193](https://arxiv.org/abs/1910.03193)
- **Authors**: Lu, Jin, Pang, Zhang, Karniadakis
- **Why**: The other major neural operator architecture, based on the universal 
  approximation theorem for operators (Chen & Chen, 1995). DeepONet uses a "branch" 
  network to encode the input function and a "trunk" network to encode the query 
  points, then merges them. Complementary to FNO — different inductive bias.
- **Key idea**: A neural network with a single hidden layer can approximate any 
  nonlinear continuous operator. DeepONet implements this with a branch-trunk 
  architecture: branch encodes the input function evaluations, trunk encodes the 
  output coordinates, and their dot product gives the output.
- **Your angle**: The branch-trunk decomposition is like the encoder-decoder pattern 
  you know from transformers — the encoder (branch) processes the input sequence, 
  the decoder (trunk) generates the output at query positions. In Conditional-GQE, 
  your Hamiltonian encoder is the "branch" and the operator decoder is the "trunk."

### 5. Neural Operator Survey (The Comprehensive Review)
- **Venue**: JMLR 2023
- **Link**: [JMLR v24/21-1524](https://jmlr.org/papers/volume24/21-1524/21-1524.pdf)
- **Authors**: Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart, Anandkumar
- **Why**: The definitive survey. Unifies FNO, DeepONet, graph neural operators, 
  multi-pole graph neural operators, and low-rank neural operators under a single 
  framework. Proves the universal approximation theorem for neural operators and 
  provides exhaustive numerical comparisons on Burgers, Darcy flow, and Navier-Stokes.
- **Key idea**: Neural operators are compositions of linear integral operators and 
  nonlinear activation functions, defined on function spaces (not discretized grids). 
  Four parameterizations: graph-based, multi-pole graph, low-rank (SVD truncation), 
  and Fourier (spectral). All share the same theoretical guarantees.
- **Your angle**: Read this for the unifying mathematical framework. The integral 
  operator formulation generalizes the attention mechanism — attention is a kernel 
  integral operator with a learned kernel. FNO is attention with a spectral kernel.

### 6. Neural Operators for Accelerating Scientific Simulations and Design
- **Venue**: Nature Reviews Physics 2024
- **Link**: [nature.com/s42254-024-00712-5](https://www.nature.com/articles/s42254-024-00712-5)
- **Authors**: Azizzadenesheli, Kovachki, Li, et al.
- **Why**: The Nature Reviews perspective piece — accessible overview of how neural 
  operators are transforming computational science. Covers CFD, weather, material 
  modeling, and inverse design. 4-5 orders of magnitude speedup over conventional solvers.
- **Your angle**: The inverse design application is directly relevant to your quantum 
  circuit design problem — neural operators can optimize parameters for inverse problems 
  because they're differentiable. Same principle as your L-BFGS-B coefficient optimization, 
  but end-to-end.

---

## Tier 2: Physics-Informed Neural Networks (PINNs)

### 7. Physics-Informed Neural Networks (PINNs)
- **Venue**: Journal of Computational Physics 2019
- **Link**: [sciencedirect.com/S0021999118307125](https://www.sciencedirect.com/science/article/abs/pii/S0021999118307125)
- **arXiv**: [1711.10561](https://arxiv.org/abs/1711.10561) (Part I), [1711.10566](https://arxiv.org/abs/1711.10566) (Part II)
- **Authors**: Raissi, Perdikaris, Karniadakis
- **Why**: The foundational PINN paper. Embeds physical laws (PDEs) directly into the 
  loss function as soft constraints. The network learns to satisfy both data AND physics. 
  This is the "physics-based" in "physics-based deep learning."
- **Key idea**: Loss = data_misfit + λ · PDE_residual. The PDE residual is computed 
  via automatic differentiation — you differentiate the network output w.r.t. its inputs 
  to get derivatives, then plug into the PDE. No mesh, no solver, just a network and 
  autodiff.
- **Your angle**: You know this from the physicsbaseddeeplearning.org materials. The 
  deep connection to your quantum work: the Schrödinger equation is a PDE, and 
  variational quantum eigensolvers (VQE) are essentially physics-informed — the energy 
  expectation value is the "physics residual" that you minimize. Your Conditional-GQE 
  reward function (energy + entanglement + commutativity) is a multi-physics-informed 
  loss.

### 8. Data-Driven Discovery of Nonlinear PDEs
- **arXiv**: [1711.10566](https://arxiv.org/abs/1711.10566)
- **Authors**: Raissi, Perdikaris, Karniadakis
- **Why**: The inverse problem companion to PINNs. Instead of solving a known PDE, 
  discover the PDE itself from data. The network learns the coefficients of the PDE 
  terms. This is physics discovery, not just physics solving.
- **Key idea**: Parameterize the PDE as a linear combination of candidate terms 
  (u, u_x, u_xx, u·u_x, etc.) with learnable coefficients. Train the network to fit 
  data while simultaneously learning which PDE terms are important.
- **Your angle**: This is like learning the Hamiltonian from data — which is exactly 
  what your Hamiltonian generation pipeline does (computing molecular Hamiltonians 
  from geometry). The PINN approach could be used to discover effective Hamiltonians 
  from experimental data.

---

## Tier 3: AI for Weather and Climate (The Big Impact Papers)

### 9. GraphCast: Learned Global Weather Forecasting
- **Venue**: Science 2023
- **Link**: [science.org/adi2336](https://www.science.org/doi/10.1126/science.adi2336)
- **arXiv**: [2212.12794](https://arxiv.org/abs/2212.12794)
- **Code**: [github.com/google-deepmind/graphcast](https://github.com/google-deepmind/graphcast)
- **Authors**: Lam, Sanchez-Gonzalez, Willson, et al. (Google DeepMind)
- **Why**: The paper that proved AI can beat numerical weather prediction. GraphCast 
  uses graph neural networks on an icosahedral mesh to predict 10-day global weather 
  at 0.25° resolution in under 1 minute. Outperforms ECMWF HRES on 90% of 1380 targets.
- **Key idea**: Encode the atmospheric state onto a multi-resolution icosahedral mesh. 
  Message passing propagates information globally (long-range) and locally (fine-scale). 
  Decode back to the grid. The mesh structure naturally handles spherical geometry.
- **Your angle**: The icosahedral mesh is a natural multi-resolution representation — 
  similar to how your DINOv2 patch tokens at different scales capture hierarchical 
  features. The graph-based approach handles irregular geometries, which is crucial 
  for both weather (spherical Earth) and molecular systems (3D atomic positions).

### 10. FourCastNet: AFNO for Global Weather Forecasting
- **arXiv**: [2202.11214](https://arxiv.org/abs/2202.11214)
- **Code**: [github.com/NVlabs/FourCastNet](https://github.com/NVlabs/FourCastNet)
- **Authors**: Pathak, Subramanian, Harrington, et al. (NVIDIA)
- **Why**: NVIDIA's answer to AI weather forecasting. Uses Adaptive Fourier Neural 
  Operator (AFNO) attention — a vision transformer where attention is replaced by 
  FNO layers. This is the direct application of FNO to weather, and it's the paper 
  you mentioned about NVIDIA's weather sim work.
- **Key idea**: Replace O(N²) self-attention with O(N log N) FFT-based attention. 
  The adaptive Fourier layer learns which frequency modes to keep, providing both 
  global receptive field and computational efficiency. Generates a week-long forecast 
  in <2 seconds.
- **Your angle**: AFNO is essentially a vision transformer with spectral attention — 
  directly relevant to your DINOv2/V-JEPA2 work. The idea of replacing attention with 
  spectral operations is powerful and could apply to your transformer decoder: instead 
  of standard attention over operator tokens, use spectral attention to capture global 
  operator relationships.

### 11. GenCast: Diffusion-Based Ensemble Weather Forecasting
- **Venue**: Nature 2025
- **Link**: [nature.com/s41586-024-08252-9](https://www.nature.com/articles/s41586-024-08252-9)
- **arXiv**: [2312.15796](https://arxiv.org/abs/2312.15796)
- **Authors**: Price, Sanchez-Gonzalez, Alet, et al. (Google DeepMind)
- **Why**: GenCast is a **diffusion model** for weather forecasting — the same type 
  of generative model you work with in your diffusion research. It generates ensemble 
  forecasts (probabilistic) rather than single deterministic forecasts. Outperforms 
  ECMWF ENS on 97.2% of targets. This is where diffusion models meet physics-based ML.
- **Key idea**: A conditional diffusion model on the sphere. Given the current weather 
  state, generate a sample from the distribution of future weather states. The ensemble 
  of samples captures forecast uncertainty. Uses a score-based diffusion model adapted 
  to spherical geometry.
- **Your angle**: You know diffusion from first principles. GenCast shows that diffusion 
  models can capture the full distribution of physical outcomes, not just the mean. 
  This is directly relevant to your RL mode collapse problem — a diffusion-based approach 
  to circuit generation would naturally produce diverse outputs without needing 
  frequency penalties or diversity rewards. The distribution-matching property of 
  diffusion is the ultimate anti-mode-collapse mechanism.

### 12. NeuralGCM: Hybrid Physics-ML for Climate
- **Venue**: Nature 2024
- **Link**: [nature.com/s41586-024-07744-y](https://www.nature.com/articles/s41586-024-07744-y)
- **arXiv**: [2311.07222](https://arxiv.org/abs/2311.07222)
- **Authors**: Kochkov, Yuval, Langmore, et al. (Google Research)
- **Why**: A hybrid approach that combines traditional physics-based GCMs with ML 
  components. The dynamical core solves the resolved-scale equations (physics), while 
  ML parameterizes the sub-grid processes (learned). This is the "best of both worlds" 
  approach — physics for what we know, ML for what we don't.
- **Key idea**: Split the simulation into deterministic physics (large-scale dynamics 
  via spectral methods) and stochastic ML (small-scale parameterizations via neural 
  networks). The ML component learns from high-resolution simulations and observational 
  data. More accurate than pure physics for 2-15 day forecasts, and reproduces 40-year 
  climate statistics.
- **Your angle**: The hybrid physics-ML approach is exactly what your Conditional-GQE 
  does — the Hamiltonian (physics) defines the energy landscape, and the transformer 
  (ML) learns to navigate it. NeuralGCM's split between "known physics" and "learned 
  corrections" maps to your split between "UCCSD operator pool (physics)" and "RL policy 
  (learned)."

---

## Tier 4: Graph-Based Physics Simulation

### 13. Learning to Simulate Complex Physics with Graph Networks (GNS)
- **Venue**: ICML 2020
- **Link**: [arXiv:2002.09405](https://arxiv.org/abs/2002.09405)
- **Authors**: Sanchez-Gonzalez, Godwin, Pfaff, et al. (DeepMind)
- **Why**: The "learned simulator" paper. GNS learns to simulate particle-based physics 
  (fluids, granular materials, rigid bodies) using graph neural networks. Each particle 
  is a node; edges connect nearby particles. Message passing propagates forces and 
  velocities. Generalizes across different initial conditions and even different systems.
- **Key idea**: Encode particle state → message passing over spatial neighbors → 
  predict acceleration → integrate (Euler/Verlet). The learned simulator is 1-2 orders 
  of magnitude faster than physics engines like MuJoCo for comparable accuracy.
- **Your angle**: You know MuJoCo. GNS is the ML version of what MuJoCo does — but 
  learned from data instead of hand-coded physics. The graph structure naturally 
  represents physical interactions. This connects to your molecular GNN work: atoms 
  are particles, bonds are edges, and the "physics" is quantum mechanics.

---

## Tier 5: Connecting Physics-Based ML to Your Other Domains

### 14. Transformer for PDE Operator Learning (GalPT)
- **Venue**: TMLR 2023
- **Link**: [TMLR](https://openreview.net/forum?id=YiDVTlV3mE)
- **Authors**: Li, Meidani, Farimani
- **Why**: Applies the transformer architecture to PDE operator learning. Instead of 
  FNO's spectral convolutions, uses self-attention to capture long-range dependencies 
  in PDE solutions. Shows that transformers can be effective operator learners.
- **Your angle**: This is the bridge between your transformer expertise (Conditional-GQE, 
  surgical AI) and physics-based ML. The same transformer that generates quantum 
  circuits can, in principle, solve PDEs — the architecture is general enough.

### 15. Geo-FNO: Fourier Neural Operator on Arbitrary Geometries
- **Venue**: JMLR 2023
- **Authors**: Li, Huang, Liu, et al.
- **Why**: Extends FNO from regular grids to arbitrary geometries by learning a 
  deformation from the physical domain to a regular grid, applying FNO, then mapping 
  back. Enables FNO on complex 3D geometries (airfoils, pipes, arteries).
- **Your angle**: The deformation learning is like learning a coordinate transformation 
  in quantum mechanics — you transform to a basis where the problem is simpler, solve 
  there, then transform back. This is the same principle as Jordan-Wigner 
  transformations in your UCCSD operator pool.

---

## Suggested Reading Order

```
Tier 0 (Foundations you know, but read the papers):
  U-Net (1505.04597) → MPNN (1704.01212)

Tier 1 (Neural Operators — the core revolution):
  FNO (2010.08895) → DeepONet (1910.03193) → Survey (JMLR 2023) → Nature Reviews 2024

Tier 2 (PINNs):
  PINN Part I (1711.10561) → PINN Part II / Discovery (1711.10566)

Tier 3 (Weather & Climate — the big impact):
  FourCastNet (2202.11214) → GraphCast (2212.12794) → GenCast (2312.15796) → NeuralGCM (2311.07222)

Tier 4 (Graph-based simulation):
  GNS (2002.09405)

Tier 5 (Bridges to your other domains):
  GalPT (TMLR 2023) → Geo-FNO (JMLR 2023)
```

---

## How These Connect to Your Work

| Your Project | Papers That Inform It |
|---|---|
| Conditional-GQE Hamiltonian encoder | MPNN, DeepONet (branch-trunk), NeuralGCM (hybrid physics-ML) |
| Operator sequence generation | FNO (spectral operations), GalPT (transformer for PDEs) |
| Energy reward function | PINN (physics-informed loss), NeuralGCM (physics + ML hybrid) |
| UCCSD operator pool | Geo-FNO (coordinate transformations), GNS (particle-based physics) |
| Chemistry encoder (graph features) | MPNN, GNS (graph-based physical simulation) |
| Future: diffusion-based circuit gen | GenCast (diffusion for physical systems) |
| Surgical AI (DINOv2 + decoder) | U-Net (encoder-decoder), FourCastNet (AFNO = ViT + spectral) |
| V-JEPA2 / world models | GNS (learned simulators), NeuralGCM (hybrid models) |
| MuJoCo / robotics | GNS (learned physics), SAC (from RL list) |
| Inverse design / optimization | Neural Operator Survey (differentiable surrogates) |

---

## The Big Picture: Why This Matters for Your Research

The progression you described — **UNet → FNO → PINN → GraphCast/GenCast** — is the 
story of physics-based ML moving from:

1. **Fixed-grid surrogates** (U-Net): Learn a mapping on a specific discretization. 
   Fast but not generalizable to new resolutions or geometries.

2. **Resolution-invariant operators** (FNO, DeepONet): Learn a mapping between 
   function spaces. Train on one grid, evaluate on another. The operator is the object 
   of learning, not the grid function.

3. **Physics-constrained learning** (PINNs): Embed physical laws directly into the 
   loss. The network can't violate physics. Data-efficient and interpretable.

4. **Learned simulators** (GraphCast, GenCast, GNS): Replace entire physics engines 
  with learned models. Graph-based for irregular domains, diffusion-based for 
  uncertainty quantification, hybrid for combining known physics with learned corrections.

Your Conditional-GQE sits at the intersection of all of these:
- The **Hamiltonian** is the physics (like PINN's PDE residual)
- The **transformer** is the operator learner (like FNO/GalPT)
- The **UCCSD pool** encodes physical structure (like NeuralGCM's physics core)
- The **RL reward** is the physics-informed loss (like PINN's λ · PDE_residual)
- The **graph encoder** captures molecular structure (like MPNN/GNS)

The next frontier for your work could be:
- **Diffusion-based circuit generation** (inspired by GenCast): Generate diverse 
  circuits by sampling from a learned distribution, not maximizing a reward. This 
  would solve mode collapse by construction.
- **Neural operator for quantum Hamiltonians** (inspired by FNO): Learn a 
  resolution-invariant operator that maps molecular geometry → ground state energy, 
  bypassing the VQE loop entirely.
- **Hybrid physics-RL** (inspired by NeuralGCM): Use known quantum chemistry 
  (Hartree-Fock, MP2) as the "deterministic core" and RL as the "learned correction" 
  for correlation effects.

---

## Reference Materials You've Already Completed

- [UvA DL Course Notebooks](https://uvadlc-notebooks.readthedocs.io/en/latest/index.html) 
  — Covers transformers, GNNs, normalizing flows, energy-based models, and more
- [Physics-Based Deep Learning](https://www.physicsbaseddeeplearning.org/intro.html) 
  — Covers PINNs, differentiable physics, and surrogate models

These reading lists assume you've internalized both.

---

*Last updated: June 2026*
*Maintained for: Gyanateet Dutta (@Ryukijano)*
*Context: Physics-based ML, neural operators, AI for weather/climate, quantum ML*
