import time
from typing import Tuple, List

from requests import Session

from core.config import get_settings
from scraper import MessageScraper
from adapters import BaseRepository


SETTINGS = get_settings()


class ChannelCrawler:
    """
    fetches data from channel
    """

    def __init__(
        self,
        http_agent: Session,
        scraper: MessageScraper,
        repository: BaseRepository,
    ) -> None:
        self.channel_name = SETTINGS.CHANNEL_NAME
        self.channel_url = f"https://{SETTINGS.EITAA_DOMAIN}/{SETTINGS.CHANNEL_NAME}"
        self._http_agent = http_agent
        self._scraper = scraper
        self._repository = repository

    def start(self) -> int:
        msg_offset, info_str = self.get_channel_info()
        self._repository.create_channel(info_str)

        if self.get_prev_run_offset and self.get_prev_run_offset >= msg_offset:
            return msg_offset

        current_offset = msg_offset
        while True:
            time.sleep(SETTINGS.MESSAGE_FETCH_INTERVAL / 1000)
            next_page_offset, messages = self.get_msg_page(current_offset)
            self._repository.add_msg_to_channel(self.channel_name, messages)

            if (
                not next_page_offset
                or next_page_offset == 1
                or (
                    self.get_prev_run_offset
                    and next_page_offset <= self.get_prev_run_offset
                )
            ):
                break

            current_offset = next_page_offset

        self.update_channel_offset(msg_offset)

        return msg_offset

    @property
    def get_prev_run_offset(self) -> int | None:
        try:
            with open(f"./offsets/{self.channel_name}", "r") as f:
                return int(f.read())

        except FileNotFoundError:
            return None

    def update_channel_offset(self, offset: int) -> None:
        with open(f"./offsets/{self.channel_name}", "w+") as f:
            data = f.read()
            if data:
                current_offset = int(data)
                if offset > current_offset:
                    f.seek(0)
                    f.write(str(offset))
                    f.truncate()
            else:
                f.write(str(offset))

    def get_msg_page(self, offset: int) -> Tuple[int, List[str]]:
        return self._scraper.extarct_messages(
            self._fetch_msg_page(offset))

    def get_channel_info(self) -> Tuple[int, str]:
        return self._scraper.extract_channel_info(
            self._fetch_channel())

    def _fetch_msg_page(self, offset: int) -> str:
        return self._http_agent.get(f"{self.channel_url}?before={offset}").text

    def _fetch_channel(self) -> str:
        return self._http_agent.get(self.channel_url).text
