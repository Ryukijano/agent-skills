---
description: Prepare research code for public release alongside a paper submission
---

## Paper Code Release

1. Add LICENSE file (MIT or Apache-2.0).

2. Write README with: description, installation, quick start, results table, citation.

3. Create `requirements.txt` or `environment.yml` with pinned versions.

4. Remove hardcoded paths:
   ```bash
   grep -rn "/scratch/\|/home/\|C:\\" --include="*.py" | grep -v "config\|args\|#"
   ```

5. Remove debug prints and secrets:
   ```bash
   grep -rn "print(\|api_key\|password\|token" --include="*.py" | grep -v "logger\|tqdm\|wandb\|#"
   ```

6. Add `.gitignore` for data/, outputs/, wandb/, __pycache__/.

7. Upload pretrained weights and add download links.

8. Add citation block (BibTeX) to README.

9. Create `CITATION.bib`.

10. Summarize: release readiness, any remaining gaps.
