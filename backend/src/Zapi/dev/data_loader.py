import json
import os

from dev.data_path import DevData


class LocalData:

    def get_categories(self):
        path = os.path.join(DevData().dev_data_dir(), "sample_categories_2.json")
        data = json.load(open(path))
        return data

    def get_feed_list(self):
        path = os.path.join(DevData().dev_data_dir(), "sample_feed_list.json")
        return json.load(open(path))

    def get_article(self):
        # path = os.path.join(DevData().dev_data_dir(), "sample_article.json")
        path = os.path.join(DevData().dev_data_dir(), "sample_article_1.html")
        return open(path).read()

    def load_section_channels(self):
        path = os.path.join(DevData().dev_data_dir(), "news_list.json")
        with open(path) as fo:
            data = json.load(fo)
            return {"feeds": data}

