from tracemalloc import start
import uuid

import queue as q

from utils import validators
from utils import networking
from core.parser import Parser
from core.downloader import Downloader

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
        Starts crawler with given starting points. Crawls until there is no more websites found.
        Downloads every crawled website.
    
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
            [self.queue.put(url) for url in start_urls]
        else: raise TypeError(f"URL(s) was not of accepted type")
        
        if allowed_urls is not None:
            if validators.URLValidator(allowed_urls):
                self.allowed_urls = allowed_urls
            else: raise TypeError(f"URL(s) was not of accepted type")
    
        self.downloader = Downloader()
        self.parser = None
        self.crawling = False
    
    def __str__(self):
        return f"Crawler: ", self._ID
     
    def crawl(self) -> None:
        if self.crawling:
            raise RuntimeError("Already crawling!")
        self.crawling = True
        print("Starting to crawl...")
        
        while self.crawling:
            try:
                if self.queue.empty():
                    raise RuntimeError("Nothing to crawl...")
            except Exception:
                self.crawling = False
                break
                
            #get next free URL from queue
            URL_to_download = self.queue.get()
            response = networking.get_http_response(URL_to_download)
            self.downloader.give_response(response)
                
            filepath = self.downloader.get_filepath()
            print(filepath)
            filename = self.downloader.get_filename()
                
            #print("Downloading...", filename)
            self.downloader.download()
        
        if self.crawling is False:
            print("Stopping to crawl... Please wait.")

if __name__ == "__main__":
    #ws1 = Interface("https://google.com/")
    #ws1.run()
    #ws1 = WebSurfer("https://google.com/")
    test_sites = ["https://www.w3schools.com/", 
            "https://www.github.com/", 
            "https://www.youtube.com/",
            "https://github.com/HRemonen/Python-Websurfer"]
    
    ws = Crawler(test_sites).crawl()