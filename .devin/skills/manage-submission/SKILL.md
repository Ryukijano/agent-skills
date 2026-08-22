---
name: manage-submission
description: End-to-end submission management — venue selection, deadline tracking, anonymization, camera-ready prep, arXiv timing, and artifact packaging.
---

## Submission Management

### Venue fit
- Match scope, not prestige: read the venue's call for papers + last year's accepted titles.
- Check page limit + template + supplementary policy + double-blind rules **before** writing starts.
- Keep a `SUBMISSIONS.md`: venue, deadline (abstract/full), status, reviews, decision.

### Timeline (working backwards from deadline)
- T-4w: results frozen, all figures regenerate from committed code.
- T-2w: full draft; internal adversarial review pass (`adversarial-review`).
- T-1w: co-author pass, reproducibility checklist, anonymization sweep.
- T-2d: PDF compiles clean; page-limit check; all authors approved final.
- T-0: submit early — portals crash on deadline day.

### Anonymization sweep (double-blind)
- Third-person self-citations ("Prior work [7] showed...").
- Strip: PDF Author metadata (`exiftool -all= paper.pdf`), acknowledgments, grant numbers, repo URLs (use anonymous.4open.science).
- Check figure filenames and code comments for identity leaks.

### Camera-ready
- Incorporate reviewer feedback; add acknowledgments/funding back.
- IEEE eCopyright / ACM eRights forms; verify final PDF is X/2 generation compliant if required.
- Upload source (LaTeX) when mandated; confirm published version renders correctly.

### arXiv timing
- Post after acceptance decision or per advisor policy; endorsement may be needed for new categories.
- Version the arXiv post to match the camera-ready tag in git.

Related: `publishing-and-peer-review`, `paper-submission-prep`, `repro-bundle`.
