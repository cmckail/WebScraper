from datetime import datetime
from webscraper.utility.utils import add_to_database
from webscraper.models.bestbuy import BestBuy, BestBuyCheckOut
from webscraper.models.cc import CanadComputersCheckout, CanadaComputers
from webscraper.models.profiles import Address, ShoppingProfile, CreditCard
import regex, logging, requests, json, random
from enum import Enum
import requests, json
from bs4 import BeautifulSoup
from base64 import b64decode
import time, lxml
from Crypto.PublicKey import RSA

# profile = ShoppingProfile(
#     email="anthonyma940603@gmail.com",
#     actEmail="anthonyma940603@gmail.com",
#     actPassword="8290F9AF",
#     shippingAddress=Address(
#         address="3692 Water St",
#         city="Kitchener",
#         firstName="Test",
#         lastName="Test",
#         phoneNumber="2894439715",
#         province="ON",
#         postalCode="N2H5A5",
#     ),
#     creditCard=CreditCard(
#         firstName="Test",
#         lastName="Test",
#         creditCardNumber="4263982640269299",
#         cvv="837",
#         expMonth="2",
#         expYear="2023",
#         type="VISA",
#         billingAddress=Address(
#             address="3692 Water St",
#             city="Kitchener",
#             firstName="Test",
#             lastName="Test",
#             phoneNumber="2894439715",
#             province="ON",
#             postalCode="N2H5A5",
#         ),
#     ),
# )

with open("realprofile.json", "r") as f:
    result = json.load(f)

    shippingAddress = Address(**result["shippingAddress"])
    billingAddress = Address(**result["creditCard"]["billingAddress"])

    result["creditCard"]["billingAddress"] = billingAddress
    result["shippingAddress"] = shippingAddress
    card = CreditCard(**result["creditCard"])

    result["creditCard"] = card

    profile = ShoppingProfile(**result)


item = BestBuy(
    "https://www.bestbuy.ca/en-ca/product/razer-viper-esports-16000-dpi-5g-optical-sensor-gaming-mouse-black/13845995"
)

checkout = BestBuyCheckOut(profile=profile, item=item)

order_id = checkout.checkout()

print(order_id)

# cookies, res = checkout.checkout()

# with open("cookies.py", "w") as f:
#     f.write(str(cookies))

# with open("4-bankresponse.html", "wb") as f:
#     f.write(res.content)

# session = requests.Session()

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en-US,en;q=0.9",
#     "cache-control": "no-cache",
#     "Connection": "keep-alive",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "dnt": "1",
#     "host": "0eaf.cardinalcommerce.com",
#     "origin": "https://www.bestbuy.ca",
#     "Pragma": "no-cache",
#     "Referer": "https://www.bestbuy.ca/",
#     "sec-fetch-dest": "iframe",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "cross-site",
#     "sec-fetch-user": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
# }

# data = {
#     "PaReq": "P.97c61ec938669abf31da9046285e9eac75a806c9d67c2c9f3bd60ceba2e4135ef8b770171d73875676563db695b65b20af4a694a10b4d1c3812320e34c610578",
#     "MD": "30e3d92d-f2e5-42da-880d-d3d07590ae8e",
#     "TermUrl": "https://www.bestbuy.ca/api/checkout/payment/secureauth/bankresponse",
# }

# res = session.post(
#     "https://0eaf.cardinalcommerce.com/EAFService/jsp/v1/redirect",
#     headers=headers,
#     data=data,
# )

# with open("redirect.html", "wb") as f:
#     f.write(res.content)

# soup = BeautifulSoup(res.content, "html.parser")

# with open("1-redirect.html", "r") as f:
#     soup = BeautifulSoup(f.read(), "html.parser")

# form = soup.find(name="form", attrs={"method": "POST"})
# url = form["action"]
# inputs = form.find_all(name="input", attrs={"type": "hidden"})

# data = {}
# for i in inputs:
#     name = i["name"]
#     value = i["value"]
#     data[name] = value


# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en-US,en;q=0.9",
#     "cache-control": "no-cache",
#     "Connection": "keep-alive",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "dnt": "1",
#     "host": "authentication.cardinalcommerce.com",
#     "origin": "https://0eaf.cardinalcommerce.com",
#     "Pragma": "no-cache",
#     "Referer": "https://0eaf.cardinalcommerce.com/",
#     "sec-fetch-dest": "iframe",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "same-site",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
# }


# res = session.post(url, headers=headers, data=data)

# with open("2-payer-authentication.html", "wb") as f:
#     f.write(res.content)

# with open("2-payer-authentication.html", "r") as f:
#     soup = BeautifulSoup(f.read(), "html.parser")

# form = soup.find(name="form", attrs={"id": "TermForm"})
# url = form["action"]
# inputs = form.find_all(name="input", attrs={"type": "hidden"})
# data = {}

# for i in inputs:
#     data[i["name"]] = i["value"]


# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en-US,en;q=0.9",
#     "cache-control": "no-cache",
#     "Connection": "keep-alive",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "dnt": "1",
#     "host": "0eaf.cardinalcommerce.com",
#     "origin": "https://authentication.cardinalcommerce.com",
#     "Pragma": "no-cache",
#     "Referer": "https://authentication.cardinalcommerce.com/",
#     "sec-fetch-dest": "iframe",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "same-site",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
# }

# res = session.post(url, headers=headers, data=data)

# with open("3-term.html", "wb") as f:
#     f.write(res.content)

# with open("3-term.html", "r") as f:
#     soup = BeautifulSoup(f.read(), "html.parser")

# form = soup.find(name="form", attrs={"method": "post"})
# url = form["action"]

# inputs = form.find_all(name="input", attrs={"type": "hidden"})

# data = {}
# for i in inputs:
#     data[i["name"]] = i["value"]

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en-US,en;q=0.9",
#     "cache-control": "no-cache",
#     "Connection": "keep-alive",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "dnt": "1",
#     "host": "0eaf.cardinalcommerce.com",
#     "origin": "https://0eaf.cardinalcommerce.com",
#     "Pragma": "no-cache",
#     "Referer": "https://0eaf.cardinalcommerce.com/",
#     "sec-fetch-dest": "iframe",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "cross-site",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
# }

# res = session.post(url, headers=headers, data=data)
# with open("4-bankresponse.html", "wb") as f:
#     f.write(res.content)


# url = "https://www.canadacomputers.com/product_info.php?cPath=11_180_181&item_id=136484&sid=kv9lsjdtpa7shoh3mvsisgsen0"


# with open("realprofile.json", "r") as f:
#     result = json.load(f)

# shippingAddress = Address(**result["shippingAddress"])
# billingAddress = Address(**result["creditCard"]["billingAddress"])

# result["creditCard"]["billingAddress"] = billingAddress
# result["shippingAddress"] = shippingAddress
# card = CreditCard(**result["creditCard"])

# result["creditCard"] = card

# profile = ShoppingProfile(**result)


# itemStart = time.perf_counter()
# item = CanadaComputers(
#     "https://www.canadacomputers.com/product_info.php?cPath=21_279_275&item_id=140314"
# )
# itemTotal = time.perf_counter() - itemStart
# print(f"Item time: {itemTotal}s")

# checkoutStart = time.perf_counter()
# checkout = CanadComputersCheckout(profile=profile, item=item)
# checkoutTotal = time.perf_counter() - checkoutStart
# print(f"Checkout time: {checkoutTotal}s")

# sidStart = time.perf_counter()
# checkout.getSID()
# sidTotal = time.perf_counter() - sidStart
# print(f"SID time: {sidTotal}s")

# loginStart = time.perf_counter()
# res = checkout.login()
# loginTotal = time.perf_counter() - loginStart
# print(f"Login time: {loginTotal}s")

# with open("login.html", "w") as f:
#     f.write(res.text)

# exit(0)

# deleteStart = time.perf_counter()
# checkout.deleteCart()
# deleteTotal = time.perf_counter() - deleteStart
# print(f"Delete time: {deleteTotal}s")

