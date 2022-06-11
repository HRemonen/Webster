import requests
import lxml.html

from urllib.parse import urljoin

from utils import validators
from utils import http_response


class Parser:
    """
    A class that represents Parser module used to parse 
    response objects. 
    
    Attributes
    ----------
    response : object
        Response object.
    
    Methods
    -------
    parse_anchors()
        Parses the downloaded html file for anchors. 
    
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
            #if anchor is URL instead of relative path add it to the urls list.
            if validators.URLValidator(anchor):
                url = anchor
            #if anchor start with / it means it is relative path or sub domain

            else:
                url = urljoin(base_url, anchor)
                
            if url in urls:
                    continue
            else:
                urls.append(url)   

        return urls

if __name__ == "__main__":
    
    response = requests.get("https://webscraper.io/test-sites")
    p = Parser(response)
    ps = p.parse_anchors()
    print(ps)
    print(len(ps))
