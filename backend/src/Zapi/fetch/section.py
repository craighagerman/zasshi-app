import json
# from feed.clean import strip_tags
# from feed.parser import parse_summary
# import feedparser
from dev.data_path import DevData
import os


# ----------------------------------------
# Public
# ----------------------------------------
def get_section_metadata(section_id):
    return _load_section_data(section_id)


# ----------------------------------------
# Private
# ----------------------------------------

# TODO : section data should be loaded rom SQL DB. This is a temp dev solution
def _load_section_data(section_id):
    gaming = {"display_name": "Gaming", "channels": get_gaming()["channels"] }
    business = {"display_name": "Business", "channels": get_business()["channels"] }
    news = {"display_name": "News", "channels": get_news()["channels"] }
    politics = {"display_name": "News", "channels": get_politics()["channels"] }
    sports = {"display_name": "News", "channels": get_sports()["channels"] }
    tech = {"display_name": "News", "channels": get_tech()["channels"] }

    match section_id.lower():
      case "gaming":
        return gaming
      case "business":
        return business
      case "news":
        return news
      case "politics":
        return politics
      case "sports":
        return sports
      case "tech":
        return tech


def get_gaming():
    return {
        "channels": [
            {
                "channel_name": "Gamespot",
                "xml_url": "https://www.gamespot.com/feeds/mashup/",
            },
            {
                "channel_name": "Nintendo Life",
                "xml_url": "https://www.nintendolife.com/feeds/latest",
            },
            {"channel_name": "JoyStiq", "xml_url": "https://www.engadget.com/gaming/"},
            {
                "channel_name": "Indiegames.com",
                "xml_url": "https://indiegamesplus.com/feed",
            },
            {
                "channel_name": "Arstechnica - Gaming",
                "xml_url": "http://feeds.arstechnica.com/arstechnica/gaming/",
            },
            {
                "channel_name": "Polygon",
                "xml_url": "https://www.polygon.com/rss/index.xml",
            },
            {
                "channel_name": "Touch Arcade",
                "xml_url": "https://toucharcade.com/feed/",
            },
            {
                "channel_name": "Game Informer",
                "xml_url": "https://www.gameinformer.com/",
            },
            {
                "channel_name": "Xbox.com - News",
                "xml_url": "http://news.xbox.com/en-us/feed/",
            },
            {
                "channel_name": "/r/gamers - Reddit",
                "xml_url": "https://www.reddit.com/r/gamers/.rss",
            },
            {"channel_name": "vg247", "xml_url": "https://www.vg247.com/feed"},
            {
                "channel_name": "My Nintendo News",
                "xml_url": "https://mynintendonews.com/feed/",
            },
            {
                "channel_name": "Rock Paper Shotgun",
                "xml_url": "https://www.rockpapershotgun.com/feed",
            },
            {
                "channel_name": "pcgamesn.com",
                "xml_url": "https://www.pcgamesn.com/mainrss.xml",
            },
            {
                "channel_name": "Operation Sports",
                "xml_url": "https://www.operationsports.com/rss.xml",
            },
            {"channel_name": "Kotaku", "xml_url": "https://kotaku.com/rss"},
            {
                "channel_name": "Videogamer.com",
                "xml_url": "http://feeds.videogamer.com/rss/allupdates.xml",
            },
            {
                "channel_name": "Pushsquare",
                "xml_url": "https://www.pushsquare.com/feeds/latest",
            },
        ]
    }


def get_business():
    return {
        "channels": [
            {
                "channel_name": "Atlantic Business Channel",
                "xml_url": "http://feeds.feedburner.com/AtlanticBusinessChannel",
            },
            {
                "channel_name": "Entrepeneur.com",
                "xml_url": "http://feeds.feedburner.com/entrepreneur/latest",
            },
            {
                "channel_name": "Harvard Business",
                "xml_url": "http://feeds.harvardbusiness.org/harvardbusiness/",
            },
            {
                "channel_name": "Freakonomics",
                "xml_url": "https://freakonomics.com/feed/",
            },
            {
                "channel_name": "The Big Picture",
                "xml_url": "http://feeds.feedburner.com/TheBigPicture",
            },
            {
                "channel_name": "Venture Beat",
                "xml_url": "http://feeds.feedburner.com/venturebeat/SZYF",
            },
            {
                "channel_name": "Fortune",
                "xml_url": "https://fortune.com/feed/fortune-feeds/?id=3230629",
            },
            {
                "channel_name": "Economist",
                "xml_url": "https://www.economist.com/the-world-this-week/rss.xml",
            },
            {
                "channel_name": "The Non-Profit Times",
                "xml_url": "http://thenonprofittimes.com/feed/",
            },
            {"channel_name": "SBN Online", "xml_url": "https://sbnonline.com/feed/"},
            {
                "channel_name": "McKinsey",
                "xml_url": "https://www.mckinsey.com/insights/rss",
            },
            {
                "channel_name": "Home Business Mag",
                "xml_url": "https://homebusinessmag.com/feed/",
            },
            {
                "channel_name": "Business Insider",
                "xml_url": "http://feeds2.feedburner.com/businessinsider",
            },
            {
                "channel_name": "Calculated Risk",
                "xml_url": "http://feeds.feedburner.com/CalculatedRisk",
            },
            {
                "channel_name": "Huffington Post - Business",
                "xml_url": "https://www.huffpost.com/section/business/feed",
            },
        ]
    }


