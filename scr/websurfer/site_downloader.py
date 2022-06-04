import os
import requests

from datetime import datetime
from urllib import parse

    
###########################--SETTINGS--###########################

NOW = datetime.now()
DL_DIR = "downloads/html/" + NOW.strftime("%m-%d-%Y")

#Create downloads folder with todays date (check from above).
#Folder is then used (Parser module) to store downloaded html and data (JSON) files.
try:
    os.makedirs(DL_DIR)
except FileExistsError:
    pass

###########################-/SETTINGS/-###########################

class Downloader:
    """
    A class that represents Downloader module used to download 
    webpages and saving said webpages in html format.
    
    Attributes
    ----------
    site : str
        a string of site URL. URL must be in form of https://example.com/.
        Without the URL scheme Downloader is not able to recognise the URL.
    
    Methods
    -------
    download_website()
        Downloads site content and saves the content as html file.
        Writes information about the download to the first rows of file.
        Information consists of site URL and date downloaded.
    
    """
    def __init__(self, site: str):
        """
        Parameters
        ----------
        site : str
            a string of site URL. URL must be in form of https://example.com/.
            Without the URL scheme Downloader is not able to recognise the URL.
        """
        self.site = site
        
    def download_website(self):
        """
        Downloads site content and saves the content as html file.
        Writes information about the download to the first rows of file.
        Information consists of site URL and date downloaded.
    
        Parameters
        ----------
        None.
        
        Raises
        ------
        FileExistsError
            If the website already has been downloaded and saved on this date
            raise error and print out error message.
    
        Returns
        -------
        None.
    
        """
        
        self.obj = parse.urlparse(self.site)
        self.filename = "".join([o.replace("/", ".") for o in self.obj])
        
        #Check if filename has "." as last char.
        #If the last character was a "." add "html" filetype extension to the filename
        if self.filename[-1] == ".":
            self.filename += "html"
        #Else add ".html" extension to the filename, making it a html file.
        else: self.filename += ".html"

        #Construct filepath from DL_DIR (check first rows of this file)
        #and from the filename we just declared above. 
        filepath = os.path.join(DL_DIR, self.filename)

        #Try to save the file in DL_DIR folder
        try:
            #Check if the file is there, and if not get the URL request for said website
            if not os.path.isfile(filepath):
                # getting the request from url
                r = requests.get(self.site)

                #Create new file and write the website content to the file. 
                #Saves the file if succesfull. Print message to terminal.
                with open(filepath, 'w') as file:
                    file.write(self.site+"\n\n")
                    file.write("File downloaded: ")
                    file.write(NOW.strftime("%d-%m-%Y, %H:%M:%S")+"\n\n")
                    file.write(r.text)
                    print("File creation succesfull")

            #If the file already exists, raise error
            else: raise FileExistsError

        except FileExistsError:
            msg = "File " + self.filename + " already exists."
            print(msg)


if __name__ == "__main__":
    site="https://webscraper.io/test-sites"

    d = Downloader(site)
    d.download_website()