__author__ = "Vladimir"
from datetime import datetime, timedelta

from flask_executor.executor import Executor

from app.repo import Repo
from settings import CELERY_BROKER, CELERY_RESULTS, MONGODB_URI
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from app.words_utils import proccess_articles
from app.tasks import fetch_for_day, executor
from app.news_fetcher import Fetcher


app = Flask(__name__)
app.config["CELERY_BROKER"] = CELERY_BROKER
app.config["CELERY_RESULTS"] = CELERY_RESULTS
app.config["MONGO_URI"] = MONGODB_URI


mongo = PyMongo(app, f"{MONGODB_URI}/news_analyzer")

repo = Repo(mongo)


@app.route("/", methods=["GET"])
def index_page():
    return f"run client at client folder by npm start"


@app.route("/news", methods=["GET"])
def news_and_stats():
    token = request.args.get("token")
    amount = int(request.args.get("amount"))
    days = int(request.args.get("days"))
    articles, stats = repo.fetch_news_by_amount(amount)
    if articles:
        return jsonify({"articles": articles, "stats": stats})

    fetched = Fetcher(token).set_amount(amount).set_day_before(days).fetch()
    articles = fetched["articles"] if "articles" in fetched else []
    stats = proccess_articles(fetched)
    repo.store_news(articles, stats, days)
    return jsonify({"articles": articles, "stats": stats})


# @app.route("/test", methods=["GET"])
# def db_testing():
#     executor.submit_stored("fibonacci", fib, 10)
#     future = executor.futures.pop("fibonacci")
#     return jsonify({"result": future.result()})


@app.route("/test", methods=["GET"])
def db_testing():
    token = request.args.get("token")
    for day in range(7):
        executor.submit(fetch_for_day, day, token)

    return "OK"
