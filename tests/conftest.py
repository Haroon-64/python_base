import os
from unittest.mock import patch

import pytest

from core.config import settings


@pytest.fixture(autouse=True)
def mock_env():
    """Ensure environment variables are isolated for tests."""
    with patch.dict(os.environ, {"DEBUG": "true", "LOG_LEVEL": "DEBUG"}):
        yield


@pytest.fixture
def test_settings():
    """Provide common test settings."""
    return settings
