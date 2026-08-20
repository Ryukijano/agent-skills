SKILLS = [
    {
        "name": "explainable-ai",
        "title": "Explainable AI (XAI)",
        "description": "Feature attribution, concept-based explanations, saliency maps, and interpretability for black-box models.",
        "devin_body": r'''
## When to use

You need to explain why a model made a particular prediction to users, regulators, or domain experts.

## Key concepts

- **Feature attribution**: SHAP, LIME, Integrated Gradients, permutation importance.
- **Saliency maps**: Grad-CAM, SmoothGrad, attention visualization.
- **Concept-based explanations**: TCAV, concept activation vectors.
- **Global vs local**: explanations for single instances or model behavior overall.

## Code pattern

```python
import shap
import xgboost as xgb

model = xgb.XGBClassifier().fit(X_train, y_train)
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

## Tuning notes

- Explanations must be faithful to the model, not just plausible.
- Be cautious with correlated features; attribution can be unstable.
- Use multiple explanation methods and compare them.

## Verification

1. Explain a model on a tabular dataset and compare SHAP and LIME.
2. Generate Grad-CAM maps for an image classifier and sanity-check.
3. Measure explanation stability under small input perturbations.
''',
        "references": [
            "https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202400304",
            "https://arxiv.org/abs/2503.24365",
            "https://www.nature.com/articles/s41598-025-25839-y",
            "https://christophm.github.io/interpretable-ml-book/"
        ],
    },
    {
        "name": "ai-fairness",
        "title": "Fairness in Machine Learning",
        "description": "Detect, measure, and mitigate bias across demographic groups in classification, ranking, and regression.",
        "devin_body": r'''
## When to use

You are concerned that model predictions may be unfair to individuals or groups defined by protected attributes.

## Key concepts

- **Fairness criteria**: demographic parity, equalized odds, calibration.
- **Disparate impact**: statistical evidence of differential treatment.
- **Bias mitigation**: pre-processing, in-processing, post-processing.
- **Intersectionality**: fairness across combinations of protected attributes.

## Code pattern

```python
from aif360.sklearn.metrics import disparate_impact_ratio
from aif360.sklearn.inprocessing import AdversarialDebiasing

ratio = disparate_impact_ratio(y_true, y_pred, prot_attr='gender')
print(ratio)
```

## Tuning notes

- Choose a fairness criterion grounded in the deployment context.
- Fairness often conflicts with accuracy; document trade-offs.
- Test across subgroups and intersectional groups.

## Verification

1. Compute demographic parity and equalized odds on a dataset.
2. Apply a debiasing method and re-measure fairness metrics.
3. Evaluate whether accuracy drops disproportionately for any group.
''',
        "references": [
            "https://arxiv.org/abs/2406.06330",
            "https://aif360.res.ibm.com/",
            "https://fairlearn.org/",
            "https://arxiv.org/abs/2402.08662"
        ],
    },
    {
        "name": "privacy-preserving-ml",
        "title": "Privacy-Preserving Machine Learning",
        "description": "Differential privacy, federated learning, homomorphic encryption, and secure multi-party computation for ML.",
        "devin_body": r'''
## When to use

You are training or deploying models on sensitive data and must protect individual privacy.

## Key concepts

- **Differential privacy**: randomized mechanisms with formal privacy budgets.
- **Federated learning**: train across decentralized data without centralization.
- **Homomorphic encryption / MPC**: compute on encrypted data.
- **Synthetic data**: generate privacy-safe training data.

## Code pattern

```python
import tensorflow_privacy as tfp
from tensorflow_privacy.privacy.optimizers.dp_optimizer import DPKerasSGDOptimizer

optimizer = DPKerasSGDOptimizer(
    l2_norm_clip=1.0,
    noise_multiplier=0.8,
    num_microbatches=1,
    learning_rate=0.01
)
```

## Tuning notes

- Balance privacy budget with model utility; smaller epsilon, larger noise.
- Federated learning protects data in transit but does not guarantee privacy alone.
- Consider threat models and linkability attacks.

## Verification

1. Train a model with DP-SGD and report (epsilon, delta) for a fixed accuracy.
2. Run a membership-inference attack on a standard and a private model.
3. Implement a federated averaging loop on a partitioned dataset.
''',
        "references": [
            "https://arxiv.org/abs/2508.13730",
            "https://www.oecd.org/publications/sharing-trustworthy-ai-models-with-privacy-enhancing-technologies_5df6fd05",
            "https://tensorflow.github.io/compliance/privacy/",
            "https://opacus.ai/"
        ],
    },
    {
        "name": "federated-learning",
        "title": "Federated Learning",
        "description": "Decentralized model training across clients, handling non-IID data, aggregation, and personalization.",
        "devin_body": r'''
## When to use

You need to train a model on data that is distributed across devices, hospitals, or institutions.

## Key concepts

- **Horizontal vs vertical FL**: same features across clients vs different feature sets.
- **FedAvg**: average client model updates weighted by data size.
- **Non-IID challenges**: client drift, pathological data distributions.
- **Personalization**: per-client or cluster-specific model heads.

## Code pattern

```python
import flower as fl

# Define a simple FedAvg server
strategy = fl.server.strategy.FedAvg(
    fraction_fit=0.5,
    min_available_clients=5,
)
fl.server.start_server(server_address="0.0.0.0:8080", strategy=strategy)
```

## Tuning notes

- Use secure aggregation for privacy-sensitive gradients.
- Adjust local epochs and learning rate to control client drift.
- Monitor per-client metrics, not just global loss.

## Verification

1. Partition a dataset into non-IID clients and run FedAvg.
2. Compare centralized and federated test accuracy.
3. Evaluate a personalized FL method on a heterogeneous client set.
''',
        "references": [
            "https://arxiv.org/abs/2511.22616",
            "https://flower.ai/",
            "https://github.com/google-research/federated",
            "https://arxiv.org/abs/2507.15796"
        ],
    },
    {
        "name": "active-learning",
        "title": "Active Learning",
        "description": "Iteratively select the most informative unlabeled data points for efficient annotation and model improvement.",
        "devin_body": r'''
## When to use

You have a large pool of unlabeled data and limited labeling budget.

## Key concepts

- **Uncertainty sampling**: query points the model is least confident about.
- **Diversity sampling**: cover different regions of the data distribution.
- **Expected model change**: query points that would most change the model.
- **Pool-based vs stream-based**: select from a fixed pool or online.

## Code pattern

```python
import numpy as np

# Uncertainty sampling: pick points with lowest max probability
probs = model.predict_proba(X_pool)
uncertainty = 1 - np.max(probs, axis=1)
query_idx = np.argsort(uncertainty)[-k:]
```

## Tuning notes

- Combine uncertainty and diversity to avoid outliers.
- Re-train the model after each query batch.
- Track learning curves versus random sampling as a baseline.

## Verification

1. Implement uncertainty sampling on a text or image dataset.
2. Plot model accuracy versus number of labeled samples.
3. Compare uncertainty, diversity, and random acquisition strategies.
''',
        "references": [
            "https://aclanthology.org/2025.acl-long.708/",
            "https://arxiv.org/abs/2405.00334",
            "https://modal-python.readthedocs.io/",
            "https://github.com/google-research/google-research/tree/master/active_learning"
        ],
    },
    {
        "name": "meta-learning",
        "title": "Meta-Learning",
        "description": "Learn-to-learn methods such as MAML, metric learning, and neural processes for fast adaptation.",
        "devin_body": r'''
## When to use

You need a model that adapts to new tasks with only a few examples.

## Key concepts

- **Optimization-based**: MAML, iMAML, Reptile.
- **Metric-based**: Prototypical Networks, Matching Networks, Siamese networks.
- **Model-based**: Neural Turing Machines, LSTM meta-learners, Neural Processes.
- **Task distribution**: meta-train and meta-test on separate tasks.

## Code pattern

```python
import learn2learn as l2l

maml = l2l.algorithms.MAML(model, lr=0.01, first_order=False)
for task in tasks:
    # Inner loop adaptation
    learner = maml.clone()
    for _ in range(5):
        train_error = loss(learner(X_train), y_train)
        learner.adapt(train_error)
```

## Tuning notes

- Meta-learning can overfit to the meta-train task distribution.
- Second-order MAML is expensive; first-order methods are common.
- Use proper task sampling to ensure diversity.

## Verification

1. Train MAML on a few-shot image classification benchmark.
2. Adapt the model to a held-out class with 5 examples.
3. Compare meta-learned initialization to pretrained + fine-tuning.
''',
        "references": [
            "https://arxiv.org/abs/2402.03017",
            "https://github.com/learn2learn/",
            "https://arxiv.org/abs/1703.03400",
            "https://arxiv.org/abs/1707.03141"
        ],
    },
    {
        "name": "few-shot-learning",
        "title": "Few-Shot Learning",
        "description": "Learning from a handful of labeled examples through meta-learning, prompt tuning, and data augmentation.",
        "devin_body": r'''
## When to use

You have only a few labeled examples per class and need strong generalization.

## Key concepts

- **k-shot, N-way**: few examples and many classes.
- **Prototypical / matching networks**: compare embeddings to class prototypes.
- **In-context learning**: prompt LLMs with examples.
- **Augmentation and self-supervised pretraining**: generate more signal from few labels.

## Code pattern

```python
import torch
import torch.nn.functional as F

# Prototypical network: compute class prototypes and classify by distance
prototypes = torch.stack([support[labels == c].mean(0) for c in classes])
logits = -torch.cdist(query, prototypes)
```

## Tuning notes

- Pretrain on a related large dataset before few-shot adaptation.
- Metric scaling and temperature affect performance.
- Use data augmentation and prompt engineering when labels are scarce.

## Verification

1. Train a prototypical network on Omniglot or miniImageNet.
2. Evaluate 5-way 1-shot and 5-way 5-shot accuracy.
3. Compare with a fine-tuned baseline using the same shots.
''',
        "references": [
            "https://arxiv.org/abs/2402.03017",
            "https://github.com/orobix/Prototypical-Networks-for-Few-shot-Learning-PyTorch",
            "https://arxiv.org/abs/1703.05175",
            "https://huggingface.co/docs/transformers/tasks/prompting"
        ],
    },
    {
        "name": "curriculum-learning",
        "title": "Curriculum Learning",
        "description": "Order training examples from easy to hard to improve convergence and generalization.",
        "devin_body": r'''
## When to use

You want to speed up training or improve generalization by presenting examples in a meaningful order.

## Key concepts

- **Difficulty score**: loss, length, noise, or expert-defined difficulty.
- **Pacing functions**: control how fast the curriculum mixes hard examples.
- **Self-paced learning**: the curriculum is derived from the model's own loss.
- **Transfer curricula**: reuse difficulty metrics from a related task.

## Code pattern

```python
def curriculum_sampler(epoch, dataset, difficulties):
    # Increase the threshold for including harder examples over time
    threshold = min(1.0, epoch / 10)
    indices = [i for i, d in enumerate(difficulties) if d <= threshold]
    return torch.utils.data.Subset(dataset, indices)
```

## Tuning notes

- Define difficulty carefully; a bad curriculum can hurt.
- Combine with standard shuffling to avoid overfitting to easy data.
- Monitor whether hard examples improve final metrics, not just speed.

## Verification

1. Train a model with and without a curriculum on the same data.
2. Define a difficulty measure and plot its correlation with loss.
3. Compare final test accuracy and convergence time.
''',
        "references": [
            "https://arxiv.org/abs/2004.11101",
            "https://huggingface.co/docs/transformers/training",
            "https://github.com/terryum/curriculum_learning",
            "https://arxiv.org/abs/1806.06044"
        ],
    },
    {
        "name": "domain-adaptation",
        "title": "Domain Adaptation",
        "description": "Transfer knowledge from a labeled source domain to an unlabeled or partially labeled target domain.",
        "devin_body": r'''
## When to use

You have labeled data in one domain but need to deploy in a different but related domain.

## Key concepts

- **Covariate shift vs concept drift**: input or label distribution differences.
- **Feature alignment**: minimize distribution distance (MMD, adversarial).
- **Self-training / pseudo-labeling**: label target data with a source model.
- **Domain randomization**: train on diverse synthetic domains.

## Code pattern

```python
import torch
import torch.nn as nn

# Adversarial domain adaptation: gradient reversal on domain classifier
class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, alpha):
        ctx.alpha = alpha
        return x.view_as(x)

    @staticmethod
    def backward(ctx, grad_output):
        return -ctx.alpha * grad_output, None
```

## Tuning notes

- Match feature extractors across domains before the classifier.
- Pseudo-label quality matters; use confident predictions and iterative refinement.
- Consider domain-specific batch normalization.

## Verification

1. Train a source model on MNIST and adapt to USPS or SVHN.
2. Compare target accuracy of source-only, fine-tuning, and adversarial adaptation.
3. Visualize source and target feature distributions before/after alignment.
''',
        "references": [
            "https://arxiv.org/abs/2302.02627",
            "https://github.com/thuml/Xlearn",
            "https://arxiv.org/abs/1505.07818",
            "https://adapt.readthedocs.io/"
        ],
    },
    {
        "name": "model-interpretability",
        "title": "Model Interpretability",
        "description": "Intrinsic and post-hoc methods for understanding model behavior, features, and decision boundaries.",
        "devin_body": r'''
## When to use

You need to understand which inputs, features, or concepts drive model decisions.

## Key concepts

- **Intrinsic interpretability**: decision trees, linear models, attention weights.
- **Post-hoc explanation**: SHAP, LIME, counterfactuals, prototypes.
- **Feature interactions**: H-statistics, partial dependence, ICE curves.
- **Concept-based methods**: TCAV, concept bottleneck models.

## Code pattern

```python
from sklearn.inspection import partial_dependence

result = partial_dependence(model, X, features=[0])
pd_values = result["average"]
```

## Tuning notes

- Simpler models are easier to interpret but may be less accurate.
- Post-hoc explanations can be unstable; test on multiple samples.
- Explainability needs differ by stakeholder.

## Verification

1. Train a decision tree and an MLP on the same tabular task; compare performance and interpretability.
2. Compute partial dependence for the top two features.
3. Generate counterfactual explanations for a few instances.
''',
        "references": [
            "https://link.springer.com/article/10.1007/s10994-025-06852-8",
            "https://arxiv.org/abs/2506.06330",
            "https://christophm.github.io/interpretable-ml-book/",
            "https://github.com/tensorflow/tcav"
        ],
    },
    {
        "name": "robust-ml",
        "title": "Robust Machine Learning",
        "description": "Adversarial robustness, distribution shift, out-of-distribution detection, and reliable model performance.",
        "devin_body": r'''
## When to use

Your model must perform reliably under adversarial attacks, distribution shift, or noisy inputs.

## Key concepts

- **Adversarial training**: augment training with adversarial examples.
- **Robust optimization**: minimize worst-case loss.
- **Out-of-distribution (OOD) detection**: identify inputs far from training data.
- **Certified defenses**: provable robustness bounds.

## Code pattern

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Fast gradient sign method (FGSM) for adversarial training
x_adv = x + epsilon * torch.sign(x.grad)
```

## Tuning notes

- Adversarial training improves robustness at the cost of clean accuracy.
- OOD detection should be calibrated on a representative out-distribution.
- Certified methods are expensive; use for small or safety-critical models.

## Verification

1. Run a simple FGSM or PGD attack on a trained image classifier.
2. Evaluate accuracy on a distribution-shifted test set.
3. Implement an OOD detector and compute AUROC on in/out data.
''',
        "references": [
            "https://arxiv.org/abs/2408.06132",
            "https://madry-lab.github.io/",
            "https://github.com/MadryLab/robustness",
            "https://arxiv.org/abs/2106.03098"
        ],
    },
    {
        "name": "uncertainty-quantification-ml",
        "title": "Uncertainty Quantification in ML",
        "description": "Predictive uncertainty, calibration, conformal prediction, and Bayesian methods for reliable ML.",
        "devin_body": r'''
## When to use

You need to estimate and communicate the uncertainty of model predictions.

## Key concepts

- **Aleatoric vs epistemic uncertainty**: data noise vs model uncertainty.
- **Calibration**: match predicted confidence with observed accuracy.
- **Conformal prediction**: distribution-free prediction sets with coverage guarantees.
- **Bayesian methods**: MC dropout, variational inference, deep ensembles.

## Code pattern

```python
import numpy as np

# Conformal prediction: construct a prediction set
n = len(y_cal)
scores = 1 - proba_cal[y_cal]
q = np.quantile(scores, np.ceil((n+1)*(1-alpha))/n, method='higher')
```

## Tuning notes

- Ensembles often provide the best uncertainty estimates.
- Temperature scaling can fix overconfidence.
- Conformal prediction requires an exchangeable calibration set.

## Verification

1. Train an ensemble and measure prediction uncertainty on a held-out set.
2. Apply temperature scaling and check expected calibration error (ECE).
3. Build conformal prediction sets and verify coverage on test data.
''',
        "references": [
            "https://arxiv.org/abs/2404.02678",
            "https://github.com/uncertainty-toolbox/uncertainty-toolbox",
            "https://arxiv.org/abs/2005.14137",
            "https://arxiv.org/abs/2107.07511"
        ],
    },
]
