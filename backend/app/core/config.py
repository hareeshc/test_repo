from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "workspace-analytics-api"
    environment: str = "dev"
    database_url: str = "sqlite:///./workspace_analytics.db"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="WA_")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