# atcStart = time.perf_counter()
# res = checkout.atc()
# atcTotal = time.perf_counter() - atcStart
# print(f"ATC time: {atcTotal}s")

# with open("atc.html", "wb") as f:
#     f.write(res.content)

# res = checkout.getCart()

# with open("cart.html", "w") as f:
#     f.write(str(res))
# f.write(res.text)

# shippingStart = time.perf_counter()
# res = checkout.shipping()
# shippingTotal = time.perf_counter() - shippingStart
# print(f"Shipping time: {shippingTotal}s")

# with open("shipping.html", "wb") as f:
#     f.write(res.content)

# deliveryStart = time.perf_counter()
# res = checkout.delivery()
# deliveryTotal = time.perf_counter() - deliveryStart
# print(f"Delivery time: {deliveryTotal}s")

# with open("delivery.html", "w") as f:
#     f.write(res.text)

# paymentStart = time.perf_counter()
# res = checkout.payment()
# paymentTotal = time.perf_counter() - paymentStart
# print(f"Payment time: {paymentTotal}s")

# with open("payment.html", "w") as f:
#     f.write(res.text)

# reviewStart = time.perf_counter()
# checkout.review()
# reviewTotal = time.perf_counter() - reviewStart
# print(f"Review time: {reviewTotal}s")

# with open("review.html", "w") as f:
#     f.write(res.text)

# monerisStart = time.perf_counter()
# res = checkout.moneris()
# monerisTotal = time.perf_counter() - monerisStart
# print(f"Moneris time: {monerisTotal}s")

# with open("moneris-post-3dsecure.html", "wb") as f:
#     f.write(res.content)

# with open("test.json", "w") as f:
#     f.write(res.text)

# res = checkout.success()

# with open("success.html", "wb") as f:
#     f.write(res.content)


# monerisResult = res.json()
# if monerisResult["response"]["data"]["doVbv"] == "true":
#     html = b64decode(monerisResult["response"]["data"]["form"])

#     with open("moneris2.html", "wb") as f:
#         f.write(html)

#     soup = BeautifulSoup(str(html), "html.parser")

#     form = soup.find(name="form", attrs={"name": "downloadForm"})
#     url = form.get("action").strip()

#     data = {}

#     inputs = soup.find_all(name="input", attrs={"type": "hidden"})

#     for input in inputs:
#         data[input["name"]] = input["value"]

#     headers = {
#         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "accept-encoding": "gzip, deflate, br",
#         "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
#         "cache-control": "max-age=0",
#         "content-type": "application/x-www-form-urlencoded",
#         "origin": "https://www3.moneris.com",
#         "referer": "https://www3.moneris.com/HPPDP/hprequest.php",
#         "upgrade-insecure-requests": "1",
#         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
#     }

#     res = checkout.session.post(url, data=data, headers=headers)

#     headers["origin"] = "https://authentication.cardinalcommerce.com"
#     headers["referer"] = res.url

#     with open("3dsecure.html", "wb") as f:
#         f.write(res.content)

#     soup = BeautifulSoup(res.text, "html.parser")

#     form = soup.find(name="form", attrs={"id": "TermForm"})
#     url = form.get("action").strip()

#     inputs = form.find_all(name="input", attrs={"type": "hidden"})
#     data = {}

#     for input in inputs:
#         data[input["name"]] = input["value"]

# data["PaRes"] = form.find(
#     name="input", attrs={"type": "hidden", "name": "PaRes"}
# ).get("value")

# url += "?" + form.find(name="input", attrs={"type": "hidden", "name": "MD"}).get(
#     "value"
# )

# res = checkout.session.post(url, data=data, headers=headers)

# res = checkout.session.post(
#     "https://www3.moneris.com/HPPDP/hprequest.php", data=data
# )

# with open("moneris-post-3dsecure.html", "wb") as f:
#     f.write(res.content)


# with open("success.html", "r") as f:
#     soup = BeautifulSoup(f.read(), "html.parser")

# pattern = regex.compile(r"^Order Number: (\d+)$")

# order = soup.find(text=pattern)

# id = regex.search(pattern, order)

# print(id.group(1))