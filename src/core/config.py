from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    CHANNEL_NAME: str = "world_py"
    START_MESSAGE_OFFSET: int = 10
    EITAA_DOMAIN: str = "eitaa.com"
    MESSAGE_FETCH_INTERVAL: int = 3000
    CHANNEL_REFRESH_INTERVAL: int = 60000

    INFO_CONTAINER_SELECTOR: str = ".etme_channel_info"
    MESSAGE_CONTAINER_SELECTOR: str = ".etme_widget_message_wrap"

    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
