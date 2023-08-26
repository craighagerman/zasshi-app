from typing import Union
from dev.data_loader import LocalData
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fetch.article import FetchArticle

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # allow_methods=["*"],
    allow_headers=["*"],
)


# ----------------------------------------------------------------------------------------
# Endpoints
# ----------------------------------------------------------------------------------------
@app.get("/categories")
def categories():
    return LocalData().get_categories()


@app.get("/feed_list")
def feed_list():
    return LocalData().get_feed_list()


@app.get("/article")
def article():
    return LocalData().get_article()


@app.get("/get_article")
def get_article(url: Union[str, None] = None):
    if url:
        return FetchArticle().fetch(url)



