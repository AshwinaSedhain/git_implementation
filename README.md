# Python Calculator — CI/CD Learning Project

A simple calculator library used to demonstrate Git, GitHub, pytest, and CI/CD concepts.

## Project Structure

```
calculator/       # Source code
tests/            # Unit and integration tests
.github/workflows # GitHub Actions CI pipeline
```

## Run Tests Locally

```bash
pip install pytest pytest-cov
pytest -v
pytest --cov=calculator --cov-report=term-missing
```

## Git Workflow Practiced

- `main` — stable production branch
- `develop` — integration branch
- Feature branches merged via Pull Requests
- Tags used to mark releases (e.g. `v1.0.0`)

## CI/CD

GitHub Actions runs automatically on every push and pull request:
- Runs unit tests
- Runs integration tests
- Reports code coverage
