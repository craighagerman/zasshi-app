# see:
#   https://stackoverflow.com/questions/72407052/how-to-use-asyncio-aiohttp-web-scraper-with-fastapi


# ==========================================================================================
# web scraper code
# ==========================================================================================
import asyncio
import aiohttp
from bs4 import BeautifulSoup, SoupStrainer


class TestScraper:
    def __init__(self, query):
        self.query = query

    async def main(self):
        urls = [
            f"https://books.toscrape.com/catalogue/page-{self.query}.html",
            f"https://quotes.toscrape.com/page/{self.query}/",
        ]

        def get_urls(session):
            tasks = []
            for url in urls:
                tasks.append(session.get(url))
            return tasks

        async with aiohttp.ClientSession() as session:
            tasks = get_urls(session)
            responses = await asyncio.gather(*tasks)
            results = []
            for r in responses:
                if (str(r.url).split(".")[0][8:]) == "books":
                    soup = BeautifulSoup(
                        await r.read(), "lxml", parse_only=SoupStrainer("article")
                    )
                    for books in soup.find_all("article"):
                        book_name = books.find("h3").find("a").get("title")
                        book_price = books.find("p", class_="price_color").text
                        books_item = {
                            "book_name": book_name,
                            "book_price": book_price,
                        }
                        results.append(books_item)
                elif (str(r.url).split(".")[0][8:]) == "quotes":
                    soup = BeautifulSoup(
                        await r.read(),
                        "lxml",
                        parse_only=SoupStrainer("div", {"class": "quote"}),
                    )
                    for quotes in soup.find_all("div", class_="quote"):
                        quote_text = quotes.find("span", class_="text").get_text()
                        quote_author = quotes.find("small", class_="author").get_text()
                        quotes_item = {
                            "quote_text": quote_text,
                            "quote_author": quote_author,
                        }
                        results.append(quotes_item)
                else:
                    results.append({"error": f"No results found for {r.url}"})
            yield results
            # print(results)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(TestScraper(6).main())
# asyncio.run(TestScraper({query}).main())


# ==========================================================================================
# fastAPI code
# ==========================================================================================

import asyncio
from fastapi import FastAPI

from scrapers.books_quotes import TestScraper

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/test/{test_query}")
async def read_test_items(test_query: str):
    async for results in TestScraper(test_query).main():
        return results
