import tkinter as tk
import os
import queue
import requests

from tkinter import filedialog
from typing import Type
from pathlib import Path

from bs4 import BeautifulSoup

class Parser:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.initialdir = os.getcwd()+"/downloaded"

        try:
            self.filepath = filedialog.askopenfilename(initialdir=self.initialdir, title="Select files")
            if not self.filepath.endswith(".html"):
                raise TypeError
            self.soup = BeautifulSoup(open(self.filepath, "r"), "html.parser")
        except TypeError:
            print("File was not of accepted type.")
            exit()
        except OSError:
            print("Something went from reading the file...")
            exit()

    def create_dataset(self):
        """
        Creates dataset of chosen html file
    
        Parameters:
        None.
    
        Returns:
        JSON dataset.
        """

        dataset = {
            "website" : self.filepath,
            "title" : "",
            "keywords" : "",
            "description" : "",
            "links" : []
        }

    def parse_anchors(self):
        """
        Parse html file for all the links 
    
        Parameters:
        None.
    
        Returns:
        List of URLs.
        """

        anchors = []
        urls = []

        # check base url from downloaded file.
        with open(self.filepath, "r") as f:
            base_url = f.readline().strip()

        # find every <a> tag from file, with href attribute.
        # store these anchors to a list
        for a in self.soup.find_all("a"):
            anchor = a.attrs['href'] if "href" in a.attrs else ''
            if anchor.startswith("/"):
                anchors.append(anchor)

        # if the file had any anchors, combine these 
        # directories with base url.
        if anchors:
            for a in anchors:
                url = base_url + a
                if url in urls:
                    continue
                urls.append(url)

        return urls

if __name__ == "__main__":
    p = Parser()
    for a in p.parse_anchors():
        print(a)
