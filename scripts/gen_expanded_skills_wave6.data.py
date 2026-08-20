SKILLS = [
    {
        "name": "topological-data-analysis",
        "title": "Topological Data Analysis (TDA) for ML",
        "description": "Persistent homology, Ripser, GUDHI, Mapper, and topological deep learning for shape-aware scientific ML.",
        "devin_body": '''
## When to use

You want to extract robust, shape-driven features from complex, high-dimensional, or noisy scientific data.

## Key concepts

- **Persistent homology**: track birth/death of connected components, loops, voids across scales.
- **Persistence diagrams/barcodes**: compact topological descriptors.
- **Ripser/GUDHI**: fast C++ persistent homology libraries.
- **Mapper**: simplicial complex summarizing data shape.
- **Topological deep learning**: integrate persistence diagrams into neural networks.

## Code pattern

```python
import ripser
import gudhi

# Compute persistent homology with Ripser
diagrams = ripser.ripser(data, maxdim=2)['dgms']
```

## Tuning notes

- Choose distance metric carefully (Euclidean, Wasserstein, bottleneck).
- Subsample large datasets for Ripser.
- Vectorize persistence diagrams (e.g., persistence images, Betti curves) for ML.

## Verification

1. Compute persistence diagrams for a torus and a sphere and show they differ.
2. Use persistence images as features in a classifier.
3. Compare Mapper output to UMAP for a small dataset.
''',
        "references": [
            "https://ripser.scikit-tda.org/",
            "https://gudhi.inria.fr/",
            "https://www.jmlr.org/papers/volume22/20-325/20-325.pdf",
            "https://github.com/scikit-tda"
        ],
    },
    {
        "name": "differential-geometry-ml",
        "title": "Differential Geometry for ML",
        "description": "Riemannian manifolds, geodesics, natural gradients, hyperbolic ML, and optimization on curved spaces.",
        "devin_body": '''
## When to use

You are working with data or parameters that naturally live on curved spaces (spheres, manifolds, hierarchical graphs).

## Key concepts

- **Riemannian manifolds**: curved spaces with a metric.
- **Geodesics**: shortest paths on manifolds.
- **Natural gradient**: steepest descent with respect to Fisher metric.
- **Hyperbolic ML**: embed hierarchical data in hyperbolic space (Poincaré/Lorentz).
- **Stiefel/Grassmann**: optimization with orthogonality constraints.

## Code pattern

```python
import geoopt

# Hyperbolic manifold
manifold = geoopt.PoincareBall()
point = manifold.random(2, 3)
```

## Tuning notes

- Use manifold-aware optimizers (e.g., geoopt.RiemannianAdam).
- Hyperbolic space works well for tree-like/hierarchical data.
- Watch for numerical instabilities near the boundary of Poincaré ball.

## Verification

1. Embed a tree in Euclidean and hyperbolic space; compare distortion.
2. Train a classifier with hyperbolic embeddings.
3. Verify a Riemannian optimizer preserves constraints (e.g., orthogonality).
''',
        "references": [
            "https://geoopt.readthedocs.io/",
            "https://arxiv.org/pdf/2207.07287",
            "https://optml.mit.edu/papers/sra_hosseini_chapter.pdf",
            "https://arxiv.org/abs/2604.02969"
        ],
    },
    {
        "name": "information-geometry-ml",
        "title": "Information Geometry for ML",
        "description": "Fisher information metric, natural gradient, alpha-connections, and geometry of probability distributions.",
        "devin_body": '''
## When to use

You want to optimize or compare probability distributions in a geometrically meaningful way.

## Key concepts

- **Statistical manifold**: family of distributions parameterized by $\theta$.
- **Fisher information metric**: natural Riemannian metric on statistical manifolds.
- **Natural gradient**: $\tilde{\nabla} = G^{-1}\nabla$ where $G$ is Fisher information.
- **Alpha-connections**: Amari's dual connections; $\alpha=\\pm 1$ for e/m-flat manifolds.

## Code pattern

```python
import torch

# Natural gradient preconditioner (simplified)
F = compute_fisher_matrix(model, data)  # E[grad log p grad log p^T]
natural_grad = torch.linalg.solve(F + 1e-4*torch.eye(len(F)), grad)
```

## Tuning notes

- Fisher can be expensive; use Kronecker factored approximations (KFAC) or diagonal.
- Natural gradient is parameterization-invariant.
- Combine with trust-region methods for stability.

## Verification

1. Compare natural gradient vs Adam on a small logistic regression.
2. Compute Fisher information for a simple exponential family.
3. Show invariance under reparameterization of the natural gradient.
''',
        "references": [
            "https://en.wikipedia.org/wiki/Information_Geometry",
            "https://www.jmlr.org/papers/volume21/17-678/17-678.pdf",
            "https://link.springer.com/article/10.1007/s41884-025-00187-y",
            "https://en.wikipedia.org/wiki/Fisher_information_metric"
        ],
    },
    {
        "name": "random-matrix-theory-ml",
        "title": "Random Matrix Theory for ML",
        "description": "Marchenko-Pastur, semicircle law, free probability, and spectral analysis of neural networks.",
        "devin_body": '''
## When to use

You are analyzing the spectrum of large matrices (covariance, kernels, Hessians, NTKs) in ML.

## Key concepts

- **Marchenko-Pastur law**: limiting eigenvalue distribution of sample covariance matrices.
- **Semicircle law**: Wigner matrices.
- **Free probability**: non-commutative probability for large random matrices.
- **NTK spectrum**: random matrix approach to neural tangent kernel.

## Code pattern

```python
import numpy as np

# Sample covariance eigenvalues
X = np.random.randn(n, p) / np.sqrt(n)
S = X.T @ X
lam = np.linalg.eigvalsh(S)
```

## Tuning notes

- Compare empirical spectrum to theoretical predictions.
- Use Tracy-Widom laws for edge eigenvalues.
- Free probability helps analyze products/sums of random matrices.

## Verification

1. Generate a sample covariance matrix and compare histogram of eigenvalues to Marchenko-Pastur.
2. Compute NTK spectrum at init for a shallow network.
3. Use free probability to approximate eigenvalues of A+B.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2109.09304",
            "https://proceedings.neurips.cc/paper/2020/file/572201a4497b0b9f02d4f279b09ec30d-Paper.pdf",
            "https://projecteuclid.org/journals/annals-of-applied-probability/volume-28/issue-2/A-random-matrix-approach-to-neural-networks/10.1214/17-AAP1328.full",
            "https://arxiv.org/abs/2001.06188"
        ],
    },
    {
        "name": "high-dimensional-statistics",
        "title": "High-Dimensional Statistics for ML",
        "description": "Sparsity, LASSO, compressed sensing, concentration inequalities, and covariance estimation.",
        "devin_body": '''
## When to use

You have many features relative to samples and need structured estimation.

## Key concepts

- **LASSO**: $\\ell_1$-regularized regression for sparse coefficients.
- **Compressed sensing**: recover sparse signals from few measurements.
- **Concentration inequalities**: Hoeffding, Bernstein, matrix concentration.
- **Sparse covariance/precision**: graphical LASSO, inverse covariance estimation.

## Code pattern

```python
from sklearn.linear_model import Lasso
from sklearn.covariance import GraphicalLasso

lasso = Lasso(alpha=0.1).fit(X, y)
glasso = GraphicalLasso(alpha=0.1).fit(X)
```

## Tuning notes

- Cross-validate regularization strength.
- Check irrepresentable conditions for LASSO support recovery.
- Use knockoffs or stability selection for variable selection.

## Verification

1. Recover a sparse vector with LASSO and compare support.
2. Generate compressed sensing measurements and reconstruct a sparse signal.
3. Estimate a sparse inverse covariance and compare to true graph.
''',
        "references": [
            "https://www.cs.cmu.edu/~pradeepr/paperz/LogDet.pdf",
            "https://statistics.berkeley.edu/sites/default/files/tech-reports/709.pdf",
            "https://www.jmlr.org/papers/volume11/yuan10b/yuan10b.pdf",
            "https://www.stat.berkeley.edu/~bickel/Rothman%20et%20al%202007-spice.pdf"
        ],
    },
    {
        "name": "kernel-methods-science",
        "title": "Kernel Methods and RKHS for Scientific ML",
        "description": "RKHS, Gaussian processes, MMD, kernel mean embeddings, and kernel methods for PDEs.",
        "devin_body": '''
## When to use

You want nonlinear methods with strong theoretical guarantees, or kernel-based inference on distributions.

## Key concepts

- **RKHS**: reproducing kernel Hilbert space.
- **Kernel trick**: replace dot products with kernel evaluations.
- **Gaussian processes**: Bayesian kernel regression.
- **MMD**: maximum mean discrepancy for two-sample testing and generative modeling.
- **Kernel mean embedding**: represent distributions in RKHS.

## Code pattern

```python
import gpytorch
import torch

class GP(gpytorch.models.ExactGPModel):
    pass

likelihood = gpytorch.likelihoods.GaussianLikelihood()
model = GP(train_x, train_y, likelihood).cuda()
```

## Tuning notes

- Choose kernel to match prior assumptions (RBF, Matérn, polynomial).
- Kernel hyperparameters can be learned by maximizing marginal likelihood.
- MMD is sensitive to kernel choice; use mixture or learned kernels.

## Verification

1. Train a GP regression and check negative log-likelihood.
2. Run an MMD two-sample test on two distributions.
3. Use kernel mean embedding to estimate a distribution property.
''',
        "references": [
            "https://docs.gpytorch.ai/",
            "https://doi.org/10.1561/2200000060",
            "https://projecteuclid.org/journals/annals-of-statistics/volume-36/issue-3/Kernel-methods-in-machine-learning/10.1214/009053607000000677.pdf",
            "https://jmlr.csail.mit.edu/papers/v19/16-291.html"
        ],
    },
    {
        "name": "spectral-graph-ml",
        "title": "Spectral Methods and Graph Theory for ML",
        "description": "Graph Laplacian, spectral clustering, spectral GNNs, graph partitioning, and spectral sparsification.",
        "devin_body": '''
## When to use

You are analyzing graphs or networks and want to use spectral tools.

## Key concepts

- **Graph Laplacian**: $L = D - A$ and normalized variants.
- **Spectral clustering**: use eigenvectors of Laplacian for clustering.
- **Spectral GNNs**: filters in graph frequency domain.
- **Graph partitioning**: ratio cut, normalized cut, Cheeger cut.

## Code pattern

```python
import scipy.sparse as sp
import scipy.sparse.linalg as sla

L = sp.csgraph.laplacian(adj, normed=True)
eigvals, eigvecs = sla.eigsh(L, k=10, which='SM')
```

## Tuning notes

- Normalized Laplacian often better for irregular graphs.
- Spectral clustering works well when clusters are well-separated.
- Spectral GNNs are less common than spatial GNNs but have theoretical appeal.

## Verification

1. Compute Laplacian eigenvectors and use for spectral clustering.
2. Compare spectral clustering to k-means on a graph dataset.
3. Implement a simple spectral graph filter and verify signal smoothing.
''',
        "references": [
            "https://www.cs.yale.edu/homes/spielman/sagt/sagt.pdf",
            "https://arxiv.org/pdf/1608.04845",
            "https://proceedings.mlr.press/v162/wang22am.html",
            "https://link.springer.com/article/10.1007/s44163-024-00102-x"
        ],
    },
    {
        "name": "optimal-transport-ml",
        "title": "Optimal Transport for ML",
        "description": "Wasserstein distance, Sinkhorn algorithm, sliced Wasserstein, and applications to generative modeling and domain adaptation.",
        "devin_body": '''
## When to use

You need to compare or align probability distributions with geometry-aware metrics.

## Key concepts

- **Monge-Kantorovich**: optimal transport problem.
- **Wasserstein distance**: metric with cost grounded in sample space.
- **Entropic regularization**: Sinkhorn algorithm for fast approximate OT.
- **Sliced Wasserstein**: 1D projections for computational tractability.
- **Applications**: WGAN, domain adaptation, Bayesian inference.

## Code pattern

```python
import ot

# Wasserstein distance with Sinkhorn
M = ot.dist(x, y)
W = ot.sinkhorn2(a, b, M, reg=0.1)
```

## Tuning notes

- Sinkhorn regularization trades accuracy for speed; too small = slow, too large = blur.
- Sliced Wasserstein is cheaper but has different geometry.
- Use cost function matched to data (e.g., Euclidean for images).

## Verification

1. Compute Wasserstein distance between two 1D distributions and compare to closed form.
2. Train a WGAN or domain adaptation model with OT loss.
3. Compare Sinkhorn convergence for different regularization values.
''',
        "references": [
            "https://pythonot.github.io/",
            "http://cermics.enpc.fr/~jourdain/OT/polyOT.pdf",
            "https://math.columbia.edu/~mnutz/docs/EOT_lecture_notes.pdf",
            "https://arxiv.org/pdf/2311.05134"
        ],
    },
    {
        "name": "stochastic-processes-ml",
        "title": "Stochastic Processes and Neural SDEs for ML",
        "description": "Itô calculus, score-based generative models, neural SDEs, rough paths, and continuous-time generative modeling.",
        "devin_body": '''
## When to use

You are modeling continuous-time stochastic systems, time series, or score-based generative models.

## Key concepts

- **Itô calculus**: stochastic integrals with respect to Brownian motion.
- **Diffusion/SDE models**: forward noising and reverse-time SDE.
- **Neural SDEs**: learn drift/diffusion with neural networks.
- **Rough paths**: handle low-regularity stochastic processes.

## Code pattern

```python
import torchsde

sde = SDE(...)
y0 = torch.randn(batch, dim)
ys = torchsde.sdeint(sde, y0, ts)
```

## Tuning notes

- Use adaptive SDE solvers for stiff or multi-scale problems.
- Score matching can be replaced by flow matching for faster training.
- Neural CDEs/SDEs are good for irregular time series.

## Verification

1. Solve a simple SDE and compare moments to analytic solution.
2. Train a small diffusion/score model and sample.
3. Fit a neural SDE to a time series and compare to ODE baseline.
''',
        "references": [
            "https://github.com/google-research/torchsde",
            "https://proceedings.neurips.cc/paper_files/paper/2023/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf",
            "https://arxiv.org/abs/2106.10340",
            "https://proceedings.mlr.press/v139/kidger21b/kidger21b.pdf"
        ],
    },
    {
        "name": "optimization-under-uncertainty",
        "title": "Optimization Under Uncertainty",
        "description": "Robust optimization, stochastic programming, distributionally robust optimization, and Wasserstein DRO.",
        "devin_body": '''
## When to use

You need to make decisions that are robust to uncertainty, distribution shift, or rare events.

## Key concepts

- **Robust optimization**: optimize worst case over an uncertainty set.
- **Stochastic programming**: optimize expected value over known distribution.
- **DRO**: optimize over an ambiguity set of distributions.
- **Wasserstein DRO**: ambiguity set defined by Wasserstein ball.

## Code pattern

```python
import cvxpy as cp

# Robust linear program
x = cp.Variable(n)
objective = cp.Minimize(c @ x)
constraints = [A @ x <= b + delta]  # uncertainty in b
prob = cp.Problem(objective, constraints)
prob.solve()
```

## Tuning notes

- Robustness comes at cost (conservatism).
- DRO often reduces to regularization with small ambiguity sets.
- Use convex duality for tractable reformulations.

## Verification

1. Solve a robust LP and compare to nominal solution.
2. Implement Wasserstein DRO on a small regression problem.
3. Test robustness on perturbed test data.
''',
        "references": [
            "https://www.cvxpy.org/",
            "https://optimization-online.org/2021/04/8360/",
            "https://dl.acm.org/doi/10.1287/moor.2022.1275",
            "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5B4E65E3A5A2AEF24E218A6B34E6EAA2"
        ],
    },
    {
        "name": "game-theory-multiagent-ml",
        "title": "Game Theory and Multi-Agent Learning",
        "description": "Nash equilibria, mean-field games, mechanism design, and deep multi-agent reinforcement learning.",
        "devin_body": '''
## When to use

You are modeling strategic interactions among multiple agents or designing incentives.

## Key concepts

- **Nash equilibrium**: no agent can benefit by unilateral deviation.
- **Mean-field games**: approximate large N games with infinite-population limit.
- **Mechanism design**: design rules to achieve desired equilibria.
- **Multi-agent RL**: independent learners, opponent shaping, population-based training.

## Code pattern

```python
import nashpy as nash

A = [[3, 1], [0, 2]]
B = [[2, 1], [0, 3]]
game = nash.Game(A, B)
for eq in game.support_enumeration():
    print(eq)
```

## Tuning notes

- Equilibrium computation is hard; use approximations for large games.
- Mean-field games reduce complexity from O(N²) to O(N).
- Multi-agent training can be unstable; use curriculum or self-play.

## Verification

1. Compute Nash equilibria for a 2x2 matrix game.
2. Implement a mean-field game solver and compare to N-agent simulation.
3. Train two agents in a simple game and check convergence.
''',
        "references": [
            "https://nashpy.readthedocs.io/",
            "https://doi.org/10.48550/arxiv.2510.21442",
            "https://proceedings.mlr.press/v202/yardim23a.html",
            "https://jmlr.org/papers/v24/21-0505.html"
        ],
    },
    {
        "name": "category-theory-ml",
        "title": "Category Theory for ML",
        "description": "Functorial data modeling, categorical deep learning, structured cospans, string diagrams, and topos theory for ML.",
        "devin_body": '''
## When to use

You want compositional, modular, or mathematically rigorous foundations for ML architectures.

## Key concepts

- **Categories, functors, natural transformations**.
- **Functorial data modeling**: map between categories for data semantics.
- **Categorical deep learning**: architectures as functors, monads.
- **Structured cospans/string diagrams**: compositional neural circuits.
- **Topos theory**: internal logic, invariances.

## Code pattern

```python
# No standard library; use Catlab.jl (Julia) or implement small examples
# Example: category as objects + morphisms
class Category:
    def __init__(self, objects, morphisms):
        self.objects = objects
        self.morphisms = morphisms
```

## Tuning notes

- Category theory is more about design and understanding than direct implementation.
- Useful for neuro-symbolic AI and compositional generalization.
- Tools: Catlab.jl, DisCoPy (Python for string diagrams).

## Verification

1. Model a small domain as a category and check composition rules.
2. Use string diagrams to represent a neural circuit.
3. Verify a functor preserves composition.
''',
        "references": [
            "https://proceedings.mlr.press/v235/gavranovic24a.html",
            "https://arxiv.org/abs/2603.16123v1",
            "https://www.mdpi.com/2075-1680/14/3/204",
            "https://algebraicjulia.github.io/Catlab.jl/stable/"
        ],
    },
]
