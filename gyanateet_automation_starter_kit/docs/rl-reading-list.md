# RL Papers Reading List for Gyanateet Dutta

> Curated for someone with a strong background in computer vision (DINOv2, V-JEPA2, 
> self-supervised learning, representation learning), diffusion models, VLA's, world models 
> (VAE+RNN), MuJoCo, and quantum machine learning — but who wants to go deeper into the 
> RL theory and algorithms powering modern post-training and RL-from-scratch systems.

---

## Tier 0: Foundations (Read These First)

### 1. Proximal Policy Optimization Algorithms (PPO)
- **arXiv**: [1707.06347](https://arxiv.org/abs/1707.06347)
- **Authors**: Schulman, Wolski, Dhariwal, Radford, Klimov (OpenAI, 2017)
- **Why**: PPO is the backbone of nearly all modern RL post-training. DAPO, GRPO, and 
  REPO are all descendants of PPO. Understanding the clipped surrogate objective is 
  essential before touching any of the newer algorithms.
- **Key idea**: Alternate between sampling data via environment interaction and optimizing 
  a surrogate objective with a trust-region clip. Simpler than TRPO, more stable than 
  vanilla policy gradient.
- **Your angle**: You know representation learning — PPO is where the encoder meets the 
  policy. The clip mechanism is what makes it stable enough for large-scale training.

### 2. Trust Region Policy Optimization (TRPO)
- **arXiv**: [1502.05477](https://arxiv.org/abs/1502.05477)
- **Authors**: Schulman, Levine, Abbeel, Jordan, Abbeel (2015)
- **Why**: The theoretical predecessor to PPO. Introduces the idea of monotonic policy 
  improvement under a KL-divergence trust region. PPO is the approximation; TRPO is the 
  proof.
- **Key idea**: Guarantee that each policy update improves the expected return, using a 
  quadratic approximation to the KL-constrained objective.
- **Your angle**: If you've ever wondered "why doesn't the policy just collapse?", TRPO 
  is where the mathematical answer lives.

### 3. Soft Actor-Critic (SAC)
- **arXiv**: [1801.01290](https://arxiv.org/abs/1801.01290)
- **Authors**: Haarnoja, Zhou, Hartikainen, et al. (2018)
- **Why**: Introduces **maximum entropy RL** — the idea that the optimal policy should 
  maximize both reward AND entropy. This is the deep theoretical root of every entropy 
  preservation technique we use in our Conditional-GQE pipeline (REPO, BF16, 
  ε-exploration, distribution mixing).
- **Key idea**: The soft Bellman equation adds an entropy bonus to the Q-value, making 
  the agent explicitly value exploration. Off-policy, sample-efficient, and the 
  theoretical basis for "entropy as a regularizer."
- **Your angle**: You already understand self-supervised learning and the importance of 
  representation diversity. SAC formalizes the same intuition for action distributions. 
  The temperature parameter α controls the exploration-exploitation tradeoff — exactly 
  like the temperature in our transformer sampling.

---

## Tier 1: Modern LLM RL Post-Training (The Core Stack)

### 4. DeepSeekMath / GRPO (Group Relative Policy Optimization)
- **arXiv**: [2402.03300](https://arxiv.org/abs/2402.03300)
- **Authors**: Shao, Wang, et al. (DeepSeek, 2024)
- **Why**: GRPO is the algorithm that powers DeepSeek-R1 and most modern reasoning 
  training. It eliminates the critic network from PPO by using group-relative advantage 
  estimation (Monte-Carlo samples from the same prompt). This is what our 
  `compute_advantages` function implements.
- **Key idea**: Instead of training a value function to estimate the baseline, sample 
  G outputs per prompt and use their mean reward as the baseline. Advantage = 
  (R_i - mean(R)) / std(R). Simpler, cheaper, and surprisingly effective.
- **Your angle**: The group-relative normalization is conceptually similar to batch 
  normalization in vision — you're centering the learning signal relative to peers, 
  not an absolute target. This is the algorithm your Conditional-GQE RL pipeline is 
  built on.

### 5. DAPO: Decoupled Clip and Dynamic Sampling Policy Optimization
- **arXiv**: [2503.14476](https://arxiv.org/abs/2503.14476)
- **Project**: [dapo-sia.github.io](https://dapo-sia.github.io/)
- **Authors**: ByteDance Seed team (2025)
- **Why**: DAPO is the direct algorithm our `train_rl_dapo.py` implements. It improves 
  GRPO with four key innovations: (1) decoupled clipping (separate low/high clip bounds), 
  (2) dynamic sampling (skip groups with zero reward variance), (3) token-level loss 
  (instead of sequence-level), and (4) overlong reward shaping.
- **Key idea**: The clip-higher trick (clip_high > clip_low) allows the policy to explore 
  more aggressively on positive advantages while still being conservative on negative 
  ones. Dynamic sampling avoids wasting compute on degenerate sample groups.
- **Your angle**: The decoupled clip is like asymmetric augmentation in vision — you 
  want to encourage some transformations (exploration) while preventing others 
  (collapse). The dynamic sampling is analogous to hard negative mining.

### 6. Entropy-Preserving Reinforcement Learning (REPO + ADAPO)
- **arXiv**: [2603.11682](https://arxiv.org/abs/2603.11682)
- **Venue**: ICLR 2026
- **Authors**: (2026)
- **Why**: This is the paper that directly inspired our 5-layer entropy collapse defense. 
  It formally proves that PPO's clipping bounds entropy change, that DAPO's and GSPO's 
  clipping implicitly preserve entropy, and that numerical precision (BF16 vs FP16) 
  significantly impacts entropy dynamics. REPO modifies the advantage function to 
  explicitly regulate entropy.
- **Key idea**: REPO (Regulated Entropy Policy Optimization) adds a centered log-prob 
  penalty to the advantage: A_REPO = A - β·(log π(a|s) - E[log π(a|s)]). This penalizes 
  high-probability (deterministic) actions and boosts low-probability (diverse) ones. 
  ADAPO extends this with adaptive asymmetric clipping.
- **Your angle**: The BF16 vs FP16 analysis is critical — the paper shows that FP16's 
  5 exponent bits cause multiplicative bias in softmax gradients that systematically 
  reduces entropy. This is why we switched to BF16 (8 exponent bits). The entropy 
  trajectory analysis ("it's the journey, not the destination") resonates with your 
  understanding of representation learning dynamics.

---

## Tier 2: RL From Scratch (No Supervised Pretraining)

### 7. General Intelligence Requires Reward-based Pretraining
- **arXiv**: [2502.19402](https://arxiv.org/abs/2502.19402)
- **Authors**: Han, Pari, Gershman, Agrawal (MIT, 2025)
- **Why**: This is the paper that justifies our entire "pure RL from scratch" pipeline. 
  It demonstrates that RL from scratch (RPT) outperforms SFT-then-RL (93% vs 80% on 
  test set), drawing the AlphaGo vs AlphaZero analogy. SFT memorizes patterns; RL 
  discovers general strategies.
- **Key idea**: Supervised pretraining creates a local minimum in the reasoning space 
  that subsequent RL can't escape. Pure RL from scratch, with a curriculum of synthetic 
  tasks, discovers more generalizable reasoning functions. The paper also advocates for 
  small context windows to reduce spurious correlations.
- **Your angle**: You've worked with DINOv2 and V-JEPA2 — you know that self-supervised 
  learning discovers richer representations than supervised pretraining. This paper 
  makes the same argument for RL: reward-based pretraining discovers richer policies 
  than imitation-based pretraining. Your Conditional-GQE pipeline is a concrete 
  instantiation of this philosophy.

### 8. RL Excursions during Pre-training
- **Project**: [rl-excursions.github.io](https://rl-excursions.github.io/)
- **Authors**: (2025)
- **Why**: Complementary to the above. Shows that RL is effective surprisingly early in 
  pretraining (from 4B tokens), that RL preserves general capabilities while SFT degrades 
  them, and that parallel averaging of RL and SFT gradients achieves the best of both 
  worlds.
- **Key idea**: Direct RL matches or outperforms the full SFT→RL pipeline. SFT 
  consistently degrades non-math benchmarks by 4-8 percentage points, while RL leaves 
  them unchanged. Parallel gradient averaging is a simple but powerful combination.
- **Your angle**: The "parallel averaging" idea is like mixing losses in multi-task 
  learning — you've done this in vision (detection + segmentation + depth). The same 
  principle applies to mixing RL and SFT gradients.

### 9. Mastering the Game of Go Without Human Knowledge (AlphaZero)
- **Nature**: [nature24270](https://www.nature.com/articles/nature24270)
- **Authors**: Silver, Schrittwieser, Simonyan, et al. (DeepMind, 2017)
- **Why**: The original "RL from scratch" paper. AlphaZero learned Go, chess, and shogi 
  tabula rasa — no human data, no domain knowledge beyond game rules. It became its own 
  teacher through self-play. This is the philosophical ancestor of our pure RL pipeline.
- **Key idea**: A neural network trained purely via self-play RL, combined with MCTS, 
  achieves superhuman performance. The key insight: removing human demonstrations 
  allows the system to discover strategies that humans never found.
- **Your angle**: You've watched the Two Minute Papers coverage of this — now read the 
  actual paper. The self-play loop is the same concept as our energy-reward loop: 
  sample → evaluate → update → repeat. The system discovers quantum circuit strategies 
  the same way AlphaZero discovered Go strategies.

### 10. Mastering Chess and Shogi by Self-Play (AlphaZero Generalization)
- **arXiv**: [1712.01815](https://arxiv.org/abs/1712.01815)
- **Authors**: Silver, Hubert, Schrittwieser, et al. (DeepMind, 2017)
- **Why**: Generalizes the AlphaZero algorithm beyond Go. Shows that a single RL 
  algorithm can achieve superhuman performance in multiple domains with no domain-specific 
  knowledge.
- **Key idea**: Same algorithm, different games. The generality of the approach is the 
  key finding.

---

## Tier 3: Diversity and Mode Collapse Prevention (Directly Relevant to Our Fix)

### 11. DARLING: Diversity-Aware Reinforcement Learning
- **arXiv**: [2509.02534](https://arxiv.org/abs/2509.02534)
- **Authors**: Li, Zhang, Yu, Saha, Khashabi, Weston, Lanchantin, Wang (Meta AI, 2025)
- **Code**: [github.com/facebookresearch/darling](https://github.com/facebookresearch/darling)
- **Why**: Directly inspired our diversity reward component. DARLING jointly optimizes 
  for response quality AND semantic diversity. It introduces a learned partition 
  function to measure diversity beyond surface-level lexical variations, then combines 
  this diversity signal with a quality reward.
- **Key idea**: Partition rollouts into semantic clusters using a classifier, then 
  multiply the diversity assessment with the quality reward. Trajectories that are 
  both high-quality AND semantically distinct get amplified advantages. Strikingly, 
  optimizing for diversity catalyzes exploration, which manifests as higher quality.
- **Your angle**: The "diversity catalyzes quality" finding is exactly what we observe 
  in quantum circuit generation — diverse operator sequences explore more of the 
  Hilbert space and find better energy minima. The semantic clustering idea could be 
  applied to cluster quantum circuits by their entanglement structure.

### 12. GAPO: Group-Aware Policy Optimization
- **Venue**: EMNLP 2025
- **Link**: [aclanthology.org/2025.emnlp-main.1649](https://aclanthology.org/2025.emnlp-main.1649/)
- **Authors**: Anschel, Shoshan, Botach, et al. (Amazon, 2025)
- **Why**: Directly inspired our group-level diversity approach. GAPO is a simple 
  extension of GRPO that computes rewards over the group as a whole, enabling 
  group-level properties like diversity and coverage. Uses a frequency-aware reward 
  function that penalizes over-represented outputs.
- **Key idea**: Instead of computing reward independently per rollout, compute it 
  jointly across the group. Penalize outputs that appear frequently in the group, 
  reward outputs that are rare. This directly addresses mode collapse without changing 
  the model architecture or decoding strategy.
- **Your angle**: The frequency-aware reward is exactly what our `w_diversity` 
  (unique operator fraction) implements. GAPO provides the theoretical framework for 
  why group-level reward computation is more effective than individual reward 
  computation.

### 13. SetPO: Set-Level Policy Optimization
- **arXiv**: [2602.01062](https://arxiv.org/abs/2602.01062)
- **Venue**: ICML 2026
- **Authors**: Li, Zhang, Wang, et al. (2026)
- **Code**: [github.com/chenyili0818/SetPO](https://github.com/chenyili0818/SetPO)
- **Why**: The most principled diversity-preserving method. SetPO assigns each 
  trajectory a set-level marginal diversity credit using a leave-one-out estimator. 
  Trajectories that cover distinct semantic modes receive higher credits; redundant 
  ones receive lower credits. Uses kernelized similarity and diminishing-returns 
  principles.
- **Key idea**: For each prompt, sample a group of rollouts, compute pairwise semantic 
  similarities using a pretrained embedding model, then quantify how redundant each 
  trajectory is. The leave-one-out marginal contribution estimator rewards rarer 
  trajectories more. The shaping function g(x) = -log(1+x) embodies diminishing 
  marginal sensitivity.
- **Your angle**: The leave-one-out estimator is elegant — it's like leave-one-out 
  cross-validation but for diversity credit assignment. Could be applied to quantum 
  circuits by measuring pairwise similarity in terms of operator overlap or 
  entanglement structure.

### 14. Diversity-Aware Policy Optimization for LLM Reasoning
- **Link**: [openreview.net/pdf/c884fab9a8271939813690f5af1e6cebe20f7a2a](https://openreview.net/pdf/c884fab9a8271939813690f5af1e6cebe20f7a2a.pdf)
- **Why**: Introduces token-level entropy as a diversity metric (instead of sequence-level 
  entropy, which has length bias). Strategically applies diversity enhancement only on 
  positive samples, avoiding the pitfall of increasing diversity in incorrect solutions.
- **Key idea**: Token-level entropy H(πθ(·|q, o<t)) per token, averaged over the 
  sequence. The gradient of diversity w.r.t. the policy promotes increasing probability 
  of low-probability tokens. Excluding diversity enhancement for negative samples 
  mitigates conflicts between quality and diversity.
- **Your angle**: The token-level entropy idea is directly applicable to our transformer 
  — we could compute per-operator entropy instead of per-sequence entropy. The 
  "diversity only on positive samples" insight is important: we don't want to encourage 
  diversity in bad circuits.

---

## Tier 4: Exploration and Curiosity (Connecting to Your SSL/CV Background)

### 15. Curiosity-driven Exploration by Self-supervised Prediction (ICM)
- **arXiv**: [1705.05363](https://arxiv.org/abs/1705.05363)
- **Authors**: Pathak, Agrawal, Efros, Darrell (UC Berkeley, 2017)
- **Why**: Bridges your self-supervised learning expertise with RL. The Intrinsic 
  Curiosity Module (ICM) uses a forward prediction model in a learned feature space 
  to compute curiosity rewards. The feature space is learned via self-supervised 
  inverse dynamics — exactly the kind of representation learning you know from DINOv2.
- **Key idea**: The agent is rewarded for visiting states where its prediction model 
  is surprised (high prediction error). The prediction model operates in a learned 
  feature space (not pixel space) to avoid being distracted by irrelevant environmental 
  details. The inverse dynamics model (state + action → next state) learns useful 
  features without requiring the full environment model.
- **Your angle**: This is self-supervised learning applied to RL exploration. The 
  inverse dynamics model is like a contrastive learning objective — it learns what 
  features are controllable. You could imagine a quantum version: curiosity rewards 
  for exploring unexplored regions of Hilbert space.

### 16. World Models
- **arXiv**: [1803.10122](https://arxiv.org/abs/1803.10122)
- **Authors**: Ha, Schmidhuber (2018)
- **Why**: You already understand world models from first principles (VAE+RNN). This 
  is the canonical paper. It shows that an RL agent can learn to operate in a compressed 
  latent space (VAE) with a predictive model (RNN) of the environment, and that 
  policies trained in this "dream" transfer to reality.
- **Key idea**: Three components: (1) V (Vision) compresses observations into latent 
  z, (2) M (Memory) predicts the next latent given current latent and action 
  (LSTM/MDN-RNN), (3) C (Controller) is a simple linear policy in latent space. The 
  agent can train entirely inside the dream model.
- **Your angle**: You know this already, but read it for the RL training details — 
  how the controller is evolved (CMA-ES, not gradient descent!) in the original paper. 
  The connection to your V-JEPA2 work: V-JEPA learns a predictive world model in 
  latent space, which is exactly what M does here.

---

## Tier 5: Quantum-Specific RL (Directly Relevant to Conditional-GQE)

### 17. Reinforcement Learning for Variational Quantum Circuits Design
- **arXiv**: [2409.05475](https://arxiv.org/abs/2409.05475)
- **Why**: Trains an RL agent to autonomously generate quantum circuit ansätze for VQE. 
  The agent discovered a novel family of ansätze ("Ryz-connected") that achieves high 
  approximation ratios for MaxCut problems. Validates the RL-for-circuit-design approach.
- **Key idea**: PPO agent with graph-based state observations. The action space is gate 
  selection. The reward is the approximation ratio. The agent generalizes across graph 
  topologies and sizes.
- **Your angle**: This is exactly what your Conditional-GQE does, but for combinatorial 
  optimization instead of molecular energy. The "Ryz-connected" discovery is analogous 
  to your model discovering entangling operators.

### 18. Automated Design of Structured Variational Quantum Circuits (RLVQC)
- **arXiv**: [2507.16001](https://ar5iv.labs.arxiv.org/html/2507.16001)
- **Why**: Two RL variants: RLVQC Block (discovers a repeated block applied to all 
  interacting qubit pairs, generalizing QAOA) and RLVQC Global (unconstrained gate 
  placement). Uses PPO with empirical measurement outcomes as state observations.
- **Key idea**: The Block variant is like a structured ansatz (good inductive bias), 
  while the Global variant is like a fully flexible ansatz. The Block variant 
  outperforms QAOA while producing comparable depth circuits.
- **Your angle**: The Block vs Global distinction maps to your UCCSD pool (structured) 
  vs unconstrained operator generation. The paper shows that structure helps — which 
  is why your UCCSD pool approach is well-founded.

### 19. FlowQ-Net: Generative Framework for Automated Quantum Circuit Design
- **arXiv**: [2510.26688](https://doi.org/10.48550/arxiv.2510.26688)
- **Why**: Uses Generative Flow Networks (GFlowNets) instead of RL to sample circuits 
  in proportion to a flexible reward. Learns to generate a diverse family of 
  high-quality designs rather than converging on a single optimum. Directly addresses 
  the mode collapse problem in quantum circuit generation.
- **Key idea**: GFlowNets sample from a distribution proportional to the reward, not 
  just maximizing it. This naturally produces diversity — the model generates a 
  portfolio of circuits with varying tradeoffs between quality, depth, and resource 
  efficiency. Uses up to 10x fewer gates than conventional approaches.
- **Your angle**: GFlowNets are to RL what variational inference is to MAP estimation — 
  they capture the full posterior, not just the mode. This could be a future direction 
  for Conditional-GQE: instead of DAPO (which maximizes reward), use GFlowNets (which 
  sample proportional to reward) to naturally generate diverse circuit portfolios.

### 20. Entanglement-Aware DRL-QAS
- **Journal**: [Phys. Rev. A](https://journals.aps.org/pra/abstract/10.1103/7rc4-p446)
- **Why**: Overcomes the "fidelity trap" in RL-based quantum architecture search by 
  adding entanglement as an auxiliary reward. Fidelity-driven agents get stuck in 
  suboptimal, overly complex circuits; entanglement-aware agents discover minimal-depth 
  circuits.
- **Key idea**: Reward = fidelity + entanglement_measure. The entanglement reward 
  provides a more complete physical description of the state space, enabling the agent 
  to distinguish between states that are superficially similar but structurally distinct.
- **Your angle**: This is exactly the principle behind our `w_entangle` reward 
  component. The paper provides rigorous evidence that entanglement-aware rewards 
  are not just a hack — they provide fundamentally better gradients for circuit search.

### 21. TensorRL-QAS: RL with Tensor Networks for Quantum Architecture Search
- **Venue**: NeurIPS 2025
- **Link**: [proceedings.neurips.cc/paper_files/paper/2025/file/af008ae1c0301e218ee89a86833198e3-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2025/file/af008ae1c0301e218ee89a86833198e3-Paper-Conference.pdf)
- **Why**: Warm-starts RL-QAS with tensor network (DMRG) methods. Uses MPS 
  approximations of the ground state to initialize the RL agent's circuit, then 
  refines via RL. Reduces function evaluations by 100-fold and accelerates training 
  by 98%.
- **Key idea**: Don't start RL from an empty circuit — start from a TN-optimized 
  circuit and let RL refine it. The TN warm-start provides structural priors that 
  dramatically reduce the search space.
- **Your angle**: This is the "pretraining helps RL" argument, but with tensor 
  networks instead of supervised learning. Could be a middle ground between pure RL 
  from scratch and SFT-then-RL: use TN methods to provide structural initialization, 
  then let RL discover the details.

---

## Suggested Reading Order

```
Tier 0 (Foundations):
  PPO (1707.06347) → TRPO (1502.05477) → SAC (1801.01290)

Tier 1 (Modern LLM RL):
  GRPO (2402.03300) → DAPO (2503.14476) → REPO (2603.11682)

Tier 2 (RL From Scratch):
  AlphaZero (nature24270) → RPT (2502.19402) → RL Excursions

Tier 3 (Diversity/Mode Collapse):
  DARLING (2509.02534) → GAPO (EMNLP 2025) → SetPO (2602.01062)

Tier 4 (Exploration/Curiosity):
  ICM (1705.05363) → World Models (1803.10122)

Tier 5 (Quantum RL):
  RL-VQC (2409.05475) → FlowQ-Net → Entanglement-Aware QAS → TensorRL-QAS
```

## How These Connect to Your Work

| Your Project | Papers That Inform It |
|---|---|
| Conditional-GQE RL pipeline | DAPO, GRPO, REPO, AlphaZero, RPT |
| Mode collapse fix (diversity reward) | DARLING, GAPO, SetPO, Diversity-Aware PO |
| UCCSD operator pool | RL-VQC, Entanglement-Aware QAS, TensorRL-QAS |
| BF16 mixed precision choice | REPO (entropy dynamics analysis) |
| Curriculum learning | RPT (synthetic task curriculum), AlphaZero (self-play curriculum) |
| Frequency penalty in sampling | GAPO (frequency-aware reward), CTRL/LZ penalty |
| Future: GFlowNet approach | FlowQ-Net |
| Future: TN warm-start | TensorRL-QAS |
| DINOv2 / V-JEPA2 connection | ICM (self-supervised exploration), World Models |
| VLA / world model connection | World Models, SAC (maximum entropy) |

## Papers You Can Skip (For Now)

- **DQN** (Mnih et al., 2013) — important historically, but you're working with 
  continuous/discrete sequence generation, not Atari frames. Read if you want the 
  full historical context.
- **A3C** (Mnih et al., 2016) — asynchronous training is less relevant with modern 
  distributed training frameworks. The ideas are subsumed by PPO + distributed sampling.
- **DDPG/TD3** — continuous action space methods. Less relevant for your discrete 
  operator sequence generation. Read if you get into robotics control.

---

*Last updated: June 2026*
*Maintained for: Gyanateet Dutta (@Ryukijano)*
*Context: Conditional-GQE pure RL from scratch pipeline, mode collapse fixes*
