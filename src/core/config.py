from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "base"
    app_version: str = "0.1.0"
    debug: bool = False
    log_level: str = "INFO"


settings = Settings()
