import os

import requests
from utils import validators
from core.downloader import Downloader

def get_http_response(url: str) -> requests.Response:
    if not validators.URLValidator(url):
        raise TypeError(f"URL(s) was not of accepted type")
    try:
        response = requests.get(url, timeout=1)
    except requests.RequestException:
        print("Something went wrong requesting page")
        
    filename = response.url.split("//")[1].replace("/", "") + ".html"    
    return Downloader(response, filename)

        
        
if __name__ == "__main__":
    s="https://webscraper.io/test-sites"

    
    d = get_http_response(s)
    d.download()     