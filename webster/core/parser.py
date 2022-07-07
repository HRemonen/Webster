import lxml.html
import lxml.etree

from urllib.parse import urljoin

from utils import validators
from net.request import Request


class Parser:
    """
    A class that represents Parser module 
    used to parse request objects. 
    
    Attributes
    ----------
    request : object
        Request object.
    
    Methods
    -------
    parse_anchors()
        Parses the downloaded html file for anchors. 
    
    """
    def __init__(self, request: object) -> None:
        """
        Parameters
        ----------
        response : object
            Response object of the URL to parse data out of.   
        """
        
        if not isinstance(request, Request):
            raise TypeError(
                "Expected response type of Request, instead got: "
                , type(request))
        else: 
            
            self.request = request
            self.response = self.request.get()
            if self.response is not None:
                self.extractor = lxml.html.fromstring(self.response)
            
            
        
    def parse_anchors(self) -> list:
        """
        Parses anchors from the file 
        / response object and return anchor list.  
    
        Returns
        -------
        list
            a list of parsed anchors, 
            or subURLs found in the website.
    
        """
        if self.response is None:
            raise TypeError("Response body is missing.")
        
        urls = [] 
          
        base_url = self.request.base_url()
        extractor_elements = self.extractor.xpath('.//a/@href')
        
        # find every <a> tag from file, with href attribute.
        for anchor in extractor_elements:
            url = None
            #if anchor is URL instead of relative path add it to the urls list.
            if validators.URLValidator(anchor):
                url = anchor
                
            elif anchor.startswith("/"):
                url = urljoin(base_url, anchor)
            
            if url is not None and url not in urls:
                urls.append(url)   
                    
        return urls
    
    
    
    def parse_elements(self, elements: list):
        raise NotImplementedError



if __name__ == "__main__":
    url = "https://webscraper.io/test-sites"
    request = Request(url)
    
    p = Parser(request)

    print(p.parse_anchors())
