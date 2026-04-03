import os
import shutil
import subprocess
import sys

import pytest

from core.config import settings
from core.logger import get_logger, setup_logging

logger = get_logger(__name__)


def run_command(command: str) -> None:
    """Run a shell command and exit with its return code if it fails."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {command}")
        sys.exit(e.returncode)


def dev() -> None:
    """Run the application in development mode."""
    os.environ["DEBUG"] = "true"
    os.environ["LOG_LEVEL"] = "DEBUG"
    setup_logging(debug=True, log_level="DEBUG")
    logger.info("Starting in DEV mode")


def start() -> None:
    """Run the application in production mode."""
    os.environ["DEBUG"] = "false"
    os.environ["LOG_LEVEL"] = "INFO"
    setup_logging(debug=False, log_level=settings.log_level)
    logger.info("Starting in PROD mode")


def test() -> None:
    """Run tests."""
    sys.exit(pytest.main())


def lint() -> None:
    """Run linting checks."""
    logger.info("Running linting checks...")
    run_command("ruff check src tests")


def format() -> None:
    """Run formatting checks."""
    logger.info("Running formatting...")
    run_command("ruff format src tests")


def check() -> None:
    """Run all linting and formatting checks."""
    format()
    lint()
    logger.info("Running type checks...")
    run_command("mypy src")


def docs() -> None:
    """Serve the project documentation."""
    run_command("mkdocs serve")


def build_docs() -> None:
    """Build the project documentation."""
    run_command("mkdocs build")


def clean() -> None:
    """Clean up temporary files and directories."""
    directories = [".pytest_cache", ".mypy_cache", ".ruff_cache", "site", "dist"]
    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            logger.info(f"Removed directory: {directory}")
