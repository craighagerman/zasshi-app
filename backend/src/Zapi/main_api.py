from typing import Union
from backend.src.Zapi.fetch.fetch_rss import get_feed
from backend.src.Zapi.fetch.section import get_section_metadat
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
    ''' 
        Return a list of Categories/Sections
        e.g. 
            { "items": [ 
                "News & Current Affairs", 
                "Sports", 
                "Tech" ] }
    '''
    return LocalData().get_categories()


@app.get("/feed_list")
def feed_list():
    return LocalData().get_feed_list()


@app.get("/article")
def article():
    '''
        Return one (hard-coded) example article
        TODO: Deprecate and delete this route & method
    '''
    return LocalData().get_article()


@app.get("/get_article")
def get_article(url: Union[str, None] = None):
    '''
        Return article for given url
    '''
    if url:
        return FetchArticle().fetch(url)



'''
TODO : Needed routes / endpoints

get_section_channels 
- given input (section/category name) -> return channels (name & url) in that section

fetch_feed
- given input (feed url) -> fetch feed and return


'''

@app.get("/fetch_feed")
def fetch_feed(q: Union[str, None] = None):
    if q:
        # return get_userdefined_feed(q)
        return get_feed(q)
    
    

@app.get("section_channels")
def section_channels(q: Union[str, None] = None):
    if q:
        return get_section_metadat(q)
    

