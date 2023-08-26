# MVP Plan

What does MVP look like? Need a vision to have something to aim towards, 
prioritize towards and know when I am "done".

Original vision -> news aggregator app. But now thinking maybe an RSS
app is better for MVP and news aggregator comes after. 

RSS App Vision
- pre-populated with categorized RSS feeds
- user can turn on/off feeds, also rate them (to preference)
- 3 views:
  1. RSS feed - click on feed title -> presented with articles from that feed
  2. category - click on category title -> presented with articles from that category
     - have to score/rank articles from multiple feeds
     - don't want to just do all feed 1... then all feed 2 etc
     - should use feed rating (inferred) to preference some over others 
     - easy -> order by timestamp
     - harder -> order by popularity, personalization etc 
  3. personalized -  a "for you" view that presents articles from ALL feeds
    - same ideas & constraints as above
    - n.b. this ^ is basically the news aggregator app 
- Engine should have a massive list of RSS feeds, but only choose/present a subset for a user
  - engine should play with what is on that sublist over time to create a personalized feed list  
    - NOTE: "personalized" can be about the FEED as well as the ARTICLE content! 
  - engine should be profiling the user over time to learn likes/dislikes across multiple dimensions
    - with more users can create a collection of Personas
    - start with a default persona, collect profile info, move to other persona as signal improves 
  - explore and exploit. Offer up new feeds, content types -> see if user interacts
  - infer other content user might like (you read Fox ... maybe you'd like Drudge) 





News Aggregator App Vision
- basically #3 above
- like Zite - don't even present "feeds" to users. Just give them a content aggregator experience

Caveat
- there is a chicken and egg problem
- if I had a lot of users I could infer what is popular overall
- but difficult to personalize cold start with zero users
- personalized news aggregator problem is basically Cold Start writ large.   

Ideas
- there are lots of ways to take this (RSS or aggregator). 
- Just have to choose ONE vision for MVP. Options include
  - one big main list of articles (the personalized aggregator) 
  - separate tabs for different categories (like Smart News). User can add/disable categories
  - make user organize/categorize RSS feeds (like NewsBlur) 



# V0 - RSS reader app 

## Front End
Vue Web app


## API
fastAPI on backend to return article lists
- endpoint with query to return single feed (like feedly, newsblur etc)
- endpoints to return categories of articles (news, tech, sports) i.e. combine feeds
- endpoint to return "for you" selected articles
Two modes:
1. api call fetches RSS feed(s), and returns articles
2. api call fetches and returns persisted articles

## RSS Feed Parser
Async process to concurrently fetch one/many rss feeds
- fetch raw xml
- parse html into feed, parse that into json object
- for each feed return list of json articles 

## Async http client
Use with above
- input a list of URLS, use asyncio to fetch & gather all concurrently








