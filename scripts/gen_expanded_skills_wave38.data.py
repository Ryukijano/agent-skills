SKILLS = [
    {
        "name": "ai-for-synthetic-data",
        "title": "AI for Synthetic Data",
        "description": "Use generative models and differential privacy to create realistic, useful, and privacy-preserving synthetic datasets.",
        "devin_body": r'''
## When to use

You need to augment, privatize, or replace a real dataset with artificial samples for downstream ML, testing, or sharing while preserving privacy and utility.

## Usage

- Generate tabular synthetic records with GANs, VAEs, diffusion, copulas, and Bayesian networks.
- Apply differential privacy budgets when training generative models for release.
- Synthesize text, images, and low-resource NLP data with LLMs.
- Audit the utility-privacy trade-off with fidelity, downstream, and membership-inference tests.

## Steps

1. Profile the real dataset and identify sensitive variables and downstream use cases.
2. Choose a synthesis method (GAN, VAE, diffusion, copula, LLM) and set privacy parameters.
3. Train the generative model and apply differential privacy or other protections.
4. Evaluate fidelity with marginals, conditionals, and propensity-score-based metrics.
5. Audit with membership-inference and attribute-inference attacks before release.
6. Document method, privacy assumptions, and utility limitations for downstream users.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Compare downstream utility on real vs synthetic data
X_real, y_real = real_df.drop("target", axis=1), real_df["target"]
X_syn, y_syn = synth_df.drop("target", axis=1), synth_df["target"]

real_model = RandomForestClassifier(random_state=42).fit(X_real, y_real)
syn_model = RandomForestClassifier(random_state=42).fit(X_syn, y_syn)

real_on_real = real_model.score(X_real, y_real)
syn_on_real = syn_model.score(X_real, y_real)
print("Utility gap:", real_on_real - syn_on_real)
```

## Tuning notes

- Preserve marginal and joint distributions; use propensity-score-based metrics for high-dimensional tables.
- Choose epsilon carefully: smaller values increase privacy but can destroy utility.
- Audit with membership-inference or attribute-inference attacks before release.
- Document the synthesis method and privacy assumptions for downstream users.

## Verification

1. Train a classifier on synthetic data and evaluate its test AUC on real held-out data.
2. Run a membership-inference attack against the synthetic release and report precision at fixed recall.
3. Compare histograms and conditional distributions of key variables between real and synthetic data.
        ''',
        "references": [
            "https://arxiv.org/abs/2403.04190",
            "https://arxiv.org/abs/2302.04062",
            "https://doi.org/10.48550/arxiv.2401.02524",
            "https://arxiv.org/abs/2503.20846",
        ],
    },
    {
        "name": "ai-for-generative-engineering",
        "title": "AI for Generative Engineering",
        "description": "Use diffusion, VAEs, and flow models to generate engineering designs that meet performance and manufacturing constraints.",
        "devin_body": r'''
## When to use

You are exploring novel engineering designs (shapes, structures, materials, or processes) and want to generate or complete candidates that satisfy performance and manufacturing constraints.

## Usage

- Generate design candidates conditioned on target performance with generative inverse design.
- Embed physics, safety, and feasibility constraints into the generative process.
- Apply diffusion and flow matching to continuous or structured design spaces.
- Produce Pareto-optimal designs across multiple objectives.

## Steps

1. Define the design space, performance targets, and constraints (physics, safety, manufacturability).
2. Train a generative model on existing designs and their performance labels.
3. Add feasibility classifiers or repair loops to reject physically impossible designs.
4. Generate a diverse set of candidates and evaluate with surrogate or full simulations.
5. Check constraint satisfaction and compute the Pareto front across objectives.
6. Validate top designs with high-fidelity FE/CFD and physical tests.

## Code pattern

```python
import torch

# Simple constrained repair loop for generated designs
def repair(design, simulator, target, max_iter=20, lr=0.01):
    for _ in range(max_iter):
        pred = simulator(design)
        loss = ((pred - target) ** 2).mean()
        if loss < 0.01:
            break
        design = design - lr * torch.autograd.grad(loss, design)[0]
    return design
```

## Tuning notes

- Train separate feasibility classifiers to reject physically impossible designs.
- Use surrogate simulators to amortize expensive FE/CFD evaluations.
- Balance novelty with distributional similarity to avoid unrealistic extrapolations.
- Validate generated designs with the full simulator or physical tests.

## Verification

1. Generate 100 structural/aerodynamic candidates and check what fraction satisfy constraints.
2. Compare a generative inverse-design pipeline to a gradient-based inverse-design baseline.
3. Plot the Pareto front of generated designs across performance and manufacturability.
        ''',
        "references": [
            "https://arxiv.org/abs/2412.13281",
            "https://arxiv.org/abs/2306.15166",
            "https://arxiv.org/abs/2309.02040",
            "https://arxiv.org/abs/2406.09143",
        ],
    },
    {
        "name": "ai-for-computational-design",
        "title": "AI for Computational Design",
        "description": "Use differentiable simulation, topology optimization, and CAD-aware generative models to co-design products and structures.",
        "devin_body": r'''
## When to use

You are designing buildings, products, mechanical parts, or architectural structures and need to integrate physical simulation, constraints, and AI-driven exploration into the design loop.

## Usage

- Combine neural networks with differentiable physics and geometry kernels.
- Run topology and shape optimization with SIMP, level-set, evolutionary, or gradient methods.
- Ensure procedural CAD and structural feasibility with solver-aided generative models.
- Explore multi-fidelity design spaces and interpolate shapes.

## Steps

1. Translate the design brief into geometry parameters, physics constraints, and objectives.
2. Build or wrap a differentiable surrogate or high-fidelity solver for the design.
3. Optimize topology or shape parameters with gradient or evolutionary search.
4. Add fabrication and assembly constraints early in the loop.
5. Validate optimized designs with high-fidelity FE/CFD and physical prototypes.
6. Generate production-ready CAD and run DRC or kernel checks.

## Code pattern

```python
import torch

# Differentiate a simple surrogate simulator with respect to a design variable
def compliance_loss(design, solver, target_shape):
    shape = solver(design)
    return ((shape - target_shape) ** 2).mean()

design = torch.nn.Parameter(torch.zeros(16))
optimizer = torch.optim.Adam([design], lr=0.01)
for _ in range(100):
    optimizer.zero_grad()
    loss = compliance_loss(design, surrogate_solver, target)
    loss.backward()
    optimizer.step()
```

## Tuning notes

- Ensure the surrogate simulator is accurate enough in the target design region.
- Use mesh-independent representations when possible to avoid retraining for new topologies.
- Augment with fabrication and assembly constraints early in the loop.
- Validate optimized designs with high-fidelity FE/CFD and physical prototypes.

## Verification

1. Optimize a simple truss or shell structure and compare compliance to a baseline.
2. Generate a parametric CAD part from a design brief and verify it with a CAD kernel.
3. Run a multi-objective design sweep and identify the knee of the Pareto front.
        ''',
        "references": [
            "https://arxiv.org/abs/2409.02606",
            "https://arxiv.org/abs/2511.17111",
            "https://arxiv.org/abs/2405.18075",
            "https://arxiv.org/abs/2502.09819",
        ],
    },
    {
        "name": "ai-for-human-centered-ai",
        "title": "AI for Human-Centered AI",
        "description": "Use human-AI interaction, explainability, and participatory design to keep people at the center of AI systems.",
        "devin_body": r'''
## When to use

You are building an AI system that people must understand, trust, and effectively collaborate with, and you want to center end-user needs, capabilities, and values in the design.

## Usage

- Design prompts and interfaces for effective human-AI collaboration.
- Provide feature attribution, counterfactuals, and model cards for explainability.
- Collect human feedback with active learning and interactive model refinement.
- Calibrate trust and avoid overreliance through appropriate reliance interfaces.
- Co-design with stakeholders and impacted communities.

## Steps

1. Identify user needs, mental models, and values for the target task or decision.
2. Design the interaction (prompts, displays, explanations) and collect user feedback.
3. Implement explainability methods matched to the user's level of expertise.
4. Run human-AI experiments and measure task success, trust, and overreliance.
5. Iterate on the interface and model based on user feedback.
6. Deploy with monitoring for fairness, accessibility, and sustained human control.

## Code pattern

```python
import shap
from sklearn.inspection import permutation_importance

# Explain a model to a human reviewer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test.iloc[:100])

# Identify which features most affect predictions
importance = permutation_importance(model, X_test, y_test, n_repeats=5)
feature_rank = dict(zip(X_test.columns, importance.importances_mean))
```

## Tuning notes

- Explainability should match the user's mental model, not just the model internals.
- Avoid over-automation; keep meaningful human control and graceful failure.
- Test with diverse user groups; trust and utility are context- and population-dependent.
- Measure task outcomes, not just model accuracy, in human-AI experiments.

## Verification

1. Run a human-AI co-creation study and compare idea quality and ownership across interaction modes.
2. Evaluate an explanation interface with a think-aloud protocol and task success.
3. Monitor for overreliance in a deployed decision-support tool and adjust confidence displays.
        ''',
        "references": [
            "https://arxiv.org/abs/2601.11812",
            "https://dl.acm.org/doi/10.1145/3544548.3580959",
            "https://arxiv.org/abs/2310.07127",
            "https://arxiv.org/abs/2105.05424",
        ],
    },
    {
        "name": "ai-for-ai-ethics",
        "title": "AI for AI Ethics",
        "description": "Audit automated hiring and public-sector AI systems for disparate impact, transparency gaps, and compliance with bias-auditing laws like NYC Local Law 144.",
        "devin_body": r'''
## When to use

You need to identify, measure, and mitigate ethical risks such as bias, discrimination, privacy violations, lack of transparency, or harm in an AI system or dataset.

## Usage

- Audit models for demographic parity, equalized odds, and calibration across groups.
- Generate SHAP, LIME, and counterfactual explanations for high-stakes decisions.
- Maintain model cards, datasheets, and algorithmic audit logs.
- Apply differential privacy, consent, and data minimization practices.
- Engage stakeholders and use value-sensitive design.

## Steps

1. Define the protected groups and ethical risks for the use case.
2. Run a quantitative fairness audit and report subgroup performance.
3. Generate explanations and conduct stakeholder impact assessments.
4. Choose and apply an intervention (reweighting, threshold tuning, etc.).
5. Re-audit the system and document trade-offs in a model card.
6. Establish ongoing monitoring and governance for ethical risks.

## Code pattern

```python
from fairlearn.metrics import demographic_parity_difference, equalized_odds_difference

# Audit a classifier for fairness across a protected group
y_pred = model.predict(X_test)
dp = demographic_parity_difference(y_test, y_pred, sensitive_features=A_test)
eo = equalized_odds_difference(y_test, y_pred, sensitive_features=A_test)
print("DP:", dp, "EO:", eo)
```

## Tuning notes

- Choose a fairness criterion that matches the legal, social, and business context.
- Report subgroup performance and intersectional metrics, not just aggregate.
- Pair quantitative audits with qualitative stakeholder impact assessments.
- Document limitations and intended use in model cards and datasheets.

## Verification

1. Run a fairness audit on a credit or hiring model and report disparities by protected group.
2. Generate SHAP or counterfactual explanations for high-stakes decisions.
3. Compare an intervention (e.g., reweighting or threshold tuning) against a baseline across metrics.
        ''',
        "references": [
            "https://arxiv.org/abs/2402.08323",
            "https://arxiv.org/abs/2311.17228",
            "https://arxiv.org/abs/2107.06641",
            "https://arxiv.org/abs/2411.09973",
        ],
    },
    {
        "name": "ai-for-ai-governance",
        "title": "AI for AI Governance",
        "description": "Use frameworks, risk registers, and lifecycle oversight to manage AI systems responsibly.",
        "devin_body": r'''
## When to use

You are establishing or operating governance for an AI system or portfolio and need to map risks, assign accountability, and align with standards and regulations.

## Usage

- Map, assess, treat, and monitor risks across the AI lifecycle.
- Align with NIST AI RMF, OECD AI Principles, ISO/IEC 42001, and other frameworks.
- Assign accountability to developers, deployers, users, and impacted parties.
- Maintain lifecycle governance over data, model, deployment, monitoring, and incident response.
- Engage oversight boards and multi-stakeholder governance.

## Steps

1. Identify the AI system, use case, and applicable regulations or standards.
2. Create a risk register with likelihood, impact, owners, and treatment controls.
3. Map the lifecycle against the chosen governance framework.
4. Assign roles and responsibilities for each lifecycle stage.
5. Run incident-response tabletop exercises and establish monitoring.
6. Review and update governance artifacts as the system and regulations evolve.

## Code pattern

```python
import pandas as pd

# Maintain a lightweight AI risk register
risks = pd.DataFrame([
    {"id": "R1", "risk": "unfair outcomes", "likelihood": 3, "impact": 4, "owner": "ML team"},
    {"id": "R2", "risk": "privacy breach", "likelihood": 2, "impact": 5, "owner": "security"},
])
risks["score"] = risks["likelihood"] * risks["impact"]
print(risks.sort_values("score", ascending=False))
```

## Tuning notes

- Governance must be proportionate to risk, use-case, and organizational capacity.
- Document decisions, assumptions, and trade-offs in a model card and risk log.
- Engage domain experts and impacted communities early, not just after deployment.
- Align internal governance with external standards to reduce fragmentation.

## Verification

1. Produce a risk register and control plan for a high-risk AI use case.
2. Map an AI system's lifecycle against a chosen framework (e.g., NIST AI RMF).
3. Run a tabletop incident-response exercise for a model failure or bias complaint.
        ''',
        "references": [
            "https://www.oecd.org/en/topics/ai-principles.html",
            "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
            "https://www.oecd.org/en/publications/advancing-accountability-in-ai_2448f04b-en.html",
            "https://legalinstruments.oecd.org/api/print?ids=648&lang=en",
        ],
    },
    {
        "name": "ai-for-ai-safety",
        "title": "AI for AI Safety",
        "description": "Use alignment, red teaming, interpretability, and monitoring to reduce harmful or unintended AI behavior.",
        "devin_body": r'''
## When to use

You are training, aligning, evaluating, or deploying an AI system and want to reduce harmful, unintended, or adversarial behavior before and after release.

## Usage

- Align models with RLHF, RLAIF, DPO, Constitutional AI, and preference learning.
- Red-team for jailbreaks, adversarial behavior, and safety benchmark failures.
- Interpret representations with activation probes and concept-based explanations.
- Monitor behavior and detect anomalies in deployment.
- Provide scalable oversight for tasks where human evaluation is expensive.

## Steps

1. Define the safety properties and adversarial evaluation set.
2. Run red teaming with diverse, multilingual, and multi-turn attacks.
3. Apply an alignment or preference-learning method and measure safety vs. capability.
4. Use interpretability tools to inspect harmful concepts and steering.
5. Implement behavioral monitoring and anomaly detection.
6. Iterate with human review, incident-response playbooks, and deployment gating.

## Code pattern

```python
import torch

# Lightweight activation-probe-style safety monitor
class SafetyProbe(torch.nn.Module):
    def __init__(self, hidden_dim):
        super().__init__()
        self.head = torch.nn.Linear(hidden_dim, 1)

    def forward(self, hidden_states):
        return torch.sigmoid(self.head(hidden_states[:, -1, :]))

probe = SafetyProbe(hidden_dim=4096)
# train on safe/unsafe activation pairs ...
```

## Tuning notes

- Safety and capability can trade off; measure both on held-out adversarial sets.
- Red-team with diverse, multilingual, and multi-turn attacks, not just static prompts.
- Use interpretability cautiously; it can also enable steering attacks.
- Pair automated evaluation with human review and incident-response playbooks.

## Verification

1. Run an automated red-team benchmark and report attack success rate before and after mitigations.
2. Train or evaluate an alignment method (e.g., DPO) on a preference dataset.
3. Inspect model activations for a harmful concept and compare to a benign baseline.
        ''',
        "references": [
            "https://arxiv.org/abs/2310.19852",
            "https://arxiv.org/abs/2604.20945",
            "https://arxiv.org/abs/2404.12038",
            "https://arxiv.org/abs/2603.06727",
        ],
    },
    {
        "name": "ai-for-ai-policy",
        "title": "AI for AI Policy",
        "description": "Use regulatory analysis, risk classification, and standards mapping to inform AI policy and compliance.",
        "devin_body": r'''
## When to use

You are advising or developing AI policy, mapping regulations to technical requirements, or evaluating how a law or standard affects an AI system or market.

## Usage

- Classify AI systems by risk tier and map obligations (e.g., EU AI Act).
- Compare policy instruments: hard law, soft law, standards, sandboxes, procurement.
- Track regulatory learning and iterative updates as technology evolves.
- Align international standards (OECD, ISO) and cross-border requirements.
- Evaluate ex-ante and ex-post policy impacts.

## Steps

1. Identify the AI system, jurisdiction, and relevant legal and standards landscape.
2. Map features and risk tier to specific obligations and technical requirements.
3. Translate legal terms into verifiable engineering checks (data quality, logging, oversight).
4. Compare national or regional strategies for convergence and divergence.
5. Produce a policy brief with concrete technical and governance measures.
6. Track regulatory changes and update compliance mapping.

## Code pattern

```python
import pandas as pd

# Map system features to risk categories and obligations
systems = pd.DataFrame({
    "system": ["recruiting_tool", "chatbot", "medical_imaging"],
    "risk_tier": ["high", "limited", "high"],
    "obligation": ["conformity", "transparency", "conformity"],
})
compliance_matrix = systems.groupby(["risk_tier", "obligation"]).size().unstack(fill_value=0)
print(compliance_matrix)
```

## Tuning notes

- Translate legal terms into verifiable technical requirements (data quality, human oversight, logging).
- Track regulatory changes across jurisdictions; AI policy is evolving rapidly.
- Involve technologists, legal experts, and civil society in policy design.
- Evaluate policies for innovation effects, not just risk reduction.

## Verification

1. Map the EU AI Act obligations for a candidate high-risk AI system.
2. Compare national AI strategies across at least three jurisdictions for convergence and divergence.
3. Produce a policy brief with technical requirements derived from a regulation or standard.
        ''',
        "references": [
            "https://arxiv.org/pdf/2409.00264",
            "https://arxiv.org/abs/2503.05787",
            "https://arxiv.org/abs/2307.12218",
            "https://arxiv.org/pdf/2407.21717",
        ],
    },
    {
        "name": "ai-for-responsible-innovation",
        "title": "AI for Responsible Innovation",
        "description": "Use anticipatory governance, stakeholder engagement, and impact assessment to steer emerging AI technologies responsibly.",
        "devin_body": r'''
## When to use

You are developing or steering a novel AI technology and want to anticipate social, ethical, and regulatory impacts early and embed responsible practices into R&D.

## Usage

- Conduct foresight, horizon scanning, and scenario planning.
- Apply responsible research and innovation principles (inclusivity, anticipation, reflexivity, responsiveness).
- Engage the public and stakeholders through deliberative forums and co-design.
- Run regulatory sandboxes and adaptive governance experiments.
- Assess societal, environmental, and human-rights impacts.

## Steps

1. Identify the emerging technology and its possible societal implications.
2. Run horizon scanning and develop scenarios with diverse stakeholders.
3. Map stakeholders, risks, and responsible-innovation actions.
4. Design a sandbox, pilot, or stakeholder deliberation to test assumptions.
5. Evaluate impacts and document trade-offs and uncertainties.
6. Iterate governance and R&D as impacts become clearer.

## Code pattern

```python
import pandas as pd

# Stakeholder-action mapping for responsible innovation
actions = pd.DataFrame([
    {"stakeholder": "researchers", "action": "pre-publish risk assessment", "priority": 1},
    {"stakeholder": "regulators", "action": "adaptive sandbox", "priority": 2},
    {"stakeholder": "public", "action": "deliberative consultation", "priority": 1},
])
print(actions.sort_values("priority"))
```

## Tuning notes

- Start early: anticipatory governance is cheaper and more effective before deployment.
- Combine quantitative impact modeling with qualitative stakeholder deliberation.
- Design feedback loops so governance can adapt as impacts become clearer.
- Document trade-offs and uncertainty; responsible innovation is iterative.

## Verification

1. Conduct a scenario-planning workshop for an emerging AI application and document key uncertainties.
2. Map stakeholders, risks, and mitigation actions for a technology launch.
3. Evaluate a regulatory sandbox proposal against responsible-innovation criteria.
        ''',
        "references": [
            "https://arxiv.org/pdf/2501.05921",
            "https://arxiv.org/abs/2502.14869",
            "https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/steering-ai-s-future_70e4a856/5480ff0a-en.pdf",
            "https://arxiv.org/abs/2406.04554",
        ],
    },
    {
        "name": "ai-for-tech-forecasting",
        "title": "AI for Tech Forecasting",
        "description": "Use patents, publications, funding, and expert judgment to forecast technological progress and emerging capabilities.",
        "devin_body": r'''
## When to use

You want to predict the pace, direction, or feasibility of technological progress to guide R&D investment, policy, or safety planning.

## Usage

- Collect patents, papers, funding, product releases, and expert surveys.
- Model S-curves, ARIMA, autoencoders, and transformer-based technology trends.
- Discover technological convergence and opportunities with topic and link models.
- Aggregate expert judgment with Delphi and structured elicitation.
- Evaluate forecasts with Brier scores and calibration over horizons.

## Steps

1. Define the technology, metric, and forecasting horizon.
2. Gather historical data (patents, papers, funding, product releases) and expert judgments.
3. Train or fit trend, topic, or link-prediction models.
4. Backtest on held-out time periods and avoid look-ahead bias.
5. Combine model and expert forecasts and report uncertainty scenarios.
6. Update regularly as new signals and events emerge.

## Code pattern

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Simple trend extrapolation of a technology metric
years = np.array([[2015], [2018], [2021], [2024]])
metric = np.array([0.2, 0.4, 0.65, 0.85])  # e.g., capability score

model = LinearRegression().fit(years, metric)
future_years = np.array([[2027], [2030]])
print("Forecasts:", model.predict(future_years))
```

## Tuning notes

- Combine quantitative signals with domain expertise; neither is sufficient alone.
- Distinguish capability trends from adoption and diffusion curves.
- Use holdout time periods and avoid look-ahead bias in feature construction.
- Report uncertainty and scenarios, not just point estimates.

## Verification

1. Build a model to forecast a technology metric and backtest on historical data.
2. Use patent topic modeling to identify emerging technology combinations.
3. Compare an ML forecast to expert elicitation on a set of concrete questions.
        ''',
        "references": [
            "https://arxiv.org/abs/2605.22681",
            "https://arxiv.org/pdf/2008.01848",
            "https://arxiv.org/abs/2605.04875",
            "https://arxiv.org/abs/2211.15334",
        ],
    },
    {
        "name": "ai-for-future-of-work",
        "title": "AI for Future of Work",
        "description": "Use AI exposure and skill-demand analysis to understand workforce transitions and support human-centered labor policy.",
        "devin_body": r'''
## When to use

You are analyzing how AI changes occupations, tasks, hiring, productivity, job quality, or workforce skills and designing policy or organizational responses.

## Usage

- Estimate task-level automation and augmentation potential.
- Model skill demand, reskilling, upskilling, and occupational mobility.
- Analyze algorithmic management in scheduling, monitoring, and evaluation.
- Assess job quality, wages, equity, and worker voice.
- Co-design labor policy with workers and social partners.

## Steps

1. Collect task-level occupational data and identify AI-exposed tasks.
2. Build or use an AI-exposure scoring model and validate against expert labels.
3. Model task reallocation, reskilling needs, and occupational mobility.
4. Pilot an AI tool and measure effects on task time, output, and job quality.
5. Engage workers and unions in co-designing transitions and safeguards.
6. Evaluate outcomes and adjust policy or organizational responses.

## Code pattern

```python
import pandas as pd

# Compute a simple AI-exposure score from task-level data
tasks = pd.DataFrame({
    "task": ["data entry", "client negotiation", "code review"],
    "ai_exposure": [0.9, 0.2, 0.7],
    "importance": [0.3, 0.4, 0.3],
})
job_exposure = (tasks["ai_exposure"] * tasks["importance"]).sum()
print("Job-level AI exposure:", job_exposure)
```

## Tuning notes

- Use task-level data rather than crude occupation-level automation probabilities.
- Distinguish automation (replacement) from augmentation (complementarity).
- Measure job quality, not only employment levels.
- Engage workers and social partners in designing transitions.

## Verification

1. Compute AI-exposure scores for a set of occupations and compare to official estimates.
2. Model the effect of an AI tool on task time and output quality with a pilot study.
3. Evaluate a reskilling program by tracking job placement and wage outcomes.
        ''',
        "references": [
            "https://www.oecd.org/en/topics/future-of-work.html",
            "https://oecd.ai/en/working-group-future-of-work",
            "https://www.ilo.org/observatory-ai-and-work-digital-economy",
            "https://webapps.ilo.org/static/english/intserv/working-papers/wp096/index.html",
        ],
    },
    {
        "name": "ai-for-digital-twin-simulation",
        "title": "AI for Digital Twin Simulation",
        "description": "Use physics-informed and data-driven simulation to build digital twins of physical assets, processes, and environments.",
        "devin_body": r'''
## When to use

You are building a virtual replica of a physical asset, process, or environment to monitor, simulate, optimize, or train AI agents before real-world deployment.

## Usage

- Mirror physical assets with ISO 23247 architecture and IoT data pipelines.
- Synchronize real-time state with sensor fusion and state estimation.
- Combine first-principle models with ML surrogates.
- Train and test AI agents safely in virtual replicas.
- Support predictive maintenance, what-if analysis, and closed-loop control.

## Steps

1. Define the physical asset, process, or environment and the twin's purpose.
2. Build a physics-based or data-driven model and connect live sensor streams.
3. Train ML surrogates for computationally expensive sub-models.
4. Validate the twin continuously against real measurements and detect drift.
5. Run what-if scenarios, optimize control, or train RL agents in the twin.
6. Deploy closed-loop control with safety limits and update the twin over its lifecycle.

## Code pattern

```python
import numpy as np

# Simple digital-twin state update with a learned surrogate
def twin_step(state, control, dt, surrogate):
    return state + dt * surrogate(state, control)

state = np.array([1.0, 0.0])
control = np.array([0.1])
for t in range(100):
    state = twin_step(state, control, 0.01, learned_model)
```

## Tuning notes

- Validate the twin against real data continuously; model drift can invalidate decisions.
- Balance fidelity with latency and computational cost.
- Use standardized interfaces and semantic descriptions for interoperability.
- Ensure safety when the twin controls the physical asset.

## Verification

1. Build a digital twin of a production line and compare predicted KPIs to actual measurements.
2. Train an RL agent in the twin and transfer the policy to the physical system.
3. Run what-if scenarios and stress tests to assess resilience to disruptions.
        ''',
        "references": [
            "https://arxiv.org/abs/2506.06580",
            "https://arxiv.org/abs/2601.01321",
            "https://arxiv.org/abs/2511.03742",
            "https://arxiv.org/abs/2301.13350",
        ],
    },
]