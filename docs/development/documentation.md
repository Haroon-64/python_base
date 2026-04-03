# Documentation Guide

This project uses [**MkDocs**](https://www.mkdocs.org/) with the [**Material for MkDocs**](https://squidfunk.github.io/mkdocs-material/) theme to generate its static documentation site.

---

## What is MkDocs?

MkDocs is a fast, simple static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.

### Material Theme

We use the Material theme, which provides:

- Responsive design (mobile/table/desktop).
- Dark/Light mode switching.
- Integrated search.
- Code syntax highlighting with copy-to-clipboard.

---

## How to Add New Docs

### 1. Create a Markdown File

All documentation files reside in the `docs/` directory. Create a new `.md` file in the appropriate subdirectory.

```bash
touch docs/development/new-guide.md
```

### 2. Update Navigation

Open **`mkdocs.yml`** and add your new page to the `nav` section.

```yaml
nav:
  - Home: index.md
  - Development Guide:
      - New Guide: development/new-guide.md
```

### 3. Preview Locally

Use the built-in script to start the development server with hot-reloading:

```bash
uv run docs
```

Visit `http://localhost:8000` to see your changes in real-time.

---

## Technical Documentation (`mkdocstrings`)

We use [**mkdocstrings**](https://mkdocstrings.github.io/) to automatically generate documentation from your source code's docstrings.

### Usage

To insert API documentation for a Python module, use the following syntax in any Markdown file:

```markdown
::: path.to.module
    options:
      show_root_heading: true
```

Example (from `reference.md`):

```markdown
::: scripts
```

Ensure your docstrings follow a consistent style (e.g., Google or Google-style) for the best results.
