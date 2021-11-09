import tkinter as tk
import os
from tkinter import filedialog
from typing import Type

from bs4 import BeautifulSoup

class Parser():
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
    
    def parse_anchor(self):
        anchors = []
        for a in self.soup.find_all("a"):
            anchor = a.attrs['href'] if "href" in a.attrs else ''
            anchors.append(anchor)
        return anchors

if __name__ == "__main__":
    p = Parser()
    print(p.parse_anchor())
