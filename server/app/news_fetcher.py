import requests


class News_Fetcher:
    url = "http://newsapi.org/v2/everything"
    language = "en"
    page_size = 5
    sort_by = "publishedAt"
    sources = "bbc-news"
    amount = 5

    def __init__(self, token) -> None:
        self.api_token = token

    def set_token(self, api_key):
        self.api_key = api_key
        return self

    def set_source(self, source):
        self.news_source = source
        return self

    def set_amount(self, amount):
        self.amount = amount
        return self

    def fetch(self):
        url_query = f"{self.url}?language={self.language}&pageSize={self.amount}&sortBy={self.sort_by}&sources={self.sources}&apiKey={self.api_key}"
        r = requests.get(url_query)
        return r.json()
