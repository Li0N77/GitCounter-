import asyncio
import time
import aiohttp
from aiohttp.client import ClientSession

counter = 0
async def download_link(url:str,session:ClientSession):
    async with session.get(url) as response:
        result = await response.text()
        global counter
        counter = counter + 1
        print(counter)

async def download_all(urls:list):
    my_conn = aiohttp.TCPConnector(limit=10)
    async with aiohttp.ClientSession(connector=my_conn) as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_link(url=url,session=session))
            tasks.append(task)
        await asyncio.gather(*tasks,return_exceptions=True) # the await must be nest inside of the session

url = input("Please enter your image url : ")
countx = int(input("Please enter count : "))
url_list = [url] * countx
start = time.time()
asyncio.run(download_all(url_list))
end = time.time()
print(f'download {len(url_list)} links in {end - start} seconds')