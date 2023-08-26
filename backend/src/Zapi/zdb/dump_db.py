import json
import sqlite3
import os
from collections import defaultdict



# Reading Data from the SQLite Database

def dump_csv(db_path, outpath):
    con = _connect_to_sqlite(db_path)
    cursor = con.cursor()
    raw_rows = cursor.execute("SELECT * FROM channels").fetchall()
    con.close()
    dd = defaultdict(list)
    for r in raw_rows:
        dd[r[4]].append(r)
    unique_rows = [v[0] for k, v in dd.items()]
    jsonlines = {"items" : unique_rows}
    print(f"Writing CSV file to {outpath}")
    with open(outpath, "w") as fo:
        fo.write(json.dumps(jsonlines))



def dump_json(db_path, outpath):
    con = _connect_to_sqlite(db_path)
    cursor = con.cursor()
    raw_rows = cursor.execute("SELECT * FROM channels").fetchall()
    con.close()
    dd = defaultdict(list)
    for r in raw_rows:
        dd[r[4]].append(r)
    col_names = [x[0] for x in cursor.description]
    unique_rows = [v[0] for k, v in dd.items()]
    def jsonify(r, col_names):
        d = dict()
        for i in range(len(col_names)):
            d[col_names[i]] = r[i]
        return d

    items = [jsonify(r, col_names) for r in unique_rows]
    jsonlines = {"items" : items}
    print(f"Writing JSON lines file to {outpath}")
    with open(outpath, "w") as fo:
        fo.write(json.dumps(jsonlines))










def bulk_insert(cur):
    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]
    cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)

def single_insert(cur):
    cur.execute("""
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5)
    """)



def _connect_to_sqlite(db_path):
    return sqlite3.connect(db_path)


if __name__ == '__main__':
    PROJECT_DIR = "/Users/chagerman/MyProjects/Zasshi-2023"
    DATA_DIR = os.path.join(PROJECT_DIR, "Code/Data/CHANNEL_URLS")
    DB_DIR = os.path.join(PROJECT_DIR, "Code/DB")
    db_path = os.path.join(DB_DIR, "zasshi.db")

    csv_outpath = os.path.join(DB_DIR, "dump", "zasshi_dump.csv")
    json_outpath = os.path.join(DB_DIR, "dump", "zasshi_dump.jsonl")

    dump_csv(db_path, csv_outpath)
    dump_json(db_path, json_outpath)