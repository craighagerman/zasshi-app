import json
import sqlite3
from sqlite3 import IntegrityError
import os
import feedparser
from datetime import datetime
from feed.profile_feed import parse_feed_metadata
import time

class ChannelLoader:
    '''
    To Do - might be good to abstract the class below using strategy design pattern
    in case there are different file formats to load other than "my" json lines format
    '''


    # def _process_category_feed_data(self, data):
    #     for k in data.keys():
    #         for line in data[k]:
    #             name = line["title"]
    #             yield k, name, self._deserialize_feed_line(line)


    def _add_to_channel_table(self, cursor, row, name, category):
        # cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
        values = (name,
                  row["title"],
                  json.dumps(row["categories"]),
                  json.dumps(row["tags"]),
                  row["subtitle"],
                  row["xml_url"],
                  row["html_url"],
                  row["language"],
                  row["num_articles"],
                  row["profile_date"],
                  row["published"],
                  row["status"],
                  row["update_period"],
                  row["update_frequency"],
                  row["fetch_ms"],
                  row["description"],
                  row["image"]
                  )
        print(f"processing: {name}")
        # cols = "(channel_name, title, subtitle, xml_url, html_url, language, num_articles, access_date, status, update_period, update_frequency, category, description)"
        # query = f"INSERT INTO channels {cols} VALUES {values}"
        # cursor.execute(query)
        self._update_channels_table(cursor, values)



    def _add_to_channel_table_2(self, cursor, d):
        # cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
        values = (d["channel_name"],
                  d["status"],
                  d["title"],
                  d["subtitle"],
                  d["xml_url"],
                  d["html_url"],
                  d["language"],
                  d["num_articles"],
                  d["profile_date"],
                  d["published"],
                  d["update_period"],
                  d["update_frequency"],
                  d["fetch_ms"],
                  json.dumps(d["categories"]),
                  json.dumps(d["tags"]),
                  d["description"],
                  d["image"]
                  )
        name = d["channel_name"] if d["channel_name"] else d["title"]
        print(f"processing: {name}")
        cols = "(channel_name, status, title, subtitle, xml_url, html_url, language, num_articles, profile_date, published, update_period, update_frequency, fetch_ms, categories, tags, description, image)"
        query = f"INSERT INTO channels {cols} VALUES {values}"
        cursor.execute(query)




    def _update_channels_table(self, cursor, values):
        # FIXME : currently if a string (subtitle, description etc) contains commas this breaks the SQL statement
        # TODO : make sql insert query more robust
        cols = "(channel_name, title, subtitle, xml_url, html_url, language, num_articles, access_date, status, update_period, update_frequency, category, description)"
        query = f"INSERT INTO channels {cols} VALUES {values}"
        # print(f"Columns:\n{cols}\n\n") #deleteme
        # print(f"Values:\n{values}\n\n")
        cursor.execute(query)

    def _fetch_feed_metadata(self, url):
        ts = time.time()
        f = feedparser.parse(url)
        meta = parse_feed_metadata(f, url)
        te = time.time()
        duration = te - ts
        meta["fetch_ms"] = duration
        return meta


    def _connect_to_sqlite(self, db_path):
        return sqlite3.connect(db_path)


    def _read_jsonl_file(self, jl_path):
        return json.loads(open(jl_path).read())



class JL_ChannelLoader(ChannelLoader):
    '''
    Purpose: load and parse json lines files containing feed urls with schema like
        {
        "news":[
            {"link": "http://online.wsj.com/xml/rss/3_7011.xml", "title": "Wallstreet Journal"},
            ...
    i.e.
    - top level keys = category
    - under category is a list of json objects containing
    - feed url, title

    Load an parse above data, connect to SQLiteDB, for each feed url use feedparser to
    (1) fetch feed and (2) profile (i.e. extract feed metadata) and return a feed
    metadata object. Then use that metadata object to populate a row in the SQLite3 DB
    CHANNELS table. Finally commit and close the db connection.
    '''

    def execute(self, jl_path, db_path):
        con = self._connect_to_sqlite(db_path)
        cursor = con.cursor()
        data = self._read_jsonl_file(jl_path)
        for category, name, row in self.process_category_feed_data(data):
            self._add_to_channel_table(cursor, row, name, category)
        con.commit()
        con.close()

    def process_category_feed_data(self, data):
        for k in data.keys():
            for line in data[k]:
                name = line["title"]
                url = line["link"]
                yield k, name, self._fetch_feed_metadata(url)



class List_ChannelLoader(ChannelLoader):
    '''
    Purpose: same as above.
    `data` is just a list of RSS feed urls
    '''

    def execute(self, jl_path, db_path):
        con = self._connect_to_sqlite(db_path)
        cursor = con.cursor()
        data = self._read_jsonl_file(jl_path)
        data = data["other"]
        for row in self.process_feed_list(data):
            self._add_to_channel_table(cursor, row, row["title"], "")
        con.commit()
        con.close()

    def process_feed_list(self, data):
        for url in data:
            yield self._fetch_feed_metadata(url)





