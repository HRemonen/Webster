import os

import queue as q
import json
import tkinter as tk

from tkinter import filedialog

from utils import validators
from utils import request_response
from core.parser import Parser
from core.downloader import Downloader

class Crawler:
    """
    A class that represents crawler object used to crawl websites.
    
    Attributes
    ----------
    start_urls : str | list of strs
        Define starting URL or optionally give list of URLs. First URL in list is then defined
        as the starting point and the rest are stored in Queue.
        URLs must be in correct form: ex. https://example.com/ or https://www.example.com/
       
    allowed_urls : (Optional) list, default = None.
        Define allowed URLs to visit.  
         
    mode : (Optional) str, default = auto.
        Define used mode.
        Default: "auto" -> Supports automation.
        Optional: "manual" -> Manual mode is used with userinterface, does not support automation.
    
    Methods
    -------
    None.
    
    """
    
    def __init__(self, 
                start_urls: str,
                allowed_urls: list = None,
                mode: str = "auto",
        ) -> None:
        self.queue = q.Queue(maxsize=0)
        
        if validators.ModeValidator(mode):
            self.mode = mode
        else: self.mode = "auto"           
        
        if validators.URLValidator(start_urls):
            if isinstance(start_urls, str):
                self.start_urls = start_urls
            elif isinstance(start_urls, list):
                [self.queue.put(url) for url in start_urls]
        else: raise TypeError(f"URL(s) was not of accepted type")
        
        if allowed_urls is not None:
            if validators.URLValidator(allowed_urls):
                self.allowed_urls = allowed_urls
            else: raise RuntimeError(f"URL(s) was not of accepted type")
    
        self.spider = None
        self.parser = None
        self.crawling = False
        
    def crawl(self) -> None:
        if self.crawling:
            raise RuntimeError("Already crawling!")
        self.crawling = True
        
        while self.crawling:
            try:
                if self.queue.empty():
                    raise RuntimeError("Nothing to crawl...")
                
                URL = self.queue.get()
                http_response = request_response.get_http_response(URL)
                
                print("Downloading", http_response)
                http_response.download()
                
            except Exception:
                self.crawling = False
            
            
        

class Interface(Crawler):
    def run(self):
        CHOICES = ["s", "a", "d", "p", "e"]
        print("""
        Welcome to WebSurfer!
        What would you like to do?
        """)

        while True:
            print("Main menu.")
            print(f"""
            Choices:
            (s)ettings..............
            (a)uto downloader.......(auto)
            (d)ownload site.........(manual)
            (p)arse site............(manual)
            (e)xit..................
            """)

            c = input("Enter choice: ").lower()
            if c == "e":
                break
            elif c not in CHOICES:
                print("Incorrect choice, try again")
            elif c == "s":
                self.__settingsMenu()
            elif c == "a":
                self.__autoDownloader()
            elif c == "d":
                self.__downloadMenu()           
            elif c == "p":
                self.__parseMenu()             
            else:
                print("Something went wrong.")

    def __settingsMenu(self):
        SETTINGS_CHOICES = ["c", "i", "b"]

        #TODO:  Implement queue for URLs.
        #       user could import queue from text file or
        #       user could also create queue from dataset URLS.
         
        while True:
            settings_choices = f"""
            (i)mport URLs from text file to queue
            (t)oggle autodownloader auto queue      {self.autoQueue}
            (b)ack
            """
            print("Settings menu.")
            print(settings_choices)

            c = input("Enter choice: ").lower()
            if c == "b":
                break
            elif c == "t":
                self.autoQueue = not self.autoQueue
 
    def __autoDownloader(self):
        #TODO:  Automatic downloader.
        #       Downloads and parses every URL from queue if there is any.
        #       while self.queue.empty() is not True:
        
        pass

    def __downloadMenu(self):
        """
        Download manually selected site address ex. "https://ocw.mit.edu/".
    
        Parameters:
        None.
    
        Returns:
        HTML file.
        """

        print("Download menu.")
        site_to_download = input("Enter site URL: ")
        print()

        Downloader(site_to_download).download_website()

    def __parseMenu(self):
        """
        Parse manually selected html file.
    
        Parameters:
        None.
    
        Returns:
        JSON dataset from the site.
        """

        print("Parse menu.")
        
        root = tk.Tk()
        root.withdraw()
        directory = os.getcwd()+"/downloads"

        try:
            filepath = filedialog.askopenfilename(initialdir=directory, title="Select files")
            if not filepath.endswith(".html"):
                raise TypeError

        except TypeError:
            print("File was not of accepted type.")
            exit()

        except OSError:
            print("Something went from reading the file...")
            exit()

        
        data = Parser(filepath).create_dataset()
        filename = "downloads/scrapedata/" + data["title"]
        
        #FIX: files not showing as json.
        with open(filename, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        #TODO:  You could start downloading all the associated URLs related to
        #       the initial sites URL
        #       for site in data["URLs"]:
        #           site_downloader.download_site(site)


if __name__ == "__main__":
    #ws1 = Interface("https://google.com/")
    #ws1.run()
    #ws1 = WebSurfer("https://google.com/")
    sites = ["https://google.com/", 
            "https://github.com/", 
            "https://youtube.com/"]
    ws = Crawler(sites).crawl()