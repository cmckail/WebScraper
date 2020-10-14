from webscraper.models.bestbuy import BestBuy, BestBuyCheckOut
from webscraper.models.cc import CanadaComputers
from webscraper.models.profiles import ShoppingProfile, CreditCard
import regex, logging, requests, json, random
from enum import Enum
import requests, json
from bs4 import BeautifulSoup
import time
from Crypto.PublicKey import RSA


class Sites(Enum):
    bestbuy = BestBuy
    cc = CanadaComputers


item = Sites.bestbuy.value(
    "https://www.bestbuy.ca/en-ca/product/nintendo-switch-console-with-neon-red-blue-joy-con/13817625"
)

print(item)


# profile = ShoppingProfile(
#     address="3692 Water St",
#     city="Kitchener",
#     country="CA",
#     email="test@gmail.com",
#     firstName="Test",
#     lastName="test",
#     phoneNumber="2894439715",
#     postalCode="N2H5A5",
#     province="ON",
#     creditCardNumber="4263982640269299",
#     cvv="837",
#     expMonth="2",
#     expYear="2023",
# )

# itemStart = time.perf_counter()
# item = BestBuy(
#     "https://www.bestbuy.ca/en-ca/product/nintendo-switch-console-with-neon-red-blue-joy-con/13817625"
# )
# itemTotal = time.perf_counter() - itemStart
# print(f"Item time: {itemTotal}s.")

# session = BestBuyCheckOut(
#     profile=profile,
#     item=item,
# )

# statusStart = time.perf_counter()
# print(f"Is available: {item.isAvailable}")
# statusTotal = time.perf_counter()
# print(f"Status time: {statusTotal}s.")


# atcStart = time.perf_counter()
# basketID = session.atc(1)
# atcTotal = time.perf_counter() - atcStart
# print(f"ATC time: {atcTotal}s.")

# tokenStart = time.perf_counter()
# # Needed to get CSRF token
# tx = session.getToken()
# tokenTotal = time.perf_counter() - tokenStart
# print(f"Token time: {tokenTotal}s.")
# # print(tx)


# basketStart = time.perf_counter()
# res = session.getBasket()
# basketTotal = time.perf_counter() - basketStart
# print(res)
# print(f"Basket time: {basketTotal}s.")


# checkoutStart = time.perf_counter()
# res = session.startCheckout()
# checkoutTotal = time.perf_counter() - checkoutStart
# print(f"Checkout time: {checkoutTotal}s.")

# paymentStart = time.perf_counter()
# res = session.startPayment()
# paymentTotal = time.perf_counter() - paymentStart
# print(res)
# print(f"Payment time: {paymentTotal}s.")

# submitStart = time.perf_counter()
# res = session.submitOrder()
# submitTotal = time.perf_counter() - submitStart
# print(res)
# print(f"Submit time: {submitTotal}s.")

# encrypted = CreditCard.encrypt(4263982640269299)
# # print(encrypted)
# decrypted = CreditCard.decrypt(encrypted)
# print(decrypted)