import os
import requests

from datetime import datetime

from webster.utils import validators
    
###########################--SETTINGS--###########################

NOW = datetime.now()
DL_DIR = "downloads/html/" + NOW.strftime("%m-%d-%Y")

#Create downloads folder with todays date (check from above).
#Folder is then used (Parser module) to store downloaded html and data (JSON) files.

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
    def __init__(self, site: str) -> None:
        if validators.URLValidator(site):
            self.site = site
            self.filename = self.site.replace("/", "")
        try:
            os.makedirs(DL_DIR)
        except FileExistsError:
            pass
        
        #Check if filename has "." as last char.
        #If the last character was a "." add "html" filetype extension to the filename
        if self.filename[-1] == ".":
            self.filename += "html"
        #Else add ".html" extension to the filename, making it a html file.
        else: self.filename += ".html"
        
        self._filepath = os.path.join(DL_DIR, self.filename)
        self._request = self._get_http_request(self.site)
        
    def _get_http_request(self, site: str) -> object:
        try:
            request = requests.get(site, timeout=0.1)
        except requests.RequestException:
            print("Something went wrong requesting page")
        
        return request    

    def download(self) -> None:
        """
        Downloads site content and saves the content as html file.
        Writes information about the download to the first rows of file.
        Information consists of site URL and date downloaded.
        
        Raises
        ------
        FileExistsError
            If the website already has been downloaded and saved on this date
            raise error and print out error message.
    
        """

        #Try to save the file in DL_DIR folder
        try:       
            if not os.path.isfile(self.filepath):
                with open(self.filepath, 'w') as file:
                    file.write(self.site+"\n\n")
                    file.write("File downloaded: ")
                    file.write(NOW.strftime("%d-%m-%Y, %H:%M:%S")+"\n\n")
                    file.write(r.text)
                    print("File creation succesfull")

            #If the file already exists, raise error
            else: raise FileExistsError

        except FileExistsError:
            print("File " + self.filename + " already exists.")
            

if __name__ == "__main__":
    s="https://webscraper.io/test-sites"

    
    d = Downloader(s)
    d.download()
    