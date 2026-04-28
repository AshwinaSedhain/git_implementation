# Python Calculator — Git & CI/CD Implementation

## Project Overview

This project was built as a practical demonstration of Git version control, GitHub collaboration,
Python testing with pytest, and CI/CD pipeline automation. A simple Python calculator library
was chosen as the base application because it is straightforward enough to understand quickly,
yet complex enough to demonstrate all the required concepts in a meaningful way. The calculator
supports eight operations: addition, subtraction, multiplication, division, power, modulo,
square root, and absolute value.

---

## Repository Structure

The repository was organized into three main areas. The `calculator/` folder holds the source
code where all the mathematical operations are defined. The `tests/` folder contains both the
unit tests and integration tests written using pytest. The `.github/workflows/` folder holds
the CI/CD pipeline configuration that runs automatically on GitHub whenever code is pushed.

---

## Git Initialization and Commit History

The repository was initialized using `git init` and a `.gitignore` file was created to ensure
that unnecessary files such as `__pycache__`, `.pytest_cache`, virtual environments, and log
files were never tracked by Git. Over the course of the project, more than fifteen meaningful
commits were made, each following a conventional commit message format. Commit messages were
prefixed with labels such as `feat:` for new features, `fix:` for bug fixes, `test:` for
test additions, `ci:` for pipeline changes, `docs:` for documentation updates, and `refactor:`
for code improvements. This approach was followed to make the commit history readable and
professional, so that anyone reviewing the repository can understand what changed and why.

---

## Branch Strategy

Three types of branches were used in this project. The `main` branch was kept as the stable,
production-ready branch. The `develop` branch was used as the integration branch where all
features were collected before being released to main. Feature branches were created for each
individual piece of work. The branch `feature/power-modulo` was created to add the power and
modulo operations, and `feature/sqrt-abs` was created to add square root and absolute value.
Once the work on a feature branch was complete, it was merged into develop, and once develop
was stable, it was merged into main. All feature branches were deleted after merging to keep
the repository clean.

---

## Merge Types

Two types of merges were demonstrated in this project to show the difference between them.

A fast-forward merge was performed when `feature/power-modulo` was merged into `develop`. This
type of merge happens when the target branch has no new commits since the feature branch was
created. In this case, Git simply moves the branch pointer forward without creating a separate
merge commit. The history appears linear as if the work was done directly on develop.

A non-fast-forward merge was performed when `feature/sqrt-abs` was merged into `develop`, and
again when `develop` was merged into `main`. The `--no-ff` flag was used to force Git to always
create a merge commit even when a fast-forward was possible. This preserves the fact that a
feature was developed on a separate branch, making the branch history visible in the commit graph.

---

## Merge Conflict

A merge conflict was intentionally created to demonstrate how conflicts arise in team environments
and how they are resolved. A file called `conflict_demo.py` was created on both the
`feature/conflict-demo` branch and the `develop` branch with different content on each. When the
merge was attempted, Git detected that the same file had been modified in two different ways and
could not automatically decide which version to keep. The conflict was resolved manually by editing
the file to contain the correct final version, after which the resolved file was staged and
committed. This commit is visible in the repository history as `fix: resolve merge conflict in
conflict_demo.py manually`.

---

## Tagging and Versioning

Two annotated tags were created to mark releases. The tag `v1.0` was created after the core
calculator operations were implemented with unit tests and the CI pipeline was set up. The tag
`v2.0` was created after all additional operations, integration tests, quality assurance work,
and conflict resolution were complete. Both tags were pushed to GitHub and are visible under
the Releases and Tags section of the repository.

---

## Unit Testing

Unit tests were written using pytest and are located in `tests/test_unit.py`. A total of thirty
unit tests were written, each testing a single function in complete isolation. Three categories
of test cases were covered. Normal cases test the function with expected everyday input, for
example verifying that `add(2, 3)` returns `5`. Edge cases test boundary or unusual but valid
input, such as passing zero or negative numbers. Failure cases verify that the function raises
the correct error when given invalid input, for example confirming that `divide(5, 0)` raises
a `ValueError` with the message "Cannot divide by zero". This coverage ensures that every
function behaves correctly across all possible scenarios.

---

## Integration Testing

Integration tests are located in `tests/test_integration.py` and were written to test multiple
calculator functions working together, rather than in isolation. For example, one test verifies
that `divide(subtract(100, 20), 4)` correctly returns `20.0`, meaning the output of subtract
is correctly passed into divide. Another test chains four operations together to verify a complex
expression. These tests simulate real-world usage where components interact with each other, and
they catch bugs that unit tests alone would miss.

---

## Quality Assurance

Quality assurance was demonstrated in two ways. First, a bug was intentionally introduced in a
file called `calculator_buggy_demo.py` where the divide function was written to return `a * b`
instead of `a / b`. This bug was committed to the repository with the message `bug: introduce
divide bug — returns product instead of quotient`. The fix was then applied and committed
separately with the message `fix: correct divide bug — use division not multiplication`. This
commit pair shows the full QA cycle of identifying a problem and resolving it.

Second, the code style tool `flake8` was used to check the codebase for formatting and style
violations. When flake8 was run, it reported unused imports, lines that were too long, and
missing blank lines between functions. All of these issues were fixed and committed with the
message `fix: resolve all flake8 linting errors (F401, E501, E302)`. After the fix, running
`flake8 calculator/ tests/` produced no output, confirming that the code is fully clean.

---

## CI/CD Pipeline

The CI/CD pipeline was configured using GitHub Actions and is defined in `.github/workflows/ci.yml`.
This pipeline runs automatically every time code is pushed to the `main`, `develop`, or any
`feature/*` branch, and also runs on every pull request targeting `main` or `develop`. The
pipeline consists of two jobs. The first job, called `quality`, installs flake8 and runs it
against the calculator and tests folders to check for any code style violations. The second job,
called `test`, only runs after the quality job passes. It installs pytest and pytest-cov, runs
the unit tests, runs the integration tests, and finally generates a code coverage report showing
which lines of the calculator module are covered by tests. This pipeline ensures that no broken
or poorly formatted code can be merged without being caught automatically.

---

## How to Run the Project

To run this project locally, the dependencies must be installed first using the command
`pip install pytest pytest-cov flake8`. Once installed, all tests can be run with `pytest -v`,
the coverage report can be generated with `pytest --cov=calculator --cov-report=term-missing`,
and the linter can be run with `flake8 calculator/ tests/`.

---

## Tags

| Tag | Description |
|-----|-------------|
| v1.0 | Initial release with core operations, unit tests, and CI pipeline |
| v2.0 | Full release with all operations, integration tests, QA cycle, and conflict resolution |
