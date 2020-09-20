import unittest as test
import aiohttp as http
import asyncio
import requests
from bs4 import BeautifulSoup
import time


url = "https://www.bestbuy.ca/en-ca/product/hp-15-6-laptop-silver-intel-core-i3-1005g1-256gb-ssd-8gb-ram-windows-10/13863131"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}


async def fetch(session: http.ClientSession, url) -> BeautifulSoup:
    async with session.get(url, headers=headers) as response:

        assert response.status < 400, f"Website returned {response.status} error."

        return BeautifulSoup(await response.content.read(), "html.parser")


async def test1():
    await asyncio.sleep(3)
    print("First.")


async def test2():
    await asyncio.sleep(2)
    print("Second.")


async def main():
    t = time.perf_counter()
    task = asyncio.create_task(test1())
    task2 = asyncio.create_task(test2())
    await task
    await task2
    print(f"Finished. Total time is {time.perf_counter() - t}.")


if __name__ == "__main__":
    # t = time.perf_counter()
    # data = requests.get(
    #     "https://www.bestbuy.ca/en-ca/product/samsung-58-4k-uhd-hdr-qled-tizen-smart-tv-qn58q60tafxzc-titan-grey-only-at-best-buy/14471420")
    # print(f"Finished. Total time is {time.perf_counter() - t}.")
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

    x = []
    print(type(x))
    print(isinstance(x, list))
