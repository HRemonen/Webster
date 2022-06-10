import uuid

import queue as q

from utils import validators
from utils import http_response
from core.parser import Parser

class Crawler:
    """
    A class that represents crawler object used to crawl websites.
    
    Attributes
    ----------
    start_urls : list
        Define starting URLs as a list. First URL in list is then defined
        as the starting point and the rest are stored in Queue.
        URLs must be in correct form: ex. https://example.com/ or https://www.example.com/
       
    allowed_urls : (Optional) list, default = None.
        Define allowed URLs to visit.  
         
    mode : (Optional) str, default = auto.
        Caution:
            NotImplemented
        Define used mode.
        Default: "auto" -> Supports automation.
        
    
    Methods
    -------
    crawl()
        Starts crawler with given starting points.
    
    """
    
    def __init__(self, 
                start_urls: list,
                allowed_urls: list = None,
                mode: str = None,
        ) -> None:
        self.queue = q.Queue(maxsize=0)
        self._ID = uuid.uuid1()
        
        if mode is not None:
            if validators.ModeValidator(mode):
                self.mode = mode
        else: self.mode = "auto"           
        
        if validators.URLValidator(start_urls):
            self.start_urls = start_urls
        else: raise TypeError(f"URL(s) was not of accepted type")
        
        if allowed_urls is not None:
            if validators.URLValidator(allowed_urls):
                self.allowed_urls = allowed_urls
            else: raise TypeError(f"URL(s) was not of accepted type")
        
        self.crawling = False
    
    def _start_requests(self, urls):
        """
        Start requesting urls from the starting urls.
        """
        
        for url in urls:
            if any(http_response.netloc(url) 
                   in s for s in self.allowed_urls):
                yield http_response.response(url)
            else: continue
    
    def crawl(self) -> None:
        """
        Crawl domains to get response objects.
        """
        responses = {}
        items = self._start_requests(self.start_urls)
        
        if self.crawling:
                raise RuntimeError("Already crawling!")
        self.crawling = True
        
        while self.crawling: 
            for item in items:
                item_anchors = Parser(item).parse_anchors()

                if item.url not in responses:
                    print("Adding...", item.url)
                    responses[item.url] = item
                
            items = self._start_requests(item_anchors)
            
        return responses
    
    def __str__(self):
        return f"Crawler: ", self._ID
        
    
if __name__ == "__main__":
    #ws1 = Interface("https://google.com/")
    #ws1.run()
    #ws1 = WebSurfer("https://google.com/")
    sites = [ 
            "https://webscraper.io/test-sites",  
            ]
    empty = []
    
    allowed = ["https://webscraper.io/"]
    
    ws = Crawler(sites, allowed_urls=allowed)
    xs = ws.crawl()
    
    print(len(xs))

  