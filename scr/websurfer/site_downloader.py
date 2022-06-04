import os
import requests

from datetime import datetime
from urllib import parse

    
###########################--SETTINGS--###########################

NOW = datetime.now()
DL_DIR = "downloads/html/" + NOW.strftime("%m-%d-%Y")

# create folder for this date
try:
    os.makedirs(DL_DIR)
except FileExistsError:
    pass

###########################-/SETTINGS/-###########################

class Downloader:
    def __init__(self, site):
        self.site = site
        
    def download_website(self):
        """
        Downloads site content and saves the content as html file.
    
        Parameters:
        None.
    
        Returns:
        None.
    
        """
        self.obj = parse.urlparse(self.site)
        self.filename = "".join([o.replace("/", ".") for o in self.obj])
        
        #Check if filename has "." as last char. This is just for the html filetype declaration.
        if self.filename[-1] == ".":
            self.filename += "html"
        else: self.filename += ".html"

        #filepath, pretty explanatory I guess.. 
        filepath = os.path.join(DL_DIR, self.filename)

        # save the file
        try:
            if not os.path.isfile(filepath):
                # getting the request from url
                r = requests.get(self.site)

                # create new file and write the html content to it
                with open(filepath, 'w') as file:
                    file.write(site+"\n\n")
                    file.write("File downloaded: ")
                    file.write(NOW.strftime("%d-%m-%Y, %H:%M:%S")+"\n\n")
                    file.write(r.text)
                    print("File creation succesfull")

            else: raise FileExistsError

        except FileExistsError:
            msg = "File " + self.filename + " already exists."
            print(msg)


if __name__ == "__main__":
    site="https://webscraper.io/test-sites"

    d = Downloader(site)
    d.download_website()