from settings import CELERY_BROKER, CELERY_RESULTS
from celery import Celery
from flask import Flask

flask = Flask(__name__)


app = Celery(__name__, broker=CELERY_BROKER, backend=CELERY_RESULTS)


@app.task()
def add_together(a, b):
    print("celery is called")
    return a + b