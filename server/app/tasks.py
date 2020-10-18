from app.repo import Repo
from flask_pymongo import PyMongo
from app.words_utils import proccess_articles
from app.news_fetcher import Fetcher
from flask_executor.executor import Executor
from settings import CELERY_BROKER, CELERY_RESULTS, MONGODB_URI

# from celery import Celery
from flask import Flask

flask = Flask(__name__)

executor = Executor(flask)
mongo = PyMongo(flask, f"{MONGODB_URI}/news_analyzer")

repo = Repo(mongo)


def fetch_for_day(day: int, token: str):
    fetched = Fetcher(token).set_day_before(day).set_amount(3).fetch()
    articles = fetched["articles"] if "articles" in fetched else []
    stats = proccess_articles(fetched)
    repo.store_day(day, articles, stats)
