import logging
import motor.motor_asyncio
from config import DB_URL, DB_NAME  # Explicit imports are usually safer

logging.basicConfig(level=logging.INFO)

class NewsDB:
    def __init__(self, db_url: str, db_name: str):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(db_url)
        self.database = self.client[db_name]

        # Collections
        self.posted_news = self.database["posted_news"]
        self.rss_feeds = self.database["rss_feeds"]
        self.channels = self.database["channels"]

    # --- News Tracking ---

    async def is_posted(self, link: str) -> bool:
        try:
            result = await self.posted_news.find_one({"link": link})
            return result is not None
        except Exception as e:
            logging.error(f"Error checking if posted ({link}): {e}")
            return False

    async def mark_posted(self, link: str):
        try:
            await self.posted_news.update_one(
                {"link": link},
                {"$setOnInsert": {"link": link}},
                upsert=True
            )
        except Exception as e:
            logging.error(f"Error marking as posted ({link}): {e}")

    async def get_total_posted(self) -> int:
        """Gets the total number of articles ever posted."""
        try:
            return await self.posted_news.count_documents({})
        except Exception as e:
            logging.error(f"Error getting total posted count: {e}")
            return 0

    # --- RSS Feed Management ---

    async def add_rss_db(self, url: str):
        try:
            await self.rss_feeds.update_one(
                {"url": url},
                {"$setOnInsert": {"url": url}},
                upsert=True
            )
        except Exception as e:
            logging.error(f"Error adding RSS feed ({url}): {e}")

    async def rem_rss_db(self, url: str):
        try:
            await self.rss_feeds.delete_one({"url": url})
        except Exception as e:
            logging.error(f"Error removing RSS feed ({url}): {e}")

    async def get_all_rss(self) -> list:
        try:
            feeds = await self.rss_feeds.find({}).to_list(None)
            return [feed["url"] for feed in feeds if "url" in feed]
        except Exception as e:
            logging.error(f"Error fetching RSS feeds: {e}")
            return []

    # --- Channel Management ---

    async def add_channel_db(self, chat_id: int):
        try:
            await self.channels.update_one(
                {"chat_id": int(chat_id)},
                {"$setOnInsert": {"chat_id": int(chat_id)}},
                upsert=True
            )
        except Exception as e:
            logging.error(f"Error adding channel ({chat_id}): {e}")

    async def rem_channel_db(self, chat_id: int):
        try:
            await self.channels.delete_one({"chat_id": int(chat_id)})
        except Exception as e:
            logging.error(f"Error removing channel ({chat_id}): {e}")

    async def get_all_channels(self) -> list:
        try:
            channels = await self.channels.find({}).to_list(None)
            return [ch["chat_id"] for ch in channels if "chat_id" in ch]
        except Exception as e:
            logging.error(f"Error fetching channels: {e}")
            return []

# Initialize the database instance
db = NewsDB(DB_URL, DB_NAME)
