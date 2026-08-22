# Experiment Pre-Registration Checklist

Complete **before** any results-producing run. Check each item.

## Hypothesis Linkage

- [ ] Primary hypothesis ID from hypothesis canvas referenced
- [ ] Pre-specified prediction stated (direction and magnitude if applicable)
- [ ] Falsification criterion documented

## Design

- [ ] Primary outcome metric defined (one only)
- [ ] Secondary/exploratory metrics labeled as exploratory
- [ ] Unit of analysis specified
- [ ] Inclusion/exclusion criteria for data samples
- [ ] Train/validation/test split frozen and documented

## Controls

- [ ] Baseline method identified and justified
- [ ] Ablation plan pre-specified (not invented post-hoc)
- [ ] Random seed list fixed (minimum 3 for stochastic methods)
- [ ] Hyperparameters fixed or search budget pre-specified
- [ ] Hardware and software versions recorded

## Analysis

- [ ] Statistical test or comparison method named
- [ ] Multiple-comparison correction plan (if applicable)
- [ ] Stopping rules defined (epochs, convergence, budget)
- [ ] Outlier handling policy pre-specified

## Reproducibility

- [ ] Git commit hash recorded
- [ ] Data version / snapshot ID recorded
- [ ] Environment lockfile created
- [ ] Output directory structure defined

## Integrity Gates

- [ ] No peeking at test set during development
- [ ] No condition added after viewing interim results
- [ ] Negative results will be reported

## Sign-off

```
Protocol ID:
Checklist completed: YYYY-MM-DD
Author:
Amendments: [none | see protocol amendments section]
```
