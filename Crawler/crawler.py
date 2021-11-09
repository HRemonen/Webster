from bs4 import BeautifulSoup
from pathlib import Path

import queue
import requests

def crawl(base_url, start_anchor):
    search_anchors = queue.Queue()
    urls = []

    while True:
        if not start_anchor:
            start_anchor = "/"
        response = requests.get(base_url + start_anchor)

        soup = BeautifulSoup(response.text, "html.parser")
        anchors = find_local_anchors(soup, start_anchor)

        if anchors:
            for a in anchors:
                url = base_url + a
                if url in urls:
                    continue
                if not Path(a).suffix:
                    search_anchors.put(a)
                urls.append(url)
                print(url)
                
        if search_anchors.empty():
            break
        start_anchor = search_anchors.get()

    return urls


def find_local_anchors(soup, start_anchor):
    anchors = []
    for a in soup.find_all("a"):
        anchor = a.attrs['href'] if "href" in a.attrs else ''
        if anchor.startswith(start_anchor):
            anchors.append(anchor)     
    return anchors

if __name__ == "__main__":
    url = "https://webscraper.io/test-sites"
    start_anchor = "/"

    urls = crawl(url, start_anchor)
    print(len(urls))