'''
PURPOSE
- fetch HTML and then parse with feedparser

'''


import asyncio
import time

import aiohttp
import async_timeout
import feedparser
from feed.parse_feed import parse_feed_article
from feed.profile_feed import parse_feed_metadata


# def get_metadata(feed):
#     return parse_feed_metadata(feed)
#
# def get_article(feed):
#     return parse_feed_article(feed)


async def fetch_feed(session, url, func):
    print(f"url: {url}")
    ts = time.time()
    html = await fetch_html(session, url)
    feed = feedparser.parse(html)
    # data = get_metadata(feed)
    data = func(feed, url)
    te = time.time()
    duration = te - ts
    duration = float(f"{duration:.2f}")
    data["fetch_ms"] = duration
    return data


async def fetch_html(session, url):
    async with async_timeout.timeout(1.5):
        async with session.get(url) as response:
            html = await response.text()
            return html

async def fetch_all_feeds(urls, func):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch_feed(session, url, func) for url in urls])
        return results

# ----------------------------------------------------------------------------------------

def fetch_metedata(urls):
    return asyncio.run(fetch_all_feeds(urls, parse_feed_metadata))

def fetch_articles(urls):
    return asyncio.run(fetch_all_feeds(urls, parse_feed_article))

def run():
    urls = [
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://www.yahoo.com/news/rss/topstories"
    ]
    metas = fetch_metedata(urls)
    articles = fetch_articles(urls)


if __name__ == "__main__":
    urls = [
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://www.yahoo.com/news/rss/topstories"
    ]
    loop = asyncio.get_event_loop()
    # htmls = loop.run_until_complete(fetch_all_html(urls, loop))
    feeds = loop.run_until_complete(fetch_all_feeds(urls, parse_feed_metadata))
