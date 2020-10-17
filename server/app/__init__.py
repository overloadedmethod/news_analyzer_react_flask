__author__ = "Vladimir"

from app.celery import make_celery
from app.repo import Repo
from settings import CELERY_BROKER, CELERY_RESULTS, MONGODB_URI
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from app.words_utils import proccess_articles
from .tasks import add_together, fetch_for_day, fetch_last_news

app = Flask(__name__)
app.config["CELERY_BROKER"] = CELERY_BROKER
app.config["CELERY_RESULTS"] = CELERY_RESULTS
app.config["MONGO_URI"] = MONGODB_URI
celery = make_celery(app)

mongo = PyMongo(app)

repo = Repo(mongo)


@app.route("/", methods=["GET"])
def index_page():
    return f"hello world"


@app.route("/news", methods=["GET"])
def news_and_stats():
    articles, stats = repo.fetch_news()
    if any(articles):
        return jsonify({"articles": articles, "stats": stats})

    fetched = fetch_last_news(5)
    articles = fetched["articles"] if "articles" in fetched else []
    stats = proccess_articles(fetched)
    repo.store_news(articles, stats)
    return jsonify({"articles": articles, "stats": stats})
