import requests
import lxml

from time import sleep

from utils import validators
from core.downloader import Downloader

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
    def __init__(self, response: object) -> None:
        """
        Parameters
        ----------
        response : object
            Response object of the URL to parse data out of.   
        """
        
        if not isinstance(response, requests.Response):
            raise TypeError("Response object was not of accepted type")
        else: 
            self.response = response
            self.downloader = Downloader()
            self.downloader.give_response(response)
            self.downloader.download()
            
            sleep(1)
            
            self.filepath = self.downloader.get_filepath()
            self.soup = BeautifulSoup(open(self.filepath, "r"), "html.parser")
        
    def get_base_url(self) -> str:
        """
        Get websites base URL (URL netloc) from the downloaded file.

        Returns
        -------
        string
            Base URL (<scheme>://<netloc>/)
    
        """
        response_url = urlparse(self.response.url)
    
        
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
    response = requests.get("https://github.com/")
    p = Parser(response)
    
    print(p.get_base_url())
    print(p.parse_anchors())

