import uuid
import queue

from concurrent.futures import ThreadPoolExecutor

from typing import Optional

from webster.utils import validators
from webster.utils import url_tools
from webster.net.request import Request
from webster.core.parser import Parser


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
        
        self.queue = queue.Queue()
        #Store response objects in a hashmap for easy access.
        self.responses = {}
    
    def crawl(self) -> None:
        """
        Crawl domains to get Crawler.Request objects.
        """
        
        if self.crawling:
            raise RuntimeError("Already crawling!")
        self.crawling = True
        
        #Get requests to queue
        self._start_requests(self.start_urls)
             
        while self.crawling:
            print("Queue size:", self.queue.qsize())
            next_request = self.queue.get()
            
            #Check for bogus requests
            if next_request is not None:
                self._crawl(next_request)
            
            if self.queue.empty():
                self.crawling = False
            
        return self.responses
    
    def _start_requests(self, urls: list) -> None:
        """
        Start requesting from the given URLs.
        Send Requests to ThreadPool and execute them using threading.
        
        Put Webster.Request objects to queue.
        """
        
        def _request(url: str) -> Request:
            """
            Helper function for making get requests.
            
            Checks if request is already made to this URL.
            """
            
            #If this URL is already requested, it is stored in 
            #responses hashmap. Check this before anything.
            if url not in self.responses:
                request = Request(url)
                print(f"{self} Requesting {request}")
                self.responses[request.url] = request
                
                #Check if allowed urls exists.
                if self.allowed_urls is None:
                    return request
                
                #IF allowed urls are given, check if request is 
                #in the allowed ulrs. 
                elif any(url_tools.URLnetloc(request.url)
                        in url_tools.URLnetloc(s) 
                        for s 
                        in self.allowed_urls):
                    return request
        
        #Create thread pool executor. Worker count matches our 
        #count of awaiting urls.
        with ThreadPoolExecutor(len(urls)) as executor:
            #Add requests to ThreadPool    
            request_futures = executor.map(lambda url : _request(url), urls)
            #Add Crawler.Requests to queue
            _ = executor.map(self.queue.put, request_futures)
    
    def _crawl(self, rqs: Request) -> None:
        """
        Helper function for crawling.
        
        Parse request for new URLs or anchors.
        Start requesting new URLs.
        """
    
        print(f"{self} Parsing {rqs}")
        
        try:
            #Parse response anchors with Parser module.
            response_anchors = Parser(rqs).parse_anchors()
            #Store new URLs to this list later on.
            new_URLs = []
            
            #If new anchors were found, add them to the
            #list if they have not already been requested.
            if response_anchors:
                for resp in response_anchors:
                    if resp not in self.responses:
                        new_URLs.append(resp)
            
            #IF new URLs were found, start requesting them.
            if new_URLs:
                self._start_requests(new_URLs) 
        
        #Skip invalid requests where Webster.Request.body is None
        #and thus cannot be parsed.
        #Webster.Parser module raises TypeError if body is None.       
        except TypeError:
            print(f"{self} Skipping {rqs}")
                              
    def __str__(self):
        return f"Crawler: " + str(self._ID)
        
if __name__ == "__main__":
    url = "https://github.com/"
    sites = [ 
            url, 
            ]
    empty = []
    
    allowed = ["https://github.com/"]
    
    ws = Crawler(sites)
    
    print(ws)
    xs = ws.crawl()
    
    print(len(xs))
    print(xs)

  