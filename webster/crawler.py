import uuid
import queue

from concurrent.futures import ThreadPoolExecutor

from typing import Optional

from utils import validators
from utils import url_tools
from net.request import Request
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
        Default: "auto" -> Supports automation.
        
    Methods
    -------
    crawl()
        Starts crawler with given starting points.
    
    """
    
    def __init__(self, 
                start_urls: list,
                allowed_urls: Optional[list] = None,
                mode: Optional[list] = None,
        ) -> None:
        
        self._ID = uuid.uuid1()
        
        if mode is not None:
            if validators.ModeValidator(mode):
                self.mode = mode
        else: self.mode = "auto"           
        
        if validators.URLValidator(start_urls):
            self.start_urls = start_urls
        
        if allowed_urls is not None:
            if validators.URLValidator(allowed_urls):
                self.allowed_urls = allowed_urls
        else: self.allowed_urls = None
        
        self.crawling = False
        self.pool = ThreadPoolExecutor()
        
        self.queue = queue.Queue()
        self.responses = {}
    
    def crawl(self) -> None:
        """
        Crawl domains to get response objects.
        """
        if self.crawling:
            raise RuntimeError("Already crawling!")
        self.crawling = True
        
        self._start_requests(self.start_urls)
             
        while self.crawling:
            print("Queue size:", self.queue.qsize())
            next_request = self.queue.get()
            
            self._crawl(next_request)
            
            if self.queue.empty():
                self.crawling = False
            
        return self.responses
    
    def _start_requests(self, urls: list) -> None:
        """
        Start requesting from the given URLs.
        Put requests to the queue for the crawler to use.
        """
        def _request(url: str) -> Request:
            request = Request(url)

            #Check if allowed url
            if self.allowed_urls is None:
                return request
            elif any(url_tools.URLnetloc(request.url)
                in url_tools.URLnetloc(s) for s in self.allowed_urls):
                return request
            
        requests = self.pool.map(lambda url : _request(url), urls)
        self.pool.map(self.queue.put, requests)
    
    def _crawl(self, rqs):
        """
        Helper function for crawling.
        
        Parse request for new URLs or anchors.
        Start requesting new URLs.
        """
        
        response_anchors = []
        if rqs.url not in self.responses:
                print(f"{self} Crawled {rqs}")
                self.responses[rqs.url] = rqs
                response_anchors = Parser(rqs).parse_anchors()
        else: print(f"{self} Skipped {rqs}")      
                        
        new_URLs = []
        if response_anchors:
            for resp in response_anchors:
                if resp not in self.responses:
                     new_URLs.append(resp)
        
        if new_URLs:
            self._start_requests(new_URLs)               
    
    def __str__(self):
        return f"Crawler: " + str(self._ID)
        
    
if __name__ == "__main__":

    #ws = Crawler(["https://google.com/"])
    sites = [ 
            "https://webscraper.io/test-sites",
            "https://webscraper.io/test-sites", 
            "https://webscraper.io/test-sites", 
            ]
    empty = []
    
    allowed = ["https://webscraper.io/"]
    
    ws = Crawler(sites, allowed_urls=allowed)
    
    print(ws)
    xs = ws.crawl()
    
    print(len(xs))
    print(xs)

  