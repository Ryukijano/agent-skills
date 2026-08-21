# AI for Event Planning

## Description

Use AI to match venues and vendors, aggregate guest preferences, schedule activities, and stay within budget for events.

## When to use

You want to plan a party, wedding, meeting, or community event by finding vendors, scheduling activities, managing guests, and staying within budget.

## Usage

- Aggregate attendee dietary, accessibility, and location preferences.
- Score and match vendors to event briefs and budgets.
- Schedule sessions or ceremonies under room and time constraints.
- Forecast RSVPs and no-shows from past event data.

## Steps

1. Collect event goals, budget, guest list, and constraints.
2. Gather vendor or venue options and review ratings and availability.
3. Match candidates to the brief using text similarity and budget filters.
4. Build a schedule and menu that respects dietary and accessibility needs.
5. Track RSVPs and generate a day-of run sheet with human approval for contracts.

## Code pattern

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Match vendor descriptions to event requirements
vectorizer = TfidfVectorizer().fit(vendor_descriptions + [event_requirements])
X = vectorizer.transform(vendor_descriptions + [event_requirements])
scores = cosine_similarity(X[-1:], X[:-1])
```

## Tuning notes

- Collect group preferences early and provide ranked alternatives.
- Check vendor availability, insurance, and cancellation policies.
- Handle dietary restrictions and accessibility needs explicitly.
- Keep human final approval for contracts and payments.

## Verification

1. Match a list of vendors to a sample event brief and budget.
2. Build an RSVP forecaster and evaluate on past events.
3. Schedule a multi-session event with room and time constraints.

## References

- https://dl.acm.org/doi/10.1145/3314421
- https://doi.org/10.5281/zenodo.20046609
- https://doi.org/10.56741/jnest.v5i01.1050
- https://doi.org/10.1609/aaai.v40i19.38684
