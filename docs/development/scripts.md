# Scripting & Task Automation

The Base Python Project uses a minimalist, native approach to task automation, consolidating all logic in **[src/scripts.py](../../src/scripts.py)**. This eliminates the need for external tools like `make` or `just`, leveraging **`uv run`** as the primary developer interface.

---

## Common Tasks

All tasks are defined in `pyproject.toml` under `[project.scripts]` and can be executed via `uv run <command>`.

### Quality & Testing

| Command | Action |
| --- | --- |
| `uv run check` | Runs **formatting**, **linting**, and **type checking** in series. |
| `uv run test` | Executes the full **pytest** suite with coverage reporting. |
| `uv run lint` | Runs `ruff check` on `src/` and `tests/`. |
| `uv run format` | Runs `ruff format` on `src/` and `tests/`. |

### Operations

| Command | Action |
| --- | --- |
| `uv run dev` | Starts the application with `DEBUG=true` and verbose logging. |
| `uv run start` | Starts the application in production mode. |
| `uv run clean` | Removes all temporary caches (`.pytest_cache`, `dist/`, etc.). |
| `uv run sync` | Synchronizes the local virtual environment with `uv.lock`. |
| `uv run lock` | Updates the `uv.lock` dependency file. |

### Documentation

| Command | Action |
| --- | --- |
| `uv run docs` | Starts the **MkDocs** development server (hot-reloading). |
| `uv run build-docs` | Generates a static HTML build of the documentation in `site/`. |

---

## Adding New Scripts

To add a new automation task:

1. **Define the Logic**: Open `src/scripts.py` and add a new Python function.

    ```python
    def my_task() -> None:
        """Informative docstring."""
        print("Running my custom task...")
        # Use run_command() for shell operations
    ```

2. **Register in `pyproject.toml`**: Add your task to the `[project.scripts]` section.

    ```toml
    [project.scripts]
    my-task = "scripts:my_task"
    ```

3. **Use It**: Run your task via `uv run my-task`.

---

## Best Practices

- **Use `run_command`**: This helper function in `scripts.py` ensures that if a step fails, the entire task exits with a non-zero code.
- **Keep it Lean**: Only add tasks that are strictly necessary for development or CI/CD.
