# AI for Education

## Description

Personalized learning, knowledge tracing, automated assessment, and intelligent tutoring systems.

## When to use

You are building adaptive learning, student modeling, or automated grading systems.

## Key concepts

- **Knowledge tracing**: predict what skills a student has mastered (BKT, DKT).
- **Personalized recommendation**: next-item or next-exercise suggestion.
- **Automated essay / code scoring**: LLM or learned rubric scoring.
- **Learning analytics**: engagement, dropout prediction, performance dashboards.
- **Fairness**: ensure models do not disadvantage subgroups.

## Code pattern

```python
import torch
import torch.nn as nn

class DKT(nn.Module):
    def __init__(self, n_questions, hidden_dim=128):
        super().__init__()
        self.lstm = nn.LSTM(n_questions, hidden_dim, batch_first=True)
        self.out = nn.Linear(hidden_dim, n_questions)

    def forward(self, x):
        h, _ = self.lstm(x)
        return torch.sigmoid(self.out(h))
```

## Tuning notes

- Student data is sensitive; protect privacy and obtain consent.
- Use temporally aware splits and avoid leakage.
- Interpretability helps teachers trust the system.

## Verification

1. Train a knowledge-tracing model on a public dataset (e.g., ASSISTments).
2. Recommend the next exercise and measure correctness improvement.
3. Evaluate an LLM grader against human rubrics.

## References

- https://arxiv.org/abs/2402.12142
- https://sites.google.com/site/assistmentsdata/
- https://arxiv.org/abs/2404.03025
- https://pytorch.org/tutorials/
