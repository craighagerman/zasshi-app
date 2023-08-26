from feed.clean import strip_tags




def parse_feed_article(feed):
    # feed = feedparser.parse(html)
    entries = feed.entries
    source = feed.feed.title
    status = feed.get("status", 200)
    if status == 200:
        norm_entries = [_extract(i, e, source) for i, e in enumerate(entries)]
    else:
        print(f"status: {status} for feed {source}")
        return None
    return {
        "source": source,
        "items": norm_entries
    }


def _extract(i, e, source):
    id = i
    source = get_source(e, source)
    title = e.title
    author = e.get("author", "")
    pub_date = e.published
    url = e.link
    image = _get_image(e)
    summary = get_summary(e)
    content = _get_content(e)
    return {
        "id": id,
        "source": source,
        "title": title,
        "author": author,
        "published": pub_date,
        "link": url,
        "image": image,
        "description": summary,
        "content": content
    }


def get_source(e, source):
    return e.get("source", {}).get("title", source)

def _get_image(e):
    data = e.get("media_thumbnail", e.get("media_content", [{}]))
    # e.media_thumbnail[0]["url"]
    return data[0].get("url", "")

def get_summary(e):
    summary = e.get("summary", e.get("content", ""))
    return strip_tags(summary)

def _get_content(e):
    return e.get("content", [{}])[0].get("value", "")