def get_news():
    return {
        "channels": [
            {
                "channel_name": "Fox News Science",
                "xml_url": "https://moxie.foxnews.com/google-publisher/tech.xml",
            },
            {
                "channel_name": "CNN - Top Stories",
                "xml_url": "http://rss.cnn.com/rss/cnn_topstories.rss",
            },
            {
                "channel_name": "Time Magazine - Top Stories",
                "xml_url": "http://feeds.feedburner.com/time/topstories",
            },
            {
                "channel_name": "NYTimes - Homepage",
                "xml_url": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
            },
            {
                "channel_name": "Yahoo News - Latest news and headlines",
                "xml_url": "https://www.yahoo.com/news/rss/topstories",
            },
            {
                "channel_name": "Washington Post",
                "xml_url": "https://feeds.washingtonpost.com/rss/world",
            },
            {
                "channel_name": "Vox - All",
                "xml_url": "https://www.vox.com/rss/index.xml",
            },
            {
                "channel_name": "BBC News - World",
                "xml_url": "http://feeds.bbci.co.uk/news/world/rss.xml",
            },
            {
                "channel_name": "Huffington Post",
                "xml_url": "https://www.huffpost.com/section/front-page/feed",
            },
            {
                "channel_name": "CNN - World news",
                "xml_url": "http://rss.cnn.com/rss/cnn_world.rss",
            },
            {
                "channel_name": "ABC News -  Top stories",
                "xml_url": "https://abcnews.go.com/abcnews/topstories",
            },
            {
                "channel_name": "Reuters News First",
                "xml_url": "https://www.reutersagency.com/feed/?best-types=reuters-news-first&post_type=best",
            },
            {
                "channel_name": "Drudge Report",
                "xml_url": "https://www.drudgereportfeed.com/rss.xml",
            },
            {
                "channel_name": "Market Watch - Top stories",
                "xml_url": "http://feeds.marketwatch.com/marketwatch/topstories/",
            },
            {"channel_name": "Salon.com", "xml_url": "https://www.salon.com/feed/"},
            {
                "channel_name": "New Yorker - Everything",
                "xml_url": "https://www.newyorker.com/feed/everything",
            },
            {
                "channel_name": "Daily Mail - Latest stories",
                "xml_url": "https://www.dailymail.co.uk/articles.rss",
            },
            {"channel_name": "New York Post", "xml_url": "https://nypost.com/feed/"},
        ]
    }


def get_politics():
    return {
        "channels": [
            {
                "channel_name": "Slate.com - Politics",
                "xml_url": "https://slate.com/feeds/all.rss",
            },
            {
                "channel_name": "World Affair Journal",
                "xml_url": "https://www.worldaffairsjournal.org/",
            },
            {
                "channel_name": "Fox News - Politics",
                "xml_url": "https://moxie.foxnews.com/google-publisher/politics.xml",
            },
            {
                "channel_name": "CNN Politics",
                "xml_url": "http://rss.cnn.com/rss/cnn_allpolitics.rss",
            },
            {
                "channel_name": "Reuters - Politcs",
                "xml_url": "http://feeds.reuters.com/Reuters/PoliticsNews",
            },
            {
                "channel_name": "USA Today - Politics",
                "xml_url": "http://rssfeeds.usatoday.com/TP-OnPolitics",
            },
            {
                "channel_name": "Washington Examiner",
                "xml_url": "https://www.washingtonexaminer.com/tag/politics.rss",
            },
            {
                "channel_name": "The Nation",
                "xml_url": "https://www.thenation.com/feed/?post_type=article",
            },
            {
                "channel_name": "Daily Signal",
                "xml_url": "https://www.dailysignal.com//feed/",
            },
            {
                "channel_name": "MSNBC",
                "xml_url": "https://feeds.nbcnews.com/msnbc/public/news",
            },
            {
                "channel_name": "Politico",
                "xml_url": "https://rss.politico.com/politics.xml",
            },
            {
                "channel_name": "Realwire",
                "xml_url": "https://www.realwire.com/rss/feeds.asp?cat=Politics",
            },
        ]
    }


