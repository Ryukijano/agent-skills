# AI for Future of Work

## Description

Automation and augmentation analysis, skill demand forecasting, workforce transitions, algorithmic management, and human-centered labor market policy.

## When to use

You are analyzing how AI changes occupations, tasks, hiring, productivity, job quality, or workforce skills and designing policy or organizational responses.

## Key concepts

- **AI exposure and task automation**: task-level models of automation and augmentation potential.
- **Skill demand and transitions**: reskilling, upskilling, and occupational mobility.
- **Algorithmic management**: AI-driven scheduling, monitoring, evaluation, and worker autonomy.
- **Job quality and equity**: wages, working conditions, discrimination, and worker voice.
- **Human-centered labor policy**: social dialogue, safety nets, and lifelong learning.

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

## References

- https://www.oecd.org/en/topics/future-of-work.html
- https://oecd.ai/en/working-group-future-of-work
- https://www.ilo.org/observatory-ai-and-work-digital-economy
- https://webapps.ilo.org/static/english/intserv/working-papers/wp096/index.html
