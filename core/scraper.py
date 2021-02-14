from bs4 import BeautifulSoup
import requests
from django.utils import timezone
from core.models import AssetData


def get_info(asset, url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    price = None
    for x in soup.find_all("div", class_="price-large"):
        price = x.text.split("$")[1]
    price = float(price.replace(',', ''))
    divs = soup.find_all("div", class_="price-medium")
    low_24h = None
    for x in divs[2:3]:
        low_24h = x.text.split("$")[1]
    low_24h = float(low_24h.replace(',', ''))
    high_24h = None
    for x in divs[3:4]:
        high_24h = x.text.split("$")[1]
    high_24h = float(high_24h.replace(',', ''))
    volatility = None
    for x in divs[5:6]:
        volatility = float(x.text)

    spans = soup.find_all("span", class_="percent-value-text")

    retunrs_24h = None
    for x in spans[1:2]:
        retunrs_24h = float(x.text)
    retunrs_ytd = None
    for x in spans[2:]:
        retunrs_ytd = float(x.text)
    data_datetime = timezone.now()

    data = AssetData.objects.create(
        asset=asset,
        price=price,
        low_24h=low_24h,
        high_24h=high_24h,
        retunrs_24h=retunrs_24h,
        retunrs_ytd=retunrs_ytd,
        volatility=volatility,
        data_datetime=data_datetime

    )

    data.save()
