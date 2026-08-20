SKILLS = [
    {
        "name": "self-supervised-learning",
        "title": "Self-Supervised Learning (SSL)",
        "description": "Pretext tasks, contrastive and non-contrastive SSL, masked prediction, and unsupervised representation learning for vision, language, and graphs.",
        "devin_body": r'''
## When to use

You have large amounts of unlabeled data and limited labels, or you want a pretrained representation that transfers well to downstream tasks.

## Key concepts

- **Pretext tasks**: predict rotation, solve jigsaw puzzles, inpaint, or forecast masked inputs to generate supervision.
- **Contrastive SSL**: SimCLR, MoCo, BYOL, DINO learn by pulling positive views together and pushing negatives apart.
- **Non-contrastive SSL**: VICReg, Barlow Twins, Bootstrap Your Own Latent (BYOL) avoid explicit negative pairs.
- **Masked modeling**: BERT-style token masking, MAE for vision, or data2vec for multimodal data.
- **Transfer learning**: pretrain on unlabeled data, then add a small head and finetune.

## Code pattern

```python
import torch, torchvision
from lightly.loss import NTXentLoss
from lightly.models.modules import SimCLRProjectionHead
from lightly.transforms.simclr_transform import SimCLRTransform

backbone = torchvision.models.resnet18(weights=None)
backbone.fc = torch.nn.Identity()
projector = SimCLRProjectionHead(512, 512, 128)
transform = SimCLRTransform(input_size=32)
criterion = NTXentLoss()
```

## Tuning notes

- Data augmentations (crop, color jitter, blur, grayscale) are the main inductive bias.
- Larger batch sizes help contrastive methods; non-contrastive methods can use smaller batches.
- Use a projection head during pretraining and a prediction head for non-contrastive methods.
- Monitor representation collapse via kNN accuracy, not just training loss.

## Verification

1. Train an SSL model on an unlabeled image set and run a linear probe.
2. Compare linear-probe accuracy to a supervised baseline and a random-initialized baseline.
3. Inspect embeddings with t-SNE/UMAP and nearest-neighbor retrieval.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2301.05712",
            "https://docs.lightly.ai/self-supervised-learning/",
            "https://arxiv.org/abs/2006.08218",
            "https://github.com/lightly-ai/lightly",
        ],
    },
    {
        "name": "contrastive-learning",
        "title": "Contrastive Learning",
        "description": "Instance discrimination, InfoNCE, SimCLR, MoCo, CLIP, and deep metric learning for vision, language, and retrieval.",
        "devin_body": r'''
## When to use

You want an embedding space where semantically similar samples are close and dissimilar samples are far apart, often with limited labels.

## Key concepts

- **Positive and negative pairs**: views of the same sample vs. other samples.
- **InfoNCE / NT-Xent**: noise-contrastive loss that scores positive pairs against negatives.
- **Momentum encoders and memory banks**: maintain a large and consistent set of negative examples.
- **Multimodal contrastive learning**: CLIP aligns images and text in a shared embedding space.
- **Hard negative mining**: focus on difficult negatives to improve sample efficiency.

## Code pattern

```python
from pytorch_metric_learning import losses, miners

miner = miners.MultiSimilarityMiner()
loss_func = losses.TripletMarginLoss()

for data, labels in dataloader:
    optimizer.zero_grad()
    embeddings = model(data)
    hard_pairs = miner(embeddings, labels)
    loss = loss_func(embeddings, labels, hard_pairs)
    loss.backward()
    optimizer.step()
```

## Tuning notes

- Batch size, temperature, and the number of negatives strongly affect InfoNCE.
- Choose a distance function (cosine, Euclidean) and mining strategy suited to the task.
- For CLIP-style multimodal training, balance image and text encoders and cap sequence length.
- Watch for mode collapse where embeddings collapse to a constant.

## Verification

1. Train a retrieval model and report Recall@K or mAP on a held-out query set.
2. Run a kNN classifier on learned embeddings and compare to a supervised baseline.
3. Visualize embedding space and confirm clusters align with classes.
''',
        "references": [
            "https://arxiv.org/abs/2002.05709",
            "https://arxiv.org/abs/1911.05722",
            "https://arxiv.org/abs/2103.00027",
            "https://kevinmusgrave.github.io/pytorch-metric-learning/",
        ],
    },
    {
        "name": "masked-autoencoders",
        "title": "Masked Autoencoders (MAE)",
        "description": "BERT-style masked prediction for vision, BEVT, data2vec, and generative masked image and language modeling.",
        "devin_body": r'''
## When to use

You want to pretrain a transformer with high input masking ratios and reconstruct the masked content, especially for images or multimodal signals.

## Key concepts

- **Asymmetric encoder-decoder**: encoder processes only visible patches; decoder is lightweight.
- **High masking ratio**: vision MAE often masks 75% of input patches.
- **Pixel/ token reconstruction**: target is the original masked patch, often after per-patch normalization.
- **Masked language modeling**: BERT, RoBERTa, and DeBERTa use token masking for text.
- **data2vec and BEiT**: unified masked-prediction frameworks for multiple modalities.

## Code pattern

```python
import torch
from mae import models_mae

model = models_mae.mae_vit_base_patch16()
loss, pred, mask = model(images, mask_ratio=0.75)
loss.backward()
```

## Tuning notes

- Use a high masking ratio for images; lower ratios work better for dense signals or video.
- Keep the decoder small; most compute should be in the encoder.
- Normalize pixel targets by their mean and std within each patch.
- Minimal augmentation is usually sufficient for MAE pretraining.

## Verification

1. Reconstruct masked image patches and report PSNR/SSIM.
2. Run a linear probe or finetune on a downstream classification task.
3. Ablate masking ratio and decoder depth and measure downstream accuracy.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2111.06377",
            "https://github.com/facebookresearch/mae",
            "https://ar5iv.labs.arxiv.org/html/2202.03670",
            "https://github.com/huggingface/pytorch-image-models",
        ],
    },
    {
        "name": "world-models",
        "title": "World Models",
        "description": "Latent dynamics models, recurrent state-space models, Dreamer, PlaNet, and agents that plan in imagination.",
        "devin_body": r'''
## When to use

You need to learn an environment model from high-dimensional observations and use it for planning, credit assignment, or transferring policies from simulated rollouts.

## Key concepts

- **Recurrent state-space model (RSSM)**: combines deterministic and stochastic latent states.
- **Encoder/decoder**: compress observations into latents and reconstruct observations.
- **Latent imagination**: plan and optimize policies entirely in the learned latent space.
- **Dreamer**: actor-critic agent trained on imagined trajectories with long-term gradients.
- **MuZero and PlaNet**: model-based planning without reconstructing observations.

## Code pattern

```python
import torch
import torch.nn as nn

class WorldModel(nn.Module):
    def __init__(self, obs_dim, act_dim, hid=256):
        super().__init__()
        self.encoder = nn.Linear(obs_dim, hid)
        self.dynamics = nn.GRUCell(act_dim + hid, hid)
        self.decoder = nn.Linear(hid, obs_dim)
        self.reward = nn.Linear(hid, 1)

    def forward(self, obs, action, hidden):
        e = self.encoder(obs)
        h = self.dynamics(torch.cat([action, e], -1), hidden)
        return self.decoder(h), self.reward(h), h
```

## Tuning notes

- Balance reconstruction, reward, and dynamics losses.
- Stochastic latent states help capture partial observability and multi-modal futures.
- Use straight-through or REINFORCE estimators for discrete latent variables.
- Regularize the latent space (e.g., KL loss) to prevent overfitting to idiosyncrasies.

## Verification

1. Roll out the learned model and compare imagined vs. real trajectories.
2. Train a policy inside the world model and transfer it to the real environment.
3. Measure long-horizon reward prediction error and sample-efficiency gains.
''',
        "references": [
            "https://arxiv.org/abs/1803.10122",
            "https://worldmodels.github.io/",
            "https://github.com/danijar/dreamerv3",
            "https://arxiv.org/abs/1912.01603",
        ],
    },
    {
        "name": "model-based-rl",
        "title": "Model-Based Reinforcement Learning",
        "description": "Learn environment dynamics for sample-efficient planning and policy optimization with PETS, MBPO, PlaNet, and MuZero.",
        "devin_body": r'''
## When to use

Environment interactions are expensive, slow, or risky, and you want a policy that is more sample-efficient than model-free methods.

## Key concepts

- **Learned transition and reward models**: train a neural network from real transitions.
- **Probabilistic ensembles**: capture epistemic uncertainty and avoid compounding errors.
- **Trajectory optimization / shooting**: CEM, MPPI, or cross-entropy planning in the learned model.
- **Model-based policy optimization (MBPO)**: use a learned model to generate synthetic training data.
- **PETS and PlaNet**: well-known probabilistic and latent model-based methods.

## Code pattern

```python
import mbrl.util.common as mutil
import mbrl.planning as planning
import gymnasium as gym

env = gym.make('CartPole-v1')
obs_shape = env.observation_space.shape
act_shape = env.action_space.shape

# Requires an OmegaConf-style config
dynamics_model = mutil.create_one_dim_tr_model(cfg, obs_shape, act_shape)
agent = planning.create_trajectory_optim_agent_for_model(model_env, cfg.algorithm.agent)
```

## Tuning notes

- Longer planning horizons amplify model bias; start short and increase gradually.
- Ensemble disagreement is a useful signal for exploration and uncertainty.
- Replan at every step or use a learned action sequence for real-time control.
- Use early termination and reward shaping to keep model rollouts stable.

## Verification

1. Compare sample efficiency (environment steps to target return) with model-free baselines.
2. Measure model prediction error on a holdout real transition set.
3. Verify that planning in the learned model transfers to the real environment.
''',
        "references": [
            "https://doi.org/10.1561/2200000086",
            "https://github.com/facebookresearch/mbrl-lib",
            "https://arxiv.org/abs/2104.10159",
            "https://arxiv.org/abs/1805.12114",
        ],
    },
    {
        "name": "hierarchical-rl",
        "title": "Hierarchical Reinforcement Learning",
        "description": "Options, feudal networks, and goal-conditioned hierarchies for long-horizon, sparse-reward tasks.",
        "devin_body": r'''
## When to use

Tasks are long-horizon, rewards are sparse or delayed, and you need temporal abstraction or reusable sub-skills.

## Key concepts

- **Options framework**: high-level actions are closed-loop sub-policies with initiation, execution, and termination conditions.
- **Semi-Markov Decision Process (SMDP)**: formalizes actions that take variable time.
- **Feudal networks**: manager sets abstract goals and worker selects primitive actions.
- **Goal-conditioned HRL**: high-level policy proposes subgoals; low-level policy reaches them (HIRO, HRO).
- **Option-critic**: joint learning of options and their policies end-to-end.

## Code pattern

```python
import torch
import torch.nn as nn

class HierarchicalAgent(nn.Module):
    def __init__(self, state_dim, action_dim, goal_dim):
        super().__init__()
        self.high_level = nn.Linear(state_dim, goal_dim)     # subgoal generator
        self.low_level = nn.Linear(state_dim + goal_dim, action_dim)

    def forward(self, state, goal):
        return self.low_level(torch.cat([state, goal], -1))
```

## Tuning notes

- Non-stationarity between high-level and low-level policies is the main challenge; use off-policy correction or fixed low-level pretraining.
- Choose subgoal spaces that are learnable but expressive.
- Control the time scale of each level; common values range from 10 to 100 steps.
- Reward the low-level with intrinsic goal-reaching rewards.

## Verification

1. Solve a maze or long-horizon navigation task and compare to a flat RL baseline.
2. Measure success rate and sample efficiency across difficulty levels.
3. Analyze option/subgoal usage to confirm meaningful temporal abstraction.
''',
        "references": [
            "https://doi.org/10.3390/make4010009",
            "https://arxiv.org/abs/1609.05140",
            "https://arxiv.org/abs/1709.02374",
            "https://arxiv.org/abs/1805.08296",
            "https://github.com/tensorflow/models/tree/master/research/efficient-hrl",
        ],
    },
    {
        "name": "offline-rl",
        "title": "Offline Reinforcement Learning",
        "description": "Learn from static logged datasets with CQL, IQL, TD3+BC, D4RL, and conservative/batch RL methods.",
        "devin_body": r'''
## When to use

You have a fixed, previously collected dataset and cannot or should not interact with the environment during training.

## Key concepts

- **Batch RL / offline RL**: learn a policy from a static set of transitions without new environment interaction.
- **Distributional shift**: the learned policy may visit out-of-distribution actions and states.
- **Conservative Q-Learning (CQL)**: regularizes Q-values to avoid overestimating OOD actions.
- **Implicit Q-Learning (IQL)**: learns a value function without querying OOD actions explicitly.
- **Decision Transformer and TD3+BC**: alternative offline methods using sequence modeling or behavior cloning regularization.

## Code pattern

```python
import d3rlpy
from d3rlpy.datasets import get_d4rl

dataset, env = get_d4rl('hopper-medium-v2')
cql = d3rlpy.algos.CQL(use_gpu=True)
cql.fit(dataset, n_steps=100000)
```

## Tuning notes

- The dataset quality and coverage heavily influence final performance.
- Conservative regularization should be strong enough to avoid OOD overestimation but not so strong that it paralyzes the policy.
- For continuous control, IQL is often a strong, easy-to-tune baseline.
- Use D4RL normalized scores for fair comparison.

## Verification

1. Train an offline algorithm on a D4RL dataset and report the normalized score.
2. Compare the offline policy to behavior cloning and online SAC baselines.
3. Evaluate on the real environment and check for OOD action selection.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2006.04779",
            "https://arxiv.org/abs/2110.06169",
            "https://takuseno.github.io/d3rlpy/",
            "https://github.com/takuseno/d3rlpy",
            "https://github.com/Farama-Foundation/D4RL",
        ],
    },
    {
        "name": "safe-rl",
        "title": "Safe Reinforcement Learning",
        "description": "Constrained Markov Decision Processes, CPO, P3O, Lagrangian methods, and safety-gym benchmarks for constrained RL.",
        "devin_body": r'''
## When to use

The task has explicit safety limits (velocity, collision, power) and the agent must maximize reward while keeping expected costs below a threshold.

## Key concepts

- **Constrained MDP (CMDP)**: maximize return subject to constraints on expected cumulative cost.
- **Constrained Policy Optimization (CPO)**: trust-region policy search with near-constraint satisfaction.
- **Primal-dual / Lagrangian methods**: PPO-Lagrangian, P3O, and TRPO-Lagrangian update a cost multiplier online.
- **Chance constraints and shielding**: ensure safety with high probability or via explicit safety filters.
- **Safety-Gymnasium**: standardized benchmark for constrained RL in navigation and locomotion.

## Code pattern

```python
import safety_gymnasium

env = safety_gymnasium.make('SafetyPointGoal1-v0')
obs, info = env.reset()
for _ in range(1000):
    action = env.action_space.sample()
    obs, reward, cost, terminated, truncated, info = env.step(action)
```

## Tuning notes

- Start with a strict cost limit and relax it as the policy converges.
- Primal-dual methods can oscillate; tune the Lagrange multiplier learning rate and projection.
- CPO is more conservative but expensive; Lagrangian methods scale better.
- Separate cost and value critics to avoid interference.

## Verification

1. Train with a cost limit and plot cumulative cost vs. training episodes.
2. Compare constrained return to an unconstrained baseline.
3. Test zero-shot constraint satisfaction on held-out cost limits.
''',
        "references": [
            "https://arxiv.org/abs/1705.10528",
            "https://github.com/PKU-Alignment/safety-gymnasium",
            "https://safety-gymnasium.readthedocs.io/en/latest/",
            "https://proceedings.mlr.press/v162/liu22b.html",
            "https://arxiv.org/abs/2205.11814",
        ],
    },
    {
        "name": "imitation-learning",
        "title": "Imitation Learning",
        "description": "Behavioral cloning, DAgger, GAIL, and learning policies from expert demonstrations with or without a reward function.",
        "devin_body": r'''
## When to use

Expert demonstrations are available but a reward function is hard to design, or you want a good warm-start policy before RL fine-tuning.

## Key concepts

- **Behavioral cloning (BC)**: supervised learning of actions from state-action expert demonstrations.
- **DAgger**: iterative dataset aggregation that queries an expert on states visited by the learned policy.
- **Generative Adversarial Imitation Learning (GAIL)**: adversarially matches the state-action distribution of the expert.
- **SQIL**: soft Q imitation learning that assigns positive rewards to expert transitions.
- **DAgger with noisy rollouts**: improves robustness by collecting data under the learner's own state distribution.

## Code pattern

```python
from imitation.algorithms.bc import BC
from imitation.data import rollout

transitions = rollout.flatten_trajectories(expert_trajectories)
bc_trainer = BC(
    observation_space=env.observation_space,
    action_space=env.action_space,
    demonstrations=transitions,
)
bc_trainer.train(n_epochs=50)
```

## Tuning notes

- Demonstration coverage and quality dominate BC performance.
- Use DAgger when the test-time state distribution differs from the expert data.
- For GAIL, carefully tune the discriminator and use a strong policy optimizer.
- Add entropy regularization and early stopping to avoid overfitting.

## Verification

1. Evaluate the learned policy on the task and compare return to the expert.
2. For BC, report action MSE or classification accuracy on a held-out expert set.
3. For DAgger, show that test-time rollouts improve over multiple iterations.
''',
        "references": [
            "https://arxiv.org/abs/1606.03476",
            "https://arxiv.org/abs/1011.0686",
            "https://imitation.readthedocs.io/en/stable/",
            "https://github.com/humancompatibleai/imitation",
        ],
    },
    {
        "name": "inverse-rl",
        "title": "Inverse Reinforcement Learning",
        "description": "Recover reward functions from expert demonstrations using MaxEnt IRL, apprenticeship learning, and adversarial IRL.",
        "devin_body": r'''
## When to use

You need to infer the objective that an expert is optimizing, design a reward function from behavior, or understand intent in sequential tasks.

## Key concepts

- **Reward ambiguity / degeneracy**: many reward functions can explain the same optimal policy.
- **Feature expectations**: match expected feature counts between expert and learned policy.
- **Maximum Entropy / Maximum Causal Entropy IRL**: resolves ambiguity via a principled distribution over trajectories.
- **Apprenticeship learning**: learn a policy whose feature expectations match the expert.
- **Adversarial IRL (AIRL) and GAIL**: recover rewards via a discriminator that distinguishes expert from learner.

## Code pattern

```python
import numpy as np
from imitation.algorithms.mce_irl import MCEIRL
from imitation.rewards import reward_nets

reward_net = reward_nets.BasicRewardNet(
    env.observation_space,
    env.action_space,
    hid_sizes=[256],
)
mce_irl = MCEIRL(
    expert_demonstrations,
    env,
    reward_net,
    log_interval=250,
    optimizer_kwargs=dict(lr=0.01),
    rng=np.random.default_rng(0),
)
mce_irl.train()
```

## Tuning notes

- Feature/reward network design is critical; include state, action, and next-state features when relevant.
- Add regularization to avoid degenerate reward solutions.
- Use a strong RL algorithm to re-optimize the recovered reward.
- Ground-truth rewards, when available, are the best validation signal.

## Verification

1. Optimize a policy with the recovered reward and compare its return to the expert.
2. Measure feature-expectation distance between expert and learned policy.
3. Inspect the learned reward on a grid of representative states.
''',
        "references": [
            "https://people.eecs.berkeley.edu/~russell/papers/ml00-irl.pdf",
            "https://www.cs.cmu.edu/~bziebart/publications/maximum-causal-entropy.pdf",
            "https://arxiv.org/abs/1710.11248",
            "https://arxiv.org/abs/1806.06877",
        ],
    },
    {
        "name": "curriculum-rl",
        "title": "Curriculum Reinforcement Learning",
        "description": "Task sequencing, automatic curriculum generation, and progressive difficulty for sample-efficient RL.",
        "devin_body": r'''
## When to use

The target task is too hard to learn from scratch, and you can generate a sequence of easier tasks or starting states that gradually build skills.

## Key concepts

- **Curriculum learning**: present tasks from easy to hard according to the learner's current ability.
- **Teacher-student curriculum (TSCL)**: a teacher selects subtasks where the student makes the fastest progress.
- **Reverse curriculum generation**: start near the goal and sample increasingly distant initial states.
- **Prioritized level replay (PLR) and domain randomization**: adapt task difficulty via learning progress or regret.
- **Reward/constraint curricula**: gradually introduce terms or increase strictness.

## Code pattern

```python
import gymnasium as gym

def make_env(level=0):
    # difficulty increases with level
    return gym.make('FrozenLake-v1', map_name=["4x4", "8x8", "12x12"][level], is_slippery=True)

curriculum = [make_env(level=i) for i in range(3)]
# train agent sequentially on each level before advancing
```

## Tuning notes

- Choose a difficulty measure aligned with true learning progress (not just episodic return).
- Keep easier tasks in the mix to avoid catastrophic forgetting.
- Advance the curriculum only when the current level reaches a threshold.
- Monitor transfer from curriculum tasks to the target task.

## Verification

1. Compare final performance and sample complexity with and without the curriculum.
2. Track success rate at each curriculum stage over time.
3. Ablate curriculum pacing and measure robustness on the target task.
''',
        "references": [
            "https://arxiv.org/abs/2003.04960",
            "https://arxiv.org/abs/1707.00183",
            "https://proceedings.mlr.press/v78/florensa17a.html",
            "https://proceedings.mlr.press/v70/graves17a.html",
        ],
    },
    {
        "name": "multi-task-learning",
        "title": "Multi-Task Learning",
        "description": "Shared representations, hard and soft parameter sharing, MTL architectures (MMoE, PLE, MTAN), and gradient balancing.",
        "devin_body": r'''
## When to use

You have several related prediction or control tasks and want a single model that shares computation, improves generalization, or reduces inference cost.

## Key concepts

- **Hard vs. soft parameter sharing**: shared trunk with task-specific heads, or cross-stitch/MMoE-style gates.
- **Multi-gate mixture of experts (MMoE) and PLE**: route examples through task-specific or shared experts.
- **Attention-based sharing (MTAN)**: learn task-specific attention masks over a shared network.
- **Gradient balancing**: GradNorm, uncertainty weighting, PCGrad, CAGrad, IMTL reduce negative transfer.
- **Negative transfer**: sharing can hurt some tasks; diagnose with per-task gradients.

## Code pattern

```python
import torch
import torch.nn as nn

class MultiTaskNet(nn.Module):
    def __init__(self, input_dim, task_dims):
        super().__init__()
        self.shared = nn.Sequential(nn.Linear(input_dim, 256), nn.ReLU())
        self.heads = nn.ModuleList([nn.Linear(256, d) for d in task_dims])

    def forward(self, x):
        h = self.shared(x)
        return [head(h) for head in self.heads]
```

## Tuning notes

- Group tasks with related inputs and labels; unrelated tasks cause negative transfer.
- Start with equal task weights and switch to GradNorm or PCGrad if one task dominates.
- Match head capacities to task difficulty; some tasks need deeper task-specific layers.
- Use LibMTL for fair benchmarking of architectures and weighting strategies.

## Verification

1. Train single-task baselines and compare per-task metrics to the multi-task model.
2. Measure gradient conflict via cosine similarity of task gradients.
3. Ablate sharing depth and task-weighting strategy on a fixed suite of tasks.
''',
        "references": [
            "https://arxiv.org/html/2404.18961",
            "https://github.com/median-research-group/LibMTL",
            "https://libmtl.readthedocs.io/en/latest/",
            "https://arxiv.org/abs/1801.06704",
            "https://www.jmlr.org/papers/v24/22-0347.html",
        ],
    },
]
