import requests
import lxml.html

from utils import validators
from utils import http_response


class Parser:
    """
    A class that represents Parser module used to parse 
    downloaded webpages (html or response objects files). 
    
    Attributes
    ----------
    response : object
        Response object.
    
    Methods
    -------
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
            self.extractor = lxml.html.fromstring(self.response.text)
        
    def parse_anchors(self) -> list:
        """
        Parses anchors from the file / response object and return anchor list.  
    
        Returns
        -------
        list
            a list of parsed anchors, or subURLs found in the website.
    
        """
        
        urls = []    
        base_url = http_response.base_url(self.response)
        extractor_elements = self.extractor.xpath('.//a/@href')
        
        # find every <a> tag from file, with href attribute.
        for anchor in extractor_elements:
            #anchor = a.attrs['href'] if "href" in a.attrs else ''
            #if anchor start with / it means it is relative path or sub domain
            if anchor.startswith("/"):
                if anchor.startswith("//"):
                    url = base_url + anchor[1:]
                else:
                    url = base_url + anchor
                    if url in urls:
                        continue
                    else:
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
    
    response = requests.get("https://stackoverflow.com/")
    p = Parser(response)
    
    print(p.parse_anchors())
