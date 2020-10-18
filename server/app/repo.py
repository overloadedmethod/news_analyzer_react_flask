from flask_pymongo import PyMongo
from datetime import datetime


class Repo:
    def __init__(self, driver: PyMongo):
        self.driver = driver

    def fetch_news(self, amount: int):
        vals = self.driver.db.articles.find_one({"amount": amount})
        if not vals:
            return None, None
        return vals["articles"], vals["stats"]

    def store_news(self, articles, stats):
        self.driver.db.articles.insert_one(
            {
                "articles": articles,
                "stats": stats,
                "amount": len(articles),
                "timestamp": int(datetime.utcnow().timestamp()),
            }
        )
