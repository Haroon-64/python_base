# Base Python Project

Welcome to the **Base Python Project** template. This repository is designed as a foundational boilerplate for professional, high-quality Python applications, emphasizing **observability**, **type safety**, and **developer experience**.

---

## Core Philosophy

This base repo rejects complex toolchains in favor of native Python power combined with **`uv`**, the extremely fast Python package and project manager.

---

## Tooling & DX

- **Fast Dependency Management**: Powered by [`uv`](https://github.com/astral-sh/uv).
- **Scripting & Task Automation**: Centralized logic in `src/scripts.py` accessible via `uv run`.
- **Dynamic Versioning**: Powered by `hatch-vcs` (versioning via Git tags).

## Type Safety & Quality

- **Formatting & Linting**: Super-fast checks via [`ruff`](https://github.com/astral-sh/ruff).
- **Strict Typing**: Integrated [`mypy`](https://github.com/python/mypy) support.
- **Git Hygiene**: Pre-configured hooks via `pre-commit`.

## Observability

- **Structured Logging**: Pre-configured [`structlog`](https://github.com/hynek/structlog).
- **Configuration Management**: Type-safe settings via `pydantic-settings`.

---

## Getting Started

1. **Clone & Setup**:

    ```bash
    uv sync
    ```

2. **Run Development Mode**:

    ```bash
    uv run dev
    ```

3. **Verify Everything**:

    ```bash
    uv run check
    uv run test
    ```

---

## Explore the Docs

- **[Development Guides](development/scripts.md)**: Task automation, quality checks, and commit standards.
- **[Architecture](development/features.md)**: How to add new features and organize code.
- **[Documentation](development/documentation.md)**: How to use MkDocs and add new pages.
- **[API Reference](reference.md)**: Code-level documentation.
