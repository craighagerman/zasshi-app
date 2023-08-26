from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from feed.profile_feed import parse_feed_metadata
from fetch.async_fetcher import fetch_all_feeds
from fetch.fetch_feeds import load_feed_list
from fetch.fetch_rss import (
    get_articles,
    get_feed,
    # get_userdefined_feed,
    load_bbc_articles,
)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # allow_methods=["*"],
    allow_headers=["*"],
)


# ======================================================================

@app.get("/feed_metadata")
async def feed_metadata():
    urls = [
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://www.yahoo.com/news/rss/topstories"
    ]
    data = await fetch_all_feeds(urls, parse_feed_metadata)
    return data


# ======================================================================

@app.get("/fetch_feed")
def fetch_feed(q: Union[str, None] = None):
    if q:
        # return get_userdefined_feed(q)
        return get_feed(q)


@app.get("/static_articles")
def articles():
    return get_articles()


@app.get("/feed_articles")
def feed_articles():
    return get_feed()


@app.get("/bbc_articles")
def bbc_articles():
    return load_bbc_articles()


# ======================================================================

@app.get("/feed_list")
def feed_list():
    return load_feed_list()
