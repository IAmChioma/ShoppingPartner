import requests
from bs4 import BeautifulSoup


def request_session(url: str) -> BeautifulSoup:
    r = requests.get(url)
    if (r.status_code != 200):
        print("ERROR: returned status code", r.status_code)
        return None
    return BeautifulSoup(r.content, 'html.parser')
