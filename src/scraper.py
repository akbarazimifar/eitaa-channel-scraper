from typing import Tuple, List

from bs4 import BeautifulSoup

from core.config import get_settings

SETTINGS = get_settings()


class MessageScraper:
    """
    extracts data from html.
    """

    def extract_channel_info(self, channel_text: str) -> Tuple[int | None, str]:
        return 1000, "some str"

    def extarct_messages(self, messages_text: str) -> Tuple[int | None, List[str]]:
        return 10, ["msg1", "msg2"]
