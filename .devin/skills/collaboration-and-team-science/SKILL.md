# Collaboration and Team Science

## Description

Build, lead, and sustain productive interdisciplinary research teams with clear roles, communication, and shared tools.

## When to use

You are assembling a research team, coordinating a multi-site or interdisciplinary project, or establishing authorship and data-sharing agreements.

## Key concepts

- **Team science**: collaborative, often interdisciplinary research to tackle complex problems.
- **Role clarity**: define who does what, including data, methods, writing, and management.
- **Psychological safety**: create an environment where team members can raise concerns.
- **Authorship and contribution agreements**: decide early and revisit regularly.
- **Communication cadence and shared infrastructure**: version control, shared drives, and meeting rituals.

## Code pattern

```python
import csv
from datetime import datetime


def create_team_charter(roles, contributions):
    with open("team_charter.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "role", "contribution", "start_date"])
        for member in roles:
            writer.writerow([
                member["name"],
                member["role"],
                contributions.get(member["name"], ""),
                datetime.now().isoformat(),
            ])


def authorship_matrix(members, tasks):
    matrix = {m: {t: 0 for t in tasks} for m in members}
    # Populate manually or from contribution logs
    return matrix
```

## Tuning notes

- Agree on goals, roles, authorship, and data-sharing rules at kickoff.
- Schedule regular syncs and keep decision logs to reduce misalignment.
- Use shared repositories and documents; avoid siloed files and email chains.
- Address conflict early and revisit team norms at major milestones.

## Verification

1. Create a team charter with roles, contributions, and authorship principles.
2. Publish a shared data and authorship plan that all members approve.
3. Review the charter and collaboration health at each project milestone.

## References

- https://www.cancer.gov/about-nci/organization/crs/research-initiatives/team-science-field-guide/collaboration-team-science-guide.pdf?rid=267&tid=1
- https://nap.nationalacademies.org/resource/29043/interactive/
- https://www.ncbi.nlm.nih.gov/books/NBK617881/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8599160/
- https://www.nigms.nih.gov/grants/Pages/Considerations-for-Multiple-Principal-Investigator-Applications
