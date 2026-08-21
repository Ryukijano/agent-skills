# AI for Future of Work

## Description

Use AI exposure and skill-demand analysis to understand workforce transitions and support human-centered labor policy.

## When to use

You are analyzing how AI changes occupations, tasks, hiring, productivity, job quality, or workforce skills and designing policy or organizational responses.

## Usage

- Estimate task-level automation and augmentation potential.
- Model skill demand, reskilling, upskilling, and occupational mobility.
- Analyze algorithmic management in scheduling, monitoring, and evaluation.
- Assess job quality, wages, equity, and worker voice.
- Co-design labor policy with workers and social partners.

## Steps

1. Collect task-level occupational data and identify AI-exposed tasks.
2. Build or use an AI-exposure scoring model and validate against expert labels.
3. Model task reallocation, reskilling needs, and occupational mobility.
4. Pilot an AI tool and measure effects on task time, output, and job quality.
5. Engage workers and unions in co-designing transitions and safeguards.
6. Evaluate outcomes and adjust policy or organizational responses.

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
