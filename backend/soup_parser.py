import requests
from bs4 import BeautifulSoup


def walmart_json(soup: BeautifulSoup):
    items = soup.find_all(attrs={"data-testid": "item-stack"})
    if (items.__len__() == 0):
        print("Didn't find item stack")
        return None
    for item in items[0].children:
        intermediate = first_child(first_child(item))
        if (intermediate is None):
            break
        link = walmart_link_cleaner(first_child(intermediate)["href"])
        if (len(link) == 0):
            break;
        #print(link)
    
    # TODO: return data as JSON
    pass


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

