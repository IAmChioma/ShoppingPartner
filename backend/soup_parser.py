import requests
from bs4 import BeautifulSoup
import json


def walmart_json(soup: BeautifulSoup):
    result = []
    items = soup.find_all(attrs={"data-testid": "item-stack"})
    if (items.__len__() == 0):
        print("Didn't find item stack")
        return json.dumps(result)
    for item in items[0].children:
        intermediate = first_child(first_child(item))
        if (intermediate is None):
            break
        link = walmart_link_cleaner(first_child(intermediate)["href"])
        if (len(link) == 0):
            break
        #print(link)
        img_url = intermediate.find("img")["src"]
        #print(img_url)
        priceTag = intermediate.find(attrs={"data-automation-id": "product-price"})
        price = "n/a"
        i = 0
        for child in priceTag.children:
            if (i == 1):
                price = child.contents
                break
            i += 1
        price = price[0]
        price = price[price.find("$"):len(price)]
        #print(price)
        titleTag = intermediate.find(attrs={"data-automation-id": "product-title"})
        title = titleTag.contents[0]
        #print(title)
        data = {"link": link, "img_url": img_url, "price": price, "title": title}
        result.append(data)
    return json.dumps(result)


def walmart_link_cleaner(url):
    start = url.find("https%3A%2F%2F")
    end = url.find("%3F", start, len(url))
    url = url[start:end]
    return requests.utils.unquote(url)


def first_child(tag):
    if (tag is None):
        return None
    for child in tag.children:
        return child
    return None

