from bs4 import BeautifulSoup
import requests
import re


def getWebsite(url: str) -> BeautifulSoup:
    """
    Convenience method to render webpage into a BeautifulSoup object
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

    page = requests.get(url, headers=headers)

    assert page.status_code < 400, f"Website returned {page.status_code} error."

    return BeautifulSoup(page.content, 'html.parser')


def getAmazonPrice(url: str) -> float:
    """
    Retrieves prices of product from Amazon when given its URL
    """
    soup = getWebsite(url)

    priceDiv = soup.find(name="div", attrs={"id": "price"})

    price = priceDiv.find(id=re.compile(
        "^priceblock_ourprice$|^priceblock_dealprice$")).get_text().strip()
    price = float(price[4:].strip())

    return price


def getBestBuyPrice(url: str) -> float:
    """
    Retrieves prices of product from Best Buy when given its URL
    """
    soup = getWebsite(url)

    title = soup.find(name="h1", attrs={"class": re.compile(
        "^productName")}).get_text().strip()

    priceDiv = soup.find("div", class_=re.compile("^pricingContainer"))
    price = float(priceDiv.find(itemprop="price")["content"])

    print(price)
    return price


getBestBuyPrice(
    "https://www.bestbuy.ca/en-ca/product/hp-14-chromebook-mineral-silver-intel-celeron-n4000-64gb-emmc-4gb-ram-chrome/14481355")


# print(getAmazonPrice("https://www.amazon.ca/New-Balance-Sport-Slide-Sandal/dp/B07JGP1PXF?ref_=Oct_DLandingS_D_5ccd8aa7_61&smid=A3DWYIK6Y9EEQB&th=1&psc=1"))
