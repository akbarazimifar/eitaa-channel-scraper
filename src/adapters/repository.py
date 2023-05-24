from typing import List
import abc

from pymongo import MongoClient

from core.config import get_settings


SETTINGS = get_settings()


class BaseRepository(abc.ABC):
    @abc.abstractmethod
    def create_channel(self, channel_name: str, channel_info: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def add_msg_to_channel(self, channel_name: str, msgs: List[str]) -> None:
        raise NotImplementedError


class ConsoleRepository(BaseRepository):
    def create_channel(self, channel_name: str,channel_info: str) -> None:
        print(channel_name)
        print(channel_info)
        print("###############")

    def add_msg_to_channel(self, channel_name: str, msgs: List[str]) -> None:
        print(channel_name)
        print(msgs)
        print("###############")


class MongoRepository(BaseRepository):
    def __init__(self, client: MongoClient) -> None:
        self._db = client["eitaa"]

    def create_channel(self, channel_name: str, channel_info: str) -> None:
        self._db[SETTINGS.CHANNELS_COLLECTION].update_one(
            {"name": channel_name},
            {"$set": {"info": channel_info} },
            upsert=True
        )

    def add_msg_to_channel(self, channel_name: str, msgs: List[str]) -> None:
        for msg in msgs:
            self._db[SETTINGS.MESSAGES_COLLECTION].insert_one({"channel": channel_name, "text": msg})
