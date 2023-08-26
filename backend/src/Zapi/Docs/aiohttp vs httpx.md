# aiohttp vs httpx

Both are python HTTP client libraries (similar to requests, but asyncio native)

- both are similar to requests
- aiohttp uses AsyncIO for async
- httpx uses AsynIO, Trio or Ask for asysc (?)


aiohttp is built in in python3, httpx is not
- that alone is a good reason to choose aiohttp initially

aiohttp is faster and a better choice for async only applications (my case)




