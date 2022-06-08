import requests

from utils import validators
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class Parser:
    """
    A class that represents Parser module used to parse 
    downloaded webpages (html or response objects files). 
    
    Attributes
    ----------
    filepath : (Optional) str
        Filepath of the file user wants to parse data out of.
        User defines filepath with filedialog.
    
    Methods
    -------
    get_base_url()
        Get websites base URL (URL netloc) from the downloaded file.
        
    parse_anchors()
        Parses the downloaded html file for anchors. 
    
    create_dataset()
        Creates a dataset (dictionary) of html file.
    
    """
    def __init__(self, filepath: str = None, response: object = None) -> None:
        """
        Parameters
        ----------
        filepath : (Optional) str
            Filepath of the file to parse data out of. 
        response : (Optional) object
            Response object of the URL to parse data out of.   
        """
        self.filepath = filepath
        self.response = response
        self.soup = None
        
        if filepath is not None:
            self.filepath = filepath
            self.soup = BeautifulSoup(open(filepath, "r"), "html.parser")
        
        if response is not None:
            if response is not isinstance(response, requests.Response):
                raise TypeError("Response object was not of accepted type")
            else: self.response = response
            
        
    def get_base_url(self) -> str:
        """
        Get websites base URL (URL netloc) from the downloaded file.

        Returns
        -------
        string
            Base URL (<scheme>://<netloc>/)
    
        """
        if self.response is not None:
            response_url = self.response.url
    
        else:
            if self.filepath is not None:
                #read site URL from the file downloaded.
                with open(self.filepath, "r") as f:
                    response_url = urlparse(f.readline().strip())
            else: 
                raise RuntimeError("Nothing to get base URL from! Please provide needed parameters or class attributes.")
        
        #Get the "base URL" for the relative URLs to work correctly
        #Base URL consist of URL scheme and netloc basically, ignore anything else.
        base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=response_url)
        
        return base_url

    def parse_anchors(self) -> list:
        """
        Parses anchors from the file / response object and return anchor list.  
    
        Returns
        -------
        list
            a list of parsed anchors, or subURLs found in the website.
    
        """
        
        urls = []    
        base_url = self.get_base_url()
        
        # find every <a> tag from file, with href attribute.
        for a in self.soup.find_all("a"):
            anchor = a.attrs['href'] if "href" in a.attrs else ''
            #if anchor start with / it means it is relative path or sub domain
            if anchor.startswith("/"):
                #strip the first / from the URL to prevent "//" that would crash program
                """
                anchors.append(anchor[1:])
                """
                
                url = base_url + anchor[1:]
                if url in urls:
                    continue
                urls.append(url)

            #if anchor is URL istead of relative path add it to the urls list.
            elif validators.URLValidator(anchor):
                urls.append(anchor)
        
        return urls

    def create_dataset(self) -> dict:
        """
        Creates a dataset (dictionary) of chosen downloaded html file.
        
        Parameters
        ----------
        None.
        
        Raises
        ------
        None.
    
        Returns
        -------
        dict
            a dictionary that resembles data gathered from the website.
            data consist of:
                Filepath
                Website URL
                Title
                Keywords
                Description
                URLs
    
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
            "website URL" : self.get_base_url(),
            "title" : self.soup.title.string,
            "keywords" : keywords.split(",") if keywords else None,
            "description" : description if description else None,
            "URLs" : self.parse_anchors()
        }

        return dataset

if __name__ == "__main__":
    filepath = "downloads/html/github.comHRemonenPython-Websurfer.html"
    p = Parser(filepath=filepath)
    print(p.get_base_url())
    print(p.parse_anchors())
