import os
import requests

from datetime import datetime
    
###########################--SETTINGS--###########################

NOW = datetime.now()
DL_DIR = "downloads/html/"

#Create downloads folder with todays date (check from above).
#Folder is then used (Parser module) to store downloaded html and data (JSON) files.

###########################-/SETTINGS/-###########################
class Downloader:
    """
    A class that represents Downloader module used to download 
    webpages and saving webpages in html format.
    
    Methods
    -------
    download()
        Downloads site content and saves the content as html file.  
    """
    def __init__(self) -> None:
        try:
            os.makedirs(DL_DIR)
        except FileExistsError:
            pass
        
        self._response = None
        self._filename = None
        self._filepath = None
        
    def give_response(self, response: requests.Response):
        """
        Give response object to Downloader module.
        Do this before using download() method.
        """
        if not isinstance(response, requests.Response):
            raise TypeError("Response object was not of accepted type")
        self._response = response
        self._filename = response.url.split("//")[1].replace("/", "") + ".html"   
        self._filepath = os.path.join(DL_DIR, self._filename)
              
    def get_downloader_response(self):
        return self._response
    
    def get_filename(self):
        return self._filename
    
    def get_filepath(self):
        return self._filepath
    
    def __str__(self):
        return self._filename
        
    __repr__= __str__
        
    def download(self) -> None:
        """
        Downloads site content and saves the content as html file.
        
        Raises
        ------
        FileExistsError
            If the website already has been downloaded and saved.
        """

        #Try to save the file in DL_DIR folder
        try:       
            if not os.path.isfile(self._filepath):
                with open(self._filepath, 'w') as file:
                    file.write(self._response.url+"\n\n")
                    file.write("File downloaded: ")
                    file.write(NOW.strftime("%d-%m-%Y, %H:%M:%S")+"\n\n")
                    file.write(self._response.text)

            #If the file already exists, raise error
            else: raise FileExistsError
        except FileExistsError:
            print("File exists already...")
        
if __name__ == "__main__":
    response = requests.get("https://www.google.com/")
    
    d = Downloader()
    d.give_response(response)

    
    