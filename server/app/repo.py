from flask_pymongo import PyMongo
from datetime import datetime


class Repo:
    def __init__(self, driver: PyMongo):
        self.driver = driver

    def fetch_news_by_amount(self, amount: int):
        vals = self.driver.db.articles.find_one({"amount": amount})
        if not vals:
            return None, None
        return vals["articles"], vals["stats"]

    def fetch_news_by_days(self, days: int):
        vals = self.driver.db.articles.find_one({"amount": days})
        if not vals:
            return None, None
        return vals["articles"], vals["stats"]

    def store_news(self, articles, stats, days):
        self.driver.db.articles.insert_one(
            {
                "days": days,
                "articles": articles,
                "stats": stats,
                "amount": len(articles),
                "timestamp": int(datetime.utcnow().timestamp()),
            }
        )

    def store_day(self, day, articles, stats):
        self.driver.db.days.insert_one(
            {
                "day": day,
                "articles": articles,
                "stats": stats,
                "amount": len(articles),
                "timestamp": int(datetime.utcnow().timestamp()),
            }
        )

    def fetch_days(self):
        vals = list(self.driver.db.days.find({}, {"_id": False}))
        return vals