# Commits & Versioning

This project uses modern standards for Git management to ensure a clean, historical record and automated release cycles.

---

## Conventional Commits

We follow the [**Conventional Commits**](https://www.conventionalcommits.org/) specification for commit messages. This standard allows us to automate changelog generation and provide a consistent history.

### Format

`<type>[optional scope]: <description>`

### Key Types

| Type | Use Case |
| --- | --- |
| `feat` | A new feature or capability. |
| `fix` | A bug fix. |
| `docs` | Documentation changes only. |
| `style` | Formatting or non-functional changes. |
| `refactor` | Code changes that neither fix a bug nor add a feature. |
| `perf` | Changes that improve performance. |
| `test` | Adding or correcting tests. |
| `chore` | Maintenance tasks (dependency updates, build scripts). |

### Example

`feat(auth): add GitHub OAuth provider support`

---

## Dynamic Versioning (`hatch-vcs`)

We do **not** manually update versions in `pyproject.toml`. Instead, versions are dynamically generated from **Git tags**, powered by [**hatch-vcs**](https://github.com/ofek/hatch-vcs).

### How It Works

- **v0.1.0** (tagged): The project version will be reported as `0.1.0`.
- **Commits since tag**: The version will include the number of commits and a hash (e.g., `0.1.1.dev5+gabcdef`).

### Releasing a New Version

1. **Tag the commit**:

    ```bash
    git tag v0.2.0
    git push origin v0.2.0
    ```

2. **GitHub Actions**: CI pipeline will automatically pick up the tag and can be configured to publish a new release artifact.

---

## Branching Strategy

- **`main`**: The stable branch. All code must pass CI/CD tests before being merged.
- **Feature Branches**: Create descriptive branches (e.g., `feat/auth-system`) for new work.
- **Pull Requests**: All changes require a PR with at least one review and a successful "Tests" workflow execution.
