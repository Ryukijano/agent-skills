# proof-forensics references

- `history.md`: the 7 Oct 2026 withdrawals (3) and fixes (14 manuscripts, plus 13 citation-only updates).
- Withdrawal notices: `preprints/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/README.md`, `preprints/Algebraicity-of-Kuga-Satake-Correspondences-for-K3-Surfaces-October-3-2026/README.md`, `preprints/The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026/README.md`. Archived PDFs are at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.
- Revised pairs (old/new dated dirs): Taming-implies-compatibility, Deforming-hypersymplectic, Incompressible-Box-Transport, the Kähler MMP/abundance set, Lipschitz heights / Ashkin–Teller. List them with `ls preprints | sed -E 's/-[A-Z][a-z]+-[0-9]+-2026$//' | sort | uniq -d` (28 titles have more than one version).
- Diff of the release update: `git diff --stat adc7f1241 fd4aeeb2e`.
