from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    CHANNEL_NAME: str
    START_MESSAGE_OFFSET: int
    EITAA_DOMAIN: str
    MESSAGE_FETCH_INTERVAL: int
    CHANNEL_REFRESH_INTERVAL: int

    INFO_CONTAINER_SELECTOR: str
    MESSAGE_CONTAINER_SELECTOR: str

    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_USER: str
    MONGO_PASSWORD: str
    CHANNELS_COLLECTION: str
    MESSAGES_COLLECTION: str

    LOG_LEVEL: str

    class Config:
        env_file = ".env"

    @property
    def db_uri(self) -> str:
        return f"mongodb://{self.MONGO_USER}:{self.MONGO_PASSWORD}@{self.MONGO_HOST}:{self.MONGO_PORT}/"


@lru_cache
def get_settings() -> Settings:
    return Settings()
