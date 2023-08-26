# Notes

## Current solution
- fastAPI to fetch RSS feeds
- feedparser to parse returned xml

## Eventual Needs
Vue app makes one single API call 


1. need to fetch multiple feeds concurrently
2. need to combine & organize/order results

- #1 above 
  - probably means using async/await
  - maybe use asyncio, aiohttp (investigate - what is difference)
  - need to investigate what pattern is best in 2023


- #2 above
  - can combine by putting in a dict by feed (e.g. CBC articles, Reuter articles....)
  - could combine by pushing all into a queue
  - can order by date initially
  - eventually need a personalization score for articles to promote or suppress

----

## Approach Suggestions


From: 
https://stackoverflow.com/questions/23847555/asynchronous-feedparser-requests

You're probably better off to decouple the fetching from the parsing. Feedparser is an amazing parsing library, but probably not the best HTTP client libary. Luckily that's fairly easy to do as Feedparser can also parse a blob of text.

Then, this means you can pick any HTTP library to actually do the polling, as long as it supports your asyncrhonous requirement. You'll probably end up using something like Twisted and its WebClient.

Another solution is to of course avoid doing all that expensive polling yourself and rely on a solution like Superfeedr which will use webhooks to send you only what's new in a given feed.


## Current Plan

Break apart functionality as suggested above
- fastAPI for an API that Vue can access
- feedparser to parse textblob of RSS xml
- but don't use feedparser to make http calls! instead
  - aiohttp (or some other) http client to asycronously make http calls





