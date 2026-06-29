---
name: git-advanced-workflows
description: >-
  Advanced git workflows including interactive rebase, cherry-picking, bisect,
  reflog recovery, subtree merge, and conflict resolution strategies. Use when
  the user needs complex git operations beyond basic commit/push.
---

# Git Advanced Workflows

## Interactive Rebase
```bash
git rebase -i HEAD~5  # Rebase last 5 commits
# Commands: pick, squash, fixup, reword, drop, edit
```

## Cherry-Picking
```bash
git cherry-pick <commit-hash>  # Apply a specific commit
git cherry-pick <hash1> <hash2>  # Multiple commits
git cherry-pick A..B  # Range (exclusive A, inclusive B)
```

## Bisect (Binary Search for Bugs)
```bash
git bisect start
git bisect bad          # Current commit is broken
git bisect good <hash>  # Known good commit
# Git checks out middle commit; test and mark:
git bisect good  # or git bisect bad
git bisect reset  # Exit bisect mode
```

## Reflog Recovery
```bash
git reflog  # Show history of HEAD changes
git reset --hard HEAD@{2}  # Restore to a previous state
```

## Subtree Merge
```bash
git remote add sub https://github.com/user/repo.git
git fetch sub
git merge --allow-unrelated-histories sub/main
```

## Conflict Resolution
1. `git status` to see conflicted files
2. Edit files to resolve conflicts (remove <<<<, ====, >>>>)
3. `git add <file>` to mark resolved
4. `git commit` to complete the merge

## Stash Management
```bash
git stash save "work in progress"
git stash list
git stash pop  # Apply and drop most recent
git stash apply stash@{1}  # Apply specific stash
```

## Worktrees (Parallel Branches)
```bash
git worktree add ../feature-branch feature
# Work on feature in ../feature-branch without switching main repo
```
