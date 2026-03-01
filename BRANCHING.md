# Branching strategy (solo dev)

- `main` is always deployable.
- Use feature branches for bigger work:
  - `feature/seo-pages`
  - `feature/styling`
  - `feature/portal-v3`
- Small fixes can go directly to `main`.

## Flow
1. `git checkout -b feature/<name>`
2. Work + commits
3. Merge back to main:
   - `git checkout main`
   - `git pull`
   - `git merge feature/<name>`
   - `git push`
