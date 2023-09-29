import json
from feed.clean import strip_tags
from feed.parser import parse_summary
import feedparser
import os

# TODO - rename; move to a different module? (article)

# ----------------------------------------
# Public
# ----------------------------------------
def get_articles():
    path = "/Users/chagerman/MyProjects/Zasshi-2023/Code/Data/dev_data/ctv_articles.json"
    return load_ctv_articles(path)


def get_predefined_feed():
    url = "https://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009"
    return get_feed(url)


# def get_userdefined_feed(url):
#     return get_feed(url)


# ----------------------------------------
# Private
# ----------------------------------------
def get_feed(url):
    f = feedparser.parse(url)
    feed_published = f.feed.get("published", "")
    entries = f.entries
    return {
        "items": [
            {
                "id": i,
                "source": f.feed.title,
                "title": e.title,
                "author": e.get("author", ""),
                "published": e.get("published", feed_published), # TODO - infer date if it isn't present
                "link": e.link,
                "description": parse_summary(e)
            }
            for i, e in enumerate(entries)
        ]
    }


def load_file(path):
    with open(path) as fo:
        data = json.load(fo)
    return data


def load_ctv_articles(path):
    return load_file(path)


def load_bbc_articles():
    data_dir = "/Users/chagerman/MyProjects/Zasshi-2023/Code/Data/dev_data"
    path = os.path.join(data_dir, "bbc_articles.json")
    return load_file(path)
