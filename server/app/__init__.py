__author__ = "Vladimir"
from datetime import datetime, timedelta
from app.celery import make_celery
from app.repo import Repo
from settings import CELERY_BROKER, CELERY_RESULTS, MONGODB_URI
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from app.words_utils import proccess_articles
from .tasks import fetch_for_day, fetch_last_news, fib
from app.news_fetcher import Fetcher


app = Flask(__name__)
app.config["CELERY_BROKER"] = CELERY_BROKER
app.config["CELERY_RESULTS"] = CELERY_RESULTS
app.config["MONGO_URI"] = MONGODB_URI
celery = make_celery(app)


mongo = PyMongo(app, f"{MONGODB_URI}/news_analyzer")

repo = Repo(mongo)


@app.route("/", methods=["GET"])
def index_page():
    return f"hello world"


@app.route("/news", methods=["GET"])
def news_and_stats():
    token = request.args.get("token")
    amount = int(request.args.get("amount"))
    articles, stats = repo.fetch_news_by_amount(amount)
    if articles:
        return jsonify({"articles": articles, "stats": stats})

    fetched = Fetcher(token).set_amount(amount).fetch()
    articles = fetched["articles"] if "articles" in fetched else []
    stats = proccess_articles(fetched)
    repo.store_news(articles, stats)
    return jsonify({"articles": articles, "stats": stats})


@app.route("/news/day")
def fetch_for_day():
    token = request.args.get("token")
    day = request.args.get("day")


@app.route("/test", methods=["GET"])
def db_testing():
    from_date = datetime.now() - timedelta(days=7)
    fetch = Fetcher().set_amount(10).set_day_before(3).fetch()
    return "OK"
