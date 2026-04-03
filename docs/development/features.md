# Project Structure & Architecture

This repository adopts a clean, modular structure that separates infrastructure and configuration from application-specific logic.

---

## Core Layout

| Path | Purpose |
| --- | --- |
| `src/core/` | **Infrastructure Layer**: Logging, global settings, and shared utilities. |
| `src/app/` | **Application Layer**: Business logic, API routes, and service controllers. |
| `src/scripts.py` | **Task Layer**: Development and CI/CD automation logic. |
| `tests/` | **Testing Layer**: Multi-stage automated tests. |
| `docs/` | **Documentation Layer**: Comprehensive project guides. |

---

## Adding New Features

Follow these guidelines when expanding the codebase:

### 1. Define Configuration

If your feature requires new settings, add them to **[src/core/config.py](../../src/core/config.py)** as part of the `Settings` class. This ensures they are type-safe and automatically loaded from environment variables.

### 2. Implementation logic

Place implementation code in **`src/app/`**.

- Create a new module (e.g., `src/app/auth.py`) for specific services.
- If you need shared infrastructure (e.g., a database client), place it in `src/core/`.

### 3. Add Tests

For every new feature, add a corresponding test in **`tests/`**.

- Aim for high unit test coverage.
- Use `pytest` fixtures in `conftest.py` for shared setup logic.

---

## Environment Management

- **`.env.example`**: Keep this file updated with all required environment variables.
- **`pydantic-settings`**: All configuration is automatically validated at startup.
- **`uv sync`**: Always run this after pulling changes to ensure your local environment matches the `uv.lock`.

---

## Logging Standards

- **Use `structlog`**: Always use the logger from `src/core/logger.py`.
- **Structured Fields**: Use extra fields for context:

    ```python
    logger.info("user_authenticated", user_id=user.id, provider="github")
    ```

- **Avoid string formatting**: Let `structlog` handle formatting and serialization for structured output (JSON in production).
