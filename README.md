# Task 1: Pipeline Setup and Testing Example

This repository contains a simple project setup designed to demonstrate a Continuous Integration (CI) pipeline using GitHub Actions, complete with GitLeaks for secret scanning and a basic unit testing framework.

## What's Included

The primary goal of this repository is to demonstrate a functional CI pipeline setup. We've implemented the following components:

1. **GitHub Actions Workflow (`.github/workflows/ci.yml`)**:
   - Triggers on `push` and `pull_request` to any branch.
   - Sets up a Python 3.10 environment.
   - Runs **GitLeaks** as a pipeline step to scan for hardcoded secrets.
   - Executes real Python unit tests.
   - Contains placeholder steps for Build and Deploy processes.

2. **GitLeaks Pre-commit Hook (`.pre-commit-config.yaml`)**:
   - Configures GitLeaks to run automatically before every local commit, preventing secrets from ever being committed to the repository.

3. **Sample Application & Tests**:
   - `main.py`: Contains simple Python math functions (`add_numbers` and `divide_numbers`) with type hinting and exception handling.
   - `test_main.py`: Contains actual unit tests using Python's built-in `unittest` framework to verify the behavior of the functions in `main.py`, including testing division-by-zero errors.

## How to Use and Test

### 1. Run Unit Tests Locally
You can manually run the unit tests to verify the core logic works as expected:
```bash
python -m unittest test_main.py
```
You should see output similar to this if the tests pass:
```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

### 2. Set Up the GitLeaks Pre-commit Hook
To ensure secrets are not committed locally, install and activate the pre-commit hook (requires Python and `pip`):
```bash
pip install pre-commit
pre-commit install
```
Now, GitLeaks will run automatically whenever you run `git commit`.

### 3. Test the CI Pipeline (GitHub Actions)
The pipeline is fully configured. To see it in action:
1. Push this code to a new or existing repository on GitHub.
2. Navigate to the **"Actions"** tab in your GitHub repository.
3. You will see the `CI Pipeline` workflow running automatically. It will check out the code, set up Python, run GitLeaks, execute the tests, and simulate the build/deploy steps.

Alternatively, if you create a Pull Request, GitHub will run these checks before allowing the merge.