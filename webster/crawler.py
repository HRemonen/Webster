import uuid

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
    
    def _start_requests(self, urls: list) -> object:
        """
        Start requesting urls from the starting urls.
        """
        
        for url in urls:
            request = Request(url)
            if self.allowed_urls is not None:
                if any(url_tools.URLnetloc(request.url)
                    in url_tools.URLnetloc(s) for s in self.allowed_urls):
                    yield request
            else: yield request
    
    def crawl(self) -> None:
        """
        Crawl domains to get response objects.
        """
        
        responses = {}
        requests = self._start_requests(self.start_urls)
        
        if self.crawling:
                raise RuntimeError("Already crawling!")
        self.crawling = True
        
        while self.crawling:
            response_anchors = []
            
            for rqs in requests:
                if rqs is not None:
                    if rqs.url not in responses:
                        print("Adding...", rqs.url)
                        responses[rqs.url] = rqs
                        try:
                            response_anchors = Parser(rqs).parse_anchors()
                        except Exception:
                            #TODO: Check why sometimes request is empty.
                            continue
                    else: print("Skipping url,", rqs.url)
                        
                else: continue
                
            if response_anchors:
                requests = self._start_requests(response_anchors)
            else:
                print("Nothing to crawl. Exiting crawler.")
                self.crawling = False
            
        return responses
    
    def __str__(self):
        return f"Crawler: " + str(self._ID)
        
    
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
    print(ws)
    xs = ws.crawl()
    
    print(len(xs))
    print(xs)

  