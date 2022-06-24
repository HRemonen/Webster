import os

from datetime import datetime

from net.request import Request

    
###########################--SETTINGS--###########################

NOW = datetime.now()
DL_DIR = "downloads/html/"

#Create downloads folder with todays date (check from above).
#Folder is then used (Parser module) to store downloaded html 
#and data (JSON) files.

###########################-/SETTINGS/-###########################

class Downloader:
    """
    A class that represents Downloader module 
    used to download webpages and saving 
    webpages in html format.
    
    Attributes
    ----------
    request : object
        Request object.
    
    Methods
    -------
    download()
        Downloads site content and saves the content as html file.  
    """
    def __init__(self, request: object) -> None:
        """
        Parameters
        ----------
        response : object
            Response object of the URL to download.   
        """
        
        if not isinstance(request, Request):
            raise TypeError(
                "Expected response type of Request, instead got: "
                , type(request))
        else:
            
            self.request = request
            self.filename = request.url.split(
                "//")[1].replace(
                "/", "") + ".html"   
            self.filepath = os.path.join(
                DL_DIR, self.filename)
            
            try:
                os.makedirs(DL_DIR)
            except FileExistsError:
                pass #Folder already exists not a big deal
              
    def get_request(self):
        return self.request
    
    def get_filename(self):
        return self.filename
    
    def get_filepath(self):
        return self.filepath
    
    def __str__(self):
        return self.filename
        
    __repr__= __str__
        
    def download(self) -> None:
        """
        Downloads site content and saves the content as html file.
        """

        #Try to save the file in DL_DIR folder
        try:       
            if not os.path.isfile(self.filepath):
                with open(self.filepath, 'w') as file:
                    file.write(self.request.url+"\n\n")
                    file.write("File downloaded: ")
                    file.write(NOW.strftime("%d-%m-%Y, %H:%M:%S")+"\n\n")
                    file.write(self.request.text())

            #If the file already exists, raise error
            else: raise FileExistsError
        except FileExistsError:
            print("File exists already...")
        
if __name__ == "__main__":
    url = "https://webscraper.io/test-sites"
    request = Request(url)
    
    d = Downloader(request)
    d.download()


    
    