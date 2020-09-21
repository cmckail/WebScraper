from asyncio import tasks
import unittest as test
from webscraper.models.bestbuy import BestBuy
import aiohttp as http
import asyncio
import requests
from bs4 import BeautifulSoup
import time

url = "https://bestbuy.ca/en-ca/product/oculus-rift-s-vr-headset-with-touch-controllers/13542985"


async def test1():
    tasks = []
    models = []

    t1 = time.perf_counter()
    for _ in range(30):
        tasks.append(asyncio.create_task(BestBuy.create(url)))

    for i in tasks:
        models.append(await i)

    t2 = time.perf_counter()
    print(f"Test 1: {t2-t1}s")

    return len(models)


async def test2():
    models = []

    t1 = time.perf_counter()
    for _ in range(30):
        models.append(await BestBuy.create(url))

    t2 = time.perf_counter()
    print(f"Test 2: {t2-t1}s")

    return len(models)


async def main():
    await test1()
    await test2()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())