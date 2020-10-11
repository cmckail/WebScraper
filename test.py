from webscraper.models.bestbuy import BestBuy, BestBuyCheckOut
import regex, logging, requests, json, aiohttp, random
from selenium.webdriver import Firefox, FirefoxOptions
import requests, json
from bs4 import BeautifulSoup
import time

# header = None
# with open("user-agents.json", "r") as f:
#     headers = json.load(f)
#     header = headers[random.randint(0, len(headers) - 1)]

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7",
#     "Cache-Control": "no-cache",
#     "User-Agent": header,
#     "Postal-Code": "L8J",
#     "Region-Code": "ON",
#     "dnt": "1",
#     "pragma": "no-cache",
#     "upgrade-insecure-requests": "1",
#     # "sec-fetch-dest": "document",
#     # "sec-fetch-mode": "navigate",
#     # "sec-fetch-site": "none",
#     # "sec-fetch-user": "?1",
# }


# base = "https://www.bestbuy.ca"

session = BestBuyCheckOut(
    "L8J",
    "ON",
    BestBuy(
        "https://www.bestbuy.ca/en-ca/product/lg-ok55-500w-bluetooth-party-system-with-karaoke-dj-effects-only-at-best-buy/14432356"
    ),
)

atcStart = time.perf_counter()
basketID = session.atc(1)
atcTotal = time.perf_counter() - atcStart
print(f"ATC time: {atcTotal}s.")

tokenStart = time.perf_counter()
# Needed to get CSRF token
tx = session.getToken()
tokenTotal = time.perf_counter() - tokenStart
print(f"Token time: {tokenTotal}s.")
# print(tx)


basketStart = time.perf_counter()
res = session.getBasket()
basketTotal = time.perf_counter() - basketStart
print(f"Basket time: {basketTotal}s.")


checkoutStart = time.perf_counter()
res = session.startCheckout()
checkoutTotal = time.perf_counter() - checkoutStart

print(f"Checkout time: {checkoutTotal}s.")