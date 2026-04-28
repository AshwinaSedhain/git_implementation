# Python Calculator — CI/CD & Git Learning Project

A Python calculator library built to demonstrate Git version control, GitHub collaboration,
pytest testing, and CI/CD concepts as part of a structured learning syllabus.

---

## Project Overview

This project implements a simple calculator with operations:
`add`, `subtract`, `multiply`, `divide`, `power`, `modulo`, `square_root`, `absolute`

It is intentionally structured to showcase every Git and testing concept from the syllabus.

---

## Features

- Core arithmetic and math operations
- Full unit test coverage (30+ tests)
- Integration tests for chained operations
- GitHub Actions CI pipeline
- Code quality checks with flake8
- Gitflow branch strategy

---

## Project Structure

```
calculator/         # Source code
tests/              # Unit and integration tests
.github/workflows/  # GitHub Actions CI pipeline
README.md
.gitignore
```

---

## How to Run the Project

```bash
# Install dependencies
pip install pytest pytest-cov flake8

# Run all tests
pytest -v

# Run with coverage
pytest --cov=calculator --cov-report=term-missing

# Run linter
flake8 calculator/ tests/
```

---

## Branch Strategy

```
main          ← stable, production-ready
develop       ← integration branch
feature/*     ← individual feature branches
```

Feature branches are merged into `develop` via Pull Request.
`develop` is merged into `main` for releases.

---

## Git Workflow Explanation

This project follows the **Feature Branch Workflow** (with elements of Gitflow):

1. Create a feature branch from `develop`
2. Make commits on the feature branch
3. Open a Pull Request: `feature/*` → `develop`
4. Merge into `develop` (non-fast-forward to preserve history)
5. When ready for release, merge `develop` → `main`
6. Tag the release (e.g. `v1.0`, `v2.0`)

---

## Merge Types

### Fast-Forward Merge
Happens when the target branch has no new commits since the feature branch was created.
Git simply moves the pointer forward — no merge commit is created.

```bash
git merge feature/branch   # fast-forward (default when possible)
```

### Non-Fast-Forward Merge (--no-ff)
Forces a merge commit even when fast-forward is possible.
This preserves the branch history and makes it clear a feature was developed separately.

```bash
git merge --no-ff feature/branch   # always creates a merge commit
```

We use `--no-ff` for all feature → develop and develop → main merges.

---

## Testing Importance

| Benefit | Description |
|---|---|
| Time saving | Catch bugs early before they reach production |
| Readability | Tests document expected behavior |
| Quality | Forces clean, modular code design |
| Confidence | Refactor safely knowing tests will catch regressions |

### Unit Tests
Test individual functions in isolation.
Located in `tests/test_unit.py`

### Integration Tests
Test multiple components working together.
Located in `tests/test_integration.py`

---

## Tags / Releases

| Tag | Description |
|---|---|
| v1.0 | Initial release: add, subtract, multiply, divide |
| v2.0 | Full release: power, modulo, square_root, absolute + CI |

---

## CI/CD Pipeline

GitHub Actions runs on every push and pull request:
- Lint with flake8
- Run unit tests
- Run integration tests
- Report code coverage
