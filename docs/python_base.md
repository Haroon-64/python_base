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
  - mypy
  - pytest

  some are commented out, add as required

## config

- setup uv and pre-commit
  - install talisman: `bash -c "$(curl -fsSL https://raw.githubusercontent.com/thoughtworks/talisman/main/install.sh)"`
      (for windows download binary from `https://github.com/thoughtworks/talisman/releases`)
  - install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - sync dependencies: `uv sync`
  - install pre-commit: `uv pre-commit install`

- define start/dev scripts in tasks.py

## get started

- run `uv run docs`
