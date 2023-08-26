
# Priority To Dos
------------------------------------------------------------------

## Refactpr code
- put parser code in one place
- class-ify python code 



# Features & To Dos
------------------------------------------------------------------

## RSS Feed Metadata
- detect 301 status and update with correct url
-


## RSS Entries
- functionality to detect/get an image to go with an entry
- dedup entries (i.e. some feeds have multiple stories that are the same, just updated) 

## OMPL
- write an ompl parser to convert ompl files to 'my' JSON format

## Browser extension (if possible)
- export history or parse history and then crawl through every TLD in history to extract feeds


## Backend polling functionality
- define a list of feeds to be retrieved every T interval (feed-specific)
- need process during feed profiling to infer refresh interval (based on articles), 
  - and also an automated process to probe the feed to identify the refresh interval (based on updates) 
- automated process to poll feed, retrieve articles and (temporarily?) persist locally  
- on API request respond with persisted data 


## Article Card Enhancements
- contextual "how long ago" timestamp 
- add image if available
- pills displaying category/keywords from article
- thumbs up / down 


## Keyboard navigation
- like NewsBlur - allow for scrolling around with arrow keys etc


## Categories and Tags
- need to define a heirarchy of article categories (news, sport, entertainment, etc)
  - could be two+ levels deep. e.g. News -> news/business, news/polities...  
- also need to have tags that can be associated with a feed/article
  - tags can significy many different dimensions that could be relevant for like/dislike
  - e.g. behind_firewall, clickbait, video, right-wing-bias 
- keywords 
  - look at GDelet keywords as examples - want something similar to help identify stories about the same subject 
- maybe instead of hashtags a Json structure to allow for associating a number with a tag
  - useful for 'truthiness', 'bias', 'popularity', etc
- use kaggle news categorization competition to build/customize a model that can be applied to articles
- experiment with labeling RSS feed vs complete article text (i.e. can I categorize from RSS alone) 


## Popularity
- would be useful for deciding how to order feeds to have a measure of popularity
- can use Alexis etc ranking 
- other idea - maybe somethind like frequency of posts in reddit news (for news) etc.

## HITL app
- would be very useful to have a simple web app to help to label RSS feeds
- e.g. display a list of feeds with metadata as a table
- can use mouse to move around table
- can choose category or tags etc from dropdown or type-ahead
- maybe display a mini view showing the htmlUrl contents when a row is selected






