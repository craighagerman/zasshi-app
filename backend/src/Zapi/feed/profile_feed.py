
import json
import asyncio
import time
import os
import aiohttp
import async_timeout
import feedparser


def parse_feed_metadata(feed, url):
    f = feed
    try:
        status = f.get("status", "")
        xmlUrl = f.get("href", url)
        htmlUrl = f.feed.get("link", "")
        title = f.feed.get("title", "")
        subtitle = f.feed.get("subtitle", "")
        language = f.feed.get("language", "")
        feed_image = f.feed.get("image", {}).get("href", "")
        published = f.feed.get("published", "")
        updated = f.feed.get("updated", "")
        updateperiod = f.feed.get("sy_updateperiod", "")
        updatefrequency = f.feed.get("sy_updatefrequency", "")
        return {
            "status": status,
            "html_url": htmlUrl,
            "title": title,
            "subtitle": subtitle,
            "language": language,
            "image": feed_image,
            "xml_url": xmlUrl,
            "updated": updated,
            "published": published,
            "update_period": updateperiod,
            "update_frequency": updatefrequency,
            "num_articles": len(f.entries),
            "category": "",
            "tags": []
        }
    except AttributeError as e:
        # return {"status": 400, "href": f.get("href", "")}
        return {"status": 400, "xmlUrl": url}


async def _fetch_feed(session, url):
    print(f"url: {url}")
    ts = time.time()
    html = await _fetch_html(session, url)
    try:
        feed = feedparser.parse(html)
        data = parse_feed_metadata(feed, url)
        te = time.time()
        duration = te - ts
        duration = float(f"{duration:.2f}")
        data["fetch_ms"] = duration
        return data
    except AttributeError as e:
        return {"status": 400, "xmlUrl": url}


async def _fetch_html(session, url):
    try:
        async with async_timeout.timeout(2.5):
            try:
                async with session.get(url) as response:
                    html = await response.text()
                    return html
            except aiohttp.ClientConnectorError as e:
                print(f"Connection Error {str(e)} for url: {url}")
    except asyncio.TimeoutError:
        return {"results": f"timeout error", "xmlUrl": url}

async def _fetch_all_feeds(urls, func):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[_fetch_feed(session, url) for url in urls])
        return results


# ----------------------------------------------------------------------------------------
# main function
# ----------------------------------------------------------------------------------------
def fetch_metedata(urls):
    meta = asyncio.run(_fetch_all_feeds(urls, parse_feed_metadata))
    def isdead(x):
        if (x['status'] == 400) or (x["num_articles"] == 0):
            return True
        return False
    dead = [x for x in meta if isdead(x)]
    meta = [x for x in meta if not isdead(x)]
    return meta, dead

# meta, dead = fetch_metedata(urls)






# ----------------------------------------------------------------------------------------
# Examples only
# ----------------------------------------------------------------------------------------
async def aiohttp_example_w_timeout(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with async_timeout.timeout(2.5):
                try:
                    async with session.get(url) as resp:
                        print(resp.status)
                        print(await resp.text())
                except aiohttp.ClientConnectorError as e:
                    print('Connection Error', str(e))
                except asyncio.TimeoutError as e:
                    print('Connection Error', str(e))
    except asyncio.TimeoutError:
        return {"results": f"timeout error on {url}"}


async def aiohttp_example(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                print(resp.status)
                print(await resp.text())
        except aiohttp.ClientConnectorError as e:
            print('Connection Error', str(e))



# url = "http://digitalbuzzard.com/feed/"
# url = 'http://httpbin.org/get'
# asyncio.run(aiohttp_example(url))
# asyncio.run(aiohttp_example_w_timeout(url))
