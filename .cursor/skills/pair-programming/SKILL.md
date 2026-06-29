---
name: pair-programming
description: >-
  Structured pair programming workflow with AI agent. Use when the user wants to
  collaboratively develop code, review in real-time, or follow driver-navigator
  pattern.
---

# Pair Programming with AI

## Driver-Navigator Pattern
- **Driver (You)**: Writes code, makes decisions, asks questions
- **Navigator (AI)**: Reviews, suggests alternatives, catches bugs, asks clarifying questions

## Workflow
1. **Plan together**: Discuss the approach before coding
2. **Write incrementally**: Small changes, test frequently
3. **Review each change**: Navigator reviews before moving on
4. **Refactor together**: Both agree on improvements

## Effective Collaboration
- State intent before writing code: "I'm going to add a function that..."
- Ask for alternatives: "Is there a better way to structure this?"
- Explain reasoning: "I chose this approach because..."
- Catch issues early: Navigator flags potential problems immediately

## When to Pair
- Complex logic that benefits from two perspectives
- New codebase or unfamiliar patterns
- Security-sensitive code
- Algorithm design

## When NOT to Pair
- Simple boilerplate or config changes
- Well-defined tasks with clear solutions
- Exploratory prototyping (better to solo then review)
