import requests
from bs4 import BeautifulSoup
import soup_parser


fake_headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br, zstd",
"DNT": "1",
"Sec-GPC": "1",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "none",
"Sec-Fetch-User": "?1",
"Priority": "u=0, i"
}


def request_session(url, headers) -> BeautifulSoup:
    r = requests.get(url, headers = headers)
    if (r.status_code != 200):
        print("ERROR: returned status code", r.status_code)
        return None
    return BeautifulSoup(r.content, 'html.parser')


def walmart_request(search_phrase: str):
    url = "https://www.walmart.com/search?q=" + search_phrase.replace(" ", "+")
    fake_headers["Host"] = "www.walmart.com"
    response = request_session(url, fake_headers)
    if (response is None):
        return None
    return soup_parser.walmart_json(response)

