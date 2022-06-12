import lxml.html
import lxml.etree

from urllib.parse import urljoin

from utils import validators
from net.request import Request


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
            try:
                self.extractor = lxml.html.fromstring(self.request.get())
            except lxml.etree.ParseError:
                pass
        
    def parse_anchors(self) -> list:
        """
        Parses anchors from the file / response object and return anchor list.  
    
        Returns
        -------
        list
            a list of parsed anchors, or subURLs found in the website.
    
        """
        
        urls = [] 
          
        base_url = self.request.base_url()
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
    pass
