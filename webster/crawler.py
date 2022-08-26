import time
import uuid
import queue

from concurrent.futures import ThreadPoolExecutor

from typing import Optional

from webster import robotstxt
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
        
        self.robots_allowed = {}
        self.robots_excluded = {}
    
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
            print("Queue size:", self.queue.qsize())        #SWITCH TO LOGGING? NECESSARY????
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
            #responses. Check this before anything.
            #Also check if the URL has already been excluded by the robotstxt
            #ignore these scenarios.
            if url not in self.responses and url not in self.robots_excluded:
                #BEFORE WE MAKE THE REQUEST TO THE SERVER!!!!
                #IF we have already encountered this URL and fetched its
                #robots.txt file, we have stored it inside robots_allowed.
                #IF we haven't, then we have to fetch the robots.txt and read it
                base_url = url_tools.base_url(url)
                if base_url not in self.robots_allowed:
                    rp = robotstxt.RobotParser(base_url + "robots.txt")
                    #Store the RobotParser object to the hashmap for later use cases.
                    self.robots_allowed[base_url] = rp
                
                rp = self.robots_allowed[base_url]
                
                if rp.allowed(url):
                    #Check robots.txt crawl_delay and act accordingly
                    #We do not want to overload the host and have our IP banned...
                    #Set delay to the value in robots.txt or 1 if not given.
                    delay = 1 if not rp.delay() else rp.delay()
                    
                    #Send the request to the server and sleep for the time of
                    #delay parameter.
                    request = Request(url)
                    time.sleep(delay)
                    
                    print(f"{self} Requesting {request}")                   #SWITCH TO LOGGING
                    self.responses[request.url] = request
                    
                    #IF allowed urls was not given as parameter, and
                    #we are respecting the robots.txt we can return our request.
                    if self.allowed_urls is None:
                        return request
                    
                    #IF allowed urls are given, check if request is 
                    #in the allowed ulrs. 
                    elif any(url_tools.URLnetloc(request.url)
                            in url_tools.URLnetloc(s) 
                            for s 
                            in self.allowed_urls):
                        return request
                else:
                    #Request did not respect the robots.txt so we skip that
                    #and store the excluded url for later use.
                    #The content of this hashmap is trivial, so we store 1 as the value.
                    self.robots_excluded[base_url] = 1
                    print(f"{self} Robots.txt not allowing {base_url}")       #SWITCH TO LOGGING
            
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
    
        print(f"{self} Parsing {rqs}")                                      #SWITCH TO LOGGING
        
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
            print(f"{self} Skipping {rqs}")                                 #SWITCH TO LOGGING
                              
    def __str__(self):
        return f"Crawler: " + str(self._ID)
        
if __name__ == "__main__":
    url = ""
    sites = [ 
            url, 
            ]
    empty = []
    
    allowed = [""]
    
    ws = Crawler(sites)
    
    print(ws)
    xs = ws.crawl()
    
    print(len(xs))
    print(xs)

  