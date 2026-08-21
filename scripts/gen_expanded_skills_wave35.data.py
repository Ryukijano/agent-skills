SKILLS = [
    {
        "name": "ai-for-computational-complexity",
        "title": "AI for Computational Complexity",
        "description": "Use machine learning to predict solver runtime, characterize complexity classes, and learn hardness proxies for computational problems.",
        "devin_body": r'''
## When to use

You want to estimate the difficulty of an algorithmic or combinatorial problem, predict solver runtime, or learn hardness proxies for reductions and complexity classes.

## Usage

- Predict solver runtime and average-case hardness for SAT/MIP/SMT instances from structural features.
- Characterize complexity classes and reductions, including P, NP, fine-grained, and parameterized frameworks.
- Model hardness proxies such as statistical-query lower bounds, low-degree likelihood ratios, and the Franz–Parisi criterion.
- Generate data-driven conjectures about phase transitions and average-case hardness boundaries.

## Steps

1. Collect or generate problem instances and extract features such as clause/variable ratio, graph metrics, and symmetry.
2. Train regressors or classifiers to predict solver runtime, satisfiability, or a hardness proxy.
3. Use the model to rank instances or select solver configurations for a target distribution.
4. Compare learned predictions with theoretical hardness proxies and worst-case bounds.
5. Deploy the best predictor inside a solver toolchain and monitor for distribution shift.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# instance features: n_vars, n_clauses, clause/variable ratio, graph metrics
X = np.array([[100, 420, 4.2, 0.35], [500, 2100, 4.2, 0.32], ...])
y = np.array([0.12, 1.4, ...])  # solver runtime in seconds

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = GradientBoostingRegressor(random_state=42).fit(X_train, y_train)
print("MAE:", np.mean(np.abs(model.predict(X_test) - y_test)))
```

## Tuning notes

- Use instance features that capture structure, not just size.
- Compare predicted runtimes against classical worst-case bounds.
- Watch for distribution shift when generalizing across problem families.

## Verification

1. Train a runtime predictor on a set of SAT/MIP instances and evaluate with time-based splits.
2. Plot predicted vs. actual runtimes and identify systematic underestimation on hard instances.
3. Compare the learned ranking of instances to a theoretical hardness proxy.
        ''',
        "references": [
            "https://doi.org/10.1088/1742-5468/ad3a5b",
            "https://plato.stanford.edu/entries/computational-complexity/",
            "https://doi.org/10.48550/arxiv.2103.05127",
            "https://cacm.acm.org/research/fifty-years-of-p-vs-np-and-the-possibility-of-the-impossible/",
            "https://link.springer.com/article/10.1007/s10208-023-09607-w",
        ],
    },
    {
        "name": "ai-for-algorithms",
        "title": "AI for Algorithms",
        "description": "Use machine learning to augment classic algorithms with learned predictions, indexes, and data structures.",
        "devin_body": r'''
## When to use

You want to improve classic algorithms with machine-learned predictions, design learned indexes or data structures, or tune algorithmic decisions on a distribution of instances.

## Usage

- Build learning-augmented algorithms that take ML predictions as advice while retaining worst-case guarantees.
- Replace or augment B-trees, Bloom filters, and sketches with learned indexes and data structures.
- Select and configure solvers, sorters, or search algorithms based on instance features.
- Prove competitive or approximation ratios that degrade gracefully with prediction error.

## Steps

1. Identify the algorithmic decision (caching, indexing, search, or routing) to enhance and collect instance features.
2. Train a lightweight predictor on historical instances to provide advice for that decision.
3. Design the algorithm to incorporate predictions while bounding worst-case cost when predictions are poor.
4. Benchmark the learning-augmented method against the classical worst-case baseline on held-out distributions.
5. Validate on adversarial or pathological inputs and tune the reliance on predictions.
6. Deploy as a drop-in replacement or wrapper and monitor performance on production traffic.

## Code pattern

```python
import numpy as np
from sklearn.linear_model import Ridge

# Predicted next request in a caching/paging problem
X = np.array([[1, 0, 1], [0, 1, 0], ...])  # recent access patterns
y = np.array([2, 0, ...])                   # next accessed item

predictor = Ridge().fit(X, y)

def learned_paging_predict(cache, request):
    scores = predictor.predict([request])
    return int(np.argmax(scores))
```

## Tuning notes

- Start with strong classical baselines and measure incremental lift.
- Use held-out instance distributions that differ from training.
- Validate worst-case behavior on adversarial or pathological inputs.

## Verification

1. Implement a learned Bloom filter and compare false-positive rate to a standard Bloom filter.
2. Train a learned index on integer keys and measure query latency vs. space.
3. Benchmark a learning-augmented algorithm against the prediction-free worst-case baseline.
        ''',
        "references": [
            "https://arxiv.org/abs/2006.09123",
            "https://cacm.acm.org/opinion/algorithms-with-predictions/",
            "https://arpi.unipi.it/bitstream/11568/1038818/1/BookChapter__Learned_data_structures.pdf",
            "http://theory.stanford.edu/~sergei/slides/HALG-slides.pdf",
            "https://proceedings.neurips.cc/paper_files/paper/2024/file/2db08b94565c0d582cc53de6cee5fd47-Paper-Conference.pdf",
        ],
    },
    {
        "name": "ai-for-formal-methods",
        "title": "AI for Formal Methods",
        "description": "Use machine learning and LLMs to translate informal specifications into formal models and guide theorem provers and model checkers.",
        "devin_body": r'''
## When to use

You want to translate informal specifications into formal models, guide proof search, or apply ML to model checking, program verification, and certified systems.

## Usage

- Autoformalize natural-language or code specifications into formal logic using LLMs and domain-tuned models.
- Combine neural guidance with SAT/SMT/TLA+ solvers and model checkers for neuro-symbolic verification.
- Predict the next proof step, relevant premises, and useful tactics from the current proof state.
- Discover loop invariants and safety certificates from data and program structure.

## Steps

1. Collect a corpus of informal specifications, code, and corresponding formal models for the target domain.
2. Train or prompt an LLM to autoformalize specifications and validate outputs with a trusted checker.
3. Build a premise selector or tactic predictor from a proof corpus and integrate it with the proof assistant.
4. Run model-checking or verification tasks with learned guidance and compare proof search effort.
5. Use the system to synthesize invariants or certificates for safety-critical programs.
6. Iterate with human experts to correct formalizations and maintain soundness guarantees.

## Code pattern

```python
# Autoformalization sketch using an LLM and a proof checker
from transformers import pipeline

formalizer = pipeline("text2text-generation", model="t5-formalizer")

spec = "The array is sorted in non-decreasing order."
formal = formalizer(f"formalize: {spec}")[0]["generated_text"]
print(formal)

# Proof guidance with a learned premise ranker
premises = ["le_refl", "le_trans", "sorted_def"]
scores = predictor.predict(premises)  # trained on proof corpora
best = premises[int(np.argmax(scores))]
```

## Tuning notes

- Always verify LLM output with a trusted proof assistant or solver.
- Use smaller, domain-tuned models for autoformalization to reduce hallucination.
- Distinguish between sound automation and heuristic guidance.

## Verification

1. Formalize a small English specification and check it in a proof assistant.
2. Train a premise selector on a proof corpus and measure recall of used lemmas.
3. Compare a model-guided proof search to an unguided baseline on a benchmark.
        ''',
        "references": [
            "https://doi.org/10.1007/s10664-025-10729-8",
            "https://doi.org/10.48550/arxiv.2404.09939",
            "https://aclanthology.org/2026.bigpicture-main.1/",
            "https://arxiv.org/abs/2606.08728v4",
            "https://doi.org/10.48550/arxiv.2403.04017",
        ],
    },
    {
        "name": "ai-for-program-synthesis",
        "title": "AI for Program Synthesis",
        "description": "Generate executable programs from natural-language descriptions or input-output examples for non-expert users and new APIs.",
        "devin_body": r'''
## When to use

You want to generate programs from examples, partial sketches, or natural language, or combine symbolic search with neural models for reliable code generation.

## Usage

- Synthesize programs consistent with input-output examples using programming by example (PBE).
- Generate code from natural-language specifications or partial sketches with transformer models.
- Combine symbolic search, constraint solving, and neural priors for reliable synthesis.
- Fill holes in user-provided program templates while satisfying types and constraints.

## Steps

1. Collect input-output examples, sketches, or natural-language specifications for the target program.
2. Choose a synthesis approach: enumerative search, constraint solving, LLM generation, or neurosymbolic search.
3. Train or prompt the model with few-shot examples and constrain output with a grammar or type system.
4. Filter candidates by executing tests and, where possible, verifying them with a symbolic checker.
5. Measure pass@k and compare the synthesizer to a human-written or symbolic baseline.
6. Integrate the synthesis loop into an IDE, API, or code-generation assistant.

## Code pattern

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("codellama/CodeLlama-7b-hf")
tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-hf")

prompt = "# Python function that returns the sum of even numbers in a list\ndef sum_evens(lst):\n    "
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=64)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Tuning notes

- Constrain generation with a grammar or type system to improve correctness.
- Filter candidates with test-case execution and a symbolic verifier.
- Use few-shot examples that match the target domain and style.

## Verification

1. Synthesize a program from a small set of input-output examples and run it on hidden tests.
2. Compare a neural synthesizer against an enumerative synthesizer on the same benchmark.
3. Measure pass@k on a program-synthesis dataset (e.g., HumanEval, APPS, SyGuS).
        ''',
        "references": [
            "https://www.cs.utexas.edu/~swarat/pubs/ns-handbook-2025.pdf",
            "https://doi.org/10.1117/12.3011627",
            "https://www.mdpi.com/2078-2489/16/5/401",
            "https://doi.org/10.1007/978-3-642-11931-6_3",
            "https://www.mdpi.com/2076-3417/15/22/12150",
        ],
    },
    {
        "name": "ai-for-software-verification",
        "title": "AI for Software Verification",
        "description": "Use machine learning to generate tests, localize bugs, and verify code produced by humans or LLMs.",
        "devin_body": r'''
## When to use

You want to improve functional verification of software, generate tests, find bugs, or verify code generated by LLMs or human developers.

## Usage

- Generate fuzz tests and coverage-guided test inputs with learned and LLM-based fuzzers.
- Predict uncovered branches and rank suspicious lines for coverage closure and bug localization.
- Infer loop invariants, assertions, and static-analysis properties from code and execution traces.
- Check code generated by LLMs with type checkers, solvers, and test suites.

## Steps

1. Build or collect the target codebase, seed inputs, and an oracle or differential testing harness.
2. Train or configure an ML-guided fuzzer, bug localizer, or test generator on the target language.
3. Run the tool to discover new coverage, crashes, or suspicious code regions.
4. Rank and triage findings with a human reviewer and a static or dynamic analyzer.
5. Verify LLM-generated code with unit tests, type checkers, and formal or symbolic methods.
6. Track coverage, false-positive rate, and bug-fix time in the development workflow.

## Code pattern

```python
import random
from typing import List

def coverage_guided_fuzz(target, seed_inputs: List[bytes], rounds: int = 1000):
    corpus = list(seed_inputs)
    seen = set()
    for _ in range(rounds):
        base = random.choice(corpus)
        mutant = bytearray(base)
        if mutant:
            mutant[random.randrange(len(mutant))] ^= random.randint(1, 255)
        coverage = target(bytes(mutant))
        if coverage not in seen:
            seen.add(coverage)
            corpus.append(bytes(mutant))
    return corpus
```

## Tuning notes

- Combine ML-generated tests with a strong oracle or differential testing.
- Monitor for overfitting to the training distribution of bugs.
- Use static and dynamic analysis together for better precision.

## Verification

1. Run an ML-guided fuzzer on a small C/Python target and report new coverage.
2. Train a bug-localization model and evaluate its ranked suspicious lines.
3. Verify a set of LLM-generated functions with unit tests and a static analyzer.
        ''',
        "references": [
            "https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1655469/full",
            "https://www.mdpi.com/2079-9292/10/21/2688",
            "https://dvcon-proceedings.org/wp-content/uploads/1135-A-Survey-of-Machine-Learning-Applications-in-Functional-Verification.pdf",
            "https://dl.acm.org/doi/10.1145/3661308",
            "https://doi.org/10.1016/j.ijar.2024.109206",
        ],
    },
    {
        "name": "ai-for-type-theory",
        "title": "AI for Type Theory",
        "description": "Use machine learning to predict tactics, select premises, and synthesize terms in dependently typed proof assistants.",
        "devin_body": r'''
## When to use

You are working in a dependently typed proof assistant (Coq, Lean, Agda, Idris) and want to automate tactic selection, lemma retrieval, or term synthesis.

## Usage

- Represent dependent type theories (Martin-Löf, CIC, homotopy/cubical) as features for ML.
- Predict the next tactic from the current proof state and available hypotheses.
- Rank library lemmas that are likely to be useful for a given goal.
- Generate auxiliary lemmas and well-typed terms guided by types and proof context.

## Steps

1. Extract proof-state features, goal types, and tactic histories from a proof assistant corpus.
2. Train a tactic predictor and evaluate top-1 and top-5 accuracy on held-out proofs.
3. Build a premise selector that ranks lemmas by relevance and check how often the human-used lemma is top-ranked.
4. Generate helper lemmas or terms and type-check them in the proof assistant kernel.
5. Integrate the models into an interactive tactic recommendation system.
6. Validate that suggestions improve proof length and maintain soundness.

## Code pattern

```python
# Tactic prediction as a ranking problem
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Features encode goal/argument types and available tactics
X_train = np.array([[0, 1, 0, 1], [1, 0, 1, 0], ...])
y_train = np.array(["intro", "apply", "rewrite", ...])

clf = RandomForestClassifier(random_state=42).fit(X_train, y_train)
state_features = np.array([[0, 1, 0, 0]])
predicted_tactic = clf.predict(state_features)[0]
print("Next tactic:", predicted_tactic)
```

## Tuning notes

- Use tree-based models for fast interactive feedback in proof assistants.
- Augment tactic data with type-checker feedback and proof-state context.
- Validate synthesized terms by replaying them through the proof assistant kernel.

## Verification

1. Train a tactic predictor on a proof corpus and measure top-1 / top-5 accuracy.
2. Implement a premise-selection tool and check how often the human-used lemma is ranked first.
3. Synthesize a simple helper lemma and verify it with the proof assistant.
        ''',
        "references": [
            "https://www.danielgratzer.com/papers/type-theory-book.pdf",
            "https://agda.readthedocs.io/en/latest/getting-started/what-is-agda.html",
            "https://doi.org/10.1145/3563306",
            "https://arxiv.org/abs/2304.00994",
            "https://arxiv.org/abs/2410.19605v1",
        ],
    },
    {
        "name": "ai-for-logic",
        "title": "AI for Logic",
        "description": "Use machine learning to combine logical reasoning with neural models, learning rules, constraints, and solver guidance.",
        "devin_body": r'''
## When to use

You want to combine logical reasoning with machine learning: learning rules, constraints, or logical representations from data, or using ML to accelerate logic solvers.

## Usage

- Integrate neural networks with symbolic logic for neuro-symbolic reasoning.
- Learn interpretable rules and constraints from data and logical formulas.
- Apply probabilistic and statistical relational logics to structured problems.
- Guide SAT/SMT/ASP solvers with learned value functions and heuristics.

## Steps

1. Collect logical data, truth tables, or structured examples for the target rules or constraints.
2. Train a rule learner, constraint extractor, or neuro-symbolic model on the data.
3. Validate learned rules on held-out logical formulas and compare to expert constraints.
4. Combine the learned heuristic with a SAT/SMT/ASP solver and measure runtime improvements.
5. Enforce logical constraints as regularizers or post-hoc corrections in the neural model.
6. Monitor that model predictions respect the specified logical constraints.

## Code pattern

```python
# Simple rule learning from a truth table
from sklearn.tree import DecisionTreeClassifier

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]  # XOR

clf = DecisionTreeClassifier(max_depth=2).fit(X, y)

# Extract propositional rules from the tree
from sklearn.tree import export_text
rules = export_text(clf, feature_names=["A", "B"])
print(rules)
```

## Tuning notes

- Balance expressivity and interpretability: shallow rule sets are human-readable, deep models may be more accurate.
- Use logical constraints as regularizers or post-hoc corrections.
- Evaluate rule learning on held-out logical formulas, not just tabular data.

## Verification

1. Learn a Boolean formula from examples and verify it on a held-out truth table.
2. Combine a learned heuristic with a SAT solver and compare runtimes.
3. Train a neuro-symbolic model and check that its predictions respect given logical constraints.
        ''',
        "references": [
            "https://doi.org/10.1016/j.ijar.2024.109206",
            "https://doi.org/10.48550/arxiv.2403.04017",
            "https://doi.org/10.1016/j.artint.2023.104062",
            "https://drops.dagstuhl.de/storage/04dagstuhl-reports/volume12/issue07/22291/DagRep.12.7.80/DagRep.12.7.80.pdf",
            "https://neurosymbolic-ai-journal.com/system/files/nai-paper-949.pdf",
        ],
    },
    {
        "name": "ai-for-automated-reasoning",
        "title": "AI for Automated Reasoning",
        "description": "Use machine learning to guide proof search, premise selection, and tactic prediction in theorem provers and proof assistants.",
        "devin_body": r'''
## When to use

You are building or using automated theorem provers, SMT solvers, or proof assistants and want to accelerate search with learned guidance.

## Usage

- Guide proof search by selecting clauses, ordering variables, and scheduling strategies.
- Predict which axioms or lemmas are relevant to a conjecture.
- Generate the next proof step in an interactive theorem prover from the current goal.
- Combine LLM-generated proof steps with verification by a trusted symbolic kernel.

## Steps

1. Collect a corpus of conjectures, axioms, and proof traces from an ATP or ITP library.
2. Train an axiom/premise selector and measure mean reciprocal rank of used premises.
3. Build a clause or tactic predictor and integrate it into the prover's search loop.
4. Run the prover with and without learned guidance and compare inferences or proof time.
5. Use an LLM to suggest proof steps and reject or accept them with a proof checker.
6. Retrain selectors as the library grows and evaluate on new benchmark problems.

## Code pattern

```python
# Axiom selection as a binary-relevance ranking problem
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Conjectures and axioms as strings
conjecture = "forall x y, x + y = y + x"
axioms = ["commutativity_add", "associativity_add", "distributivity_mul"]

corpus = [conjecture] + axioms
vectorizer = TfidfVectorizer().fit(corpus)
X = vectorizer.transform(corpus)

nbrs = NearestNeighbors(n_neighbors=2, metric="cosine").fit(X[1:])
distances, indices = nbrs.kneighbors(X[0])
print("Relevant axioms:", [axioms[i] for i in indices[0]])
```

## Tuning notes

- Use proof-state embeddings that capture local context and environment.
- Retrain selectors as the library grows (online learning).
- Always check predicted proof steps with the proof assistant or ATP.

## Verification

1. Train an axiom selector and measure mean reciprocal rank of the used axioms.
2. Run a theorem prover with and without learned clause selection and compare the number of inferences.
3. Integrate an LLM with a proof checker and report the percentage of accepted proof steps.
        ''',
        "references": [
            "https://doi.org/10.48550/arxiv.2403.04017",
            "https://doi.org/10.1561/2200000081",
            "https://www.tcs.ifi.lmu.de/staff/jasmin-blanchette/axiom_sel.pdf",
            "https://doi.org/10.48550/arxiv.2404.09939",
            "https://arxiv.org/abs/2606.08728v4",
        ],
    },
    {
        "name": "ai-for-satisfiability",
        "title": "AI for Satisfiability",
        "description": "Guide CDCL SAT solver branching and resets with offline neural predictions to solve more competition instances without GPU overhead.",
        "devin_body": r'''
## When to use

You want to solve Boolean satisfiability, MaxSAT, QSAT, or SMT problems faster by using machine learning for branching, restarts, or end-to-end search.

## Usage

- Improve CDCL and local-search SAT solvers with learned branching and restart policies.
- Build end-to-end neural SAT solvers to predict satisfiability and assignments.
- Combine neural guidance with CDCL variable activity in hybrid solvers.
- Learn heuristics for quantified and theory-laden satisfiability problems.

## Steps

1. Curate SAT/SMT/QSAT training instances close to the target problem distribution.
2. Train a neural model or learned heuristic to predict satisfiability, assignments, or variable activity.
3. Integrate the learned guidance into a CDCL or local-search solver.
4. Benchmark the hybrid, pure neural, and classical solvers on the target instance family.
5. Train on a distribution close to the target and test generalization across domains.
6. Compare runtimes and solution quality on SAT-COMP or SMT-LIB benchmarks.

## Code pattern

```python
import torch
import torch.nn as nn

# Simplified message-passing module for a graph neural SAT solver
class MessagePassingSAT(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.L_init = nn.Linear(1, dim)
        self.C_init = nn.Linear(1, dim)
        self.L_update = nn.GRUCell(dim, dim)
        self.C_update = nn.GRUCell(dim, dim)

    def forward(self, L, C, var_to_clauses, clause_to_vars):
        # Message passing between literals and clauses
        return self.L_update(C[clause_to_vars].mean(dim=1), L)
```

## Tuning notes

- Hybrid solvers usually outperform pure neural SAT solvers on industrial instances.
- Train on a distribution close to the target problem; generalization across domains is hard.
- Use unsat-core prediction for CDCL guidance rather than full assignment prediction.

## Verification

1. Train NeuroSAT on random 3-SAT and evaluate on graph-coloring encodings.
2. Integrate a learned branching heuristic into a CDCL solver and run SAT-COMP benchmarks.
3. Compare pure neural, hybrid, and classical solvers on a family of problem instances.
        ''',
        "references": [
            "https://github.com/dselsam/neurosat",
            "https://arxiv.org/pdf/1802.03685",
            "https://doi.org/10.48550/arxiv.2203.04755",
            "https://doi.org/10.1561/2200000081",
            "https://doi.org/10.1609/socs.v18i1.35997",
        ],
    },
    {
        "name": "ai-for-constraint-programming",
        "title": "AI for Constraint Programming",
        "description": "Use machine learning to learn constraints, heuristics, and models for constraint programming and CP-SAT solvers.",
        "devin_body": r'''
## When to use

You are modeling and solving constraint satisfaction and optimization problems and want to learn constraints, heuristics, or entire models from data.

## Usage

- Learn constraints from examples of feasible and infeasible solutions.
- Learn variable and value ordering heuristics for CP and CP-SAT solvers.
- Synthesize optimization or CSP models from observations of behavior.
- Combine lazy clause generation and CP-SAT with neural predictors.

## Steps

1. Gather labeled examples of feasible, infeasible, or optimal solutions for the target problem.
2. Train a constraint learner or heuristic predictor from the example set.
3. Combine learned constraints with expert-written constraints for safety.
4. Integrate the learned heuristic into a CP or CP-SAT solver and compare search nodes.
5. Acquire a candidate CP model from data and validate it on an independent test set.
6. Benchmark against default CP solver strategies and tune with active learning.

## Code pattern

```python
from ortools.sat.python import cp_model

# Small CP-SAT model learned/specified for a scheduling problem
model = cp_model.CpModel()
starts = [model.NewIntVar(0, 10, f"s{i}") for i in range(3)]
durations = [2, 3, 1]
ends = [model.NewIntVar(0, 15, f"e{i}") for i in range(3)]

for s, d, e in zip(starts, durations, ends):
    model.Add(e == s + d)

# No-overlap constraints
model.Add(ends[0] <= starts[1]).OnlyEnforceIf(model.NewBoolVar(""))

solver = cp_model.CpSolver()
status = solver.Solve(model)
print("Status:", status, "Makespan:", solver.ObjectiveValue())
```

## Tuning notes

- Use active learning when constraint examples are expensive to label.
- Combine learned constraints with expert-written constraints for safety.
- Benchmark learned heuristics against default CP solver strategies.

## Verification

1. Learn a set of constraints from feasible/infeasible examples and check solution feasibility.
2. Train a variable-ordering heuristic and compare search nodes to the default solver.
3. Acquire a CP model from data and validate it against an independent test set.
        ''',
        "references": [
            "https://doi.org/10.1613/jair.1.19533",
            "https://jair.org/index.php/jair/article/download/19533/27252",
            "https://www.ijcai.org/proceedings/2018/0772.pdf",
            "https://www.ijcai.org/proceedings/2021/0610.pdf",
            "https://www.jair.org/index.php/jair/article/view/21207",
        ],
    },
    {
        "name": "ai-for-discrete-optimization",
        "title": "AI for Discrete Optimization",
        "description": "Use machine learning to speed up combinatorial optimization through branching, graph neural networks, and data-driven configuration.",
        "devin_body": r'''
## When to use

You need to solve combinatorial optimization problems such as scheduling, routing, packing, or integer programming and want to use ML to speed up exact or heuristic solvers.

## Usage

- Learn branching, node selection, and cutting-plane policies for branch-and-bound.
- Encode combinatorial structure as graphs and train graph neural network policies.
- Learn construction or improvement heuristics by imitation or reinforcement learning.
- Tune solver parameters from historical data with algorithm configuration.

## Steps

1. Formulate the combinatorial problem (scheduling, routing, packing, etc.) and collect benchmark instances.
2. Train a GNN or learned policy for branching, selection, or heuristic construction.
3. Integrate the learned policy into an exact solver such as SCIP, Gurobi, or CP-SAT.
4. Compare nodes, runtime, and solution quality to the solver's default strategy.
5. Use algorithm configuration to tune solver parameters on the instance family.
6. Evaluate on held-out and out-of-distribution instances to assess robustness.

## Code pattern

```python
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

# GNN that scores nodes/edges for a combinatorial decision
class COGNN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, hidden_channels)
        self.score = torch.nn.Linear(hidden_channels, 1)

    def forward(self, x, edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        return self.score(x).squeeze(-1)

# Score candidate nodes for branching
scores = model(node_features, edge_index)
next_node = int(torch.argmax(scores))
```

## Tuning notes

- Use strong OR baselines (SCIP, Gurobi, CP-SAT) to evaluate ML additions.
- Distinguish between pure learned solvers and learned heuristics inside exact solvers.
- Reward functions in RL must account for solver time, not just solution quality.

## Verification

1. Train a GNN branching policy and compare branch-and-bound nodes to SCIP defaults.
2. Learn a primal heuristic for a routing problem and benchmark against LKH or OR-Tools.
3. Run algorithm configuration (e.g., SMAC) and compare cross-validated solver runtimes.
        ''',
        "references": [
            "https://doi.org/10.1016/j.ejor.2020.07.063",
            "https://doi.org/10.48550/arxiv.2601.10583",
            "https://ojs.aaai.org/index.php/AAAI/article/view/26810",
            "https://jmlr.org/papers/volume24/21-0449/21-0449.pdf",
            "https://link.springer.com/article/10.1007/s10107-024-02130-y",
        ],
    },
    {
        "name": "ai-for-approximation-algorithms",
        "title": "AI for Approximation Algorithms",
        "description": "Use machine learning to improve polynomial-time approximations and rounding for NP-hard problems.",
        "devin_body": r'''
## When to use

You want polynomial-time approximate solutions for NP-hard problems and are willing to use ML predictions to improve approximation factors or runtime.

## Usage

- Predict approximate solution values and rounding decisions for NP-hard maximization and CSPs.
- Use learning-augmented predictions to improve average-case approximation factors.
- Learn fast heuristics that approximate optimal solutions on typical instances.
- Build convex relaxations (LP/SDP) as scaffolds for learned rounding policies.

## Steps

1. Choose an NP-hard problem and generate training instances with exact or relaxed labels.
2. Train a regressor or policy to predict objective values or rounding probabilities.
3. Combine the learned predictions with an LP/SDP relaxation or greedy algorithm.
4. Empirically verify approximation ratios on instance families and compare to classical algorithms.
5. Evaluate on out-of-distribution instances and certify average-case guarantees.
6. Deploy the fast approximation inside an optimization or decision pipeline.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

# Predict an approximate cut weight or rounding probability for Max-Cut
features = np.array([[0.5, 0.2, 0.8], [0.1, 0.9, 0.3], ...])
# Oracle labels from small exact solves
labels = np.array([1.2, 0.9, ...])

approx = GradientBoostingRegressor(random_state=42).fit(features, labels)
print("Predicted value:", approx.predict([[0.4, 0.3, 0.7]]))
```

## Tuning notes

- Verify that learned approximations retain valid worst-case or average-case guarantees.
- Use convex relaxations (LP/SDP) as a scaffold for learned rounding.
- Evaluate on out-of-distribution instance families, not just the training domain.

## Verification

1. Solve small Max-Cut instances exactly and compare a learned rounding policy to random rounding.
2. Prove or empirically verify an approximation ratio on a family of instances.
3. Benchmark a learned approximation heuristic against a classical constant-factor algorithm.
        ''',
        "references": [
            "https://proceedings.neurips.cc/paper_files/paper/2024/file/2db08b94565c0d582cc53de6cee5fd47-Paper-Conference.pdf",
            "https://doi.org/10.1016/j.ejor.2020.07.063",
            "https://doi.org/10.1109/access.2020.3004964",
            "https://doi.org/10.48550/arxiv.2601.10583",
            "https://arxiv.org/abs/2006.09123",
        ],
    },
]