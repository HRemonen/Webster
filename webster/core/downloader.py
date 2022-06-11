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
    
    Attributes
    ----------
    response : object
        Response object.
    
    Methods
    -------
    download()
        Downloads site content and saves the content as html file.  
    """
    def __init__(self, response: object) -> None:
        """
        Parameters
        ----------
        response : object
            Response object of the URL to download.   
        """
        
        if not isinstance(response, requests.Response):
            raise TypeError(
                    "Expected response type of requests.Response, instead got: "
                    , type(response))
        else:
            self.response = response
            self.filename = response.url.split("//")[1].replace("/", "") + ".html"   
            self.filepath = os.path.join(DL_DIR, self.filename)
            try:
                os.makedirs(DL_DIR)
            except FileExistsError:
                pass
              
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
        """

        #Try to save the file in DL_DIR folder
        try:       
            if not os.path.isfile(self.filepath):
                with open(self.filepath, 'w') as file:
                    file.write(self.response.url+"\n\n")
                    file.write("File downloaded: ")
                    file.write(NOW.strftime("%d-%m-%Y, %H:%M:%S")+"\n\n")
                    file.write(self.response.text)

            #If the file already exists, raise error
            else: raise FileExistsError
        except FileExistsError:
            print("File exists already...")
        
if __name__ == "__main__":
    response = requests.get("https://www.google.com/")
    
    d = Downloader(response)
    d.download()


    
    