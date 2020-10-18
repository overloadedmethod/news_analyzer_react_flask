from datetime import datetime, timedelta
import requests


class Fetcher:
    url = "http://newsapi.org/v2/everything"
    language = "en"
    page_size = 5
    sort_by = "publishedAt"
    sources = "bbc-news"
    amount = 5

    def __init__(self, token, days=7) -> None:
        self.api_key = token
        now = datetime.now()
        self.max_iso_str_date = now.isoformat()
        self.min_iso_str_date = datetime.now() - timedelta(days=days)

    def set_token(self, api_key):
        self.api_key = api_key
        return self

    def set_day_before(self, day):
        now = datetime.now()
        self.min_iso_str_date = now - timedelta(days=day)
        self.max_iso_str_date = now - timedelta(days=day - 1)
        return self

    def set_source(self, source):
        self.news_source = source
        return self

    def set_min_date(self, min_iso_str_date):
        self.min_iso_str_date = min_iso_str_date
        return self

    def set_max_date(self, max_iso_str_date):
        self.max_iso_str_date = max_iso_str_date
        return self

    def set_amount(self, amount):
        self.amount = amount
        return self

    def fetch(self):
        url_query = f"{self.url}?language={self.language}&from={self.min_iso_str_date}&to={self.max_iso_str_date}&pageSize={self.amount}&sortBy={self.sort_by}&sources={self.sources}&apiKey={self.api_key}"
        r = requests.get(url_query)
        return r.json()
