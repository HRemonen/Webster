"""
Helper file for networking related stuff

"""

import requests

from fileinput import filename

from utils import validators
from core.downloader import Downloader

def get_http_response(url: str) -> requests.Response:
    """
    Return http response using requests package
    """
    if not validators.URLValidator(url):
        raise TypeError(f"URL(s) was not of accepted type")
    try:
        response = requests.get(url, timeout=2)
    except requests.RequestException:
        print("Something went wrong requesting page")
        
    return response

if __name__ == "__main__":
    s="https://webscraper.io/test-sites"
    response, filename = get_http_response(s)
    
    d = Downloader(response).download()
         