import site_downloader
import site_parser
import queue
import json
import os
import tkinter as tk

from tkinter import filedialog

from bs4 import BeautifulSoup

class WebSurfer:
    def __init__(self) -> None:
        self.queue = queue.Queue()
        self.autoQueue = False

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

        #Implement queue for URLs.
        #user could import queue from text file or
        #user could also create queue from dataset urls.
         
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
        #Automatic downloader.
        #Downloads and parses every URL from queue if there is any.
        #while self.queue.empty() is not True:


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

        site_downloader.download_site(site_to_download)

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
        directory = os.getcwd()+"/downloaded"

        try:
            filepath = filedialog.askopenfilename(initialdir=directory, title="Select files")
            if not filepath.endswith(".html"):
                raise TypeError
            soup = BeautifulSoup(open(filepath, "r"), "html.parser")

        except TypeError:
            print("File was not of accepted type.")
            exit()

        except OSError:
            print("Something went from reading the file...")
            exit()

        p = site_parser.Parser(soup, filepath)
        filename = "downloads/scrapedata/" + p.create_dataset()["title"]
        data = p.create_dataset()

        with open(filename, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        #You could start downloading all the associated URLs related to
        #the initial sites URL
        #for site in data["URLs"]:
            #site_downloader.download_site(site)


if __name__ == "__main__":
    ws1 = WebSurfer()
    ws1.run()