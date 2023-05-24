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

    MONGO_HOST: str = "localhost"
    MONGO_PORT: str = "27017"
    MONGO_USER: str = "user"
    MONGO_PASSWORD: str = "pass"
    CHANNELS_COLLECTION: str = "channels"
    MESSAGES_COLLECTION: str = "messages"

    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

    @property
    def db_uri(self) -> str:
        return f"mongodb://{self.MONGO_USER}:{self.MONGO_PASSWORD}@{self.MONGO_HOST}:{self.MONGO_PORT}/"


@lru_cache
def get_settings() -> Settings:
    return Settings()
