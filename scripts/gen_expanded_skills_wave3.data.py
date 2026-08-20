SKILLS = [
    {
        "name": "scientific-linear-algebra-gpu",
        "title": "Scientific Linear Algebra on GPU",
        "description": "Dense and sparse linear algebra with cuBLAS, cuSOLVER, cuSPARSE, cuDSS, MAGMA, and device-side cuSolverDx.",
        "devin_body": '''
## When to use

You need to solve linear systems, factorize matrices, compute eigenvalues, or perform sparse matrix operations on GPU.

## Key concepts

- **cuBLAS**: GPU BLAS (Level 1/2/3) with Tensor Core paths.
- **cuSOLVER**: dense and sparse direct solvers, eigenvalue solvers. `cusolverDn` for dense, `cusolverRF` for refactorization.
- **cuDSS**: new direct sparse solver (replaces `cusolverSP`).
- **cuSPARSE**: SpMV, SpMM, sparse triangular solve, preconditioners.
- **MAGMA**: heterogeneous CPU+GPU LAPACK/ScaLAPACK routines.
- **cuSolverDx**: device-side factorizations for kernel fusion.

## Code pattern

```python
import cupy as cp

A = cp.random.randn(4096, 4096, dtype=cp.float64)
b = cp.random.randn(4096, dtype=cp.float64)
x = cp.linalg.solve(A, b)
```

For PyTorch:

```python
import torch
A = torch.randn(4096, 4096, device='cuda', dtype=torch.float64)
L, pivots = torch.linalg.lu_factor(A)
```

## Tuning notes

- cuBLAS uses Tensor Cores for FP32 (TF32) on Ampere+ and FP16/BF16.
- Large dense systems (>8K) often benefit from MAGMA's two-stage solvers.
- Sparse direct solvers (cuDSS, cuSolverRF) are best for many right-hand sides or refactorization.

## Verification

1. Solve a known linear system and check residual `||Ax - b||`.
2. Compare cuBLAS GEMM to PyTorch `torch.mm` and confirm speedup.
3. Check MAGMA installation with `python -m pip show magma-cuda` or a C test.
''',
        "references": [
            "https://docs.nvidia.com/cuda/cublas/",
            "https://docs.nvidia.com/cuda/cusolver/",
            "https://docs.nvidia.com/cuda/cudss/",
            "https://developer.nvidia.com/magma"
        ],
    },
    {
        "name": "optimization-gpu",
        "title": "Optimization for Scientific ML on GPU",
        "description": "First- and second-order optimization, Optax/JAXopt, L-BFGS, trust-region, constrained, and Newton-Krylov methods on GPU.",
        "devin_body": '''
## When to use

You are training or solving an optimization problem on GPU and need to go beyond Adam/SGD.

## Key concepts

- **First-order**: SGD, AdamW, schedule-free (AdamW with no learning-rate schedule), Lion, Muon.
- **Second-order**: L-BFGS, Newton-CG, trust-region, Hessian-free methods.
- **JAX**: `optax` for stochastic, `jaxopt` for deterministic/constrained, `optimistix` for root finding.
- **PyTorch**: `pytorch-minimize`, `PyTorch-LBFGS`, `torch.optim.LBFGS`.
- **Newton-Krylov**: `scipy.optimize.newton_krylov` or Hessian-vector products in JAX/PyTorch.

## Code pattern

```python
import jax
import jax.numpy as jnp
import optax

optimizer = optax.adamw(1e-3)
params = model.init(...)
opt_state = optimizer.init(params)

@jax.jit
def train_step(params, opt_state, x, y):
    loss, grads = jax.value_and_grad(loss_fn)(params, x, y)
    updates, opt_state = optimizer.update(grads, opt_state, params)
    params = optax.apply_updates(params, updates)
    return params, opt_state, loss
```

## Tuning notes

- Second-order methods can converge in fewer steps but are expensive per step; use for small/medium deterministic problems.
- Use `jaxopt.ScipyBoundedMinimize` for constrained problems.
- For large neural nets, keep first-order; second-order is rarely worth it.

## Verification

1. Solve a small nonlinear least-squares with L-BFGS and compare to `scipy.optimize.minimize`.
2. Verify `jaxopt.GradientDescent` converges on a quadratic.
3. Check that GPU is used (e.g., `nvidia-smi` shows compute activity).
''',
        "references": [
            "https://optax.readthedocs.io/en/stable/",
            "https://jaxopt.github.io/stable/",
            "https://github.com/patrick-kidger/optimistix",
            "https://github.com/rfeinman/pytorch-minimize"
        ],
    },
    {
        "name": "bayesian-inference-gpu",
        "title": "Bayesian Inference and Gaussian Processes on GPU",
        "description": "MCMC, NUTS, variational inference, NumPyro, BlackJAX, and GPyTorch on NVIDIA GPUs.",
        "devin_body": '''
## When to use

You need uncertainty estimates, posterior sampling, or Bayesian model calibration on GPU.

## Key concepts

- **MCMC**: HMC, NUTS, MALA, Langevin. Use `numpyro` or `blackjax` for JIT-compiled samplers.
- **VI**: ADVI, mean-field, pathfinder. Faster but approximate.
- **Gaussian Processes**: MVM-based inference (BBMM) in `gpytorch`; avoids Cholesky O(N³).
- **GPU**: JAX/PyTorch back ends compile log-prob and kernels to CUDA.

## Code pattern

```python
import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS

def model(x, y):
    alpha = numpyro.sample("alpha", dist.Normal(0, 10))
    beta = numpyro.sample("beta", dist.Normal(0, 1))
    numpyro.sample("obs", dist.Normal(alpha + beta * x, 0.1), obs=y)

mcmc = MCMC(NUTS(model), num_warmup=500, num_samples=1000)
mcmc.run(jax.random.PRNGKey(0), x, y)
```

For GPyTorch:

```python
import gpytorch
model = ExactGPModel(train_x, train_y, likelihood)
model = model.cuda()
model.train(); likelihood.train()
```

## Tuning notes

- NUTS needs gradients; JAX is ideal.
- For large GPs, use variational sparse approximations or SKI/KISS-GP.
- Set `numpyro.set_host_device_count(n)` for CPU parallelism; on GPU, one chain per GPU is typical.

## Verification

1. Run NUTS on a simple Bayesian linear regression and compare posterior means to analytic solution.
2. Train a small GPyTorch GP and check predictive log-likelihood.
3. Verify `jax.devices()` shows the GPU and the kernel is running there.
''',
        "references": [
            "https://pyro.ai/numpyro/",
            "https://blackjax-devs.github.io/blackjax/",
            "https://docs.gpytorch.ai/",
            "https://github.com/patrick-kidger/diffrax"
        ],
    },
    {
        "name": "differential-equations-gpu",
        "title": "Differential Equations on GPU",
        "description": "ODE/PDE/SDE solvers, spectral and finite element methods, Diffrax, FEniCSx, PETSc, and NekRS on GPU.",
        "devin_body": '''
## When to use

You are solving ODEs, PDEs, or SDEs in scientific ML on GPU.

## Key concepts

- **ODE/SDE solvers**: Diffrax (JAX), `torchdiffeq`, `torchsde`.
- **Finite element**: FEniCSx with `cuDOLFINx` plugin for GPU assembly.
- **PETSc**: GPU back end (`AIJCUSPARSE`, `MATAIJKOKKOS`) for sparse solvers.
- **Spectral element**: NekRS, JAX-Fluids, PhiFlow.
- **Neural differential equations**: solve ODEs inside a neural network with `jax.experimental.ode` or Diffrax.

## Code pattern

```python
import jax
import jax.numpy as jnp
from diffrax import diffeqsolve, Dopri5, ODETerm, SaveAt

term = ODETerm(lambda t, y, args: -y)
sol = diffeqsolve(term, Dopri5(), t0=0, t1=1, dt0=0.1, y0=1.0, saveat=SaveAt(ts=jnp.linspace(0, 1, 10)))
```

## Tuning notes

- Use adaptive step-size controllers (PID) for stiff or multi-scale problems.
- FEniCSx/PETSc multi-GPU scaling requires MPI and matching CUDA-aware MPI.
- Spectral methods (NekRS) can scale to thousands of GPUs but need good meshes.

## Verification

1. Solve a linear ODE with known analytic solution; check RMSE.
2. Run FEniCSx Poisson on GPU and compare to CPU result.
3. Benchmark Diffrax `Tsit5` vs `scipy.integrate.solve_ivp`.
''',
        "references": [
            "https://docs.kidger.site/diffrax/",
            "https://fenicsproject.org/",
            "https://petsc.org/release/overview/gpu_roadmap/",
            "https://github.com/tumaer/jaxfluids"
        ],
    },
    {
        "name": "signal-image-processing-gpu",
        "title": "Signal and Image Processing on GPU",
        "description": "FFT, wavelets, filtering, compressed sensing, and tomography with cuFFT, RAPIDS, and GPU pipelines.",
        "devin_body": '''
## When to use

You are processing large 1D/2D/3D signals or images on GPU.

## Key concepts

- **cuFFT**: 1D/2D/3D FFT, batched, multi-GPU up to 16 GPUs.
- **cuFFT callbacks**: pre/post-process inside FFT for DSP pipelines.
- **Wavelets**: PyWavelets, `cupy` wrapper, or custom CUDA.
- **Compressed sensing**: TV-regularized reconstruction, SART, filtered back-projection.
- **GPU image stacks**: RAPIDS cuCIM, `cupy`, `dask-cuda`.

## Code pattern

```python
import cupy as cp

x = cp.random.randn(1024, 1024, dtype=cp.float32)
X = cp.fft.fft2(x)
```

For tomography:

```python
# ASTRA or TomoPy on GPU
import astra
proj_id = astra.create_projector('cuda', ...)
```

## Tuning notes

- Batch FFTs for better occupancy; use `cufftXt` for multi-GPU 3D FFTs.
- Compressed-sensing reconstructions often use `cupy.linalg` for TV proximal steps.
- Use `float32` for speed; `float64` for accuracy-critical inverse problems.

## Verification

1. Compare `cupy.fft.fft2` to NumPy `np.fft.fft2` and confirm accuracy/speed.
2. Run a filtered back-projection on a test sinogram and compare to ground truth.
3. Profile with Nsight Systems to separate I/O from compute.
''',
        "references": [
            "https://docs.nvidia.com/cuda/cufft/",
            "https://cupy.dev/",
            "https://rapids.ai/",
            "https://doi.org/10.1364/ao.378466"
        ],
    },
    {
        "name": "equivariant-neural-networks-science",
        "title": "Equivariant Neural Networks for Science",
        "description": "E(3)/SE(3)-equivariant networks (E3NN, Equiformer, MACE, NequIP, steerable CNNs) for atomic and molecular systems.",
        "devin_body": '''
## When to use

You are building models for molecules, materials, point clouds, or 3D data where physical symmetries should be preserved.

## Key concepts

- **E(3) equivariance**: rotations, translations, reflections. Models built with irreducible representations (irreps).
- **E3NN**: PyTorch library for equivariant neural networks.
- **Equiformer/EquiformerV2**: transformer with equivariant attention.
- **NequIP/MACE/Allegro**: equivariant GNNs for interatomic potentials.
- **Steerable CNNs**: SO(2)/SO(3) steerable convolutions.

## Code pattern

```python
import e3nn
from e3nn import o3, nn

irreps = o3.Irreps("1x0e + 1x1o")
model = nn.Gate(...)
```

For MACE/NequIP, use the respective packages directly.

## Tuning notes

- Equivariant models are data-efficient but can be slower to train.
- Use `cuEquivariance` for fast tensor products on GPU.
- Match the symmetry group to the problem (E(3) for molecules, SE(2) for images).

## Verification

1. Train a small E3NN model and verify it is equivariant: `f(Rx) ≈ Rf(x)`.
2. Run a MACE training and compare forces/energies to a reference.
3. Check `cuEquivariance` is installed and active for 3×+ speedup.
''',
        "references": [
            "https://e3nn.org/",
            "https://github.com/atomicarchitects/equiformer_v3",
            "https://github.com/ACEsuit/mace",
            "https://developer.nvidia.com/cuequivariance"
        ],
    },
    {
        "name": "gnn-science",
        "title": "Graph Neural Networks for Science",
        "description": "GNNs for molecules, materials, weather, neural operators, and large-scale graph training on GPU.",
        "devin_body": '''
## When to use

You are working with graph-structured scientific data: molecules, crystals, meshes, point clouds, or spatiotemporal grids.

## Key concepts

- **Message passing**: MPNN, GCN, GAT, SchNet, DimeNet, GemNet.
- **GraphCast**: mesh-based GNN for global weather forecasting.
- **GNNs for MD**: MACE, NequIP, Allegro, GemNet-OC.
- **Large-scale training**: PyTorch Geometric, DGL, GraphStorm, whole-graph training.
- **Heterogeneous graphs**: different node/edge types (e.g., spatial transcriptomics, knowledge graphs).

## Code pattern

```python
import torch_geometric
from torch_geometric.nn import GCNConv

class GCN(torch.nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv1 = GCNConv(in_channels, 64)
        self.conv2 = GCNConv(64, out_channels)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index).relu()
        return self.conv2(x, edge_index)
```

## Tuning notes

- Use `edge_index` (COO) for small graphs; `SparseTensor` or DGL for large graphs.
- Add self-loops and normalize adjacency.
- For equivariant molecular graphs, prefer equivariant GNNs over plain GCN.

## Verification

1. Train GCN on QM9 for a property and check MAE.
2. Run a GraphCast inference on a single time step and compare to IFS.
3. Benchmark PyG vs DGL on a large graph.
''',
        "references": [
            "https://pytorch-geometric.readthedocs.io/",
            "https://www.dgl.ai/",
            "https://github.com/google-deepmind/graphcast",
            "https://www.nature.com/articles/s41467-022-29939-5"
        ],
    },
    {
        "name": "transformers-for-science",
        "title": "Transformers and Foundation Models for Science",
        "description": "Transformers for protein, genomics, weather, chemistry, math, and symbolic regression; ESM, AlphaFold, Prithvi, DNABERT, AI-Descartes.",
        "devin_body": '''
## When to use

You want to apply large transformer-based foundation models to scientific data or use transformers for symbolic and mathematical discovery.

## Key concepts

- **Protein**: ESM-2, ESMFold, AlphaFold, Boltz.
- **Genomics**: DNABERT/DNABERT-2, Enformer, Nucleotide Transformer.
- **Weather/climate**: Prithvi, ClimaX, FourCastNet, GraphCast.
- **Chemistry**: ChemBERTa, MolFormer, GPT for chemistry.
- **Math/symbolic**: LLM-SR, AI-Descartes, formal provers (Lean, Isabelle).

## Code pattern

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("facebook/esm2_t33_650M_UR50D")
model = AutoModel.from_pretrained("facebook/esm2_t33_650M_UR50D").to("cuda")
inputs = tokenizer("MKTAYIAKQRQISFVK", return_tensors="pt").to("cuda")
outputs = model(**inputs)
```

## Tuning notes

- Use FlashAttention for long sequences (genomics, weather).
- Fine-tune with LoRA/QLoRA for limited data.
- For symbolic regression, combine LLM-generated hypotheses with constrained fitting.

## Verification

1. Extract ESM-2 embeddings and train a small head for a protein task.
2. Fine-tune DNABERT-2 on a GUE benchmark and compare to baseline.
3. Use AI-Descartes/LLM-SR to rediscover a known physical law from data.
''',
        "references": [
            "https://github.com/facebookresearch/esm",
            "https://github.com/magics-lab/dnabert_2",
            "https://huggingface.co/ibm-nasa-geospatial",
            "https://www.nature.com/articles/s41467-023-37236-y"
        ],
    },
    {
        "name": "generative-models-science",
        "title": "Generative Models for Scientific Discovery",
        "description": "Diffusion, flow matching, score-based models, and normalizing flows for molecules, materials, and inverse design.",
        "devin_body": '''
## When to use

You are generating molecules, materials, structures, or trajectories with diffusion/flow models.

## Key concepts

- **Diffusion models**: DDPM, score-based, EDM, MOFDiff, CDVAE.
- **Flow matching**: FlowMol, FlowER, Rectified Flow; deterministic ODEs, faster sampling.
- **Normalizing flows**: for continuous molecular/crystal generation.
- **Inverse design**: generate candidates with target properties.
- **Evaluation**: validity, uniqueness, novelty, property distribution matching.

## Code pattern

```python
import torch

# Diffusion model training loop
noise = torch.randn_like(x)
t = torch.rand(x.size(0), device='cuda')
noisy = alpha_t * x + sigma_t * noise
pred = model(noisy, t)
loss = F.mse_loss(pred, noise)
```

For flow matching:

```python
# Interpolate x0 (noise) and x1 (data)
t = torch.rand(b, 1, device='cuda')
xt = (1 - t) * x0 + t * x1
# velocity field v_t(x)
loss = F.mse_loss(model(xt, t), x1 - x0)
```

## Tuning notes

- Flow matching often trains more stably than diffusion and has fewer hyperparameters.
- E(3) equivariant diffusion for molecules preserves physical symmetries.
- For crystals, use periodic E(3)-equivariant flows (DiffCSP).

## Verification

1. Train a small diffusion/flow model and sample 1000 candidates.
2. Compute validity/uniqueness/novelty metrics.
3. Relax generated structures with a surrogate (MACE, CHGNet) and check stability.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2404.19739",
            "https://github.com/jiaor17/DiffCSP",
            "https://github.com/microsoft/mattergen",
            "https://www.nature.com/articles/s43588-025-00924-4"
        ],
    },
    {
        "name": "reinforcement-learning-science",
        "title": "Reinforcement Learning for Scientific Control",
        "description": "RL for tokamak plasma control, drug design, experiment design, and autonomous scientific systems.",
        "devin_body": '''
## When to use

You are using RL to control a scientific system or optimize a design process.

## Key concepts

- **Algorithms**: PPO, SAC, DQN, model-based RL, offline RL.
- **Plasma control**: real-time tokamak shape/position tracking with deep RL at kHz rates.
- **Drug design**: ReLeaSE, AlphaDrug, ClickGen — RL agents in chemical space.
- **Experiment design**: RL for automated lab protocols.
- **Sim-to-real**: domain randomization, privileged information, simulators like NSFsim.

## Code pattern

```python
import torch
import gymnasium as gym

# Stable-Baselines3 PPO on a custom env
from stable_baselines3 import PPO
env = gym.make("Pendulum-v1")
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100000)
```

For scientific envs, define state (observations), action, reward, and simulator.

## Tuning notes

- Sample efficiency matters; use model-based or offline RL for expensive simulators.
- Reward shaping should encode domain knowledge.
- Plasma control needs 4 kHz inference; use a small MLP/CNN and TensorRT.

## Verification

1. Train PPO on a toy control task and confirm policy converges.
2. Test in simulator before real hardware.
3. Measure inference latency on target deployment hardware.
''',
        "references": [
            "https://www.nature.com/articles/s41586-021-04301-9",
            "https://www.science.org/doi/10.1126/sciadv.aap7885",
            "https://github.com/DLR-RM/stable-baselines3",
            "https://doi.org/10.1088/1741-4326/ae34c6"
        ],
    },
    {
        "name": "causal-inference-science",
        "title": "Causal Inference and Discovery for Science",
        "description": "Do-calculus, causal discovery, structural causal models, transportability, and mediation for observational and experimental data.",
        "devin_body": '''
## When to use

You want to go beyond correlation and identify causal effects in scientific data.

## Key concepts

- **Causal graphs**: DAGs, d-separation, back-door criterion.
- **Do-calculus**: rules for identifying causal effects from observational data.
- **Causal discovery**: PC, FCI, GES, NOTEARS, DAG-GNN.
- **Transportability**: transfer causal findings across settings.
- **Mediation analysis**: direct/indirect effects.

## Code pattern

```python
import dowhy
from dowhy import CausalModel

model = CausalModel(
    data=df,
    treatment='treatment',
    outcome='outcome',
    common_causes=['age', 'sex']
)
identified = model.identify_effect()
estimate = model.estimate_effect(identified, method_name='backdoor.linear_regression')
```

For causal discovery:

```python
from g castle import PC
pc = PC()
pred_dag = pc.fit(data).adjacency_matrix_
```

## Tuning notes

- Strong causal claims need domain knowledge and/or randomized experiments.
- Use sensitivity analysis (e.g., DoWhy refute) to test robustness.
- High-dimensional causal discovery can be unstable; validate with domain experts.

## Verification

1. Recover a known DAG from synthetic data with PC/NOTEARS.
2. Estimate an ATE on a dataset with a known ground-truth intervention.
3. Run DoWhy refutation tests and report placebo/random-common-cause outcomes.
''',
        "references": [
            "https://www.pywhy.org/dowhy/",
            "https://causalml.org/",
            "https://ftp.cs.ucla.edu/pub/stat_ser/r402.pdf",
            "https://doi.org/10.1007/s41060-016-0038-6"
        ],
    },
    {
        "name": "uncertainty-quantification-science",
        "title": "Uncertainty Quantification in Scientific ML",
        "description": "Conformal prediction, evidential learning, Bayesian neural nets, ensembles, Fortuna, and UQ for PDE surrogates.",
        "devin_body": '''
## When to use

You need calibrated uncertainty for safety-critical scientific predictions.

## Key concepts

- **Ensembles**: deep ensembles for epistemic uncertainty.
- **MC dropout**: cheap approximate Bayesian inference.
- **Conformal prediction**: coverage guarantees for prediction sets.
- **Evidential deep learning**: model uncertainty as evidence distributions.
- **Fortuna**: scalable UQ library built on Flax/JAX.

## Code pattern

```python
from fortuna import ProbRegressor
import jax

prob_model = ProbRegressor()
status = prob_model.train(train_data_loader, ...)
means = prob_model.predictive.mean(inputs)
```

Conformal:

```python
from nonconformist import IcpRegressor
icp = IcpRegressor(model)
icp.calibrate(calibration_x, calibration_y)
prediction_sets = icp.predict(test_x, significance=0.1)
```

## Tuning notes

- Conformal prediction requires exchangeable data; adapt for time-series/distribution shift.
- Evidential learning needs careful priors to avoid overconfident predictions.
- Ensembles scale linearly in compute but are easy to implement.

## Verification

1. Train an ensemble and measure calibration error (ECE).
2. Apply conformal prediction and verify marginal coverage on held-out data.
3. Test uncertainty on OOD inputs; uncertainty should increase.
''',
        "references": [
            "https://fortuna.readthedocs.io/",
            "https://arxiv.org/pdf/1806.01768",
            "https://iopscience.iop.org/article/10.1088/2632-2153/ae2e7b",
            "https://proceedings.mlr.press/v267/gopakumar25a.html"
        ],
    },
    {
        "name": "astrophysics-cosmology-ml",
        "title": "Astrophysics and Cosmology ML on GPU",
        "description": "Gravitational lensing, galaxy classification, N-body simulations, dark matter mapping, and cosmological parameter inference.",
        "devin_body": '''
## When to use

You are applying ML to astrophysics or cosmology problems, especially with survey data or N-body simulations.

## Key concepts

- **Gravitational lensing**: GIGA-Lens, TinyLensGPU, GLaD for lens modeling.
- **N-body simulations**: GADGET-4, Shenqi, BlueTides, ASTRID.
- **Galaxy classification**: CNNs, vision transformers on DESI/Euclid/LSST images.
- **Cosmological inference**: emulator-based, simulation-based inference (SBI), neural density estimators.
- **GPU**: JAX/TensorFlow for lens modeling; CUDA for tree-walk gravity.

## Code pattern

```python
import jax
import jax.numpy as jnp

# JAX-based lens model
# TinyLensGPU / GIGA-Lens use NumPyro/TensorFlow for posterior sampling
```

For N-body:

```bash
# Run GADGET-4 or Shenqi with MPI+CUDA
mpirun -np 8 ./Shenqi param.txt
```

## Tuning notes

- Survey images can be large; use data augmentations and TFRecord/WebDataset.
- N-body codes need excellent MPI-GPU load balancing.
- Use simulation-based inference for expensive forward models.

## Verification

1. Classify 1000 galaxy images and compare accuracy to published baselines.
2. Run a small N-body box and check halo mass function against a reference.
3. Recover a lens parameter with MCMC and compare to known truth.
''',
        "references": [
            "https://iopscience.iop.org/article/10.3847/1538-4357/ac6de4",
            "https://github.com/caoxiaoyue/TinyLensGpu",
            "https://github.com/MP-Gadget/shenqi",
            "https://arxiv.org/abs/2606.17145"
        ],
    },
    {
        "name": "fluid-dynamics-cfd-ml",
        "title": "Fluid Dynamics and CFD ML on GPU",
        "description": "Neural operators, PhysicsNeMo (Modulus), JAX-Fluids, PhiFlow, and surrogate CFD on GPU.",
        "devin_body": '''
## When to use

You want to build surrogate models for fluid dynamics or accelerate CFD with ML and GPUs.

## Key concepts

- **Neural operators**: FNO, DeepONet, GraphCast, L-ESHyRA.
- **Differentiable CFD**: JAX-Fluids, PhiFlow, PhysicsNeMo (Modulus).
- **Turbulence modeling**: LES, RANS closures, PINNs for turbulence.
- **Surrogate CFD**: train on simulation data, deploy for fast inference.
- **Datasets**: Darcy flow, 2D turbulence, DrivAerML, ERA5.

## Code pattern

```python
import jaxfluids

# JAX-Fluids fully-differentiable compressible Navier-Stokes
```

For FNO:

```python
from neuralop.models import FNO

fno = FNO(n_modes=(16, 16), hidden_channels=64, in_channels=1, out_channels=1)
fno = fno.to('cuda')
```

## Tuning notes

- FNO works best on regular grids; use GNNs or point-cloud methods for unstructured meshes.
- Physics-informed loss can improve generalization but increases training cost.
- For production, deploy with TensorRT/TorchScript for low-latency inference.

## Verification

1. Train FNO on 2D Navier-Stokes and compare to reference solver at test time.
2. Run a JAX-Fluids simulation and verify conservation properties.
3. Profile surrogate vs CFD wall time for the same geometry.
''',
        "references": [
            "https://github.com/tumaer/jaxfluids",
            "https://tum-pbs.github.io/PhiFlow/",
            "https://developer.nvidia.com/PhysicsNeMo",
            "https://github.com/neuraloperator/neuraloperator"
        ],
    },
    {
        "name": "quantum-chemistry-gpu",
        "title": "Quantum Chemistry and Quantum ML on GPU",
        "description": "GPU-accelerated DFT, Hartree-Fock, coupled cluster with PySCF/GPU4PySCF, and hybrid quantum-classical ML.",
        "devin_body": '''
## When to use

You are running electronic structure calculations or hybrid quantum-classical ML on GPU.

## Key concepts

- **GPU4PySCF**: CUDA plugin for PySCF; 1000× speedup on A100 for DFT with density fitting.
- **Methods**: SCF, DFT, MP2, CCSD, geometry optimization, frequency analysis.
- **Quantum ML**: VQE, QAOA, quantum kernels, PennyLane, Qiskit.
- **Datasets**: QM9, MD17, GMTKN55, Materials Project.
- **Hybrid**: PySCF active space + Qiskit Nature VQE.

## Code pattern

```python
from gpu4pyscf.scf import RHF

mol = pyscf.M(atom='H 0 0 0; H 0 0 0.74', basis='def2-tzvp')
mf = RHF(mol)
mf.kernel()
```

Quantum ML:

```python
import pennylane as qml
dev = qml.device("default.qubit", wires=2)
@qml.qnode(dev, interface="torch")
def circuit(params):
    qml.RX(params[0], wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(1))
```

## Tuning notes

- Use density fitting for large systems to reduce ERI cost.
- GPU4PySCF supports SCF/DFT and some post-HF; coupled cluster may still be CPU.
- Quantum ML on classical simulators is limited to <50 qubits without tensor network tricks.

## Verification

1. Run a DFT single point and compare energy to CPU PySCF.
2. Optimize a small molecule and compare bond lengths to experimental data.
3. Run a small VQE on H2 and compare exact ground-state energy.
''',
        "references": [
            "https://pyscf.org/user/gpu.html",
            "https://pennylane.ai/",
            "https://qiskit.org/ecosystem/nature/",
            "https://doi.org/10.48550/arxiv.2602.02234"
        ],
    },
    {
        "name": "neuroscience-ml-gpu",
        "title": "Neuroscience and Brain ML on GPU",
        "description": "fMRI, calcium imaging, connectomics, and neural decoding with cuBNM, DeepWonder, scGPT, and RAPIDS.",
        "devin_body": '''
## When to use

You are analyzing large-scale neural data (imaging, electrophysiology, connectomics) on GPU.

## Key concepts

- **Connectome modeling**: cuBNM for whole-brain network models (Wong-Wang, Jansen-Rit).
- **Calcium imaging**: DeepWonder, DeepCAD-RT, CAPT for denoising and neuron extraction.
- **fMRI/MEG/EEG**: PAGANI, NeuralSet, resting-state analysis.
- **Single-cell**: scVI/scGPT for transcriptomics, RAPIDS cuDF.
- **Neural decoding**: population dynamics, latent variable models.

## Code pattern

```python
# cuBNM example (Python wrapper)
from cubnm import simulations
sim = simulations.Sim(...)
sim.run()
```

For calcium imaging:

```python
# DeepWonder / DeepCAD-RT are deep models run in PyTorch
```

## Tuning notes

- Large imaging datasets need efficient video loading (e.g., Zarr/FFMPEG + dask).
- Connectome models can be highly parallel; use one GPU per subject or model instance.
- Calcium signals are noisy; use self-supervised or synthetic pretraining.

## Verification

1. Run cuBNM on a small connectome and reproduce known BOLD dynamics.
2. Extract neurons from a short calcium video and compare to manual labels.
3. Train scVI on 100k cells and compare latent space to CPU run.
''',
        "references": [
            "https://github.com/amnsbr/cubnm",
            "https://www.nature.com/articles/s41592-023-01838-7",
            "https://github.com/bowang-lab/scGPT",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC6866286/"
        ],
    },
    {
        "name": "scientific-workflows-hpc",
        "title": "Reproducible Scientific Workflows on HPC",
        "description": "Workflow engines (Snakemake, Nextflow, CWL), containers, DVC, SLURM job arrays, checkpointing, and cloud HPC.",
        "devin_body": '''
## When to use

You are running multi-step scientific pipelines on a cluster and need reproducibility, scaling, and fault tolerance.

## Key concepts

- **Workflow engines**: Snakemake (Pythonic, file-based), Nextflow (dataflow, portable), CWL/WDL (standardized).
- **Containers**: Docker for dev, Singularity/Apptainer for HPC (no root needed).
- **Reproducibility**: `conda-lock`, `pip-tools`, DVC for data/models.
- **HPC**: SLURM/PBS job arrays, `--dependency`, checkpointing, `$SCRATCH` vs permanent storage.
- **Cloud HPC**: AWS ParallelCluster, Azure Batch, GCP Slurm, cloud bursting.

## Code pattern

```python
# Snakemake rule
rule train:
    input:
        "data/train.csv"
    output:
        "models/model.pt"
    shell:
        "python train.py --input {input} --output {output}"
```

SLURM:

```bash
#SBATCH --array=1-10%1
#SBATCH --gpus=1
python train.py --seed $SLURM_ARRAY_TASK_ID
```

## Tuning notes

- Job arrays are ideal for embarrassingly parallel sweeps; limit concurrency with `%N`.
- Checkpoint model + optimizer + RNG state for long jobs.
- Store checkpoints in `$SCRATCH`, copy final artifacts to permanent storage.

## Verification

1. Run a Snakemake/Nextflow pipeline end-to-end with `--dry-run` first.
2. Verify a container reproduces results across two hosts.
3. Resume a job from a checkpoint and confirm identical loss curve.
''',
        "references": [
            "https://snakemake.readthedocs.io/",
            "https://www.nextflow.io/",
            "https://dvc.org/doc",
            "https://docs.mila.quebec/examples/good_practices/checkpointing/"
        ],
    },
    {
        "name": "experiment-tracking-optimization",
        "title": "Experiment Tracking and Hyperparameter Optimization",
        "description": "W&B, MLflow, Neptune, Aim, Optuna, Ray Tune, and reproducible hyperparameter search on HPC.",
        "devin_body": '''
## When to use

You need to track experiments, compare runs, and search hyperparameters for scientific ML.

## Key concepts

- **Experiment tracking**: W&B, MLflow, Neptune, TensorBoard, Aim.
- **HPO**: Optuna, Ray Tune, Ax, W&B Sweeps, Hyperband/ASHA.
- **Reproducibility**: log hyperparameters, code commit, data version, random seeds, environment.
- **Distributed search**: Ray Tune across a SLURM cluster; Optuna with RDB storage.

## Code pattern

```python
import wandb
import optuna

def objective(trial):
    lr = trial.suggest_float("lr", 1e-5, 1e-1, log=True)
    # train and return validation metric
    return val_loss

study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=100)
```

W&B:

```python
wandb.init(project="science-ml", config={"lr": 1e-3})
wandb.log({"loss": loss})
```

## Tuning notes

- W&B has the best UI but is SaaS; MLflow/Aim are self-hosted.
- Optuna is lightweight; Ray Tune is best for large distributed sweeps.
- Use ASHA/Hyperband early stopping to cut compute.

## Verification

1. Log 10 training runs and compare them in the tracking UI.
2. Run an Optuna search and verify the best trial improves over random search.
3. Re-run the best config with a different seed and check variance.
''',
        "references": [
            "https://docs.wandb.ai/",
            "https://mlflow.org/",
            "https://optuna.readthedocs.io/",
            "https://docs.ray.io/en/latest/tune/index.html"
        ],
    },
]
