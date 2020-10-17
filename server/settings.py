__author__ = "Vladimir"

DB_NAME = "news_analyzer"
MONGODB_URI = "mongodb://localhost:27017"
MONGODB_URL = "news_analyzer"
CELERY_BROKER = f"{MONGODB_URI}/celery_tasks"
CELERY_RESULTS = f"{MONGODB_URI}/celery_results"
