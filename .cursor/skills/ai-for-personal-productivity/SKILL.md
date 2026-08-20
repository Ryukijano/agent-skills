# AI for Personal Productivity

## Description

Time management, task prioritization, calendar scheduling, meeting optimization, and personal workflow automation.

## When to use

You want to prioritize tasks, resolve calendar conflicts, block focus time, or automate repetitive personal workflows.

## Key concepts

- **Task prioritization**: Eisenhower matrix, urgency/importance scoring, or learned user preferences.
- **Calendar conflict resolution**: decide which meetings to attend, reschedule, or decline based on preferences.
- **Time blocking**: allocate fixed windows for deep work, admin, and rest.
- **Intelligent scheduling**: propose times that respect energy patterns and travel buffers.
- **Agentic workflows**: combine LLMs with calendar, email, and task tools via tool use.

## Code pattern

```python
# Simplified task ordering by priority (lower number = higher priority)
tasks = [("email", 3), ("planning", 2), ("deep_work", 1)]
ordered = sorted(tasks, key=lambda x: x[1])
print([t[0] for t in ordered])
```

## Tuning notes

- Learn from user edits rather than overriding their preferences.
- Respect focus time and avoid over-scheduling back-to-back meetings.
- Integrate with calendar APIs using minimal, scoped permissions.
- Test on synthetic calendars before applying to a user's real schedule.

## Verification

1. Build a daily task scheduler and compare its plan to a user's manual plan.
2. Resolve a synthetic calendar conflict using stated priorities.
3. Auto-categorize low-priority emails and measure time saved.

## References

- https://aclanthology.org/2026.acl-long.1648.pdf
- https://arxiv.org/abs/2601.11957
- https://arxiv.org/abs/2509.25693
- https://aclanthology.org/2026.acl-long.1614.pdf
