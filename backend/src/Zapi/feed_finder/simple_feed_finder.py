import urllib.parse
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as bs4

"""
ref:
https://scrapfly.io/blog/how-to-find-all-links-using-beautifulsoup/
https://scrapeops.io/python-web-scraping-playbook/python-beautifulsoup-findall/
https://stackoverflow.com/questions/35616434/how-can-i-get-the-base-of-a-url-in-python
"""


def find_feed_tags(url):
    soup = _fetch_soup(url)
    feeds = soup.findAll(type="application/rss+xml") + soup.findAll(type="application/atom+xml")
    return feeds


def find_feeds(url):
    feeds = find_feed_tags(url)

    def jsonify(t):
        return {"title": t.get("title"),
                "href": t.get("href"),
                "type": t.get("type")
                }

    return [jsonify(t) for t in feeds]


def _fetch_soup(url):
    user_agent = {
        "User-agent":
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17"}
    raw = requests.get(url, headers=user_agent).text
    # html = bs4(raw,"html5lib")
    # html = bs4(raw,"html.parser")
    soup = bs4(raw)
    return soup


# --------------------------------------------------------------------------------

def find_html_links(url):
    soup = _fetch_soup(url)
    links = [node.get('href') for node in soup.find_all("a")]
    base_url = get_base_url(url)
    links = [urljoin(base_url, link) for link in links]


def filter_outbound(base_url, links):
    return [x for x in links if not x.startswith(base_url)]


def get_base_url(url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')
    return parsed.geturl()


def main():
    pass


if __name__ == "__main__":
    main()
