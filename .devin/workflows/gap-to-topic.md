# Gap to Topic Run

1. State candidate topic in one sentence.
2. GATE 1 Open: search arXiv/OpenAlex + last 2 years of 3 target venues; list 5 closest papers with one-line deltas. Direct hit = NO-GO.
3. GATE 2 Contribution: one-sentence delta a reviewer accepts ("Unlike X, we Y, enabling Z"). Only "+2% on one dataset" = unclear → pivot.
4. GATE 3 Feasible: data (access/license/ethics), compute (GPU-hours vs AIRE/Spark budget, pilot <1 week), skills/time. Define minimal viable experiment.
5. Verdict: GO / PIVOT / NO-GO with `verdict_reason` recorded in `topic_dossier.md`.

Apply `gap-to-topic`, `research-strategy-project-design`, `literature-triage-matrix`.
