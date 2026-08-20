# AI for Event Planning

## Description

Venue and vendor recommendation, guest-list management, scheduling, budget optimization, and group preference aggregation for personal and small events.

## When to use

You want to plan a party, wedding, meeting, or community event by finding vendors, scheduling activities, managing guests, and staying within budget.

## Key concepts

- **Group preference aggregation**: combine attendee tastes, dietary needs, and location constraints.
- **Venue and vendor matching**: score vendors by event requirements, reviews, and price.
- **Scheduling under constraints**: room, time, and sequence constraints for sessions or ceremonies.
- **Budget multi-objective optimization**: trade cost, quality, and capacity.
- **Attendance forecasting**: predict RSVPs and no-shows from historical data.

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
