from core.config import Settings


def test_settings_load():
    """Verify that settings can be loaded from environment."""
    settings = Settings()
    assert hasattr(settings, "log_level")
    assert isinstance(settings.log_level, str)


def test_settings_default_values(test_settings):
    """Verify default values if any."""
    assert test_settings.log_level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
