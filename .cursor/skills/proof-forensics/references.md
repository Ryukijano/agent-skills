# proof-forensics references

- `history.md`: the 7 Oct 2026 withdrawals and fixes. Don't give it to an agent under benchmark (see `math-proof-skills/benchmark/answers/README.md`).
- Withdrawal notices sit in each withdrawn manuscript's `README.md`. Archived PDFs are at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.
- Revised titles have more than one dated directory: `ls preprints | sed -E 's/-[A-Z][a-z]+-[0-9]+-2026$//' | sort | uniq -d` (28 titles).
- Diff of the release update: `git diff --stat adc7f1241 fd4aeeb2e`.
