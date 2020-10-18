from flask_pymongo import PyMongo


class Repo:
    def __init__(self, driver: PyMongo):
        self.driver = driver

    def fetch_news(self, amount: int):
        vals = self.driver.db.collection_names()
        # return [], {}
        return None, None

    def store_news(self, articles, stats):
        pass
