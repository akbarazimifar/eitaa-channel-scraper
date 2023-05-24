from typing import List
import abc


class BaseRepository(abc.ABC):
    @abc.abstractmethod
    def create_channel(self, channel_info: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def add_msg_to_channel(self, channel_name: str, msgs: List[str]) -> None:
        raise NotImplementedError


class SqlRepository(BaseRepository):
    def create_channel(self, channel_info: str) -> None:
        pass

    def add_msg_to_channel(self, channel_name: str, msgs: List[str]) -> None:
        pass