def get_sports():
    return {
        "channels": [
            {
                "channel_name": "BBC Sports",
                "xml_url": "https://feeds.bbci.co.uk/sport/rss.xml?edition=int",
            },
            {"channel_name": "ESPN", "xml_url": "https://www.espn.com/espn/rss/news"},
            {
                "channel_name": "NBA.com",
                "xml_url": "https://www.nba.com/rss/nba_rss.xml",
            },
            {"channel_name": "NFL.com", "xml_url": "https://www.nfl.com/"},
            {
                "channel_name": "Yahoo Sports",
                "xml_url": "https://www.yahoo.com/news/rss/sports",
            },
            {
                "channel_name": "BBC Sports - World edition",
                "xml_url": "https://feeds.bbci.co.uk/sport/rss.xml",
            },
            {
                "channel_name": "We the sports guys",
                "xml_url": "https://westhesportsguy.com/feed/",
            },
            {
                "channel_name": "Fox Sports",
                "xml_url": "https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30",
            },
            {"channel_name": "Talk Sports", "xml_url": "https://talksport.com/feed/"},
            {
                "channel_name": "CBS Sports",
                "xml_url": "https://www.cbssports.com/rss/headlines/",
            },
            {
                "channel_name": "Fifa.com",
                "xml_url": "https://www.fifa.com/rss/index.xml",
            },
            {
                "channel_name": "NU Sports",
                "xml_url": "https://nusports.com/rss_feeds.aspx",
            },
            {"channel_name": "Sport1.de", "xml_url": "https://www.sport1.de/news.rss"},
            {
                "channel_name": "TriathlonMag",
                "xml_url": "https://www.triathlonmag.com.au/feed/",
            },
            {
                "channel_name": "ISSF-sports.org",
                "xml_url": "https://www.issf-sports.org/rss/news.html",
            },
        ]
    }


def get_tech():
    return {
        "channels": [
            {
                "channel_name": "Techcrunch",
                "xml_url": "http://feeds.feedburner.com/Techcrunch",
            },
            {"channel_name": "Wired", "xml_url": "https://www.wired.com/feed"},
            {
                "channel_name": "NYTimes - Technology",
                "xml_url": "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
            },
            {"channel_name": "MacWorld", "xml_url": "https://www.macworld.com/feed"},
            {
                "channel_name": "PCWorld",
                "xml_url": "https://feeds.pcworld.com/pcworld/latestnews",
            },
            {"channel_name": "Techworld", "xml_url": "https://www.computerworld.com/"},
            {"channel_name": "LifeHacker", "xml_url": "https://lifehacker.com/rss"},
            {
                "channel_name": "ReadWriteWeb",
                "xml_url": "http://feeds.feedburner.com/readwriteweb",
            },
            {
                "channel_name": "Engadget.com",
                "xml_url": "https://www.engadget.com/rss-full.xml",
            },
            {"channel_name": "ReadWrite", "xml_url": "https://readwrite.com/feed/"},
            {
                "channel_name": "Mashable",
                "xml_url": "http://feeds.mashable.com/Mashable",
            },
            {
                "channel_name": "O'Reilly Radar",
                "xml_url": "http://feeds.feedburner.com/oreilly/radar/atom",
            },
            {"channel_name": "Gizmodo", "xml_url": "https://gizmodo.com/rss"},
            {
                "channel_name": "Technology Review",
                "xml_url": "https://www.technologyreview.com/feed/",
            },
            {
                "channel_name": "VentureBeat",
                "xml_url": "https://venturebeat.com/business/venturebeat-rss/",
            },
            {
                "channel_name": "Recode.net",
                "xml_url": "https://www.recode.net/rss/index.xml",
            },
            {
                "channel_name": "Computer World",
                "xml_url": "https://www.computerworld.com/index.rss",
            },
            {
                "channel_name": "MakeUsOf",
                "xml_url": "http://feeds.feedburner.com/Makeuseof",
            },
            {"channel_name": "CNet.com", "xml_url": "https://www.cnet.com/rss/news/"},
            {"channel_name": "HowToGeek", "xml_url": "https://www.howtogeek.com/"},
            {
                "channel_name": "HowToGeek",
                "xml_url": "http://feeds.howtogeek.com/HowToGeek",
            },
        ]
    }
