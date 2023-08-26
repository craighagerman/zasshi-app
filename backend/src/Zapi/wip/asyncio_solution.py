# See:
# https://stackoverflow.com/questions/23847555/asynchronous-feedparser-requests

import aiohttp
import asyncio
import async_timeout
import feedparser

import pprint

INTERVAL = 60


async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def fetchfeeds(loop, feedurls, ircsock):
    last_entry = None

    feeds = []

    for url in feedurls:
        feeds.append({"url": url, "last": ""})

    while True:
        for feed in feeds:
            async with aiohttp.ClientSession(loop=loop) as session:
                html = await fetch(session, feed["url"])
                rss = feedparser.parse(html)
                if feed["last"]:
                    if (
                        feed["last"]["title"] != rss["entries"][0]["title"]
                        and feed["last"]["link"] != rss["entries"][0]["link"]
                    ):
                        print("new entry")
                        feed["last"] = rss["entries"][0]

                        print("MSG {}".format(feed["last"]["title"]))
                        print("MSG {}".format(feed["last"]["link"]))
                else:
                    feed["last"] = rss["entries"][0]

        await asyncio.sleep(INTERVAL)


loop = asyncio.get_event_loop()
loop.run_until_complete(
    fetchfeeds(
        loop, ["https://n-o-d-e.net/rss/rss.xml", "http://localhost:8000/rss.xml"], None
    )
)
