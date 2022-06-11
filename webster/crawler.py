import uuid

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
    
    def _start_requests(self, urls):
        """
        Start requesting urls from the starting urls.
        """
        
        for url in urls:
            if self.allowed_urls is not None:
                if any(http_response.netloc(url) 
                    in http_response.netloc(s) for s in self.allowed_urls):
                    yield http_response.response(url)
            else: yield http_response.response(url)
    
    def crawl(self) -> None:
        """
        Crawl domains to get response objects.
        """
        
        responses = {}
        response_list = self._start_requests(self.start_urls)
        
        if self.crawling:
                raise RuntimeError("Already crawling!")
        self.crawling = True
        
        while self.crawling:
            response_anchors = []
            
            for resp in response_list:
                if resp is not None:
                    if resp.url not in responses:
                        print("Adding...", resp.url)
                        responses[resp.url] = resp
                        response_anchors = Parser(resp).parse_anchors()
                    else: print("Skipping url,", resp.url)
                        
                else: continue
                
            if response_anchors:
                response_list = self._start_requests(response_anchors)
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

  