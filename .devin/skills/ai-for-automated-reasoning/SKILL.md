# AI for Automated Reasoning

## Description

Learning to guide proof search, premise selection, tactic prediction, and combining LLMs with symbolic reasoners.

## When to use

You are building or using automated theorem provers, SMT solvers, or proof assistants and want to accelerate search with learned guidance.

## Key concepts

- **Proof search guidance**: clause selection, variable ordering, and strategy scheduling.
- **Premise selection**: predict which axioms or lemmas are relevant to a conjecture.
- **Tactic prediction in ITPs**: generate the next proof step from the current goal and context.
- **LLM + symbolic reasoners**: generate candidate proof steps and verify them with a trusted kernel.

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

## References

- https://doi.org/10.48550/arxiv.2403.04017
- https://doi.org/10.1561/2200000081
- https://www.tcs.ifi.lmu.de/staff/jasmin-blanchette/axiom_sel.pdf
- https://doi.org/10.48550/arxiv.2404.09939
- https://arxiv.org/abs/2606.08728v4
