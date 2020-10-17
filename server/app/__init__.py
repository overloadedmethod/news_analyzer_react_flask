__author__ = "Vladimir"

from app.celery import make_celery
from settings import CELERY_BROKER, CELERY_RESULTS, MONGODB_URI
from flask import Flask
from flask_pymongo import PyMongo

from .tasks import add_together

app = Flask(__name__)
app.config["CELERY_BROKER"] = CELERY_BROKER
app.config["CELERY_RESULTS"] = CELERY_RESULTS
app.config["MONGO_URI"] = MONGODB_URI
celery = make_celery(app)

mongo = PyMongo(app)


@app.route("/", methods=["GET"])
def index_page():
    # mongo.db.create_collection("news")
    result = add_together.delay(23, 42)
    result = result.wait()
    return f"hello world db is exists {mongo.db.list_collection_names()} celery result {result}"


# def view_logs():
#     from pprint import pprint

#     # fetch all logs and show them
#     data = list(db.page_access_log.find({}))
#     pprint(data)
