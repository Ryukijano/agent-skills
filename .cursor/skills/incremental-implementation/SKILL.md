# Incremental Implementation

## The Increment Cycle
1. Pick smallest meaningful slice
2. Implement it
3. Verify (tests, manual check)
4. Commit
5. Repeat

## Slicing Strategies
- Vertical Slices (preferred): full stack through one path
- Contract-First: define interfaces, then implement
- Risk-First: tackle riskiest part first

## Rules
- Simplicity First: simplest thing that works
- One Thing at a Time: single concern per increment
- Keep It Compilable: code always builds
- Feature Flags for incomplete features
- Rollback-Friendly: each commit revertible
