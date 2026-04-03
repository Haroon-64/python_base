# Code Quality & Testing

This project maintains high software quality standards through a multi-layered approach to static analysis, type checking, and automated testing.

---

## Static Analysis (`ruff`)

We use [**Ruff**](https://github.com/astral-sh/ruff), an extremely fast Python linter and formatter. Ruff replaces dozens of tools (like `flake8`, `isort`, `black`, and `pyupgrade`) with a single, highly-optimized binary.

### Configuration

Ruff is configured in `pyproject.toml` under `[tool.ruff]`. We currenty enforce:

- **E/F/W**: Standard flake8 errors, warnings, and logical issues.
- **I**: Import sorting and grouping.
- **UP**: Modern Python syntax upgrades.
- **PL**: Pylint-inspired rules for common pitfalls.
- **T20**: Rules against `print` statements (prefer `structlog`).

---

## Type Checking (`mypy`)

Modern Python development relies heavily on type hints. We enforce **strict** typing with [**Mypy**](https://github.com/python/mypy).

### Standards

- All public functions must have return type hints and typed parameters.
- We avoid `Any` wherever possible.
- Run `uv run check` to verify types across the entire `src/` directory.

---

## Automated Checks (`pre-commit`)

We use [**pre-commit**](https://pre-commit.com/) to ensure that every commit meets our quality standards *before* it enters the repository.

### Key Hooks

- **trailing-whitespace/check-yaml/check-toml**: Basic file hygiene.
- **talisman**: Automatically prevents secrets and sensitive data from being committed.
- **ruff**: Automated linting and formatting.
- **mypy**: Type checking.
- **pytest**: Ensures the full test suite passes before every commit.

To run all hooks manually on the current state of the repo:

```bash
pre-commit run --all-files
```

---

## Testing Infrastructure

The testing foundation is built on **pytest** and located in `tests/`.

### Config

- **[conftest.py](../../tests/conftest.py)**: Contains global fixtures and environment mocks (e.g., forcing `DEBUG=true`).
- **`uv run test`**: Runs the suite and generates a coverage report.

### Writing Tests

Place new tests in the `tests/` directory with the prefix `test_`. Use descriptive function names and leverage fixtures from `conftest.py` for common setup logic.
