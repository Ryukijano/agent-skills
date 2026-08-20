# AI for Travel

## Description

Itinerary planning, point-of-interest recommendation, flight and hotel personalization, trip optimization, and conversational travel agents.

## When to use

You want to plan a trip, recommend points of interest, build an itinerary, or personalize travel options within time and budget constraints.

## Key concepts

- **POI recommendation**: predict attractions and restaurants a traveler will enjoy.
- **Itinerary optimization**: orienteering and routing under time, budget, and preference constraints.
- **Multi-constraint planning**: combine opening hours, travel times, group preferences, and accessibility.
- **LLM travel agents**: conversational planning with tool use for live data.
- **Real-time data integration**: weather, events, prices, and transport disruptions.

## Code pattern

```python
import itertools

# Simplified orienteering: maximize POI score within a time budget
pois = [("museum", 90, 9), ("park", 60, 7), ("cafe", 45, 5)]  # (name, time, score)
budget = 180
best = max(
    (combo for r in range(1, len(pois) + 1)
     for combo in itertools.combinations(pois, r)
     if sum(p[1] for p in combo) <= budget),
    key=lambda combo: sum(p[2] for p in combo),
    default=(),
)
print([p[0] for p in best])
```

## Tuning notes

- Account for realistic travel times and attraction opening hours.
- Balance personalization with serendipity and group fairness.
- Verify bookings, prices, and availability through live APIs or links.
- Include fallback options for weather or cancellation.

## Verification

1. Build a one-day city itinerary that respects time and budget constraints.
2. Recommend POIs based on a small set of past trips and user ratings.
3. Compare an LLM-generated plan to a solver-based baseline on feasibility.

## References

- https://aclanthology.org/2025.acl-long.1339.pdf
- https://link.springer.com/article/10.1007/s40558-025-00318-2
- https://link.springer.com/article/10.1007/s44443-025-00178-0
- https://www.mdpi.com/2079-9292/14/10/2077
- https://arxiv.org/abs/2409.08069
