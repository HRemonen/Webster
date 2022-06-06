import os

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
    response : request.Response object
        response object
    filename : str
        filename for the file
    
    Methods
    -------
    download()
        Downloads site content and saves the content as html file.  
    """
    def __init__(self, response: object, filename: str) -> None:
        try:
            os.makedirs(DL_DIR)
        except FileExistsError:
            pass
        
        self._response = response
        self._filename = filename
        self._filepath = os.path.join(DL_DIR, self._filename)
    
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
    pass

    
    