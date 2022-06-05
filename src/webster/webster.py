import os

import queue as q
import json
import tkinter as tk

from tkinter import filedialog

from src.utils.loader import Downloader
from src.utils.parser import Parser
from src.utils import validators


class Webster:
    """
    A class that represents WebSurfer module used to download and parse websites.
    Creates dataset of said websites. 
    
    Attributes
    ----------
    start : str | list of strs
        Define starting URL or optionally give list of URLs. First URL in list is then defined
        as the starting point and the rest are stored in Queue.
        URLs must be in correct form: ex. https://example.com/ or https://www.example.com/
        
    mode : (Optional) str, default = auto.
        Define used mode.
        Default: "auto" -> Supports automation.
        Optional: "manual" -> Manual mode is used with userinterface, does not support automation.
        
    autoQueue : (Optional) bool, default = False.
        Define if parsed website URLs contribute to the queue automatically.
        Queued items are waiting to be parsed.
        Default: False -> Does not add parsed URLs to the queue.
        Optional: True -> Automatically add parsed URLs to the queue, making the program run recursively.
    
    
    Methods
    -------
    None.
    
    """
    def __init__(self, 
                 #name: str,
                 start: str,
                 mode: str = "auto",
                 autoQueue: bool = False,
                 #allowed: str = None,
                #status: bool = True
        ) -> None:
        
        self.queue = q.Queue(maxsize=0)
        
        if validators.ModeValidator(mode):
            self.mode = mode
        else: self.mode = "auto"           
        
        if not isinstance(autoQueue, bool):
            raise TypeError(f"mode type {autoQueue} not understood")
        else: self.autoQueue = autoQueue
        
        if validators.URLValidator(start):
            if isinstance(start, str):
                self.start = start
            elif isinstance(start, list):
                self.start = start[0]
                [self.queue.put(url) for url in start[1:]]
        else: raise TypeError(f"URL(s) was not of accepted type")
    

class Interface(Webster):
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
    ws1 = Interface("https://google.com/")
    ws1.run()
    #ws1 = WebSurfer("https://google.com/")