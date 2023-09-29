import re

from newspaper import Article


# TODO - move to separate module? (article)

class FetchArticle:

    def fetch(self, url):
        a = Article(url, keep_article_html=True)
        a.download()
        a.parse()
        return self._enrich_html(a)

    def _enrich_html(self, a):
        title = a.title
        top_img = a.top_image
        html = a.article_html
        h1_tag = f"<h1>{title}</h1>"
        img_tag = f'<img src="{top_img}">\n'
        injected = f"\n{h1_tag}\n{img_tag}\n "
        s = re.sub("^<div>", f'<div id="abody">\n{injected}\n', html)
        s = re.sub("<img ", '<img class="resize" ', s)

        return re.sub('<p id="[-_0-9a-zA-Z]+">', '<p id="apara">', s)
