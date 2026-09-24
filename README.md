# LLMOps Lab 01 — Engineering Environment, Git, Python, Make, and Automated Testing

This lab introduces the software-engineering workflow used throughout the semester in CSYE 7374 — Large Language Models Operations (LLMOps).

## Purpose

The goal of this first lab is to establish the basic development workflow students will use all semester:

- clone a repository
- create a Python virtual environment
- install dependencies
- run tests and linting through `make`
- implement small Python functions
- use Git to commit and push changes
- interpret automated test results from GitHub Actions

## Learning Objectives

By completing this lab, students should be able to:

1. Clone and work with a Git repository.
2. Understand a basic Python project structure.
3. Create and use a Python virtual environment.
4. Install project dependencies.
5. Run a project through a Makefile.
6. Read and understand function specifications.
7. Implement small Python functions.
8. Write or understand basic `pytest` tests.
9. Use Git to commit and push changes.
10. Interpret automated test results from GitHub Actions.
11. Use an AI coding assistant responsibly to help implement and debug code.
12. Understand the basic development → test → commit → CI workflow used in LLMOps.

## Prerequisites

Before starting this lab, make sure you have:

- Python 3.11 or newer installed
- `git` installed
- access to a GitHub repository
- a terminal or command prompt

## Repository Structure

```text
llmops-lab01/
├── README.md
├── Makefile
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   └── system_info.py
├── tests/
│   └── test_system_info.py
└── .github/
    └── workflows/
        └── tests.yml
```

## Installation

From the repository root, run:

```bash
make install
```

This will create a local Python virtual environment in `.venv` and install the required dependencies.

## Running Tests

Run the full test suite with:

```bash
make test
```

## Running Linting

Run linting with:

```bash
make lint
```

## Running the Application

A small demonstration target is also provided:

```bash
make run
```

This target is intended to exercise the same functions you will implement.

## What to Implement

The module `src/system_info.py` contains the required function stubs.

You must implement the following functions:

- `get_python_version()`
- `get_platform_name()`
- `normalize_name(name)`
- `build_environment_report(name)`

Do not remove the TODO markers. Your job is to complete the missing functionality and verify the behavior with tests.

## Functional Specifications

### `get_python_version()`

Return the current Python version as a human-readable string.

Requirements:

- return a string
- obtain the version from Python runtime information
- do not hard-code a version number

### `get_platform_name()`

Return the current operating-system/platform name.

Requirements:

- return a non-empty string
- obtain the information from the Python runtime
- do not hard-code `Linux`, `macOS`, or another platform

### `normalize_name(name)`

Normalize a user-provided name.

Requirements:

- remove leading whitespace
- remove trailing whitespace
- convert the result to a consistent display form
- reject values that are not strings
- reject an empty name after trimming

Use appropriate Python exceptions for invalid input.

### `build_environment_report(name)`

Return a dictionary containing:

- `name`
- `python_version`
- `platform`

The values must be generated dynamically.

The `name` value must use `normalize_name()`.

## Testing Expectations

The visible tests in `tests/test_system_info.py` are designed to check observable behaviors.

They cover:

- normal Python version retrieval
- platform retrieval
- name normalization
- whitespace handling
- invalid input
- empty input
- environment report structure
- integration between normalization and environment reporting

The tests should guide you toward the correct behavior without requiring a specific implementation strategy.

## Submission Requirements

Complete the required functionality in `src/system_info.py`, run the test suite, and make sure linting passes.

Then:

1. review the updated files
2. commit your changes
3. push your repository to GitHub
4. confirm that GitHub Actions runs successfully

## AI / Copilot Policy

GitHub Copilot and other AI coding assistants are permitted for this lab. You are responsible for understanding, testing, and validating any code generated with AI assistance.

The purpose of this assignment is not to prevent AI use. The purpose is to ensure that students can read the specification, inspect the starter repository, implement the required behavior, run tests, and debug failures.

Do not submit Copilot conversation history as part of the lab.

## Expected Workflow

A reasonable workflow for this lab is:

1. Read the specification carefully.
2. Inspect the repository structure.
3. Ask Copilot for implementation help if needed.
4. Review any generated code for correctness.
5. Run `make test`.
6. Investigate any failing tests.
7. Adjust the implementation.
8. Run the tests again.
9. Run `make lint`.
10. Commit and push.

The core principle is simple:

AI-generated code must be tested and validated.

## Clean Up

When you are finished, you can remove local build artifacts with:

```bash
make clean
```