class Obj_ChannelLoader(ChannelLoader):
    '''
    Purpose: same as above.
    Input Files contain list of Json objects with a format same/similar to
    the schema used by the Channels table.
    '''

    def execute(self, jl_path, db_path):
        con = self._connect_to_sqlite(db_path)
        cursor = con.cursor()

        data = self._read_jsonl_file(jl_path)

        for category, d in self.process(data):
            self._add_to_channel_table(cursor, d, "", category)
            # _add_to_channel_table(self, cursor, row, name, category):
        con.commit()
        con.close()

    def process(self, data):
        for d in data:
            d1 = self._fetch_feed_metadata(d["xmlUrl"])
            d["html_url"] = d["htmlUrl"]
            d["xml_url"] = d["xmlUrl"]
            d["update_period"] = d["updateperiod"]
            d["update_frequency"] = d["updatefrequency"]
            d["access_date"] = d["published"]
            for k in ["status", "htmlUrl", "xmlUrl", "updateperiod", "updatefrequency"]:
                d.pop(k)
            yield  d["category"], d | d1



class SmObj_ChannelLoader(ChannelLoader):
    '''
    Purpose: Similar to above.
    Input Files contain list of SMALL Json objects

    '''

    def execute(self, jl_path, db_path):
        con = self._connect_to_sqlite(db_path)
        cursor = con.cursor()

        data = self._read_jsonl_file(jl_path)
        data = data["feeds"]
        for datum in data:
            category = datum["category"]
            print(f"CATEGORY:\t{category}")
            items = datum["items"]
            for item in items:
                name = item["title"]
                print(f"\tNAME:\t{name}")
                d = self._fetch_feed_metadata(item["xmlUrl"])
                self._add_to_channel_table(cursor, d, name, category)
        con.commit()
        con.close()





class Dump_ChannelLoader(ChannelLoader):
    '''
    Purpose: Load json lines files previously dumped by Channels table.
    Input Files contain list of SMALL Json objects

    NOTE: - The dump file contains data in the previously-used schema
    ... but I intend to delete the table and recreate with some different settings, Therefore
    some transformation may be needed

    '''

    def execute(self, jl_path, db_path):
        con = self._connect_to_sqlite(db_path)
        cursor = con.cursor()

        data = self._read_jsonl_file(jl_path)
        data = data["items"]

        for d in data:
            meta = self._fetch_feed_metadata(d["xml_url"])
            d["fetch_ms"] = meta["fetch_ms"]
            d["num_articles"] = meta["num_articles"]
            d["status"] = meta["status"]
            d["image"] = meta["image"]
            d["published"] = meta["published"]
            d["profile_date"] = int(datetime.now().timestamp())
            d["categories"] = {"categories": [d["category"]] }
            d["tags"] = ""
            try:
                self._add_to_channel_table_2(cursor, d)
            except IntegrityError:
                print(f"Record exists for url: {d['xml_url']}. Skipping")
        con.commit()
        con.close()



# ======================================================================================================================


if __name__ == '__main__':
    PROJECT_DIR = "/Users/chagerman/MyProjects/Zasshi-2023"
    DATA_DIR = os.path.join(PROJECT_DIR, "Code/Data/CHANNEL_URLS")
    DB_DIR = os.path.join(PROJECT_DIR, "Code/DB")
    db_path = os.path.join(DB_DIR, "zasshi.db")
    jl_path = os.path.join(DATA_DIR, "done_processed", "feed_list.json")

    def run_JL_ChannelLoader():
        jcl = JL_ChannelLoader()
        jcl.execute(jl_path, db_path)
        # ------------------------------
        lcl = List_ChannelLoader()
        jlist_path = os.path.join(DATA_DIR, "done_processed", "feeds_2.json")
        lcl.execute(jlist_path, db_path)

    # ------------------------------
    def run_Obj_ChannelLoader():
        lcl = Obj_ChannelLoader()
        obj_dir = os.path.join(DATA_DIR, "master_list")
        paths = [os.path.join(obj_dir, p) for p in os.listdir(obj_dir) if p.endswith(".json") and not p.startswith("dead") and not p.startswith("business")]
        for path in paths:
            print(f"processing {path}")
            lcl.execute(path, db_path)
    # ------------------------------

    def run_SmObj_ChannelLoader():
        socl = SmObj_ChannelLoader()

        "/Users/chagerman/MyProjects/Zasshi-2023/Code/Data/CHANNEL_URLS/opml_processed"
        # jf_dir = os.path.join(DATA_DIR, "json_files", "plenary-countries")
        jf_dir = os.path.join(DATA_DIR, "opml_processed")
        paths = [os.path.join(jf_dir, p) for p in os.listdir(jf_dir) if p.endswith(".json")]
        paths.sort()
        for path in paths:
            print("\n" + "-"*80)
            print(f"processing PATH {path}")
            socl.execute(path, db_path)


    # ------------------------------
    def run_Dump_ChannelLoader():
        dcl = Dump_ChannelLoader()
        dump_file = "/Users/chagerman/MyProjects/Zasshi-2023/Code/DB/dump/zasshi_dump.jsonl"
        dcl.execute(dump_file, db_path)



    run_Dump_ChannelLoader()



