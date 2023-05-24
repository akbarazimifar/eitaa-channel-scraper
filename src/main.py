import logging
import time

import requests
from pymongo import MongoClient

from adapters import MongoRepository
from crawler import ChannelCrawler
from scraper import MessageScraper

from core.config import get_settings


SETTINGS = get_settings()

logging.basicConfig(level=SETTINGS.LOG_LEVEL)
logger = logging.getLogger(__name__)


def main() -> None:
    with requests.Session() as session:
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        })

        crawler = ChannelCrawler(
            http_agent=session,
            scraper=MessageScraper(),
            repository=MongoRepository(MongoClient(SETTINGS.db_uri))
        )

        while True:
            crawler.start()

            logger.info(f"Channel will be refreshed in {SETTINGS.CHANNEL_REFRESH_INTERVAL / 1000} seconds")
            time.sleep(SETTINGS.CHANNEL_REFRESH_INTERVAL / 1000)


if __name__ == "__main__":
    logger.info(f"Starting crawler for channel: `{SETTINGS.CHANNEL_NAME}`")

    try:
        main()

    except Exception as e:
        logger.exception(e, exc_info=True)
