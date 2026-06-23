---
name: reproducibility-checklist
description: Concrete audit checklist for making a project or paper release reproducible. Use before submission or when onboarding to an existing codebase.
---

## Reproducibility Checklist (Paper / Release Ready)

- [ ] Git commit for every reported result is recorded and tagged or branch noted.
- [ ] All configs for main tables/figures committed (with exact command lines).
- [ ] Random seeds set and logged; multi-seed variance reported where claims are made.
- [ ] Environment captured (conda/pip export or lock file).
- [ ] Dataset splits versioned or hashed; leak-free splits documented.
- [ ] Preprocessing code versioned; any hand edits to data noted.
- [ ] Pretrained weights used have provenance (source + download date or HF commit).
- [ ] Training + eval can be launched with one or two documented commands.
- [ ] No absolute local paths or user-specific env vars in committed scripts.
- [ ] README has "Reproduce main result" section with expected numbers ± tolerance.
- [ ] For hardware-sensitive results, hardware (GPU model, driver) listed.

Apply with `/reproducibility-checklist` workflow and `reproducibility` + `data-management` skills.
