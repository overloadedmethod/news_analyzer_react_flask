from settings import CELERY_BROKER, CELERY_RESULTS
from celery import Celery
from flask import Flask

flask = Flask(__name__)


app = Celery(__name__, broker=CELERY_BROKER, backend=CELERY_RESULTS)


@app.task()
def add_together(a, b):
    print("celery is called")
    return a + b


def fetch_for_day(day):
    pass


def fetch_last_news(amount: int):
    return {
        "status": "ok",
        "totalResults": 6477,
        "articles": [
            {
                "source": {"id": "bbc-news", "name": "BBC News"},
                "author": None,
                "title": "Everton 2-2 Liverpool: Dominic Calvert-Lewin heads Toffees level",
                "description": "Everton twice come from behind to draw with Liverpool and maintain their three-point lead at the top of the Premier League.",
                "url": "https://www.bbc.co.uk/sport/football/54489179",
                "urlToImage": "https://ichef.bbci.co.uk/live-experience/cps/624/cpsprodpb/11F7A/production/_114949537_whatsubject.jpg",
                "publishedAt": "2020-10-17T13:33:43Z",
                "content": "Dominic Calvert-Lewin has become just the fourth player in Premier League history to score in each of the opening five matchdays of a season\r\nEverton twice came from behind to draw a dramatic Merseys… [+3614 chars]",
            },
            {
                "source": {"id": "bbc-news", "name": "BBC News"},
                "author": None,
                "title": "Celtic 0-2 Rangers: visitors make title statement with dominant win",
                "description": "Rangers inflicted the first Old Firm derby blow in a historic Scottish Premiership campaign - and moved four points clear at the top - with a dominant 2-0 win at Celtic Park.",
                "url": "https://www.bbc.co.uk/sport/football/54489133",
                "urlToImage": "https://ichef.bbci.co.uk/live-experience/cps/624/cpsprodpb/5842/production/_114949522_19987624.jpg",
                "publishedAt": "2020-10-17T13:22:17Z",
                "content": "Connor Goldson side-footed home his second to secure victory for Rangers\r\nRangers inflicted the first Old Firm derby blow in a historic Scottish Premiership campaign - and moved four points clear at … [+6748 chars]",
            },
            {
                "source": {"id": "bbc-news", "name": "BBC News"},
                "author": "https://www.facebook.com/bbcnews",
                "title": "Covid in Scotland: Deaths from virus increase by 15",
                "description": "The Scottish government confirmed 1,167 more people had tested positive within the same 24-hour period.",
                "url": "https://www.bbc.co.uk/news/uk-scotland-54583356",
                "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/E28A/production/_114949975_hi063850629.jpg",
                "publishedAt": "2020-10-17T13:13:12Z",
                "content": "The Scottish government confirmed 1,167 more people had tested positive within the same 24-hour period.",
            },
            {
                "source": {"id": "bbc-news", "name": "BBC News"},
                "author": None,
                "title": "Doyle lands first Group One victory with Glen Shiel",
                "description": "Hollie Doyle wins her first Group One race as Glen Shiel takes the British Champions Sprint Stakes at Ascot.",
                "url": "https://www.bbc.co.uk/sport/horse-racing/54584413",
                "urlToImage": "https://ichef.bbci.co.uk/live-experience/cps/624/cpsprodpb/13590/production/_97584297_breaking_news.png",
                "publishedAt": "2020-10-17T13:07:14Z",
                "content": "Jockey Hollie Doyle won her first Group One race as Glen Shiel claimed the British Champions Sprint Stakes at Ascot in a photo finish.\r\nThe victory on the 16-1 shot on Champions Day saw the 24-year-o… [+353 chars]",
            },
            {
                "source": {"id": "bbc-news", "name": "BBC News"},
                "author": None,
                "title": "2020/10/17 13:00 GMT",
                "description": "The latest five minute news bulletin from BBC World Service.",
                "url": "https://www.bbc.co.uk/programmes/w172x5p1kfj1v8s",
                "urlToImage": "https://ichef.bbci.co.uk/images/ic/1200x675/p060dh18.jpg",
                "publishedAt": "2020-10-17T13:06:00Z",
                "content": "The latest five minute news bulletin from BBC World Service.",
            },
        ],
    }
