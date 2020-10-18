# News analyzer

## Purpose

The purpose of application is to analyze news given by https://newsapi.org/

## Installation

### Prerequisite

1. MongoDB server
2. NPM and Node 12+

### Client

Go to client and `run npm/yarn install`

### Server

Go to server folder and run:

`pip install -r requirements.txt `

Relevant settings are in settings.py at root.

#### Structure

1. repo.py is repository that allows to separate abstractions between database and code.
2. words_utils.py is utilities that will allow parse and count words
3. news_fetcher is a query builder to communicate with newsapi.org

## UI

![header](/assets/header_tq6xuvlkd.png)

After acquiring token just type it inside "provided token" field and you already may use the program

After for example fetching last 100 you should see something like that:

![last-100](/assets/last-100_fo0yrsr0m.png)

You will get counts for the words that were common in last 100 news.
Notice: words with less than 3 symbols or non alphabetics symbols are filtered.

![news](/assets/news_tdvfdur1d.png)

The Bottom part will show the actual titles and description.

After Clicking on show loaded 7 days you should see news of last 7 days when each day is represented by number of used words

![days](/assets/days_5ydht8uyj.png)

The empty line signalize end of the chunk.
The days are going from recent to oldest from now.
