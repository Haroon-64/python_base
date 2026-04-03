# Base

- Base project to setup python apps

## included

- UV: package/env and config management
- TOX: test automation/matrix
- Ruff: linting and formatting
- Mypy: type checking
- Logging: structured logging
- actions for testing
- pre-commit:
  - talisman: secret scanning
  - ruff
  - pytest
  - mypy

## config

- setup uv and pre-commit
  - install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - sync dependencies: `uv sync`
  - install pre-commit: `uv pre-commit install`

- define start/dev scripts in tasks.py
