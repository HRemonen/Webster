import tkinter as tk
import os

from tkinter import filedialog

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

    def __get_base_url(self):
        with open(self.filepath, "r") as f:
            base_url = f.readline().strip()
        return base_url

    def __parse_anchors(self):
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
        
        base_url = self.__get_base_url()
        

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


    def create_dataset(self):
        """
        Creates dataset of chosen html file
    
        Parameters:
        None.
    
        Returns:
        Dictionary dataset.
        """
        try:
            keywords = self.soup.find("meta", 
                attrs={"name" : "keywords"}).get("content")
        except AttributeError:
            keywords = ""
        
        try:
            description = self.soup.find("meta", 
                attrs={"name" : "description"}).get("content")
        except AttributeError:
            description = ""

        dataset = {
            "filepath" : self.filepath,
            "website URL" : self.__get_base_url(),
            "title" : self.soup.title.string,
            "keywords" : keywords.split(",") if keywords else None,
            "description" : description if description else None,
            "anchors" : self.__parse_anchors()
        }

        return dataset

if __name__ == "__main__":
    p = Parser()
    print(p.create_dataset())
